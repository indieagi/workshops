# Welcome
Welcome to the Intro to Full Stack LLM Workshop.

# Agenda
```
4:00p-4:20p  Development Environment Setup
4:20p-4:40p  Code Tutorial
4:40p-5:00p  Extra Time, Questions, Discussion
```

We will likely go off schedule as this is our first time offering the workshop.

In `Development Environment Setup`, we will set up two things:
1. `git`: the global standard in text version control
2. `python3`: the standard programming environment for AI and other data applications

# What if I get stuck?
You may get stuck because we haven't learned how people get stuck yet.

Just get one of the instructors' attention. Or ask someone near you. 

# Instructions
## Development Environment Setup
Use the instructions for the type of computer you have with you.

### Windows

#### Check for `python3`
Open a terminal. You can search for "cmd" in the Start Menu.

Test that `python3` is installed on your system:
```
python3 --version
```
If this command fails or there is no output, you must install Python.

#### Install `python3`
You can install `python` by downloading and running the installer at `https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe`

#### Install `pip`
Run the following command:
```
python -m ensurepip --upgrade
```

#### Check for `git`
Run the following command:
```
git --version
```
If you get no output or a failure, you'll need to install `git`.

#### Install `git`
Download the installer from `https://github.com/git-for-windows/git/releases/download/v2.42.0.windows.2/Git-2.42.0.2-64-bit.exe`.

Follow the prompts.

Finally, run the following command to check that `git` installed correctly:
```
git --version
```

#### Clone This Repo
Make a directory to save source code to. Using `~/src` is common for professional programmers:
```
cd %USERPROFILE%
mkdir src
```

Change to that directory:
```
cd src
```

Clone this repo:
```
git clone https://github.com/indieagi/workshops.git
```

You should see a folder called `workshops` now:
```
dir
```

### MacOS
Open a terminal. You can do this by hitting `cmd + space` and then typing "terminal".

#### Check for `python3`
Test that `python3` is installed on your system:
```
python3 --version
```
If this command fails or there is no output, you must install Python.

#### Install `pip`
Run the following command:
```
python3 -m ensurepip --upgrade
```

#### Install `git`
```
xcode-select --install
```

Next, test that installing `git` was successful. If the output of this command is blank, there was a problem with your installation:
```
git --version
```

#### Clone This Repo
Make a directory to save source code to. Using `~/src` is common for professional programmers:
```
mkdir ~/src
```

Change to that directory:
```
cd ~/src
```

Clone this repo:
```
git clone https://github.com/indieagi/workshops.git
```

You should see a folder called `workshops` now:
```
ls -l
```

### Ubuntu Linux
Open a terminal. You can open the application launcher and then type "terminal".

#### Check for `python3`
Test that `python3` is installed on your system:
```
python3 --version
```
If this command fails or there is no output, you must install Python.

#### Install `pip`
Run the following command:
```
sudo apt install python3-pip
```

#### Install `git`
Install `git`:
```
sudo apt update        # Update package list
sudo apt install git   # Install Git
```

Next, test that installing `git` was successful. If the output of this command is blank, there was a problem with your installation:
```
git --version
```

#### Clone This Repo
Make a directory to save source code to. Using `~/src` is common for professional programmers:
```
mkdir ~/src
```

Change to that directory:
```
cd ~/src
```

Clone this repo:
```
git clone https://github.com/indieagi/workshops.git
```

You should see a folder called `workshops` now:
```
ls -l
```

## Code Tutorial
First, you need to activate Google Colab for your Google Account. This is free.

Go to `colab.research.google.com`

Click the "Upload" tab. Navigate to your `~/src/workshops` folder and select `intro-to-full-stack-llm.ipynb`

Your workshop notebook should now be open. Go ahead and start the tutorial from there.

Easter Egg: In Colab, go to `Tools > Settings > Miscellaneous > Corgi mode`.
