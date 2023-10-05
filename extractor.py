def extract_pdf_data(txt_file_path):
    # Initialize an empty list to store labeled PDF data
    labeled_pdfs = []

    try:
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                # Split each line into components: file_path, subject, section
                components = line.strip().split(',')
                if len(components) == 3:
                    pdf_file_path = components[0].strip().strip('"')  # Remove quotation marks
                    subject = components[1].strip()
                    section = components[2].strip()
                    labeled_pdfs.append((pdf_file_path, subject, section))
                else:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"Error: File '{txt_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return labeled_pdfs

print(extract_pdf_data(r"C:\Users\ASUS\OneDrive\Desktop\Automation Project\labeled_pdfs.txt"))


