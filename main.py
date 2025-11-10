from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# -------------------------------------------------
# 1️⃣ KONFIGURASI KONEKSI DATABASE POSTGRESQL
# -------------------------------------------------
# Format URI: postgresql://username:password@host:port/nama_database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5433/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi database
db = SQLAlchemy(app)

# -------------------------------------------------
# 2️⃣ MODEL SESUAI DENGAN TABEL KAMU
# -------------------------------------------------
class Tb_mahasiswa(db.Model):
    __tablename__ = 'Tb_mahasiswa'  # sesuai nama tabel di PostgreSQL

    NIM = db.Column(db.String(20), primary_key=True)
    NAMA_MAHASISWA = db.Column(db.String(100))
    ALAMAT = db.Column(db.String(150))
    TGL_LAHIR = db.Column(db.Date)

    def __repr__(self):
        return f"<Mahasiswa {self.NAMA_MAHASISWA}>"

# -------------------------------------------------
# 3️⃣ ROUTE UNTUK CEK DATA DARI DATABASE
# -------------------------------------------------
@app.route("/mahasiswa")
def get_mahasiswa():
    data = Tb_mahasiswa.query.all()
    hasil = ""
    for mhs in data:
        hasil += f"{mhs.NIM} - {mhs.NAMA_MAHASISWA} - {mhs.ALAMAT} - {mhs.TGL_LAHIR}<br>"
    return hasil

# -------------------------------------------------
# 4️⃣ ROUTE BAWAAN KAMU
# -------------------------------------------------
@app.route("/get")
def hello_get():
    return "Hello, Anak Baik (GET)"

@app.route("/post")
def hello_post():
    return "Hello, Anak Baik (POST)"

@app.route("/delete")
def hello_delete():
    return "Hello, Anak Baik (DELETE)"

@app.route("/detail/<nama>")
def hello_detail(nama):
    return f"Halo {nama}, ini halaman detail kamu"

# -------------------------------------------------
# 5️⃣ MENJALANKAN APLIKASI
# -------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
