from flask import Flask

from app.app import create_app


application: Flask = create_app()

if __name__ == "__main__":
    application.run(load_dotenv=True)
