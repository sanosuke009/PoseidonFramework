# Playwright-Pytest
To Practice &amp; Learn New Stuffs in Playwright with Python

## Installation Required:
Either you can run 
```python
    python3 -m pip install -r requirements.txt
    python3 -m playwright install
```
Or, if you know what you are doing, then run
```python
    python3 -m pip install pytest
    python3 -m pip install pytest-xdist
    python3 -m pip install allure-pytest
    python3 -m pip install pytest-playwright
    python3 -m playwright install  #For installing Chromium, Firefox and Webkit browsers
```
## If allure is not recognized as powershell command Troubleshooting:
1. Install nvm from here https://github.com/coreybutler/nvm-windows/releases (For Windows)
2. Install node using nvm
```node
    nvm install <version>
    nvm use <installed version>
    npm install -g allure-commandline --save-dev
```
3. If you find authentication error then
```shell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
4. Now allure serve command should work

## VENV Troubleshooting:
In VSCode, there is no default option to create virtual environment in Python. So follow below steps to create one:
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

## Remove VENV:
```python
    source venv/bin/activate
    pip freeze > requirements.txt
    pip uninstall -r requirements.txt -y
    deactivate
    rm -r venv/
```

## Troubleshooting Importerror: module not found _greenlet:
1. Reinstall the Microsoft Visual c++
Here is the link for downloading [Microsoft Visual c++] https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0.
2. Restart the system
3. Reinstall the venv & Python packages

## Starting with the first Playwright test:
1. Install all the required packages and set up vscode as mentioned above
2. Run:
```python
    pytest --alluredir=allure-results --headed --numprocesses auto
    allure serve .\allure-results
```

# TODO:
1. Debugging using page.pause() & inspector
2. https://shields.io/



# Jenkins Integration:
## TODO

## Troubleshooting for allure report:
1. Install allure plugin for jenkins
2. Add below code in the jenkins file:
```bash
    stage('Generating Reports') {
        steps {
            script {
                allure([
                    includePorperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
```