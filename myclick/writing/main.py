import re
import time
from collections import defaultdict
from pathlib import Path

import click

from myclick.writing.utils import _clean_text, _paragraph_words, _newline_locator


@click.command()
@click.argument('input', type=click.File(mode='r', encoding='utf-8'))
def clean_html(input):
    """
    Strips most of an HTML file and opens directly in your default browser so you can easily run a spell check.

    input: path to HTML file\n
    """
    clean_pattern = re.compile(r'(</?[adehi][^>]*>|<pre>.*?</pre>|\n|{%[^%}]*%})', flags=re.DOTALL)

    Path('_temp.html').touch()
    with open('_temp.html', mode='w') as output:
        output.write(re.sub(clean_pattern, "", input.read())) 

    click.launch(output.name)
    time.sleep(0.5)    
    Path('_temp.html').unlink()


@click.command()
@click.argument('input', type=click.File(mode='r', encoding='utf-8'))
def ly_words(input):
    """
    Locates words ending on 'ly' and prints the line number, word, and sentence to stdout. Having too many words
    ending on 'ly' is an indicator of writing too loose, which we want to prevent.
    """
    text = input.read()
    ly_pattern = re.compile(r'(^.*(\b\w+ly\b).*)', flags=re.MULTILINE|re.IGNORECASE) 

    match_start_list = []
    matches = []

    for match in re.finditer(ly_pattern, text):
        match_start_list.append(match.start())
        matches.append((match.group(1).strip(), match.group(2).strip()))   

    newlines = _newline_locator(text, match_start_list)

    for lineno, (sentence, word) in zip(newlines, matches):
        click.echo(f"{lineno} ({word}): {sentence}")


@click.command()
@click.argument('input', type=click.File(mode='r', encoding='utf-8'))
def word_counter(input):
    """
    Returns the number of words per paragraph. Useful to get an idea of the flow of your post, 
    e.g., is there too much text in certain areas of the post?  
    """
    clean_text = _clean_text(input.read())
    p_lists = _paragraph_words(clean_text)

    words_per_paragraph = {idx: len(p_list) for idx, p_list in enumerate(p_lists, start=1)}

    for key, value in words_per_paragraph.items():
        click.echo(f"<p> {key}: {value} words")


@click.command()
@click.argument('input', type=click.File(mode='r', encoding='utf-8'))
@click.option('--mincount', default=5, help="Minimum number of occurences in the file.")
def top_n_words(input, mincount):
    """
    Returns the most prevalent words in the HTML input. This may be useful to detect unconsious
    preferences for certain words, e.g., 'I', 'me', or 'also'.
    """
    clean_text = _clean_text(input.read())
    p_lists = _paragraph_words(clean_text)

    word_counter = defaultdict(int)

    for p_list in p_lists:
        for word in p_list:
            word_counter[word] += 1

    sorted_word_counter = {key: value for key, value in sorted(word_counter.items(), key=lambda x: x[1], reverse=True) if value >= mincount}

    for key, value in sorted_word_counter.items():
        click.echo(f"{key}: {value}")