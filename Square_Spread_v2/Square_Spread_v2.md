# Square Spread (All Coordinates)

## **Problem Statement**

You are given:

* A starting point **`start_point`** on a 2D grid represented as a **tuple `(x, y)`**
* A positive integer **`spread`**

Your task is to generate **all coordinate points inside the square (including boundary)** centered at the given starting point, where each side of the square extends `spread` units away from the center in all four directions.

---

## **Detailed Explanation**

For the given:

* `start_point = (x, y)`
* `spread = s`

---

# **Example Test Cases**


## **Test Case 1**

### **Input:**

```python
start_point = (0, 0)
spread = 2
```

### **Output:**

```
{
 (-2,-2), (-1,-2), (0,-2), (1,-2), (2,-2),
 (-2,-1), (-1,-1), (0,-1), (1,-1), (2,-1),
 (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
 (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
 (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2)
}
```

### **Explanation:**

* Square spans from x = -2 to 2 and y = -2 to 2

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
 (2,3), (3,3), (4,3),
 (2,4), (3,4), (4,4),
 (2,5), (3,5), (4,5)
}
```

### **Explanation:**

* Square spans from x = 2 to 4 and y = 3 to 5

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
 (-4,-4), (-3,-4), (-2,-4), (-1,-4), (0,-4), (1,-4), (2,-4),
 (-4,-3), (-3,-3), ... , (2,-3),
 ...
 (-4, 2), (-3, 2), ... , (2, 2)
}
```

### **Explanation:**

* Square spans from x = -4 to 2 and y = -4 to 2

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

Spread of 0 → only the center point.

---
