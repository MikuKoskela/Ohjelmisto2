from flask import Flask, request
import json
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='S4l4_sana',
         autocommit=True)
def haku(icao):
    sql = 'select gps_code,name from airport where gps_code = "'+ icao +'"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    response = kursori.fetchall()
    return(response)

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    try:
        icao = str(icao)
        vastaus1 = haku(icao)

        tilakoodi = 200
        vastaus = {
            "ICAO": icao,
            "Name": vastaus1,
            "Municipality": "Helsinki"
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)