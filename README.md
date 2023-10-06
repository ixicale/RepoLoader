# Repo Loader

<p align="center">
    <img align="center" src="assets/gif/coding.gif" alt="Coding" height="200px" />
</p>
<p align="center">
    <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?size=25&color=F75C7E&center=true&vCenter=true&width=540&lines=REPO+LOADER;Help+me+with+one+star!"></img></a>
</p>

## Description

📋 `Repo Loader` is a Python script designed to clone all your GitHub repositories to your local machine.

## Configuration

### Requirements:

- 🛑 REQUIRED: Set your `GITHUB_TOKEN`and set it on gitconfig (`git config --global github.token`). More info on [creating a GitHub Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
- 🛑 REQUIRED: ssh configured on github! This script use `git clone <ssh_url_repo>`, so its required to have ssh configured on github.
- ⚙ OPTIONAL: Set `PATH_TO_SAVE_REPOS` environment variable if you wish to customize the directory where repositories will be saved. The default directory is `.repos`.

## Usage

🚀 Execute the script directly from a remote repository:

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ixicale/RepoLoader/main/exec.sh)";
```

## Features

- 🔄 Automatically checks and clones repositories.
- 🗂 Organizes repositories by the owner's username.
- 📊 Provides a breakdown of repositories cloned.

## Feedback

If you encounter any issues or have feedback to improve this script, please raise an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Disclaimer

This project is not affiliated with GitHub, Inc in any way.
