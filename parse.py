from pathlib import Path
from loguru import logger

import fire

from cvx.boilerplate.parse import toml_data, write, jinja_environment

def parse(file="pyproject.toml"):
    logger.info(f"parsing toml file {file} in folder {Path(__file__).parent}")
    d = toml_data(file)
    for key, value in d.items():
        logger.info(f"  {key}: {value}")

    env = jinja_environment(Path(__file__).parent / "contributions")
    logger.info("Jinja environment created")

    templates = [
        ("ContributingTemplate.md", "CONTRIBUTING.md"),
        ("CodeOfConductTemplate.md", "CODE_OF_CONDUCT.md")
    ]

    for template in templates:
        logger.info(f"rendering template {template[0]} to {template[1]}")
        t = env.get_template(template[0])
        write(t, template[1], **d)

    #template = env.get_template("CodeOfConductTemplate.md")
    #write(template, "CODE_OF_CONDUCT.md", **d)


if __name__ == '__main__':
    fire.Fire(parse)
