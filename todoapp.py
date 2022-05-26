from flask import Flask, redirect, render_template, request, url_for, flash

#Ruta donde esta los templates 
app = Flask(__name__, template_folder='templates')

#Clave de la app
app.secret_key = '123456789'

#Arreglo
tareas_pen = []

# Ruta principal
@app.route('/')
def principal():
    return render_template('tablas.html', tareas_pen=tareas_pen)

#Controlador para enviar los datos
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':

        tarea = request.form['tarea']
        correo = request.form['correo']
        prioridad = request.form['prioridad']

        if tarea == '' or correo == '':
            flash('Por favor ingresar todos los campos de texto  y verificar que no esten vacios')
            return redirect(url_for('principal'))
        else:

            flash('Se agrego una nueva tarea a la lista')

            tareas_pen.append({'tarea': tarea, 'correo': correo, 'prioridad': prioridad })

            return redirect(url_for('principal'))