import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from faker import Faker
import random
from ContactBook import ContactBook


class ContactBookApp:
    def __init__(self, root) -> None:
        """
        Initializes the ContactBookApp instance.
        :param root: The main Tkinter window where the application will be displayed.
        """
        self.book = ContactBook()
        self.root = root
        self.root.title("Книга контактів")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", rowheight=25, font=("Helvetica", 10))
        self.style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

        self.fake = Faker()

        self.create_widgets()
        self.load_contacts()
        self.generate_random_contacts()

    def create_widgets(self) -> None:
        """
        Creates and arranges the UI components such as buttons, treeview, and entry fields.
        """
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.tree = ttk.Treeview(
            self.frame, columns=("ID", "Name", "Phone", "Email", "Group"), show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Ім'я")
        self.tree.heading("Phone", text="Телефон")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Group", text="Група")
        self.tree.column("ID", width=50)
        self.tree.grid(row=0, column=0, columnspan=5, pady=5)

        self.btn_add = ttk.Button(self.frame, text="Додати", command=self.add_contact)
        self.btn_add.grid(row=1, column=0, padx=5, pady=5)

        self.btn_edit = ttk.Button(self.frame, text="Редагувати", command=self.edit_contact)
        self.btn_edit.grid(row=1, column=1, padx=5, pady=5)

        self.btn_delete = ttk.Button(self.frame, text="Видалити", command=self.delete_contact)
        self.btn_delete.grid(row=1, column=2, padx=5, pady=5)

        self.entry_search = ttk.Entry(self.frame)
        self.entry_search.grid(row=2, column=0, padx=5, pady=5)

        self.btn_search = ttk.Button(self.frame, text="Пошук", command=self.search_contact)
        self.btn_search.grid(row=2, column=1, padx=5, pady=5)

        self.group_filter = ttk.Combobox(self.frame, values=["Всі", "Робота", "Сім'я", "Друзі", "Інше"])
        self.group_filter.grid(row=2, column=2, padx=5, pady=5)
        self.group_filter.set("Всі")

        self.btn_change_theme = ttk.Button(self.frame, text="Змінити тему", command=self.change_theme)
        self.btn_change_theme.grid(row=1, column=3, padx=5, pady=5)

        self.btn_reset = ttk.Button(self.frame, text="Скинути", command=self.load_contacts)
        self.btn_reset.grid(row=2, column=3, padx=5, pady=5)

        self.btn_export = ttk.Button(self.frame, text="Експортувати", command=self.export_contacts)
        self.btn_export.grid(row=3, column=0, padx=5, pady=5)

        self.btn_import = ttk.Button(self.frame, text="Імпортувати", command=self.import_contacts)
        self.btn_import.grid(row=3, column=1, padx=5, pady=5)

    def load_contacts(self, sort_by: str = "id") -> None:
        """
        Loads and displays the contacts from the database into the Treeview.
        :param sort_by: The field to sort contacts by (default is "id").
        """
        group_name = self.group_filter.get() if self.group_filter.get() != "Всі" else None
        for row in self.tree.get_children():
            self.tree.delete(row)
        contacts = self.book.get_contacts(sort_by, group_name)
        for contact in contacts:
            self.tree.insert("", tk.END, values=contact)

    def search_contact(self) -> None:
        """
        Searches for contacts based on a keyword and applies a group filter.
        Displays the results in the Treeview.
        """
        keyword = self.entry_search.get()
        group = self.group_filter.get()

        results = self.book.search_contact(keyword)
        if group != "Всі":
            results = [contact for contact in results if contact[4] == group]

        for row in self.tree.get_children():
            self.tree.delete(row)

        for result in results:
            self.tree.insert("", tk.END, values=result)

    def export_contacts(self) -> None:
        """
        Exports the contacts to a CSV file. Prompts the user to choose a location and saves the contacts.
        Displays a success message after exporting.
        """
        contacts = self.book.get_contacts()
        file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file:
            with open(file, mode='w', newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Phone", "Email", "Group"])
                for contact in contacts:
                    writer.writerow(contact)
            messagebox.showinfo("Успіх", "Контакти експортовані!")

    def import_contacts(self) -> None:
        """
        Imports contacts from a CSV file. Prompts the user to select a file, reads the contact data,
        and adds them to the contact book. Displays a success message after importing.
        """
        file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file:
            with open(file, mode='r', encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.book.add_contact(row[1], row[2], row[3], row[4])
            self.load_contacts()
            messagebox.showinfo("Успіх", "Контакти імпортовані!")

    def change_theme(self) -> None:
        """
        Changes the theme of the application between 'clam' and 'alt'.
        If the current theme is 'clam', it switches to 'alt', and vice versa.
        """
        if self.style.theme_use() == "clam":
            self.style.theme_use("alt")
        else:
            self.style.theme_use("clam")

    def add_contact(self) -> None:
        """
        Opens a new window to add a contact to the contact book.
        It validates the input fields and adds the contact to the database if all fields are filled.
        """

        def save() -> None:
            """
            Saves the contact to the contact book after validating the input fields.
            If any required field is empty, a warning message is shown.
            """
            name = entry_name.get()
            phone = entry_phone.get()
            email = entry_email.get()
            group_name = entry_group.get()
            if not name or not phone or not email:
                messagebox.showwarning("Помилка", "Всі поля обов'язкові!")
                return
            self.book.add_contact(name, phone, email, group_name)
            self.load_contacts()
            messagebox.showinfo("Успіх", "Контакт додано!")
            add_window.destroy()

        add_window = tk.Toplevel(self.root)
        add_window.title("Додати контакт")
        tk.Label(add_window, text="Ім'я:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Телефон:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Група:").grid(row=3, column=0, padx=5, pady=5)

        entry_name = ttk.Entry(add_window)
        entry_name.grid(row=0, column=1, padx=5, pady=5)
        entry_phone = ttk.Entry(add_window)
        entry_phone.grid(row=1, column=1, padx=5, pady=5)
        entry_email = ttk.Entry(add_window)
        entry_email.grid(row=2, column=1, padx=5, pady=5)

        group_options = ["Робота", "Сім'я", "Друзі", "Інше"]
        entry_group = ttk.Combobox(add_window, values=group_options)
        entry_group.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(add_window, text="Зберегти", command=save).grid(row=4, column=0, columnspan=2, pady=10)

    def edit_contact(self) -> None:
        """
        Opens a new window to edit an existing contact.
        The selected contact is loaded, and the user can modify the details.
        If no contact is selected, a warning is shown.
        """
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Помилка", "Оберіть контакт для редагування.")
            return
        contact_id = self.tree.item(selected)["values"][0]
        contact_data = self.book.get_contacts("id")
        contact_data = next((c for c in contact_data if c[0] == contact_id), None)
        if not contact_data:
            return
        name, phone, email, group_name = contact_data[1], contact_data[2], contact_data[3], contact_data[4]

        def save() -> None:
            """
            Opens a new window to edit an existing contact. The selected contact's details are preloaded
            into the input fields. After editing, the user can save the changes. If any required fields are empty,
            a warning is shown.
            Updates the contact information in the database and reloads the contacts list.
            """
            new_name = entry_name.get()
            new_phone = entry_phone.get()
            new_email = entry_email.get()
            new_group_name = entry_group.get()
            self.book.edit_contact(contact_id, new_name, new_phone, new_email, new_group_name)
            self.load_contacts()
            messagebox.showinfo("Успіх", "Контакт відредаговано!")
            edit_window.destroy()

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Редагувати контакт")

        tk.Label(edit_window, text="Ім'я:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="Телефон:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="Група:").grid(row=3, column=0, padx=5, pady=5)

        entry_name = ttk.Entry(edit_window)
        entry_name.insert(0, name)
        entry_name.grid(row=0, column=1, padx=5, pady=5)
        entry_phone = ttk.Entry(edit_window)
        entry_phone.insert(0, phone)
        entry_phone.grid(row=1, column=1, padx=5, pady=5)
        entry_email = ttk.Entry(edit_window)
        entry_email.insert(0, email)
        entry_email.grid(row=2, column=1, padx=5, pady=5)

        entry_group = ttk.Combobox(edit_window, values=["Робота", "Сім'я", "Друзі", "Інше"])
        entry_group.set(group_name)
        entry_group.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(edit_window, text="Зберегти", command=save).grid(row=4, column=0, columnspan=2, pady=10)

    def delete_contact(self) -> None:
        """
        Deletes the selected contact from the contact list. If no contact is selected,
        a warning is shown. After deletion, the contact list is reloaded to reflect the changes.
        If the contact is successfully deleted, a success message is displayed.
        """
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Помилка", "Оберіть контакт для видалення.")
            return
        contact_id = self.tree.item(selected)["values"][0]
        self.book.delete_contact(contact_id)
        self.load_contacts()
        messagebox.showinfo("Успіх", "Контакт видалено!")

    def generate_random_contacts(self) -> None:
        """
        Generates 10 random contacts using the Faker library and adds them to the contact book.
        Each contact includes a random name, phone number, email, and a randomly chosen group
        from the list ["Робота", "Сім'я", "Друзі", "Інше"].
        This method does not return any value but populates the contact book with random data.
        """
        for _ in range(10):
            name = self.fake.name()
            phone = self.fake.phone_number()
            email = self.fake.email()
            group = random.choice(["Робота", "Сім'я", "Друзі", "Інше"])
            self.book.add_contact(name, phone, email, group)
