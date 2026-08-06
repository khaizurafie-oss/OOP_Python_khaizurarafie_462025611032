from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "cuci_sepatu"
data_pelanggan = []
data_transaksi = []

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":
        session["admin"] = username
        return redirect("/dashboard")

    return "Login gagal"


@app.route("/dashboard")
def dashboard():

    if "admin" in session:
        return render_template("dashboard.html")

    return redirect("/")


@app.route("/pelanggan")
def pelanggan():
    return render_template(
        "pelanggan.html",
        pelanggan=data_pelanggan
    )


@app.route("/hapus_pelanggan/<int:index>")
def hapus_pelanggan(index):

    if 0 <= index < len(data_pelanggan):
        data_pelanggan.pop(index)

    return redirect("/pelanggan")


@app.route("/edit_pelanggan/<int:index>", methods=["GET", "POST"])
def edit_pelanggan(index):

    if request.method == "POST":

        data_pelanggan[index]["nama"] = request.form["nama"]
        data_pelanggan[index]["no_hp"] = request.form["no_hp"]
        data_pelanggan[index]["alamat"] = request.form["alamat"]

        return redirect("/pelanggan")

    return render_template(
        "edit_pelanggan.html",
        pelanggan=data_pelanggan[index],
        index=index
    )


@app.route("/tambah_pelanggan", methods=["GET", "POST"])
def tambah_pelanggan():

    if request.method == "POST":

        nama = request.form["nama"]
        no_hp = request.form["no_hp"]
        alamat = request.form["alamat"]

        data_pelanggan.append({
            "nama": nama,
            "no_hp": no_hp,
            "alamat": alamat
        })

        print(data_pelanggan)

        return redirect("/pelanggan")

    return render_template("tambah_pelanggan.html")


@app.route("/transaksi")
def transaksi():
    return render_template(
        "transaksi.html",
        transaksi=data_transaksi
    )

@app.route("/tambah_transaksi", methods=["GET", "POST"])
def tambah_transaksi():

    if request.method == "POST":

        pelanggan = request.form["pelanggan"]
        jenis_sepatu = request.form["jenis_sepatu"]
        layanan = request.form["layanan"]
        harga = request.form["harga"]
        status = request.form["status"]

        data_transaksi.append({
            "pelanggan": pelanggan,
            "jenis_sepatu": jenis_sepatu,
            "layanan": layanan,
            "harga": harga,
            "status": status
        })

        return redirect("/transaksi")

    return render_template("tambah_transaksi.html")


@app.route("/hapus_transaksi/<int:index>")
def hapus_transaksi(index):

    if 0 <= index < len(data_transaksi):
        data_transaksi.pop(index)

    return redirect("/transaksi")


@app.route("/edit_transaksi/<int:index>", methods=["GET", "POST"])
def edit_transaksi(index):

    if request.method == "POST":

        data_transaksi[index]["pelanggan"] = request.form["pelanggan"]
        data_transaksi[index]["jenis_sepatu"] = request.form["jenis_sepatu"]
        data_transaksi[index]["layanan"] = request.form["layanan"]
        data_transaksi[index]["harga"] = request.form["harga"]
        data_transaksi[index]["status"] = request.form["status"]

        return redirect("/transaksi")

    return render_template(
        "edit_transaksi.html",
        transaksi=data_transaksi[index]
    )


@app.route("/pendapatan")
def pendapatan():

    total = 0

    for t in data_transaksi:
        total += int(t["harga"])

    return render_template(
        "pendapatan.html",
        transaksi=data_transaksi,
        total=total
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")