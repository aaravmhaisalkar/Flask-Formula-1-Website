from flask import Flask, request, render_template
from Formula1_API import getFinalStandings
app = Flask(__name__)
locations = [
    "",
    "Melbourne 🇦🇺",
    "Shanghai 🇨🇳",
    "Suzuka 🇯🇵",
    "Sakhir 🇧🇭",
    "Jeddah 🇸🇦",
    "Miami 🇺🇸",
    "Imola 🇮🇹",
    "Monte Carlo 🇲🇨",
    "Catalunya 🇪🇸",
    "Montreal 🇨🇦",
    "Spielberg 🇦🇹",
    "Silverstone 🇬🇧",
    "Spa-Francorchamps 🇧🇪",
    "Hungaroring 🇭🇺",
    "Zandvoort 🇳🇱",
    "Monza 🇮🇹",
    "Baku 🇦🇿",
    "Singapore 🇸🇬",
    "Austin 🇺🇸",
    "Mexico City 🇲🇽",
    "Interlagos 🇧🇷",
    "Las Vegas 🇺🇸",
    "Lusail 🇶🇦",
    "Yas Marina Circuit 🇦🇪"
]


@app.route("/", methods=["GET"]) 
def dropdown():
    return render_template('main.html', locations=locations)

@app.route("/submit", methods=["POST"]) 
def submit():
    if request.method == "POST":
        track = request.form.get('dropdown', type=str)
        if track not in locations:
            return "Invalid Track", 400
        elif track == "":
            return "<h1>Please pick a track, do not leave it blank.</h1>"
        track = track[:-3]
        standings = getFinalStandings(track)
        return render_template('table.html',locations=locations, standings=standings, track=track)

if __name__ == "__main__": 
    app.run(debug=True) 