from flask import Flask, render_template, request, redirect,redirect,session
import sqlite3

app = Flask(__name__)
app.secret_key ="hms_secret"

def db():
    return sqlite3.connect("hospital.db")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = db()
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM admin WHERE username=? AND password=?",
            (username, password)
        )
        user = cur.fetchone()
        con.close()

        if user:
            session["admin"] = username
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/login")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/add_patient", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        con = db()
        con.execute(
            "INSERT INTO patient(name, age, disease) VALUES (?, ?, ?)",
            (request.form["name"], request.form["age"], request.form["disease"])
        )
        con.commit()
        con.close()
        return redirect("/dashboard")
    return render_template("add_patient.html")

@app.route("/add_doctor", methods=["GET", "POST"])
def add_doctor():
    if request.method == "POST":
        con = db()
        con.execute(
            "INSERT INTO doctor(name, specialization) VALUES (?, ?)",
            (request.form["name"], request.form["specialization"])
        )
        con.commit()
        con.close()
        return redirect("/dashboard")
    return render_template("add_doctor.html")

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        con = db()
        con.execute(
            "INSERT INTO appointment(patient_id, doctor_id) VALUES (?, ?)",
            (request.form["patient_id"], request.form["doctor_id"])
        )
        con.commit()
        con.close()
        return redirect("/dashboard")
    return render_template("appointment.html")

@app.route("/view_patients")
def view_patients():
    con = db()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    patients = cur.fetchall()
    con.close()
    return render_template("view_patients.html", patients=patients)

@app.route("/view_doctors")
def view_doctors():
    con = db()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM doctor")
    doctors = cur.fetchall()
    con.close()
    return render_template("view_doctors.html", doctors=doctors)

@app.route("/view_appointments")
def view_appointments():
    if "admin" not in session:
        return redirect("/login")

    con = db()
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("""
        SELECT appointment.id,
               patient.name AS patient_name,
               doctor.name AS doctor_name
        FROM appointment
        JOIN patient ON appointment.patient_id = patient.id
        JOIN doctor ON appointment.doctor_id = doctor.id
    """)

    appointments = cur.fetchall()
    con.close()

    return render_template("view_appointments.html", appointments=appointments)



if __name__ == "__main__":
    app.run(debug=True)
