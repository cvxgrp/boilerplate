from cvx.boilerplate.parse import toml_data, write, jinja_environment

if __name__ == "__main__":
    d = toml_data()
    env = jinja_environment()

    template = env.get_template("book/_configTemplate.yml")
    write(template, "_config.yml", **d)

    template = env.get_template("book/sphinx/confTemplate.py")
    write(template, "conf.py", **d)
