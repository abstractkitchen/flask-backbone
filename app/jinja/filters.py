"""
https://flask.palletsprojects.com/en/2.2.x/templating/#registering-filters

Check list of default Jinja filters
https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-builtin-filters
"""

from flask import Flask


# this is example filter
# {% for x in mylist | reverse %}
# {% endfor %}
def reverse_filter(s: list) -> list:
    return s[::-1]


# Add your filters
def register_filters(app: Flask) -> Flask:
    app.jinja_env.filters['reverse']: list = reverse_filter

    return app
