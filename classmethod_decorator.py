def classmethod_rewritten(meth):
    def inner(*arg, **kwargs):
         
        cls = cls.__class__
        return meth(cls, *arg, **kwargs)
    return inner

def staticmethod_rewritten(meth):
    def inner(self, *arg, **kwargs):
        print self, "will be removed"
        return meth(*arg, **kwargs)
    return inner


class RandomClass():
    @classmethod
    def some_other_method(self, a, b):
        print self
        return a + b
    @classmethod_rewritten
    def some_method(self, a, b):
        print self
        return a + b
    @staticmethod_rewritten
    def some_static_supposed_to_be_method(a, b):
        return a - b
print RandomClass.some_method(2, 2)
print RandomClass.some_other_method(2, 2)
#print RandomClass().some_static_supposed_to_be_method(2, 2)
#print RandomClass().some_method(2, 2)
