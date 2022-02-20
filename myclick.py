import re

import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--launch/--no-launch', default=False)
@click.argument('input', type=click.File(mode='r', encoding='utf-8'))
@click.argument('output', type=click.File(mode='w', encoding='utf-8'), default='-')
def clean_html(launch, input, output):
    """
    Takes in a HTML file and returns a cleaned HTML file which can be easily ran through a spell checker, hence
    the <p> and <br> elements remain. 

    input: path to HTML file\n
    output: name of the to be created cleaned HTML file, the default is stdout
    """
    clean_pattern = re.compile(r'(</?[adehi].*?>|<pre>.*?</pre>|\n|{%.*?%})', flags=re.DOTALL|re.MULTILINE)
    output.write(re.sub(clean_pattern, "", input.read()))  

    if launch:
        click.launch(output.name)


cli.add_command(clean_html)