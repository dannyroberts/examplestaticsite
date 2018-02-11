import jinja2
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')

def build():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
        autoescape=jinja2.select_autoescape(['html', 'xml']),
    )
    for page in ['home', 'cv']:
        template = env.get_template('{page}.html.j2'.format(page=page))
        output = template.render(active_page=page)
        with open('{page}.html'.format(page=page), 'w') as f:
            f.write(output)


if __name__ == '__main__':
    build()