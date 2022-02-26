from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# Comando necessário para criar o db e fazer manipulação
engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Criar tabela Pessoa
class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    # Representar o objeto (repr -> representacao)
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    # criar metodo para registrar e comitar
    def save(self):
        # fazer o registro (commit)
        db_session.add(self)
        db_session.commit()

    # criar metodo para deletar (commit)
    def delete(self):
        db_session.delete(self)
        db_session.commit()


# Criar tabela Atividades relacionada com Pessoas
class Atividades(Base):
    __tablename__= 'atividades'
    id = Column(Integer,primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")


  # Representar o objeto (repr -> representacao)
    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    # criar metodo para registrar e comitar
    def save(self):
        # fazer o registro (commit)
        db_session.add(self)
        db_session.commit()

    # criar metodo para deletar (commit)
    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Criação de tabela de usuarios
class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return'<usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Criar metodo init db para criar o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
        init_db()