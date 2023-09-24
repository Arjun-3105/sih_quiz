from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('quiztrophic')
root.config(bg = '#CBD18F')
root.geometry('1000x800')

label_question = Label(root, text = 'hello world',font = ("Arial", 15), fg = '#3A6B35', bg = '#CBD18F', wraplength=200, justify = 'left')
label_question.pack()

#defining a function that would take random options from list of questions
def shuffler():
    global questions

    ip_mcq_questions = [
        {
            "question": "Which type of IP protection is typically granted to literary and artistic works like books and music?",
            "options": ["Patent", "Trademark", "Copyright", "Trade Secret"],
            "correct_answer": "Copyright"
        },
        {
            "question": "What does the term 'WIPO' stand for in the context of IP?",
            "options": ["World Intellectual Property Organization", "Worldwide IP Oversight", "International Copyright Office", "Global Trademark Registry"],
            "correct_answer": "World Intellectual Property Organization"
        },
        {
            "question": "What is the primary purpose of a trademark?",
            "options": ["Protect inventions", "Protect trade secrets", "Identify the source of goods or services", "Protect artistic works"],
            "correct_answer": "Identify the source of goods or services"
        },
        {
            "question": "Which type of IP protection is granted to inventors for their inventions?",
            "options": ["Patent", "Copyright", "Trademark", "Trade Secret"],
            "correct_answer": "Patent"
        },
        {
            "question": "What legal doctrine allows limited use of copyrighted material without permission for purposes like education and criticism?",
            "options": ["Fair use", "Public domain", "Creative Commons", "Copyright exemption"],
            "correct_answer": "Fair use"
        },
        {
            "question": "What is the term for the exclusive rights granted to the creator of a work, allowing them to control its use and distribution?",
            "options": ["Monopoly", "Patent", "Copyright", "Trademark"],
            "correct_answer": "Copyright"
        },
        {
            "question": "What type of IP protection is typically associated with unique product names or logos?",
            "options": ["Patent", "Copyright", "Trade Secret", "Trademark"],
            "correct_answer": "Trademark"
        },
        {
            "question": "What international treaty sets standards for IP protection?",
            "options": ["WTO", "UNESCO", "TRIPS", "WIPO"],
            "correct_answer": "TRIPS"
        },
        {
            "question": "What is the term for the unauthorized use or reproduction of someone else's IP?",
            "options": ["Exemption", "Infringement", "Fair use", "Public domain"],
            "correct_answer": "Infringement"
        },
        {
            "question": "Which type of IP protection is associated with confidential business information?",
            "options": ["Copyright", "Trademark", "Trade Secret", "Patent"],
            "correct_answer": "Trade Secret"
        },
        {
            "question": "What is the purpose of a patent?",
            "options": ["Protect artistic works", "Identify the source of goods or services", "Protect inventions", "Protect trade secrets"],
            "correct_answer": "Protect inventions"
        },
        {
            "question": "What is the maximum duration of copyright protection in many countries?",
            "options": ["20 years", "50 years", "75 years", "Life of the author plus 70 years"],
            "correct_answer": "Life of the author plus 70 years"
        },
        {
            "question": "What is the term for a work that is no longer protected by copyright and can be freely used by the public?",
            "options": ["Fair use", "Infringement", "Public domain", "Creative Commons"],
            "correct_answer": "Public domain"
        },
        {
            "question": "What does the term 'Fair use' refer to in IP law?",
            "options": ["Permission to use copyrighted material", "Limitation on IP rights", "Legal exemption for certain uses", "Trademark protection"],
            "correct_answer": "Legal exemption for certain uses"
        },
        {
            "question": "What organization is responsible for registering trademarks in the United States?",
            "options": ["WIPO", "USPTO", "UNESCO", "WTO"],
            "correct_answer": "USPTO"
        },
        {
            "question": "What is the primary role of the Berne Convention in IP law?",
            "options": ["Establishing patent standards", "Harmonizing copyright laws", "Protecting trade secrets", "Defining fair use"],
            "correct_answer": "Harmonizing copyright laws"
        },
        {
            "question": "What type of IP protection is associated with undisclosed business information and practices?",
            "options": ["Patent", "Trademark", "Trade Secret", "Copyright"],
            "correct_answer": "Trade Secret"
        },
        {
            "question": "What is the purpose of the Madrid Protocol in IP law?",
            "options": ["Protecting copyrights", "Streamlining trademark registration", "Defining patent standards", "Enforcing trade secrets"],
            "correct_answer": "Streamlining trademark registration"
        },
        {
            "question": "What is the key difference between a copyright and a trademark?",
            "options": ["Duration of protection", "Applicability to inventions", "Protection of artistic works", "Identification of source"],
            "correct_answer": "Duration of protection"
        },
        {
            "question": "What is the term for a legally binding agreement allowing limited use of copyrighted material under certain conditions?",
            "options": ["Public domain", "Fair use", "Creative Commons", "Copyright exemption"],
            "correct_answer": "Creative Commons"
        },
        {
            "question": "What does the acronym 'DMCA' stand for in the context of IP law?",
            "options": ["Digital Media Copyright Act", "Digital Millennium Copyright Act", "Domain Management and Copyright Act", "Data Mining and Copyright Authorization"],
            "correct_answer": "Digital Millennium Copyright Act"
        },
        {
            "question": "What is the term for the process of disclosing an invention to the public before applying for a patent?",
            "options": ["Copyrighting", "Public domain release", "Prior art", "Trademarking"],
            "correct_answer": "Prior art"
        },
        {
            "question": "What type of IP protection is typically associated with confidential formulas or manufacturing processes?",
            "options": ["Trademark", "Copyright", "Patent", "Trade Secret"],
            "correct_answer": "Trade Secret"
        },
        {
            "question": "What is the role of the WIPO (World Intellectual Property Organization) in global IP governance?",
            "options": ["Enforcing IP laws", "Creating IP laws", "Administering IP registrations", "Promoting IP cooperation"],
            "correct_answer": "Promoting IP cooperation"
        },
        {
            "question": "What is the purpose of a cease and desist letter in IP law?",
            "options": ["Requesting compensation for IP infringement", "Informing the public of IP rights", "Demanding immediate legal action", "Demanding the cessation of IP infringement"],
            "correct_answer": "Demanding the cessation of IP infringement"
        },
        {
            "question": "What is the primary function of the USPTO (United States Patent and Trademark Office)?",
            "options": ["Enforcing IP rights", "Creating IP laws", "Administering IP registrations", "Promoting IP cooperation"],
        

    "correct_answer": "Administering IP registrations"
        },
        {
            "question": "What is the term for an invention or work that is intentionally placed in the public domain with no copyright or patent protection?",
            "options": ["Fair use", "Public domain", "Trademark", "Trade secret"],
            "correct_answer": "Public domain"
        }
    ]
    global ques
    global mcq
    mcq = []
    global answer
    temp = choice(ip_mcq_questions)
    ques = temp['question']
    mcq.extend(temp['options'])
    answer = temp['correct_answer']
    label_question.config(text = ques)

    # creating list of options
    
    button1.config(text=mcq[0])
    button2.config(text=mcq[1])
    button3.config(text=mcq[2])
    button4.config(text=mcq[3])
    

