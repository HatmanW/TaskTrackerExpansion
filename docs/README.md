# TaskTrackerExpansion
## AKA IkesTaskTrackerExpansion

Task Tracker Expansion is a task tracker addon for Github Project that allow users to organizes tasks in a Eisenhower Matrix
The Eisenhower Matrix has a lot of literature but no one really visualizes it correctly. 

Asana's how to on the Eisenhower Matrix

Asana puts the Eisenhower Matrix best:

"The Eisenhower Matrix is a task management tool that prioritizes tasks by urgency and importance. 
The tool divides tasks into four boxes based on what to do first, what to schedule, what to delegate, what to not do."



https://asana.com/resources/eisenhower-matrix

Todoist's Video on how to use the Eisenhower Matrix. 
https://todoist.com/productivity-methods/eisenhower-matrix



Some observations I've had when using the matrix, specifically on the delete section. 
If you feel a task is important enough to write down, it may change priority as time goes on. 
You may find the task was more important or is now more urgent, but you will see that much of the tasks change locations as priorities and urgency change. This is by design. 
By sectioning things accordingly it's easy for someone to keep track of their tasks, and allows you to focus on one section of your tasks at once time rather then strictly time, or strictly urgency, or how other sorting methods work. 
it's also a different mentality of putting something in 'delete' instead of "don't do" so that you can potentially be aware of the task, but not deleteing the task from your tasks when the task may change urgency or importance.


## Installation
Install Python 

Then from your target directory:
```bash
git clone https://github.com/HatmanW/TaskTrackerExpansion
```

## Getting Started
To run Task Tracker,
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## User Stories section
User-Stories The user stories identify a user role, goal, and rationale that dictates a user’s behavior in the product to be created or assessed.
# User Stories
As a user/role, I want to goal so I can rationale. 0. As a User, I want to be able to read tasks, so that I can read my tasks.


1.	As a User, I want to be able to add tasks, so I can create a matrix.
2.	As a User, I want to be able to delete tasks, so I can update the matrix to be the most accurate.
3.	As a User, I want to be able to update the prioity of a task, so I can tell what tasks are the most important
4.	As a User, I want to be able to update my task information, so I can edit my tasks accordingly to my situation.
5.	As a User, I want to be able to log in/log out so my task tracking is only showing my tasks.
6.	As a user, I want to be able to integrate with github projects.
7.	As a User, I want to be able to check off my tasks, and place them in a completed tasks section for review.
8.	As a User, I want to be able to review my tasks that I have checked off.


# User stories Acceptance criteria
Acceptance Crieteria is 

1.	As a User, I want to be able to read tasks, so that I can read my tasks.

1.1.	 Acceptance criteria: If logged in user can view their tasks effectively.

2.	As a User, I want to be able to add tasks, so I can create a matrix.

2.1.	 Acceptance criteria: If logged in user can add a task to a particular category.

3.	As a User, I want to be able to delete tasks, so I can update the matrix to be the most accurate.

3.1.	 Acceptance criteria: If logged in user can can delete a task that is no longer relevent.

4.	As a User, I want to be able to update the prioity of a task, so I can tell what tasks are the most important

4.1.	 Acceptance criteria: If logged in user can update where their task belongs in the task matrix.

5.	As a User, I want to be able to update my task information, so I can edit my tasks accordingly to my situation.

5.1.	 Acceptance criteria: If logged in user can chante their task information individually.

6.	As a User, I want to be able to log in/log out so my task tracking is only showing my tasks.

6.1.	 Acceptance criteria: If logged in user can log in, and log out.

7.	As a user, I want to be able to integrate with github projects.

7.1.	 Acceptance criteria: If a logged in user can see the tasks on github projects.

8.	As a User, I want to be able to check off my tasks.

8.1.	 Acceptance criteria: If a logged in user can check and uncheck tasks as completed or in progress.

9.	As a User, I want to be able to review my tasks that I have checked off. 

9.1.	 Acceptance criteria: If the user can read and edit completed tasks.


# Mis-user stories
In addition to the user stories identify the ways in which users might be able to mis-use your app. Mis-user stories are just like user stories except the user, goal, and rationale are malicious.


1.	As a malicious user, I want to log in to someone elses acount, to change their tasks.
2.	As a malicious user, I want to intercept communication with a Machine in the Middle attack. 
3.	As a malicious user, I want to inject SQL commands that will allow manipulation of the database
4.	As a malicious user, I want to use the API endpoints so retrieve or manipulate data I’m not supposed to have access to. 
5.	As a malicious user, Weak Password Exploit


