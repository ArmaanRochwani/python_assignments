import pdfplumber

class File_comparison: # class oops
    def __init__(self, file1_path, file2_path): # constructor
        
        # Initializes the File_comparison with two PDF file paths.
        # :param file1_path: Path to the first PDF file.
        # :param file2_path: Path to the second PDF file.
        
        self.file1_path = file1_path # self is instance variables oops
        self.file2_path = file2_path 

    def extracting_text_from_the_pdf(self, file_path):   
        
        # Extract text from a PDF file and return it as a list of lines.
        # :param file_path: Path to the PDF file.
        # :return: List of lines in the file.
        
        with pdfplumber.open(file_path) as pdf:
            text_lines = []
            for page in pdf.pages:
                text = page.extract_text()  # Extract text from the page
                if text:
                    # Split the text into individual lines and extend the list
                    text_lines.extend(text.splitlines())
        return text_lines

    def comparing_two_files(self):
        
        # Compare the two PDF files and print the differences line by line.
        
        # Extract text from both PDF files
        file1_lines = self.extracting_text_from_the_pdf(self.file1_path)
        file2_lines = self.extracting_text_from_the_pdf(self.file2_path)

        # Determine the number of lines to compare
        try:
            total_lines = max(len(file1_lines), len(file2_lines))
        except:
            print("An error occured")

        # Compare each line and print differences
        for i in range(total_lines):
            line1 = file1_lines[i] if i < len(file1_lines) else ""
            line2 = file2_lines[i] if i < len(file2_lines) else ""

            if line1 != line2:
                print(f"Difference at line {i + 1}:")
                print(f"File 1: {line1}")
                print(f"File 2: {line2}")
                print("-" * 40)

# Example usage:
if __name__ == "__main__":
    file1 = 'file1.pdf'  # Path to the first PDF file
    file2 = 'file2.pdf'  # Path to the second PDF file
    
    comparator = File_comparison(file1, file2)  # Initialize the File_comparison object # object created oops
    comparator.comparing_two_files()  # Compare the two files
