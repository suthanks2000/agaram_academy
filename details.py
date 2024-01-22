from flask import Flask,render_template,request
app=Flask(__name__)
books=[
        {"id":1,"title":"book 1","author":"Author 1"},
        {"id":2,"title":"book 2","author":"Author 2"},
        {"id":3,"title":"book 3","author":"Author 3"}

      ]
#get all books
@app.route("/books")
def books_name():
    return books


#get a specfic book by id 
@app.route("/books/<int:book_id>")
def get_books(book_id):
    for book in books:
        if book ["id"]==book_id:
            return book
    return{"error":"book not found"}

# create a book 
@app.route("/create",methods=["GET","POST"])
def todo():
    if request.method=="POST":
        new_book={"id":len(books)+1,
                "title":request.form["title_name"],
                "author":request.form["author_name"]
                }
        books.append(new_book)
        return books
    
    else:
        return render_template("details.html")

#remove the book 
@app.route("/delete/<int:id_no>")
def delete(id_no):
    for book in books:
        if book["id"]==id_no:
            books.remove(book)
            return books
        else:
            {"invaild index"}

# update specfic book
@app.route("/update/<update_book>",methods=["GET","POST"])
def update(update_book):
    if request.method=="POST":
        up_data={"id":int(request.form["id_name"]),
                 "title":request.form["title_name"],
                 "author":request.form["author_name"]}
        books[int(update_book)]=up_data
        return books
    else:
        value=books[int(update_book)]
        return render_template("update_book.html",value=value)
