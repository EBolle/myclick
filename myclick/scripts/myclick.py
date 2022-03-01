import click

import myclick.writing.main as writing


@click.group()
def cli():
    pass

cli.add_command(writing.clean_html)
cli.add_command(writing.ly_words)
cli.add_command(writing.word_counter)
cli.add_command(writing.top_n_words)