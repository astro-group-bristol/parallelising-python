---
marp: true
---

# Parallelizing Code in Python
Dev Group
https://github.com/astro-group-bristol/parallelising-python

Sept 2024
Rhys & Claude

---
## Objective of the session

- Expose everyone to some 'easy' methods for getting a code preformance boots.
- Get everyone able to parallelise some simple code.
- Get everyone able to do some GPU code.

---
## Plan

- Quick intro to some routes in python
- demo of some examples of where you might want to implenent these features.
- Some time to experiement for yourself with this code or your own.

---

## Why Parallelize?

- Improve performance.
- Utilize multi-core processors.
- Handle multiple tasks simultaneously.
- Reduce execution time for CPU-bound tasks.

---

## When to Parallelize

- CPU-intensive operations.
- Independent tasks.
- Large data processing.
- Simulations and numerical computations.

---

## Tools for Parallelization in Python

1. multiprocessing
3. Numba
3. Cupy (GPU)
---

## multiprocessing

- Uses separate processes
- Bypasses Global Interpreter Lock (GIL)
- Ideal for CPU-bound tasks
- Example:

```python
from multiprocessing import Pool

def process_item(item):
    # CPU-intensive task here
    return result

with Pool() as p:
    results = p.map(process_item, items)
```
---
## Parallel Numba

- Supports parallel execution of loops
- Use `prange` for parallel loops
Example:
```python
from numba import njit, prange

@njit(parallel=True)
def process_items(items):
    results = []
    for i in prange(len(items)):
        # CPU-intensive task here
        results.append(result)
    return results

results = process_items(items)
```

- Can achieve significant speedups for loop-heavy computations.
- Easy to integrate with existing Numba code.
- Ideal for data-parallel tasks.s

---
## Numba

- Just-in-time (JIT) compiler
- Translates Python functions to optimized machine code
- Ideal for numerical computations
Example:

```python
from numba import jit

@jit(nopython=True)
def process_item(item):
    # CPU-intensive task here
    return result

results = [process_item(item) for item in items]
```

- Easy to use with minimal code changes
- Supports NumPy arrays and functions
- Can achieve significant speedups
---

## CuPy
https://docs.cupy.dev/en/stable/index.html
- GPU array library
- Drop-in replacement for NumPy & scipy (not every function is supported)
- Ideal for GPU-accelerated computing
- Example:

```python
import cupy as cp
# Create a CuPy array
x = cp.array([1, 2, 3, 4, 5])
# Perform operations on the GPU
y = cp.square(x)
print(y)  # Output: [ 1  4  9 16 25]
```

- Supports a wide range of NumPy functions
- Easy to integrate with existing NumPy code

---

## Best Practices
- SET YOUR MAX CORES!!!!!!!!!!!!!!!!!!
- Choose the right tool for the job
- Be aware of overhead
- Consider data sharing and synchronization
- Test and profile your code
- Start with simple parallelization and iterate
- experiment with multiple options to see if the overhead for you is worth it.

---

## Examples ....

---

## Your Turn to have a go