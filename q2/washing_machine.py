import time
from time import sleep
from tqdm import tqdm

def get_protocol():
    protocol_info = '''\n++++++++++++++++++++++++++++++++++++++++
    Protcols:
      [0] Insert Coin(s)
      [1] Choose Washing Type 
      [2] Start Washing
      [3] Maintenance Info
    '''
    print(protocol_info)
    option = input("    Enter option: ")
    return int(option)

def choose_insert_coins():
    coins_info = '''\n++++++++++++++++++++++++++++++++++++++++
    Insert Coins:
      [0] 10 cents
      [1] 20 cents
      [2] 50 cents
      [3] 1 dollar
      [4] Back
    '''
    print(coins_info)
    option = input("    Enter option: ")
    return int(option)


def choose_washing_type():
    washing_types_info = '''\n++++++++++++++++++++++++++++++++++++++++
    Washing Types:
      [0] Quick Wash (10 minutes - $2)
      [1] Mild Wash (30 minutes - $2.50)
      [2] Medium Wash (45 minutes - $4.20)
      [3] Heavy Wash (1 hour - $6)
    '''
    print(washing_types_info)
    option = input("    Enter option: ")
    globals()['washing_type'] = int(option)
    washing_types_info_array = ['[0] Quick Wash (10 minutes - $2)','[1] Mild Wash (30 minutes - $2.50)','[2] Medium Wash (45 minutes - $4.20)','[3] Heavy Wash (1 hour - $6)']
    print("Washing Type of:", washing_types_info_array[int(option)], "was chosen")
    return int(option)

def confirm_washing():
    confirm_washing_info = '''\n++++++++++++++++++++++++++++++++++++++++
    Please Select:
      [0] Confirm Start Wash  --> To check balance here and prompt
      [1] Cancel & Refund
    '''
    print(confirm_washing_info)
    option = input("    Enter option: ")
    return int(option)

def wallet_sum(wallet,input):
    # print("input: ", input)
    # print(type(input))
    
    if input == 0:
        
        wallet += 0.1
    elif input == 1:
        wallet += 0.2
    elif input == 2:
        wallet += 0.5
    elif input == 3:
        wallet += 1

    
    globals()['wallet'] = wallet
    print ("Final Balance: $", wallet)

# get_protocol()
def progress_bar(time_taken):
    for i in tqdm(range(time_taken)): ## 10/30/45/60 
        sleep(1) ## update per minute


start_time = time.time()
machine_earnings = 0
wallet = 5
is_locked = 0
washing_pricetime_dict = {0:[2,10],1:[2.5,30],2:[4.2,45],3:[6,60]}

washing_type = "\n+++++++++++ Washing type unchosen, please choose in [1] +++++++++++\n"
  
while True:

    choice_get_protocol = get_protocol()
    if(choice_get_protocol == 0):
        print ("Current Balance: ", wallet)
        wallet_sum(wallet, choose_insert_coins())   

    elif(choice_get_protocol == 1):
        choice_washing_type = choose_washing_type()
    
    elif(choice_get_protocol == 2):
        ## check if user chosen washing type
        print("washing type:", washing_type)
        print(type(washing_type))
        if (washing_type not in [0,1,2,3]):
            print(washing_type)

        else:
            choice_confirm_washing = confirm_washing()
            if (choice_confirm_washing==0):
                required_amount = washing_pricetime_dict[choice_washing_type][0]



                ## Insufficient balance
                if (wallet < required_amount):
                    print('inssuficient wallet balance: $' + str(wallet) + "\nRequired amount: $" + str(required_amount))
                else:
                    ## Check Door Lock
                    while (is_locked != 1):
                        print("door is not locked, please press 1 to lock door")
                        user_input = input()
                        if (user_input == "1"):
                            is_locked = 1
                            break
                        # else:
                        #     is_locked = int(input())

                    ## Deduct Money and Start Washing
                    remaining_amount = wallet - required_amount
                    machine_earnings += required_amount
                    if (remaining_amount == 0):
                        print("Balance $" + str(remaining_amount) + " no excess")
                    else:
                        print("Balance of $" + str(remaining_amount) + " will be returned")
                    wallet = 0

                    required_time = washing_pricetime_dict[choice_washing_type][1]
                    print("++++++++++ Starting Wash Cycle ++++++++++")
                    # progress_bar(required_time*60)
                    progress_bar(required_time)
                    while (is_locked != 0):
                        print("door is locked, please press 0 to lock door")
                        user_input = input()
                        if (user_input == "0"):
                            is_locked = 0
                            break
                    print("++++++++++ Collect your fresh Laundry ++++++++++")
            
            ## Cancel Wash and Refund Option
            elif (choice_confirm_washing==1):
                print("Wash cancelled, balance of $" + str(wallet) + " will be returned")
                wallet = 0

    # if(get_protocol() == 3):

    # print(get_protocol_call)