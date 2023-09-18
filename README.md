# cvxboilerplate

This is code to automate the often tedious process of writing
boilerplate files such as

* README.md
* CONTRIBUTING.md
* CODE_OF_CONDUCT.md
* book/sphinx/conf.py
* book/_config.yml

All those files are created from Jinja2 templates, e.g.
the file 'book/_config.yml' is created from the template

```yaml
# Book settings
# Learn more at https://jupyterbook.org/customize/config.html

title: {{ name }}
author: {{ authors[0] }}
only_build_toc_files: true

execute:
  execute_notebooks: force
  timeout: 240

parse:
  myst_enable_extensions:
    - substitution
    - linkify
    - dollarmath
  myst_substitutions:
    book_url: {{ homepage }}

# needed for plotly
sphinx:
  config:
    html_js_files:
    - https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js

# Information about where the book exists on the web
repository:
  url: {{ repository }}
  path_to_book: book
  branch: main

# Add GitHub buttons to your book
# See https://jupyterbook.org/customize/config.html#add-a-link-to-your-repository
html:
  use_issues_button: true
  use_repository_button: true
  extra_navbar: Powered by <a href="https://jupyterbook.org">Jupyter Book</a>
  # Will be displayed underneath the left navbar.
```

The data in double curly braces is replaced by the data injected into the template.
We get the data from parsing the projects 'pyproject.toml' in the root of the repository.

Of course, we do not want to entertain the idea of having copies of all those
templates in all the repositories. Instead, we have this central repository
and every repository that wants to use this functionality adds in its Makefile
the job

```make
.PHONY: boil
boil: ## Update the boilerplate code
 @gh repo clone git@github.com:cvxgrp/boilerplate.git .tmp
 @cd .tmp  && poetry install -vv && cd ..
 @.tmp/.venv/bin/python .tmp/parse.py pyproject.toml
 @rm -rf .tmp
```
