import fitz
import joblib
import unittest
import os
from sklearn.feature_extraction.text import TfidfVectorizer

class TestPDFClassification(unittest.TestCase):
    def test_classify_and_move_pdfs(self):
        # Load the trained subject_classifier model and tfidf_vectorizer
        subject_classifier = joblib.load("subject_classifier_model.pkl")
        tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

        # Define the root directory where the PDFs are located
        root_directory = r"C:\Users\ASUS\OneDrive\Desktop\Training data\testing"

        # Walk through the root directory and its subdirectories
        for root, _, files in os.walk(root_directory):
            for filename in files:
                if filename.endswith(".pdf"):
                    # Create the full path to the PDF file
                    pdf_file_path = os.path.join(root, filename)

                    # Open the PDF file using PyMuPDF within a context manager
                    with fitz.open(pdf_file_path) as pdf_document:
                        # Extract text from the PDF
                        text = ''
                        for page_num in range(pdf_document.page_count):
                            page = pdf_document[page_num]
                            blocks = page.get_text("blocks")
                            for b in blocks:
                                if b[4].strip():
                                    text += b[4] + ' '

                    # Vectorize the text using the same TF-IDF vectorizer used during training
                    tfidf_matrix = tfidf_vectorizer.transform([text])  # Use transform, not fit_transform

                    # Predict the subject of the PDF
                    predicted_subject = subject_classifier.predict(tfidf_matrix)[0]

                    # Move the PDF to the corresponding subject folder
                    destination_folder = os.path.join(root_directory, predicted_subject)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    new_pdf_path = os.path.join(destination_folder, filename)

                    # Use shutil.move to avoid permission issues
                    import shutil
                    shutil.move(pdf_file_path, new_pdf_path)

                    # Check if the PDF has been moved to the correct folder
                    self.assertTrue(os.path.exists(new_pdf_path))

if __name__ == '__main__':
    unittest.main()
