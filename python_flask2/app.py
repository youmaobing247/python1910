from flask import Flask

app = Flask(__name__)
a=F
def hello_world():
    return 'Hello World!'
# @app.route('/')
app.add_url_rule("/",None,hello_world)



if __name__ == '__main__':
    app.run()
