from com.bridgelab.functional.Utility import getInput


def questionToFindYourNumber(start, last):
    while start <= last:
        mid = int((start + last) / 2)
        if getInput("are you guess this number : ", mid) == 1:
            print("Number found.")
            break
        elif int(getInput("If your number will greater than then enter 1 else 0 : ", mid)) == 1:
            start = mid + 1
        elif int(getInput("If your number will less than then enter 1 else 0 : ", mid)) == 1:
            last = mid - 1


questionToFindYourNumber(1, 10)
