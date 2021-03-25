from flask import Flask, render_template, request, redirect, url_for, flash




app = Flask(__name__)

data = [    ["1", "Bon N°1",156,"25/01/21","done"],
            ["2", "Bon N°2",234,"23/02/21","clear"],
            ["3", "Bon N°3",176,"27/03/21","hourglass_empty"],
            ["4", "bon N°4",517,"28/04/21","done"],
            ["5", "Bon N°5",363,"26/05/21","clear"],
            ["6", "Bon N°6", 156, "25/06/21", "hourglass_empty"],
            ["7", "Bon N°7", 234, "23/07/21", "hourglass_empty"],
            ["8", "Bon N°8", 76, "27/08/21", "clear"],
            ["9", "Bon N°9", 517, "28/09/21", "hourglass_empty"],
            ["10", "Bon N°10", 133, "24/10/21", "clear"],
            ["11", "Bon N°11", 159, "25/11/21", "clear"],
            ["12", "Bon N°12", 239, "23/08/21", "done"],
            ["13", "Bon N°13", 199, "27/01/21", "hourglass_empty"],
            ["14", "Bon N°14", 317, "28/10/21", "hourglass_empty"],
            ["15", "Bon N°15", 363, "26/02/21", "clear"],
            ["16", "Bon N°16", 196, "25/01/21", "done"],
            ["17", "Bon N°17", 214, "23/10/21", "done"],
            ["18", "Bon N°18", 706, "27/03/21", "done"],
            ["19", "bon N°19", 497, "28/04/21", "clear"],
            ["20", "Bon N°20", 173, "26/05/21", "done"],
            ["21", "Bon N°21", 186, "25/04/21", "hourglass_empty"],
            ["22", "Bon N°22", 244, "23/07/21", "done"],
            ["23", "Bon N°23", 464, "27/03/21", "clear"],
            ["24", "Bon N°24", 177, "28/09/21", "done"],
            ["25", "Bon N°25", 155, "24/06/21", "clear"],
            ["26", "Bon N°26", 178, "25/11/21", "done"],
            ["27", "Bon N°27", 278, "23/12/21", "hourglass_empty"],
            ["28", "Bon N°28", 461, "27/12/21", "clear"],
            ["29", "Bon N°29", 107, "28/12/21", "done"],
            ["30", "Bon N°30", 133, "26/12/21", "clear"],
            ["31", "Bon N°31",106,"02/01/21","done"],
            ["32", "Bon N°32",274,"03/02/21","hourglass_empty"],
            ["33", "Bon N°33",160,"07/08/21","hourglass_empty"],
            ["34", "bon N°34",117,"08/12/21","done"],
            ["35", "Bon N°35",163,"06/05/21","hourglass_empty"],
            ["36", "Bon N°36", 176, "05/06/21", "done"],
            ["37", "Bon N°37", 274, "03/07/21", "clear"],
            ["38", "Bon N°38", 706, "07/08/21", "clear"],
            ["39", "Bon N°39", 207, "08/09/21", "clear"],
            ["40", "Bon N°40", 333, "04/12/21", "hourglass_empty"],
            ["41", "Bon N°41", 506, "05/11/21", "hourglass_empty"],
            ["42", "Bon N°42", 174, "03/12/21", "clear"],
            ["43", "Bon N°43", 251, "17/01/21", "clear"],
            ["44", "Bon N°44", 317, "18/02/21", "done"],
            ["45", "Bon N°45", 133, "16/02/21", "hourglass_empty"]]
