import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def search_fipe():
    fipe_codes_input = fipe_codes_entry.get()
    anos_input = anos_entry.get()
    
    if not fipe_codes_input or not anos_input:
        messagebox.showerror("Erro", "Por favor, insira os códigos FIPE e os anos.")
        return

    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    time.sleep(2)
    driver.find_element(By.ID, "fipe_search_button").click()

    def processa_codigo_fipe(fipe_codes_input):
        fipe_input = driver.find_element(By.ID, 'fipe_input')
        fipe_input.send_keys(fipe_codes_input)

    def processa_ano_modelo(anos_input):
        ano_input = driver.find_element(By.ID, "ano_input")
        ano_input.send_keys(anos_input)

    processa_codigo_fipe(fipe_codes_input)
    processa_ano_modelo(anos_input)
    driver.find_element(By.ID, "search_button").click()

    time.sleep(50)
    driver.quit()

root = tk.Tk()
root.title("Busca FIPE")
root.geometry("600x300")
root.resizable(False, False)

title_frame = ttk.Frame(root, padding="20")
title_frame.pack(fill=tk.X)
title_label = ttk.Label(title_frame, text="Busca FIPE", font=("Helvetica", 16))
title_label.pack()

input_frame = ttk.Frame(root, padding="20")
input_frame.pack(fill=tk.X, padx=10, pady=10)

ttk.Label(input_frame, text="Códigos FIPE: ").grid(row=0, column=0, sticky=tk.W, pady=5)
fipe_codes_entry = ttk.Entry(input_frame, width=50)
fipe_codes_entry.grid(row=0, column=1, pady=5)

ttk.Label(input_frame, text="Anos dos modelos: ").grid(row=1, column=0, sticky=tk.W, pady=5)
anos_entry = ttk.Entry(input_frame, width=50)
anos_entry.grid(row=1, column=1, pady=5)

button_frame = ttk.Frame(root, padding="20")
button_frame.pack(fill=tk.X)
search_button = ttk.Button(button_frame, text="Buscar", command=search_fipe)
search_button.pack()

root.mainloop()
