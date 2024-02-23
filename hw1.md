Build a simple autograd engine, supporting following features:

* Creation of scalar variables (no vectors or matrices needed)
* Simple arithmetical operations plus, minus, multiplication, and division with your scalar values or number constants. Each operation produces a new variable.
* Calculating derivatives of all inputs for given variable.
* Advanced operations: exp, log, tanh for given input

Your code should have class Variable containing most of the logic.
Variable should be created as follows: `x = Variable(47.42)`.
Doing arithmetic operations should look like this:

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

Calculate of derivatives should be called explicitly on the required variable by a backward method.
Each input variable should have a `d` member, which contains the required derivative in value property.

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

For 50% of points, your code should be able to calculate first-order derivatives of any expression containing plus, minus, and multiplication. If you fail this requirement, your number of points is zero.
Otherwise, your grade depends on a number of passed tests.

You are provided a set of files with unittests. [test1.py](https://raw.githubusercontent.com/usamec/ml2/master/test1.py) contains tests for plus, minus, and multiplication and calculating derivatives using them. [test2.py](https://raw.githubusercontent.com/usamec/ml2/master/test2.py) contains tests also other expressions. [test3.py](https://raw.githubusercontent.com/usamec/ml2/master/test3.py) contains slightly ugly computation, which might make poorly written autograd engine run much longer.
Your code might be graded on other tests, which are not visible to you right now. You can run unit tests as any other Python script.

You can expect that all Variables in tests would fall into a reasonable range, and there will be no gotchas for rounding errors, overflows, and similar phenomena.

## Limitations

No external libraries, only pure Python3 and its standard libraries (and numpy if you really insist).
Create file named `solution.py`, which makes unittests pass (and fulfills requirements stated above, i.e. does not have hardcode results). Do not edit unit test files! 

## Sending solution
Submit solution via classroom.
