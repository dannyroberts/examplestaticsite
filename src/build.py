import jinja2
import os
from collections import namedtuple

Page = namedtuple('Page', ['name', 'title', 'background_image'])

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
PAGES = [
    Page(name='home', title='Home', background_image='home_background.jpg'),
    Page(name='cv', title='CV', background_image='cv_background.jpg'),
]

def build():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
        autoescape=jinja2.select_autoescape(['html', 'xml']),
    )
    for page in PAGES:
        template = env.get_template('{page}.html.j2'.format(page=page.name))
        output = template.render(current_page=page, PAGES=PAGES)
        with open('{page}.html'.format(page=page.name), 'w') as f:
            f.write(output)


if __name__ == '__main__':
    build()
