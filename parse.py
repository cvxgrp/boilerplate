#!.venv/bin/python
from pathlib import Path
import fire

from cvx.boilerplate.parse import toml_data, write, jinja_environment

def parse(file="pyproject.toml"):
    d = toml_data(file)
    env = jinja_environment(Path(__file__).parent / "contributions")

    template = env.get_template("ContributingTemplate.md")
    write(template, "CONTRIBUTING.md", **d)

    template = env.get_template("CodeOfConductTemplate.md")
    write(template, "CODE_OF_CONDUCT.md", **d)


if __name__ == '__main__':
    fire.Fire(parse)
