import tkinter as tk

def btn_callback():
    print("Bye!")
    exit(0)

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Window")

    tk.Button(root, text="Click", command=btn_callback)

    root.mainloop()
    exit(0)

if __name__ == "__main__":
    main()