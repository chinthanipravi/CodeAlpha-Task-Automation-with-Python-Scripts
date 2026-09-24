import re


def extract_emails(input_file, output_file):
    """Extracts all valid email addresses from input_file and saves them to output_file."""
    # Regular expression pattern for matching email addresses
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    try:
        # Read the source file
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Find all email matches
        emails = re.findall(email_pattern, content)

        # Remove duplicates and sort alphabetically
        unique_emails = sorted(list(set(emails)))

        # Write extracted emails to the target file
        with open(output_file, "w", encoding="utf-8") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print(
            f"Automation Complete: Found {len(unique_emails)} unique email(s). Saved to '{output_file}'."
        )

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")


if __name__ == "__main__":
    INPUT_TXT = "sample_data.txt"
    OUTPUT_TXT = "extracted_emails.txt"

    extract_emails(INPUT_TXT, OUTPUT_TXT)