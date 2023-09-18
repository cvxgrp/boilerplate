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
import codecs

from jinja2 import FileSystemLoader, Environment
import toml


def toml_data(toml_file="pyproject.toml"):
    d = toml.load(toml_file)
    return d["tool"]["poetry"]


def jinja_environment(folder):
    environment = Environment(loader=FileSystemLoader(folder))
    return environment


def write(template, output_file, **kwargs):
    # output the file
    output_file = codecs.open(output_file, "w", "utf-8")
    output_file.write(template.render(**kwargs))
    output_file.close()
