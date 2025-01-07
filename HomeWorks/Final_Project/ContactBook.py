import sqlite3
import re
from tkinter import messagebox


class ContactBook:
    def __init__(self, db_name: str = "contacts.db") -> None:
        """
        Initializes a ContactBook object.
        :param db_name: The name of the database file. Default is 'contacts.db'.
        """
        self.connection = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self) -> None:
        """
        Creates the contacts table if it does not exist in the database.
        The table includes fields for ID, name, phone number, email, and group name.
        """
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                group_name TEXT DEFAULT 'General'
            )
            """)

    def add_contact(self, name: str, phone: str, email: str, group_name: str) -> None:
        """
        Adds a new contact to the database.
        :param name: The name of the contact.
        :param phone: The phone number of the contact.
        :param email: The email address of the contact.
        :param group_name: The group the contact belongs to.
        """
        formatted_phone = self.format_phone(phone)
        formatted_email = self.format_email(email)
        if formatted_email:
            with self.connection:
                self.connection.execute(
                    "INSERT INTO contacts (name, phone, email, group_name) VALUES (?, ?, ?, ?)",
                    (name, formatted_phone, formatted_email, group_name)
                )
        else:
            messagebox.showwarning("Помилка", "Невірний формат email!")

    def get_contacts(self, sort_by: str = "name", group_name: str = None) -> list[tuple]:
        """
        Retrieves a list of contacts from the database, optionally filtered by group and sorted.
        :param sort_by: The field by which to sort the results (default is "name").
        :param group_name: The name of the group to filter by (optional).
        :return: A list of tuples containing contact details.
        """
        query = "SELECT id, name, phone, email, group_name FROM contacts"
        params = []
        if group_name:
            query += " WHERE group_name = ?"
            params.append(group_name)
        query += f" ORDER BY {sort_by}"
        with self.connection:
            return self.connection.execute(query, params).fetchall()

    def edit_contact(self, contact_id: int, name: str, phone: str, email: str, group_name: str) -> None:
        """
        Edits an existing contact in the database.
        :param contact_id: The ID of the contact to be edited.
        :param name: The updated name of the contact.
        :param phone: The updated phone number of the contact.
        :param email: The updated email address of the contact.
        :param group_name: The updated group name of the contact.
        """
        formatted_phone = self.format_phone(phone)
        formatted_email = self.format_email(email)
        if formatted_email:
            with self.connection:
                self.connection.execute(
                    """
                    UPDATE contacts
                    SET name = ?, phone = ?, email = ?, group_name = ?
                    WHERE id = ?
                    """,
                    (name, formatted_phone, formatted_email, group_name, contact_id)
                )
        else:
            messagebox.showwarning("Помилка", "Невірний формат email!")

    def delete_contact(self, contact_id: int) -> None:
        """
        Deletes a contact from the database.
        :param contact_id: The ID of the contact to be deleted.
        """
        with self.connection:
            self.connection.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))

    def search_contact(self, keyword: str, group_name: str = None) -> list:
        """
        Searches for contacts in the database based on a keyword and optional group name.
        :param keyword: The keyword to search for in the contact's name, phone, or email.
        :param group_name: Optional group name to filter the contacts by. Default is None.
        :return: A list of contacts matching the search criteria.
        """
        query = """
        SELECT id, name, phone, email, group_name
        FROM contacts
        WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?
        """
        params = [f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"]
        if group_name:
            query += " AND group_name = ?"
            params.append(group_name)
        with self.connection:
            return self.connection.execute(query, params).fetchall()

    def is_unique(self, phone: str, email: str, contact_id: int = None) -> bool:
        """
        Checks if the given phone number and email are unique in the database.
        :param phone: The phone number to check.
        :param email: The email to check.
        :param contact_id: Optional contact ID to exclude from the check. Default is None.
        :return: True if the phone and email are unique, False otherwise.
        """
        with self.connection:
            query = "SELECT id FROM contacts WHERE (phone = ? OR email = ?)"
            params = [phone, email]
            if contact_id:
                query += " AND id != ?"
                params.append(contact_id)
            return not self.connection.execute(query, params).fetchone()

    def close(self) -> None:
        """
        Closes the connection to the database.
        """
        self.connection.close()

    def format_phone(self, phone: str) -> str:
        """
        Formats the phone number by removing non-digit characters and ensuring it follows a specific format.
        :param phone: The phone number as a string.
        :return: The formatted phone number if valid, otherwise the original phone number.
        """
        phone = re.sub(r'\D', '', phone)
        if len(phone) == 12 and phone.startswith('380'):
            return f"+{phone}"
        return phone

    def format_email(self, email: str) -> str | None:
        """
        Validates and formats the email address.
        :param email: The email address as a string.
        :return: The email address if it is valid, otherwise None.
        """
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        return None
