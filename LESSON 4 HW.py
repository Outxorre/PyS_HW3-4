#Task 2
import random

class Encryptor:
    def __init__(self, numbers):
        self._numbers = numbers

    def process(self):
        return sum(self._numbers) * random.randint(1, 10)

class AdvancedEncryptor(Encryptor):
    def __init__(self, numbers, modifier):
        super().__init__(numbers)
        self.modifier = modifier

    def process(self):
        return super().process() + self.modifier

basic = Encryptor([10, 5, 2])
print(basic.process())

advanced = AdvancedEncryptor([10, 5, 2], 10)
print(advanced.process())