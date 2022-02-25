from email.policy import default
import re
from collections import defaultdict

import click

from writing import _paragraph_words, _newline_locator


@click.group()
def cli():
    pass


@click.command()
@click.option('--launch/--no-launch', default=False, help="Launches the cleaned HTML file in your default browser.")
@click.argument('input', type=click.File(mode='r', encoding='utf-8'))
@click.argument('output', type=click.File(mode='w', encoding='utf-8'), default='-')
def clean_html(launch, input, output):
    """
    Strips most of an HTML file and opens directly in your default browser so you can easily run a spell check, 

    input: path to HTML file\n
    output: name of the to be created cleaned HTML file, the default is stdout
    """
    clean_pattern = re.compile(r'(</?[adehi].*?>|<pre>.*?</pre>|\n|{%.*?%})', flags=re.DOTALL|re.MULTILINE)
    output.write(re.sub(clean_pattern, "", input.read()))  

    if launch:
        click.launch(output.name)

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
    text = input.read()
    tag_stripped_text = re.sub(r'</?\s*(a|br|em|strong|sup).*?>', '', text, flags=re.IGNORECASE|re.DOTALL)
    clean_text = re.sub(r'(\n|[.,!])', '', tag_stripped_text, flags=re.IGNORECASE|re.DOTALL)

    p_pattern = re.compile(r'(<p\s+.*?>)\s+(.*?)</p>', flags=re.IGNORECASE|re.DOTALL)
    p_lists = _paragraph_words(p_pattern, clean_text)
    words_per_paragraph = {idx: len(p_list) for idx, p_list in enumerate(p_lists, start=1)}

    for key, value in words_per_paragraph.items():
        click.echo(f"<p> {key}: {value} words")


cli.add_command(clean_html)
cli.add_command(ly_words)
cli.add_command(word_counter)