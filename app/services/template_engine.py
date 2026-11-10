from jinja2 import Environment

env = Environment(autoescape=False)


def render(template_str, **ctx):
    return env.from_string(template_str).render(**ctx)
