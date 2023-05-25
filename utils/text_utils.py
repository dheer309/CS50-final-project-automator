from nltk import word_tokenize, pos_tag
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


def replace_with_synonyms(text):
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    replaced_tokens = []

    for token, pos in tagged_tokens:
        synsets = wordnet.synsets(token)
        if synsets:
            synonyms = []
            for synset in synsets:
                for lemma in synset.lemmas():
                    if lemma.name() != token and not lemma.name().count('_'):
                        syn_pos = lemma.synset().pos()
                        if syn_pos.startswith(pos[0].lower()):
                            synonyms.append(lemma.name())
            if synonyms:
                replaced_tokens.append(synonyms[0])
            else:
                replaced_tokens.append(token)
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
