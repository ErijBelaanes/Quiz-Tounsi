####Phase1####
#1rst step
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import json
import pygame
#2nd step
#Creation of quiz's data
quiz_data = {
    "Food":[
     {
        "question": "What Tunisian food will a 40-year-old mother cook on a rainy day?⛈️",
        "options": ["Fish & chips 🐟🍟", "Vegetables noodles 🍜", "Mhamesa 🍲"],
        "answer": "Mhamesa 🍲"
     },
     {
        "question": "You’re fasting in Ramadan and can’t wait for Ftour. What’s the first thing most Tunisian families eat?👨🏼‍👩🏼‍👧🏼‍👦🏼",
        "options": ["Brik 🥟", "Sushi 🍣", "Samsa 🥠"],
        "answer": "Brik 🥟"
     },
     {
        "question": "In a 🎉Tunisian wedding🎉, what dish is the star of the night?",
        "options": ["Lablabi 🥣", "Pizza Tunisienne 🍕","Couscous with meat 🍲"],
        "answer": "Couscous with meat 🍲"
     },
     {
        "question": "On a rainy morning, what food would a construction worker eat before going to work? ⛈️",
        "options": ["Croissant 🥐", "Bssisa🍲", "Dro3 🥣"],
        "answer": "Dro3 🥣"
     },
     {
        "question": "Which spicy condiment🥵 is in almost every Tunisian dish?",
        "options": ["Ketchup 🥫","Harissa 🌶", "Mayonnaise 🥚"],
        "answer": "Harissa 🌶"
     },
     {
        "question": "Which Tunisian sweet is also a symbol of hospitality and is offered to guests?🍬😋",
        "options": ["Chocolate mousse 🍫", "Tiramisu 🍰","Baklawa 🥮"],
        "answer": "Baklawa 🥮"
     },
     {
        "question": "Which sweet is made with dates, almonds, and often served during Ramadan?",
        "options": ["Brioche 🥐", "Samsa","Makroud 🥮"],
        "answer": "Makroud 🥮"
     },
     {
        "question": "Which Tunisian bread is traditionally baked in a clay oven?",
        "options": ["Tabouna 🫓", "Pita bread 🫓", "French baguette 🥖"],
        "answer": "Tabouna 🫓"
     }],
    "Geography":[
     {
        "question": "Which Tunisian city is famous for Harissa🌶?",
        "options": ["Nabeul","Tozeur", "Kairouan"],
        "answer": "Nabeul"
     },
     {
        "question": "Which Tunisian region is famous for its vast Sahara desert landscapes and oasis? 🏜️",
        "options": ["Tozeur", "Bizerte", "Sfax"],
        "answer": "Tozeur"
     },
     {
        "question": "If you want to see houses🏠 built inside caves⛰️, where should you go?",
        "options": ["Carthage", "Sidi Bou Saïd","Matmata"],
        "answer": "Matmata"
     },
     {
        "question": "Which Tunisian island is famous for its sandy beaches and luxurious resorts🏝️?",
        "options": ["Djerba", "Kerkennah", "Galite Islands"],
        "answer": "Djerba"
     },
     {
        "question": "You want the best dates in Tunisia. Which region are you heading to?🤔",
        "options": ["Gabes", "Touzeur", "Bizerte"],
        "answer": "Touzeur"
     },
     {
        "question": "Which Tunisian city is famous for its blue-painted doors and white streets🏠🔵🌊?",
        "options": ["Sidi Bou Said", "La Marsa", "Mahdia"],
        "answer": "Sidi Bou Said"
     },
     {
        "question": "The ancient ruins of Carthage are located near which modern city?🏛️",
        "options": ["Tunis", "Sfax", "Bizerte"],
        "answer": "Tunis"
     },
     {
        "question": "Which Tunisian city is known for its ancient amphitheater, one of the best preserved in the world?🏛️",
        "options": ["El Djem", "Kairouan", "Carthage"],
        "answer": "El Djem"
     }],
    "Known_Celebrities":[
     {
        "question": "Who is the famous Tunisian tennis player🎾 known worldwide and nicknamed “Minister of Happiness”?",
        "options": ["Selima Sfar","Ons Jabeur", "Nada Mezni Hafaiedh"],
        "answer": "Ons Jabeur"
     },
     {
        "question": "Which sport brought Ahmed Jaouadi fame in Tunisia and earned him a spot representing his country at the Olympics🥇?",
        "options": ["Football ⚽🇹🇳","Swimming 🏊", "Basketball 🏀"],
        "answer": "Swimming 🏊"
     },
     {
        "question": "Which Tunisian comedian is famous for his humorous sketches and social satire? 😂🎭",
        "options": ["Karim Gharbi", "Hichem Rostom", "Nidhal Saadi"],
        "answer": "Karim Gharbi"
     },
     {
        "question": "Which sport is most loved in Tunisia?",
        "options": ["Football ⚽🇹🇳", "Handball 🤾", "Basketball 🏀"],
        "answer": "Football ⚽🇹🇳"
     },
     {
        "question": "Which Tunisian actress played in 🎬Egyptian movies🎭 and became a star across the Arab world?",
        "options": ["Hend Sabri", "Rim Riahi", "Julia Roberts"],
        "answer": "Hend Sabri"
     },
     {
        "question": "Which Tunisian singer is known for patriotic songs and folk music?",
        "options": ["Balti 😎🎤🇹🇳", "Emel Mathlouthi 👩‍🎤🎤","Hedi Jouini 👴🎤🇹🇳"],
        "answer": "Hedi Jouini 👴🎤🇹🇳"
     },
     {
        "question": "What is Samy Chaffai, the famous Tunisian, known for?🎥🌍",
        "options": ["Singer 🎤", "Content creator and filmmaker 🎬", "Footballer ⚽"],
        "answer": "Content creator and filmmaker 🎬"
     },
     {
        "question": "Mouna Noureddine is best known for her work in which field?🎭",
        "options": ["Politics 🏛️", "Acting 🎬", "Singing 🎤"],
        "answer": "Acting 🎬"
     }],
    "TV_Series":[
     {
        "question": "Who is the main character of Choufli Hal🤭😉?",
        "options": ["Slimane", "Douja","Sbou3i"],
        "answer": "Sbou3i"
     },
     {
        "question": "If your mom says “Don’t change the channel, I’m watching Choufli Hal”, what do you do?",
        "options": ["Take the remote📺🎛 and run🏃","🩴Obey🩴", "Negotiate with chocolate🍫"],
        "answer": "🩴Obey🩴"
     },
     {
        "question": "Who plays the character of Douja in 'Choufli Hal'?👩",
        "options": ["Sonia Ben Cheikh", "Dorra Zarrouk", "Rim Riahi"],
        "answer": "Sonia Ben Cheikh"
     },
     {
        "question": "In 'Nsibti Laaziza', who drives Baboucha crazy?😂", 
        "options": ["Khmissa & El Fehim 👩‍🦰👨‍🦰", "His customers 🛍", "Bad news 🎙"], 
        "answer": "Khmissa & El Fehim 👩‍🦰👨‍🦰"
     },
     {
        "question": "Which TV series features the daily life of Tunisian families in humorous situations?🏠😂",
        "options": ["Choufli Hal 🤭", "El Khottab Al Bab 🏠", "Nsibti Laaziza 💍"],
        "answer": "Choufli Hal 🤭"
     },
     {
        "question": "Which Tunisian TV series is famous for its Ramadan special episodes and drama?🌙📺",
        "options": ["Maktoub 📜", "Choufli Hal 🤭", "El Khottab Al Bab 🏠"],
        "answer": "El Khottab Al Bab 🏠"
     },
     {
        "question": "What is Ammar known for in 'Bolice' besides solving crimes?😂",
        "options": ["Always eating while on duty 🍕", "Chicken wings 🍗", "Being strict 😎"], 
        "answer": "Chicken wings 🍗"
     },
     {
        "question": "In 'Jari Ya Hamoudi', what does Hamouda do in life?",
        "options": ["A lawyer ⚖️", "Unemployed 😅", "Fish seller 🐟"], 
        "answer": "Fish seller 🐟"
     }],
    "Clothing":[
     {
        "question": "What is the traditional Tunisian hat, usually red and worn proudly by men, called?",
        "options": ["Koufia","Sombrero","Chechia"],
        "answer": "Chechia"
     },
     {
        "question": "What is the traditional Tunisian Farmla? 👗✨",
        "options": ["A richly decorated vest worn by women","A type of traditional hat for men","A Tunisian sandal style"],
        "answer": "A richly decorated vest worn by women"
     },
     {
        "question": "On Eid morning🕌, what will your grandpa absolutely refuse to leave the house without?",
        "options": ["His jogging suit", "His jebba", "His football jersey"],
        "answer": "His jebba"
     },
     {
        "question": "What is the name of the veil that aunt Fadila (Choufli Hal) wears when she goes to the market?🧕", 
        "options": ["Sefsari", "Hijab", "Chechia"],
        "answer": "Sefsari"
     },
     {
        "question": "What type of footwear is traditionally worn with the jebba or Sefsari?👞",
        "options": ["Balgha", "Sneakers", "Flip-flops"],
        "answer": "Balgha"
     },
     {
        "question": "Which piece of clothing is guaranteed to make a Tunisian aunt comment, 'You can’t go out like that!'😂",
        "options": ["Ripped jeans 👖", "Fancy dress 👗", "Traditional karako 🟣"],
        "answer": "Ripped jeans 👖"
     },
     {
        "question": "What is a 'Barnous' in Tunisia?🧥",
        "options": ["A traditional hooded cloak worn by men", "A type of hat", "A sandal style"],
        "answer": "A traditional hooded cloak worn by men"
     },
     {
        "question": "It's your cousin's wedding—what's the first thing that comes to your mind to wear at her Henna party?💃",
        "options": ["Blouza and Fouta", "Green dress", "A pair of jeans"], 
        "answer": "Blouza and Fouta"
     }]
}
#Saving the in a JSON file
with open("quiz_data.json","w") as file:
    json.dump(quiz_data,file,ensure_ascii=True,indent=4)
