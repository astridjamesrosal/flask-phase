# Pando - Plan. Do. 
> A self-directed Flask Project for logging and tracking daily study sessions.

# Features
- Navigation Bar for navigating between pages
- Main Hub for showing either Empty Logs or display Study Sessions by Card
- Adding a Study Session with Subject, Start and End Time, Key Takeaways, and Productivity Rating
- Confirmation before Deletion of Session Log

# How to Run
1. Clone the repository
2. Navigate to project5_study_tracker/
3. Run: python session_app.py
4. Open http://127.0.0.1:5000 in your browser

# What I learned
- Implemented Flask Routing - Uses the @app.route() decorators to map URLs to Python functions that handles specific actions that the user requests.
- HTTP Request and Response Cycle - GET method request serves the pages and forms that requires information to the user. POST method request submits the form data to the server where Flask will read it via request.form and it will process it first before redirecting.
- Implemented Separation of Python Files - session_app.py and database.py are separate in order to keep the maintenance and debugging of code easier. session_app.py handles all the routing and presentation of the website logic, while database.py handles the CRUD operations on SQLite.
- What I could improve on is to never name route functions the same as imported database functions — causes naming conflicts

# What I would add in the future
- Built-in session timer — a floating button that starts and stops a timer, automatically filling in start and end times on the add session form.
- We could also add Subject Goals Per Week
- We could also add a Table showing Productivity Chart based on the previous Productivity Ratings

# Preview
![Empty Main Hub](Pando_Empty-Main-Hub.jpg)
![Main Hub](Pando_Main-Hub.jpg)
![Adding A Session](Pando_Add-Session.jpg)
![Delete Session Confirmation](Pando_Confirm-Delete.jpg)