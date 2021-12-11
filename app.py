from flask import Flask,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

# Configuracion de la base de datos

app.config['MYSQL_HOST']='btp2x2yfvgcrum10qncp-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='ugoaz5dsxhyp2x0s'
app.config['MYSQL_PASSWORD']='NTSBJMZc1OYKkyTU0fVt'
app.config['MYSQL_BD']='btp2x2yfvgcrum10qncp'
app.config['MYSQL_PORT']=3306

mysql=MySQL(app)

cors=CORS(app,resource={r"/*":{"origin":"*"}})

@app.route('/')
def getCharacters():
    
    lista=requests.get('https://chavo.s3.us-east-2.amazonaws.com/characters.json')
    
    return jsonify(lista.json())


@app.route('/character/<int:id>')
def getCharacterId(id):
    lista=requests.get('https://chavo.s3.us-east-2.amazonaws.com/characters.json')
    
    
    for element in lista.json():
        if(id==element["id"]):
            insertCharacter(element)
            return jsonify({"message":" Dato se guardo correctamente"})
        else:
            jsonify({"message":"usuario no encontrado"})

def insertCharacter(character):
    nombrePersonaje=character['name']
    categoriaPersonaje=character['category']
    frase=character['quote']
    url=character['URL']
    cur=mysql.connection.cursor()
    cur.execute(f"INSERT INTO personajes(name, category, quote, url) VALUES('{nombrePersonaje}','{categoriaPersonaje}','{frase}','{url}')")
    mysql.connection.commit()
    cur.close()
    return jsonify({"message":"Personaje creado correctamente"})


if __name__=='__main__':
    app.run(debug=True)