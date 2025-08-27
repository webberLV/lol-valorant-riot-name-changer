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


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/yourusername/riot-name-changer">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Riot ID Name Changer</h3>

  <p align="center">
    A simple Python tool to change your Riot ID directly through the local Riot client API
    <br />
    <a href="https://github.com/yourusername/riot-name-changer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/yourusername/riot-name-changer/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/yourusername/riot-name-changer/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/yourusername/riot-name-changer)

Riot ID Name Changer is a lightweight Python script that allows you to change your Riot ID without using the web interface. It connects directly to your local Riot client using the official local API, making the process quick and seamless.

**Why use this tool?**
- No need to navigate through web browsers
- Direct integration with your local Riot client
- Cross-platform support (Windows, macOS, Linux)
- Name availability checking before changes
- Simple command-line interface

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![Requests][Requests.org]][Requests-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get started with the Riot ID Name Changer, follow these simple steps.

### Prerequisites

- Python 3.6 or higher
- Riot Client installed and running
- Active Riot Games account

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/yourusername/riot-name-changer.git
   ```
2. Navigate to the project directory
   ```sh
   cd riot-name-changer
   ```
3. Install required dependencies
   ```sh
   pip install requests urllib3
   ```
4. Make sure your Riot Client is running and you're logged in

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. **Start your Riot Client** and make sure you're logged in
2. **Run the script**:
   ```sh
   python riot_name_changer.py
   ```
3. **Follow the prompts**:
   - The tool will automatically detect your current Riot ID
   - Enter your desired new name (the part before #)
   - Enter your desired tagline (the part after #) or leave blank for auto-assignment
   - Confirm the change when prompted

### Example Session
```
=== Riot ID Name Changer ===
Make sure your Riot client is running and you're logged in!

✅ Connected to Riot client
📋 Current Riot ID: OldName#1234

📝 Instructions:
   1. Enter your desired name (the part before #)
   2. Enter your desired tagline (the part after #)
   3. If you leave tagline empty, Riot will auto-assign one

Enter new name: NewAwesomeName
Enter tagline (optional, press Enter for auto-assign): COOL

🔍 Checking availability of 'NewAwesomeName#COOL'...
✅ Name is available!

Proceed with changing your Riot ID to 'NewAwesomeName#COOL'? (y/n): y

🔄 Changing name...
✅ Name changed successfully!
🎉 Your new Riot ID is: NewAwesomeName#COOL
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
## Features

- **🔍 Name Availability Checking**: Validates your desired name before attempting to change
- **🔐 Secure Local API Connection**: Uses the official Riot client local API with proper authentication
- **📱 Cross-Platform Support**: Works on Windows, macOS, and Linux
- **🎯 Current ID Detection**: Automatically displays your current Riot ID
- **⚡ Fast and Lightweight**: Single Python file with minimal dependencies
- **🛡️ Safe and Reliable**: No web scraping or unofficial methods

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Basic name changing functionality
- [x] Name availability validation
- [x] Cross-platform support
- [ ] GUI interface option
- [ ] Batch name checking
- [ ] Name change history tracking
- [ ] Integration with other Riot services

See the [open issues](https://github.com/yourusername/riot-name-changer/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/yourusername/riot-name-changer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yourusername/riot-name-changer" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/yourusername/riot-name-changer](https://github.com/yourusername/riot-name-changer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Riot Games](https://www.riotgames.com/) for providing the local client API
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template) for the README structure
* [Python Requests](https://docs.python-requests.org/) for HTTP functionality

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/yourusername/riot-name-changer.svg?style=for-the-badge
[contributors-url]: https://github.com/yourusername/riot-name-changer/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/yourusername/riot-name-changer.svg?style=for-the-badge
[forks-url]: https://github.com/yourusername/riot-name-changer/network/members
[stars-shield]: https://img.shields.io/github/stars/yourusername/riot-name-changer.svg?style=for-the-badge
[stars-url]: https://github.com/yourusername/riot-name-changer/stargazers
[issues-shield]: https://img.shields.io/github/issues/yourusername/riot-name-changer.svg?style=for-the-badge
[issues-url]: https://github.com/yourusername/riot-name-changer/issues
[license-shield]: https://img.shields.io/github/license/yourusername/riot-name-changer.svg?style=for-the-badge
[license-url]: https://github.com/yourusername/riot-name-changer/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Requests.org]: https://img.shields.io/badge/Requests-FF6B6B?style=for-the-badge&logo=python&logoColor=white
[Requests-url]: https://docs.python-requests.org/
