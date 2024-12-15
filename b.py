import tkinter as tk
from tkinter import messagebox
import numpy as np
import random as rd
from PIL import Image, ImageTk


def place_knight():
    reset_board()
    position = e1.get()
    if position:
        try:
            startRow, startColumn = map(int, position.split(','))
            if 0 <= startRow <= 7 and 0 <= startColumn <= 7:
                # Clear the board
                canvas.delete("highlight")
                canvas.delete("knight")
                canvas.delete("line")

                board = np.zeros((8, 8), dtype=int)
                current = [startRow, startColumn]
                board[current[0], current[1]] = 1
                moveCounter = 2

                moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, -2), (-1, 2)]

                def doMove(move, counter):
                    nonlocal current
                    x = current[0] + move[0]
                    y = current[1] + move[1]
                    if (0 <= x <= 7) and (0 <= y <= 7) and board[x][y] == 0:
                        board[x, y] = counter
                        current[0] = x
                        current[1] = y
                        return True
                    return False

                def completeBoard(board):
                    return np.count_nonzero(board) == 64

                # Load an image in the script
                img = ImageTk.PhotoImage(Image.open("knight.png"))

                # Place the knight at the starting position
                x_pixel = 50 + startColumn * 50
                y_pixel = 40 + startRow * 50
                canvas.create_text(x_pixel + 25, y_pixel + 25, text="1", fill='red', font=("Cambria", 12),
                                   tags="number")
                path_label.config(state=tk.NORMAL)
                path_label.insert(tk.END, f"({current[0]},{current[1]}) ")
                path_label.config(state=tk.DISABLED)
                while not completeBoard(board):
                    possibleMoves = []
                    for move in moves:
                        x = current[0] + move[0]
                        y = current[1] + move[1]
                        if (0 <= x <= 7) and (0 <= y <= 7) and board[x][y] == 0:
                            possibleMoves.append(move)
                    if len(possibleMoves) == 0:
                        break
                    moveIndex = rd.randint(0, len(possibleMoves) - 1)
                    if doMove(possibleMoves[moveIndex], moveCounter):
                        # Draw line
                        prev_x_pixel = 50 + (current[1] - possibleMoves[moveIndex][1]) * 50 + 25
                        prev_y_pixel = 40 + (current[0] - possibleMoves[moveIndex][0]) * 50 + 25
                        x_pixel = 50 + current[1] * 50 + 25
                        y_pixel = 40 + current[0] * 50 + 25
                        canvas.create_image(x_pixel, y_pixel, image=img, tags="knight")
                        canvas.create_line(prev_x_pixel, prev_y_pixel, x_pixel, y_pixel, fill='blue', tags="line")
                        canvas.update()
                        canvas.after(500)
                        canvas.delete("knight")
                        canvas.update()
                        canvas.after(500)
                        canvas.create_text(x_pixel, y_pixel, text=str(moveCounter), fill='red', font=("Cambria", 12),
                                           tags="number")
                        canvas.update()
                        canvas.after(500)
                        moveCounter += 1
                        # Show path in the label
                        path_label.config(state=tk.NORMAL)
                        path_label.insert(tk.END, f"({current[0]},{current[1]}) ")
                        path_label.config(state=tk.DISABLED)

                messagebox.showinfo("Path Completed", "Knight's tour completed.")
                canvas.delete("line")
                canvas.delete("number")

            else:
                messagebox.showerror("Error", "Invalid position. Please enter values between 0 and 7.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input format. Please enter the position as row,column.")
    else:
        messagebox.showinfo("Error", "No position entered.")


def reset_board():
    canvas.delete("highlight")
    canvas.delete("knight")
    canvas.create_text(250, 250, text="Knight's Tour", font=("Cambria", 20))
    for i in range(8):
        for j in range(8):
            if not (i + j) % 2:
                fill_color = '#eeeed2'
            else:
                fill_color = '#769656'
            x_pixel = 50 + j * 50
            y_pixel = 40 + i * 50
            canvas.create_rectangle(x_pixel, y_pixel, x_pixel + 50, y_pixel + 50, fill=fill_color)
    path_label.config(state=tk.NORMAL)
    path_label.delete(1.0, tk.END)
    path_label.config(state=tk.DISABLED)


window = tk.Tk()
window.title("Knight's Tour")

l1 = tk.Label(window, text="Knight's Tour", font=("Cambria", 20))
l1.grid(row=0, columnspan=3)
l2 = tk.Label(window)
l2.grid(row=1, columnspan=3)
l3 = tk.Label(window, text="Enter position: ")
l3.grid(row=2, columnspan=3)
e1 = tk.Entry(window)
e1.grid(row=3, columnspan=3)
l4 = tk.Label(window)
l4.grid(row=4, columnspan=3)

place_btn = tk.Button(window, text="Place Knight", command=place_knight)
place_btn.grid(row=5, columnspan=3)

path_label = tk.Text(window, width=12, height=22, state=tk.DISABLED)
path_label.grid(row=6, column=3)

canvas = tk.Canvas(window, width=500, height=500)
color = True
for x in range(50, 401, 50):
    for y in range(40, 401, 50):
        if not color:
            canvas.create_rectangle(x, y, x + 50, y + 50, fill='#eeeed2')
        else:
            canvas.create_rectangle(x, y, x + 50, y + 50, fill='#769656')
        color = not color
    color = not color
canvas.grid(row=6, column=0, columnspan=2)

# Create the ruler for columns
for i in range(8):
    x_pixel = 50 + i * 50 + 25
    y_pixel = 20
    canvas.create_text(x_pixel, y_pixel, text=str(i), font=("Cambria", 12))

# Create the ruler for rows
for i in range(8):
    x_pixel = 20
    y_pixel = 40 + i * 50 + 25
    canvas.create_text(x_pixel, y_pixel, text=str(i), font=("Cambria", 12))

window.mainloop()