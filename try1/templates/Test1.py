from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def principal():
    return render_template('Test1.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguaje')
def lenguaje():
    mislenguajes=("Python" , "C++" , "Java" , "JavaScript" , "C#")
    return render_template('lenguajes.html' , lenguaje=mislenguajes)

if __name__=='__main__':
    app.run(debug=True)