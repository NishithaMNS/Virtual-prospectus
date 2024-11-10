import tkinter
import mysql.connector
import pyttsx3
import speech_recognition as sr

# Initialize speech recognition and synthesis
r = sr.Recognizer()
a = pyttsx3.init()
a.setProperty('rate', 178)
a.say("Welcome to GLWEC virtual prospectus")
a.runAndWait()

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="user_hostname",
    password="user_password",
    database="college_responses"
)
cursor = conn.cursor()

def get_answer_from_db(question_text):
    """Retrieve answer from database based on keywords in question."""
    words = question_text.lower().split()
    query = "SELECT answer FROM faq WHERE "
    
    # Construct the query by including each word with the LIKE operator
    query += " OR ".join(f"keywords LIKE '%{word}%'" for word in words)
    query += " LIMIT 1"  # We only need one matching result

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else "Sorry, I couldn't find an answer to that question."
    except mysql.connector.Error as err:
        return f"Error: {err}"

def voice_assistant():
    """Listen for a question and provide an answer using speech synthesis."""
    with sr.Microphone() as source:
        a.say("Please ask your question")
        a.runAndWait()
        print("Listening for your question...")
        try:
            audio_text = r.listen(source, phrase_time_limit=7)
            question_text = r.recognize_google(audio_text)
            print("You asked:", question_text)
            answer = get_answer_from_db(question_text)
            a.say(answer)
            print("Answer:", answer)
            a.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            a.say("Sorry, I couldn't understand that.")
            a.runAndWait()
        except sr.RequestError:
            print("Sorry, there was an issue with the speech service.")
            a.say("Sorry, there was an issue with the speech service.")
            a.runAndWait()

# GUI Code (Retained as in original)
def clg():
    # Functionality to read PDF about college info
    pass

def adm():
    # Functionality to read PDF about administration
    pass

def s():
    exit()

# GUI Window
wn = tkinter.Tk()
wn.title("GLWEC Prospectus")
wn.geometry('800x520')
wn.config(bg='lavender')

# Labels and buttons for the GUI
tkinter.Label(wn, text='Welcome to meet the GLWEC Virtual Prospectus', bg='lavender',
              fg='black', font=('Helvetica', 18, "bold")).place(x=103, y=20)
tkinter.Label(wn, text="You can ask questions like:", bg="lavender", fg='black', font=('Helvetica', 18)).place(x=103, y=50)
tkinter.Label(wn, text="Who is the principal", bg="lavender", fg='black', font=('Helvetica', 18)).place(x=103, y=80)
tkinter.Label(wn, text="Mission of the college", bg="lavender", fg='black', font=('Helvetica', 18)).place(x=103, y=110)
tkinter.Label(wn, text="What is the vision of the college", bg="lavender", fg='black', font=('Helvetica', 18)).place(x=103, y=140)
tkinter.Label(wn, text="What courses are offered?", bg="lavender", fg='black', font=('Helvetica', 18)).place(x=103, y=170)

tkinter.Button(wn, text="Start", bg='grey', font=('Comic Sans MS', 15), command=voice_assistant).place(x=112, y=200)
tkinter.Button(wn, text="Stop", bg='grey', font=('Comic Sans MS', 15), command=s).place(x=192, y=200)
tkinter.Button(wn, text="About College", bg='grey', font=('Comic Sans MS', 15), command=clg).place(x=267, y=200)
tkinter.Button(wn, text="About Administration", bg='grey', font=('Comic Sans MS', 15), command=adm).place(x=427, y=200)
tkinter.Label(wn, text="To ask a question press start", bg="lavender", fg='black', font=('Helvetica', 18)).place(x=103, y=250)
tkinter.Label(wn, text="To quit press stop", bg="lavender", fg='black', font=('Helvetica', 18)).place(x=103, y=280)

wn.mainloop()

# Close the database connection when finished
cursor.close()
conn.close()
