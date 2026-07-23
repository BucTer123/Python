import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("WINDOW!")

    tk.Label(root, text="Welcome!").pack()

    entry_text = tk.Label(root, text="> ")
    entry_text.pack()
    entry = tk.Entry(root)
    entry.pack()
    
    root.mainloop()
    exit(0)
if __name__ == "__main__":
    main()
