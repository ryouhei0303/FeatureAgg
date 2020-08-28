import json
import requests
import datetime
import csv
import time

year = ["2019", "2020"]
month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
language = ["python","Java"]

for l in language:
  print(l)
  for y in year:
    for m in month:
      check_point = y + "年" + m + "月"
      print(check_point)
      url = "https://api.github.com/search/repositories?q=created%3A" + y + "-" + m + "+language%3A" + l
      response = requests.get(url)
      data = json.loads(response.text)
      x = data["total_count"]
      print(x)

      with open("Data.csv", "a") as csvFile:
        fieldnames = [ "Language", "date", "count"]
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writerow({ "Language":l, "date":check_point,"count":x})
        csvFile.close()
        time.sleep(7)