from flask import Flask
import setting

app = Flask(__name__)
app.config.from_object(setting)


@app.route('/')
def hello_world():
    return 'Hello World!' \
           '你好'


if __name__ == '__main__':
    app.run()
