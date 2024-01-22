from flask import Flask,render_template,request



app=Flask(__name__)

list=[]
@app.route("/list",methods=["GET","POST"])

def todo():

    if request.method=="POST":
        
        
        list.append(request.form["item_name"])

    return render_template("list.html",viewlist=list)

@app.route("/detodo/<deletevalue>",methods=["GET","POST"])

def delete(deletevalue):
    if deletevalue in list:
        list.remove(deletevalue)

    return render_template("list.html",viewlist=list)

@app.route("/update/<v_index>",methods=["GET","POST"])

def updatelist(v_index):
    if request.method=="POST":
        list[int(v_index)]=request.form["item_name"]
        return render_template("list.html",viewlist=list)
    else:
     value=list[int(v_index)]
    return render_template("update.html",updatevalue=value)



    


if __name__=="__main__":
    app.run(debug=True)