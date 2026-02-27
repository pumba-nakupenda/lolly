from crew import MiniBookCrew


def main():
    crew = MiniBookCrew()
    crew.add_writer("Alice")
    sample_text = "This is a sample mini-book created by the crew."
    book = crew.generate_book("Sample Book", sample_text)
    print(book)


if __name__ == "__main__":
    main()
