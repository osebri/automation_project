import fitz
from extractor import extract_pdf_data
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Data Collection (Assuming you have labeled PDFs)
# ... Code to collect and label PDFs ...

# Step 2: Data Preprocessing
pdf_texts = []
subject_labels = []
section_labels = []
labeled_pdfs = extract_pdf_data(r"C:\Users\ASUS\OneDrive\Desktop\Automation Project\labeled_pdfs.txt")

for pdf_file_path, subject, section in labeled_pdfs:
    doc = fitz.open(pdf_file_path)
    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        for b in blocks:
            if b[4].strip():  # Check if the block contains text
                text += b[4] + ' '  # Concatenate block text
    pdf_texts.append(text)
    subject_labels.append(subject)
    section_labels.append(section)

# Step 3: TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(pdf_texts)

# Step 4: Model Selection and Splitting
X_train, X_test, y_train_subject, y_test_subject, y_train_section, y_test_section = train_test_split(
    tfidf_matrix, subject_labels, section_labels, test_size=0.2, random_state=42
)

# Step 5: Model Training for Subject Classification
subject_classifier = MultinomialNB()
subject_classifier.fit(X_train, y_train_subject)

# Step 6: Model Evaluation for Subject Classification
y_pred_subject = subject_classifier.predict(X_test)
subject_accuracy = accuracy_score(y_test_subject, y_pred_subject)
print(f'Subject Classification Accuracy: {subject_accuracy:.2f}')

# Print classification report for subject classification
subject_classification_rep = classification_report(y_test_subject, y_pred_subject)
print(f'Subject Classification Report:\n{subject_classification_rep}')

# Step 7: Model Training for Section Classification (Repeat for section)
section_classifier = MultinomialNB()
section_classifier.fit(X_train, y_train_section)

# Step 8: Model Evaluation for Section Classification
y_pred_section = section_classifier.predict(X_test)
section_accuracy = accuracy_score(y_test_section, y_pred_section)
print(f'Section Classification Accuracy: {section_accuracy:.2f}')

# Print classification report for section classification
section_classification_rep = classification_report(y_test_section, y_pred_section)
print(f'Section Classification Report:\n{section_classification_rep}')
joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(subject_classifier, "subject_classifier_model.pkl")
