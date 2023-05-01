import time
import random
import sys

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = input ('너의 이름은? : ')
island = input ('섬 이름을 새로 지어달라구리 : ')

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = [["릴리안", 0], ["탁호", 0], ["미첼", 0], ["리처드", 0]]
my_bell = 3000
my_pocket = []
store = {'가습기' : 1400, '강아지 인형' : 2400, '강의실 책상' : 2500, '몬스테라' : 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    
    # 0. 게임 종료
    if answer_action == "0":
        sys.exit("\n게임을 종료합니다...\n다음에 또 오세요!")

    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        print("\n상점에 온걸 환영해구리! \n현재 상점에는 이런 물건들이 있어구리!\n")

        i = 1
        for key, value in store.items():
            print(str(i),  ". ", str(key), ": ", str(value), "벨")
            i += 1
        
        # 물건 구매
        get_stuff = int(input("\n어떤 물건을 구입하겠어구리 ? (숫자로 입력)"))
        time.sleep(1)   

        buy_stuff = store[list(store.keys())[get_stuff - 1]]

        if my_bell - buy_stuff > 0:
            my_bell = my_bell - buy_stuff

            print("\n", list(store.keys())[get_stuff - 1], "를(을) 구입하셨습니다!")
            time.sleep(0.6)
            print("남은 벨: ", str(my_bell))
            
            my_pocket.append(list(store.keys())[get_stuff - 1])
            del store[list(store.keys())[get_stuff - 1]]
        
        else:
            print("잔액이 부족하다구리!")
            time.sleep(1)
            print("남은 벨: " + str(my_bell))


        


    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":

        print("\n우리 마을에 있는 주민이야")
        for i in range(4):
            print(i+1,". ", animal[i][0])
        choose_animal = int(input("어떤 주민을 찾아갈까?"))
        print("\n", animal[choose_animal-1][0], "에게 무엇을 할까?")
        answer_animal_action = int(input("1. 말걸기 2. 선물하기 3. 때리기"))
       

        # 2-1. 말걸기를 선택한경우
        if answer_animal_action == 1:
            if choose_animal == 1:
                print("\n릴리안: 어머 ", name,"왔구나~ 반가워!\n어제는 어찌나 벚꽃이 이쁘던지 기분이 참 좋더라니까\n", name,"도 놀러다녀오는건 어때? 그렇지 뭐")
                print(animal[choose_animal-1][0], "친밀도 +1")
                animal[choose_animal-1][1] += 1
            elif choose_animal == 2:
                print("\n탁호: 안녀엉~ ", name, "아~ 반가워어~\n오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")
                print(animal[choose_animal-1][0], "친밀도 +1")
                animal[choose_animal-1][1] += 1
            elif choose_animal == 3:
                print("\n미첼: ", name, "아~! 반가워! 오늘 날씨 되게 좋지 않아?\n마구마구 산책을 하고 싶어져 동글")
                print(animal[choose_animal-1][0], "친밀도 +1")
                animal[choose_animal-1][1] += 1
            elif choose_animal == 4:
                print("\n리처드: ", name,"야아~\n나무를 흔들었더니 100벨이 나왔어어~\n",name,"도 한 번 흔들어봐아~ 그래유")
                print(animal[choose_animal-1][0], "친밀도 +1")
                animal[choose_animal-1][1] += 1

          
        # 2-2. 선물하기를 선택한 경우
        elif answer_animal_action == 2:

            if len(my_pocket) == 0:
                print("어라? 주머니에 아무것도 없어!")

            else: 
                print("내 주머니엔 이렇게 있어 \n")

                j = 1
                for i in my_pocket:
                    print (j, ". ", i, "\n")
                    j += 1
                
                animal_gift = int (input ("어떤 것을 선물할까? (숫자로 입력) "))
                print(animal[choose_animal-1][0], "에게", my_pocket[animal_gift-1], "을(를) 선물했다!")                
                print(animal[choose_animal-1][0], "친밀도 +5")
                animal[choose_animal-1][1] += 5
                my_pocket.remove(my_pocket[animal_gift-1])


        # 2-3. 때리기를 선택한 경우
        elif answer_animal_action == 3:
            print(animal[choose_animal-1][0],": ", "응..? 아야! 왜 그러는거야!\n",animal[choose_animal-1][0],"을(를) 때렸다!")

            animal[choose_animal-1][1] -= 1
            print(animal[choose_animal-1][0], "친밀도 -1")
            time.sleep(1)


        else:
             print("섬을 키워서 다른 주민들도 데려와보자구리!")




    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        print("나무를 흔듭니다.")
        time.sleep(1)
        result = random.choice(["100벨", "사과", "벌"])

        # 100벨이 떨어질경우
        if result == "100벨":
            print("앗, ", result, "이(가) 떨어졌다!")
            my_bell += 100
            time.sleep(0.5)
            print("+ 100벨")
            print("남은 벨: ",  str(my_bell))

        # 사과가 떨어질경우
        elif result == "사과":
            print("앗, ", result, "이(가) 떨어졌다!")
            time.sleep(0.5)
            my_pocket.append("사과")
            print("내 주머니에 사과가 추가되었습니다.")

        # 벌이 나타날경우
        elif result == "벌":
            print("앗, ", result, "이(가) 떨어졌다!")
            time.sleep(0.5)
            print("벌이 나타났습니다!")
            time.sleep(0.6)
            print("아야... 벌에 물렸어!")



    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
        print("\n내 정보")
        time.sleep(0.5)

        # 이름 출력
        print("- 이름 : ", name)

        # 남은 벨 출력
        print("- 남은 벨 : ", my_bell)

        # 주머니 출력
        print("- 내 주머니 : ", my_pocket)

        # 주민 친밀도 출력
        print("- 주민과 친밀도 : ")
        
        for i in range(4):
            print(str(i+1), ". ", animal[i][0], ": ", animal[i][1])
            

        time.sleep(1)
        
        
        
    # 잘못된 입력을 했을경우
    else:
       print("\n다른 활동을 골라줘구리!")
       time.sleep(0.7)

