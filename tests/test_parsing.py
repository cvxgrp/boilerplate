from cvx.boilerplate.parse import toml_data, jinja_environment
from jinja2 import environment


def test_load_data(resource_dir):
    d = toml_data(resource_dir / "data.toml")
    assert d["name"] == "test"
    assert d["authors"][0] == "Peter Maffay"
    assert d["packages"][0]["include"] == "cvx"


def test_environment(resource_dir):
    env = jinja_environment(resource_dir / "docs")
    assert isinstance(env, environment.Environment)
