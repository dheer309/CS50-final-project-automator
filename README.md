# automate50 - By Dheer Maheshwari and Pritansh Sahsani

#### Video Demo:  *url

#### Description:

Our project is a series of command-line automations in python related to words and language, such as summerizing text, spell checking, news summerizing, etc.


**News summarizer:** Takes the top news from Google News and summarizes them to give a list of the latest news.

**File organizer:** Sorts the files in the input directory into separate directories based on their file type. 

**Text summarizer:** Takes a input number of lines and summarizes the input text in that number of lines.

**Text spin:** Similar to quillbot, it replaces the words in the input text with synonyms.

**Sentiment analysis:** Takes the input text and analyzes if it comments positively, negatively or neutrally on a topic.

**Spell checker:** Takes the input text and checks and fixes the spelling errors.

## Lessons Learned

This project provided us several valuable learning opportunities:

- Understanding APIs and package functionality: While doing this project, we explored different APIs and packages, which helped us gain a deeper understanding of how they work and the functionalities they provide. This knowledge can be valuable for us, when we integrate APIs and different libraries/packages in our projects or when we work on other programs that rely on APIs or packages.

- Practicing implementation: By using different APIs, we practiced integrating them into our project. This project strengthened our programming skills and we learnt many different coding patterns, libraries, and frameworks which we can use in development process.

- Learning best practices: Documentation provided by package developers was a valuable resource for understanding how to use their package effectively. Reading and understanding different documentation taught us  about best coding practices, recommended usage patterns, and error handling. These things helped us write cleaner and more efficient code, and avoid common errors.

- Understanding documentation: Often, we found some documentations were complex and it was hard to wrap our head around, and the documentation often used extremely technical language and specifing every small detail, things that were rarely useful to us, and through this project, we learnt a lot about how we can get the useful information out of documentations.

- Practicing/improving problem-solving abilities: Using different packages and reading their documentation has taught us wide range of their functionalities and how we can write code to make them work. This project overall has helped us enhance our problem-solving abilities as we gone through various hurdles and challenges.

## Setup Locally

Download this project, and go to the project directory

```bash
  cd CS50-final-project-automator
```

Create a virtual environment

```bash
  python -m venv /path/to/folder
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

## Run the code

```bash
  python main.py --(argument) (value)
```
Arguments:
- summarize-news : Run the news summarizer. 
- organize : Run the file organizer. requires input-dir and output-dir.
- input-dir : add the path for input directory for the file organizer. Enter the value with the file organizer utility.
- output-dir : add the path for output directory for the file organizer. Enter the value with the file organizer utility.
- summarize-text : Run the text summarizer. Requires str value and num_sentences.
- num_sentences : number of sentences in the summary. enter this value with summarize-text function. 
- text_spin : Run the text spin. Requires str value, use double quotation around string value.
- sentiment-analysis : Run the sentiment analysis. Requires str value, use double quotation around string value.
- spell-checker : Run the spell checker. Requires str value, use double quotation around string value.

## Example Usages
```bash
python main.py --summarize-news
python main.py --organize --input-dir /path/to/input --output-dir /path/to/output
python main.py --summarize-text "Lorem ipsum dolor sit amet."
python main.py --text-spin "Replace this text with synonyms."
python main.py --sentiment-analysis "This is a positive sentence."
python main.py --spell-checker "Thiss is a testt with incorreect spellings."
```

## About Us
We are high school students and classmates who are passionate about programming and love to solve different problems and take on challenges. We took the CS50 course as it presented us with an opportunity to learn and demonstrate our skills.

## Authors
- [@dheer309](https://www.github.com/dheer309)
- [@pritansh-sahsani](https://www.github.com/pritansh-sahsani)
