



play_again = "play again" #initially sets the play again variable to satisfy the loop condition for the game to start


leaderboard = {} #initially sets the leaderbord to a empty dictionary (it stores the names of the players and their scores after they play)


#! this procedure is called when the player wishes to see his score after each question (by typing "score")
def show_score(score) :
    print(f"\nYour score is {score}\n")
    question_right = "next" #automatically moves to the next question
    return question_right #returns the string "next" which will be used to move to the next question




while play_again == "play again" and play_again != "exit" : #Game will repeat while the player answers "play again" and not "exit" in the play again question that appears in the end of the game
   
    i = 0 #index variable that will be used to enumerate the players in the leaderboard (initally set to 0)


   #introduces the game asking for the players name and setting the score to 0
    name = input("\nWhat is your name? ")
    introduction = input("\nWelcome to the 5 question who am I game! Type skip to skip a question (you wont recieve points) and type tip to see tips (two per question). Type okay to begin! ")
    print("\nObs: All answers are in undercase (except numbers)!!\n")
    score = 0


#!------------------------------------------------------------------QUESTION 1 ----------------------------------------------------------------




    if introduction == "okay":
        print("\n--------------------------------QUESTION 1--------------------------------------------------------")
        question1 = input("\n1) I can fly but have no wings. I can cry but have no eyes. What am I? ")  #print the first question
        while question1 != "cloud" and question1 != "skip" :  #while the player doesnt answer with the correct answer (cloud) or wishes to skip the question it will repeat  
                if question1 == "tip" :
                    question1 = input("\nTip 1: When I cry I change colors and become darker. ") #print first tip if player types tip
                    if question1 == "tip" :
                        question1 = input("\nLast tip: I can be seen from outer space. ")  #prints second tip if player types tip again
                else :
                    question1 = input("\nTRY AGAIN! I can fly but have no wings. I can cry but have no eyes. What am I? ") #if player types anything else than cloud or tip the question loops


        if question1 == "skip" : #if input value of the first question equals "skip" then player will be asked if he wants to see the score or head straight to the next question
            question_right = input("\nYou skipped this question. Do you want to see your score or start the next question (type next)? ")
       
        if question1 == "cloud" : #if input value of the first question equals the answer "cloud" then 10 points will be added to the score.
            score = score + 10
            question_right = input("\nCongratulations! you got the first question right! Do you want to see your score or start the next question (type next)? ")
       


        if question_right == "score" : #if input value of the question asking if he wishes to see the score is "score" then the show_score procedure is called
            question_right = show_score(score) #sets the question_right variable to "next" which will move to the next question




#!------------------------------------------------------------------QUESTION 2 ----------------------------------------------------------------
       
        if question_right == "next" :
            print("\n--------------------------------QUESTION 2--------------------------------------------------------")
            question2 = input("\n2) I speak but have no mouth. I hear but have no ears. I have no body but I live in the wind. Who am I? ") #print the second question
            while question2 != "echo" and question2 != "skip" :  #while the player doesnt answer with the correct answer (echo) or wishes to skip the question it will repeat
                if question2 == "tip" :
                    question2 = input("\nTip 1: I live in certain, enclosed places. ") #print first tip if player types tip
                    if question2 == "tip" :
                        question2 = input("\nYell in a cave. ")  #prints second tip if player types tip again
                else :
                    question2 = input("\nTRY AGAIN! I speak but have no mouth. I hear but have no ears. I have no body but I live in the wind. Who am I? ")#if player types anything else than echo or tip the question loops
       
            if question2 == "skip" : #if input value of the second question equals "skip" then player will be asked if he wants to see the score or head straight to the next question
                question_right = input("\nYou skipped this question. Do you want to see your score or start the next question (type next)? ")
       
            if question2 == "echo" : #if input value of the second question equals the answer "echo" then 10 points will be added to the score.
                score = score + 10
                question_right = input("\nCongratulations! you got the second question right! Do you want to see your score or start the next question (type next)? ")
       


            if question_right == "score" : #if input value of the question asking if he wishes to see the score is "score" then the show_score procedure is called
               question_right = show_score(score) #sets the question_right variable to "next" which will move to the next question






#!------------------------------------------------------------------QUESTION 3 ----------------------------------------------------------------


        if question_right == "next" :
            print("\n--------------------------------QUESTION 3--------------------------------------------------------")
            question3 = input("\n3) If 11 + 2 is equal to 1, how much is 9 + 5? ") #print the third question
            while question3 != "2" and question3 != "skip" : #while the player doesnt answer with the correct answer (2) or wishes to skip the question it will repeat
                if question3 == "tip" :
                    question3 = input("\nTip 1: Its all about time. ") #print first tip if player types tip
                    if question3 == "tip" :
                        question3 = input("\nLast tip: Evening is comming. ") #prints second tip if player types tip again
                else :
                    question3 = input("\nTRY AGAIN! If 11 + 2 is equal to 1, how much is 9 + 5? ") #if player types anything else than 2 or tip the question loops
       
            if question3 == "skip" : #if input value of the third question equals "skip" then player will be asked if he wants to see the score or head straight to the next question
                question_right = input("\nYou skipped this question. Do you want to see your score or start the next question (type next)? ")
           
            if question3 == "2" : #if input value of the third question equals the answer 2 then 10 points will be added to the score.
                score = score + 10
                question_right = input("\nCongratulations! you got the third question right! Do you want to see your score or start the next question (type next)? ")
           
           
            if question_right == "score" : #if input value of the question asking if he wishes to see the score is "score" then the show_score procedure is called
               question_right = show_score(score) #sets the question_right variable to "next" which will move to the next question
 


