import argparse

from utils.file_utils import organize_files
from utils.news_utils import get_top_stories, present_in_bulleted_list
from utils.text_utils import summarize_text, replace_with_synonyms, get_sentiment_score, spell_check


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
        summary_sentences = summarize_text(args.summarize_text, args.num_sentences)
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
