from nltk import word_tokenize
from nltk.corpus import wordnet
from spellchecker import SpellChecker
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from textblob import TextBlob


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
