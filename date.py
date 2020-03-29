import sys

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def canBeMonth(value):
  return value > 0 and value <= 12

def canBeDay(value):
  return value > 0 and value <= 31

def canBeYear(value):
  return (value >= 0 and value <= 999) or (value >= 2000 and value <= 2999)

def getDate(filePath):
  with open(filePath, 'r') as f:
    value = f.read()
  f.close()

  l = value.split("/")
  for i in range(len(l)):
    l[i] = int(l[i])
  l.sort()
  if not (l[0] >= 0 or l[2] > 2999):
    return "it's illegal"
  
  possibleDays = list(filter(canBeDay, l))
  
  if possibleDays:
    day = possibleDays[-1]
    l.remove(day)
  else:
    return "it's illegal"

  possibleMonths = list(filter(canBeMonth, l))
  if possibleMonths:
    month = possibleMonths[-1]
    l.remove(month) 
  else:
    return "it's illegal"

  possibleYears = list(filter(canBeYear, l))
  if possibleYears:
    year = possibleYears[-1]
  else:
    return "it's illegal"
  
  if year <= 999:
    year = year + 2000

  if (( year % 400 == 0) or (( year % 4 == 0 ) and ( year % 100 != 0))):
    daysInMonth[1] = 29

  if not (day > 0 and day < daysInMonth[month-1]):
    day = daysInMonth[month-1]

  if month <= 9:
    month = f"0{month}"
  if day <= 9:
    day = f"0{day}"
  return f"{year}-{month}-{day}"    

if __name__ == "__main__":
  print(getDate(sys.argv[1]))