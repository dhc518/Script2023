import csv
import tkinter as tk
from tkinter import filedialog


class CsvWriter:
    def __init__(self, root):
        self.root = root
        self.root.title("CsvWriter")
        self.root.geometry("500x600")

        # Label and Entry widgets for data input
        tk.Label(self.root, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Age").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Country").grid(row=2, column=0)
        self.country_entry = tk.Entry(self.root)
        self.country_entry.grid(row=2, column=1)

        # Button to save data
        tk.Button(self.root, text="Save", command=self.save_data).grid(row=3, column=0, columnspan=2)

    def save_data(self):
        # Get the file path to save the data
        file_path = filedialog.asksaveasfilename(title="Save CSV File", filetypes=[("CSV files", "*.csv")])

        # If user cancels the file dialog, return
        if not file_path:
            return

        # Create the list of data to be saved
        data = [
            [self.name_entry.get(), self.age_entry.get(), self.country_entry.get()]
        ]

        # Write the data to the CSV file
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)


if __name__ == '__main__':
    root = tk.Tk()
    app = CsvWriter(root)
    root.mainloop()



