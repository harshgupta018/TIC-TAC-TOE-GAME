import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("360x470")
root.configure(bg="#1E3A5F")
root.resizable(False, False)

current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

turn_label = tk.Label(
    root,
    text="Current Turn : X",
    font=("Arial", 18, "bold"),
    bg="#1E3A5F",
    fg="white"
)
turn_label.grid(row=0, column=0, columnspan=3, pady=10)


def check_winner():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def check_draw():

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False

    return True


def button_click(row, col):

    global current_player

    if buttons[row][col]["text"] == "":

        buttons[row][col]["text"] = current_player

        if current_player == "X":
            buttons[row][col]["fg"] = "red"
        else:
            buttons[row][col]["fg"] = "blue"

        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} Wins!")
            reset_game()

        elif check_draw():
            messagebox.showinfo("Draw", "Match Draw!")
            reset_game()

        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

            turn_label.config(text=f"Current Turn : {current_player}")


def reset_game():

    global current_player

    current_player = "X"

    turn_label.config(text="Current Turn : X")

    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col]["fg"] = "black"


for row in range(3):
    for col in range(3):

        buttons[row][col] = tk.Button(
            root,
            text="",
            font=("Arial", 24, "bold"),
            width=5,
            height=2,
            bg="white",
            activebackground="#D6EAF8",
            relief="ridge",
            bd=4,
            command=lambda r=row, c=col: button_click(r, c)
        )

        buttons[row][col].grid(
            row=row+1,
            column=col,
            padx=5,
            pady=5
        )


reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 15, "bold"),
    bg="green",
    fg="white",
    width=18,
    command=reset_game
)

reset_btn.grid(row=4, column=0, columnspan=3, pady=20)

root.mainloop()