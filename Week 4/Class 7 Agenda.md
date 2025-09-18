# Class 7 – Loops and Collections

---

## Learning Objectives (show these briefly)

- Use **while** and **for** loops to repeat actions.
- Use **`range()`** to generate numbers to loop over (what it is, how to read it, and why it’s useful).
- Treat **strings, lists, and tuples** as sequences you can index, slice, and iterate.
- Apply **loop control** (`break`, `continue`, `pass`) for fine-grained behavior.

---

## Class Flow (planned timings)

1. Review Conditionals – 20 min
2. Loops: while → for – 25 min
3. `range()` and loop control – 15 min
4. Sequences: strings, lists, tuples – 25 min
5. Wrap + assign Week 4 exercises + preview Assignment 2 – 15 min

---

## 1) Review of Conditionals (20 min)

**Talking points (keep tight):**

- Conditionals = decision making; only one branch of an if/elif/else chain runs.
- **Indentation matters**: code under a condition must be indented exactly.
- **`==` vs `=`**: comparison vs assignment.
- Boolean expressions (`<`, `>`, `==`, `!=`, `<=`, `>=`, `in`) drive branches.

**Demo 1 — if/else**

```python
temperature = 5
if temperature < 0:
    print("It's freezing!")
else:
    print("It's above freezing.")
```

**Emphasize:** The expression after `if` must evaluate to **True** to run that block.

**Demo 2 — chained conditions**

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: Pass")
else:
    print("Grade: Fail")
```

**Prompt:** “What prints if `score = 95`? If `score = 50`?” (Only one branch executes.)

---

## 2) Loops: Why, When, and Two Types (25 min)

### Why loops?

- To repeat actions without copy/paste.
- Two main loop types in Python:
  - **`while`**: repeats **while a condition remains true** (condition-controlled).
  - **`for`**: repeats **over items in a sequence** (or a `range`).

---

### A. `while` loops (beginner framing)

**What it is:** Repeats its body **as long as** the condition is True.  
**Beginners’ rule of thumb:** A `while` loop needs three pieces:

1. **Initialization** (set up a variable before the loop)
2. **Condition** (checked at the top every time)
3. **Progress** (change something inside the loop so the condition will eventually be False)

**Demo — counting up (safe termination)**

```python
count = 0                # 1) initialize
while count < 5:         # 2) condition (will eventually be False)
    print("Count is", count)
    count += 1           # 3) progress (prevents infinite loop)
```

**Callouts (say out loud):**

- “If I forget `count += 1`, this becomes an **infinite loop**.”
- “Use `Ctrl+C` (terminal) to stop an accidental infinite loop.”
- “Use a `while` loop when you **don’t know** how many repeats you’ll need.”

**Demo — input loop with a **sentinel** (‘done’)**

```python
while True:
    text = input('Enter something (or "done" to stop): ')
    if text.lower() == "done":
        print("Thanks—stopping now.")
        break                # exit immediately
    print("You entered:", text)
```

**Emphasize:**

- Pattern: `while True: ... if <done>: break` is a **clean, beginner-friendly** input loop.
- `break` exits the loop right away.

---

### B. `for` loops (beginner framing)

**What it is:** Repeats once for **each item** in a sequence (string/list/tuple) or for **each number** from `range()`.

**Demo — fixed repeats with `range()` (preview, details next section)**

```python
for i in range(5):
    print("i is", i)
```

**NOTE:** It's ok to use a one letter variable here by convention `i` stands for iterator.
**Say:** “`i` takes each value from the sequence returned by `range(5)`.”  
**When to choose `for`:** When you **know** the items/length in advance (iterate through them).

---

## 3) `range()` and Loop Control (15 min)

### What is `range()` (beginner friendly)

- **`range()` is a built-in function** that produces a special, efficient **sequence of integers** you can loop over.
- It **does not** create a list by default (it returns a _range object_, which is iterable).
- You’ll commonly use it in `for` loops to run code a specific number of times.

**Reading `range()`:**

- `range(stop)` → `0, 1, 2, ..., stop-1`
- `range(start, stop)` → `start, start+1, ..., stop-1`
- `range(start, stop, step)` → counts by `step` (can be negative)

**Demos — read out loud while running:**

```python
for i in range(5):
    print(i)            # 0 1 2 3 4
```

> “Starts at 0. Stop is **exclusive** (5 is not printed).”

```python
for i in range(2, 6):
    print(i)            # 2 3 4 5
```

> “Start is included, stop is excluded.”

```python
for i in range(0, 10, 2):
    print(i)            # 0 2 4 6 8
```

> “Third argument is the step—here we’re printing evens.”

```python
for i in range(10, 0, -3):
    print(i)            # 10 7 4 1
```

> “A negative step counts down.”

**Common beginner pitfalls:**

- Expecting the stop value to be included (it **isn’t**).
- Forgetting that step defaults to `1`.
- Using `range(a, b)` with `a >= b` (results in **no iterations** if step is positive).

---

### Loop control statements (keep concrete)

```python
# break: exit the loop immediately
for n in range(10):
    if n == 5:
        break
    print(n)
