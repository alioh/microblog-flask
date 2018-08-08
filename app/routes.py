from app import micro

@micro.route('/')
@micro.route('/index')

def index():
    return('Hello, World!')