def answer():
    if answer.lower() == entry_answer.get().lower():
        answer_label.config(text="Correct answer!", bg='#CBD18F', fg='#3A6B35')
    else:
        answer_label.config(text="Wrong answer, please try again.", bg='#CBD18F', fg='#3A6B35')

global hint_count
hint_count = 0
def hint():
    global hint_count
    word_length = len(answer)
    if hint_count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {answer[hint_count]}', bg='#CBD18F')
        hint_count += 1


# generating a basic GUI
entry_answer = Entry(root, font=("Arial", 24))
entry_answer.pack(pady=20)
button_frame = Frame(root, bg='#CBD18F')
button_frame.pack(pady=20)

options_frame = Frame(root, bg = '#CBD18F')
options_frame.pack(pady = 20)

#creating options buttons
button1 = Button(options_frame, text ='', bg ='#E3B448', width = 15, font = 10,  justify = "left",wraplength=100)
button2 = Button(options_frame, text ='', bg ='#E3B448', width =15, font = 10, justify = "left",wraplength=100)
button3 = Button(options_frame, text ='', bg ='#E3B448', width = 15, font = 10, justify = "left",wraplength=100)
button4 = Button(options_frame, text ='', bg ='#E3B448', width = 15, font = 10, justify = "left",wraplength=100)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

answer_button = Button(button_frame, text="Answer", command=answer, bg='#E3B448', width=8, font=10)
answer_button.grid(row=0, column=0, padx=10)
change_button = Button(button_frame, text="Pick Another Question", command=shuffler, bg='#E3B448', width=15, font=10)
change_button.grid(row=0, column=1, padx=10)
hint_button = Button(button_frame, text="Hint", command=lambda: hint(), bg='#E3B448', width=5, font=10)
hint_button.grid(row=0, column=2, padx=10)

answer_label = Label(root, text='', font=("Arial", 22))
answer_label.pack(pady=20)
hint_label = Label(root, text='', font=("Arial", 22), bg='#CBD18F')
hint_label.pack(pady=10)






shuffler()
root.mainloop()