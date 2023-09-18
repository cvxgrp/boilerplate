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
from loguru import logger

import fire

from cvx.cooker.parse import toml_data, write, jinja_environment


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
    f("templates/contributions/ContributingTemplate.md", "CONTRIBUTING.md"),
    f("templates/contributions/CodeOfConductTemplate.md", "CODE_OF_CONDUCT.md")
    f("templates/book/_configTemplate.yml", "book/_config.yml")
    f("templates/book/sphinx/confTemplate.py", "book/sphinx/conf.py")
    f("templates/readme/readmeTemplate.md", "README2.md")


def main():
    fire.Fire(parse)
