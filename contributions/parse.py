import codecs
from json import load
from pathlib import Path

import toml
from jinja2 import Template, Environment, FileSystemLoader


def write(file, output_file, **kwargs):
    # output the file
    folder = Path(__file__).parent
    
    environment = Environment(loader=FileSystemLoader(folder))
    template = environment.get_template(file)
    
    output_file = codecs.open(folder.parent / output_file, "w", "utf-8")
    # template = Template(folder / file, trim_blocks=True)
    output_file.write(template.render(**kwargs))
    output_file.close()


if __name__ == "__main__":
    
    #environment = Environment(loader=FileSystemLoader("tmp/"))
    #template = environment.get_template("message.txt")
    
    
    root = Path(__file__).parent.parent
    d = toml.load(root / "pyproject.toml")
    name = d["tool"]["poetry"]["name"]
    repo = d["tool"]["poetry"]["repository"]

    write("Contributing.md", "CONTRIBUTING.md", package=name, repo=repo)
    write("CodeOfConduct.md", "CODE_OF_CONDUCT.md", package=name, repo=repo)
