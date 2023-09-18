from pathlib import Path
from loguru import logger

import fire

from cvx.boilerplate.parse import toml_data, write, jinja_environment

def parse(file="pyproject.toml"):
    def f(source, target):
        logger.info(f"rendering template {source} to {target}")
        t = env.get_template(source)
        write(t, target, **data)

    logger.info(f"parsing toml file {file} in folder {Path(file).parent}")
    data = toml_data(file)
    for key, value in data.items():
        logger.info(f"  {key}: {value}")

    env = jinja_environment(Path(__file__).parent)
    logger.info("Jinja environment created")
    f("contributions/ContributingTemplate.md", "CONTRIBUTING.md"),
    f("contributions/CodeOfConductTemplate.md", "CODE_OF_CONDUCT.md")
    f("book/_configTemplate.yml", "book/_config.yml")
    f("book/sphinx/confTemplate.py", "book/sphinx/conf.py")
    f("readme/readmeTemplate.md", "README2.md")


if __name__ == '__main__':
    fire.Fire(parse)