#Loading the JSON file
with open("quiz_data.json","r") as file:
    loaded_quiz=json.load(file)
#3rd step
class Quiz:
    def __init__(self,loaded_quiz):
        self.questions=loaded_quiz
        self.user_score=0
        self.current_question=0
        self.total_questions=len(self.questions)
    def get_current_question(self):
        if self.current_question<self.total_questions:
            return self.questions[self.current_question]
        return None
    def get_user_score(self,user_answer):
        if user_answer==self.questions[self.current_question]["answer"]:
            self.user_score+=1
            return True
        else:
            return False
    def next_question(self):
        self.current_question+=1
        return self.get_current_question()
    def quiz_finished(self):
        return self.current_question==self.total_questions
#4th step
quiz=Quiz(loaded_quiz)

window=tk.Tk()
window.title("Quiz Tounsi ")
window.attributes("-fullscreen",True)
window.configure(bg="#f5f5f5")
label=tk.Label(window,text="Welcome to Quiz Tounsi 🇹🇳 !",font=("Times New Roman",40,"bold italic"),bg="#f5f5f5", fg="#005f99")
label.pack(pady=20)
label_question=tk.Label(window,text="",font=("Times New Roman",20,"bold"),bg="#f5f5f5", fg="#d62828")
selected_option=tk.StringVar(value="")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
intro_label = tk.Label(window, text="🎉 Ready to test your Tunisian knowledge?", font=("Times New Roman", 30),bg="#f5f5f5")
intro_label.pack(pady=20)
intro_msg=tk.Label(window,text="The steps are easy:\n1) Click Start to play the quiz.\n2) Choose the correct answers.\n3) See whether you have Tunisian blood in you or not!",font=("Times New Roman",30,"bold"),bg="#f5f5f5", fg="#d62828")
intro_msg.pack(pady=50)
from PIL import Image, ImageTk
pygame.mixer.init()
#Image of the Tunisian flag
flag_image = Image.open("assets\images\waving-flag-map-tunisia.png") 
flag_image = flag_image.resize((350, 220))  # Adjust the size
flag_photo = ImageTk.PhotoImage(flag_image)

