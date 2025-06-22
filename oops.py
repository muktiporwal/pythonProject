import random
class Question:
    def __init__(self,text,options,answer):
        self.text=text
        self.options=options
        self.answer=answer

    def check_answer(self,user_input):
        return self.options[user_input-1]==self.answer
    
class User:
    def __init__(self,username):
        self.username=username
        self.score=0

    def update_score(self):
        self.score+=1

    def show_result(self,total):
        print(f"\n{self.username},your final score is: {self.score}/{total}")

class Quiz:
    def __init__(self,user,questions):
        self.user=user
        self.questions=questions
        
    def start(self):
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions,1):
            print(f"Q{i}: {question.text}")
            for idx, option in enumerate(question.options,1):
                print(f" {idx}.{option}")
            try:
                user_input=int(input("your answer(1-4)"))

                if question.check_answer(user_input):
                    print("correct\n")
                    self.user.update_score()
                else:
                    print(f"Wrong. correct answer was: {question.answer}\n")
            except (ValueError, IndexError):
                print("Invalid Input")

        self.user.show_result(len(self.questions))

q1=Question("What is the capital of France?",["Paris","Rome","Berlin","Madrid"],"Paris")
q2=Question("What is 2+2?",["2","8","4","22"],"4")
q3=Question("What is the color of sky?",["Blue","Pink","Red","Orange"],"Blue")
q4=Question("What is the largest continent?",["Africa","America","Asia","Australia"],"Asia")
q5=Question("Which planed is called red planet?",["Earth","Venus","Jupiter","Mars"],"Mars")

name=input("Enter your name: ")
user=User(name)
quiz=Quiz(user,[q1,q2,q3,q4,q5])
quiz.start()