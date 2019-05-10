from app import counter_greet


def test_counter_greet():
    gen = (x for x in range(10000))
    greeter = counter_greet(lambda: next(gen))
    assert '0' in greeter()
    assert '1' in greeter()
