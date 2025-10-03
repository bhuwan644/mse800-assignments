"""Module for working with string operations."""

class StringProcessor:
    """Class representing a string processor."""

    def __init__(self, text: str) -> None:
        """Initialize with the provided text."""
        self.text = text

    def calculate_length(self) -> int:
        """Return the total length of the provided string."""
        return len(self.text)

    def find_length_of_uppercase(self) -> int:
        """Return the number of uppercase letters in the provided string."""
        return len([c for c in self.text if c.isupper()])



def main() -> None:
    """Main function to run the program."""
    input_string = input("Enter the text: ")
    provided_text = StringProcessor(input_string)

    print("Total length:", provided_text.calculate_length())
    print("Uppercase count:", provided_text.find_length_of_uppercase())


if __name__ == "__main__":
    main()
