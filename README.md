# DAP_RP

## About This Project

This is a personal project of Emil Dohne & Vera Großkop. This Digital Audio Player Software will run on our custom Raspberry Pi Audio Player. 
The repository is still a work in process. Below you can find some implemented features and previews:

- Basic UI with different colour schemes.
- Database implementation with SQLAlchemy.
- Personal Usage Data and Statistics.
- Future Feature: Personalized Playlists with AI
- Future Feature: Spotify Accessibility


## Hardware Specs

We are stsill troubleshooting some parts, but so far we are using:
- Raspberry Pi Sero 2 W
- 3,5" Touch Display for Raspberry Pi from BerryBase

## Install instructions

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
