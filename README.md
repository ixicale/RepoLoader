# RepoLoader
```
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
```

Clone all your GitHub repositories to your local machine.
Usage:
    python -c "$(curl -fsSL https://raw.githubusercontent.com/user/repo/branch/test.py)"
Required:
    Set your GITHUB_TOKEN environment variable. 
    More info: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
Optional:
    Set PATH_TO_SAVE_REPOS environment variable to customize the root save directory. Default is '.repos'
