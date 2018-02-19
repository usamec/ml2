Build a simple autograd engine, supporting following features:

* Creation of scalar variables (no vectors or matrices needed)
* Simple arithmetical operations plus, minus, multiplication, division with your scalar values or number constants. Each operation produces a new variable.
* Calculating derivatives of all inputs for given variable.
* Advanced operations: exp, log, tanh, sigmoid for given input
* Bonus point: Higher order derivatives

Your code should have class Variable containing most of the logic.
Variable should be created as follows: `x = Variable(47.42)`.
Doing aritmetic operation should look like this:

```python
x = Variable(2.0)
y = Variable(5.0)
x2 = 2*x
z = x2 + y
```

We should be also able to inspect the value of Variable:

```python
x = Variable(2.0)
x2 = 2*x
print(x.value)     # Should be 2.0
print(x2.value)    # Should be 4.0
```

Calculate of derivatives should be called explicitly on required variable by backward method.
Each input variable should have `d` member, which contains required derivative in value property.

```python
x = Variable(7.0)
y = Variable(10.0)
z = Variable(1.0)

q = x*y
a = q + 3*z + x
print(a.value)     # Prints 80.0
a.backward()       # Calculates da / dx, da / dy, da / dz, dq / dz
print(x.d.value)   # Prints 11.0
print(y.d.value)   # Prints 7.0
print(z.d.value)   # Prints 3.0
print(q.d.value)   # Prints 1.0
```

### Grading

For 50% of points your code should be able to calculate first order derivatives of any expression containing plus, minus and multiplication (whole file test1.py, TODO link).
Otherwise your score is: % tests passed in test2.py + % of tests passed in bonus.py.  
