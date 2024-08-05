class Counter:
    def __init__(self):
        self.count = 0
        self.history = []
    
    def increment(self):
        self.count += 1
        self.history.append(('increment', self.count))
    
    def decrement(self):
        self.count -= 1
        self.history.append(('decrement', self.count))
    
    def get_count(self):
        return self.count
    
    def reset(self):
        self.count = 0
        self.history.append(('reset', self.count))
    
    def get_history(self):
        return self.history


counter = Counter()     # Creates a new EnhancedCounter object with count initialized to 0
counter.increment()             # Increases count by 1
print(counter.get_count())      # Should print 1
print(counter.get_history())    # Should print [('increment', 1)]
counter.decrement()             # Decreases count by 1
print(counter.get_count())      # Should print 0
print(counter.get_history())    # Should print [('increment', 1), ('decrement', 0)]
counter.reset()                 # Resets count to 0
print(counter.get_count())      # Should print 0
print(counter.get_history())    # Should print [('increment', 1), ('decrement', 0), ('reset', 0)]
