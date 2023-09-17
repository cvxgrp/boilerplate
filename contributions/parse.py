import codecs
from pathlib import Path

from cvx.boilerplate.parse import jinja_environment, toml_data


def write(file, output_file, **kwargs):
    # output the file
    folder = Path(__file__).parent
    template = jinja_environment(folder).get_template(file)
    
    output_file = codecs.open(folder.parent / output_file, "w", "utf-8")
    output_file.write(template.render(**kwargs))
    output_file.close()


if __name__ == "__main__":
    d = toml_data()
    write("Contributing.md", "CONTRIBUTING.md", **d)
    write("CodeOfConduct.md", "CODE_OF_CONDUCT.md", **d)
