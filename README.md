# Flask-Backbone
#### _Your Next Flask Boilerplate_

![Create sitemaps with Sitemapa](https://abstractkitchen.com/static/flask-backbone/flask-backbone-boilerplate.jpg "Flask-Backbone")

## UPD: March 15, 2023
- Removed alembic from the codebase. You can install by yourself.
- Removed SQLAlchemy extensions to avoid unnecessary complexity in the blueprint. 
- Added .env support for the application config with from_prefixed_env. Check app.py for the details.
  - Access FLASK_MY_CONFIG_PROP as app.config.get("MY_CONFIG_PROP"). 
  - Priorities: .env > config/{env}.py > instance/config.py. Instance folder config is top priority.
- SQLAlchemy 2 support
- Added [Python Typing](https://docs.python.org/3/library/typing.html)
- Moved to Python 3.11

## Features
- Predefined basic structure, so you'll end up with a clean architecture.
- Database support via **SQLAlchemy**. However, you can skip database setup and use Flask-Backbone without the database. I also do not use Flask-SQLAlchemy, but you can.
- Development/Production/You own configs with **instance_relative_config**.
- Cache support via **flask_caching**. Setup easily with configuration.
- **Flask-Debug**
- **Sentry** support. Just add your DSN, and you're good to go.
- **Jinja** filters and custom variables.
- Designed to be **blueprint-first**. Keep your structure clean and steady with blueprints. Everything is a blueprint. Your future self will thank you.
- Interactive commands to create your next blueprint. Define your blueprint skeletons to speed up your development. To create your next blueprint simply run flask app create-blueprint. It's up to you and you can completely ignore or remove this part and everything will work perfectly fine.
- Initial setup with a configuration script.
- WSGI config

## Getting Started

**Note: Tested with Python 3.11**

**1 — Clone flask-backbone.**

`git clone https://github.com/abstractkitchen/flask-backbone.git .`

**2** — As a rule of thumb, make sure that you use a virtual environment. For example python3 -m venv pythonenv. This will create an environment in the folder pythonenv. I prefer to name my python environment as a pythonenv, because it's more descriptive.

`python3 -m venv pythonenv`

`. pythonenv/bin/activate`

`pip install -r requirements.txt`

**3** — Launch configure.py. It will ask you some question about your future setup.
`python configure.py`

This utility will create: .env and instance/config.py.


## Usage
Please read this article. You'll learn more details about the boilerplate and Flask.

[Read about usage on my website](https://abstractkitchen.com/blog/flask-backbone/).

## Contacts
- [visit abstractkitchen.com](https://abstractkitchen.com)
- drop me a line: dmitry@abstractkitchen.com
- [connect with me on reddit](https://www.reddit.com/user/denisberezovsky)

## License

MIT