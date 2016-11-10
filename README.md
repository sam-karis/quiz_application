# quiz_application(TEST YOURSELF)
###Andela cohort XI boot-camp week two project

__This is a project done as one of the requirement for completion of Andela cohort XI application process__

quiz_application(*TEST YOURSELF*) is a **console** application that enable users to take quiz on 
different topics of their choice and each question has multiple choices

The application contain the following functionality:

**Command** | **Purpose(Explanation)**
------------|-------------------------
quiz list | list available quizzes in the library
quiz import | Import a quiz from a json file 
quiz take | It prompt the user to take a quiz
option | It enable the user to choose what to do with app

###WHAT USERS CAN DO WITH THE APP
1. view the quizzes available in the library
2. Choose the quiz to take
3. At the end of each quiz the user get a score based on the answers he/she gets right
4. At end of the quiz the user gets to know how long it took him/her to complete the quiz
5. User are given only one attempt in case of typing an answer that does not exist otherwise
   the app conclude the user does not know the right answer.

###SETUP

1. Navigate to a directory of your choice in you computer on **terminal**
2. Clone a repository on that directory:
    * using SSH 
       * git@github.com:sam-karis/quiz_application.git
      
    * Using HTTPS
       * https://github.com/sam-karis/quiz_application.git
 3. Navigate to the repo on terminal and run the app with the command 
      *python quiz_app.py*
      
     
###Bug
1. creating an online quiz repository has an error of creating several repo instead of one
    [firebase](https://quiz-app-e9563.firebaseio.com/)
