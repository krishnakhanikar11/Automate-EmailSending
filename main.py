import pandas
from datetime import date
import random
import smtplib

MY_EMAIL = "pythonemail.day32@gmail.com"
PASSWORD = "abcd1234()"

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {
     #dict comprehension
     (data_row['month'],data_row['day']) : data_row for (index,data_row) in data.iterrows()
}

today = date.today()
today_tuple = (today.month, today.day)

if today_tuple in birthdays_dict:
     name_to = birthdays_dict[today_tuple]['name']
     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
     with open(file_path) as final:
          content = final.read()
          content = content.replace("[NAME]",name_to)

     with smtplib.SMTP("smtp.gmail.com") as connection:
          connection.starttls()
          connection.login(MY_EMAIL,PASSWORD)
          connection.sendmail(
               from_addr=MY_EMAIL,
               to_addrs=birthdays_dict[today_tuple]['email'],
               msg=f"Subject:Happy Birthday!\n\n{content} "
          )








