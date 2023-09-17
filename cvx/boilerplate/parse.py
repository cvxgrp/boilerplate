import codecs

from jinja2 import FileSystemLoader, Environment
import toml


def toml_data(toml_file="pyproject.toml"):
    d = toml.load(toml_file)
    return d["tool"]["poetry"]

def jinja_environment():
    environment = Environment(loader=FileSystemLoader("."))
    return environment

def write(template, output_file, **kwargs):
    # output the file
    output_file = codecs.open(output_file, "w", "utf-8")
    output_file.write(template.render(**kwargs))
    output_file.close()