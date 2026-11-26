import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Pakistan Quiz Game - By Ayesha")
root.geometry("550x500")
root.config(bg="#EAF2F8")

tk.Label(root, text="🇵🇰 Pakistan Quiz Game", font=("Arial", 20, "bold"), bg="#EAF2F8", fg="#1A5276").pack(pady=15)

questions = [
    ("Pakistan ka Capital kya hai?", ["Karachi", "Lahore", "Islamabad", "Quetta"], "Islamabad"),
    ("Pakistan ka National Game kya hai?", ["Cricket", "Hockey", "Football", "Kabaddi"], "Hockey"),
    ("Lahore ka famous khana kya hai?", ["Biryani", "Paye", "Nihari", "Sajji"], "Paye"),
    ("Pakistan kab azaad hua?", ["1946", "1947", "1948", "1950"], "1947"),
    ("Minar-e-Pakistan kahan hai?", ["Karachi", "Lahore", "Islamabad", "Multan"], "Lahore"),
]

current_q = 0
score = 0

question_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#EAF2F8", wraplength=450)
question_label.pack(pady=20)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12, "bold"), bg="#EAF2F8", fg="#27AE60")
score_label.pack()

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=30, bg="white")
    btn.pack(pady=5)
    buttons.append(btn)

def show_question():
    q, options, correct = questions[current_q]
    question_label.config(text=f"Q{current_q+1}: {q}")
    for i, opt in enumerate(options):
        buttons[i].config(text=opt, command=lambda o=opt: check_answer(o))

def check_answer(selected):
    global current_q, score
    correct = questions[current_q][2]
    if selected == correct:
        score += 10
        messagebox.showinfo("Sahi! 🎉", "Bilkul Sahi Jawab!")
    else:
        messagebox.showerror("Ghalat 😢", f"Sahi jawab tha: {correct}")
    
    score_label.config(text=f"Score: {score}")
    current_q += 1
    if current_q < len(questions):
        show_question()
    else:
        messagebox.showinfo("Game Khatam! 🏆", f"Tumhara Final Score: {score}/50\nShabash Ayesha!")
        root.destroy()

show_question()
root.mainloop()
