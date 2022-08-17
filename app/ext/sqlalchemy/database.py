# More on this stuff
# https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/
# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#session-getting


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.ext.sqlalchemy.base_query import BaseQuery


# create empty session for future usage
db_session = scoped_session(sessionmaker())


def init_database(app):
    engine = create_engine(
        app.config.get("SQLALCHEMY_DATABASE_URI"),
        echo=app.config.get("SQLALCHEMY_ENGINE_ECHO")
    )

    db_session.configure(
        bind=engine,
        autocommit=app.config.get("SQLALCHEMY_AUTOCOMMIT"),
        autoflush=app.config.get("SQLALCHEMY_AUTOFLUSH"),
        query_cls=BaseQuery
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):

        # https://docs.sqlalchemy.org/en/14/orm/contextual.html#using-thread-local-scope-with-web-applications
        db_session.remove()
