from api_config import db


class Libros(db.Model):
    __tablename__ = "libros"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(500))
    email  = db.Column(db.String(150), nullable=True)
    depto_fk = db.Column(db.Integer, db.ForeignKey("editoriales.id"))
    departamento = db.relationship('Editoriales', backref='autores_depto')