import db_settings
from .base import db
from . import user

db.bind(**db_settings.db_params)
db.generate_mapping(create_tables=True)