flag_label = tk.Label(window, image=flag_photo, bg="#f5f5f5")
flag_label.image = flag_photo 
flag_label.pack(pady=2)
selected_theme = tk.StringVar()
selected_theme.set("Food")  # Default Value
def show_theme_selection():
    global theme_label,theme_menu,begin_button
    start_button.pack_forget()  #Hide the widget Start
    intro_label.pack_forget()   #Hide the label "🎉 Ready to test your Tunisian knowledge?"
    intro_msg.pack_forget()     #Hide the label "The steps are easy: ..."
    flag_label.pack_forget()    #Hide the flag
    theme_label=tk.Label(window, text="Choose your quiz theme:", font=("Times New Roman", 25, "bold"), bg="#f5f5f5")
    theme_label.pack(pady=(250,0))
    theme_menu=ttk.Combobox(window, textvariable=selected_theme, values=list(loaded_quiz.keys()), font=("Times New Roman", 20))
    theme_menu.pack(pady=(0,20))
    begin_button=tk.Button(window, text="Begin Quiz", font=("Times New Roman", 20, "bold"), bg="#27ae60", fg="white",
                           command=lambda: start_quiz(selected_theme.get()))
    begin_button.pack(side="bottom",pady=50)
def start_quiz(theme):
    global quiz
    theme_label.pack_forget()  
    theme_menu.pack_forget()
    start_button.pack_forget()
    begin_button.pack_forget()
    quiz = Quiz(loaded_quiz[theme])
    label.pack(pady=20)   
    label_question.pack(pady=20)
    label_result.pack(pady=10)
    display_current_question()
    quit_button.pack(side="bottom",pady=20)
    next_button.pack(side="bottom",pady=20)
