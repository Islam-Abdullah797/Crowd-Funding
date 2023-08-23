import Re_Log_Forg as RL
import project as PR
print("===============================================")
print("=================== Welcome ===================")
print("===============================================")

Choice = input("For Registration Please Enter 'R': \nIF You Already Have An Acount Please Enter 'L': ")
if Choice.lower() == "r":
    Ac=RL.Register()
    if Ac == 'success':
        PR.Project_Choice() 
elif Choice.lower() == 'l':
    Log = RL.Login()
    if Log == True:
        print("========== Create Your Project ==========")
        PR.Project_Choice()
    elif Log == 'forget':
            forg = RL.Forgett()
            if forg == 'login':
                RL.Login()
            else:
                RL.Register() 
    elif Log == 'ask register':
        RL.Register()
else:
    print("Please Just Enter R or L :")                
