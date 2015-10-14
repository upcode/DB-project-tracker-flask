from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""
    # first once form was submitted and returned users github and displays student info by rendering html template 
    github = request.args.get('github', 'jhacks')
     # takes student_search html from once its 
    # sumbitted and returns student info template 
    first, last, github = hackbright.get_student_by_github(github) 
    html = render_template("student_info.html", first=first, last=last, github=github)
    return html
    #first previous code changed it to the above 
    # github = "jhacks"
    # first, last, github = hackbright.get_student_by_github(github)
    #return "%s is the GitHub account for %s %s" % (github, first, last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""
    #This route renders the info from get_student to student_info template
    first, last, github = hackbright.ge

    return render_template("student_search.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student"""
    if request.method == "POST":
        first_name = request.form["first"]
        last_name = request.form["last"]
        github = request.form["github"]
    else:
        return render_template("new_student_form.html")

    return render_template("confirmation.html", first=first_name, last=last_name, github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
