

```python
x = Variable(7.0)
y = Variable(10.0)

z = x*y
print(z.value)
z.backward()
print(x.d.value)
print(y.d.value)
```

Prints 70.0, then 10.0 and then 7.0.
