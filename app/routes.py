from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Donny'}
    return '''
        <html>
            <head>
                <title>Homepage - Microblog </title>
            </head>
            <body>
                <h1>Hello, ''' + user['username'] + '''!</h1>
            </body>
        </html>
    '''