#5th step
option_buttons=[]
def display_current_question():
    question=quiz.get_current_question()
    if question!=None:
        #Display the current question
        label_question.config(text=question["question"])
        #Clear the previous options
        for btn in option_buttons:  
            btn.destroy()
        option_buttons.clear()
        #Display the current options
        for i,op in enumerate(question["options"]):  #because op here is a tuple(index,option) so if we don't pout i the result of the answer will always be wrong
            option_button=tk.Radiobutton(window,text=op,variable=selected_option,value=op,font=("Times New Roman",20,"bold"),anchor="w")
            option_button.pack(fill="x", padx=50, pady=5)
            option_buttons.append(option_button)
        selected_option.set("")
####Phase2####
#1st and 2nd step
def next_question():
    answer=selected_option.get()
    if answer=="":
        label_result.config(text="Please select an option!",fg="red")
        return
    if quiz.get_user_score(answer):
        label_result.config(text=f"Correct ✅❤️  |  Score= {quiz.user_score}",fg="green")
    else:
        label_result.config(text=f"Wrong ❌😢️  |  Score= {quiz.user_score}",fg="red")
    #Disable all the buttons(Next to prevent double-click)
    next_button.config(state="disabled")
    #Wait 1 second, then go to next question
    window.after(1000, proceed_to_next_question)
def proceed_to_next_question():
    quiz.next_question()
    if not quiz.quiz_finished():
        display_current_question()
        label_result.config(text="")
        #Enable button again
        next_button.config(state="normal")
    else:
        label_result.config(text="Quiz finished!😍")
        next_button.config(state="disabled")
        show_results_window()
