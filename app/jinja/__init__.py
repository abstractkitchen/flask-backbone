from app.jinja.filters import register_filters
from app.jinja.context_processor import register_context_processor


def register_jinja_mapping(app):
    register_filters(app)
    register_context_processor(app)
