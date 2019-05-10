import os

import pytest
from redis import Redis

from app import create_counter


@pytest.fixture
def key():
    return 'myapp.greet.counter.test'


@pytest.fixture(autouse=True, scope='function')
def unset_key(key):
    client = Redis(os.environ['REDIS_HOST'], 6379)
    yield
    client.delete(key)


@pytest.mark.integration
def test_counter_returns_incremental_numbers(key):
    counter = create_counter(key, os.environ['REDIS_HOST'], 6379)

    for i in range(1, 100):
        assert i == counter()
