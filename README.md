# Playwright-Pytest
To Practice &amp; Learn New Stuffs in Python


## VENV Troubleshooting:
In VSCode, there is no default option to create virtual environment in Python. So foloow below steps to create one:
1. Open Visual Studio Code in your project's folder.
2. In the terminal:
```python
# venv is your virtual environment name
# You can also use py -3 -m venv .venv
python -m venv venv
```
3. After the virtual environment is generated, use the following command to activate the virtual environment
```python
# venv is your virtual environment name
venv\scripts\activate
```
4. If you get error message after running above command, please do this:
    1. Change the execution policies by adding -ExecutionPolicy Bypass args. in vscode you will have to create a shell profile with these args by adding below in settings.json (ctrl + shift + p and type "settings.json")

    ```python
    "terminal.integrated.profiles.windows": {
    "PowerShell": {
        "source": "PowerShell",
        "icon": "terminal-powershell",
        "args": ["-ExecutionPolicy", "Bypass"]
    }
    },
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    ```
    2. Need to restart VS Code and the Terminal.
    3. Run:
    ```python
    # venv is your virtual environment name
    venv\scripts\activate
    ```
5. Then Python: Select Interpreter (via Ctrl + Shift + P)
6. And select the option (in my case towards the bottom)
7. Select --> Python 3.7 (venv) ./venv/Scripts/python.exe
