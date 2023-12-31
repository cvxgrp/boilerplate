from cvx.cooker.parse import toml_data, jinja_environment, write
from cvx.cook import parse
from jinja2 import environment


def test_load_data(resource_dir):
    d = toml_data(resource_dir / "data.toml")
    assert d["name"] == "test"
    assert d["authors"][0] == "Peter Maffay"
    assert d["packages"][0]["include"] == "cvx"


def test_environment(resource_dir):
    env = jinja_environment(resource_dir / "docs")
    assert isinstance(env, environment.Environment)


def test_write(resource_dir, tmp_path):
    data = toml_data(resource_dir / "data.toml")
    env = jinja_environment(resource_dir / "docs")
    source = env.get_template("test.md")
    write(template=source, output_file=tmp_path / "index.md", **data)


def test_cook(resource_dir):
    print(resource_dir.parent.parent)
    parse(resource_dir.parent.parent / "pyproject.toml")
