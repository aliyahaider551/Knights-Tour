# Knight's Tour GUI

The **Knight's Tour GUI** is a Python-based application that visualizes the knight's tour problem on a chessboard using a graphical user interface (GUI). It allows users to place a knight on any starting position on an 8x8 chessboard and watch as the knight completes its tour.

---

## Features

1. **Graphical Chessboard**:
   - A beautifully rendered 8x8 chessboard using the `tkinter` library.
   - Alternating light and dark squares, mimicking a real chessboard.

2. **Interactive Input**:
   - Enter a starting position for the knight in the format `row,column` (e.g., `0,0`).
   - Validate user input and display error messages for invalid entries.

3. **Knight's Tour Animation**:
   - Visualize the knight's movements step-by-step across the board.
   - Watch the knight's path highlighted on the board.

4. **Path Display**:
   - The path traversed by the knight is displayed in real-time in a side panel.

5. **Board Reset**:
   - Reset the chessboard and clear all animations and paths.

6. **Completion Notification**:
   - Notify the user once the knight's tour is complete.

---

## Requirements

- **Python**: 3.x
- **Dependencies**:
  - `tkinter`: For GUI elements.
  - `numpy`: For matrix-based calculations.
  - `Pillow`: For handling images (e.g., knight icon).
