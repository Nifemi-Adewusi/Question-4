import socket
import calendar

IP_ADDRESS = 'localhost'

PORT = 9090

def getMonth(month):
    mon = calendar.month_name[month]
    print(mon)
    return mon

def showResult(day, sign):
    return f"Your week day of birthday is {day} and your zodiac sign is {sign}"

def getZodiacSign(year, mm, month, date):
    weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = calendar.weekday(year, mm, date)
    day = weekDays[days]

    print(day)

    output = ""

    if month == "March" and date >= 21 or month == "April" and date <= 19:
        # output = f"Your week day of birthday is {day} and your zodiac sign is Aries"
        output = showResult(day, "Aries")
    elif month == "June" and date >= 21 or month == "July" and date <=22:
        output = showResult(day, "Cancer")
    elif month == "September" and date <= 23 or month == "October" and date <=22:
        output = showResult(day, "Libra")
    elif month == "December" and date >= 22 or month == "January" and date <=19:
        output = showResult(day, "Capricorn")
    elif month == "April" and date >= 20 or month == "May" and date <= 20:
        output = showResult(day, "Taurus")
    elif month == "July" and date >= 23 or month == "August" and date <= 22:
        output = showResult(day, "Leo")
    elif month == "October" and date >=23 or month == "November" and date <= 21:
        output = showResult(day, "Scorpio")
    elif month == "January" and date >= 20 or month == "February" and date <= 18:
        output = showResult(day, "Aquarius")
    elif month == "May" and date >= 21 or month == "June" and date <= 20:
        output = showResult(day, "Gemini")
    elif month == "August" and date >= 23 or month == "September" and date <= 22:
        output = showResult(day, "Virgo")
    elif month == "November" and date >=22 or month == "December" and date <= 21:
        output = showResult(day, "Sagittarus")
    elif month == "February" and date >= 19 or month == "March" and date <=20:
        output = showResult(day, "Pisces")
    return output




ss = socket.socket(family=socket.AF_INET, type= socket.SOCK_STREAM)
ss.bind((IP_ADDRESS, PORT))
ss.listen(5)
connection, address = ss.accept()
msg_from_client = connection.recv(1024).decode()
print(msg_from_client)
msg_to_client = "Kindly Send Your Birthday"
connection.send(msg_to_client.encode("ascii"))
msg_from_client = connection.recv(1024).decode()
split = msg_from_client.split()
year = int(split[0])
month = int(split[1])
date = int(split[2])
clientMonth = getMonth(month)
zodiacSign = getZodiacSign(year, month, clientMonth, date)
connection.send(zodiacSign.encode("ascii"))