#!------------------------------------------------------------------QUESTION 4 ----------------------------------------------------------------


        if question_right == "next" :
            print("\n--------------------------------QUESTION 4--------------------------------------------------------")
            question4 = input("\n4) The more there is of me, the less you will see me. Who am I? ") #print the fourth question
            while question4 != "darkness" and question4 != "skip": #while the player doesnt answer with the correct answer (darkness) or wishes to skip the question it will repeat
                if question4 == "tip" :
                    question4 = input("\nTip 1: Occurs in the opposite of day. ") #print first tip if player types tip
                    if question4 == "tip" :
                        question4 = input("\nLast tip: Close your eyes ") #print second tip if player types tip again
                else :
                    question4 = input("\nTRY AGAIN! The more there is of me, the less you will see me. Who am I? ") #if player types anything else than darkness or tip the question loops


            if question4 == "skip" : #if input value of the fourth question equals "skip" then player will be asked if he wants to see the score or head straight to the next question
                question_right = input("\nYou skipped this question. Do you want to see your score or start the next question (type next)? ")
           
            if question4 == "darkness" :#if input value of the fourth question equals the answer darkness then 10 points will be added to the score.
                score = score + 10
                question_right = input("\nCongratulations! you got the fourth question right! Do you want to see your score or start the next question (type next)? ")
           
               
            if question_right == "score" : #if input value of the question asking if he wishes to see the score is "score" then the show_score procedure is called
               question_right = show_score(score)


#!------------------------------------------------------------------QUESTION 5 ----------------------------------------------------------------
       
        if question_right == "next" :
            print("\n--------------------------------QUESTION 5--------------------------------------------------------")
            question5 = input("\n5) Who makes me wont admit. Who has me doesn't know they do. And who knows doesnt want to have me at all. Who am I? ")#print the fourth question
            while question5 != "fake money" and question5 != "skip":  #while the player doesnt answer with the correct answer (fake money) or wishes to skip the question it will repeat
                if question5 == "tip" :
                    question5 = input("\nTip 1: I am used for purchase. ") #print first tip if player types tip
                    if question5 == "tip" :
                        question5 = input("\nLast tip: I am easily confused by something everyone desires. ") #print second tip if player types tip again
                else :
                    question5 = input("\nTRY AGAIN! Who makes me wont admit. Who has me doesn't know they do. And who knows doesnt want to have me at all. Who am I? ") #if player types anything else than fake money or tip the question loops




            if question5 == "skip" :  #if input value of the fith question equals "skip" the leaderboard will be shown
                question_right = print("\nYou finished the game!")
           
            if question5 == "fake money" : #if input value of the fourth question equals the answer darkness then 10 points will be added to the score and the leaderboard will will be shown
                score = score + 10
                question_right = print("\nYou finished the game!")  
       
        leaderboard.update({name: score}) #updates the empty dictionary with the name of the player and the score. example: (PersonA: 30)
       
        leaderboard_ordered = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))
        #creates a copy of the leaderboard dictionary and orders it from the highest to lowest values
       
        #function recieves the leaderboard dictionary, a input of the player if he wants the leaderboard to be enumerated or not and a index (to enumerate the players)
        # as a parameter
        def display_leaderboard(leaderboard, is_enumerated, i) :
            question = input("\nDo you wish to see the leaderboard? Type yes or no. ") #asks if the player wishes to see the leaderboard
            if question == "yes":
               if is_enumerated != "no" : #if player wants to see leaderboard enumerated
                  for players, score in leaderboard.items() : #loops throught the dictionary and prints each players score ordered from highest to lowest score
                        i = i + 1 #index enumerates the position of each player
                        print(f"\n{i}) {players}: {score}") #formats the display of the leaderboard. example: 1) Student A: 40
               else :
                   for players, score in leaderboard.items() : #loops throught the dictionary and prints each players score ordered from highest to lowest score
                        i = i + 1 #index enumerates the position of each player
                        print(f"\n{players}: {score}") #formats the display of the leaderboard. example: Student A: 40
     
        is_enumerated = input("\nDo you wish to enumerate the leaderboard? Type yes or no. ") #asks wheter the user wishes to enumerate the leaderboard


        #calling the function with the ordered leaderboard, the index variables, and if the player wishes leaderboard to be enumerated or not the  as parameters
        display_leaderboard(leaderboard_ordered, is_enumerated, i)


    show_answers = input("\nDo you want to see the answers? Type yes or no. ") #asks if the player wants to see the answer key
   
    if show_answers == 'yes':
        print("\n--------------ANSWERS---------------\n1) cloud\n\n2) echo\n\n3) 2\n\n4) darkness\n\n5) fake money")
     
    play_again = input("\nDo you want to play again or exit? ")


exit()
   





