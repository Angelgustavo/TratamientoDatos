from flask import Flask, jsonify, request


app = Flask(__name__) # Inicializar una aplicacion de tipo Flask

@app.route('/')
def home(): #Ruta principal
    #return "Bienvenido a mi microservicio!"
    return jsonify({"mensaje":"Bienvenido a mi microservicio!"}) # Devuelve un mensaje de bienvenida en formato JSON

@app.route('/api/sumar', methods=['POST']) # Ruta para sumar dos numeros, metodo POST
def sumar():
    data = request.get_json() # Obtener los datos enviados en formato JSON
    a = data.get('a') # Obtener el valor de 'a' del JSON   
    b = data.get('b')  # Obtener el valor de 'b' del JSON
    if a is None or b is None: # Validar que ambos numeros esten presentes
        return jsonify({"error": "Faltan los numeros 'a' o 'b' en el JSON"}), 400 # Si falta alguno, devuelve un error
    resultado = a + b # Sumar los dos numeros
    return jsonify({"resultado": resultado})

@app.route('/api/info', methods=['GET']) # Ruta para obtener informacion del microservicio, metodo GET
def info():
    return ({
        'nombre': 'Microservicio de Suma',
        'version': '1.0'
    })

if __name__ == '__main__': #Ejecuta mi aplicacion cuando yo llame el script
    app.run(debug=True, host='0.0.0.0', port=8080) # Cuando ejecutes, corre el app. Host local = 0.0.0.0. Puerto donde va a ser visible mi aplicacion