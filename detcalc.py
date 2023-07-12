import numpy as np
Cofactors = {}
inpt = []
npinpt = []
Minors = {}

class mat2():
    def __init__(self,inpt):
        npinpt = np.array(inpt[len(inpt)-4:len(inpt)+1]).reshape(2,2)
        self.det = np.linalg.det(npinpt)
        Minors = {"M11":npinpt[1][1],"M12":npinpt[1][0],"M21":npinpt[0][1],"M22":npinpt[0][0]}
        for i in range(1,3):
            for j in range(1,3):
                if (i+j) % 2 == 0:
                    Cofactors["C"+str(i)+str(j)] = (Minors[f"M{i}{j}"])
                else:
                    Cofactors["C"+str(i)+str(j)] = (Minors[f"M{i}{j}"] * -1)
        self.minors = np.array(list(Minors.values())).reshape(2,2)
        self.cofactors = np.array(list(Cofactors.values())).reshape(2,2)
        print(Cofactors.values())
        if self.det == 0:
            self.inverse = "Inverse doesnt exist as Determinant is 0"
        else:
            self.inverse = np.around(np.multiply(np.linalg.inv(npinpt),np.linalg.det(npinpt)),2)
        self.det = "%.2f" % np.linalg.det(npinpt)
        print(npinpt)
class mat3():
    def __init__(self,inpt):
        npinpt = np.array(inpt[len(inpt)-9:len(inpt)+1]).reshape(3,3)
        Minors = {"M11":((npinpt[1][1]*npinpt[2][2])-(npinpt[1][2]*npinpt[2][1])),"M12":((npinpt[1][0]*npinpt[2][2])-(npinpt[1][2]*npinpt[2][0])),"M13":((npinpt[1][0]*npinpt[2][1])-(npinpt[1][1]*npinpt[2][0])),"M21":((npinpt[0][1]*npinpt[2][2])-(npinpt[0][2]*npinpt[2][1])),"M22":((npinpt[0][0]*npinpt[2][2])-(npinpt[0][2]*npinpt[2][0])),"M23":((npinpt[0][0]*npinpt[2][1])-(npinpt[0][1]*npinpt[2][0])),"M31":((npinpt[0][1]*npinpt[1][2])-(npinpt[0][2]*npinpt[1][1])),"M32":((npinpt[0][0]*npinpt[1][2])-(npinpt[0][2]*npinpt[1][0])),"M33":((npinpt[0][0]*npinpt[1][1])-(npinpt[0][1]*npinpt[1][0]))}
        self.det = np.linalg.det(npinpt)
        for i in range(1,4):
            for j in range(1,4):
                if (i+j) % 2 == 0:
                    Cofactors["C"+str(i)+str(j)] = (Minors[f"M{i}{j}"])
                else:
                    Cofactors["C"+str(i)+str(j)] = (Minors[f"M{i}{j}"] * -1)
        self.minors = np.array(list(Minors.values())).reshape(3,3)
        self.cofactors = np.array(list(Cofactors.values())).reshape(3,3)
        if np.linalg.det(npinpt) == 0:
            self.inverse = "Inverse doesnt exist as Determinant is 0"
        else:
            self.inverse = np.around(np.multiply(np.linalg.inv(npinpt),np.linalg.det(npinpt)),2)
        self.det = "%.2f" % np.linalg.det(npinpt)




