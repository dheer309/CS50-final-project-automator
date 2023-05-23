import argparse
import os
import shutil

import feedparser
import requests
from nltk import word_tokenize
from nltk.corpus import wordnet
from spellchecker import SpellChecker
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from textblob import TextBlob


def get_top_stories():
    url = 'https://news.google.com/rss'
    response = requests.get(url)
    feed = feedparser.parse(response.text)
    top_stories = [entry.title for entry in feed.entries]
    return top_stories


def present_in_bulleted_list(stories):
    for story in stories:
        print(f'• {story}')


def organize_files(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_extension = os.path.splitext(filename)[1][1:]
            target_folder = os.path.join(target_dir, file_extension.upper())

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_folder, filename)
            shutil.move(source_path, target_path)
            print(f"Moved {filename} to {target_folder}")


def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return [str(sentence) for sentence in summary]


def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms


def replace_with_synonyms(text):
    tokens = word_tokenize(text)
    replaced_tokens = []
    for token in tokens:
        synonyms = get_synonyms(token)
        if synonyms:
            replaced_tokens.append(synonyms[0])  # Replace with the first synonym
        else:
            replaced_tokens.append(token)
    return ' '.join(replaced_tokens)


def get_sentiment_score(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score


def spell_check(text):
    spell = SpellChecker()
    corrected_text = ""
    words = text.split()

    for word in words:
        corrected_word = spell.correction(word)
        corrected_text += corrected_word + " "

    return corrected_text.strip()


def main():
    parser = argparse.ArgumentParser(description='Automation Tools')
    parser.add_argument('--summarize-news', action='store_true', help='Summarize top stories from Google News')

    parser.add_argument('--organize', action='store_true', help='Organize files into sub folders.')
    parser.add_argument('--input-dir', type=str, help='Input directory path.')
    parser.add_argument('--output-dir', type=str, help='Output directory path.')

    parser.add_argument('--summarize-text', type=str, help='Text to summarize.')
    parser.add_argument('--num_sentences', type=int, default=3, help='Number of sentences in the summary.')

    parser.add_argument('--text-spin', type=str, help='Replace words in your text with synonyms.')

    parser.add_argument('--sentiment-analysis', type=str,
                        help='Analyses text to tell if its positive negitive or neutral.')

    parser.add_argument('--spell-checker', type=str, help='Corrects the incorrect spellings in the text.')

    args = parser.parse_args()

    if args.summarize_news:
        stories = get_top_stories()
        present_in_bulleted_list(stories)

    if args.organize and args.input_dir and args.output_dir:
        source_directory = args.input_dir
        target_directory = args.output_dir
        organize_files(source_directory, target_directory)

    if args.summarize_text:
        summary_sentences = summarize_text(args.summarizetext, args.num_sentences)
        print("Text Summary:")
        for sentence in summary_sentences:
            print("- " + sentence)

    if args.text_spin:
        new_text = replace_with_synonyms(args.text_spin)
        print("New text with synonyms: ", new_text, "\n")

    if args.sentiment_analysis:
        sentiment_score = get_sentiment_score(args.sentiment_analysis)
        print("Sentiment score: ", sentiment_score, "\n")

    if args.spell_checker:
        corrected_text = spell_check(args.spell_checker)
        print("Corrected text: ", corrected_text, "\n")


if __name__ == '__main__':
    main()
