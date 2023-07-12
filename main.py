from flask import render_template, request, flash, redirect,Flask
import detcalc

app = Flask(__name__)
app.secret_key = "Matrix"
mat = {}
ipt = []


@app.route("/", methods=["GET", "POST"])
def home():
    name = request.form.get("name")
    if request.method == "POST":
        if len(name) < 3:
            flash("Name must be atleast 3 characters", category="error")
        else:
            return redirect("/matrix")
    return render_template("index.html")


@app.route("/matrix", methods=["GET", "POST"])
def matrix():
    mat = request.form.get("grid")
    if mat == "2x2":
        return redirect("/grid-2")
    elif mat == "3x3":
        return redirect("/grid-3")
    return render_template("matrix.html")


@app.route("/grid-2", methods=["GET", "POST"])
def grid2():
    for i in range(1, 3):
        for j in range(1, 3):
            mat[f"A{i}{j}"] = request.form.get(f"A{i}{j}")
    for x in range(len(list(mat.values()))):
        if list(mat.values())[x] == None:
            ipt.append(float(0.0))
        elif list(mat.values())[x] != None:
            if list(mat.values())[x] == "":
                ipt[x] = float(0.0)
            else:
                ipt[x] = float(list(mat.values())[x])
    dets = detcalc.mat2(ipt).det
    inv = detcalc.mat2(ipt).inverse
    min = detcalc.mat2(ipt).minors
    cof = detcalc.mat2(ipt).cofactors
    return render_template("grid-2.html", dets=dets, inv=inv, cof=cof, min=min)


@app.route("/grid-3", methods=["GET", "POST"])
def grid3():
    for i in range(1, 4):
        for j in range(1, 4):
            mat[f"A{i}{j}"] = request.form.get(f"A{i}{j}")
    for x in range(len(list(mat.values()))):
        if list(mat.values())[x] == None:
            ipt.append(float(0.0))
        elif list(mat.values())[x] != None:
            if list(mat.values())[x] == "":
                ipt[x] = float(0.0)
            else:
                ipt[x] = float(list(mat.values())[x])
    dets = detcalc.mat3(ipt).det
    inv = detcalc.mat3(ipt).inverse
    min = detcalc.mat3(ipt).minors
    cof = detcalc.mat3(ipt).cofactors

    return render_template("grid-3.html", dets=dets, cof=cof, inv=inv, min=min)

if __name__ == "__main__":
    app.run(debug= True)

    