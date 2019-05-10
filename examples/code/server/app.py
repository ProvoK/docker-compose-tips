from flask import Flask
from redis import Redis

app = Flask(__name__)


def counter_greet(counter):
    def greet():
        # return f'GoT deaths {counter() ** 3}!'
        return f'Hello! You are the {counter()} visitor!'
    return greet


def create_counter(count_key: str, redis_host: str, redis_port: int):
    client = Redis(host=redis_host, port=redis_port)

    def inner():
        return client.incr(count_key)

    return inner


def create_app(options):
    app = Flask('My App')
    counter = create_counter(**options)
    app.add_url_rule('/', view_func=counter_greet(counter))

    return app
