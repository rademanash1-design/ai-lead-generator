from flask import Flask, render_template, request, send_file
import random
import csv

app = Flask(__name__)

last_result = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global last_result
    result = ""

    if request.method == "POST":
        business = request.form.get("business", "")
        audience = request.form.get("audience", "")

        areas = [
            "Facebook groups",
            "Google Maps listings",
            "Property websites",
            "Local WhatsApp groups",
            "Community forums"
        ]

        lead_types = [
            "Suburban homeowners",
            "Rental property owners",
            "Airbnb hosts",
            "Estate managers",
            "Small business owners"
        ]

        reasons = [
            "likely need regular maintenance",
            "recently moved into the area",
            "manage multiple properties",
            "want reliable service providers",
            "value property upkeep"
        ]

        leads = []

        for i in range(5):
            leads.append(
                f"{i+1}. {random.choice(lead_types)}\n"
                f"   📍 Where: {random.choice(areas)} in {audience}\n"
                f"   💡 Why: {random.choice(reasons)}\n"
            )

        result = f"""
🔥 HIGH-QUALITY LOCAL LEADS

{''.join(leads)}

---

📩 OUTREACH MESSAGE:
Hi, I offer reliable {business} in {audience}. Would you like a quick quote?

---

🔁 FOLLOW-UP:
Just checking in — still interested in improving your {business}?
"""

        last_result = result

    return render_template("index.html", result=result)


@app.route("/download")
def download():
    global last_result

    filename = "leads.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Lead Data"])
        writer.writerow([last_result])

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)