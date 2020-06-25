import sys
sys.path.append('latch_sdk_python')
import config.latch
import latch
import re
api = latch.Latch(config.latch.appId, config.latch.secret)
def main():
    print("You can:")
    print(" 1.Add a new account to the system.")
    print(" 2.Remove(unpair) an account from the system.")
    print("\n")
    selection = input("What do you want?(1/2): ")
    while selection != "1" and selection != "2":
        selection = input("Invalid answer. Retry(1/2): ")
    print("\n")
    if selection == "1":
        addAccount()
    if selection == "2":
        rmAccount()
def addAccount():
    email = input("I need your email adress for identifying you later. Enter it here: ")
    checkList = re.findall('\S+@\S+', email) 
    while len(checkList) != 1:
        email = input("Invalid format. Retry: ")
        checkList = re.findall('\S+@\S+', email)
    with open('config/accountsEmails.txt', 'r') as f:
        if email in [s.replace('\n', '') for s in f.readlines()]:
            print("Email already in database. You can only register once. Exiting...")
            exit()
    token = input("Click \"Add Latch\" in the Latch app and give me your pairing code: ")
    response = api.pair(token)
    responseData = str(response.get_data())
    #print(responseData)
    while responseData == "":
        print('Error while pairing: ', response.get_error())
        print("Retrying...")
        token = input("Click \"Add Latch\" in the Latch app and give me your pairing code: ")
        response = api.pair(token)
        responseData = str(response.get_data())
    accountId = responseData[15:-2]
    with open('config/accounts.txt', 'r') as f:
        if accountId in [s.replace('\n', '') for s in f.readlines()]:
            print("Account ID already in database. You can only register once. Exiting...")
            exit()
    with open('config/accounts.txt', 'a') as f:
        f.write(accountId + "\n")
    with open('config/accountsEmails.txt', 'a') as f:
        f.write(email + "\n")
    print("Succesful. Bye.")
def rmAccount():
    print("Ok. So, here are the registered accounts's emails:")
    with open('config/accountsEmails.txt', 'r') as f:
        emails = [s.replace('\n', '') for s in f.readlines()]
    with open('config/accounts.txt', 'r') as f:
        accountIds = [s.replace('\n', '') for s in f.readlines()]
    i=0
    for email in emails:
        i=i+1
        print(str(i) + " --- " + email)
    selection = input("\nWhich one do you want to remove(unpair): ")
    while int(selection) <= 0 or int(selection) > i:
        selection = input("Invalid answer. Retry: ")
    accountId = accountIds[int(selection) - 1]
    response = api.unpair(accountId)
    print(response.get_data())
    result = input("Did it work?([Anything]/no): ") 
    if result == "no" or result == "No":
        print(accountId)
        print("There you have your account ID in case you need it. You can retry again later by executing the script. Exiting...")
        exit()
    print("Perfect.")
    del accountIds[int(selection) - 1]
    with open('config/accounts.txt', 'w+') as f:
        for line in accountIds:
            f.write(line + "\n")
    del emails[int(selection) - 1]
    with open('config/accountsEmails.txt', 'w+') as f:
        for line in emails:
            f.write(line + "\n")
    print("Succesful. Bye.")


main()