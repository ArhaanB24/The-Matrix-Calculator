from flask import Blueprint, render_template, request, flash, redirect 
from website import detcalc
views = Blueprint("views",__name__)
mat = {}
ipt = []

@views.route("/",methods=["GET","POST"])
def home():
    data = request.form
    name = request.form.get("name")
    if request.method == "POST":
        if len(name)< 4:
            flash("Name must be atleast 3 characters",category="error")
        else:
            return redirect("/matrix")
    return render_template("index.html")

@views.route("/matrix",methods=["GET","POST"])
def matrix():
    mat = request.form.get("grid")
    if mat == "2x2":
        return redirect("/grid-2")
    elif mat == "3x3":
        return redirect("/grid-3")        
    return render_template("matrix.html")

@views.route("/grid-2",methods=["GET","POST"])
def grid2():
    for i in range(1,3):
            for j in range(1,3):
                mat[f"A{i}{j}"]=request.form.get(f"A{i}{j}")
    for x in  range(len(list(mat.values()))):
        if list(mat.values())[x] == None:
            ipt.append(float(0.0))
        elif list(mat.values())[x] != None:
            if list(mat.values())[x] == '':
                ipt[x] = (float(0.0))
            else:
                ipt[x] = float(list(mat.values())[x])
    dets = detcalc.mat2(ipt).det
    inv = detcalc.mat2(ipt).inverse
    min = detcalc.mat2(ipt).minors
    cof = detcalc.mat2(ipt).cofactors
    return render_template("grid-2.html",dets = dets,inv=inv,cof=cof,min = min)

@views.route("/grid-3",methods=["GET","POST"])
def grid3():
    for i in range(1,4):
            for j in range(1,4):
                mat[f"A{i}{j}"]=request.form.get(f"A{i}{j}")
    for x in  range(len(list(mat.values()))):
        if list(mat.values())[x] == None:
            ipt.append(float(0.0))
        elif list(mat.values())[x] != None:
            if list(mat.values())[x] == '':
                ipt[x] = (float(0.0))
            else:
                ipt[x] = float(list(mat.values())[x])
    dets = detcalc.mat3(ipt).det
    inv = detcalc.mat3(ipt).inverse
    min = detcalc.mat3(ipt).minors
    cof = detcalc.mat3(ipt).cofactors
        
    return render_template("grid-3.html",dets = dets,cof=cof,inv=inv,min=min)


