__author__ = 'Scott'

import os

# import django
# django.setup()


def populate():
    python_cat = add_cat('Python', 128, 64)

    add_page(cat=python_cat, title="Official Python Tutorial", url="http://docs.python.org/2/tutorial")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    add_page(cat=python_cat, title="Test1", url="http://www.google.com")
    add_page(cat=python_cat, title="Test2", url="http://www.live.com")
    add_page(cat=python_cat, title="Test3", url="http://www.msn.com")

    django_cat = add_cat("Django", 64, 32)

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks", 32, 16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

    cat_ex1 = add_cat("Movies", 50, 17)
    cat_ex2 = add_cat("Computers", 190, 65)
    cat_ex3 = add_cat("Aquaponics", 70, 40)
    cat_ex4 = add_cat("Boom Box", 90, 35)


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, vw=0, lks=0):
    c = Category.objects.get_or_create(name=name, views=vw, likes=lks)[0]
    return c

if __name__ == '__main__':
    print("Starting Rango Population script . . .")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tango_With_Django.settings')
    from rango.models import Category, Page
    populate()