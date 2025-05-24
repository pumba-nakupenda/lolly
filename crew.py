class MiniBookCrew:
    """A simple crew that manages writers and generates mini-books."""

    def __init__(self):
        self.writers = []

    def add_writer(self, name):
        """Add a writer to the crew."""
        if name not in self.writers:
            self.writers.append(name)

    def generate_book(self, title, text):
        """Return a draft book string using the provided title and text."""
        header = f"# {title}\n\n"
        content = text.strip() + "\n"
        writer_info = "\nWriters: " + ", ".join(self.writers) + "\n" if self.writers else ""
        return header + content + writer_info
