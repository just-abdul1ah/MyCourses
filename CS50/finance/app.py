import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session.get("user_id")
    symbol_list = db.execute("SELECT DISTINCT(symbol) FROM stocks WHERE user_id=?", user_id)
    balance = db.execute("SELECT cash FROM users WHERE id=?", user_id)
    grand_total_stocks = 0
    stock_list = []
    for symbol in symbol_list:
        stock = lookup(symbol["symbol"])
        total_amount = db.execute("SELECT amount FROM stocks WHERE user_id=? AND symbol=?", user_id, stock['symbol'])[0]['amount']
        stock['amount'] = total_amount
        stock['total_price'] = stock['price'] * total_amount
        stock['price'] = usd(stock['price'])
        grand_total_stocks += stock['total_price']
        stock['total_price'] = usd(stock['total_price'])
        stock_list.append(stock)

    grand_total = grand_total_stocks + balance[0]["cash"]

    return render_template("index.html", stock_list=stock_list, balance=usd(balance[0]["cash"]), grand_total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    action = "Buy"

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Enter a valid number!")

        if not symbol or not shares:
            return apology("Please enter symbol and number of shares!")

        if shares <= 0:
            return apology("Number of shares can't be negative or zero!")

        share = lookup(symbol)
        if share == None:
            return apology("Symbol does not exist!")

        price = share["price"] * int(shares)

        cash = (db.execute("SELECT cash FROM users WHERE id=?", session.get("user_id")))[0]["cash"]
        if price > cash:
            return apology("Sorry, you don't have enough money!")

        remainder = cash - price
        date = datetime.datetime.now()

        user_id = session.get("user_id")

        if db.execute("SELECT symbol FROM stocks WHERE user_id=? AND symbol=?", user_id, symbol) != []:
            db.execute("UPDATE stocks SET amount=amount+? WHERE symbol=? AND user_id=?", shares, symbol, user_id)
        else:
            db.execute("INSERT INTO stocks (user_id, symbol, amount) VALUES(?, ?, ?)", user_id, symbol, shares)

        db.execute("INSERT INTO transactions (user_id, symbol, price, amount, date, action) VALUES(?, ?, ?, ?, ?, ?)", user_id, share["symbol"], usd(share["price"]), shares, date, action)
        db.execute("UPDATE users SET cash=? WHERE id=?", remainder, user_id)

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id=?", session.get("user_id"))
    return render_template("history.html", transactions=transactions)

@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    if request.method == "POST":
        amount = request.form.get("cash")
        if not amount:
            return apology("Enter amount!")
        db.execute("UPDATE users SET cash=cash+?", amount)
        return redirect("/")

    else:
        return render_template("add_cash.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        if not symbol:
            return apology("Enter the symbol!")

        result = lookup(symbol)

        if result == None:
            return apology("Symbol does not exist!")

        return render_template("quoted.html", symbol=result["symbol"], name=result["name"], price=usd(result["price"]))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        username = request.form.get("username")
        user = db.execute("SELECT username FROM users WHERE username=?", username)
        password1 = request.form.get("password")
        password2 = request.form.get("confirmation")
        password_hash = generate_password_hash(password1)

        if not username or not password1 or not password2:
            return apology("Please fill the required boxes!")
        elif password1 != password2:
            return apology("Passwords do not match!")
        elif user != []:
            return apology("This username already exists!")


        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, password_hash)

        return redirect("/")

    if request.method == "GET":
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    action = "Sell"
    user_id = session.get("user_id")
    stock_list = db.execute("SELECT DISTINCT(symbol) FROM stocks WHERE user_id=?", user_id)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Select stock symbol!")

        amount = int(request.form.get("shares"))
        if amount <= 0:
            return apology("Amount can't be negative or zero!")

        total_amount = (db.execute("SELECT amount FROM stocks WHERE user_id=? AND symbol=?", user_id, symbol))[0]["amount"]
        if amount > total_amount:
            return apology("You don't have enough shares to sell!")

        single_price = lookup(symbol)['price']
        price = amount * single_price
        date = datetime.datetime.now()

        if total_amount - amount == 0:
            db.execute("INSERT INTO transactions (user_id, symbol, price, amount, date, action) VALUES(?, ?, ?, ?, ?, ?)", user_id, symbol, single_price, amount, date, action)
            db.execute("DELETE FROM stocks WHERE symbol=? AND user_id=?", symbol, user_id)
            db.execute("UPDATE users SET cash=cash+? WHERE id=?", price, user_id)
            return redirect("/")

        db.execute("INSERT INTO transactions (user_id, symbol, price, amount, date, action) VALUES(?, ?, ?, ?, ?, ?)", user_id, symbol, usd(single_price), amount, date, action)
        db.execute("UPDATE users SET cash=cash+? WHERE id=?", price, user_id)
        db.execute("UPDATE stocks SET amount=amount-? WHERE user_id=? AND symbol=?", amount, user_id, symbol)

        return redirect("/")

    else:
        return render_template("sell.html", stock_list=stock_list)
