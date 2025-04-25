#    Copyright 2023 Stanford University Convex Optimization Group
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
from pathlib import Path

import fire
from loguru import logger

from .cooker.parse import jinja_environment, toml_data, write


def parse(file="pyproject.toml"):
    def f(source, target):
        logger.info(f"rendering template {source} to {target}")
        t = env.get_template(source)
        write(t, target, **data)

    logger.info(f"parsing toml file {file} in folder {Path(file).parent}")
    data = toml_data(file)
    for key, value in data.items():
        logger.info(f"  {key}: {value}")

    assert "authors" in data, "authors must be specified in pyproject.toml"
    assert "name" in data, "name must be specified in pyproject.toml"


    env = jinja_environment(Path(__file__).parent)
    logger.info("Jinja environment created")

    book = Path("book/docs")
    book.mkdir(exist_ok=True, parents=True)
    sphinx = Path("book/sphinx")
    sphinx.mkdir(exist_ok=True, parents=True)

    f("templates/contributions/CONTRIBUTING.md", "CONTRIBUTING.md"),
    f("templates/contributions/CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.md")
    f("templates/book/_config.yml", "book/_config.yml")
    f("templates/book/docs/api.md", book / "api.md")
    f("templates/book/docs/reports.md", book / "reports.md")
    f("templates/readme/README.md", "README2.md")


def main():
    fire.Fire(parse)
