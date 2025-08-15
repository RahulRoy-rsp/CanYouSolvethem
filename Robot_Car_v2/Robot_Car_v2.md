# Robot Car Movement Problem (Version 2)

## Problem Statement
You are controlling a robot car that starts at the origin `(0, 0)` on a 2D plane, initially facing **North**. The car can receive a sequence of commands, which can be alphabetic (for engine/direction control) or numeric (for movement).  

[Refer Version 1 Here](/Robot_Car_v1/Robot_Car_v1.md)

### New Features in Version 2
1. **Reverse Command (`"R"`)**  
   - When the engine is on (`E`), `"R"` toggles the car into **reverse mode**.  
   - In reverse mode:  
     - Movement commands move the car **backward** (opposite of the current direction).  
     - Another `"R"` command exits reverse mode.  
   - If the engine is off (`S`), `"R"` is ignored.  

2. **Negative Movement Values**  
   - Negative numbers (e.g., `-3`) are valid movement commands.  
   - Interpretation:  
     - If in **forward mode**: Moves backward (like reverse).  
     - If in **reverse mode**: Moves forward (negation of negation).  

---

## Command Types
1. **Engine Commands**  
   - `E`: **Start Engine** – The car can now move.  
   - `S`: **Stop Engine** – The car cannot move until `E` is given again.  

2. **Direction Commands**  
   - `L`: **Turn Left** (90° counterclockwise).  
   - `R`: **Reverse Toggle** (only works if engine is on).  

3. **Movement Commands**  
   - Positive numbers (`3`): Move forward (or backward if in reverse mode).  
   - Negative numbers (`-2`): Move backward (or forward if in reverse mode).  

---

## Movement Rules 
| Mode          | Positive Command (`+n`) | Negative Command (`-n`) |
|--------------|------------------------|------------------------|
| **Forward**  | Move `+n` in direction | Move `-n` (backward)   |
| **Reverse**  | Move `-n` (backward)   | Move `+n` (forward)    |

---

## Example Test Cases

### Test Case 1: Simple Reverse Toggle
**Input**: `["E", 2, "R", 3]`  
**Expected Output**: `[0, -1]`  

**Explanation**:  
1. Start at `(0, 0)`, facing North.  
2. `"E"`: Engine on → can move.  
3. `2`: Move `+2` North → `(0, 2)`.  
4. `"R"`: Toggle reverse mode.  
5. `3`: Now in reverse → `-3` North → `(0, -1)`.  

---

### Test Case 2: Negative Movement in Forward Mode 
**Input**: `["E", -2, "L", -3]`  
**Expected Output**: `[3, -2]`  

**Explanation**:  
1. `"E"`: Engine on.  
2. `-2`: Move backward `2` North → `(0, -2)`.  
3. `"L"`: Turn left (North → West).  
4. `-3`: Move backward `3` West → `(3, -2)`.  

---

### Test Case 3: Reverse + Negative Movement
**Input**: `["E", "R", -4, "R", -1]` 
**Expected Output**: `[0, 3]`  

**Explanation**:  
1. `"E"`: Engine on.  
2. `"R"`: Toggle reverse mode.  
3. `-4`: In reverse → `-(-4) = +4` North → `(0, 4)`.  
4. `"R"`: Exit reverse mode.  
5. `-1`: Now forward → `-1` North → `(0, 3)`.  

---

### Test Case 4: Engine Off Ignores Reverse
**Input**: `["R", "E", 2, "S", "R", 3]`  
**Expected Output**: `[0, 2]`  

**Explanation**:  
1. `"R"`: Ignored (engine off).  
2. `"E"`: Engine on.  
3. `2`: Move `+2` North → `(0, 2)`.  
4. `"S"`: Engine off.  
5. `"R"`: Ignored (engine off).  
6. `3`: Ignored (engine off).  

---

## Solution Approach
1. Track:  
   - Position (`x`, `y`).  
   - Direction (`"N"`, `"E"`, `"S"`, `"W"`).  
   - Engine state (`0` = off, `1` = on).  
   - Reverse mode (`True`/`False`).  
2. For each command:  
   - If `"E"`/`"S"`, update engine state.  
   - If `"L"`, turn left.  
   - If `"R"` and engine on, toggle reverse mode.  
   - If numeric:  
     - Apply movement (considering reverse mode and sign).  

---
