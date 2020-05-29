from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL



# initializations
app = Flask(__name__)

# Mysql Connection
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'diana'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'pasteleria'
mysql.init_app(app)

# settings
app.secret_key = "mysecretkey"

@app.route('/')
def Index():
    cursor = mysql.connect()
    cur = cursor.cursor()
    cur.execute('SELECT * FROM orden')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', orden_s=data)

# routes
@app.route('/new_pastel_ingredient')
def Index2():
    cursor = mysql.connect()
    cur = cursor.cursor()
    cur2 = cursor.cursor()
    cur.execute('SELECT * FROM pastel')
    cur2.execute('SELECT * FROM ingrediente')
    data = cur.fetchall()
    data2 = cur2.fetchall()
    cur.close()
    cur2.close()
    return render_template('new_pastel_ingredient.html', contacts=data, ingredients=data2)


@app.route('/add_orden', methods=['POST'])
def add_orden():
    if request.method == 'POST':
        cursor = mysql.connect()
        codigo_orden = request.form['codigo_orden']
        fecha_solicitud = request.form['fecha_solicitud']
        fecha_entrega = request.form['fecha_entrega']
        especificaciones = request.form['especificaciones']
        nombre_pastel = request.form['nombre_pastel']
        cedula = request.form['cedula']
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        cur = cursor.cursor()
        cur.execute("INSERT INTO orden (codigo_orden, fecha_solicitud, fecha_entrega, especificaciones, nombre_pastel, cedula, codigo, nombre) VALUES (%s,%s,%s, %s,%s,%s, %s,%s)",
                    (codigo_orden, fecha_solicitud, fecha_entrega, especificaciones, nombre_pastel, cedula, codigo, nombre))
        cursor.commit()
        flash('Orden Added successfully')
        return redirect(url_for('Index'))

@app.route('/new_pastel_ingredient',methods=['GET', 'POST'])
def new_pastel_ingredient():
    return render_template('new_pastel_ingredient.html')

@app.route('/add_cake', methods=['POST'])
def add_cake():
    if request.method == 'POST':
        cursor = mysql.connect()
        nombre_pastel = request.form['nombre_pastel']
        tipo_pastel = request.form['tipo_pastel']
        peso_minimo = request.form['peso_minimo']
        cur = cursor.cursor()
        cur.execute("INSERT INTO pastel (nombre_pastel, tipo_pastel, peso_minimo) VALUES (%s,%s,%s)",
                    (nombre_pastel, tipo_pastel, peso_minimo))
        cursor.commit()
        flash('Cake Added successfully')
        return redirect(url_for('Index2'))


@app.route('/edit/<nombre_pastel>', methods=['POST', 'GET'])
def get_cake(nombre_pastel):
    cursor = mysql.connect()
    cur = cursor.cursor()
    cur.execute('SELECT * FROM pastel WHERE nombre_pastel = %s', (nombre_pastel))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_pastel.html', contact=data[0])


@app.route('/update/<nombre_pastel>', methods=['POST'])
def update_cake(nombre_pastel):
    if request.method == 'POST':
        cursor = mysql.connect()
        cur = cursor.cursor()
        tipo_pastel = request.form['tipo_pastel']
        peso_minimo = request.form['peso_minimo']
        cur.execute("""
            UPDATE pastel
            SET tipo_pastel = %s,
                peso_minimo = %s
            WHERE nombre_pastel = %s
        """, (tipo_pastel, peso_minimo, nombre_pastel))
        flash('Pastel Updated Successfully')
        cursor.commit()
        cur.close()
        return redirect(url_for('Index2'))


@app.route('/delete/<string:nombre_pastel>', methods=['POST', 'GET'])
def delete_cake(nombre_pastel):
    cursor = mysql.connect()
    cur = cursor.cursor()
    cur.execute('DELETE FROM pastel WHERE nombre_pastel = {0}'.format(nombre_pastel))
    cursor.commit()
    flash('Pastel Removed Successfully')
    cur.close()
    return redirect(url_for('Index2'))


@app.route('/add_ingredients', methods=['POST'])
def add_ingredients():
    if request.method == 'POST':
        cursor = mysql.connect()
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        unidad_medida = request.form['unidad_medida']
        nombre_pastel = request.form['nombre_pastel']
        cur = cursor.cursor()
        cur.execute("INSERT INTO ingrediente (nombre, cantidad, unidad_medida, nombre_pastel) VALUES (%s,%s, %s, %s)", (nombre, cantidad, unidad_medida, nombre_pastel))
        cursor.commit()
        flash('Ingredient Added successfully')
        return redirect(url_for('Index2'))


@app.route('/edit/<nombre>', methods=['POST', 'GET'])
def get_ingredient(nombre):
    cursor = mysql.connect()
    cur = cursor.cursor()
    cur.execute('SELECT * FROM ingrediente WHERE nombre = %s', (nombre))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_ingredients.html', contact=data[0])


