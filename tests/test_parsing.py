from cvx.boilerplate.parse import toml_data


def test_load_data(resource_dir):
    d = toml_data(resource_dir / "data.toml")
    assert d["name"] == "test"
    assert d["authors"][0] == "Peter Maffay"
    assert d["packages"][0]["include"] == "cvx"
