class IterableGenerator:
    def __iter__(self):
        return self.generator()

    def generator(self):
        # Генераторний код
        for i in range(5):
            yield i


iterable = IterableGenerator()

for value in iterable:
    print(value)
