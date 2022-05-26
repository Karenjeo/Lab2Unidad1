#Importacion de libreria
from flask import Flask, redirect, render_template, request, url_for
#Clave de la app
#Ruta donde esta los templates y la clave de flash
app = Flask(__name__, template_folder='templates')
#Arreglo
tareas_pen = []

# Ruta principal
@app.route('/')
def principal():
    return render_template('tablas.html', tareas_pen=tareas_pen)

#Ruta enviar 
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        tarea = request.form['tarea']
        correo = request.form['correo']
        prioridad = request.form['prioridad']

        tareas_pen.append({'tarea': tarea, 'correo': correo, 'prioridad': prioridad })

        return redirect(url_for('principal'))
            
#Controlador de la ruta para borrar
@app.route('/borrar', methods=['POST'])
def borrar():  
    if request.method == 'POST':

            tareas_pen.clear()
            return redirect(url_for('principal'))

#Ejecutar
if __name__ == '__main__':
    app.run(debug=True)