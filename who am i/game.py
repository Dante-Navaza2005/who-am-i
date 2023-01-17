play_again = "play again"

while play_again == "play again" and play_again != "exit" :
    name = input("What is your name? ")
    introduction = input("Welcome to the 5 question who am I game! Type skip to skip a question (you wont recieve points) and  type tip to see tips. Type okay to begin! ")

    score = 0

    if introduction == "okay":
        question1 = input("1) I can fly but have no wings. I can cry but have no eyes. What am I? ")
        while question1 != "cloud" and question1 != "skip" :    
                if question1 == "tip" :
                    question1 = input("Tip 1: When I cry I change colors and become darker. ")
                    if question1 == "tip" : 
                        question1 = input("Last tip: I can be seen from outer space. ")
                else :
                    question1 = input("1) I can fly but have no wings. I can cry but have no eyes. What am I? ")

        if question1 == "skip" : 
            question_right = input("You skipped this question. Do you want to see your score or start the next question (type next)? ")
        
        if question1 == "cloud" :
            score = score + 10
            question_right = input("Congratulations! you got the first question right! Do you want to see your score or start the next question (type next)? ")
        

        if question_right == "score" :
            print("Your score is ", score)
            question_right = "next"


                                                    #QUESTION 2
        
        if question_right == "next" : 
            question2 = input("2) I speak but have no mouth. I hear but have no ears. I have no body but I live in the wind. Who am I? ")
            while question2 != "echo" and question2 != "skip" : 
                if question2 == "tip" :
                    question2 = input("Tip 1: I live in certain places. ")
                    if question2 == "tip" :
                        question2 = input("I am loud. ")
                else : 
                    question2 = input("2) I speak but have no mouth. I hear but have no ears. I have no body but I live in the wind. Who am I? ")
        
            if question2 == "skip" : 
                question_right = input("You skipped this question. Do you want to see your score or start the next question (type next)? ")
        
            if question2 == "echo" :
                score = score + 10
                question_right = input("Congratulations! you got the second question right! Do you want to see your score or start the next question (type next)? ")
        

            if question_right == "score" :
                print("Your score is ", score)
                question_right = "next"



                                                            #QUESTION 3

        if question_right == "next" :
            question3 = input("3) If 11 + 2 is equal to 1, how much is 9 + 5? ")
            while question3 != "2" and question3 != "skip" :
                if question3 == "tip" :
                    question3 = input("Tip 1: Its all about time. ")
                    if question3 == "tip" :
                        question3 = input("Last tip: Evening is aproaching. ")
                else :
                    question3 = input("3) If 11 + 2 is equal to 1, how much is 9 + 5? ")
        
        if question3 == "skip" : 
            question_right = input("You skipped this question. Do you want to see your score or start the next question (type next)? ")
        
        if question3 == "2" :
            score = score + 10
            question_right = input("Congratulations! you got the third question right! Do you want to see your score or start the next question (type next)? ")
        
            
        if question_right == "score" :
            print("Your score is ", score)
            question_right = "next"


                                                                    #QUESTION 4

        if question_right == "next" :
            question4 = input("4) The more there is of me, the less you will see me. Who am I? ")
            while question4 != "darkness" and question4 != "skip":
                if question4 == "tip" :
                    question4 = input("Tip 1: Occurs in the opposite of day. ")
                    if question4 == "tip" :
                        question4 = input("Last tip: A blind man's vision. (literally) ")
                else :
                    question4 = input("4) The more there is of me, the less you will see me. Who am I? ")

        if question4 == "skip" : 
            question_right = input("You skipped this question. Do you want to see your score or start the next question (type next)? ")
        
        if question4 == "darkness" :
            score = score + 10
            question_right = input("Congratulations! you got the fourth question right! Do you want to see your score or start the next question (type next)? ")
        
            
        if question_right == "score" :
            print("Your score is ", score)
            question_right = "next"

                                                                    #QUESTION 5
        
        if question_right == "next" :
            question5 = input("5) Who makes me wont admit. Who has me doesn't know they do. And who knows doesnt want to have me at all. Who am I? ")
            while question5 != "fake money" and question5 != "skip":
                if question5 == "tip" :
                    question5 = input("Tip 1: I usally come in large amounts. ")
                    if question5 == "tip" :
                        question5 = input("Last tip: I am easily confused by something everyone desires. ")
                else :
                    question5 = input("5) Who makes me wont admit. Who has me doesn't know they do. And who knows doesnt want to have me at all. Who am I? ")

        if question5 == "skip" : 
            question_right = input("You finished the game! Type highschore to see your highscore ")
        
        if question5 == "fake money" :
            score = score + 10
            question_right = input("You finished the game! Type highscore to see your highscore ")
        
        highscore_file = open("scoreboard.txt", "w")
        highscore_file.write(name + ": " + str(score))
        
        if question_right == "highscore" :
            highscore_file = open("scoreboard.txt", "r")
            highscore = highscore_file.readline()
            highscore_number = highscore.split(" ")
            print("The highscore was " + highscore_number[1])

    play_again = input("Do you want to play again or exit? ")
exit()
    

