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
🔥 LOCAL LEAD STRATEGY REPORT

Here are the best places to find potential customers for your {business} in {audience}:

1. Facebook Community Groups
   📍 Search for local homeowner groups in {audience}
   💡 Post service offers & before/after results

2. Google Maps Businesses
   📍 Search: "property services near {audience}"
   💡 Contact businesses with outdated listings or poor reviews

3. Local WhatsApp & Community Boards
   📍 Ask for referrals in neighbourhood groups
   💡 High trust conversion source

4. Property & Rental Listings
   📍 Airbnb & rental platforms in {audience}
   💡 Target property managers directly

5. Estate Agencies
   📍 Contact local real estate agents
   💡 They constantly need maintenance partners

---

📩 OUTREACH MESSAGE:
Hi, I provide reliable {business} in {audience}. I help property owners keep everything maintained and stress-free. Would you be open to a quick quote?

---

🔁 FOLLOW-UP:
Just checking in — would you still like help with your {business} in {audience}?
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