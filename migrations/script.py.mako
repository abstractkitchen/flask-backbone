"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
import uuid
import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID, JSONB, INTEGER

${imports if imports else ""}
# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}
table_name = ''


def id_column():
    return sa.Column(
        'id',
        INTEGER,
        autoincrement=True,
        primary_key=True,
        nullable=False,
        unique=True
    )


def uuid_fk_column(name, foreign_key):
    return sa.Column(name, UUID(as_uuid=True), sa.ForeignKey(foreign_key))


def int_fk_column(name, foreign_key):
    return sa.Column(name, INTEGER, sa.ForeignKey(foreign_key))


def jsonb_field(name, default_value={}):
    return sa.Column(name, JSONB, default=lambda: default_value)


def upgrade():
    op.create_table(
        table_name,
        id_column()
    )


def downgrade():
    op.drop_table(table_name)