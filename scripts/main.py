import time
import tkinter as tk
from tkinter import ttk
from scrapers.homes_com_scrape import begin_scrape




def main():
    global result_text
    root = tk.Tk()
    root.title("Web Scraper")
    # root.geometry("300x200")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Location:").grid(column=1, row=1, sticky=tk.W)
    location_entry = ttk.Entry(frame, width=50)
    location_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
    
    ttk.Label(frame, text="For Sale or Rent:").grid(column=1, row=3, sticky=tk.W)
    status_entry = ttk.Entry(frame, width=50)
    status_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

    scrape_button = ttk.Button(frame, text="Scrape", command=lambda: scrape(location_entry, status_entry))
    scrape_button.grid(column=1, row=5, sticky=tk.W)

    # result_label = ttk.Label(frame, text="Results")
    # result_label.grid(column=1, row=6, columnspan=3, sticky=(tk.W, tk.E))
    result_text = tk.Text(frame, width=50, height=10, wrap='word')
    result_text.grid(column=1, row=6, columnspan=3, sticky=(tk.W, tk.E))

    root.mainloop()


def scrape(location_entry, status_entry):
    location = location_entry.get()
    status = status_entry.get()

    results = begin_scrape(location, status)


    result_text.delete(1.0, tk.END)

    result_text.insert(tk.END, results)






if __name__ == "__main__":
    main()