import sys
import json
import time


# It open and read the data in the json file
Data = open("C:\Users\FESTUS\Documents/bootcamp11\quiz_library.json").read()
QUIZ = json.loads(Data)



print ("\n WELCOME TO QUIZ APPLICATION \n")
print "This application offer various quizzes on different topics you can check down for more information on how to proceed. \n\n " 

#The function prompt the user to choose what he/ she would like the application to do with the application
def options():
	op_available = ["1","2","3"]
	option = raw_input('\nWhat would you like to do?\n Press 1 to view the tests available \n press 2 to Take a test \n press 3 to Exit\n')
	if option not in op_available:
		print "wrong selection select again and choose one of the option provided below"
		options()
	else:
		if int(option) == 1:
			Quiz_list()
		elif int(option) == 2:
			Quiz_take()
		elif int(option) == 3:
			sys.exit()


#The function import the quiz that the has chosen to take and also calculate the score of the quiz taken 
def Quiz_take():
	quiz_import()
	quiz_list = QUIZ.keys()
	for quiz in quiz_list:
			print quiz
	quiz_type = raw_input("Type the name of one of the QUIZ listed above:\n ").capitalize()
	if quiz_type not in quiz_list:
		print "You can press one to view the quiz available first"
		options()
	start_time = time.clock()
	print "\nTo answer the questions choose one of the options given below each question\n"
	print "You have %d minutes to take the test" % QUIZ[quiz_type]["quiz_time"]
	num_quiz = len(QUIZ[quiz_type]["question"])
	score = 0

	for i in range(num_quiz):
		print QUIZ[quiz_type]["question"][i]["qn_text"]
		key_sort = sorted(QUIZ[quiz_type]["question"][i]["options"])
		for key in key_sort:
			answer = QUIZ[quiz_type]["question"][i]["options"][key]
			print key,answer

		user_ans = raw_input("Enter you answer?\n").upper()

		if user_ans not in key_sort:
			user_ans = raw_input("One last attempt choose one of the option given\n").upper()

		if user_ans == QUIZ[quiz_type]["question"][i]["is_answer"]:
			score += 1
	end_time = time.clock()
	taken_time = round((end_time - start_time)/60.0, 2)

	print "You got a score of %d out of %d in %d minutes\n" %(score, num_quiz, taken_time)

	options()

#The function fetches the the different quiz type available in the json file  for the user to view them
def Quiz_list():
	quiz_import()
	quiz_list = QUIZ.keys()
	print "Below is a list of quiz you can take"

	for quiz in quiz_list:
		print "\n",quiz

	options()

def quiz_import():
	Data = open("C:\Users\FESTUS\Documents/bootcamp11\quiz_library.json").read()
	QUIZ = json.loads(Data)
	return QUIZ


options()