# Robot Car Movement Problem (Version 1)

## Problem Statement

You are controlling a robot car that starts at the origin `(0, 0)` on a 2D plane. Initially, the car is facing **North**. The car can receive a sequence of commands, which can be either alphabetic (for engine/direction control) or numeric (for movement). Your task is to determine the final position of the car after executing all the commands.

### Command Types:
1. **Engine Commands**:
   - `E`: **Start Engine** – The car can now move when given a movement command.
   - `S`: **Stop Engine** – The car cannot move until the engine is started again.

2. **Direction Commands**:
   - `L`: **Turn Left** – Changes the car's direction 90° to the left of its current direction.
     - Example: If the car is facing **North**, turning left makes it face **West**.
   - `R`: **Turn Right** – Changes the car's direction 90° to the right of its current direction.
     - Example: If the car is facing **North**, turning right makes it face **East**.

3. **Movement Commands** (Whole Numbers):
   - If the engine is **started (`E`)**, the car moves in its current direction by the given number of units.
   - If the engine is **stopped (`S`)**, the car ignores movement commands.

### Movement Directions:
- **North (N)**: Positive Y-direction.
- **East (E)**: Positive X-direction.
- **South (S)**: Negative Y-direction.
- **West (W)**: Negative X-direction.

### Assumptions:
- The car starts with the engine **stopped** (cannot move unless `E` is given).
- Direction changes (`L`/`R`) work even if the engine is stopped.

---

## Example Test Cases

### Test Case 1:
**Input**: `[2, "L", 2, "E", 3]`  
**Output**: `[-3, 0]`  

#### Explanation:
| Command | Action                          | Position  | Direction | Engine State |
|---------|---------------------------------|-----------|-----------|--------------|
| 2       | Ignored (engine stopped)        | (0, 0)    | North     | Stopped      |
| "L"     | Turn left (North → West)        | (0, 0)    | West      | Stopped      |
| 2       | Ignored (engine stopped)        | (0, 0)    | West      | Stopped      |
| "E"     | Start engine                    | (0, 0)    | West      | Started      |
| 3       | Move 3 units West               | (-3, 0)   | West      | Started      |

**Final Position**: `[-3, 0]`

---

### Test Case 2:
**Input**: `["E", 2, "R", 3, "S", 4, "L", 1]`  
**Output**: `[3, 2]`  

#### Explanation:
| Command | Action                          | Position  | Direction | Engine State |
|---------|---------------------------------|-----------|-----------|--------------|
| "E"     | Start engine                    | (0, 0)    | North     | Started      |
| 2       | Move 2 units North              | (0, 2)    | North     | Started      |
| "R"     | Turn right (North → East)       | (0, 2)    | East      | Started      |
| 3       | Move 3 units East               | (3, 2)    | East      | Started      |
| "S"     | Stop engine                     | (3, 2)    | East      | Stopped      |
| 4       | Ignored (engine stopped)        | (3, 2)    | East      | Stopped      |
| "L"     | Turn left (East → North)        | (3, 2)    | North     | Stopped      |
| 1       | Ignored (engine stopped)        | (3, 2)    | North     | Stopped      |

**Final Position**: `[3, 2]`

---

### **Test Case 3: Complex Movement with Multiple Turns**  
**Input**: `["E", 5, "R", 3, "L", 2, "S", 4, "E", 1]`  
**Expected Output**: `[4, 6]`  

#### **Step-by-Step Explanation**:
| Command | Action                          | Position  | Direction | Engine State |
|---------|---------------------------------|-----------|-----------|--------------|
| `"E"`   | Start engine                    | `(0, 0)`  | North     | Started      |
| `5`     | Move 5 units North              | `(0, 5)`  | North     | Started      |
| `"R"`   | Turn right (North → East)       | `(0, 5)`  | East      | Started      |
| `3`     | Move 3 units East               | `(3, 5)`  | East      | Started      |
| `"L"`   | Turn left (East → North)        | `(3, 5)`  | North     | Started      |
| `2`     | Move 2 units North              | `(3, 7)`  | North     | Started      |
| `"S"`   | Stop engine                     | `(3, 7)`  | North     | Stopped      |
| `4`     | Ignored (engine stopped)        | `(3, 7)`  | North     | Stopped      |
| `"E"`   | Start engine                    | `(3, 7)`  | North     | Started      |
| `1`     | Move 1 unit North               | `(3, 8)`  | North     | Started      |

