# Myclick

This is my personal CLI which I have developed to easily maintain the content of [my website][my_website], and to explore and wrangle data from the command-line.

## Usage

Although the commands are specific to my use cases, they might be useful to you as well. After you cloned the repo it is best to create a virtual environment before executing the following command.

```bash
pip install --editable .
```

You should now be able to execute commands directly from the command-line, which you can test with `myclick --help`. The CLI is created with [click][click], and they have additional documentation on the [setuptools integration][click-setuptools].

## Writing

This submodule is based on my ambition to become a better writer, and to learn more about regular expressions. Together they form a great combination to develop neat functionality which can be immediately applied in practice. My 2 sources of inspiration are:

- _Write Tight: Say Exactly What You Mean with Precision and Power by William Brohaugh_
- _Mastering Regular Expressions: Understand Your Data and Be More Productive by Jeffrey E.F. Friedl (3th edition)_

### clean-html

The clean-html command strips most of the html tags, but keeps enough structure so you can easily copy/paste the html output in a spellingchecker. This is convenient if you like to develop your posts directly in html, and do the spelling checks afterwards.

```bash
myclick clean-html <your-file.html>
```

This command will automatically open a new browser window with the cleaned html file.

[my_website]: https://www.ernst-bolle.com
[click]: https://click.palletsprojects.com/en/8.0.x/
[click-setuptools]: https://click.palletsprojects.com/en/8.0.x/setuptools/
