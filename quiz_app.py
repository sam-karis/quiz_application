import sys
import json
import time
import os

print ("\n WELCOME TO QUIZ APPLICATION \n")
print "This application offer various quizzes on different topics you can check down for more information on how to proceed." 


"""
The function prompt the user to choose what he/ she would like the application to do with the application
"""
def options():
	op_available = ["1","2","3"]
	option = raw_input('\nWhat would you like to do?\n Press 1 to view the tests available\n press 2 to Take a test\n press 3 to Exit\n')
	if option not in op_available:
		print "wrong selection select again and choose one of the option provided below"
		options()
	else:
		if int(option) == 1:
			quiz_list()
		elif int(option) == 2:
			quiz_take()
		elif int(option) == 3:
			sys.exit()




"""
The function import the quiz that the has chosen to take and also calculate the score of the quiz taken 
"""
def quiz_take():
	quiz_lib = quiz_import()
	quiz_list = quiz_lib.keys()
	user_option = []
	for i, quiz in enumerate(quiz_list):
		user_option.append(str(i+1))
		print "\n %d: %s \n"%(i+1,quiz)
	enter_option = raw_input("Enter the number corresponding to the QUIZ you are interested in:\n ").capitalize() # this enable the user to type their option without case sensitive issues
	
	if enter_option not in user_option:
		print "You can press one to view the quiz options available first"
		options()

	quiz_type = quiz_list[int(enter_option) - 1]
	start_time = time.clock()

	print "\nTo answer the questions choose one of the multiple choices given below each question\n"
	print "This test should take approximately %d minutes\n" % quiz_lib[quiz_type]["quiz_time"]

	num_quiz = len(quiz_lib[quiz_type]["question"])
	score = 0	
	for i in range(num_quiz):
		print quiz_lib[quiz_type]["question"][i]["qn_text"]
		key_sort = sorted(quiz_lib[quiz_type]["question"][i]["options"])
		for key in key_sort:
			answer = quiz_lib[quiz_type]["question"][i]["options"][key]
			print key,answer

		user_ans = raw_input("Enter you answer?\n").upper()

		if user_ans not in key_sort:
			user_ans = raw_input("One last attempt choose one of the option given\n").upper()

		if user_ans == quiz_lib[quiz_type]["question"][i]["is_answer"]:
			score += 1
	end_time = time.clock()
	taken_time = round((end_time - start_time)/60.0, 2)

	print "You got a score of %d out of %d in %d minutes\n" %(score, num_quiz, taken_time)

	options()

"""
The function list the the different quiz type available in the json file  for the user to view them
"""
def quiz_list():
	quiz_lib = quiz_import()
	quiz_list = quiz_lib.keys()
	print "Below is a list of quiz you can take"

	for i,quiz in enumerate(quiz_list):
		print "\n %d : %s " %(i+1,quiz)

	options()

"""
the function open and load a quiz from a json file 
"""
def quiz_import():
	quiz_open = open(os.path.abspath("Quiz_application.json")).read()
	quiz_load = json.loads(quiz_open)
	return quiz_load

	options()

options()