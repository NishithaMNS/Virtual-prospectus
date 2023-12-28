import tkinter
import PyPDF2
import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
a = pyttsx3.init()
voices = a.getProperty('voices')
a.setProperty('voice', voices[1].id)
a.setProperty("rate", 178)
a.say("welcome to g l w e c virtual prospectus ")
a.say("you can ask any questions about G L W E C ")
a.runAndWait()
def voice_assistant():
    with sr.Microphone() as source:

        a.say("talk")
        a.runAndWait()
        print("Talk")
        audio_text = r.listen(source, phrase_time_limit=7)
        print("Time over, thanks")
        try:
            print("Text: " + r.recognize_google(audio_text))
            b = r.recognize_google(audio_text)
            b = b.lower()
            l = b.split(" ")
            if("what" and ("courses" or "departments") in l or "which" and ("courses" or "departments") in l):
                ab = "CSE and IT"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif (("name" and "academic director") in l or ("name" and "ad") in l or ("who" and "ad") in l or (
                    "who" and ("director" or "Director")) in l):
                ab = "Deepa Gaanu"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif("name" and "principal" in l):
                ab = "Dr A. Sai Hanuman"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif (("who" and "principal") in l):
                ab = "Dr A. Sai Hanuman"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif ("about" and "management" in l):
                ab = "Dr. Gokaraaju Ganga Raaju, Chairman. Dr G Ganga Raaju is renowned for his dynamic, optimistic, and compassionate nature. As an outstanding team leader, he takes ownership of issues around him, takes control of situations, and promotes universal good. Notably, leading by example he drives people to change. Dr.Ganga Raaju initiated the promotion of Engineering and Pharmacy education under the Gokaraaju Rangaraaju Educational Society. In 1997, he established the Gokaraaju Rangaraaju Institute of Engineering and Technology, and in 2003, the Gokaraaju Rangaraaju College of Pharmacy. GRES is promoted by Dr Gokaraaju Ganga Raaju, Chairman of Laila Group of Industries having varied interests in Pharmaceuticals, Paper, Sugar, Agro-Products etc. Dr Gokaraaju Ganga Raaju, an educationalist and philanthropist, established GRIET as a fitting tribute to his dynamic and visionary father Late Sri Gokaraaju Ranga Raaju. Sri G V K Ranga Raaju, Vice President. Don’t sit back and take what comes…go after what you want. Sri G V K Ranga Raaju is the eldest son of Dr G Ganga Raaju. He brings to Gokaraaju Rangaraaju Educational Society his business acumen, knowledge and wide reading. His exceptional people skills have enabled him to create resounding goodwill and respect for himself and GRES. G V K Ranga Raaju takes care of all the day-to-day matters concerning GRIET, and promptly addresses the concerns of the parents and students. He believes in a no-compromise policy, when it comes to personal supervision of educational institutions and in maintaining academic schedule & discipline. Extraordinarily gifted and tech savvy, he understands the importance of technology in today’s fast paced world. He believes in exposing students on cutting edge technology so that they are equipped to not just face the challenges of the modern day living, but become leaders in their own right. For him education is a journey of discovery."
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif (("name" and "hod") in l):
                ab = "Dr Padmalaya Nayak"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif (("name" and "h o d") in l or ("who" and "hod") in l):
                ab = "Dr Padmalaya Nayak"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif (("name" and "HRD") in l or ("who" and "hrd") in l):
                ab = "Dr Padmalaya Nayak"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif ("vision" in l):
                ab = "To be world class engineering college for imparting experiential, innovative and critical skills addressing societal problems. Inspiring young women to become globally competent in technical education and research to emerge as world class leaders."
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif ("mission" in l):
                ab = "To promote experiential learning in students by engaging them in hands on experience and reflection, so that, they are able to connect theories and knowledge learned in the classroom to real-world situations.To create an ambience in which novel ideas, research and development flourish in order to shape the emerging innovators.To provide infrastructure and facilities to meet the latest technology trends.To avail necessary support for skill enhancement to reduce the industry-academia gap."
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif(("why" and "Gokaraju Leelavathi")in l or ("why" and "Gokaraju Lilavati") in l):
                ab = "Gokaraaju Lailavathi Womens Enginnering College is established in 2021 by Dr G Gangaraaju as a self-financed institute under the aegis of Gokaraaju Rangaraaju Educational Society. According to the latest study about 29% of global tech workforce are women and they predict a huge surge in it, in the coming years. Though there is a change in the workforce dynamics there are very few females who made it to the top. A majority of the boardrooms today are still a boys’ club. In a recent survey, some top notch women in Tech jobs listed some of the myths about women:They are not good at stem jobs,They cannot be entrepreneurs, barrier breakers, innovative thinkers. They are not made for hard core jobs, critical thinking, problem solving, working with equipment, etc. Here at G L W E C, we address all these problems one by one and try to create a place for our girls amidst of these challenges. We have designed various programs apart from the University Curriculum which would help our girls become globally competent and world class leaders."
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif(("about" and "ragging") in l):
                ab= "Establishment of Anti Ragging Committee Gokaraju Lailavathi Womens Engineering College, Hyderabad has formulated the Anti-Ragging policy and taken the following measures in order to constitute an effective Anti-Ragging System in line with the directives of the Honorable Supreme Court, AICTE, UGC, Telangana State Council for Higher Education and OU. The Discipline Committee, constituted having reviewed the Anti-Ragging policies of the Institution has resolved that the same requires to be implemented based upon the instructions issued by the AICTE, UGC, and the University and TSCHE. An anti-ragging committee comprising the Principal, Registrar, Coordinator of Discipline, Inspector of Police Bachupally Circle, Coordinator of Student Affairs, , the Physical Director, and Senior student representatives from all programmes met before the I st year B.E. students arrive each year, explaining to them the menace of ragging and the severity of the situation, consequences, the"
                a.say(ab)
                print(ab)
                a.runAndWait()
            elif ("exit" in l):
                ab="Thanks for giving me your time,press stop"
                a.say(ab)
                print(ab)
                a.runAndWait()

            else:
                a.say("invalid question,try again")
                print("invalid question,try again")
                a.runAndWait()
        except:
            pass

