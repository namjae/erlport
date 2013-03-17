from erlport import Atom, erlang

def switch(n):
    result = 0
    for i in range(n):
        result = erlang.call(Atom(b"python3_tests"), Atom(b"test_callback"),
            [result, i])
    return n

def identity(v):
    return v

def length(v):
    return len(v)

def print_string(s):
    print(s.to_string())

class TestClass(object):
    class TestSubClass(object):
        @staticmethod
        def test_method():
            return Atom(b"ok")