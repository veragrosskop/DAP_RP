# 💿  DAP_RP

## 📀 About This Project


A custom Digital Audio Player application designed for a Raspberry Pi-based audio device.  
The software provides a lightweight, customizable digital music player with database-backed library management and usage tracking.

### Features

- Modern MP3 player UI with customizable color themes
- Music library management using SQLAlchemy
- Playback system with track navigation and controls
- Customizable UI with different color schemes.
- User listening statistics and play history tracking
- Planned: AI-powered playlist generation
- Planned: Spotify integration

<img alt="main_menu.png" src="readme_src/main_menu.png" width="240" title="Main Menu"/> <img alt="play_screen.png" src="readme_src/play_screen.png" width="240" title="Play Screen"/>

## 📀 Feature Implementation overview 

>⚠️ This project is currently in active development. We are currently working on the ones with the  🔧.


📂 Music Library
- [ ] Sync library from PC. 
- 🔧 Complete Database with: 
   * Album, Artist, Album Image, Track, Track Info, Album Info, Genre

🎨 UI
- 🔧 functioning player UI (play, pause, next, previous)
- 🔧 library menu
- 🔧  customization menu

📊 Collect Data
- [ ] track playtimes per song
   - [ ] keep data on sync changes
- [ ] automated playlist ( Top 100 songs of all time, Top 50 songs this month, yearly playlists)

🔩 Hardware
- [ ] Set Keybindings on Raspberry Pie to click wheel input (Ipod Classic Style)
- [ ] Smooth audio transmission to headphones on Raspberry Pi.

---
## 📀 Hardware Specs

We are stsill troubleshooting some parts, but so far we are using:
- Raspberry Pi Sero 2 W
- 3,5" Touch Display for Raspberry Pi from BerryBase

---
## 📀 Install instructions

To set up and install the venv (including dev tools), copy and paste the 
following into your command line that was previously `cd`'d to the root 
of this repository.
```
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .[dev]
```

Once that is done, modify the default interpreter of your IDE to point
to the venv
