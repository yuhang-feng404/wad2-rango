import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rango_project.settings')

import django
django.setup()

from rango.models import Category, Page
from django.template.defaultfilters import slugify


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 15},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 12},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 8}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 20},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 5},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 18}
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 3},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 25}
    ]

    cats = {
        'Python': {'pages': python_pages, 'likes': 64},
        'Django': {'pages': django_pages, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'likes': 16}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['likes'])

        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    print("Database populated successfully!")


def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.slug = slugify(name)
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
