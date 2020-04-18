from tinydb.database import Table

from .database import Database

db_settings: Database = Database('./settings.json')
users: Table = db_settings.table('users')
labels: Table = db_settings.table('labels')

db_images: Database = Database('./images.json')
images: Table = db_images.table('images')
