from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)
from api_config import (
    db,
)

from .objects import (
    Autores
)
from .libros import Libros as LibrosModel
from .editoriales import Autores as AutoresModel
from .editoriales import Editoriales as EditorialesModel


class createAutores(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    autores = Field(lambda: Autores)

    def mutate(self, info, name, last_name, email=None):
        autores = AutoresModel(name=name, last_name=last_name, email=email)

        db.session.add(autores)
        db.session.commit()

        return createAutores(autores=autores)

class updateAutores(Mutation):
    class Arguments:
        persona_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    autores = Field(lambda: Autores)

    def mutate(self, info, persona_id, email=None, name=None, last_name=None):
        autores = AutoresModel.query.get(persona_id)
        if autores:
            if email:
                autores.email = email
            if name:
                autores.name = name
            if last_name:
                autores.last_name = last_name
            db.session.add(autores)
            db.session.commit()

        return updateAutores(autores=autores)


class deleteAutores(Mutation):
    class Arguments:
        autores_id = Int(required=True)

    autores = Field(lambda: Autores)

    def mutate(self, info, autores_id):
        autores = AutoresModel.query.get(autores_id)
        if autores:
            db.session.delete(autores)
            db.session.commit()

        return deleteAutores(autores=autores)

class createLibros(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    libros = Field(lambda: Autores)

    def mutate(self, info, name, last_name, email=None):
        libros = AutoresModel(name=name, last_name=last_name, email=email)

        db.session.add(libros)
        db.session.commit()

        return createAutores(libros=libros)

class update_Libros(Mutation):
    class Arguments:
        persona_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    libros = Field(lambda: LibrosModel)

    def mutate(self, info, persona_id, email=None, name=None, last_name=None):
        libros = LibrosModel.query.get(persona_id)
        if libros:
            if email:
                libros.email = email
            if name:
                libros.name = name
            if last_name:
                libros.last_name = last_name
            db.session.add(libros)
            db.session.commit()

        return update_Libros(libros=libros)

class deleteLibros(Mutation):
    class Arguments:
        libros_id = Int(required=True)

    libros = Field(lambda: LibrosModel)

    def mutate(self, info, autores_id):
        libros = AutoresModel.query.get(autores_id)
        if libros:
            db.session.delete(libros)
            db.session.commit()

        return deleteLibros(libros=libros)

class createEditoriales(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    editoriales = Field(lambda: EditorialesModel)

    def mutate(self, info, name, last_name, email=None):
        editoriales = AutoresModel(name=name, last_name=last_name, email=email)

        db.session.add(editoriales)
        db.session.commit()

        return createEditoriales(editoriales=editoriales)
    
class updateEditoriales(Mutation):
    class Arguments:
        persona_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    libros = Field(lambda: EditorialesModel)

    def mutate(self, info, persona_id, email=None, name=None, last_name=None):
        editoriales = EditorialesModel.query.get(persona_id)
        if editoriales:
            if email:
                editoriales.email = email
            if name:
                editoriales.name = name
            if last_name:
                editoriales.last_name = last_name
            db.session.add(editoriales)
            db.session.commit()

        return updateEditoriales(editoriales=editoriales)
    
class deleteEditoriales(Mutation):
    class Arguments:
        libros_id = Int(required=True)

    editoriales = Field(lambda: EditorialesModel)

    def mutate(self, info, autores_id):
        libros = AutoresModel.query.get(autores_id)
        if libros:
            db.session.delete(libros)
            db.session.commit()

        return deleteEditoriales(editoriales=editoriales)


class Mutation(ObjectType):
    create_autores = createAutores.Field()
    update_autores = updateAutores.Field()
    delete_autores = deleteAutores.Field()
    create_libros = createLibros.Field()
    update_libros = update_Libros.Field()
    delete_libros = deleteLibros.Field()
    create_editoriales = createEditoriales.Field()
    updateeditoriales = updateEditoriales.Field()
    delete_editoriales = deleteEditoriales.Field()
