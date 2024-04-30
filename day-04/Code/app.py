from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__, static_folder='static')
app.secret_key = "your_secret_key"

# Sample user data (replace with a proper database)
users = {
    "patient1": {"name": "John Doe", "email": "patient1@example.com", "password": "patient1", "role": "patient"},
    "doctor1": {"name": "Jane Smith", "email": "doctor1@example.com", "password": "doctor1", "role": "doctor"}
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match"

        # Save user data (replace with database operations)
        user = {
            "name": f"{username}",
            "email": email,
            "password": password,
            "role": "patient"  # Assume all new signups are patients
        }
        users[username] = user

        return redirect(url_for("login"))

    return render_template("patient_signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            session["user"] = username
            role = users[username]["role"]
            return redirect(url_for(f"{role}_dashboard"))
        return "Invalid username or password"
    return render_template("login.html")
    
@app.route('/register/patient', methods=['GET', 'POST'])
def register_patient():
    if "user" not in session:
        return redirect(url_for("signup"))
        
    return render_template('register_patient.html')

@app.route("/patient_dashboard")
def patient_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    user = users[session["user"]]
    return render_template("patient_dashboard.html", user=user)

@app.route('/register/doctor', methods=['GET', 'POST'])
def register_doctor():
    if "user" not in session:
        return redirect(url_for("signup"))
    return render_template('register_doctor.html')

@app.route("/doctor_dashboard")
def doctor_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    user = users[session["user"]]
    return render_template("doctor_dashboard.html", user=user)

if __name__ == '__main__':
    app.run(debug=True)