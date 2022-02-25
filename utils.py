
# importa o modelo de dados
from models import Pessoas

# Criar funções: inserção, consulta, alteração e deleção

def insere_pessoas():
    pessoa = Pessoas(nome='Galeane', idade=25)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.nome)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galeane').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
