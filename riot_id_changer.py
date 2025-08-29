#!/usr/bin/env python3
"""
Single-file Riot ID Name Changer (Refactored)
Connects to local Riot client to change your Riot ID without using the web interface.
"""

import requests
import base64
import os
import json
import urllib3

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def find_riot_client_info():
    """Find Riot client connection info by reading the lockfile."""
    possible_paths = [
        os.path.expandvars(r"%LOCALAPPDATA%\Riot Games\Riot Client\Config\lockfile"),
        os.path.expanduser("~/Library/Application Support/Riot Games/Riot Client/Config/lockfile"),
        os.path.expanduser("~/.local/share/Riot Games/Riot Client/Config/lockfile"),
    ]

    for lockfile_path in possible_paths:
        if os.path.exists(lockfile_path):
            try:
                with open(lockfile_path, 'r') as f:
                    content = f.read().strip()
                    parts = content.split(':')
                    if len(parts) >= 4:
                        return {
                            'port': parts[2],
                            'password': parts[3],
                            'protocol': parts[4] if len(parts) > 4 else 'https'
                        }
            except (OSError, IOError):
                continue
    return None


def make_riot_request(endpoint, method='GET', data=None):
    """Make a request to the local Riot client API"""
    client_info = find_riot_client_info()
    if not client_info:
        raise Exception("Riot client not running or lockfile not found")

    port = client_info['port']
    password = client_info['password']
    auth_string = f"riot:{password}"
    auth_bytes = base64.b64encode(auth_string.encode()).decode()
    headers = {
        'Authorization': f'Basic {auth_bytes}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = f"https://127.0.0.1:{port}{endpoint}"
    try:
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=data, verify=False)
        else:
            response = requests.get(url, headers=headers, verify=False)
        return response
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to connect to Riot client: {e}")


def decode_jwt_payload(token):
    """Safely decode JWT payload from an access_token"""
    try:
        if "." not in token:
            return None
        parts = token.split(".")
        if len(parts) < 2:
            return None
        payload = parts[1]
        payload += "=" * (4 - len(payload) % 4)
        decoded = base64.b64decode(payload).decode('utf-8')
        return json.loads(decoded)
    except (ValueError, json.JSONDecodeError, base64.binascii.Error, UnicodeDecodeError):
        return None  # ⚠ Added UnicodeDecodeError handling


def extract_game_name(result):
    """Helper to extract gameName and tagLine from API result"""
    # Previous version: long inline logic inside get_current_riot_id
    game_name = result.get("gameName") or result.get("game_name") or result.get("displayName")
    tag_line = result.get("tagLine") or result.get("tag_line") or result.get("tag")

    if not game_name:
        for key in ["account", "userInfo", "user", "summoner", "player"]:
            nested = result.get(key)
            if isinstance(nested, dict):
                game_name = nested.get("gameName") or nested.get("game_name") or nested.get("displayName")
                tag_line = nested.get("tagLine") or nested.get("tag_line") or nested.get("tag")
                if game_name:
                    break

    if not game_name and "access_token" in result:
        token_data = decode_jwt_payload(result["access_token"])
        if token_data:
            game_name = token_data.get("gameName") or token_data.get("riot_id", {}).get("game_name")
            tag_line = token_data.get("tagLine") or token_data.get("riot_id", {}).get("tag_line")

    return game_name, tag_line


def get_current_riot_id():
    """Get the current Riot ID - refactored for clarity and caching"""
    session_endpoints = [
        "/rso-auth/v1/authorization/userinfo",
        "/rso-auth/v1/session",
        "/player-account/aliases/v1/current",
        "/lol-summoner/v1/current-summoner",
        "/chat/v1/me"
    ]

    for endpoint in session_endpoints:
        try:
            response = make_riot_request(endpoint)
            if response.status_code == 200:
                result = response.json()
                game_name, tag_line = extract_game_name(result)
                if game_name:
                    return f"{game_name}#{tag_line if tag_line else '[unknown]'}"
        except Exception as e:
            # ⚠ Previous version silently continued, now logs for debugging
            print(f"Debug: failed endpoint {endpoint} - {e}")
            continue
    return None


def validate_name(game_name, tag_line=""):
    data = {"gameName": game_name, "tagLine": tag_line}
    response = make_riot_request("/player-account/aliases/v2/validity", "POST", data)
    result = response.json()
    return result.get("isValid", False), result.get("invalidReason", "Unknown error")


def change_name(game_name, tag_line=""):
    data = {"gameName": game_name, "tagLine": tag_line}
    response = make_riot_request("/player-account/aliases/v1/aliases", "POST", data)
    result = response.json()
    success = result.get("isSuccess", False)
    if success:
        return True, "Name changed successfully!"
    return False, f"{result.get('errorCode', '')} {result.get('errorMessage', 'Unknown error')}"


# ⚠ Refactored main to separate input, validation, and API actions
def prompt_for_name():
    game_name = input("Enter new name: ").strip()
    if not game_name:
        print("❌ Name cannot be empty")
        return None, None

    tag_line = input("Enter tagline (optional): ").strip()
    return game_name, tag_line


def main():
    print("=== Riot ID Name Changer ===")
    print("Make sure your Riot client is running and you're logged in!\n")

    client_info = find_riot_client_info()
    if not client_info:
        print("❌ Riot client not found or not running")
        input("Press Enter to exit...")
        return

    print("✅ Connected to Riot client")

    current_id = get_current_riot_id()
    if current_id:
        print(f"📋 Current Riot ID: {current_id}")
    else:
        print("⚠️ Could not retrieve current Riot ID (but name change will still work)")

    print("\n📝 Instructions:")
    print("1. Enter your desired Riot ID (before #)")
    print("2. Enter your tagline 4 digits after hashtag (after #)")

    game_name, tag_line = prompt_for_name()
    if not game_name:
        input("Press Enter to exit...")
        return

    new_riot_id = f"{game_name}#{tag_line if tag_line else '[auto]'}"

    print(f"\n🔍 Checking availability of '{new_riot_id}'...")
    is_valid, reason = validate_name(game_name, tag_line)

    if not is_valid:
        print(f"❌ Name not available: {reason}")
        input("Press Enter to exit...")
        return

    print("✅ Name is available!")
    confirm = input(f"Change Riot ID to '{new_riot_id}'? (y/n): ").lower()

    if confirm not in ['y', 'yes']:
        print("Operation cancelled.")
        input("Press Enter to exit...")
        return

    print("\n🔄 Changing name...")
    success, message = change_name(game_name, tag_line)

    if success:
        print(f"✅ {message}")
        print(f"🎉 Your new Riot ID is: {new_riot_id}")
    else:
        print(f"❌ Failed to change name: {message}")

    print()
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
