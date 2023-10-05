# automation_project
#Author: Omar Sebri
The following is an automation file management project for University students that scans the courses of their PDFs and places them
in their corresponding folder.
The following program has an accuracy of 95% and has been tested using unittest.py
In order to run this Project you must:
1-Ensure all the following libraries are installed:
  ScikitLearn
  Joblib
  Fitz
2-Make sure your train the model with your own documents:
Makse sure you create a .txt file that has in each line : directory to the pdf, the course name and the course section (3 values seprated by a comma)
You don't have to use many pdfs for each subject since this model uses a naive bayes which a great model for training small data with good accuracy.
Make sure you paste the directory to your .txt file in the extractor.py
3-Run model.py: this is the model that will be trained to classify your data
4-Paste the PDFs you want to oragnize in the root directory and run classifier.py: you will notice a new folder named Organized_PDFs appeared within it there is
a folder for each subject and each folder contains the appropriate files.
Make sure you double your check your folders since errors are possible despite being highly unlikely.
