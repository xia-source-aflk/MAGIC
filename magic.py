"""import tkinter as tk


root = tk.Tk()
root.title("Yuna's Magic🪄🧝🏻‍♀️🔮🎩")
root.geometry("1000x200")
root.configure(bg="black")

title= tk.Label(root, text="-think of a number form 1 to 100", width=65, font=("Arial", 15, "bold"), fg="white", bg="black")
title.place(relx=0.3, rely= 0.2, x=-500, y=-8)
entry = tk.Entry(root, width=65, font= ("Arial", 20), bg= "black", fg="white")
entry.place(relx=0.5, rely=0.4, anchor="center")


guess = int(input("think of a number form 1-100 "))

button = tk.Button(
    root,
    text="READ MY MIND",
    font=("Arial", 14, "bold"),
    bg="purple",
    fg="white",
    command=lambda: print("You clicked READ MY MIND!")
)

button.place(relx=0.5, rely=0.7, anchor="center")
root.mainloop()"""




import tkinter as tk
from PIL import Image, ImageTk

# ==============================
# MAIN WINDOW
# ==============================

root = tk.Tk()
root.title("Yuna's Magic 🪄🧝🏻‍♀️🔮🎩")
root.geometry("1000x200")
root.configure(bg="black")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="- Think of a number from 1 to 100 -",
    width=65,
    font=("Arial", 15, "bold"),
    fg="white",
    bg="black"
)
title.place(relx=0.3, rely=0.2, x=-500, y=-8)

# Entry box
entry = tk.Entry(
    root,
    width=65,
    font=("Arial", 20),
    bg="black",
    fg="white",
    justify="center"
)
entry.place(relx=0.5, rely=0.4, anchor="center")


# ==============================
# MAGIC FUNCTION
# ==============================

def read_my_mind():

    number = entry.get()

    # Check the entered number
    if not number.isdigit() or not 1 <= int(number) <= 100:

        error = tk.Toplevel(root)
        error.title("Oops!")
        error.geometry("350x120")
        error.configure(bg="black")

        tk.Label(
            error,
            text="Please choose a number from 1 to 100!",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="black"
        ).pack(expand=True)

        return

    number = int(number)

    # ==============================
    # MAGIC LOADING WINDOW
    # ==============================

    magic = tk.Toplevel(root)
    magic.title("Yuna's Magic 🔮")
    magic.geometry("500x450")
    magic.configure(bg="black")
    magic.resizable(False, False)

    messages = [
        "✨ Connecting to the magical universe...",
        "🔮 Reading your mind...",
        "🧠 Searching your brain...",
        "🪄 Detecting your secret thoughts...",
        "✨ Almost there... I can feel it!",
        "🎩 Revealing your secret number..."
    ]

    message_label = tk.Label(
        magic,
        text="",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="black",
        wraplength=460
    )
    message_label.pack(pady=15)

    # ==============================
    # POTION BOTTLE
    # ==============================

    canvas = tk.Canvas(
        magic,
        width=180,
        height=250,
        bg="black",
        highlightthickness=0
    )
    canvas.pack()

    # Bottle cap
    canvas.create_rectangle(
        65, 10, 115, 25,
        fill="purple",
        outline="white",
        width=2
    )

    # Bottle neck
    canvas.create_rectangle(
        70, 25, 110, 90,
        outline="white",
        width=3
    )

    # Bottle body
    canvas.create_rectangle(
        40, 85, 140, 235,
        outline="white",
        width=3
    )

    # Magical liquid
    liquid = canvas.create_rectangle(
        43, 232, 137, 232,
        fill="#A020F0",
        outline=""
    )

    # ==============================
    # FUNNY PICTURE WINDOW
    # ==============================

    def show_funny_picture():

        funny = tk.Toplevel(root)
        funny.title("THE MAGICIAN! 😂")
        funny.geometry("500x550")
        funny.configure(bg="black")
        funny.resizable(False, False)

        tk.Label(
            funny,
            text="Here you go!!! the brilliant magician!!YAAAAA!!!",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="black"
        ).pack(pady=20)

        # Load your picture
        img = Image.open(
            r"C:\Users\aaa\Downloads\yuna.jpeg"
        )

        img.thumbnail((400, 350))

        photo = ImageTk.PhotoImage(img)

        picture = tk.Label(
            funny,
            image=photo,
            bg="black"
        )
        picture.image = photo
        picture.pack()

        tk.Label(
            funny,
            text="Your welcome!",
            font=("Arial", 13, "bold"),
            fg="#E879F9",
            bg="black"
        ).pack(pady=20)

    # ==============================
    # NUMBER REVEAL
    # ==============================

    def reveal():

        for widget in magic.winfo_children():
            widget.destroy()

        tk.Label(
            magic,
            text="🔮 I READ YOUR MIND! 🔮",
            font=("Arial", 20, "bold"),
            fg="#D8B4FE",
            bg="black"
        ).pack(pady=35)

        tk.Label(
            magic,
            text="The number you were thinking of is...",
            font=("Arial", 13),
            fg="white",
            bg="black"
        ).pack(pady=10)

        tk.Label(
            magic,
            text=str(number),
            font=("Arial", 50, "bold"),
            fg="#E879F9",
            bg="black"
        ).pack(pady=10)

        tk.Label(
            magic,
            text="I told you I was SPEACIAL! 🪄😂",
            font=("Arial", 13, "italic"),
            fg="white",
            bg="black"
        ).pack(pady=10)

        # Open funny picture after 2 seconds
        magic.after(2000, show_funny_picture)

    # ==============================
    # LOADING ANIMATION
    # ==============================

    def loading(step=0):

        if step < len(messages):

            message_label.config(
                text=messages[step]
            )

            magic.after(
                3000,
                lambda: loading(step + 1)
            )

        else:
            reveal()

    # ==============================
    # POTION FILLING ANIMATION
    # ==============================

    def fill_bottle(level=0):

        if level <= 100:

            bottom = 232
            top = 232 - (level * 1.45)

            canvas.coords(
                liquid,
                43, top, 137, bottom
            )

            magic.after(
                180,
                lambda: fill_bottle(level + 1)
            )

    # Start both animations
    loading()
    fill_bottle()


# ==============================
# MAGIC BUTTON
# ==============================

button = tk.Button(
    root,
    text="READ MY MIND 🔮",
    font=("Arial", 14, "bold"),
    bg="purple",
    fg="white",
    activebackground="#A020F0",
    activeforeground="white",
    command=read_my_mind
)

button.place(
    relx=0.5,
    rely=0.7,
    anchor="center"
)


# ==============================
# RUN APPLICATION
# ==============================

root.mainloop()

