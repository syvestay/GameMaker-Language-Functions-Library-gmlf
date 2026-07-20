# GMLF (GameMaker Language Functions)

GMLF is a Python library that provides functions inspired by **GameMaker Language (GML)**.

The goal of this library is to make game development in Python easier for people who are familiar with GameMaker by providing functions with names and behaviors similar to the ones available in GML.

> GMLF is not an official GameMaker library and has no connection with YoYo Games. It is an independent recreation of some GML functions for Python.

---

# Installation

```bash
pip install gmlf
```

---

# Basic Example

In GameMaker:

```gml
lerp(0, 100, 0.5)
```

Using GMLF in Python:

```python
import gmlf

print(gmlf.lerp(0, 100, 0.5))
```

Output:

```
50
```

---

# Available Functions

## Mathematics

Functions for calculations and value manipulation.

---

### `sign(x)`

Returns the sign of a number.

Returns:

* `1` if the value is positive
* `-1` if the value is negative
* `0` if the value is zero

Example:

```python
gmlf.sign(-20)
```

Output:

```
-1
```

---

### `abs(x)`

Returns the absolute value of a number.

Example:

```python
gmlf.abs(-50)
```

Output:

```
50
```

---

### `min(...)`

Returns the smallest value among multiple numbers.

Example:

```python
gmlf.min(10, 5, 20)
```

Output:

```
5
```

---

### `max(...)`

Returns the largest value among multiple numbers.

Example:

```python
gmlf.max(10, 5, 20)
```

Output:

```
20
```

---

### `clamp(value, minimum, maximum)`

Keeps a value inside a specified range.

Example:

```python
gmlf.clamp(300, 0, 255)
```

Output:

```
255
```

---

### `lerp(a, b, amount)`

Performs linear interpolation between two values.

Example:

```python
gmlf.lerp(0, 100, 0.5)
```

Output:

```
50
```

---

### `sqr(x)`

Returns the square of a number.

Example:

```python
gmlf.sqr(5)
```

Output:

```
25
```

---

### `floor(x)`

Rounds a number down.

Example:

```python
gmlf.floor(5.8)
```

Output:

```
5
```

---

### `frac(x)`

Returns the decimal part of a number.

Example:

```python
gmlf.frac(10.75)
```

Output:

```
0.75
```

---

### `point_distance(x1, y1, x2, y2)`

Calculates the distance between two points.

Example:

```python
gmlf.point_distance(0, 0, 3, 4)
```

Output:

```
5
```

---

# Movement

Functions inspired by GameMaker's direction and movement system.

---

### `point_direction(x1, y1, x2, y2)`

Calculates the angle between two points.

Example:

```python
direction = gmlf.point_direction(0, 0, 100, 0)
```

---

### `lengthdir_x(distance, direction)`

Calculates the X movement based on a direction.

Example:

```python
x += gmlf.lengthdir_x(5, 0)
```

---

### `lengthdir_y(distance, direction)`

Calculates the Y movement based on a direction.

Example:

```python
y += gmlf.lengthdir_y(5, 90)
```

---

### `move_towards_point(x1, y1, x2, y2, speed)`

Returns the movement needed to move from one point to another.

Example:

```python
vel_x, vel_y = gmlf.move_towards_point(
    0, 0,
    100, 100,
    5
)
```

---

# Input

Functions inspired by GameMaker's keyboard system.

---

### `keyboard_check(key)`

Checks if a key is currently pressed.

Example:

```python
if gmlf.keyboard_check(pygame.K_SPACE):
    print("Jump")
```

---

### `keyboard_check_pressed(events, key)`

Checks if a key was pressed in the current frame.

---

### `keyboard_check_released(events, key)`

Checks if a key was released in the current frame.

---

# Collision

Functions inspired by GameMaker's `place_meeting`.

---

### `place_meeting(x, y, width, height, collision)`

Checks collision with a single collision object.

Example:

```python
if gmlf.place_meeting(x, y, 32, 32, wall):
    print("Collision")
```

---

### `place_meeting_all(x, y, width, height, collisions)`

Checks collision against a list of collision objects.

Example:

```python
if gmlf.place_meeting_all(x, y, 32, 32, walls):
    print("Collision")
```

---

# Arrays

Functions inspired by GameMaker's array manipulation.

---

### `array_insert(array, position, value)`

Inserts a value at a specific position.

---

### `array_delete(array, position, amount)`

Deletes values from an array.

---

### `array_push(array, value)`

Adds a value to the end of an array.

---

### `array_pop(array)`

Removes and returns the last value of an array.

---

### `array_length(array)`

Returns the length of an array.

---

### `array_find_index(array, value)`

Finds the index of a value.

Returns:

* The position if found
* `-1` if it does not exist

Example:

```python
gmlf.array_find_index([10, 20, 30], 20)
```

Output:

```
1
```

---

# License

This project uses the MIT License.
como ficaria corrigido ?