**Final Position**: `[3, 8]` 

---

### **Test Case 4: No Movement (Engine Never Started)**  
**Input**: `["L", "R", 2, "S", 5]`  
**Expected Output**: `[0, 0]`  

#### **Explanation**:
- The engine is **never started (`E`)**.  
- All movement commands (`2`, `5`) are ignored.  
- Direction changes (`"L"`, `"R"`) still work but don’t affect position.  

---

### **Test Case 5: Movement After Stopping Engine**  
**Input**: `["E", 2, "S", 3, "E", 4]`  
**Expected Output**: `[0, 6]`  

#### **Explanation**:
| Command | Action                          | Position  | Direction | Engine State |
|---------|---------------------------------|-----------|-----------|--------------|
| `"E"`   | Start engine                    | `(0, 0)`  | North     | Started      |
| `2`     | Move 2 units North              | `(0, 2)`  | North     | Started      |
| `"S"`   | Stop engine                     | `(0, 2)`  | North     | Stopped      |
| `3`     | Ignored (engine stopped)        | `(0, 2)`  | North     | Stopped      |
| `"E"`   | Start engine                    | `(0, 2)`  | North     | Started      |
| `4`     | Move 4 units North              | `(0, 6)`  | North     | Started      |

---

### **Test Case 6: Circular Path (Returns to Origin)**  
**Input**: `["E", 1, "R", 1, "R", 1, "R", 1]`  
**Expected Output**: `[0, 0]`  

#### **Explanation**:
1. Starts at `(0, 0)`, facing North.  
2. Moves `1` unit North → `(0, 1)`.  
3. Turns right (North → East).  
4. Moves `1` unit East → `(1, 1)`.  
5. Turns right (East → South).  
6. Moves `1` unit South → `(1, 0)`.  
7. Turns right (South → West).  
8. Moves `1` unit West → `(0, 0)`.  

---

### **Test Case 7: Different Case Commands (Edge Cases)**  
**Input**: `["X", -1, 0, "e", "l", 2]`  
**Expected Output**: `[-2, 0]`  

#### **Assumptions**:
- Invalid commands (`"X"`, negative numbers) are **ignored**.  
- `0` movement is valid but does nothing.  

#### **Explanation**:
| Command | Action                          | Position  | Direction | Engine State |
|---------|---------------------------------|-----------|-----------|--------------|
| `"X"`   | Ignored (invalid)               | `(0, 0)`  | North     | Stopped      |
| `-1`    | Ignored (invalid)               | `(0, 0)`  | North     | Stopped      |
| `0`     | Ignored (engine stopped)        | `(0, 0)`  | North     | Stopped      |
| `"e"`   | Start engine                    | `(0, 0)`  | North     | Started      |
| `"l"`   | Turn left (North → West)        | `(0, 0)`  | West      | Started      |
| `2`     | Move 2 units West               | `(-2, 0)` | West      | Started      |

---

### **Test Case 8: Mixed Commands (Strings vs. Integers)**  
**Input**: `["E", "2", "R", 3, "S", "1"]`  
**Expected Output**: `[3, 2]`  

#### **Explanation**:
- Handles numeric commands as both strings (`"2"`) and integers (`3`).  
- Movement `"2"` (as string) is valid when the engine is on.  

---

## Solution Approach
1. Initialize the car's state:
   - Position: `(0, 0)`
   - Direction: `North`
   - Engine: `Stopped` (cannot move unless `E` is given).
2. Process each command in order:
   - For alphabetic commands (`E`, `S`, `L`, `R`), update the engine state or direction.
   - For numeric commands, move the car only if the engine is started.
3. Return the final position after executing all commands.


---
