# League of Legends & Valorant Riot ID Changer

Change your Riot ID for League, Valorant, and other Riot games without using the web interface. Just run the script and it handles everything - checks if your name is available and changes it instantly. Works on Windows and Mac.

## Setup

### Windows Setup (pick one method):

**Method 1: Winget (Windows 10/11)**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser; winget install Python.Python.3.12; refreshenv; pip install requests urllib3
```

**Method 2: Chocolatey**
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')); choco install python -y; refreshenv; pip install requests urllib3
```

**Method 3: Scoop**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser; iwr -useb get.scoop.sh | iex; scoop install python; refreshenv; pip install requests urllib3
```

**Then download** `riot_id_changer.py` and you're ready to go.

## How to Use

1. **Start Riot client and log in** (League, Valorant, or Riot Client)
2. **Run the script:**
   ```bash
   python riot_id_changer.py
   ```
   Or double-click it:
   - **Windows:** Right-click → "Open with" → Python
   - **Mac:** Run `chmod +x riot_id_changer.py` first, then double-click

3. **Type your new name and tagline**
4. **Done!**

## Important Notes

- You need a **free name change** available on your account
- Uses **official Riot APIs** locally through your client
- **Safe and secure** - no login credentials needed, works through your existing session
- **MIT License** - free to use and modify

## How It Works

Reads your Riot client's connection info and uses the same API the official client uses. No web browser needed - everything happens locally through your already-authenticated Riot client.

## Troubleshooting

- **"Riot client not found"** - Make sure Riot client is running and you're logged in
- **"Name not available"** - Try a different name/tagline combination
- **PowerShell execution errors** - Make sure you ran the execution policy command as Administrator
- **Python not found** - Restart your terminal/command prompt after installing Python

### Extra/Untested Mac Install:
```bash
# Install Homebrew and Python
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3
pip3 install requests urllib3
```

1. **Start Riot client and log in** (League, Valorant, or Riot Client)
2. **Run the script:**
   ```bash
   python riot_id_changer.py
   ```
   Or double-click it:
   - **Windows:** Right-click → "Open with" → Python
   - **Mac:** Run `chmod +x riot_id_changer.py` first, then double-click

3. **Type your new name and tagline**
4. **Done!**

## Important Notes

- You need a **free name change** available on your account
- Uses **official Riot APIs** locally through your client
- **Safe and secure** - no login credentials needed, works through your existing session
- **MIT License** - free to use and modify

## Requirements

- Riot client running and logged in
- Python 3.6+ installed
- `requests` and `urllib3` Python packages

--- 
