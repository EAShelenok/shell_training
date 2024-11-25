from inspect import getmodule

def introspection_info(obj):
    out_d = dict()
    out_d['type'] = str(type(obj)).split("'")[1]
    out_d['attributes'] = [item for item in dir(obj) if not callable(getattr(obj, item))]
    out_d['methods'] = [item for item in dir(obj) if callable(getattr(obj, item))]
    if getmodule(obj) is None:
        out_d['module'] = getmodule(obj)
    else:
        out_d['module'] = str(getmodule(obj)).split("'")[1]

    return out_d

class MyClass():
    def __init__(self, pow):
        self.first = 2
        self.pow = pow

    def my_pow(self):
        return self.first ** self.pow

if __name__ == '__main__':
    n = 45
    powering_ = introspection_info(MyClass(2))
    my_obj = MyClass(3)
    print(powering_)
    print(introspection_info(sum))
    print(introspection_info(list))
    print(introspection_info(my_obj))
    print(introspection_info(MyClass))
    print(introspection_info(n))