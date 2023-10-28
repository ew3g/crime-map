from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    ForeignKey,
    INTEGER,
    String,
    TIMESTAMP,
    BIGINT,
    BOOLEAN,
    TEXT,
    DateTime,
    Date,
    Time
)
from sqlalchemy.orm import relationship

Base = declarative_base()


class PessoaCrime(Base):
    __tablename__ = "PessoaCrime"
    id = Column(INTEGER, primary_key=True)
    tipoPessoa = Column(String(50))
    vitimaFatal = Column(BOOLEAN, default=False)
    naturalidade = Column(String(50))
    nacionalidade = Column(String(50))
    sexo = Column(String(1))
    dataNascimento = Column(Date)
    idade = Column(INTEGER)
    estadoCivil = Column(String(50))
    profissao = Column(String(50))
    grauInstrucao = Column(String(50))
    corCutis = Column(String(50))
    tipoVinculoPessoa = Column(String(50))
    relacionamento = Column(String(50))
    parentesco = Column(String(50))
    
class VeiculoCrime(Base):
    __tablename__ = "VeiculoCrime"
    id = Column(INTEGER, primary_key=True)
    placaVeiculo = Column(String(50))
    ufVeiculo = Column(String(4))
    cidadeVeiculo = Column(String(50))
    corVeiculo = Column(String(50))
    marcaVeiculo = Column(String(50))
    anoFabricacaoVeiculo = Column(String(50))
    anoModeloVeiculo = Column(String(50))
    tipoVeiculo = Column(String(50))

class CelularCrime(Base):
    __tablename__ = "CelularCrime"
    id = Column(INTEGER, primary_key=True)
    quantidadeCelular = Column(INTEGER)
    marcaCelular = Column(String(50))

    
    
    
class Crime(Base):
    __tablename__ = "Crime"
    id = Column(INTEGER, primary_key=True)
    ano = Column(INTEGER)
    numeroBO = Column(INTEGER, unique=True)
    registroBO = Column(DateTime)
    dataOcorrencia = Column(Date)
    horaOcorrencia = Column(Time)
    periodoOcorrencia = Column(String(50))
    dataComunicacao = Column(Date)
    dataElaboracao = Column(DateTime)
    flagrante = Column(BOOLEAN, default=False)
    endLogradouro = Column(String(200))
    endNumero = Column(String(50))
    endBairro = Column(String(100))
    endCidade = Column(String(50))
    endUf = Column(String(4))
    endDescricao = Column(String(50))
    latitude = Column(String)
    longitude = Column(String)
    solucao = Column(String(200))
    delegaciaNome = Column(String(50))
    delegaciaCircunscricao = Column(String(50))
    rubrica = Column(String(100))
    desdobramento = Column(String(100))
    status = Column(String(50))
    naturezaVinculada = Column(String(200))
    pessoaCrimeId = Column(INTEGER, ForeignKey("PessoaCrime.id"))
    veiculoCrimeId = Column(INTEGER, ForeignKey("VeiculoCrime.id"))
    celularCrimeId = Column(INTEGER, ForeignKey("CelularCrime.id"))
    
    pessoaCrime = relationship("PessoaCrime", backref="Crime")
    veiculoCrime = relationship("VeiculoCrime", backref="Crime")
    celularCrime = relationship("CelularCrime", backref="Crime")