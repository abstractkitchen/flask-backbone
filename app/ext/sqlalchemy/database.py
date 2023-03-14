# More on this stuff
# https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/
# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#session-getting

from flask import Flask
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, scoped_session


# create empty session for future usage
db_session: scoped_session = scoped_session(sessionmaker())


def init_database(app: Flask) -> None:
    engine: Engine = create_engine(
        app.config.get("SQLALCHEMY_DATABASE_URI"),
        echo=app.config.get("SQLALCHEMY_ENGINE_ECHO")
    )

    db_session.configure(
        bind=engine,
        autocommit=app.config.get("SQLALCHEMY_AUTOCOMMIT"),
        autoflush=app.config.get("SQLALCHEMY_AUTOFLUSH")
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None) -> None:

        # https://docs.sqlalchemy.org/en/14/orm/contextual.html#using-thread-local-scope-with-web-applications
        db_session.remove()
