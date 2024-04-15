from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from sqlalchemy.testing.pickleable import User
from sqlalchemy.exc import DatabaseError
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:PSBD@localhost:5432/PSBD"
db = SQLAlchemy(app)


# Database model
class TypCiala(db.Model):
    __tablename__ = 'typ_ciała'
    typ_id = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.Text, nullable=False)


class BMI(db.Model):
    __tablename__ = 'BMI'
    BMI_id = db.Column(db.Integer, primary_key=True)
    wartosc = db.Column(db.Numeric, nullable=False)
    stan_zdrowia = db.Column(db.Text, nullable=False)


class Czas(db.Model):
    __tablename__ = 'czas'
    czas_id = db.Column(db.Integer, primary_key=True)
    data_modyfikacji = db.Column(db.DateTime, default=datetime.now)


class Cel(db.Model):
    __tablename__ = 'cel'
    cel_id = db.Column(db.Integer, primary_key=True)
    cel = db.Column(db.Text, nullable=False)


class TrybZycia(db.Model):
    __tablename__ = 'tryb_życia'
    tryb_id = db.Column(db.Integer, primary_key=True)
    tryb_zycia = db.Column(db.Text, nullable=False)


class PPM(db.Model):
    __tablename__ = 'PPM'
    PPM_id = db.Column(db.Integer, primary_key=True)
    PPM = db.Column(db.Numeric, nullable=False)


class PAL(db.Model):
    __tablename__ = 'PAL'
    PAL_id = db.Column(db.Integer, primary_key=True)
    PAL = db.Column(db.Numeric, nullable=False)


class CPM(db.Model):
    __tablename__ = 'CPM'
    CPM_id = db.Column(db.Integer, primary_key=True)
    CPM = db.Column(db.Numeric, nullable=False)
    PAL_id = db.Column(db.Integer, db.ForeignKey('PAL.PAL_id'), nullable=False)
    PPM_id = db.Column(db.Integer, db.ForeignKey('PPM.PPM_id'), nullable=False)
    PAL_rel = db.relationship("PAL")
    PPM_rel = db.relationship("PPM")


class Uzytkownik(db.Model):
    __tablename__ = 'użytkownik'
    id = db.Column(db.Integer, primary_key=True)
    nazwa_uzytkownika = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    haslo = db.Column(db.Text, nullable=False)
    uwagi = db.Column(db.Text)
    wiek = db.Column(db.Numeric)
    wzrost = db.Column(db.Numeric)
    waga = db.Column(db.Numeric)
    typ_id = db.Column(db.Integer, db.ForeignKey('typ_ciała.typ_id'))
    CPM_id = db.Column(db.Integer, db.ForeignKey('CPM.CPM_id'))
    BMI_id = db.Column(db.Integer, db.ForeignKey('BMI.BMI_id'))
    czas_id = db.Column(db.Integer, db.ForeignKey('czas.czas_id'))
    cel_id = db.Column(db.Integer, db.ForeignKey('cel.cel_id'))
    tryb_id = db.Column(db.Integer, db.ForeignKey('tryb_życia.tryb_id'))
    typ_rel = db.relationship("TypCiala")
    CPM_rel = db.relationship("CPM")
    BMI_rel = db.relationship("BMI")
    czas_rel = db.relationship("Czas")
    cel_rel = db.relationship("Cel")
    tryb_rel = db.relationship("TrybZycia")


class Produkt(db.Model):
    __tablename__ = 'produkty'
    produkt_id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.Text, nullable=False)
    kategoria = db.Column(db.Text, nullable=False)


class RekomendowanaLista(db.Model):
    __tablename__ = 'rekomendowana_lista'
    uzytkownik_id = db.Column(db.Integer, db.ForeignKey('użytkownik.id'), primary_key=True)
    produkt_id = db.Column(db.Integer, db.ForeignKey('produkty.produkt_id'), primary_key=True)
    uzytkownik_rel = db.relationship("Uzytkownik")
    produkt_rel = db.relationship("Produkt")


# API
@app.route('/register', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def register():
    try:
        data_json = request.get_json()

        nazwa_uzytkownika = data_json['nazwa_uzytkownika']
        email = data_json['email']
        haslo = data_json['haslo']

        new_user = Uzytkownik(
            nazwa_uzytkownika=nazwa_uzytkownika,
            email=email,
            haslo=haslo
        )

        validate_email(email)

        if db.session.query(Uzytkownik).filter_by(nazwa_uzytkownika=nazwa_uzytkownika).first():
            return jsonify({'error': 'This username is already taken. Try again with another one.'}), 400
        if db.session.query(Uzytkownik).filter_by(email=email).first():
            return jsonify({'error': 'This email is already taken. Try again with another one.'}), 400

        db.session.add(new_user)
        db.session.commit()

    except EmailNotValidError as e:
        return jsonify({'error': str(e)}), 400

    except ValueError:
        return jsonify({'error': 'Invalid data'}), 400

    except DatabaseError:
        return jsonify({'error': 'Username already exists. '}), 400

    return '', 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8081)