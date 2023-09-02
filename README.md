# Welcome
Welcome to the Intro to Full Stack LLM Workshop.

# Agenda
The workshop will proceed approximately as follows:
```
4:00p-4:20p  Development Environment Setup
4:20p-4:40p  Code Tutorial
4:40p-5:00p  Extra Time, Questions, Discussion
```

We are likely to go off schedule as this is the first time the workshop is offered.

In `Development Environment Setup`, we will setup two things:
1. `git`: the global standard in text version control
2. `python`: the standard programming environment for AI and other data applications

# What if I get stuck?
You will probably get stuck because we haven't learned all the ways people get stuck yet.

Just get one of the instructors attention. Or ask someone near you. No wrong options here.

# Instructions
## Development Environment Setup
Use the instructions for the type of computer you have with you.

### Windows

### MacOS

### Ubuntu Linux
Open a terminal. You can open the application launcher then type "terminal".

#### Check for `python3`
Test that `python3` is installed on your system:
```
python3 --version
```
If the following gives no output, just let your instructors know.

#### Install `git`
Install `git`:
```
sudo apt update        # Update package list
sudo apt install git   # Install Git
```

Next, test that installing `git` was successful. If the output of this command is blank, there was a problem with your install:
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
To start the code tutorial, we will copy the Jupyter notebook to your Google Drive then open it with Google Colab.

Open a browser window and navigate to `drive.google.com`. You'll need to sign in using a Google Account.

Click `New > File Upload` in the top-left corner of Google Drive. Navigate to your `~/src/workshops` folder and select `intro-to-full-stack-llm.ipynb`

In Google Drive, double-click on `intro-to-full-stack-llm.ipynb` to open it. You'll follow the instructions in the Jupyter notebook from here on.

Easter egg: In Colab, go to `Tools > Settings > Miscellaneous > Corgi mode`