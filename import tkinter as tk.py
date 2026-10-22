import tkinter as tk
from tkinter import messagebox

# ========================================================
# 1. GAME DATA & LOGIC SETUP
# ========================================================
# Exactly like the terminal version: 9 elements in a list
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
current_player = "X"
buttons = []  # Holds the 9 tkinter Button objects


# ========================================================
# 2. CORE GAME LOGIC (SAME AS TERMINAL VERSION)
# ========================================================
def check_win():
  """Checks all 8 winning combinations across rows, columns, and diagonals."""
  win_conditions = [
      (0, 1, 2),
      (3, 4, 5),
      (6, 7, 8),  # Rows
      (0, 3, 6),
      (1, 4, 7),
      (2, 5, 8),  # Columns
      (0, 4, 8),
      (2, 4, 6),  # Diagonals
  ]

  for a, b, c in win_conditions:
    if board[a] == board[b] == board[c]:
      return True
  return False


def check_draw():
  """Checks if all spots have been filled with 'X' or 'O'."""
  for spot in board:
    if spot != "X" and spot != "O":
      return False
  return True


def reset_game():
  """Resets the board data and clears the buttons for a fresh match."""
  global board, current_player
  board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  current_player = "X"
  turn_label.config(text="Player X's Turn")

  # Reset each button's text and re-enable it
  for btn in buttons:
    btn.config(text="", state="normal")


# ========================================================
# 3. BUTTON CLICK HANDLER (REPLACES player_turn())
# ========================================================
def on_button_click(index):
  """Handles button clicks, updates GUI & data, checks outcomes, and swaps turns."""
  global current_player

  # Check: Is the clicked spot already taken?
  if board[index] == "X" or board[index] == "O":
    return

  # Update the game board list and visual button
  board[index] = current_player
  buttons[index].config(text=current_player, state="disabled")

  # 1. Check if the current player won
  if check_win():
    messagebox.showinfo(
        "Game Over", f"Congratulations! Player {current_player} wins!"
    )
    reset_game()
    return

  # 2. Check for a draw
  if check_draw():
    messagebox.showinfo("Game Over", "It's a draw! No one wins.")
    reset_game()
    return

  # 3. Swap the active player
  if current_player == "X":
    current_player = "O"
  else:
    current_player = "X"

  # Update the turn label on top of the window
  turn_label.config(text=f"Player {current_player}'s Turn")


# ========================================================
# 4. GUI WINDOW SETUP & GRID CREATION
# ========================================================
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

# Top label displaying current status
turn_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16, "bold"))
turn_label.grid(row=0, column=0, columnspan=3, pady=10)

# Build the 3x3 grid of buttons (indices 0 through 8)
for i in range(9):
  row = (i // 3) + 1  # Rows 1, 2, 3 (Row 0 is the label)
  col = i % 3  # Columns 0, 1, 2

  btn = tk.Button(
      root,
      text="",
      font=("Arial", 24, "bold"),
      width=5,
      height=2,
      command=lambda idx=i: on_button_click(idx),
  )
  btn.grid(row=row, column=col, padx=5, pady=5)
  buttons.append(btn)

# Reset Button at the bottom
reset_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game,
    bg="#f0f0f0",
)
reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

# Start the application loop
root.mainloop()