"""
        ██████╗ ███████╗██████╗  ██████╗ 
        ██╔══██╗██╔════╝██╔══██╗██╔═══██╗
        ██████╔╝█████╗  ██████╔╝██║   ██║
        ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║
        ██║  ██║███████╗██║     ╚██████╔╝
        ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ 
            °°°°°°°°°°°°°°°°°°°°°°°°
██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

Clone all your GitHub repositories to your local machine.
Usage:
    Option 1: Run the automated script
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/ixicale/RepoLoader/main/exec.sh)";
    Option 2: Run the python script, requires python3 venv and 'requests' installed
    python -c "$(curl -fsSL https://raw.githubusercontent.com/ixicale/RepoLoader/main/repo_loader.py)"
Required:
    Set your Personal Access Token (PAT) on your git config (git config --global github.token).
    More info: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
Optional:
    Set PATH_TO_SAVE_REPOS environment variable to customize the root save directory. Default is '.repos'
"""

import os
import subprocess
from typing import Dict

import requests

# Get token from your git config
GC_PERSONAL_ACCESS_TOKEN = 'git config --global github.token'.split(" ")
PAT = subprocess.run(GC_PERSONAL_ACCESS_TOKEN,capture_output=True,text=True).stdout.strip()
# Retrieve environment variables
PATH_TO_SAVE_REPOS = os.environ.get("PATH_TO_SAVE_REPOS", ".repos")
if not PAT:
    print("❌ Please set the 'git config --global github.token' environment variable.")
    exit(1)

GH_API = "https://api.github.com"
HEADERS = {"Authorization": f"Bearer {PAT}"}
COMMON_PATH = os.path.join(os.path.expanduser("~"), PATH_TO_SAVE_REPOS)

# Counter for cloned repositories by user
repos_count_by_user: Dict[str, int] = {}

page_count = 1
# Fetch all repos associated with the authenticated user
while True:
    response = requests.get(
        f"{GH_API}/user/repos?per_page=100&page={page_count}", headers=HEADERS
    )
    if response.status_code != 200:
        print(f"❌ Error {response.status_code}: {response.text}")
        break

    list_repos = response.json()
    if not list_repos:
        break

    for repo in list_repos:
        repo_url = repo.get("ssh_url")
        owner = repo.get("owner", {}).get("login")
        user_path = os.path.join(COMMON_PATH, owner)
        os.makedirs(user_path, exist_ok=True)

        repo_path = os.path.join(user_path, repo.get("name"))
        if not os.path.exists(repo_path):
            print(f"📦 Cloning {repo_path}...")
            subprocess.run(["git", "clone", repo_url, repo_path])
        else:
            print(f"📦 Fetching {repo_path}...")
            subprocess.run(["git", "fetch"], cwd=repo_path)

        # Update repo count for each owner
        repos_count_by_user[owner] = repos_count_by_user.get(owner, 0) + 1

    page_count += 1

total = sum(repos_count_by_user.values())
print(
    f"""
🚀 Finished cloning to {COMMON_PATH}
🔢 Total repos cloned: {total}
📊 Repos breakdown: {repos_count_by_user or "<None cloned>"}
"""
)
