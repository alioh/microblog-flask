from app import micro, db
from app.models import User, Post

@micro.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}