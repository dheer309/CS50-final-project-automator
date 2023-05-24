# automate50 - By Dheer Maheshwari and Pritansh Sahsani

#### Video Demo:  *url

### description:

Our project is a series of command-line automations in python related to words and language, such as summerizing text, spell checking, news summerizing, etc.


**News summerizer:** Takes the top news from Google News and summerizes them to give a list of the latest news.

**File organizer:** Sorts the files in the input directory into seperate directories based on their file type. 

**Text summarizer:** Takes a input number of lines and summarizes the input text in that number of lines.

**Text spin:** Similar to spinbot or quillbot, it replaces the words in the input text with synonyms.

**Sentiment analysis:** Takes the input text and analyzes if it comments positively, negitively or neutrally on a topic.

**Spell checker:** Takes the input text and checks and fixes the spelling errors.

## Lessons Learned
This project provided us several valuable learning opportunities:

- Understanding API and package functionality: By using different APIs and packages, we gained a deeper understanding of how they work and the specific functionality they provide. This knowledge can be valuable when integrating APIs into your own projects or when working with existing systems that rely on APIs.

- Practicing implementation: Working with APIs involves implementing them in your code. By using different APIs, we practiced integrating them into our project. This hands-on experience strengthened our programming skills and exposed us to different coding patterns, libraries, and frameworks associated with each API.

- Learning best practices: Documentation provided by API providers is a valuable resource for understanding how to use their APIs effectively. Reading and understanding API documentation taught us  about best practices, recommended usage patterns, error handling, authentication mechanisms, and any limitations or restrictions that may exist. These guidelines help you write cleaner, more efficient code and avoid common pitfalls.

- Interpreting documentation: Ducumentations are often complex and hard to wrap our head around, using extremely technical language and specifing every small detail, even things that are rarely useful the programmers, so through this project, we could learn a lot about how we can get the useful information out of documentations.

- Enhancing problem-solving abilities: Using different APIs and reading their documentation exposes you to a wide range of functionalities and use cases. This exposure helped expand our problem-solving abilities by presenting us with various challenges and opportunities.

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
  python main.py --(arguement) (value)
```
arguements
- summarize-news : Run the news summarizer. 
- organize : Run the file organizer. requires input-dir and output-dir.
- input-dir : add the input directory for the file organizer.
- output-dir : add the output directory for the file organizer.
- summarize-text : Run the text summerizer. Requires str value and num_sentences.
- num_sentences : number of sentences in the summary. 
- text_spin : Run the text spin. Requires str value.
- sentiment-analysis : Run the sentiment analysis. Requires str value.
- spell-checker : Run the spell checker. Requires str value.

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