def clg():
    pdf_book = open(r"C:\Users\Nishitha\Downloads\Dr.pdf", 'rb')
    reading_pdf = PyPDF2.PdfFileReader(pdf_book)
    pdf_pages = reading_pdf.numPages

    pdf_speaker = pyttsx3.init()
    choose_page = reading_pdf.getPage(0)
    pdf_text = choose_page.extractText()
    pdf_speaker.say(pdf_text)
    pdf_speaker.runAndWait()
def adm():
    pdf_book = open(r"C:\Users\Nishitha\Downloads\sodapdf-converted.pdf", 'rb')
    reading_pdf = PyPDF2.PdfFileReader(pdf_book)
    pdf_pages = reading_pdf.numPages

    pdf_speaker = pyttsx3.init()
    choose_page = reading_pdf.getPage(0)
    pdf_text = choose_page.extractText()
    pdf_speaker.say(pdf_text)
    pdf_speaker.runAndWait()


def s():
    exit()
wn = tkinter.Tk()
wn.title("GLWEC Prospectus")
wn.geometry('800x520')
wn.config(bg='lavender')

tkinter.Label(wn, text='Welcome to meet the GLWEC Virtual Prospectus', bg='lavender',
              fg='black', font=('Helvetica', 18,"bold")).place(x=103, y=20)
tkinter.Label(wn, text="You can ask questions like:",bg="lavender",fg='black',font=('Helvetica',18)).place(x=103, y=50)
tkinter.Label(wn, text="who is the principal",bg="lavender",fg='black',font=('Helvetica',18)).place(x=103, y=80)
tkinter.Label(wn, text="Mission of the college",bg="lavender",fg='black',font=('Helvetica',18)).place(x=103, y=110)
tkinter.Label(wn, text="What is the vision of the college",bg="lavender",fg='black',font=('Helvetica',18)).place(x=103, y=140)
tkinter.Label(wn, text="What are the courses offered?",bg="lavender",fg='black',font=('Helvetica',18)).place(x=103, y=170)

tkinter.Button(wn, text="Start", bg='grey', font=('Comic Sans MS', 15), command=voice_assistant).place(x=112, y=200)
tkinter.Button(wn, text="Stop",bg='grey', font=('Comic Sans MS', 15), command=s).place(x=192, y=200)
tkinter.Button(wn, text="About College",bg='grey',font=('Comic Sans MS',15), command=clg).place(x=267,y=200)
tkinter.Button(wn, text="About Adminstration",bg='grey',font=('Comic Sans MS',15), command=adm).place(x=427,y=200)
tkinter.Label(wn, text="To ask a question press start",bg="lavender",fg='black',font=('Helvetica',18)).place(x=103, y=250)
tkinter.Label(wn, text="To quit press stop",bg="lavender",fg='black',font=('Helvetica',18)).place(x=103, y=280)

showCommand = tkinter.StringVar()
cmdLabel = tkinter.Label(wn, textvariable=showCommand, bg='LightBlue1',
                         fg='black', font=('Courier', 15))
cmdLabel.place(x=250, y=150)

wn.mainloop()