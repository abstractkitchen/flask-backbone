from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.dialects.postgresql.base import INTEGER

from app.ext.sqlalchemy.base_query import BaseQuery

from app.utils import camel_to_snake


def id_column():
    return Column(
        INTEGER,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True
    )


def int_fk_column(foreign_key):
    return Column(INTEGER, ForeignKey(foreign_key))


def has_column(cls, column_name):
    return column_name in list(cls.__table__.columns.keys())


def search_i18n(i18n, lang_code):
    value = None

    if not i18n:
        return None

    if lang_code not in i18n:
        if "en" in i18n:
            value = i18n["en"]

    else:
        value = i18n[lang_code]

    return value


class _BaseModel(object):
    """
    this model will be used as a base for our future models
    you can customize with some boilerplate methods and/or properties
    you can also create multiple base models for different purposes

    With this configuration you can define your new models without __tablename__ parameter,
    but class name must be the same as a table name

    # for a table "currency"
    class CurrencyModel(BaseModel):
        ...

    # for a table "user_profile"
    class UserProfileModel(BaseModel):
        ...

    """

    query_class = BaseQuery
    query = None

    @declared_attr
    def __tablename__(cls):
        return camel_to_snake(cls.__name__).replace('_model', '')


BaseModel = declarative_base(cls=_BaseModel)
