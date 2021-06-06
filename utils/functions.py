from itertools import product
import requests as req


def generatePassword(chars, min, max):
    """
        this function gets password chars, password min length and max length
        and generates all possibilities and yields them
    """

    for length in range(int(min), int(max) + 1):
        allPossiblePasswords = product(chars, repeat=length)
        for tplItem in allPossiblePasswords:
            strPassword = "".join(tplItem)
            yield strPassword


def test(url, failureMessage, usernameFormName, passwordFormName, username, testingPassword):
    """
        this function creates a data dictionary, keys are username and password input name in html form
        and values are the username that we know and the password we are testing
        it  returns true if the failureMessage is not in the response text, otherwise false
    """
    data = {}
    data[usernameFormName] = username
    data[passwordFormName] = testingPassword
    response = req.post(url=url, data=data)
    if not failureMessage in response.text:
        return True
    return False
        

