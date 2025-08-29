# Riot ID Changer (Unofficial)

⚠️ **Disclaimer**: This script uses Riot's local client API (LCU). It only works if the Riot Client is running and you're logged in. It's unofficial and not supported by Riot. Use responsibly.

## What it does

This Python script connects to the Riot Client's local API to:

- Check if a new Riot ID (gameName#tagLine) is available
- Change your Riot ID directly from the terminal if available

It doesn't spam the API — it only makes a couple of requests when you ask it to:
- One to validate the ID
- One to apply the change if you confirm

## Requirements

- Python 3.8+
- Riot Client running and logged in
- `requests` library installed

### Install dependencies

```bash
pip install requests
```

## Usage

### Make the script executable (Linux / macOS)

```bash
chmod +x riot_id_changer.py
```

### Run the script

**Linux/macOS:**
```bash
./riot_id_changer.py
```

**Windows:**
```bash
python riot_id_changer.py
```

## Example session

```
=== Riot ID Changer ===
New Riot ID: SummonerX
Tagline (optional): 1234
🔍 Checking 'SummonerX#1234'...
✅ Available!
Change to 'SummonerX#1234'? (y/n): y
🔄 Changing...
🎉 Success!
New Riot ID: SummonerX#1234
```
