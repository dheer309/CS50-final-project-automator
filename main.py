import argparse
import requests
from PIL import Image, ImageFilter
import os
import shutil
import feedparser

from nltk.corpus import wordnet

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


def get_top_stories():
    url = 'https://news.google.com/rss'
    response = requests.get(url)
    feed = feedparser.parse(response.text)
    top_stories = [entry.title for entry in feed.entries]
    return top_stories

def present_in_bulleted_list(stories):
    for story in stories:
        print(f'• {story}')

def resize_images(input_dir, output_dir, size):
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)
            resized_image = image.resize(size)
            output_path = os.path.join(output_dir, f"resized_{filename}")
            resized_image.save(output_path)
            print(f'Resized {filename} successfully. Renamed to resized_{filename}')


def crop_images(input_dir, output_dir, crop_area):
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)
            cropped_image = image.crop(crop_area)
            output_path = os.path.join(output_dir, f"cropped_{filename}")
            cropped_image.save(output_path)
            print(f'Cropped {filename} successfully. Renamed to cropped_{filename}')


def apply_blur(input_dir, output_dir, filter_type):
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)
            filtered_image = image.filter(filter_type)
            filter_name = filter_type.__name__.lower()
            output_path = os.path.join(output_dir, f"{filter_name}_{filename}")
            filtered_image.save(output_path)
            print(f'Applied {filter_type} filter to {filename} successfully. Renamed to {filter_name}_{filename}')

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
            synonym = lemma.name()
            if synonym != word:
                synonyms.append(synonym)
    return synonyms

def main():
    parser = argparse.ArgumentParser(description='Automation Tools')
    parser.add_argument('--summarizenews', action='store_true', help='Summarize top stories from Google News')
    parser.add_argument('--resize', action='store_true', help='Resize images')
    parser.add_argument('--crop', action='store_true', help='Crop images')
    parser.add_argument('--resize-size', type=int, nargs=2, metavar=('WIDTH', 'HEIGHT'), help='Size for image resizing')
    parser.add_argument('--crop-area', type=int, nargs=4, metavar=('LEFT', 'UP', 'RIGHT', 'DOWN'), help='Crop area for images')
    parser.add_argument('--blur', action='store_true', help='Apply blur effect to images')
    parser.add_argument('--organize', action='store_true', help='Organize files')
    parser.add_argument('--input-dir', type=str, help='Input directory path')
    parser.add_argument('--output-dir', type=str, help='Output directory path')
    parser.add_argument('--summarizetext', type=str, help='Text to summarize')
    parser.add_argument('--num_sentences', type=int, default=3, help='Number of sentences in the summary')
    parser.add_argument('--thesaurus', metavar='WORD', help='Find synonyms for the specified word')

    args = parser.parse_args()

    if args.summarizenews:
        stories = get_top_stories()
        present_in_bulleted_list(stories)

    if args.resize and args.input_dir and args.output_dir:
        input_directory = args.input_dir
        output_directory = args.output_dir
        size = tuple(args.resize_size)
        resize_images(input_directory, output_directory, size)

    if args.crop and args.input_dir and args.output_dir:
        input_directory = args.input_dir
        output_directory = args.output_dir
        crop_area = tuple(args.crop_area)
        crop_images(input_directory, output_directory, crop_area)

    if args.blur and args.input_dir and args.output_dir:
        input_directory = args.input_dir
        output_directory = args.output_dir
        filter_type = ImageFilter.BLUR
        apply_blur(input_directory, output_directory, filter_type)

    if args.organize and args.input_dir and args.output_dir:
        source_directory = args.input_dir
        target_directory = args.output_dir
        organize_files(source_directory, target_directory)

    if args.summarizetext:
        summary_sentences = summarize_text(args.summarizetext, args.num_sentences)
        print("Text Summary:")
        for sentence in summary_sentences:
            print("- " + sentence)
    
    if args.thesaurus:
        word = args.thesaurus
        synonyms = get_synonyms(word)
        if synonyms:
            print(f"Synonyms of '{word}':")
            for synonym in synonyms:
                print(synonym)
        else:
            print(f"No synonyms found for '{word}'")

if __name__ == '__main__':
    main()
