# PillPal

**2025 Apprentice Automation Challenge entry**

## About

PillPal is an automated pill dispensing and management system designed to simplify medication routines.  
It provides a convenient way to schedule, track, and dispense pills using a Raspberry Pi-powered hardware controller and a web-based user interface.

## Working Directory

All commands should be made from the root directory (`/PillPal`)

## Maintainence

To update any of the ports for the servers, change the debug mode, or change the server host you'll need to update it in `/ServerManagers/settings.py`

## Prerequisites

There are multiple libraries that are needed for this repository:

- flask
- flask_cors
- gpiozero
- adafruit_motor
- adafruit_pca9685

## File Structure

```
PillPal/
│   threader.py
│   __init__.py
│
├───Data
│   │   config.json
│   │   passcode.txt
│   │
│   └───Tables
│       │   data.json
│       │   failed_schedule.json
│       │   pills.json
│       │   schedule.json
│       │   user_preferences.json
│       │
│       └───Backups
│               failed_schedule_backup.json
│               pills_backup.json
│               schedule_backup.json
│
├───HardwareController
│   │   hardwarecontroller.py
│   │   __init__.py
│   │
│   └───__pycache__
│           hardwarecontroller.cpython-312.pyc
│           __init__.cpython-312.pyc
│
├───Pharmacist
│   │   pharmacist.py
│   │   __init__.py
│   │
│   ├───DataManager
│   │   │   datamanager.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           datamanager.cpython-312.pyc
│   │           datamanager.cpython-313.pyc
│   │           __init__.cpython-312.pyc
│   │           __init__.cpython-313.pyc
│   │
│   └───__pycache__
│           pharmacist.cpython-312.pyc
│           pharmacist.cpython-313.pyc
│           __init__.cpython-312.pyc
│           __init__.cpython-313.pyc
│
├───ServerManagers
│   │   pharmacistmanager.py
│   │   settings.py
│   │   standalonemanager.py
│   │   userinterfacemanager.py
│   │   __init__.py
│   │
│   └───__pycache__
│           pharmacistmanager.cpython-312.pyc
│           pharmacistmanager.cpython-313.pyc
│           settings.cpython-312.pyc
│           settings.cpython-313.pyc
│           standalonemanager.cpython-312.pyc
│           standalonemanager.cpython-313.pyc
│           userinterfacemanager.cpython-312.pyc
│           userinterfacemanager.cpython-313.pyc
│           __init__.cpython-312.pyc
│           __init__.cpython-313.pyc
│
└───UserInterface
    │   app.py
    │   __init__.py
    │
    ├───PassCodeGeneration
    │       generate_passcode_hash.py
    │
    ├───Standalone
    │   │   standaloneapp.py
    │   │
    │   ├───static
    │   │       edit_pill.css
    │   │       edit_pill.js
    │   │       requester.js
    │   │       standalone.css
    │   │       standalone.js
    │   │
    │   ├───templates
    │   │       edit_pill.html
    │   │       standalone.html
    │   │
    │   └───__pycache__
    │           standaloneapp.cpython-312.pyc
    │           standaloneapp.cpython-313.pyc
    │
    ├───static
    │   ├───css
    │   │       standalone.css
    │   │       style_login.css
    │   │       style_main.css
    │   │
    │   └───js
    │           requester.js
    │           script.js
    │           standalone.js
    │
    ├───templates
    │       edit_pill.html
    │       login_page.html
    │       main_page.html
    │       schedule.html
    │       standalone.html
    │
    └───__pycache__
            app.cpython-312.pyc
            app.cpython-313.pyc
            __init__.cpython-312.pyc
            __init__.cpython-313.pyc
```