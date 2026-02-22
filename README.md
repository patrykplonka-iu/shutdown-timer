# CWK – Shutdown Timer

CWK (Czasowy Wyłącznik Komputera) is a small desktop application written in Python using Tkinter.  
It allows the user to schedule and cancel a system shutdown through a simple graphical interface.

## Features

- Schedule system shutdown (in minutes)
- Confirmation dialog before execution
- Cancel scheduled shutdown
- Internal shutdown status tracking
- Clean separation between GUI and logic

## Project Structure

- `engine.py` – system logic (shutdown, cancel, status)
- `main.py` / `gui.py` – graphical user interface

## Requirements

- Python 3.x  
- No external runtime dependencies (Tkinter is part of the standard library)

## Run from Source

python main.py


## Build Standalone Executable (Windows)


python -m pyinstaller --onefile --windowed --add-data "icon.ico;." main.py


The executable will be generated in:


dist/main.exe


## Purpose

This project demonstrates:
- Basic desktop GUI development with Tkinter
- Separation of concerns (UI vs logic)
- Interaction with the operating system
- Packaging a Python application into a standalone executable