from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import models as dbase 
from usuario import Usuario

db = dbase.dbConnection()
app=Flask(__name__)

# Desplega los datos de la colección
@app.route('/')
def inicio():
    usuarios = db['usuarios']
    #usuariosReceived = usuarios.find()
    return render_template('index.html')

@app.route('/usuarios', methods=['POST'])
def addUsuario():
    usuarios = db['usuarios']
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']
 
    if email and password:
        usuario = Usuario(nombre,email, password)
        usuarios.insert_one(usuario.toDBCollection())
        response = jsonify({
            
            'nombre':nombre, 
            'email' : email,
            'password' : password
        })
        return redirect(url_for('inicio'))
    else:
        return notFound()

#Método de error
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
 app.run('127.0.0.1', 5000, debug=True)
