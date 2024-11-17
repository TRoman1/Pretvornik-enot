# ***********************************************************************
# Ime programa: main.py (pretvornik enot)                               *
# Datum: 17. 11. 2024                                                   *
# Verzija: 1.0                                                          *
# Avtor: Roman Tušek                                                    *
# Opis: gre za pretvornik enot. V datoteki index.html se nahaja forma   *
#       z vnosnim poljem INPUT in izbirnikom SELECT za vrsto pretvorbe. *
#       Oblikovanje (CSS datoteka) se nahaja v mapi /static.            *
#       V programu main.py se nahaja samo en kontroler, ki preko metode *
#       POST pobere, na strani index.html, vnešeno vrednost in vrsto    *
#       pretvorbe, opravi izračun in vrne rezultat "result", ki se      *
#       izpiše na strani index.html.                                    * 
# ***********************************************************************

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        value = request.form.get('value')
        unit = request.form.get('unit')

        try:
            value = float(value)
            if unit == 'km-to-miles':
                result = f"{(value):.2f} km je {(value * 0.621371):.2f} milje"
            elif unit == 'miles-to-km':
                result = f"{(value):.2f} milj je {(value * 1.60934):.2f} kilometrov"
        except ValueError:
            result = "Prosimo, vnesite veljavno številko."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()

