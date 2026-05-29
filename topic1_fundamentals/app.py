from flask import Flask, render_template, request   #Imports Flask to create the app, render_template to serve HTML files, and request to read incoming form data.

app = Flask(__name__)                               #Creates the Flask application instance. __name__ tells Flask where to find templates and static files.

@app.route('/')                                     #Registers the "/" URL to the index() function. Flask calls index() when this route is requested.
def index():                                        #A function for the index.
    return render_template('index.html')            #Finds the html file where the template would be used for user input.

@app.route('/greet', methods=['GET', 'POST'])       #For the request to find the route and call greet().
def greet():                                        #Called by Flask when /greet is requested.
    if request.method == 'POST':                    
        name = request.form['username']             #A way of reading the that arrived in the request form. username is the key.
        return render_template('greet.html', name=name) #Calls this to fill the slot in the html with the variable name maria entered.
    return render_template('index.html')            #If the request is GET, just show the form page again.

if __name__ == '__main__':                          #Ensures that the file is being run directly. To prevent unintentional server starts.
    app.run(debug=True)