# Mis-User stories acceptance criterial 
Acceptance Criteria for Mis-User stories is going to end up a bit different, as we’ll define a clear success case from a mis user, as well as a defense against that malicious action. 

1.	As a malicious user, I want to log in to someone else’s account, to change their tasks.
   
1.1.	Acceptance Criteria: Malicious User successfully uses stolen Credentials to access someone else’s account

1.1.1.	Multi Factor Authentication – this decreases the chances of a unintended user dramatically.

1.1.2.	Password Policies – Having strong password policies with sufficient enough complexity will help depend against unauthorized Account Access.

1.1.3.	Lockouts – Timed lockouts that increase unless an authorized email resets the account credentials.

1.1.4.	Authentication Mechanisms – this is similar to implementing the email a verification code. This means an attacker would have to have multiple authorization points compromised in order to successfully complete a Unauthorized Account Access.

2.	As a malicious user, I want to intercept communication with a Machine in the Middle attack. 

2.1.	Acceptance Criteria User intercepts communication for credential access or to view user’s activity. 

2.1.1.	Encryption - HTTPS (More secure HTTP) and TLS(Transport Layer Seurity Specifically 

2.1.1.1.	Github is already implementing HTTPS

2.1.2.	SSL (Secure Socket Layer) - for certificates though it may be an over stretch

2.1.3.	Audit – Red teaming to find the vulnerabilities as they appear

3.	As a malicious user, I want to inject SQL commands that will allow manipulation of the database 

3.1.	Acceptance Criteria Utilizing SQL commands unathorized manipulation of the database occurse

3.1.1.	Input Sanitization – if a user can’t utilize common SQL queries they can’t be entered by abnormal means. 

3.1.2.	Error handling – the database should only print out database error details in specific cases for specific accounts

3.1.3.	Database Role Permission – only set users should be able to see certain database information. 

4.	As a malicious user, I want to use the API endpoints so retrieve or manipulate data I’m not supposed to have access to.

4.1.	Acceptance Criteria Malicious user uses API endpoints to achieve Create Read Update and Delete access to accounts outside of their own. 

4.1.1.	API authentication – API keys for API requests

4.1.1.1.	Github may have this enabled already

4.1.2.	Input Validation – Similar to above, make sure that only validated input can be used in API inputs

4.1.2.1.	Check API endpoints from what we learned in the Postman labs. 

4.1.3.	Audit and Logging – As a part of access control, logging who is making what queries is necessary for more sensitive information. 

5.	As a malicious user, I want to take advantage of weak passwords to gain access to other users tasks. 

5.1.	Acceptance Criteria 

5.1.1.	Password Strength indicators – Show how well a User’s passwords will stand up to various attacks.

5.1.1.1.	This is something I think Github also does already  

5.1.2.	Disallow bad passwords – common passwords and passwords that repeat the username, or fail to meet a certain criteria. 

5.1.3.	Password Rotation – change the password fully every 3 months. Don’t allow the same password. 

# Mockup
A early mockup of how the task tracker final product will look like.

![alt text](https://github.com/HatmanW/TaskTrackerExpansion/blob/main/docs/Full%20Mockup.jpg?raw=true)

Add and Edit tasks

![alt text](https://github.com/HatmanW/TaskTrackerExpansion/blob/main/docs/Add%20and%20Edit%20Mockup.jpg?raw=true)

Login Page

![alt text](https://github.com/HatmanW/TaskTrackerExpansion/blob/main/docs/Login.jpg?raw=true)

# Architecture diagrams
Level 1
![alt text](https://github.com/HatmanW/TaskTrackerExpansion/blob/main/docs/ExtendedTaskTrackerLvl1.png)

Level 2
![alt text](https://github.com/HatmanW/TaskTrackerExpansion/blob/main/docs/ExtendedTaskTrackerLvl2.png)

Level 3
![alt text](https://github.com/HatmanW/TaskTrackerExpansion/blob/main/docs/ExtendedTaskTrackerLv3.png)

Note: that these will be update as we uncover a lot of the information on Github's technology stacks and how best to integrate them with the Django application. 

# LICENSE
AI disclaimer: 
This project includes code generated using OpenAI's ChatGPT, which was modified to suit the specific requirements of this project.

The MIT License (MIT)

Copyright (c) John B. Winchester, Tyler S. McCoid 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
