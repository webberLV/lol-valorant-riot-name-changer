# League of Legends & Valorant Riot ID Changer

Change your Riot ID for League, Valorant, and other Riot games without using the web interface. Just run the script and it handles everything - checks if your name is available and changes it instantly. Works on Windows and Mac.

## Setup

**Windows (pick one):**
```powershell
# Winget (Windows 10/11)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser; winget install Python.Python.3.12; refreshenv; pip install requests urllib3

# Chocolatey  
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')); choco install python -y; refreshenv; pip install requests urllib3

# Scoop
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser; iwr -useb get.scoop.sh | iex; scoop install python; refreshenv; pip install requests urllib3
```

**macOS:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install python3 && pip3 install requests urllib3
```

**Then download** `riot_id_changer.py` and you're ready to go.

## How to Use

1. Start Riot client and log in
2. Open terminal/command prompt in the folder where you downloaded `riot_id_changer.py`
3. Run: `python riot_id_changer.py` or `./riot_id_changer.py` (or double-click it)  
4. It will ask you to type in your new riotid first then it will asak you to change tagline after.
5. Done

## How It Works

Reads your Riot client's connection info and uses the same API the official client uses. No web browser needed.

## Troubleshooting

- **"Riot client not found"** - Make sure Riot client is running and you're logged in
- **"Name not available"** - Try a different name
- **PowerShell execution errors** - Make sure you ran the execution policy command as Administrator

## Notes

- You need a free name change on your account
- Uses official Riot APIs locally  
- MIT License - do whatever
