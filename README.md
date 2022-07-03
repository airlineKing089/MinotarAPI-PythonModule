# MinotarAPI-PythonModule
A Python module aiming to implement the Minotar API [minotar.net](https://minotar.net/).

## installation
1. Install the requests module.
    - Press the keys: Win+R.
    - In the small box, type: `cmd`, and press enter.
    - A Command Prompt window should open. In it type: `pip install requests`.

2. Add the MinotarAPI Module to your project.
    - Download `MinotarAPI.py` from [latest Release](https://github.com/airlineKing089/MinotarAPI-PythonModule/releases).
    - Copy it to your project directory.
    - Paste `import MinotarAPI as minotar` to the top of your Python script.
    - You have successfully imported the MinotarAPI!

Quickstart Code Example:
```python
# import minotar module
import MinotarAPI as minotar

# user input for the username
username = input("Minecraft Username: ")

# downloads the skin
minotar.download.skin(username)
```

## Documentation

### default class
- `minotar.default.Steve()` [Downloads the default steve skin],
- `minotar.default.Alex()` [Downlaods the default alex skin],

### download class
- `minotar.download.skin(username)` [Downloads the skin, requires the username to be entered],
- `minotar.download.avatar(username, size)` [Downloads the avatar, requires the size in pixels and username to be entered],
