import os

from app import create_app


options = {
    'redis_host': os.environ['REDIS_HOST'],
    'redis_port': os.environ.get('REDIS_PORT', 6379),
    'count_key': os.environ.get('REDIS_COUNTER_KEY', 'myapp.greet.counter'),
}
app = create_app(options)
