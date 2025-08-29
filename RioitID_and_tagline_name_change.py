#!/usr/bin/env python3
import requests
import base64
import os
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def find_riot_client():
    paths = [
        os.path.expandvars(r"%LOCALAPPDATA%\Riot Games\Riot Client\Config\lockfile"),
        os.path.expanduser("~/Library/Application Support/Riot Games/Riot Client/Config/lockfile"),
        os.path.expanduser("~/.local/share/Riot Games/Riot Client/Config/lockfile")
    ]
    for path in paths:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    parts = f.read().strip().split(':')
                    if len(parts) >= 4:
                        return {'port': parts[2], 'password': parts[3]}
            except Exception:
                continue
    return None

def riot_request(endpoint, method='GET', data=None):
    client = find_riot_client()
    if not client:
        raise Exception("Riot client not running")
    auth = base64.b64encode(f"riot:{client['password']}".encode()).decode()
    headers = {'Authorization': f'Basic {auth}','Content-Type': 'application/json'}
    url = f"https://127.0.0.1:{client['port']}{endpoint}"
    try:
        if method == 'POST':
            return requests.post(url, headers=headers, json=data, verify=False)
        return requests.get(url, headers=headers, verify=False)
    except Exception as e:
        raise Exception(f"Connection failed: {e}")

def validate_name(name, tag=""):
    try:
        r = riot_request("/player-account/aliases/v2/validity","POST",{"gameName": name, "tagLine": tag})
        result = r.json()
        return result.get("isValid", False), result.get("invalidReason", "Unknown")
    except Exception:
        return False, "Try connecting your Riot client or logging in"

def change_name(name, tag=""):
    try:
        r = riot_request("/player-account/aliases/v1/aliases","POST",{"gameName": name, "tagLine": tag})
        result = r.json()
        if result.get("isSuccess", False):
            return True, "Success!"
        return False, result.get("errorMessage", "Unknown error")
    except Exception:
        return False, "Try connecting your Riot client or logging in"

def main():
    print("=== Riot ID Changer ===\n")

    if not find_riot_client():
        print("❌ Riot client not running")
        input("Press Enter to exit...")
        return

    while True:
        name = input("New Riot ID: ").strip()
        if not name:
            print("❌ Name required")
            continue
        tag = input("Tagline (optional): ").strip()
        new_id = f"{name}#{tag or 'auto'}"

        print(f"🔍 Checking '{new_id}'...")
        valid, reason = validate_name(name, tag)
        if not valid:
            print(f"❌ Not available: {reason}\n")
            continue

        print("✅ Available!")
        if input(f"Change to '{new_id}'? (y/n): ").lower() in ['y', 'yes']:
            print("🔄 Changing...")
            success, msg = change_name(name, tag)
            if success:
                print(f"🎉 {msg}")
                print(f"New Riot ID: {new_id}")
            else:
                print(f"❌ {msg}")
            break
        else:
            print("Cancelled\n")
            break

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
