# Conceptual Questions

### 1. Write the format of a conditional using the following:
You might not need to use all and can use any multiple times: `if`, `else`, `==`, `<condition>`, `False`, `True`, `<do something>`.

### 2. Write the format of a conditional using the following:
You might not need to use all and can use any multiple times: `while`, `<condition>`, `==`, `False`, `True`, `<do something>`.

### 3. What does the condition of a conditional have to evaluate to in order to enter its block?

### 4. What happens when a return statement is encountered?

---

All subquestions of this problem will refer to this pseudo code snippet:

```python
if <condition1>:
    <do something>
elif <condition2>:
    <do something>
else:
    <do something>
```

### 5. From the general format of a conditional with an `elif` block, what needs to be True and/or False in order for the `elif` block to evaluate?

### 6. Is `<condition1>` not being met the same as having `if <condition1> == False:`?

---

All subquestions of this problem will refer to this code snippet:

```python
def main() -> None: 
    x: str = "x"
    y: str = "y"
    z: str = x
    y = x
    x = "y"

    if not(x != y and x != "y"):
        print(f"x: {x}")
    else:
        print("'if' condition not met.")

main()
```

### 7. What is the condition in this code?

### 8. What does the condition evaluate to? (Don’t do it in your head, draw a memory diagram!)

### 9. What values should x, y, and/or z have to be assigned to in order for the else block to run?

### 10. What other values can x, y, and/or z be assigned in order for the `if` block to run?

---

# Solutions 

## Conceptual Questions - Solutions

### Solution 1:
```python
if <condition> == True:
    <do something>
else:
    <do something>
```
OR
```python
if <condition>:
    <do something>
else:
    <do something>
```

### Solution 2:
```python
while <condition> == True:
    <do something>
```
OR
```python
while <condition>:
    <do something>
```

### Solution 3:
The condition must always evaluate to `True`.

### Solution 4:
The return value is recorded in memory and the function is immediately exited.

### Solution 5:
`<condition1>` must not be met (condition should evaluate to `False`) AND `<condition2>` must be met (condition should evaluate to `True`).

### Solution 6:
In this case, yes. If we had something like this:
```python
if ("hello" == "hello") == False:
```
the `<condition>` in this case would be everything in between the `if` and the `:`. In the pseudo-code, we are separating the `<condition>` to be separate from the rest (`== False`), while in real code the condition is always everything after the `if` and before the `:`.

---

### Solution 7:
`not(x != y and x != "y")`

### Solution 8:
The condition evaluates to `True`.

### Solution 9:
To ensure the `else` block runs in the given code, the condition `x != y and x != "y"` must be true. This means `x` should be different from `y` and `x` should also be different from the string `"y"`. For example, setting `x = "a"` and `y = "b"` will satisfy this condition, making the `else` block execute.

### Solution 10:
To make the `if` block run, the condition `not(x != y and x != "y")` must be true, which happens when `x` is either the same as `y` or the same as `"y"`, or both. In the original code where `x = "y"`, `y = "x"`, and `z = "x"`, the `if` block runs as `not(x != y and x != "y")` evaluates to true.

---