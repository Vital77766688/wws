import functools
import json

def to_json(func):
    @functools.wraps(func)
    def new_get_data(*args, **kwargs):
        data = func(*args, **kwargs)
        return json.dumps(data)

    return new_get_data


@to_json
def get_data(*args, **kwargs):
    return {
        'data' : 42
    }

if __name__ == '__main__':

    print(get_data.__name__)
    print(get_data())