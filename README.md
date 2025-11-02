# 📚 UIC Campus Library Catalog System:


Developed by ANKIT PANDEY

UID: 25MCD10070

Course: MCA Data Science (DS)

Department: UIC (University Institute of Computing)

Subject: Python Programming (25CAH-606)

Semester: 1st
________________________________________
# 🧩 Project Overview


UIC Campus Library Catalog System is a Python-based desktop application designed to manage and organize books in a campus library.

It allows users to add, remove, borrow, and return books through an interactive Tkinter-based cyber-themed interface.

The system stores data persistently in JSON format, ensuring records are maintained even after the program is closed.

It also supports real-time search and book categorization (Fiction, Non-Fiction, Reference), helping librarians and students efficiently navigate the digital catalog.

________________________________________

# 🚀 Features Implemented


✅ Add, remove, borrow, and return books

✅ Search books by title or author

✅ Categorization into Fiction, Non-Fiction, and Reference

✅ Persistent data storage using JSON

✅ Automatic tracking of borrowed and returned timestamps

✅ Cyber-themed GUI with dynamic hover effects

✅ Colored status indicators (Available / Borrowed)

________________________________________

# 🛠️ Tech Stack

Component	Technology Used

Frontend/UI	Tkinter (Custom cyber-themed UI)

Backend Storage	JSON (Persistent local storage)

Language	Python

Libraries Used	tkinter, ttk, json, datetime, os

________________________________________

# 🖥️ How to Run

1️⃣ Clone the Repository

https://github.com/ankitpandey67/UIC_campus_liberly_catlog_system.git

2️⃣ (Optional) Create and Activate Virtual Environment

For Windows:

python -m venv venv

venv\Scripts\activate

For Mac/Linux:

python3 -m venv venv

source venv/bin/activate

3️⃣ Install Required Libraries

pip install tkinter

(Tkinter is usually pre-installed with Python. If not, install manually.)

4️⃣ Run the Project


python UIC_Campus_liberly_catlog.py

________________________________________

# 📂 File Structure

UIC-Library-Catalog/

│
├── UIC_Campus_liberly_catlog.py .py       # Main application file
├── library_data.json           # JSON file for saving catalog data
└── README.md                   # Project documentation
________________________________________

# 🧠 How It Works

•	Add Book → Opens a dialog to add new books with title, author, genre, and type.

•	Remove Book → Deletes a book from the catalog permanently.

•	Borrow Book → Marks a book as borrowed and stores the timestamp.

•	Return Book → Marks a borrowed book as returned and updates records.

•	Search → Dynamically filters books by title or author.

________________________________________

# 🎨 UI Highlights

•	Futuristic dark-themed interface (#0f0f0f background).

•	Neon glow text (#00ffea and #00ffaa).

•	Hover effects for buttons with color transitions.

•	Intuitive, centered layout for smooth navigation.

________________________________________

# 🧾 Example Book Entry (Stored in JSON)
{
    "title": "Artificial Intelligence",
    "author": "Stuart Russell",
    "genre": "Technology",
    "available": false,
    "borrowed_on": "2025-11-02 10:30:00",
    "returned_on": null,
    "book_type": "Non-Fiction"
}
________________________________________

# 💡 Future Enhancements

🔹 Integrate SQLite for advanced data management

🔹 Add user authentication for librarians and students

🔹 Include analytics dashboard (borrow stats, most popular books)

🔹 Add PDF export of library reports

________________________________________

# 📜 License

This project is developed as part of MCA Data Science (DS) coursework at University Institute of Computing (UIC).

It is free for academic and non-commercial use.

________________________________________
# 👨‍💻 Developer

ANKIT PANDEY

📧 MCA Data Science | UIC

📘 Python Programming Project — Semester 1

