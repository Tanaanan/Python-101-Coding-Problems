word_eng = ["いち","に","さん","よん", "ご", "ろく", "なな", "はち", "く", "じゅう"]
word_thai = ["หนึ่ง", "สอง", "สาม", "สี่", "ห้า","หก", "เจ็ด", "แปด", "เก้า", "สิบ"]
len_word = len(word_eng)

def TypingWord_Learn():
    i = 0
    score = 0
    mode = 0

    while True:
        print("Select mode Thai-Eng(1) or Eng-Thai (2)")
        mode = int(input("Mode Select : "))
        if mode == 1:
            print("Thai-Eng Selected")
            break
        elif mode == 2:
            print("Eng-Thai Selected")
            break
        else:
            print("Please try again")
    
    while i < len_word:
        if mode == 2:
            print(f'{word_eng[i]} == ?')
            answer = str(input("Answer : "))
            answer = answer.lower().strip()
            if answer == word_thai[i]:
                print("Correct! (score +1)")
                score = score + 1
                i = i + 1
            else:
                print("Wrong, Try again!")
        elif mode == 1:
            print(f'{word_thai[i]} == ?')
            answer = str(input("Answer : "))
            answer = answer.lower().strip()
            if answer == word_eng[i]:
                print("Correct! (score +1)")
                score = score + 1
                i = i + 1
            else:
                print("Wrong, Try again!")
    print(f'Total score = {score} / {len_word}')

def TypingWord_Test():
    score = 0
    mode = 0
    Error = []
    player_ans = []

    while True:
        print("Select mode Thai-Eng(1) or Eng-Thai (2)")
        mode = int(input("Mode Select : "))
        if mode == 1:
            print("Thai-Eng Selected")
            break
        elif mode == 2:
            print("Eng-Thai Selected")
            break
        else:
            print("Please try again")
    
    for m in range(len_word):
        if mode == 2: #Eng Thai
            print(f'{word_eng[m]} == ?')
            answer = str(input("Answer : "))
            answer = answer.lower().strip()
            if answer == word_thai[m]:
                print("Correct! (score +1)")
                score = score + 1
                Error.append(0)
                player_ans.append(answer)
            else:
                print("Wrong!")
                Error.append(1)
                player_ans.append(answer)
        elif mode == 1: #Thai Eng
            print(f'{word_thai[m]} == ?')
            answer = str(input("Answer : "))
            answer = answer.lower().strip()
            if answer == word_eng[m]:
                print("Correct! (score +1)")
                score = score + 1
                Error.append(0)
                player_ans.append(answer)
            else:
                print("Wrong!")
                Error.append(1)
                player_ans.append(answer)

    print("---------------------------------------------------------")
    CorrectRate = (100*score) / len_word
    print(f"Solution | CorrectRate = {int(CorrectRate)} %")
    print(f'Total score = {score} / {len_word}')
    print("---------------------------------------------------------")

    
    for k in range(len(Error)): #Correct
        if Error[k] == 1:
            print(f"Wrong! : {word_eng[k]} = {word_thai[k]} ({player_ans[k]})")

    print("---------------------------------------------------------")

    for j in range(len(Error)): #Correct
        if Error[j] == 0:
            print(f"Correct : {word_eng[j]} = {word_thai[j]}")

print("""Enter Mode 
1. Practice Mode
2. Test Mode""")
ModeSelect = (int(input(":")))

if ModeSelect == 1:
    TypingWord_Learn()
elif ModeSelect == 2:
    TypingWord_Test()
else:
    print("Error, try again")


        






                
                    

        
        
    
    



    




        
