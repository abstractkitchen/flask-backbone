from sqlalchemy import orm

from app.ext.sqlalchemy.pagination import Pagination


class BaseQuery(orm.Query):
    """
    Influenced by
    https://github.com/pallets-eco/flask-sqlalchemy/blob/main/src/flask_sqlalchemy/__init__.py

    Extend query class here with your own methods
    e.g db_session.query(Users).filter(Users.age > 30).paginate(2, 20)

    """

    def paginate(self, page, per_page=20, error_out=False):
        """Return `Pagination` instance using already defined query
        parameters.
        """
        if error_out and page < 1:
            raise IndexError

        items = self.limit(per_page).offset((page - 1) * per_page).all()

        if not items and page != 1 and error_out:
            raise IndexError

        # No need to count if we're on the first page and there are fewer items
        # than we expected.
        if page == 1 and len(items) < per_page:
            total = len(items)
        else:
            total = self.order_by(None).count()

        return Pagination(self, page, per_page, total, items)
