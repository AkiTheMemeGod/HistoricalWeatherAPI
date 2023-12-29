from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def result(station, date):
    df = pd.read_csv(filepath_or_buffer=f"data_small/TG_STAID{str(station).zfill(6)}.txt",
                     skiprows=20,
                     parse_dates=['    DATE'])

    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    response = {
        "station": station,
        "date": date,
        "temperature": str(temp)
    }
    return response


if __name__ == '__main__':
    app.run(debug=True)
