GLWEC Virtual Prospectus

This project is a simple voice assistant powered by Python that answers frequently asked questions (FAQs) related to GLWEC (Gokaraju Lailavathi Womens Engineering College). It uses speech recognition to process the user's questions and fetches answers from a MySQL database. The system is designed to run with a graphical user interface (GUI) using Tkinter, and it supports both voice input and text-based output.

 Features

- **Speech Recognition**: Recognizes questions spoken by the user and provides answers.
- **Text-to-Speech**: Responds to the user via voice, providing answers to their queries.
- **FAQ Database**: Stores questions, keywords, and answers in a MySQL database for easy retrieval.
- **GUI**: Provides a simple and intuitive graphical interface for interaction.
  
 Technologies Used

- **Python**: Main programming language.
- **Tkinter**: Used for creating the GUI.
- **SpeechRecognition**: A Python library used for recognizing speech input.
- **pyttsx3**: A text-to-speech conversion library.
- **MySQL**: A relational database used to store questions, keywords, and answers.

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- Tkinter (Usually comes pre-installed with Python)
- MySQL
- `speechrecognition` library
- `pyttsx3` library
- `mysql-connector` library

### Install Dependencies

To install the required Python libraries, you can use the following pip commands:


pip install SpeechRecognition
pip install pyttsx3
pip install mysql-connector-python


## Setup

### 1. Set Up MySQL Database

Before running the script, set up the MySQL database by executing the following steps:

1. **Download the SQL script** from the `create_faq_db.sql` file in the repository.
2. **Run the script** to create the database and the FAQ table with sample data.

You can run the SQL script using MySQL Workbench or command line:


mysql -u root -p < create_faq_db.sql


Enter your MySQL password when prompted.

### 2. Update Database Connection Credentials

Make sure to update the database credentials in the `virtual.py` script to match your MySQL setup:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_responses"
)
```

### 3. Run the Application

1. **Run the Python script**:
   Open a terminal or command prompt and execute the following command:

  
   python virtual.py


2. The application will launch a window with buttons for interacting with the virtual assistant. You can start asking questions by clicking the **Start** button and stop the assistant using the **Stop** button.

### 4. Interact with the Voice Assistant

- Click on **Start** and ask a question like:
  - "Who is the principal?"
  - "What courses are offered?"
  - "What is the vision of the college?"
  
The assistant will listen to your query and respond with the relevant information from the database.

## Example Questions

Here are some examples of questions that the assistant can answer:

- "Who is the principal?"
- "What courses are offered?"
- "What is the vision of the college?"
- "What is the mission of the college?"
- "What departments are available?"

## Troubleshooting

- **Speech Recognition Issues**: Ensure that your microphone is properly connected and accessible by the script.
- **MySQL Connection Issues**: Verify that the database credentials are correct and that the MySQL server is running.
- **Missing Dependencies**: If you encounter issues related to missing libraries, make sure you've installed all the necessary Python packages using `pip`.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Please ensure your code adheres to the style guidelines used in the project.

