# -*- coding: utf-8 -*-

import csv
import tkinter as tk
from tkinter import filedialog, ttk
import os

# browse the csv file
root = tk.Tk()
file = filedialog.askopenfile(initialdir=os.getcwd(),mode='rt',title='Select a  csv file',filetypes=[("CSV Files", "*.csv")])
if file != None:
    # close file dialog
    root.destroy()
    
    # convert csv file to list of dict process
    # because csv reader read every cell as string,
    # we need to convert field 'kuantitas', 'harga' dan 'jumlah' from string to float manually
    transactions = []
    for row in csv.DictReader(file, skipinitialspace=True):
        new_dict = {}
        for k, v in row.items():
            if k in ['kuantitas', 'harga', 'jumlah']:
                v = float(v)
            new_dict[k] = v
        transactions.append(new_dict)

    # evaluate the transaction
    total_amount = sum(item['jumlah'] for item in transactions)
    highest_transcation_index = max(range(len(transactions)), key=lambda index: transactions[index]['jumlah']) + 1
    transaction_count = len(transactions)
    product_sold = [item['produk'] for item in transactions if item['kuantitas'] > 0]

    # prepare gui
    window = tk.Tk()
    window.columnconfigure(1, weight=1)
    
    total_amount_label = tk.Label(window, text="Total penjualan:")
    total_amount_label.grid(row=0, column=0, sticky=tk.E)
    total_amount_entry = tk.Entry(window)
    total_amount_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

    highest_transcation_label = tk.Label(window, text="Baris dengan nilai penjualan tertinggi:")
    highest_transcation_label.grid(row=1, column=0, sticky=tk.E)
    highest_transcation_entry = tk.Entry(window)
    highest_transcation_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

    transaction_count_label = tk.Label(window, text="Jumlah transaksi:")
    transaction_count_label.grid(row=2, column=0, sticky=tk.E)
    transaction_count_entry = tk.Entry(window)
    transaction_count_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

    table = ttk.Treeview(window)
    table["columns"] = ("no", "produk")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("no", anchor=tk.W, width=150)
    table.column("produk", anchor=tk.W, width=150)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("no", text="Nomor", anchor=tk.W)
    table.heading("produk", text="Produk", anchor=tk.W)
    table_title = tk.Label(window, text="Produk Terjual")
    table_title.grid(row=3, columnspan=2, pady=10)
    table.grid(row=4, columnspan=2, padx=10, pady=10)

    # set the value of gui using transaction evaluation result
    total_amount_entry.insert(0, total_amount)
    highest_transcation_entry.insert(0, highest_transcation_index)
    transaction_count_entry.insert(0, transaction_count)

    for index, product in enumerate(product_sold):
        table.insert("", tk.END, values=(index + 1, product))

    window.mainloop()