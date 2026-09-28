# Week 0: Complete Guided Project Setup Guide

**Congrats on being selected to work on an MSU AI Club Guided Project!** This week you will set up everything for your project and go over a few basics.

Don't worry if you're new to coding. This week is a comprehensive tutorial for setting up your development environment with VSCode, Python, Git, and GitHub.

This guide follows a hands-on learning path: first you'll learn essential command line basics, then set up your tools, write some Python code, learn about virtual environments and package management, and finally dive into version control with Git and GitHub.

Next week, you'll begin working on the weather forecasting project and start learning more advanced topics like data processing, model training, and evaluation.

By the way, if you are already familiar with the skills covered this week, feel free to skip this week's instructions.

---

## Table of Contents

1. [Command Line Basics](#command-line-basics)
2. [Installing VSCode](#installing-vscode)
3. [Installing Python](#installing-python)
4. [Writing Your First Python Script](#writing-your-first-python-script)
5. [Python Virtual Environments](#python-virtual-environments)
6. [Using pip](#using-pip)
7. [Installing Git](#installing-git)
8. [Understanding .gitignore](#understanding-gitignore)
9. [Creating a GitHub Account](#creating-a-github-account)
10. [Creating a Repository](#creating-a-repository)
11. [Git Basics: Commit, Push, Pull](#git-basics-commit-push-pull)
12. [Review](#review)

---

## Command Line Basics

Before installing any tools, let's learn to navigate your computer using the command line (also called terminal, shell, or console). This is essential for modern development!

### Why Learn the Command Line?

- **Essential skill**: Most development tools use command line interfaces
- **More powerful**: Do things faster than clicking through folders
- **Universal**: Works on any computer, even remote servers
- **Professional**: Expected skill for data science and software development

### Opening Your Terminal

**Windows:**

- **Command Prompt (CMD)**: Press `Win + R`, type `cmd`, press Enter
- **PowerShell** (recommended): Press `Win + X`, select "Windows PowerShell" or "Terminal"
- **Git Bash**: After installing Git, you can use Git Bash for Unix-like commands

**macOS:**

- Press `Cmd + Space`, type "Terminal", press Enter
- Or: Applications → Utilities → Terminal

**Linux:**

- Press `Ctrl + Alt + T`
- Or search for "Terminal" in your applications

---

## Windows Command Line Basics

_Note: These commands work in Command Prompt (CMD) and PowerShell. We'll note when commands differ._

### Navigation Commands

**Print current directory (where you are):**

```cmd
cd
```

Output: `C:\Users\YourName`

**List files and folders:**

```cmd
dir
```

**See hidden files too:**

```cmd
dir /a
```

**Change directory to your home folder (if you're at 'Users'):**

```cmd
cd <YourName>
```

Usually: `C:\Users\YourName`

**Go to a specific folder:**

```cmd
cd Documents
cd Desktop
cd Downloads
```

**Go up one level:**

```cmd
cd ..
```

**Go to the root of C: drive:**

```cmd
cd \
```

### Creating Your First Project Folder

Let's create a project folder in your home directory:

**Go to your home directory:**

Usually: `C:\Users\YourName`

**Create a new folder called "dev":**

```cmd
mkdir dev
```

(dev is short for "development" - a common place to store projects)

**Go into the dev folder:**

```cmd
cd dev
```

**Create your first project folder:**

```cmd
mkdir my-project-name
```

**Navigate into it:**

```cmd
cd my-project-name
```

**Confirm where you are:**

```cmd
cd
```

Should show: `C:\Users\YourName\dev\my-project-name`

### Windows Command Prompt Quick Reference

**Essential Commands:**

```cmd
cd                    Show current directory
cd folder-name        Go to folder
cd ..                 Go up one level
cd \                  Go to root
dir                   List files
mkdir folder-name     Create folder
exit                  Close terminal
```

**Additional Commands (good to know):**

```cmd
cd                    Show current directory
cd folder-name        Go to folder
cd ..                 Go up one level
cd \                  Go to root
dir                   List files
dir /a                List all files (including hidden)
mkdir folder-name     Create folder
rmdir folder-name     Delete empty folder
type file.txt         Show file contents
copy file1 file2      Copy file
move file1 file2      Move/rename file
del file.txt          Delete file
cls                   Clear screen
exit                  Close terminal
```

---

## Unix Command Line Basics (macOS/Linux)

_These commands work in Terminal on macOS and Linux. They also work in Git Bash on Windows!_

### Navigation Commands

**Print current directory (where you are):**

```bash
pwd
```

Output: `/Users/yourname` (macOS) or `/home/yourname` (Linux)

**List files and folders:**

```bash
ls
```

**More detailed list:**

```bash
ls -l
```

**Show hidden files too:**

```bash
ls -a
```

**Combine options:**

```bash
ls -la
```

**Change directory to your home folder:**

```bash
cd ~
```

Or just:

```bash
cd
```

**Go to a specific folder:**

```bash
cd Documents
cd Desktop
cd Downloads
```

**Go up one level:**

```bash
cd ..
```

**Go to root directory:**

```bash
cd /
```

**Go to previous directory:**

```bash
cd -
```

### Creating Your First Project Folder

Let's create a project folder in your home directory:

**Go to your home directory:**

```bash
cd ~
```

**Create a new folder called "dev":**

```bash
mkdir dev
```

(dev is short for "development" - a common place to store projects)

**Go into the dev folder:**

```bash
cd dev
```

**Create your first project folder:**

```bash
mkdir my-project-name
```

**Navigate into it:**

```bash
cd my-project-name
```

**Confirm where you are:**

```bash
pwd
```

Should show: `/Users/yourname/dev/my-project-name` (macOS) or `/home/yourname/dev/my-project-name` (Linux)

### Unix Command Quick Reference

**Essential Commands:**

```bash
pwd                   Show current directory
cd folder-name        Go to folder
cd ..                 Go up one level
cd ~                  Go to home directory
ls                    List files
mkdir folder-name     Create folder
exit                  Close terminal
```

**Additional Commands (good to know):**

```bash
pwd                   Show current directory
cd folder-name        Go to folder
cd ..                 Go up one level
cd ~                  Go to home directory
cd /                  Go to root
cd -                  Go to previous directory
ls                    List files
ls -la                List all files with details
mkdir folder-name     Create folder
mkdir -p a/b/c        Create nested folders
rm file.txt           Delete file
rm -r folder-name     Delete folder and contents
cp file1 file2        Copy file
mv file1 file2        Move/rename file
cat file.txt          Show file contents
clear                 Clear screen (or Ctrl+L)
exit                  Close terminal
```

---

## Essential Keyboard Shortcuts (Both Windows and Unix)

```
Ctrl + C              # Cancel current command / Stop running program
Ctrl + D              # Exit terminal (or end input)
Ctrl + L              # Clear screen
Ctrl + A              # Go to beginning of line
Ctrl + E              # Go to end of line
Ctrl + U              # Delete from cursor to beginning
Ctrl + K              # Delete from cursor to end
Ctrl + R              # Search command history (Unix)
Tab                   # Auto-complete file/folder names
↑ / ↓                 # Navigate command history
```

---

## Practice Exercise: Navigate Your File System

Now that you've learned the commands, let's practice navigating to the project folder you'll use later in this tutorial. If you already created these folders while learning above, you can skip creating them again. If you are comfortable with the CLI at this point, you can skip to the next section.

**For Windows users (Command Prompt):**

**1. Go to your home directory:**

```cmd
cd %USERPROFILE%
```

**2. See where you are:**

```cmd
cd
```

**3. List what's in this folder:**

```cmd
dir
```

**4. Navigate to (or create) your dev folder:**

```cmd
cd dev
```

If it doesn't exist yet:

```cmd
mkdir dev
cd dev
```

**5. Navigate to (or create) your first project:**

```cmd
cd my-project-name
```

If it doesn't exist yet:

```cmd
mkdir my-project-name
cd my-project-name
```

**6. Confirm you're in the right place:**

```cmd
cd
```

Should show: `C:\Users\YourName\dev\my-project-name`

**7. Go back to home:**

```cmd
cd %USERPROFILE%
```

**Success! You've navigated the command line!**

**For macOS/Linux users (Terminal):**

**1. Go to your home directory:**

```bash
cd ~
```

**2. See where you are:**

```bash
pwd
```

**3. List what's in this folder:**

```bash
ls
```

**4. Navigate to (or create) your dev folder:**

```bash
cd dev
```

If it doesn't exist yet:

```bash
mkdir dev
cd dev
```

**5. Navigate to (or create) your first project:**

```bash
cd my-project-name
```

If it doesn't exist yet:

```bash
mkdir my-project-name
cd my-project-name
```

**6. Confirm you're in the right place:**

```bash
pwd
```

Should show: `/Users/yourname/dev/my-project-name`

**7. Go back to home:**

```bash
cd ~
```

**Success! You've navigated the command line!**

---

## Installing VSCode

Visual Studio Code is a powerful, free code editor with excellent support for Python, Git, and many other languages.

### Windows

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click the "Download for Windows" button
3. Run the downloaded installer (`VSCodeUserSetup-{version}.exe`)
4. Follow the installation wizard:
   - Accept the license agreement
   - Choose installation location
   - **Important**: Check "Add to PATH" option
   - Check "Create a desktop icon" if desired
5. Click "Install" and then "Finish"

### macOS

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click "Download for Mac"
3. Open the downloaded `.zip` file
4. Drag `Visual Studio Code.app` to the Applications folder
5. Launch VSCode from Applications

To add VSCode to your PATH for command line use:

- Open VSCode
- Press `Cmd+Shift+P` to open Command Palette
- Type "shell command" and select "Shell Command: Install 'code' command in PATH"

### Linux (Ubuntu/Debian)

```bash
# Update package index
sudo apt update

# Install dependencies
sudo apt install software-properties-common apt-transport-https wget

# Import Microsoft GPG key
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -

# Add VSCode repository
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

# Install VSCode
sudo apt update
sudo apt install code
```

### Verification

Open a terminal/command prompt and type:

```bash
code --version
```

---

## Installing Python

### Windows

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python 3.x version (e.g., Python 3.11 or 3.12)
3. Run the installer
4. **CRITICAL**: Check "Add Python to PATH" at the bottom of the installer
5. Click "Install Now" for default installation
6. Wait for installation to complete

### macOS

**Option 1: Official Installer**

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the macOS installer
3. Run the `.pkg` file and follow the installation wizard

**Option 2: Homebrew (Recommended)**

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python
```

### Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip python3-venv

# Install additional useful packages
sudo apt install python3-dev build-essential
```

### Verification

Open a terminal/command prompt and type:

```bash
python --version
# or on some systems
python3 --version
```

You should see something like `Python 3.11.x` or similar.

---

## Writing Your First Python Script

Now that Python is installed, let's write a simple script to make sure everything works! We'll use the project folder you created earlier.

### Step 1: Navigate to Your Project Folder

Open your terminal and go to the project folder you created in the CLI tutorial:

**Windows:**

```cmd
cd %USERPROFILE%\dev\my-project-name
```

**macOS/Linux:**

```bash
cd ~/dev/my-project-name
```

### Step 2: Open VSCode

```bash
# Open the current folder in VSCode
code .

# If this doesn't work, open VSCode manually and:
# File → Open Folder → Navigate to your home directory → dev → my-project-name
```

### Step 3: Create a Python File

In VSCode:

1. Click "New File" or press `Ctrl+N` (Windows/Linux) or `Cmd+N` (Mac)
2. Save it as `hello.py` (File → Save As)
3. Type the following code. Avoid copy/pasting if you can, so you can learn some of the syntax:

```python
# hello.py
def greet(name):
    return f"Hello, {name}! Welcome to AI Club!"

def main():
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)

    # Do a simple calculation
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

if __name__ == "__main__":
    main()
```

### Step 4: Run Your Script

In VSCode's integrated terminal (View → Terminal, or press `` Ctrl+` ``):

```bash
python hello.py
# or on some systems
python3 hello.py
```

You should see prompts asking for your name and numbers. Congratulations! You've written and run your first Python script!

### Understanding What You Just Did

- **Created a project folder**: Organizing your code in folders is crucial
- **Wrote a Python function**: `greet()` is a reusable function
- **Got user input**: `input()` lets programs interact with users
- **Used f-strings**: `f"Hello, {name}!"` is a modern way to format strings
- **Used the main guard**: `if __name__ == "__main__":` ensures code runs only when directly executed

Now you're ready to learn about virtual environments and packages!

---

## Python Virtual Environments

Now that you've written your first script, let's learn about virtual environments. As you start using external packages (like `numpy` or `pandas`), you'll want to keep each project's dependencies separate.

### Why Use Virtual Environments?

- **Isolation**: Each project has its own dependencies
- **Reproducibility**: Easy to share exact package versions with teammates
- **Clean system**: Avoid cluttering your global Python installation
- **Version management**: Different projects can use different package versions

Think of it like this: you wouldn't want your Game of Thrones analysis project's packages interfering with your Iverson Betting platform's packages!

### Creating a Virtual Environment in VSCode

**First, make sure your project is open in VSCode:**

**Windows:**

```cmd
cd %USERPROFILE%\dev\my-project-name
code .
```

**macOS/Linux:**

```bash
cd ~/dev/my-project-name
code .
```

#### Method 1: Using VSCode Command Palette (Recommended)

This is the easiest way to create and manage virtual environments in VSCode!

**1. Open Command Palette:**

- Windows/Linux: Press `Ctrl + Shift + P`
- macOS: Press `Cmd + Shift + P`

**2. Type "Python: Create Environment"**

**3. Select "Venv"**

**4. Choose your Python interpreter** (usually the latest version)

**5. Wait for VSCode to create the environment**

- VSCode will create a `.venv` folder in your project (note the dot at the start!)
- It will automatically activate the environment in the terminal
- You'll see `(.venv)` appear in your terminal prompt

**That's it!** VSCode has created your virtual environment and activated it. You can skip to the "What Just Happened?" section below.

#### Method 2: Using the Terminal (Alternative)

If you prefer using the terminal directly, or the command palette method isn't working:

**Make sure you're in your project folder and VSCode is open.**

Open VSCode's integrated terminal (View → Terminal, or press `` Ctrl + ` ``):

**Windows:**

Create virtual environment named '.venv':

```cmd
python -m venv .venv
```

Activate the virtual environment:

```cmd
..venv\Scripts\activate
```

Your prompt should now show `(.venv)` at the beginning

**macOS/Linux:**

Create virtual environment named '.venv':

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Your prompt should now show `(.venv)` at the beginning

### What Just Happened?

When you created the .venv, you created an isolated Python environment. Notice the `(.venv)` prefix in your terminal - this means any packages you install will only affect this project!

**In VSCode, look at the bottom-right corner** - you should see something like:

- `Python 3.11.x ('.venv': venv)`

This confirms VSCode is using your virtual environment!

You can verify in the terminal:

**Windows:**

```cmd
where python
```

Should point to `...\dev\my-project-name\.venv\Scripts\python.exe`

**macOS/Linux:**

```bash
which python
```

Should point to `.../dev/my-project-name/.venv/bin/python`

### Selecting Your Virtual Environment in VSCode

If VSCode doesn't automatically detect your .venv:

**1. Click the Python version in the bottom-right corner**

- Or open Command Palette (`Ctrl/Cmd + Shift + P`) and type "Python: Select Interpreter"

**2. Choose the interpreter from your .venv folder**

- It will show as `./.venv/bin/python` or similar
- It may say `('.venv': venv)` next to it

**3. VSCode will now use this virtual environment automatically**

- New terminals will auto-activate the .venv
- Python scripts will run using the .venv's packages

### Working with Virtual Environments

**Every time you open VSCode to work on this project:**

1. Open the project folder in VSCode: `code ~/dev/my-project-name`
2. VSCode should automatically activate the .venv in new terminals
3. You should see `(.venv)` in your terminal prompt
4. If you don't see `(.venv)`, manually activate:

**Windows:**

```cmd
..venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**When you're done working:**

Deactivate the .venv:

```bash
deactivate
```

Your `(.venv)` prefix will disappear

### Important: Daily Workflow

Get used to this workflow:

1. Open VSCode to your project: `code ~/dev/my-project-name`
2. Check for `(.venv)` in terminal - VSCode usually activates it automatically
3. If no `(.venv)`, activate it manually
4. Work on your project
5. When switching projects, close VSCode or deactivate: `deactivate`

**Pro tip:** Once you've selected the Python interpreter in VSCode (Method 1 above), new terminals will automatically activate your .venv. You rarely need to manually activate!

---

## Using pip

Now that you have a virtual environment set up, let's install some packages! pip is Python's package installer.

### Your First Package Installation

Let's enhance your `hello.py` script with a package for numerical computing.

**Make sure your virtual environment is activated first!** You should see `(venv)` in your terminal.

Install the numpy package (may take a few seconds):

```bash
pip install numpy
```

### Update Your Script

Open `hello.py` and modify it to use numpy. Once again, avoid copy/paste:

```python
# hello.py
import numpy as np

def greet(name):
    return f"Hello, {name}! Welcome to Python with NumPy!"

def demonstrate_numpy():
    """Show basic numpy functionality"""
    # Create an array
    numbers = np.array([1, 2, 3, 4, 5])

    print(f"\nArray: {numbers}")
    print(f"Mean: {numbers.mean()}")
    print(f"Sum: {numbers.sum()}")
    print(f"Standard Deviation: {numbers.std():.2f}")

    # Create a 2D array
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\nMatrix:\n{matrix}")
    print(f"Matrix shape: {matrix.shape}")

def main():
    print("=== Python with NumPy ===")
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)

    demonstrate_numpy()

    # Do a simple calculation
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

if __name__ == "__main__":
    main()
```

Run it again:

```bash
python hello.py
```

Now your script uses numpy for numerical operations!

### Essential pip Commands

```bash
# Install a package
pip install package-name

# Install specific version
pip install pandas==2.0.0

# Install multiple packages at once
pip install numpy pandas matplotlib

# Upgrade a package
pip install --upgrade numpy

# Uninstall a package
pip uninstall numpy

# List all installed packages in your venv
pip list

# Show details about a package
pip show numpy
```

### Requirements Files: Sharing Your Dependencies

This is crucial for team projects! A `requirements.txt` file lists all packages your project needs.

**Create requirements.txt:**

```bash
# Save all currently installed packages
pip freeze > requirements.txt
```

**View the file:**

**Windows:**

```cmd
type requirements.txt
```

**macOS/Linux:**

```bash
cat requirements.txt
```

You should see something like:

```
numpy==1.26.3
```

**Why is this important?** When someone else (or you on another computer) wants to run your project, they can install all dependencies at once:

**Create a new venv:**

**Windows:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install all packages from requirements.txt:**

```bash
pip install -r requirements.txt
```

### Upgrading pip Itself

```bash
# Upgrade pip to the latest version
python -m pip install --upgrade pip
```

---

## Installing Git

Now that you've created a project with code and dependencies, it's time to learn version control! Git lets you track changes to your code and collaborate with others. It's like a "save point" system for your entire project.

### Windows

**Option 1: Official Installer**

1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the installer (64-bit recommended)
3. Run the installer with these recommended settings:
   - Default editor: Choose your preference (VSCode is a good option)
   - PATH environment: "Git from the command line and also from 3rd-party software"
   - Line ending conversions: "Checkout Windows-style, commit Unix-style"
   - Terminal emulator: "Use Windows' default console window" or "Use MinTTY"
4. Complete the installation

**Option 2: Git for Windows via winget**

```bash
winget install --id Git.Git -e --source winget
```

### macOS

**Option 1: Homebrew (Recommended)**

```bash
brew install git
```

**Option 2: Xcode Command Line Tools**

```bash
xcode-select --install
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```

### Verification and Configuration

Verify installation:

```bash
git --version
```

Configure Git with your identity:

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use the same email as your GitHub account)
git config --global user.email "your.email@example.com"

# Optional: Set default branch name to 'main'
git config --global init.defaultBranch main

# Verify configuration
git config --list
```

---

## Understanding .gitignore

**CRITICAL**: Before you start using Git, you need to understand `.gitignore` - it tells Git which files to ignore.

### Why .gitignore Matters

Remember that `venv` folder you created? It contains thousands of files from Python packages. **You should NEVER push your venv to GitHub!** Here's why:

1. **It's huge**: Virtual environments can be hundreds of MBs or even GBs
2. **It's platform-specific**: Your venv from Windows won't work on macOS/Linux
3. **It's redundant**: Anyone can recreate it using `requirements.txt`
4. **It clutters your repository**: Makes it slow and messy

### Create Your .gitignore File

In your project folder (`my-project-name`), create a file called `.gitignore`:

**In VSCode:**

1. Create new file
2. Save as `.gitignore` (notice the dot at the start!)

**Or in terminal:**

```bash
# macOS/Linux
touch .gitignore

# Windows (PowerShell)
New-Item .gitignore

# Windows (Command Prompt)
type nul > .gitignore
```

### Essential .gitignore for Python Projects

Add this content to your `.gitignore`:

```gitignore
# Virtual Environment
venv/
.venv/
env/
ENV/
env.bak/
venv.bak/

# Python compiled files
__pycache__/
*.py[cod]
*$py.class
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyCharm
.idea/

# VSCode
.vscode/
*.code-workspace

# Jupyter Notebook
.ipynb_checkpoints

# Environment variables
.env

# OS files
.DS_Store
Thumbs.db

# Data files (optional - uncomment if you have large data files)
# *.csv
# *.xlsx
# data/
```

### How .gitignore Works

When you have a `.gitignore` file, Git will:

- ✅ Track: `hello.py`, `requirements.txt`, `.gitignore`
- ❌ Ignore: `.venv/` folder and everything in it (or `venv/` if you used that name)
- ❌ Ignore: `__pycache__/` and other Python cache files

### Test Your .gitignore

```bash
# Initialize git in your project (if not already done)
git init

# Check what files Git sees
git status
```

You should see:

```
Untracked files:
  .gitignore
  hello.py
  requirements.txt
```

**You should NOT see `.venv/` or `venv/` in the list!** If you do, make sure:

1. Your `.gitignore` file is in the project root folder
2. It's actually named `.gitignore` (not `.gitignore.txt`)
3. The `venv/` and `.venv/` lines are in the file

---

## Creating a GitHub Account

1. Go to [https://github.com](https://github.com)
2. Click "Sign up" in the top right
3. Enter your email address and click "Continue"
4. Create a strong password
5. Choose a username (this will be your GitHub handle)
6. Complete the email verification
7. Answer the setup questions (optional)
8. Complete the CAPTCHA verification
9. Verify your email address by clicking the link sent to your inbox

### Setting up SSH (Recommended for easier authentication)

**Generate SSH key:**

```bash
# Generate a new SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter to accept default file location
# Enter a passphrase (optional but recommended)
```

**Add SSH key to ssh-agent:**

On macOS/Linux:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

On Windows (Git Bash):

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Add SSH key to GitHub:**

1. Copy your public key:

   ```bash
   # macOS
   cat ~/.ssh/id_ed25519.pub | pbcopy

   # Linux
   cat ~/.ssh/id_ed25519.pub

   # Windows (Git Bash)
   cat ~/.ssh/id_ed25519.pub | clip
   ```

2. Go to GitHub → Settings → SSH and GPG keys
3. Click "New SSH key"
4. Give it a title (e.g., "My Laptop")
5. Paste the key and click "Add SSH key"

**Test connection:**

```bash
ssh -T git@github.com
```

---

## Creating a Repository

Now let's put your `my-project-name` (with `hello.py`, `.venv`, `requirements.txt`, and `.gitignore`) on GitHub!

### Step 1: Initialize Git in Your Project

**Navigate to your project (if not already there):**

**Windows:**

```cmd
cd %USERPROFILE%\dev\my-project-name
```

**macOS/Linux:**

```bash
cd ~/dev/my-project-name
```

**Initialize Git:**

```bash
git init
```

This creates a hidden `.git` folder that tracks all changes.

**Check what Git sees:**

```bash
git status
```

You should see:

```
Untracked files:
  .gitignore
  hello.py
  requirements.txt
```

Notice `.venv/` is NOT listed - that's because your `.gitignore` is working!

### Step 2: Make Your First Commit

**Add all files to staging:**

```bash
git add .
```

**Commit with a message:**

```bash
git commit -m "Initial commit: Python project with numpy"
```

**Verify your commit:**

```bash
git log --oneline
```

You should see your commit!

### Step 3: Create Repository on GitHub

1. Go to [https://github.com](https://github.com)
2. Click the "+" icon in the top right → "New repository"
3. Fill in repository details:
   - **Repository name**: `my-project-name` (use the same name!)
   - **Description**: "My first Python project with VSCode, venv, and Git"
   - **Public/Private**: Your choice
   - **DO NOT check** "Initialize with README" (you already have files!)
   - **DO NOT add** .gitignore (you already have one!)
4. Click "Create repository"

### Step 4: Connect Your Local Repository to GitHub

GitHub will show you commands. Use these:

**Add remote origin:**

```bash
git remote add origin https://github.com/yourusername/my-project-name.git
```

Replace `yourusername` with your actual GitHub username!

**Push your code to GitHub:**

```bash
git push -u origin main
```

If this fails with an error about "master" vs "main", try:

```bash
git branch -M main
git push -u origin main
```

**Success!** Your project is now on GitHub. Visit `https://github.com/yourusername/my-project-name` to see it!

---

## Git Basics: Commit, Push, Pull

### Understanding the Git Workflow

Git has three main areas:

1. **Working Directory**: Your actual files (like `hello.py`)
2. **Staging Area**: Files ready to be committed (after `git add`)
3. **Repository**: Committed snapshots of your project (after `git commit`)

### Making Changes and Committing

Let's modify your `hello.py` file and commit the changes:

**Open hello.py in VSCode and add a new function:**

```python
# Add this at the end of hello.py
def farewell(name):
    """Say goodbye"""
    return f"Goodbye, {name}! Keep coding!"

# Update main to use it
def main():
    print("=== Python with NumPy ===")
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)

    demonstrate_numpy()

    # Do a simple calculation
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

    # New farewell message
    print(f"\n{farewell(user_name)}")
```

**Check what changed:**

```bash
git status
```

You'll see: `modified:   hello.py`

**See the actual changes:**

```bash
git diff
```

This shows exactly what lines changed (green for additions, red for deletions).

**Stage the changes:**

```bash
git add hello.py
```

Or add all changed files:

```bash
git add .
```

**Commit with a descriptive message:**

```bash
git commit -m "Add farewell function to hello.py"
```

**View your commit history:**

```bash
git log --oneline
```

You should now see two commits!

### Pushing Changes to GitHub

Now push your new changes to GitHub:

```bash
git push
```

Since you already set up the remote with `git push -u origin main` earlier, you can now just use `git push`!

**Visit your GitHub repository** to see the updated code: `https://github.com/yourusername/my-project-name`

You'll see your latest commit message and the updated `hello.py` file!

### Pulling Changes from GitHub

You may need to pull in changes if you pushed code from another device or have a teammate that pushed code.

```bash
# Fetch and merge changes from GitHub
git pull

# This is equivalent to:
git fetch    # Download changes
git merge    # Merge them into your current branch
```

### Common Workflow Example

Here's what a typical day looks like when working on your project:

```bash
# 1. Navigate to your project
cd ~/dev/my-project-name

# 2. Activate your virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# 3. Pull latest changes (important if working on multiple computers)
git pull

# 4. Make changes to files
# ... edit hello.py in VSCode ...

# 5. Check what changed
git status
git diff

# 6. Stage and commit changes
git add .
git commit -m "Improve numpy demonstration"

# 7. Push to GitHub
git push

# 8. Repeat!
```

### Useful Git Commands

```bash
# View commit history
git log
git log --graph --oneline --all  # Visual representation

# See changes in files
git diff                    # Changes not yet staged
git diff --staged          # Changes staged for commit

# Undo changes (be careful!)
git checkout -- filename   # Discard changes in working directory
git reset HEAD filename    # Unstage a file
git reset --soft HEAD~1    # Undo last commit, keep changes

# View remote repositories
git remote -v

# Create and switch to a new branch
git checkout -b feature-branch
git push -u origin feature-branch

# Switch between branches
git checkout main
git checkout feature-branch

# Merge branches
git checkout main
git merge feature-branch
```

---

## Troubleshooting Common Issues

### Git Issues

**Issue**: `fatal: not a git repository`

```bash
# Solution: Initialize git in the current directory
git init
```

**Issue**: `Permission denied (publickey)`

```bash
# Solution: Check SSH key setup
ssh -T git@github.com
# If fails, regenerate SSH key or use HTTPS instead
```

**Issue**: Merge conflicts

```bash
# Solution: Open conflicted files, resolve conflicts manually
# Look for <<<<<<, ======, >>>>>> markers
# After resolving:
git add .
git commit -m "Resolve merge conflicts"
```

### Python/pip Issues

**Issue**: `command not found: python`

```bash
# Try python3 instead
python3 --version

# Or create an alias (macOS/Linux)
alias python=python3
```

**Issue**: `pip: command not found`

```bash
# Use python -m pip instead
python -m pip install package-name
```

**Issue**: Permission errors when installing

```bash
# Make sure you're in a virtual environment!
# Never use sudo with pip
source .venv/bin/activate
pip install package-name
```

### Virtual Environment Issues

**Issue**: Can't activate virtual environment

```bash
# Windows: Enable script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Recreate the virtual environment if corrupted
rm -rf venv
python -m venv .venv
```

---

## Additional Resources

### Documentation

- **Git**: https://git-scm.com/doc
- **GitHub**: https://docs.github.com
- **Python**: https://docs.python.org
- **pip**: https://pip.pypa.io
- **VSCode**: https://code.visualstudio.com/docs

### Interactive Learning

- **Git**: https://learngitbranching.js.org
- **Python**: https://www.learnpython.org
- **Command Line**: https://www.codecademy.com/learn/learn-the-command-line

### GitHub Student Pack

If you're a student, get free access to premium developer tools:
https://education.github.com/pack

---

## Review

Now you've completed the full setup! Here's what you've learned:

1. Learned command line basics (Windows CMD and Unix)
2. Installed VSCode, Python, and Git
3. Written your first Python script
4. Created and used a virtual environment
5. Installed packages with pip and created a requirements file
6. Set up .gitignore to protect your venv
7. Created a GitHub account
8. Made your first repository and pushed code

Next week we'll be getting into the actual project! We'll start off by learning how to use an API to download data and explore how it can be used!
