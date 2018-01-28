from datetime import datetime, date

print("Your date of birth (dd mm yyyy)")
DATE_OF_BIRTH = datetime.strptime(input("--->"), "%d %m %Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

AGE = calculate_age(DATE_OF_BIRTH)

print(AGE)
