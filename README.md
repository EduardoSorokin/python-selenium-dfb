# Python Selenium DFB (Don't Follow Back)

> Check who are not following you back on Instagram.

There are **2 independent ways** to accomplish this task. It can be done by using **Jupyter** or just running the **Python script**.

1. Using **Jupyter**, selenium will do the "magic" to collect the data and then a simple chart as well as three lists will be printed on the notebook with your followers, who you are following and those who are not following you back respectively.

2. Running the **Python script**, selenium will do the "magic" to collect the data and then a prepared website page will be loaded to receive that data and show three lists containing your followers, who you are following and those who are not following you back respectively.

## Project files

```text
.
|--- jupyter_notebook
|    |--- selenium_instgrm.ipynb
|--- python_script
|    |--- selenium_instgrm.py
|--- .gitignore
|--- CHANGELOG.md
|--- LICENSE
|--- README.md
```

## Installation

### Linux

> First of all, you will need Python but Python is pre-installed on Linux, so just be sure you have at least the version 3.x.

```bash
# Update the package list
$ sudo apt update

# Install "pip" for Python 3
$ sudo apt install python3-pip

# Install "Selenium" package
$ pip3 install selenium

# Install "Beutiful Soup" package
$ pip3 install bs4

# The next packages only will need to be installed if you want to execute the code using Jupyter

# Install packages: "jupyter-core" and "jupyter-notebook"
$ sudo apt install jupyter-core jupyter-notebook

# Install packages: "NumPy", "Pandas" and "Matplotlib
$ pip3 install numpy pandas matplotlib
```

In order to run **Selenium**, you will need the right browser driver:

> By default the code will run on Firefox.

- **Firefox:** [geckodriver](https://github.com/mozilla/geckodriver/releases)
- **Google Chrome:** [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

After download and unpack the driver you want to use, open the Terminal in the directory where the driver is and give executable permissions to the driver. After that move the driver to `/usr/local/bin` (or any location on your system PATH), like this:

```bash
# Give executable permissions
$ sudo chmod +x NAME_OF_THE_DRIVER

# Move to a location that is in your system PATH
$ sudo mv NAME_OF_THE_DRIVER /usr/local/bin
```

### Windows

- Install [Python](https://www.python.org/downloads)
- Add Python to the system PATH:
    1. Open `System Properties` (Right click `Computer` in the start menu, or use the keyboard shortcut `Win`+`Pause`)
    2. Click `Advanced system settings` in the sidebar
    3. Click `Environment Variables...`
    4. Select `PATH` in the `System variables` section
    5. Click `Edit`
    6. Add Python's PATH to the end of the list. For example:
        - `C:\Python36` and `C:\Python36\scripts`
- Open the Command Prompt (`cmd.exe`) and install the required packages with the following commands:

```bash
# Install "Selenium" package
pip install selenium

# Install "Beutiful Soup" package
pip install bs4

# The next packages only will need to be installed if you want to execute the code using Jupyter

# Install packages: "NumPy", "Pandas" and "Matplotlib
pip install numpy pandas matplotlib
```
In order to run **Selenium**, you will need the right browser driver:

> By default the code will run on Firefox.

- **Firefox:** [geckodriver](https://github.com/mozilla/geckodriver/releases)
- **Google Chrome:** [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

After download and unpack the driver you want to use, move the file to a better location than the Download folder. For example: `C:\Selenium\Drivers\`

You will need to add the driver PATH to your system PATH, just like you did before with Python.

**_Do not include the filename in the PATH, just the directories._**

## Usage

Download the files or clone this repository on your computer.

### 1. selenium_instgrm.ipynb

- Open the Terminal (Linux) or Command Prompt (Windows)
- Navigate to the root project folder and then to the **jupyter_notebook** folder
- Initialize Jupyter server by running the command: `jupyter notebook` (Linux) or `jupyter-notebook` (Windows)
- The Jupyter server will initialize on your browser and then click on `selenium_instgrm.ipynb` file listed on the page
- At the `# Login` section, fill the variables `username` and `password` with your Instagram credentials
- Press the keys: `Ctrl`+`ENTER` to execute the code in the cell
- Wait and see! :-)

> _Your data (such as your username and password) will NOT be storage. Don't forget to clear these informations after finishing running the code just to be more careful._

### 2. selenium_instgrm.py

- Open the root project folder and then open the **python_script** folder
- Click to edit the file `selenium_instgrm.py` on any text editor you like
- At the `# Variables` section, fill the variables `username` and `password` with your Instagram credentials
- Open the Terminal (Linux) or Command Prompt (Windows)
- Navigate to the root project folder and then to the **python_script** folder
- Run the command: `python3 selenium_instgrm.py`
- Wait and see! :-)

> _Your data (such as your username and password) will NOT be storage. Don't forget to clear these informations after finishing running the script just to be more careful._

## Author

Eduardo Sorókin

### Contact

- [LinkedIn](https://linkedin.com/in/eduardosorokin)
- [Twitter](https://twitter.com/EduardoSorokin)

## Changelog

[CHANGELOG.md](CHANGELOG.md)

## References

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc)
- [Jupyter](http://jupyter.org)
- [Matplotlib](https://matplotlib.org)
- [Pandas](https://pandas.pydata.org)
- [pip](https://pypi.org/project/pip)
- [Python](https://www.python.org)
- [Selenium](https://selenium-python.readthedocs.io)
    - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    - [Geckodriver](https://github.com/mozilla/geckodriver/releases)

## License

[GNU General Public License v3.0](https://github.com/EduardoSorokin/python-selenium-dfb/blob/master/LICENSE)
