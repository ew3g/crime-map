import os, sys
import csv

# adicionar isso para resolver o import
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from db.database import Database
import os
import datetime


database = Database()
engine = database.get_db_connection()


files = os.listdir("./data")

# for file in files:
#     with open("./data/" + file, newline='\n', encoding="utf8") as f:
#         reader = csv.reader(f)
#         your_list = list(reader)

from collections import defaultdict
from models.models import CelularCrime, VeiculoCrime, PessoaCrime, Crime


session = database.get_db_session(engine)

columns = defaultdict(list)
with open("./data/" + "abril-furto.csv", newline="\n", encoding="utf8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        crime_existent = (
            session.query(Crime).filter(Crime.numeroBO == row["NUM_BO"]).first()
        )

        if crime_existent:
            continue

        celular_crime = CelularCrime()
        veiculo_crime = VeiculoCrime()
        pessoa_crime = PessoaCrime()
        crime = Crime()

        celular_crime.marcaCelular = row["MARCA_CELULAR"]
        celular_crime.quantidadeCelular = (
            None if row["QUANT_CELULAR"] == "" else int(row["QUANT_CELULAR"])
        )

        veiculo_crime.anoFabricacaoVeiculo = row["ANO_FABRICACAO"]
        veiculo_crime.anoModeloVeiculo = row["ANO_MODELO"]
        veiculo_crime.cidadeVeiculo = row["CIDADE_VEICULO"]
        veiculo_crime.corVeiculo = row["DESCR_COR_VEICULO"]
        veiculo_crime.cidadeVeiculo = row["CIDADE_VEICULO"]
        veiculo_crime.marcaVeiculo = row["DESCR_MARCA_VEICULO"]
        veiculo_crime.placaVeiculo = row["PLACA_VEICULO"]
        veiculo_crime.tipoVeiculo = row["DESCR_TIPO_VEICULO"]
        veiculo_crime.ufVeiculo = row["UF_VEICULO"]

        pessoa_crime.tipoPessoa = row["TIPOPESSOA"]
        pessoa_crime.vitimaFatal = True if row["VITIMAFATAL"] == "Sim" else False
        pessoa_crime.naturalidade = row["NATURALIDADE"]
        pessoa_crime.nacionalidade = row["NACIONALIDADE"]

        sexo = ""
        if row["SEXO"] == "M" or row["SEXO"] == "Masculino":
            sexo = "M"
        elif row["SEXO"] == "F" or row["SEXO"] == "Feminino":
            sexo = "F"

        pessoa_crime.sexo = sexo
        pessoa_crime.dataNascimento = (
            datetime.datetime.strptime(row["DATANASCIMENTO"], "%m/%d/%Y").date()
            if row["DATANASCIMENTO"] != ""
            else None
        )
        pessoa_crime.idade = int(row["IDADE"]) if row["IDADE"] else None
        pessoa_crime.estadoCivil = row["ESTADOCIVIL"]
        pessoa_crime.profissao = row["PROFISSAO"]
        pessoa_crime.grauInstrucao = row["GRAUINSTRUCAO"]
        pessoa_crime.corCutis = row["CORCUTIS"]
        pessoa_crime.tipoVinculoPessoa = row["TIPOVINCULO"]
        pessoa_crime.relacionamento = row["RELACIONAMENTO"]
        pessoa_crime.parentesco = row["PARENTESCO"]

        session.add(celular_crime)
        session.flush()
        session.refresh(celular_crime, attribute_names=["id"])

        session.add(veiculo_crime)
        session.flush()
        session.refresh(veiculo_crime, attribute_names=["id"])

        session.add(pessoa_crime)
        session.flush()
        session.refresh(pessoa_crime, attribute_names=["id"])

        crime.ano = row["ANO_BO"]
        crime.numeroBO = row["NUM_BO"]

        registroBOFormat = ""
        if len(row["BO_EMITIDO"]) > 16:
            registroBOFormat = "%d/%m/%Y %H:%M:%S"
        else:
            registroBOFormat = "%d/%m/%Y %H:%M"
        crime.registroBO = (
            datetime.datetime.strptime(row["BO_EMITIDO"], registroBOFormat)
            if row["BO_EMITIDO"] != ""
            else None
        )
        crime.dataOcorrencia = (
            datetime.datetime.strptime(row["DATAOCORRENCIA"], "%d/%m/%Y").date()
            if row["DATAOCORRENCIA"] != ""
            else None
        )
        crime.horaOcorrencia = (
            datetime.datetime.strptime(row["HORAOCORRENCIA"], "%H:%M").time()
            if row["HORAOCORRENCIA"] != ""
            else None
        )
        crime.periodoOcorrencia = row["PERIDOOCORRENCIA"]
        crime.dataComunicacao = (
            datetime.datetime.strptime(row["DATACOMUNICACAO"], "%d/%m/%Y").date()
            if row["DATACOMUNICACAO"] != ""
            else None
        )

        dataElaboracaoFormat = ""
        if len(row["DATAELABORACAO"]) > 16:
            dataElaboracaoFormat = "%d/%m/%Y %H:%M:%S"
        else:
            dataElaboracaoFormat = "%d/%m/%Y %H:%M"
        crime.dataElaboracao = (
            datetime.datetime.strptime(row["DATAELABORACAO"], dataElaboracaoFormat)
            if row["DATAELABORACAO"] != ""
            else None
        )
        crime.flagrante = True if row["FLAGRANTE"] == "Sim" else False
        crime.endLogradouro = row["LOGRADOURO"]
        crime.endNumero = row["NUMERO"]
        crime.endBairro = row["BAIRRO"]
        crime.endCidade = row["CIDADE"]
        crime.endUf = row["UF"]
        crime.endDescricao = row["DESCRICAOLOCAL"]

        latitude = row["LATITUDE"]
        longitude = row["LONGITUDE"]
        latitude = latitude.replace(",", "")
        longitude = longitude.replace(",", "")

        newlat = ""
        if latitude != "":
            for i in range(0, len(latitude)):
                if latitude[0] == "-" and i == 3:
                    newlat += "."
                if latitude[0] != "-" and i == 2:
                    newlat += "."
                newlat += latitude[i]

        newlong = ""
        if longitude != "":
            for i in range(0, len(longitude)):
                if longitude[0] == "-" and i == 3:
                    newlong += "."
                if longitude[0] != "-" and i == 2:
                    newlong += "."
                newlong += longitude[i]

        crime.latitude = newlat
        crime.longitude = newlong
        crime.solucao = row["SOLUCAO"]
        crime.delegaciaNome = row["DELEGACIA_NOME"]
        crime.delegaciaCircunscricao = row["DELEGACIA_CIRCUNSCRICAO"]
        crime.rubrica = row["RUBRICA"]
        crime.desdobramento = row["DESDOBRAMENTO"]
        crime.status = row["STATUS"]
        crime.naturezaVinculada = row["NATUREZAVINCULADA"]
        crime.pessoaCrimeId = pessoa_crime.id
        crime.veiculoCrimeId = veiculo_crime.id
        crime.celularCrimeId = celular_crime.id

        session.add(crime)
        session.flush()
        session.commit()
        print(str(crime.numeroBO) + " added")

session.close()
