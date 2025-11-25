# Exercise: Rock Paper Scissors

## Instructions

1. Create a file named `rock_paper_scissors.py`.
2. Design a program to play "Rock, Paper, Scissors" against the computer.
3. **Logic:**
   * **Rock** breaks **Scissors**.
   * **Scissors** cut **Paper**.
   * **Paper** covers **Rock**.
   * If both choose the same, it is a **Tie**.
4. **Computer Logic:** Use `random.randint(1, 3)` to generate the computer's choice:
   * 1 = Rock
   * 2 = Paper
   * 3 = Scissors
5. **Flow:**
   * The user enters their choice (R, P, or S).
   * The computer generates a choice.
   * Display both choices.
   * Announce the winner.
6. **Error Handling:** If the user enters an invalid letter, display "Bad choice...".