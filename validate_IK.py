import datetime
import sys

def validate_IK(ik_code):
    epochs=(1800, 1800, 1900, 1900, 2000, 2000)
    current_date=datetime.datetime.now()

    def checkSum():
        lastnum = int(ik_code[10])

        wholenum = 0
        for nextSym in range(1, 11):
            wholenum += (nextSym % 9 if nextSym != 9 else 9) * int(ik_code[nextSym - 1])
        wholenum %= 11

        if lastnum == wholenum:
            return True

    def checkDays(year, month):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = int(ik_code[5:7])

        if not year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            days_in_month[1] = 29

        if 0 < days < days_in_month[int(month) - 1]:
            return checkSum()

    def checkMonth(year):
        month = int(ik_code[3:5])
        if 0 < month <= 12:
            return checkDays(year, month)

    def checkYear():
        year_in_code = epochs[int(ik_code[0])] + int(ik_code[1:3])
        if year_in_code <= current_date.year:
            return checkMonth(year_in_code)

    def checkGender():
        index = int(ik_code[0])
        if 1 <= index <= 6:
            return checkYear()

    if ik_code.isdigit():
        if len(ik_code) == 11:
            return checkGender()

    return False

recieved_code = sys.argv[1:]
validate_IK(recieved_code[0])