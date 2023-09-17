from jinja2 import Environment, FileSystemLoader
import toml


def jinja_environment(folder):
    environment = Environment(loader=FileSystemLoader(folder))
    return environment


def toml_data(toml_file="pyproject.toml"):
    d = toml.load(toml_file)
    return d["tool"]["poetry"]