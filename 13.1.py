from flask import Flask, request
import json


def onkoalkuluku(luku1):
    while True:
        for i in range(2, luku1):
            luku = luku1 % i
            if luku == 0:
                return False
        else:
            return True


app = Flask(__name__)
@app.route('/alkuluku/<luku1>')
def alkuluku(luku1):
    try:
        luku1 = int(luku1)
        vastaus1 = onkoalkuluku(luku1)

        tilakoodi = 200
        vastaus = {
            "Number": luku1,
            "isPrime": vastaus1
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
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)