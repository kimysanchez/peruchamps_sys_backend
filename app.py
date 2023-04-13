from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS


#CONEXIÓN MYSQL
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['MYSQL_HOST'] = '192.185.45.198'
app.config['MYSQL_USER'] = 'champs17_sys'
app.config['MYSQL_PASSWORD'] = 'nG=;$0p8bwdr'
app.config['MYSQL_DB'] = 'champs17_sys'
mysql = MySQL(app)




#APIS
@app.route('/listarChamps', methods=['GET'])
def listarChamps():
    try:
        sql = "SELECT * FROM champ"
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()

        champs = []
        for dato in datos:
            champ = {
                'idChamp': dato[0],
                'dni': dato[1],
                'nombres': dato[2],
                'apellidos': dato[3],
                'sexo': dato[4],
                'grado': dato[5],
                'sede': dato[6],
                'estado': dato[7],
                'riesgoEmocional': dato[8],
                'riesgoAcademico': dato[9],
                'correo1': dato[10],
                'correo2': dato[11],
                'celular1': dato[12],
                'celular2': dato[13],
                'nacimiento': dato[14],
                'edad': dato[15],
                'region': dato[16],
                'origen': dato[17],
                'ingreso': dato[18],
                'cantera': dato[19],
                'nombreCantera': dato[20],
                'nombreEmpresa': dato[21],
                'donante': dato[22],
                'dniPapa': dato[23],
                'nombrePapa': dato[24],
                'dniMama': dato[25],
                'nombreMama': dato[26],
                'descripcionCaso': dato[27],
                'protocolo': dato[28],
                'nivelRiesgo': dato[29],
                'psicologo': dato[30]
            }
            champs.append(champ)

        response = jsonify({
            "champs": champs,
            "status": 200
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
    except Exception as ex:
        response = jsonify({
            "champs": "Error",
            "status": 400,
            "error": ex.args
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/listarIntervenciones/<idChamp>', methods=['GET'])
def listarIntervenciones(idChamp):
    try:
        sql = "SELECT * FROM intervencion WHERE idChamp='{0}'".format(idChamp)
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()

        intervenciones = []
        for dato in datos:
            intervencion = {
                'idIntervencion': dato[0],
                'fecha': dato[1],
                'motivo1': dato[2],
                'motivo2': dato[3],
                'informacion': dato[4],
                'acuerdo': dato[5],
                'psicologo': dato[7]
            }
            intervenciones.append(intervencion)

        response = jsonify({
            "champ": idChamp,
            "intervenciones": intervenciones,
            "status": 200
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        response = jsonify({
            "champ": idChamp,
            "intervenciones": "Error",
            "status": 400,
            "error": ex.args
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/listarChamps/<psicologo>', methods=['GET'])
def listarChampsPsicologo(psicologo):
    try:
        sql = "SELECT * FROM champ WHERE psicologo='{0}'".format(psicologo)
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()

        champs = []
        for dato in datos:
            champ = {
                'idChamp': dato[0],
                'dni': dato[1],
                'nombres': dato[2],
                'apellidos': dato[3],
                'sexo': dato[4],
                'grado': dato[5],
                'sede': dato[6],
                'estado': dato[7],
                'riesgoEmocional': dato[8],
                'riesgoAcademico': dato[9],
                'correo1': dato[10],
                'correo2': dato[11],
                'celular1': dato[12],
                'celular2': dato[13],
                'nacimiento': dato[14],
                'edad': dato[15],
                'region': dato[16],
                'origen': dato[17],
                'ingreso': dato[18],
                'cantera': dato[19],
                'nombreCantera': dato[20],
                'nombreEmpresa': dato[21],
                'donante': dato[22],
                'dniPapa': dato[23],
                'nombrePapa': dato[24],
                'dniMama': dato[25],
                'nombreMama': dato[26],
                'descripcionCaso': dato[27],
                'protocolo': dato[28],
                'nivelRiesgo': dato[29],
                'psicologo': dato[30]
            }
            champs.append(champ)

        response = jsonify({
            "champs": champs,
            "status": 200
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        response = jsonify({
            "champs": "Error",
            "status": 400,
            "error": ex.args
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/insertarChamp', methods=['POST'])
def insertarChamp():
    try:
        sql = "INSERT INTO champ (idChamp, dni, nombres, apellidos, sexo, grado, sede, estado, riesgoEmocional, riesgoAcademico, correo1, correo2, celular1, celular2, nacimiento, edad, region, origen, ingreso, cantera, nombreCantera, nombreEmpresa, donante, dniPapa, nombrePapa, dniMama, nombreMama, descripcionCaso, protocolo, nivelRiesgo, psicologo) VALUES (NULL, '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', {11}, {12}, '{13}', {14}, '{15}', '{16}', {17}, '{18}', '{19}', '{20}', '{21}', '{22}', '{23}', '{24}', '{25}', '{26}', '{27}', '{28}', '{29}');".format(request.json['dni'], request.json['nombres'], request.json['apellidos'], request.json['sexo'], request.json['grado'], request.json['sede'], request.json['estado'], request.json['riesgoEmocional'], request.json['riesgoAcademico'], request.json['correo1'], request.json['correo2'], request.json['celular1'], request.json['celular2'], request.json['nacimiento'], request.json['edad'], request.json['region'], request.json['origen'], request.json['ingreso'], request.json['cantera'], request.json['nombreCantera'], request.json['nombreEmpresa'], request.json['donante'], request.json['dniPapa'], request.json['nombrePapa'], request.json['dniMama'], request.json['nombreMama'], request.json['descripcionCaso'], request.json['protocolo'], request.json['nivelRiesgo'], request.json['psicologo'])
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        mysql.connection.commit()
        response = jsonify({
            "champ": request.json,
            "status": 200
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        response = jsonify({
            "champ": request.json,
            "status": 400,
            "error": ex.args
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/insertarIntervencion/<idChamp>', methods=['POST'])
def insertarIntervencion(idChamp):
    try:
        sql = "INSERT INTO intervencion (idIntervencion, fecha, motivo1, motivo2, informacion, acuerdo, idChamp, psicologo) VALUES (NULL, '{0}', '{1}', '{2}', '{3}', '{4}', {5}, '{6}');".format(request.json['fecha'], request.json['motivo1'], request.json['motivo2'], request.json['informacion'], request.json['acuerdo'], idChamp, request.json['psicologo'])
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        mysql.connection.commit()
        response = jsonify({
            "champ": idChamp,
            "intervencion": request.json,
            "status": 200
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        response = jsonify({
            "champ": idChamp,
            "intervencion": request.json,
            "status": 400,
            "error": ex
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response




@app.route('/eliminarIntervencion/<idIntervencion>', methods=['DELETE'])
def eliminarIntervencion(idIntervencion):
    try:
        sql = "DELETE FROM intervencion WHERE idIntervencion={0}".format(idIntervencion)
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        mysql.connection.commit()
        response = jsonify({
            "intervencion": idIntervencion,
            "mensaje": "Intervención eliminada",
            "status": 200
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        response = jsonify({
            "intervencion": idIntervencion,
            "mensaje": "Error",
            "status": 400,
            "error": ex.args
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response



@app.route('/editarIntervencion/<idIntervencion>', methods=['PUT'])
def editarIntervencion(idIntervencion):
    try:
        sql = "UPDATE intervencion SET fecha = '{0}', motivo1 = '{1}', motivo2 = '{2}', informacion = '{3}', acuerdo = '{4}', psicologo = '{5}' WHERE idIntervencion = '{6}'".format(request.json['fecha'], request.json['motivo1'], request.json['motivo2'], request.json['informacion'], request.json['acuerdo'], request.json['psicologo'], idIntervencion)
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        mysql.connection.commit()
        response = jsonify({
            "intervencion": idIntervencion,
            "mensaje": "Intervención editada",
            "status": 200
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        response = jsonify({
            "intervencion": idIntervencion,
            "mensaje": "Error",
            "status": 400,
            "error": ex.args
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


def pagina_no_encontrada(error):
    return "<h1>Esta página no existe</h1>"


if __name__ == "__main__":
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True)
