# CS50 Final Project - By Dheer Maheshwari and Pritansh Sahsani

this project automates basic stuff used daily by people into one command line utility... bla blah blah...... (tu likhde pritansh)

## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?

## Setup Locally

Download this project, and go to the project directory

```bash
  cd CS50-final-project-automator
```

Create a virtual environment

```bash
  python -m venv venv
```

Activate the virtual environment: Mac/Linux

```bash
  source venv/bin/activate
```

Activate the virtual environment: Windows

```bash
  venv\Scripts\activate.bat
```

Install all dependencies

```bash
  pip install -r requirements.txt
```

(this step doesn't work on every internt connection, if it doesn't work, then try running this command with a different internet source)
```bash
  python3 -c "import nltk; nltk.download('punkt'); nltk.download('wordnet');"
```

Run the code

```bash
  python main.py --(tool you wish to run)
```

## Usage

1. Open a terminal or command prompt and navigate to the root directory of the project (if you haven't done so already).

2. Run the main.py script with the desired command-line arguments to execute the different automation tools. The available options are:

* --summarize-news: Summarize top stories from Google News.
* --organize: Organize files into subfolders based on their file extensions.
* --input-dir: Specify the input directory path for the file organization tool.
* --output-dir: Specify the output directory path for the file organization tool.
* --summarize-text: Provide the text to summarize.
* --num-sentences: Specify the number of sentences in the summary (default: 3).
* --text-spin: Replace words in text with synonyms.
* --sentiment-analysis: Perform sentiment analysis on text.
* --spell-checker: Correct the incorrect spellings in the text.

Example Usages:
```bash
python main.py --summarize-news
python main.py --organize --input-dir /path/to/input --output-dir /path/to/output
python main.py --summarize-text "Lorem ipsum dolor sit amet."
python main.py --text-spin "Replace this text with synonyms."
python main.py --sentiment-analysis "This is a positive sentence."
python main.py --spell-checker "Thiss is a testt with incorreect spellings."
```

3. The output of each tool will be displayed in the terminal

## 🚀 About Us

write anything about us...

## Authors

- [@dheer309](https://www.github.com/dheer309)
- [@pritansh-sahsani](https://www.github.com/pritansh-sahsani)
