import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)



def init_db():
    conn = sqlite3.connect('notes.db')
    
    conn.execute('''CREATE TABLE IF NOT EXISTS notes( id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT NOT NULL)''')
    conn.commit()
    conn.close

init_db()





@app.route('/')
def home():
    return render_template('home.html')






@app.route('/notes',methods=['GET','POST'])
def notes_pages():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
 
            conn= sqlite3.connect('notes.db')
            conn.execute("INSERT INTO notes(text) VALUES(?)",(note,))

            conn.commit()
            conn.close()
            

        return redirect('/notes')

    conn=sqlite3.connect('notes.db')
    notes = conn.execute("SELECT * FROM notes").fetchall()

    return render_template('notes.html',notes=notes)






@app.route('/delete/<int:id>', methods=['POST'])
def delete_note(id):

    conn = sqlite3.connect('notes.db')

    conn.execute(
        "DELETE FROM notes WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/notes')

 

if __name__=="__main__":
    app.run(debug=True)
