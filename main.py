class Obyekt:
    pass

class Obyekt2:
    pass

obyekt = Obyekt()
obyekt2 = Obyekt2()

print(type(obyekt))  # <class '__main__.Obyekt'>
print(type(obyekt2))  # <class '__main__.Obyekt2'>

print(isinstance(obyekt, Obyekt))  # True
print(isinstance(obyekt, Obyekt2))  # False
print(isinstance(obyekt2, Obyekt))  # False
print(isinstance(obyekt2, Obyekt2))  # True
```

```python
class Obyekt:
    pass

class Obyekt2(Obyekt):
    pass

obyekt = Obyekt()
obyekt2 = Obyekt2()

print(type(obyekt))  # <class '__main__.Obyekt'>
print(type(obyekt2))  # <class '__main__.Obyekt2'>

print(isinstance(obyekt, Obyekt))  # True
print(isinstance(obyekt, Obyekt2))  # False
print(isinstance(obyekt2, Obyekt))  # True
print(isinstance(obyekt2, Obyekt2))  # True
