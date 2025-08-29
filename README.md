Here’s the revised README with a concise troubleshooting section added:

---

# Riot ID Name Changer (LoL & Valorant)

Uses Riot's Local Client API (LCU). Works only if the Riot Client is running and logged in.
It makes just two requests per change: validate ID → apply change.

## Requirements

* Python 3.8+
* Riot Client running
* `requests` library (`pip install requests`)

## Usage

```bash
# Windows
python riot_id_changer.py
# Mac
chmod +x riot_id_changer.py
./riot_id_changer.py
```

Or run the Windows executable.

Follow instructions:
[Example Screenshot](https://raw.githubusercontent.com/webberLV/lol-valorant-riot-name-changer/main/img/Example.png)

## Troubleshooting

1. After installing Python, **restart your shell** to ensure changes take effect.
2. If Python or `requests` isn’t recognized, check the installation path or run with the **full path**, e.g.:

```bash
C:\Users\YourName\AppData\Local\Programs\Python\Python310\python.exe riot_id_changer.py
```

3. Make sure the Riot Client is running and logged in before using the script.

---

Use responsibly. Don’t spam the LCU with thousands of requests.
Not affiliated with Riot Games.

---

I can also make this **even shorter with troubleshooting baked directly into the Usage section** for ultra-simplicity. Do you want me to do that?
