from cvx.boilerplate.parse import toml_data, write, jinja_environment

if __name__ == "__main__":
    d = toml_data()
    env = jinja_environment()

    template = env.get_template("book/_config.yml")
    write(template, "_ccc.yml", **d)

    template = env.get_template("book/sphinx/conf.py")
    write(template, "conf.py", **d)