def show_results_window():
    global result_window, quit_clicked
    #Create a new window on top of your main window
    quit_clicked = True
    quit_button.config(text="Close App")
    result_window=tk.Toplevel(window)
    result_window.title("Quiz Results")
    result_window.attributes("-fullscreen",True)
    result_window.configure(bg="#f5f5f5")
    #Calculate results
    correct_answers=quiz.user_score
    wrong_answers=quiz.total_questions - quiz.user_score
    #Display results
    label_title=tk.Label(result_window, text="🎉 Quiz Finished!", font=("Times New Roman", 35, "bold"),fg="#005f99",bg="#f5f5f5")
    label_title.pack(pady=50)
    label_correct=tk.Label(result_window, text=f"✅ Correct Answers: {correct_answers}", font=("Times New Roman", 18),bg="#f5f5f5")
    label_correct.pack(pady=20)
    label_wrong=tk.Label(result_window, text=f"❌ Wrong Answers: {wrong_answers}", font=("Times New Roman", 18),bg="#f5f5f5")
    label_wrong.pack(pady=20)
    label_score=tk.Label(result_window, text=f"📊 Final Score: {quiz.user_score}/{quiz.total_questions}",
                        font=("Times New Roman", 25, "bold"),bg="#f5f5f5",fg="green" if quiz.user_score>wrong_answers
                        else "red" if quiz.user_score<wrong_answers
                        else "orange")
    label_score.pack(pady=30)
    if quiz.user_score>wrong_answers:
        conclusion_text="You are a really spicy Tunisian 🌶🥵"
        conclusion_image=Image.open("assets\images\zagrouta.png")
        pygame.mixer.Sound("assets\sounds\zaghrouta.mp3").play()
    elif quiz.user_score == wrong_answers:
        conclusion_text="Or maybe… a Tunisian? 🤨"
        conclusion_image=Image.open("assets\images\idk.png")
        pygame.mixer.Sound("assets\sounds\sus_sound.mp3").play()
    else:
        conclusion_text="Better check your roots 🙎‍"
        conclusion_image=Image.open("assets\images\suspicious.png")
        pygame.mixer.Sound("assets\sounds\sad_trombone.mp3").play()
    conclusion_label=tk.Label(result_window,text=conclusion_text, font=("Times New Roman", 30,"bold"),fg="#d62828",bg="#f5f5f5")
    conclusion_label.pack(pady=20) 
    conclusion_image=conclusion_image.resize((200, 200))
    conclusion_photo=ImageTk.PhotoImage(conclusion_image)  # Adjust the size
    conclusion_image_label=tk.Label(result_window, image=conclusion_photo, bg="#f5f5f5")
    conclusion_image_label.image = conclusion_photo  # Keep a reference to avoid garbage collection
    conclusion_image_label.pack(pady=2)
    #Close button
    close_btn = tk.Button(result_window, text="Close", font=("Times New Roman", 16), command=result_window.destroy)
    close_btn.pack(pady=20,padx=50)
    #Restart button
    def restart():
        global quit_clicked
        quiz.user_score=0
        quiz.current_question=0
        result_window.destroy()
        label_question.pack_forget()
        label_result.pack_forget()
        for btn in option_buttons:
            btn.destroy()
        option_buttons.clear()
        next_button.pack_forget()
        quit_button.pack_forget()
        show_theme_selection()
        next_button.config(state="normal")
        quit_button.config(text="Quit")
        quit_clicked=False
    restart_button=tk.Button(result_window,text="Restart",font=("Times New Roman", 16),command=restart)
    restart_button.pack(pady=20,padx=70)
# Update quit_quiz to use this function
quit_clicked=False
def quit_quiz():
    global quit_clicked
    if not quit_clicked :
        quit_clicked = True
        next_button.config(state="disabled")
        quit_button.config(state="disabled")
        show_results_window()
        quit_button.config(text="Close App")
        window.after(150, lambda: quit_button.config(state="normal"))
    else:
        clean_up()
start_button=tk.Button(window, text="Start", font=("Times New Roman",20,"bold"), bg="#2980B9", fg="white", command=show_theme_selection)
start_button.pack(side="bottom", pady=70)
quit_button=tk.Button(window,text="Quit",command=quit_quiz,font=("Times New Roman",20,"bold"),bg="#C0392B",fg="white")
next_button=tk.Button(window,text="Next",command=next_question,font=("Times New Roman",20,"bold"),bg="white")
label_result=tk.Label(window,text="",font=("Times New Roman",20,"bold"),bg="#f5f5f5")
#3rd step: I updated the function next_question to show the new score as well. The function keeping track of the user's score is in class Quiz in phase1
#4th step: Modification in the function quit_quiz
####Phase3####
#1st step
def clean_up():
    #Destroy all the wedgets but the title "Quiz Tounsi"
    for widget in window.winfo_children():
        if widget!=label:
            widget.destroy()
    cleanup_label=tk.Label(window,text="Performing cleanup tasks...",font=("Times New Roman", 24, "bold"), fg="orange",bg="#f5f5f5")
    cleanup_label.pack(pady=50)
    def show_done(): #Display cleanup done with a delay
      cleanup_label.config(text="Cleanup done✅\n\nSee you next time!",fg="green",bg="#f5f5f5")
      window.after(2000,window.destroy)
    window.after(2000,show_done)
#2nd step: Already done it in Phase1
window.mainloop()