from cvx.boilerplate.parse import toml_data, write, jinja_environment

if __name__ == "__main__":
    d = toml_data()
    env = jinja_environment()

    template = env.get_template("contributions/Contributing.md")
    write(template, "CONTRIBUTING.md", **d)

    template = env.get_template("contributions/CodeOfConduct.md")
    write(template, "CODE_OF_CONDUCT.md", **d)

