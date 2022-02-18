import re

import click


@click.group()
def cli():
    pass


@click.command()
@click.argument('input', type=click.File(mode='r', encoding='utf-8'))
@click.argument('output', type=click.File(mode='w', encoding='utf-8'), default='-')
def clean_html(input, output):
    """
    Takes in a HTML file and returns a cleaned HTML file which can be easily ran through a spell checker, hence
    the <br> elements remain.

    input: path to HTML file\n
    output: name of the cleaned HTML file, the default is stdout
    """
    clean_pattern = re.compile(r'(</?[adehip].*?>|<code>.*?</code>|\n|{%.*?%})', flags=re.DOTALL|re.MULTILINE)
    return_html = re.sub(clean_pattern, "", input.read())

    output.write(return_html)


cli.add_command(clean_html)