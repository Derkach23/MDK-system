from datetime import date
import tkinter as tk


def calculate_age():
    today = date.today()
    birth_date_str = entry.get()
    birth_date = date.fromisoformat(birth_date_str[6:] + "-" + birth_date_str[3:5] + "-" + birth_date_str[:2])
    age_in_days = (today - birth_date).days
    result_label.config(text=f"Возраст: {age_in_days} дней")


root = tk.Tk()
root.title("Вычисление возраста")
root.geometry("300x150")

entry = tk.Entry(root, width=10)
entry.pack(pady=10)

button = tk.Button(root, text="Вычислить", command=calculate_age)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()



