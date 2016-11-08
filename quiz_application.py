import sys
import json

# It open and read the data in the json file
Data = open("C:\Users\FESTUS\Documents/bootcamp11\Quiz_application.json").read()
QUIZ = json.loads(Data)

print ("\n WELCOME TO QUIZ APPLICATION \n")
print "This application offer various test on different topics you can check down for more information on how to proceed. \n\n " 

#The function prompt the user to choose what he/ she would like the applicatin to do with the application
def options():
	option = raw_input('\nWhat would you like to do?\n Press 1 to view the tests available \n press 2 to Take a test \n press 3 to Exit\n')
	if int(option) == 1:
		Quiz_list()
	elif int(option) == 2:
		Quiz_take()
	elif int(option) == 3:
		sys.exit()
	else:
		print "wrong selection select again"
		options()

#The function import the quiz that the has choosen to take and also calculate the score of the quiz taken 
def Quiz_take():
	quiz_type = raw_input("choose your QUIZ:\n").capitalize()
	num_quiz =  len(QUIZ[quiz_type][0])
	Score = 0
	for i in range (num_quiz):
		print "\n \n %s \n \n " % QUIZ[quiz_type][0][i]
		print "\n \n %s \n \n " % QUIZ[quiz_type][1][i]
		ans = raw_input("Enter you answer?\n").upper()
		if ans == QUIZ[quiz_type][2][i]["is_answer"]:
			Score += 1
	print "You got a score of %d out of %d \n" %(Score, num_quiz)
	options()


#The function fecthes the the different quiz type available in the json file  for the user to view them
def Quiz_list():
	print "\n Below is a list of tests you can attempt \n \n %s  \n " % QUIZ.keys()
	options()


options()
