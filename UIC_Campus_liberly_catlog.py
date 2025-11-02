
import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os


# Book Classes


class Book:
    def __init__(self, title, author, genre, available=True, borrowed_on=None, returned_on=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.borrowed_on = borrowed_on
        self.returned_on = returned_on
        self.book_type = "General"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "available": self.available,
            "borrowed_on": self.borrowed_on,
            "returned_on": self.returned_on,
            "book_type": self.book_type
        }

    @staticmethod
    def from_dict(data):
        b_type = data.get("book_type", "General")
        if b_type == "Fiction":
            return FictionBook(data["title"], data["author"], data["genre"], data["available"], data["borrowed_on"], data["returned_on"])
        elif b_type == "Non-Fiction":
            return NonFictionBook(data["title"], data["author"], data["genre"], data["available"], data["borrowed_on"], data["returned_on"])
        elif b_type == "Reference":
            return ReferenceBook(data["title"], data["author"], data["genre"], data["available"], data["borrowed_on"], data["returned_on"])
        else:
            return Book(data["title"], data["author"], data["genre"], data["available"], data["borrowed_on"], data["returned_on"])

class FictionBook(Book):
    def __init__(self, title, author, genre, available=True, borrowed_on=None, returned_on=None):
        super().__init__(title, author, genre, available, borrowed_on, returned_on)
        self.book_type = "Fiction"

class NonFictionBook(Book):
    def __init__(self, title, author, genre, available=True, borrowed_on=None, returned_on=None):
        super().__init__(title, author, genre, available, borrowed_on, returned_on)
        self.book_type = "Non-Fiction"

class ReferenceBook(Book):
    def __init__(self, title, author, genre, available=True, borrowed_on=None, returned_on=None):
        super().__init__(title, author, genre, available, borrowed_on, returned_on)
        self.book_type = "Reference"

# ------------------------
# Library Catalog with Persistence
# ------------------------

class LibraryCatalog:
    def __init__(self, filename="library_data.json"):
        self.books = []
        self.filename = filename
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_data()
                return True
        return False

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

    def get_all_books(self):
        return self.books

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                book.borrowed_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_data()
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                book.returned_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_data()
                return True
        return False

    def save_data(self):
        data = [book.to_dict() for book in self.books]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]


# Cyber UI
# ------------------------

