# README

This script pulls information on "name", "modId" and "version" from the official workshop page and prints it ready for copy and paste

Example:

```json
{
    "modId": "591AF5BDA9F7CE8B",
    "version": "1.0.6",
    "name": "Capture & Hold"
},
```

## Install

1. Download [Python 3](https://www.python.org/downloads/). Make sure to tick the "add to PATH variable" option.
2. Run `pip install -r requirements.txt` (or currently simple `pip install beautifulsoup4`)
3. Open the Terminal of your choice (e.g., powershell) and navigate to the script.
4. Run with `python3 ./main.py`

## Use

You hate two options to use this script

1. Manual Use: Simply run the script using `python3 ./main.py`. Then input the Arma 3 Reforger Workshop URL (e.g., `https://reforger.armaplatform.com/workshop/591AF5BDA9F7CE8B-Capture%2526Hold`). Use `ctrl + c` or type `exit` to exit the application once you are finished with all mods.
2. Use by File: First create a txt file in the same directory as `main.py` (we'll call it `mods.txt`). Paste all URLs in the file, each URL in a separate line. Then simply run the script using `python3 ./main.py --list=<filename>` (so in our case `python3 ./main.py --list=mods.txt`).

    Exmample `mods.txt`:

    ```txt
    https://reforger.armaplatform.com/workshop/591AF5BDA9F7CE8B-Capture%2526Hold
    https://reforger.armaplatform.com/workshop/59D64ADD6FC59CBF-ProjectRedline-UH-60
    https://reforger.armaplatform.com/workshop/5AB890B71D748750-M4A1BlockIIandURG-I
    https://reforger.armaplatform.com/workshop/595F2BF2F44836FB-RHS-StatusQuo
    https://reforger.armaplatform.com/workshop/5AAF6D5352E5FCAB-ProjectRedline-Core
    ```