print("Loop ended at n == 5")
```

```python
# continue: skip just this iteration, keep looping
for n in range(5):
    if n == 2:
        continue
    print(n)     # prints 0, 1, 3, 4 (skips 2)
```

```python
# pass: do nothing (placeholder to keep code valid)
for _ in range(3):
    pass  # useful while stubbing out code
```

**Teaching Side-Note on \_:**

- The underscore (\_) is not special syntax — it’s just a variable name.
- By convention, Python programmers use \_ to mean “I don’t care about this value.”
- In for _ in range(3):, Python still assigns 0, 1, 2 to _, but we don’t use it.
- This signals to human readers: “We’re looping 3 times, but we don’t care about the counter.”

**When to use which:**

- **`break`** when you’ve found what you needed or must stop early.
- **`continue`** to **skip** bad/irrelevant items but keep going.
- **`pass`** when you need a syntactically valid block that does nothing (planning ahead).

---

## 4) Sequences/Collections: Strings, Lists, Tuples (25 min)

> Core idea: **A loop is only half the story; you need something to loop over**. Sequences are that “something.” They are **ordered** collections that support **indexing, slicing, and iteration**.

### Strings (text)

- **Ordered** sequence of characters.
- **Immutable** (you can’t change characters in-place).
- Support **indexing/slicing** and **iteration**.

**Indexing & slicing demo**

```python
message = "Hello"
print(message[0])    # 'H'  (first char)
print(message[-1])   # 'o'  (last char)
print(message[1:4])  # 'ell' (slice from index 1 up to, not including, 4)
```

**Iteration demo (each character)**

```python
for char in "banana":
    print(char)
```

**Mini-task (class prompt):** “Count vowels in a word.”

```python
text = "programming"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)
```

**Emphasize:** Using `in` with strings; great example of scanning a sequence.

---

### Lists (mutable collections)

- Store **ordered, changeable** collections (any types).
- Support **append**, assignment, deletion, iteration.

**Basics + iteration**

```python
colours = ["red", "green", "blue"]
for colour in colours:
    print(colour)
```

**Modify**

```python
colours.append("yellow")   # add to end
colours[1] = "teal"        # change by index
del colours[0]             # remove by index
print(colours)
```

**Common pitfalls:**

- **IndexError** when using an index that doesn’t exist.
- Modifying a list **while** iterating over it (advanced: often better to build a new list or iterate over a copy).

---

### Tuples (immutable collections)

- Look like lists, but **can’t be changed** after creation.
- Good for “fixed” groupings (coordinates, settings).

**Access**

```python
point = (10, 20)
print(point[0])   # 10
print(point[1])   # 20
# point[0] = 99   # TypeError: tuples are immutable
```

**Unpacking (nice to show once)**

```python
x, y = point
print(x, y)
```

**Key takeaway:**

- **Mutable**: lists (you can change).
- **Immutable**: strings, tuples (you can’t change; you make new ones).

---

## 5) Bringing It Together → In-Class Mini Demos (5–10 min total)

**Demo A — Sum of the first 10 integers**

```python
total = 0
for num in range(1, 11):   # 1..10 inclusive
    total += num
print("Total:", total)
```

**Point:** Using `range(start, stop)` and accumulation.

**Demo B — Filter a list with `continue`**

```python
scores = [88, -1, 92, 79, -5, 93]
valid = []
for score in scores:
    if score < 0:
        continue          # skip invalid
    valid.append(score)
print("Valid scores:", valid)
```

**Point:** Data validation pattern; keep looping but skip bad entries.

**Bridge to Assignment 2 (Mini Arcade Scoreboard):**

- We’ll collect **(name, score)** pairs, store in a **list of tuples**, and compute **summary statistics** using loops.
- The patterns you just saw (input loop with `break`, `continue` for skipping invalid entries, iterating over sequences) are exactly what you’ll use.

---

## Assign the Week 4 Exercises (end of class)

Remind them the exercises focus on:

- While loops (with safe termination)
- For loops + `range()`
- Loop control (`break`, `continue`, `pass`)
- Strings/lists/tuples basics (indexing, iterating, simple edits)

---

## Common Beginner Pitfalls (quick reference)

- **Infinite `while`**: No progress toward making the condition False.
- **Off-by-one with `range`**: Stop value is **exclusive**.
- **Forgetting to convert input**: `input()` returns a string; use `int()`/`float()` when needed.
- **Modifying lists during iteration**: Can skip items or cause surprises—prefer building a new list.
- **String immutability**: You can’t do `s[0] = 'X'`; build a new string.

---

## Quick Glossary (keep handy)

- **Loop**: Repeats code multiple times.
- **`while` loop**: Repeats while a condition is True; needs init/condition/progress.
- **`for` loop**: Repeats once per item in a sequence (or per number from `range()`).
- **`range()`**: Built-in function that produces an efficient integer sequence for looping (start inclusive, stop exclusive, optional step).
- **Sequence**: Ordered collection supporting indexing/slicing/iteration (strings, lists, tuples).
- **Mutable vs Immutable**: Lists are mutable; strings/tuples are immutable.
- **`break`/`continue`/`pass`**: Control loop flow (exit early / skip iteration / do nothing).
