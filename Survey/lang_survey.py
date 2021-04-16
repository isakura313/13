from Survey import *

question = "Какой язык хотите изучать первым?"
my_survey = Survey(question)

my_survey.show_question()
print("q  для остановки программы ?")
while True:
    response = input('Язык ')
    if response == "q":
        break
    my_survey.store_response(response)

my_survey.show_results()