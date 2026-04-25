from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

menu = [
    {"id":1,"name":"Pancake","price":180,"image":"https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?auto=format&fit=crop&w=600&q=80"},
    {"id":2,"name":"Omelette","price":120,"image":"https://images.unsplash.com/photo-1551218808-94e220e084d2?auto=format&fit=crop&w=600&q=80"},
    {"id":3,"name":"Pasta","price":220,"image":"https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=600&q=80"},
    {"id":4,"name":"Burger","price":180,"image":"https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=600&q=80"},
    {"id":5,"name":"Fried Rice","price":200,"image":"https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=600&q=80"},
    {"id":6,"name":"French Fries","price":90,"image":"https://images.unsplash.com/photo-1576107232684-1279f390859f?auto=format&fit=crop&w=600&q=80"},
    {"id":7,"name":"Shake","price":110,"image":"https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=600&q=80"}
]

@app.route("/")
def home():
    return render_template("index.html", menu=menu)

@app.route("/item/<int:id>")
def item(id):
    food = next(x for x in menu if x["id"] == id)
    return render_template("detail.html", item=food)

@app.route("/add/<int:id>")
def add_to_cart(id):
    cart = session.get("cart", [])
    cart.append(id)
    session["cart"] = cart
    return redirect("/cart")

@app.route("/cart")
def cart():
    cart_ids = session.get("cart", [])
    items = [x for x in menu if x["id"] in cart_ids]
    total = sum(x["price"] for x in items)
    return render_template("cart.html", items=items, total=total)

@app.route("/address", methods=["GET","POST"])
def address():
    if request.method == "POST":
        session["address"] = request.form["addr"]
        return redirect("/payment")
    return render_template("address.html")

@app.route("/payment", methods=["GET","POST"])
def payment():
    if request.method == "POST":
        session.pop("cart", None)
        return "<h2>✅ Order Placed Successfully!</h2>"
    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True)