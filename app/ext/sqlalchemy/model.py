from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.dialects.postgresql.base import INTEGER

from app.utils import camel_to_snake


def id_column() -> Column:
    return Column(
        INTEGER,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True
    )


def int_fk_column(foreign_key) -> Column:
    return Column(INTEGER, ForeignKey(foreign_key))


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

    @declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__).replace('_model', '')


BaseModel = declarative_base(cls=_BaseModel)
