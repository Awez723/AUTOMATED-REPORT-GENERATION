import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import *
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

d = pd.read_csv("data.csv")
print(d)
d["total"] = d["Math"] + d["Science"] + d["English"]
d["avg"] = d["total"] / 3

r = []
for i in d["avg"]:
    if i >= 70:
        r.append("Pass")
    else:
        r.append("Fail")
d["result"] = r
plt.bar(d["Name"], d["avg"])
plt.savefig("pic.png")
plt.close()

pdf = SimpleDocTemplate("report.pdf", pagesize=letter)
s = getSampleStyleSheet()
x = []
a = Paragraph("Student Report", s["Title"])
x.append(a)
x.append(Spacer(1,10))
b = Paragraph(
    "Average = " + str(d["avg"].mean()),
    s["BodyText"]
)
x.append(b)
x.append(Spacer(1,10))
t = [list(d.columns)]
for i in d.values:
    t.append(list(i))

table = Table(t)
table.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 1, colors.black),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),("BACKGROUND", (0,0), (-1,0), colors.lightgrey)]))
x.append(table)
x.append(Spacer(1,10))

img = Image("pic.png", width=250, height=150)
x.append(img)
pdf.build(x)
print("Done,PDF Created")