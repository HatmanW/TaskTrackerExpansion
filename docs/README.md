# TaskTrackerExpansion
Task Tracker Expansion is a task tracker addon for Github Project that allow users to organizes tasks in a Eisenhower Matrix

## Installation
First install Python, Pip, and Docker.

Then from your target directory:
```bash
git clone https://github.com/HatmanW/TaskTrackerExpansion
```

## Getting Started
To run Task Tracker,
```bash
docker-compose up
```

# License
The MIT License (MIT)

Copyright (c) John B. Winchester, Tyler S. McCoid 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## User Stories
User-Stories
The user stories identify a user role, goal, and rationale that dictates a user’s behavior in the product to be created or assessed.

# User Stories
As a user/role, I want to goal so I can rationale.
0. As a User, I want to be able to read tasks, so that I can read my tasks.
1. As a User, I want to be able to add tasks, so I can create a matrix. 
2. As a User, I want to be able to delete tasks, so I can update the matrix to be the most accurate.
3. As a User, I want to be able to update the prioity of a task, so I can tell what tasks are the most important
4. As a User, I want to be able to update my task information, so I can edit my tasks accordingly to my situation. 
5. As a User, I want to be able to log in/log out so my task tracking is only showing my tasks. 
6. As a user, I want to be able to integrate with github projects. 
7. As a User, I want to be able to check off my tasks, and place them in a completed tasks section for review. 
8. As a User, I want to be able to review my tasks that I have checked off. 

# User stories Acceptance criteria 
0. As a User, I want to be able to read tasks, so that I can read my tasks.
Acceptance criteria: If logged in user can view their tasks effectively.

1. As a User, I want to be able to add tasks, so I can create a matrix. 
Acceptance criteria: If logged in user can add a task to a particular category.

3. As a User, I want to be able to delete tasks, so I can update the matrix to be the most accurate.
Acceptance criteria: If logged in user can can delete a task that is no longer relevent.

5. As a User, I want to be able to update the prioity of a task, so I can tell what tasks are the most important
Acceptance criteria: If logged in user can update where their task belongs in the task matrix.
  
6. As a User, I want to be able to update my task information, so I can edit my tasks accordingly to my situation. 
Acceptance criteria: If logged in user can chante their task information individually.

8. As a User, I want to be able to log in/log out so my task tracking is only showing my tasks. 
Acceptance criteria: If logged in user can log in, and log out.

10. As a user, I want to be able to integrate with github projects. 
Acceptance criteria: If a logged in user can see the tasks on github projects.

12. As a User, I want to be able to check off my tasks. 
Acceptance criteria: If a logged in user can check and uncheck tasks as completed or in progress.

14. As a User, I want to be able to review my tasks that I have checked off. 
Acceptance criteria: If the user can read and edit completed tasks. 

# Mis-user stories
In addition to the user stories identify the ways in which users might be able to mis-use your app. Mis-user stories are just like user stories except the user, goal, and rationale are malicious.

0. 
1. As a malicious user, I want to be able to log in to someone elses acount, to change their tasks. 
2. As a malicious user, I want to be able to MIM to spy or change someone elses's tasks. 