class LibraryUI:
    def __init__(self, root):
        self.catalog = LibraryCatalog()
        self.root = root
        self.root.title("UIC Campus Library Catalog")
        self.root.geometry("1000x600")
        self.root.configure(bg="#0f0f0f")
        self.root.resizable(False, False)

        self.create_widgets()
        self.update_book_list()

    def create_widgets(self):
        # Title
        tk.Label(
            self.root, text="UIC Campus Library Catalog",
            font=("Orbitron", 24, "bold"), fg="#00ffea", bg="#0f0f0f"
        ).pack(pady=10)

        # Search bar
        search_frame = tk.Frame(self.root, bg="#0f0f0f")
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Search:", font=("Consolas", 12), fg="#00ffaa", bg="#0f0f0f").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.perform_search)
        tk.Entry(search_frame, textvariable=self.search_var, width=40, font=("Consolas", 12)).pack(side="left", padx=5)

        # Treeview style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#0f0f0f",
                        foreground="#00ffea",
                        rowheight=28,
                        fieldbackground="#0f0f0f",
                        font=("Consolas", 11))
        style.map("Treeview", background=[('selected', '#00ffaa')], foreground=[('selected', '#0f0f0f')])

        # Treeview
        self.tree = ttk.Treeview(self.root,
                                 columns=("Title", "Author", "Genre", "Type", "Status", "Borrowed On", "Returned On"),
                                 show='headings')
        columns = self.tree["columns"]
        for col in columns:
            width = 150 if col != "Title" else 220
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
        self.tree.pack(pady=15, fill="x", padx=20)

        # Buttons frame
        frame = tk.Frame(self.root, bg="#0f0f0f")
        frame.pack(pady=10)

        # Cyber buttons with hover effect
        self.buttons = {}
        btn_names = [("Add Book", self.add_book),
                     ("Remove Book", self.remove_book),
                     ("Borrow Book", self.borrow_book),
                     ("Return Book", self.return_book)]
        for i, (text, command) in enumerate(btn_names):
            btn = tk.Button(frame, text=text, width=15, bg="#0f0f0f", fg="#00ffea",
                            font=("Consolas", 11, "bold"), bd=2, relief="raised", activebackground="#00ffaa", activeforeground="#0f0f0f",
                            command=command)
            btn.grid(row=0, column=i, padx=5, pady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#00ffaa", fg="#0f0f0f"))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#0f0f0f", fg="#00ffea"))
            self.buttons[text] = btn

    def update_book_list(self, books=None):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if books is None:
            books = self.catalog.get_all_books()
        for book in books:
            status = "Available" if book.available else "Borrowed"
            borrowed_on = book.borrowed_on if book.borrowed_on else "-"
            returned_on = book.returned_on if book.returned_on else "-"
            row_tag = "available" if book.available else "borrowed"
            self.tree.insert("", "end", values=(book.title, book.author, book.genre, book.book_type,
                                                status, borrowed_on, returned_on), tags=(row_tag,))
        self.tree.tag_configure("available", background="#0f0f0f", foreground="#00ff00")
        self.tree.tag_configure("borrowed", background="#0f0f0f", foreground="#ff0040")

    def perform_search(self, *args):
        keyword = self.search_var.get()
        if keyword:
            results = self.catalog.search_books(keyword)
            self.update_book_list(results)
        else:
            self.update_book_list()

    def add_book(self):
        add_win = tk.Toplevel(self.root)
        add_win.title("Add New Book")
        add_win.geometry("400x350")
        add_win.configure(bg="#0f0f0f")
        add_win.resizable(False, False)

        tk.Label(add_win, text="Add New Book", font=("Orbitron", 16, "bold"), fg="#00ffea", bg="#0f0f0f").pack(pady=10)

        fields = [("Title", ""), ("Author", ""), ("Genre/Subject/Topic", ""), ("Book Type", "Fiction/Non-Fiction/Reference")]
        entries = {}
        for f, val in fields:
            tk.Label(add_win, text=f, font=("Consolas", 12), fg="#00ffaa", bg="#0f0f0f").pack()
            e = tk.Entry(add_win, width=30, font=("Consolas", 12))
            e.pack(pady=5)
            entries[f] = e

        def save_book():
            title = entries["Title"].get()
            author = entries["Author"].get()
            genre = entries["Genre/Subject/Topic"].get()
            b_type = entries["Book Type"].get().lower()
            if b_type == "fiction":
                book = FictionBook(title, author, genre)
            elif b_type == "non-fiction":
                book = NonFictionBook(title, author, genre)
            elif b_type == "reference":
                book = ReferenceBook(title, author, genre)
            else:
                messagebox.showerror("Error", "Invalid Book Type!")
                return
            self.catalog.add_book(book)
            self.update_book_list()
            messagebox.showinfo("Success", f"Book '{title}' added!")
            add_win.destroy()

        tk.Button(add_win, text="Add Book", font=("Consolas", 12, "bold"), bg="#0f0f0f", fg="#00ffea",
                  activebackground="#00ffaa", activeforeground="#0f0f0f", bd=2, relief="raised", command=save_book).pack(pady=20)

    def remove_book(self):
        selected = self.tree.focus()
        if not selected: messagebox.showwarning("Warning", "Select a book to remove!"); return
        title = self.tree.item(selected, "values")[0]
        if self.catalog.remove_book(title):
            self.update_book_list()
            messagebox.showinfo("Removed", f"Book '{title}' removed successfully.")
        else:
            messagebox.showerror("Error", "Book not found!")

    def borrow_book(self):
        selected = self.tree.focus()
        if not selected: messagebox.showwarning("Warning", "Select a book to borrow!"); return
        title = self.tree.item(selected, "values")[0]
        if self.catalog.borrow_book(title):
            self.update_book_list()
            messagebox.showinfo("Success", f"You borrowed '{title}'.")
        else:
            messagebox.showwarning("Unavailable", "Book is not available!")

    def return_book(self):
        selected = self.tree.focus()
        if not selected: messagebox.showwarning("Warning", "Select a book to return!"); return
        title = self.tree.item(selected, "values")[0]
        if self.catalog.return_book(title):
            self.update_book_list()
            messagebox.showinfo("Returned", f"Book '{title}' returned successfully.")
        else:
            messagebox.showerror("Error", "Book not found!")

# ------------------------
# Run App
# ------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryUI(root)
    root.mainloop()
