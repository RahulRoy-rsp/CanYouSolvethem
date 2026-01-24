# Square Spread (Boundary Coordinates)

## **Problem Statement**

You are given:

* A starting point **`start_point`** on a 2D grid represented as a **tuple `(x, y)`**
* A positive integer **`spread`**

Your task is to generate **all coordinate points that lie on the boundary of a square** centered at the given starting point, where each side of the square extends `spread` units away from the center in all four directions.

---

## **Detailed Explanation**

For the given:

* `start_point = (x, y)`
* `spread = s`

The square boundary lies at:

* **Top side:** all points where `y = y + s`, and `x` ranges from `(x - s)` to `(x + s)`
* **Bottom side:** all points where `y = y - s`, and `x` ranges from `(x - s)` to `(x + s)`
* **Left side:** all points where `x = x - s`, and `y` ranges from `(y - s + 1)` to `(y + s - 1)` (corners excluded to avoid duplicates)
* **Right side:** all points where `x = x + s`, and `y` ranges from `(y - s + 1)` to `(y + s - 1)`

You must combine these into a **set of tuples** representing all the boundary coordinates.

---

# **Example Test Cases**

---

## **Test Case 1**

### **Input:**

```python
start_point = (0, 0)
spread = 2
```

### **Output:**

```
{
 (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2),
 (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2),
 (-2, -1), (-2, 0), (-2, 1),
 (2, -1), (2, 0), (2, 1)
}
```

### **Explanation:**

* Top boundary at y = 2
* Bottom boundary at y = -2
* Left boundary at x = -2
* Right boundary at x = 2
* Then All boundary points are collected to form the output.

---

## **Test Case 2**

### **Input:**

```
start_point = (3, 4)
spread = 1
```

### **Output:**

```
{
 (2, 5), (3, 5), (4, 5),
 (2, 3), (3, 3), (4, 3),
 (2, 4),
 (4, 4)
}
```

### **Explanation:**

* Square extends one unit in all directions
* Top row: y = 5, x from 2 → 4
* Bottom row: y = 3, x from 2 → 4
* Left side: only (2, 4)
* Right side: only (4, 4)

---

## **Test Case 3**

### **Input:**

```
start_point = (-1, -1)
spread = 3
```

### **Output:**

```
{
 (-4, 2), (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2),
 (-4, -4), (-3, -4), (-2, -4), (-1, -4), (0, -4), (1, -4), (2, -4),
 (-4, -3), (-4, -2), (-4, -1), (-4, 0), (-4, 1),
 (2, -3), (2, -2), (2, -1), (2, 0), (2, 1)
}
```

### **Explanation:**

* The center is at (-1, -1), spreading 3 units in each direction
* Top boundary at y = 2
* Bottom boundary at y = -4
* Left boundary at x = -4
* Right boundary at x = 2

---

## **Test Case 4**

### **Input:**

```
start_point = (5, -3)
spread = 0
```

### **Output:**

```
{ (5, -3) }
```

### **Explanation:**

A spread of 0 means the "square" degenerates into a single point — the center itself.

---


