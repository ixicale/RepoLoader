#!/bin/bash

# create python3 virtual environment
python3 -m venv .venv || { echo "Python3 venv not found. Please install python3-venv package." && exit 1; }

# activate virtual environment
source .venv/bin/activate

# update pip and install requirements
pip install --upgrade pip
pip install requests

# check if github token is set
if git config --global github.token > /dev/null 2>&1; then
    echo "🚀 RepoLoader started..."
    echo ""
    # execute python script
    python -c "$(curl -fsSL https://raw.githubusercontent.com/ixicale/RepoLoader/main/repo_loader.py)"

    # deactivate virtual environment
    deactivate
    # remove virtual environment folder
    rm -rf .venv

    # message to user that the script is ended
    echo "Workflow ended. You can close this terminal.👋 Bye bye!"
else
    # show message to set github token
    echo "❌ Please set the 'git config --global github.token' environment variable."
    echo "❔ Set it using the command: git config --global github.token <your_token>"
fi
