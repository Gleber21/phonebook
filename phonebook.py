import tkinter as tk
import tkinter.messagebox
import tkinter.scrolledtext
from tkinter.ttk import Radiobutton
from tkinter import filedialog
import time
import json
import csv


def printer():
    """Обновляет поле контактов."""
    contacts.sort(key=lambda c: c[sort_by_int.get()])
    scrolled_text.configure(state="normal")
    scrolled_text.delete("1.0", tk.END)
    for contact in contacts:
        scrolled_text.insert(tk.INSERT, contact[:2])
        scrolled_text.insert(tk.INSERT, time.strftime(" %d %b %Y %H:%M:%S\n", time.localtime(contact[2])))
    scrolled_text.configure(state="disabled")


def clicked():
    """Добавление контакта."""
    name = ent_name.get()
    number = ent_number.get()
    if name != "" and number != "":
        contacts.append(list((name, number, time.time())))
        ent_name.delete(0, tk.END)
        ent_number.delete(0, tk.END)
        printer()
    else:
        if name == "" and number != "":
            tk.messagebox.showerror(title="Ошибка", message="Введите имя")
        elif number == "" and name != "":
            tk.messagebox.showerror(title="Ошибка", message="Введите номер")
        else:
            tk.messagebox.showerror(title="Ошибка", message="Введите имя и номер")


def export_to_file():
    """Экспорт в файл."""
    filename = tk.filedialog.asksaveasfilename(
        filetypes=(
            ("JSON-файл", "*.json"),
            ("CSV-файл", "*.csv"),
        )
    )
    if all((isinstance(filename, str), filename != "")):
        if filename.endswith(".json") or filename.endswith(".csv"):
            with open(filename, "w") as file:
                if filename.endswith(".json"):
                    json.dump(contacts, file, ensure_ascii=False, indent=4)
                elif filename.endswith(".csv"):
                    csv.writer(file).writerows(contacts)
        else:
            tk.messagebox.showerror(title="Ошибка сохранения", message="Ваш файл не сохранился. Нужно указать "
                                                                       "расширение (.json или .csv)")


def import_from_file():
    """Импорт из файла."""
    global contacts
    filename = tk.filedialog.askopenfilename(
        filetypes=(
            ("JSON-файл", "*.json"),
            ("CSV-файл", "*.csv"),
        )
    )
    if all((isinstance(filename, str), filename != "")):
        with open(filename) as file:
            if filename.endswith(".json"):
                if not contacts:
                    contacts = json.load(file)
                else:
                    what_to_do = tk.messagebox.askyesnocancel(title="Объединить? Возможна потеря данных!",
                                                              message="Объединить данные приложении (да),\n"
                                                                      "оставить только из файла (нет),\n"
                                                                      "ничего не делать (отмена)")
                    if what_to_do is not None:
                        if what_to_do:
                            contacts.extend(json.load(file))
                        else:
                            contacts = json.load(file)
            elif filename.endswith(".csv"):
                if not contacts:
                    contacts = list(csv.reader(file))
                    for cont in contacts:
                        cont[2] = float(cont[2])
                else:
                    what_to_do = tk.messagebox.askyesnocancel(title="Объединить? Возможна потеря данных!",
                                                              message="Объединить данные приложении (да),\n"
                                                                      "оставить только из файла (нет),\n"
                                                                      "ничего не делать (отмена)")
                    if what_to_do is not None:
                        if what_to_do:
                            temp = list(csv.reader(file))
                            for cont in temp:
                                cont[2] = float(cont[2])
                            contacts.extend(temp)
                        else:
                            contacts = list(csv.reader(file))
                            for cont in contacts:
                                cont[2] = float(cont[2])
    printer()


window = tk.Tk()
contacts = []
window.title("Телефонная книга")
window.geometry("580x580")
sort_by_int = tk.IntVar()
sort_by_int.set(2)

lbl_name = tk.Label(window, text="Введите имя контакта:  ", font=("Arial Bold", 15))
lbl_number = tk.Label(window, text="Введите номер контакта:", font=("Arial Bold", 15))
lbl_contacts = tk.Label(window, text="Контакты (имя, номер, дата создания)", font=("Arial Bold", 10))
ent_name = tk.Entry(window, width=20)
ent_number = tk.Entry(window, width=20)
btn_save = tk.Button(window, text="Добавить контакт", command=clicked)
scrolled_text = tk.scrolledtext.ScrolledText(window, width=60, height=10, state="disabled")
rad0 = tk.ttk.Radiobutton(window, text="Сортировка по имени", value=0, variable=sort_by_int)
rad2 = tk.ttk.Radiobutton(window, text="Сортировка по дате добавления", value=2, variable=sort_by_int)
btn_reload = tk.Button(window, text="Обновить список", command=printer)
btn_export = tk.Button(window, text="Экспорт в файл", command=export_to_file)
btn_import = tk.Button(window, text="Импорт из файла", command=import_from_file)

lbl_name.place(x=5, y=0)
lbl_number.place(x=5, y=30)
lbl_contacts.place(x=5, y=63)
ent_name.place(x=250, y=7)
ent_number.place(x=250, y=37)
btn_save.place(x=257, y=60)
btn_reload.place(x=50, y=87)
scrolled_text.place(x=5, y=140)
rad0.place(x=10, y=115)
rad2.place(x=200, y=115)
btn_export.place(x=60, y=310)
btn_import.place(x=200, y=310)

window.mainloop()