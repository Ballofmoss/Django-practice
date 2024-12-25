class InfiniteRange:
    def __init__(self, start: int):
        self.start = start

    def __next__(self):
        self.start += 1
        return self.start
    
    def __iter__(self):
        return self
    
# ir = InfiniteRange(1)

# for i in ir:
#     print(i)

class Fibonachi:
    prev: int = 0
    current: int = 1
    def __init__(self, end: int):
        self.end = end

    def __next__(self):
        # prev = self.prev
        
        # self.prev = self.current
        if((self.current + self.prev) < self.end):

            prev = self.current
            self.current = self.prev + self.current
            self.prev = prev

            # self.current += prev
            return self.current
        else:
            raise StopIteration
    
    def __iter__(self):
        return self
    
f = Fibonachi(100)

for i in f:
    print(i)

class Multiplier:
    prev: float = 0
    def __init__(self, multiplier: float):
        self.multiplier = multiplier
    
    def __next__(self):
        self.prev += multiplier
        return self.prev

# 1. Что такое итератор в Python?
# Класс который реализует метод __next__

# 2. Чем итерируемый объект отличается от итератора?
# итер объект это экземпляр класса-итератора

# 3. Как остановить итерацию внутри метода __next__?
# raise StopIteration
        
        


