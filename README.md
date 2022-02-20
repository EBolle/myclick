# Myclick

This is my personal CLI which I have developed to easily maintain the content of [my website][my_website], and to explore and wrangle data from the command-line.

## Usage

Although the commands are specific to my use cases, they might be useful to you as well. After you cloned the repo it is best to create a virtual environment before executing the follow command.

```bash
pip install --editable .
```

You should now be able to execute commands directly from the command-line, which you can test with `myclick --help`. The CLI is created with [click][click], and they have additional documentation on the [setuptools integration][click-setuptools].

[my_website]: https://www.ernst-bolle.com
[click]: https://click.palletsprojects.com/en/8.0.x/
[click-setuptools]: https://click.palletsprojects.com/en/8.0.x/setuptools/