@app.route('/update/<nombre>', methods=['POST'])
def update_ingredient(nombre):
    if request.method == 'POST':
        cursor = mysql.connect()
        cur = cursor.cursor()
        cantidad = request.form['cantidad']
        unidad_medida = request.form['unidad_medida']
        nombre_pastel = request.form['nombre_pastel']
        cur.execute("""
            UPDATE ingrediente
            SET cantidad = %s,
                unidad_medida = %s,
                nombre_pastel = %s
            WHERE nombre = %s
        """, (cantidad, unidad_medida, nombre_pastel, nombre))
        flash('Ingredient Updated Successfully')
        cursor.commit()
        cur.close()
        return redirect(url_for('Index2'))


@app.route('/fase_pastel',methods=['GET', 'POST'])
def fase_pastel():
    return render_template('fase_pastel.html')


@app.route('/add_horneado', methods=['POST'])
def add_horneado():
    if request.method == 'POST':
        cursor = mysql.connect()
        id_horneado = request.form['id_horneado']
        temperatura = request.form['temperatura']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        nombre_pastel = request.form['nombre_pastel']
        cur = cursor.cursor()
        cur.execute("INSERT INTO horneado (id_horneado, temperatura_coccion, fecha_inicio, fecha_fin, nombre_pastel) VALUES (%s,%s, %s, %s, %s)", (id_horneado, temperatura, fecha_inicio, fecha_fin, nombre_pastel))
        cursor.commit()
        flash('Horneado Added successfully')
        return redirect(url_for('fase_pastel'))


@app.route('/add_decorado', methods=['POST'])
def add_decorado():
    if request.method == 'POST':
        cursor = mysql.connect()
        id = request.form['id_decorado']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        peso_final = request.form['peso_final']
        nombre_pastel = request.form['nombre_pastel']
        cur = cursor.cursor()
        cur.execute("INSERT INTO decorado (id_decorado, fecha_inicio, fecha_fin, peso_final, nombre_pastel) VALUES (%s,%s, %s, %s, %s)", (id, fecha_inicio, fecha_fin, peso_final, nombre_pastel))
        cursor.commit()
        flash('Decorado Added successfully')
        return redirect(url_for('fase_pastel'))


@app.route('/registro_empleados',methods=['GET', 'POST'])
def registro_empleados():
    return render_template('registro_empleados.html')


@app.route('/add_pastelero', methods=['POST'])
def add_pastelero():
    if request.method == 'POST':
        cursor = mysql.connect()
        cur = cursor.cursor()
        codigo = request.form['codigo']
        nombre = request.form['nombrep']
        salario = request.form['salario']
        numero_pasaporte = request.form['numero_pasaporte']
        pais_origen = request.form['pais_origen']
        experiencia = request.form['experiencia']
        recomendacion = request.form['recomendacion']

        cur.execute("INSERT INTO empleado (codigo,nombre, salario) VALUES(%s,%s,%s)",
                    (codigo, nombre, salario))

        cur.execute("INSERT INTO pastelero (codigo, numero_pasaporte, pais_origen, experiencia,recomendacion) VALUES (%s,%s,%s,%s,%s)",
                      (codigo, numero_pasaporte, pais_origen, experiencia, recomendacion))


        cursor.commit()
        flash('Pastelero Added successfully')
        cur.close()
        return redirect(url_for('registro_empleados'))


@app.route('/add_decorador', methods=['POST'])
def add_decorador():
    if request.method == 'POST':
        cursor = mysql.connect()
        cur = cursor.cursor()
        codigo = request.form['codigo_decorador']
        nombre = request.form['nombre_decorador']
        salario = request.form['salario']

        cur.execute("INSERT INTO empleado (codigo, nombre, salario) VALUES (%s,%s,%s)", (codigo, nombre, salario))
        cursor.commit()
        flash('Decorador Added successfully')
        cur.close()
        return redirect(url_for('registro_empleados'))


@app.route('/add_empresa', methods=['POST'])
def add_empresa():
    if request.method == 'POST':
        cursor = mysql.connect()
        cur = cursor.cursor()
        nombre = request.form['nombre_empresa']
        nit = request.form['nit']
        direccion = request.form['direccion_empresa']

        cur.execute("INSERT INTO empresa (NIT, nombre, direccion) VALUES (%s,%s,%s)",
                      (nit, nombre, direccion))
        cursor.commit()
        flash('Empresa Added successfully')
        cur.close()
        return redirect(url_for('registro_empleados'))


@app.route('/add_persona_externa', methods=['POST'])
def add_persona_externa():
    if request.method == 'POST':
        cursor = mysql.connect()
        cur = cursor.cursor()
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        direccion = request.form['direccion_persona_externa']

        cur.execute("INSERT INTO persona_externa (cedula, nombre, direccion) VALUES (%s,%s,%s)",
                      (cedula, nombre, direccion,))
        cursor.commit()
        flash('Persona_externa Added successfully')
        cur.close()
        return redirect(url_for('registro_empleados'))


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)