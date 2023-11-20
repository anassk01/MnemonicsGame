import random
import json
import tkinter as tk

with open("mnemonics.json", "r") as f:
    mnemonics = json.load(f)

def generate_numbers():
    global sub_lists, hide_button, show_button, mnemonic_button, numbers_label
    l = int(groups_entry.get())
    o = int(size_entry.get())
    l5er = [x for _ in range(l) for x in list(range(10))]
    random.shuffle(l5er)
    sub_lists = [l5er[i:i+o] for i in range(0, len(l5er), o)]
    mnemonic_list = []
    for sub_list in sub_lists:
        codes = []
        for i in range(0, len(sub_list), 2):
            if i == len(sub_list) - 1:
                codes.append(str(sub_list[i]))
            else:
                codes.append(str(sub_list[i]) + str(sub_list[i+1]))

        mnemonics_assigned = []
        for code in codes:
            if code in mnemonics:
                mnemonics_assigned.append(mnemonics[code])
            elif code[0] in mnemonics:
                mnemonics_assigned.append(mnemonics[code[0]] + mnemonics[code[1]])
            else:
                mnemonics_assigned.append(mnemonics[code[1]])

        mnemonic_list.append(list(zip(codes, mnemonics_assigned)))
    numbers_text = " +".join("".join(map(str, sub_list)) for sub_list in sub_lists)
    mnemonic_button.config(state="normal")
    numbers_label.config(text=numbers_text)
    hide_button.config(state="normal")
    show_button.config(state="disabled")

def hide_numbers():
    global hide_button, show_button, mnemonic_button, numbers_label
    numbers_label.config(text="")
    hide_button.config(state="disabled")
    show_button.config(state="normal")
    mnemonic_button.config(state="disabled")

def show_numbers():
    global hide_button, show_button, mnemonic_button, numbers_label, sub_lists
    numbers_text = " +".join("".join(map(str, sub_list)) for sub_list in sub_lists)
    numbers_label.config(text=numbers_text)
    hide_button.config(state="normal")
    show_button.config(state="disabled")
    mnemonic_button.config(state="normal")


def show_mnemonics():
    global numbers_label, mnemonic_button, sub_lists, mnemonics

    numbers_text = " +".join("".join(map(str, sub_list)) for sub_list in sub_lists)
    mnemonic_list = []
    for sub_list in sub_lists:
        codes = []
        for i in range(0, len(sub_list), 2):
            if i == len(sub_list) - 1:
                codes.append(str(sub_list[i]))
            else:
                codes.append(str(sub_list[i]) + str(sub_list[i+1]))

        mnemonics_assigned = []
        for code in codes:
            if code in mnemonics:
                mnemonics_assigned.append(mnemonics[code])
            elif code[0] in mnemonics:
                mnemonics_assigned.append(mnemonics[code[0]] + mnemonics[code[1]])
            else:
                mnemonics_assigned.append(mnemonics[code[1]])

        mnemonic_list.append(list(zip(codes, mnemonics_assigned)))

    mnemonic_text = ""
    for mnemonics_assigned in mnemonic_list:
        for code, mnemonic in mnemonics_assigned:
            mnemonic_text += f"{code}{' ' if len(code)==2 else '  '}{mnemonic} | "
        mnemonic_text += "+  \n"
    mnemonic_text = mnemonic_text[:-4] # remove last "+  \n"
    numbers_label.config(text=numbers_text + "\n\n" + mnemonic_text)
    mnemonic_button.config(text="Hide Mnemonics", command=hide_mnemonics)


def hide_mnemonics():
    global numbers_label, mnemonic_button
    numbers_text = " +".join("".join(map(str, sub_list)) for sub_list in sub_lists)
    numbers_label.config(text=numbers_text)
    mnemonic_button.config(text="Show Mnemonics", command=show_mnemonics)

root = tk.Tk()
root.title("Mnemonics V0.4")
root.geometry("800x700")
root.configure(bg="#F5F5F5") # set background color

input_frame = tk.Frame(root, bg="#F5F5F5") # set background color
input_frame.pack(pady=10)

groups_label = tk.Label(input_frame, text="Total numbers (x10):", font=("Arial", 12), bg="#F5F5F5", fg="#333333") # set font and colors
groups_label.pack(side=tk.LEFT, padx=10)

groups_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
groups_entry.pack(side=tk.LEFT, padx=10)

size_label = tk.Label(input_frame, text="Grouping Size (/2):", font=("Arial", 12), bg="#F5F5F5", fg="#333333")
size_label.pack(side=tk.LEFT, padx=10)

size_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
size_entry.pack(side=tk.LEFT, padx=10)

generate_button = tk.Button(root, text="Generate", command=generate_numbers, bg="#FFD300", fg="#333333", font=("Arial", 12, "bold"), width=14, height=2, bd=0, activebackground="#FFD300", activeforeground="#FFFFFF")
generate_button.pack(pady=10)

hide_button = tk.Button(root, text="Hide Numbers", state="disabled", command=hide_numbers, bg="#BDBDBD", fg="#333333", font=("Arial", 12), width=14, height=2, bd=0, activebackground="#BDBDBD", activeforeground="#FFFFFF")
hide_button.pack(pady=10)

show_button = tk.Button(root, text="Show Numbers", state="disabled", command=show_numbers, bg="#BDBDBD", fg="#333333", font=("Arial", 12), width=14, height=2, bd=0, activebackground="#BDBDBD", activeforeground="#FFFFFF")
show_button.pack(pady=10)

mnemonic_button = tk.Button(root, text="Show Mnemonics", state="disabled", command=show_mnemonics, bg="#FF6B6B", fg="#FFFFFF", font=("Arial", 12), width=14, height=2, bd=0, activebackground="#FF6B6B", activeforeground="#FFFFFF")
mnemonic_button.pack(pady=10)

numbers_label = tk.Label(root, font=("Arial", 14), wraplength=800, bg="#F5F5F5", fg="#333333")
numbers_label.pack(pady=10)

root.mainloop()
