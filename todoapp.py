#Importacion de libreria
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

#Ruta enviar 
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        tarea = request.form['tarea']
        correo = request.form['correo']
        prioridad = request.form['prioridad']
#Mensaje de alerta para que ingrese todos los campos
        if tarea == '' or correo == '':
            flash('Por favor ingresar todos los campos de texto  y verificar que no esten vacios')
            return redirect(url_for('principal'))
        else:
#Mensaje de que todo fue agregado con exito
            flash('Se agrego una nueva tarea a la lista')
#Llama a las variables 
            tareas_pen.append({'tarea': tarea, 'correo': correo, 'prioridad': prioridad })

            return redirect(url_for('principal'))
            
#Controlador de la ruta para borrar
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':    
        if tareas_pen == []:
#Mensaje que no hay nada de borrar
            flash('No existen tareas en la lista')
            return redirect(url_for('principal'))
#Mensaje que fue borrado con exito 
        else:
            tareas_pen.clear()
            flash('La lista de tareas fue borrada')
            return redirect(url_for('principal'))


#Ejecutar
if __name__ == '__main__':
    app.run(debug=True)