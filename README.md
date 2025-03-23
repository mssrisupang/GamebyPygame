# Installation Guide for Pygame on Visual Studio Code

Follow this step-by-step guide to set up **Python 3.10+** and **Pygame** properly in **Visual Studio Code (VS Code)** for both Windows and macOS. This version includes verification steps and best practices to avoid common errors.

---

## Step 1: Install Python (Version 3.10 or newer)

### Windows:
1. Go to the [Python Downloads Page](https://www.python.org/downloads/windows/).
2. Download the **latest Python 3 version** (e.g., 3.10 or newer).
3. Run the installer.
4. **Important:** Check the box that says **"Add Python to PATH"** before clicking "Install Now".

### macOS:
1. Go to the [Python Downloads Page](https://www.python.org/downloads/macos/).
2. Download and install the latest Python 3 version.
3. Follow on-screen instructions to finish the installation.

---

## Step 2: Verify Python Installation

After installation, open a terminal:

```bash
python --version
```
or
```bash
python3 --version
```

You should see something like:
```
Python 3.10.12
```
If not, restart your computer or check that Python was added to your PATH.

---

## Step 3: Install Visual Studio Code (VS Code)
1. Download it from [https://code.visualstudio.com](https://code.visualstudio.com).
2. Run the installer and follow instructions.

---

## Step 4: Install the Python Extension in VS Code
1. Open VS Code.
2. Press `Ctrl+Shift+X` (Windows) or `Cmd+Shift+X` (Mac) to open the Extensions tab.
3. Search for `Python` and install the official extension by Microsoft.

---

## Step 5: Select Python Interpreter in VS Code
1. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac).
2. Type:
```
Python: Select Interpreter
```
3. Select the interpreter that points to **Python 3.10 or newer**.

---
## Step 6: Install Pygame 

Use your Python interpreter to install Pygame via `-m pip`:

```bash
python -m pip install pygame
```

Or to upgrade pip first (recommended):
```bash
python -m pip install --upgrade pip
python -m pip install pygame
```

Verify installation:
```bash
python -m pip show pygame
```

This ensures you're installing for the correct Python version (not an old one like 3.7).

---

## Step 7: Test Pygame Installation

Create a new file `test_pygame.py` and paste this code:

```python
import pygame
pygame.init()

window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Test")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
```

Run the script in VS Code. If a window appears titled "Pygame Test," your installation is successful.

---

## ✅ Step 9: Deactivate or Remove the Environment (Optional)

### To deactivate:
Just close the terminal or run:
```bash
deactivate
```
(if using CMD/bash). In PowerShell, simply open a new terminal.

### To delete it completely:
Delete the `pygame_env` folder from your project.

---

🎉 You're now ready to start developing games with **Pygame** in **VS Code** using Python 3.10+!

