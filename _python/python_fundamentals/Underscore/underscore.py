class Underscore:
    def map(self, iterable, callback):
        result = []
        for i in iterable:
            result.append(callback(i))
        return result
    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return iterable[i]
    def filter(self, iterable, callback):
        result = []
        for i in iterable:
            if callback(i):
                result.append(i)
        return result
    def reject(self, iterable, callback):
        result = []
        for i in iterable:
            if not callback(i):
                result.append(i)
        return result

_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)