gestion = [
            [["Oumar Niang","date"],["Moussa Deme","date"]],
            [["Moussa Deme","date"]],
            [["Thierno Diakhaby","16/02/21"],["Moussa Deme","date"],["Oumar Niang","date"],["Daouda Kane","16/02/21"]],
            [["Thierno Diakhaby","16/02/21"]],
            [["Oumar Niang","date"],["Moussa Deme","date"]],
            [["Thierno Diakhaby","16/02/21"]],
            [["Daouda Kane","16/02/21"]],
            [["Thierno Diakhaby","16/02/21"],["Moussa Deme","date"],["Daouda Kane","16/02/21"]],
            [["Oumar Niang", "16/02/21"]],
            [["Thierno Diakhaby","16/02/21"],["Moussa Deme","date"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Daouda Kane","16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Moussa Deme", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Moussa Deme", "16/02/21"]],
            [["Thierno Diakhaby","16/02/21"],["Moussa Deme","date"]],
            [["Moussa Deme", "16/02/21"]],
            [["Thierno Diakhaby","16/02/21"],["Moussa Deme","date"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Moussa Deme", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Oumar Niang", "16/02/21"]],
            [["Oumar Niang", "16/02/21"]],
            [["Thierno Diakhaby","16/02/21"],["Moussa Deme","date"],["Daouda Kane","16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Oumar Niang", "16/02/21"],["Daouda Kane","16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Oumar Niang", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Thierno Diakhaby", "16/02/21"]],
            [["Daouda Kane", "16/02/21"]],
            [["Oumar Niang", "16/02/21"]],
            [["Moussa Deme", "16/02/21"]]
            ]
budget = [     [["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Thierno Diakhaby","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Amadou Barry","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]],[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Amadou Barry","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Moussa Deme","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Moussa Deme","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Moussa Deme","14/03/2021"]]
             ,[["Moussa Deme","25/09/2021"],["Moussa Deme","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Oumar Niang","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Thierno Diakhaby","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Oumar Niang","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Thierno Diakhaby","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Thierno Diakhaby","14/03/2021"]]
              ]
achat = [     [["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[]
             ,[]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[]
             ,[]
             ,[]
             ,[]
             ,[]
             ,[]
             ,[["Daouda Kane","16/02/21"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]],[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Daouda Kane","16/02/21"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Amadou Barry","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Moussa Deme","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Moussa Deme","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Moussa Deme","14/03/2021"]]
             ,[["Moussa Deme","25/09/2021"],["Moussa Deme","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Daouda Kane","16/02/21"]]
             ,[["Daouda Kane","16/02/21"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Oumar Niang","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Amadou Barry","14/03/2021"]]
             ,[["Thierno Diakhaby","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Oumar Niang","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Thierno Diakhaby","14/03/2021"]]
             ,[["Oumar Niang","25/09/2021"],["Thierno Diakhaby","12/03/2021"]]
             ,[["Moussa Deme","13/03/2021"]]
             ,[["Daouda Kane","16/02/21"]]
              ]

@app.route('/')
def home():
    len_gestion = []
    for gest in gestion:
        len_gestion.append(int(len(gest)));
    len_budget = []
    for budg in budget:
        len_budget.append(int(len(budg)));
    len_achat = []
    for ach in achat:
        len_achat.append(int(len(ach)));
    return render_template('index.html',titre='workflow',tab=data, len=len(data),gestion = gestion,lenGestion = len_gestion,budget = budget,lenBudget = len_budget,achat = achat, lenAchat = len_achat)

@app.route("/test", methods=['POST','GET'])
def test():

    return render_template("test.html")
@app.route("/graphique", methods=['POST','GET'])
def graphique():
    date = []
    for donnee in data:
        date.append(int(donnee[3][3:5]))
    moi = [0] * 12
    for a in date:
        for i in range(0, 12):
            if a == i + 1:
                moi[i] += 1

    Tab_gestion = [0] * 4
    for gest in gestion:
        for g in gest:
            if g[0] == "Thierno Diakhaby":
                Tab_gestion[0] += 1
            elif g[0] == "Moussa Deme":
                Tab_gestion[1] += 1
            elif g[0] == "Oumar Niang":
                Tab_gestion[2] += 1
            elif g[0] == "Daouda Kane":
                Tab_gestion[3] += 1
    Tab_budget = [0] * 4
    for budg in budget:
        for b in budg:
            if b[0] == "Thierno Diakhaby":
                Tab_budget[0] += 1
            elif b[0] == "Moussa Deme":
                Tab_budget[1] += 1
            elif b[0] == "Oumar Niang":
                Tab_budget[2] += 1
            elif b[0] == "Amadou Barry":
                Tab_budget[3] += 1
    Tab_achat = [0] * 5
    for ach in achat:
        for a in ach:
            if a[0] == "Thierno Diakhaby":
                Tab_achat[0] += 1
            elif a[0] == "Moussa Deme":
                Tab_achat[1] += 1
            elif a[0] == "Oumar Niang":
                Tab_achat[2] += 1
            elif a[0] == "Amadou Barry":
                Tab_achat[3] += 1
            elif a[0] == "Daouda Kane":
                Tab_achat[4] += 1
    Tab_done = [0]*12
    Tab_clear = [0]*12
    Tab_empty = [0]*12
    for donnee in data:
        if donnee[4] == "done":
            Tab_done[int(donnee[3][3:5])-1] += int(donnee[2])
        elif donnee[4] == "clear":
            Tab_clear[int(donnee[3][3:5])-1] += int(donnee[2])
        elif donnee[4] == "hourglass_empty":
            Tab_empty[int(donnee[3][3:5])-1] += int(donnee[2])
    return render_template("index2.html",nbr_moi = moi,Tab_gestion = Tab_gestion,Tab_budget = Tab_budget,Tab_achat = Tab_achat,Tab_done = Tab_done,Tab_clear = Tab_clear,Tab_empty = Tab_empty)
if __name__ == "__main__":
    app.run(host='127.0.0.2', port=8005, debug=True)
