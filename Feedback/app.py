from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_feedback (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        email TEXT,
                        feedback TEXT,
                        rating INTEGER
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS driver_feedback (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        driver_id TEXT,
                        feedback TEXT,
                        rating INTEGER
                    )''')
    conn.commit()
    conn.close()

# Home route to render the feedback form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        # Check if form data is from customer or driver
        if 'customer-name' in request.form:
            # Customer feedback form data
            name = request.form['customer-name']
            email = request.form['customer-email']
            feedback = request.form['customer-feedback']
            rating = int(request.form['customer-rating'])
            # Save to customer_feedback table
            conn = sqlite3.connect('feedback.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customer_feedback (name, email, feedback, rating) VALUES (?, ?, ?, ?)",
                           (name, email, feedback, rating))
            conn.commit()
            conn.close()
        elif 'driver-name' in request.form:
            # Driver feedback form data
            name = request.form['driver-name']
            driver_id = request.form['driver-id']
            feedback = request.form['driver-feedback']
            rating = int(request.form['driver-rating'])
            # Save to driver_feedback table
            conn = sqlite3.connect('feedback.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO driver_feedback (name, driver_id, feedback, rating) VALUES (?, ?, ?, ?)",
                           (name, driver_id, feedback, rating))
            conn.commit()
            conn.close()
        
        # Redirect back to home after submission
        return redirect(url_for('index'))

# Route to view feedback
@app.route('/view-feedback')
def view_feedback():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    
    # Retrieve customer and driver feedback
    cursor.execute("SELECT name, email, feedback, rating FROM customer_feedback")
    customer_feedback = cursor.fetchall()
    
    cursor.execute("SELECT name, driver_id, feedback, rating FROM driver_feedback")
    driver_feedback = cursor.fetchall()
    
    conn.close()
    
    # Pass the data to the template
    return render_template('view_feedback.html', customer_feedback=customer_feedback, driver_feedback=driver_feedback)

if __name__ == '__main__':
    init_db()  # Create tables if they don't exist
    app.run(debug=True)
