# What is Flask and what problem does it solve 
- Flask is the bridge between A Python function and an HTML Web Page. Basically, the user inputs something, or commands something to process the output they want to get. And then Python will process it, and return the results and show it to the user through the webpage. It solves the problem for the users of seeing a python function and not know what it is just to get the output they desire. But through flask, one click is all it takes to produce something, which you can see immediately without having to look at python codes. Flask is a web framework that maps URLs to Python functions, handles HTTP requests and responses, and serves HTML pages to the browser.

# The request/response cycle 
- Maria will go to the http link and her browser will send a GET request to the URL /
- Flask receives the request and will check its route and call the index function
- Index will run and call the template function.
- Finds index html and jinja2 process it
- Flask sends the html back as response which contains the form for submission by Maria
- When maria click submit, the browser packages the form data using the input's name="username" as key
- The browser will now send a POST request to the URL /greet.
- Flask receives the request and will check its route and call the greet function
- When greet runs, it checks the method which is POST and reads request.form.
- It calls the render template and jinja2 fills the name placeholder slot for Maria's name
- Maria's browser will now display "Welcome, Maria"

# The three concepts and how they connect
- When a user wants to put commands in a website, before they even input anything, routing already starts. The browser sends a GET request, routing receives it and decides which functions run. Forms collect the user input and send it through POST request. Templates display data that Python passes to them. Those data could come from a form, a database, or anywhere.

# What confused me and how it clicked 
- The thing that confused me at first was really the whole process of the cycle. Like I studied first part by part, but when they interconnected I did not know what comes first and how do they like contact each other. But later on, I figured it out and mapped out every step of the cycle.

# One thing I want to remember going into Project 5
- Build the python functions first, before building the html web page to ensure smooth flow because routes and logic determine what data the template needs, so the HTML should follow the Python, not the other way around.