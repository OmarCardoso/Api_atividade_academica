from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import scoped_session, sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base

#USUARIOS = {
#    'Rafael': '321',
#    'Galleani': '321'
#}

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class pessoa(Resource):
    @auth.login_required
    # Consulta
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    # Alteração
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    # Exclusão
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


# listar pessoas
class ListaPessoas(Resource):
    @auth.login_required
    # Consultar
    def get(self):
        pessoas = Pessoas.query.all()
        # response = (i for i in pssoas)
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    # Incluir
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividades(Resource):
    @auth.login_required
    # Consultar
    def get(self):
        #  atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividade/')

if __name__ == '__main__':
    app.run(debug=True)
