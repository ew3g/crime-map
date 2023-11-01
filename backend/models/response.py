def Response(data, code, message, error):
    return {"data": data, "code": code, "message": message, "error": error}


def AuthResponse(token, usuarioId):
    return {"token": token, "usuarioId": usuarioId}


def UsuarioResponse(model):
    return {"nomeUsuario": model.nomeUsuario, "email": model.email, "id": model.id}


def UsuarioListResponse(list):
    response = []
    for user in list:
        response.append(UsuarioResponse(user))
    return response


def TamanhoBuracoResponse(model):
    return {"id": model.id, "nome": model.nome, "cor": model.cor}


def TamanhoBuracoListResponse(list):
    response = []
    for tamanhoBuraco in list:
        response.append(TamanhoBuracoResponse(tamanhoBuraco))
    return response


def BuracoResponse(model):
    return {
        "latitude": model.latitude,
        "longitude": model.longitude,
        "votos": model.votos,
        "id": model.id,
        "tamanho": model.tamanhoBuraco.nome,
        "cor": model.tamanhoBuraco.cor,
    }


def BuracoListResponse(list):
    response = []
    for buraco in list:
        response.append(BuracoResponse(buraco))
    return response


def QuestaoResponse(model):
    return {"id": model.id, "pergunta": model.pergunta}


def QuestaoListResponse(list):
    response = []
    for questao in list:
        response.append(QuestaoResponse(questao))
    return response


def CrimeResponse(model):
    pessoa = (
        None
        if not model.pessoaCrimeId
        else {
            "id": model.pessoaCrime.id,
            "tipoPessoa": model.pessoaCrime.tipoPessoa,
            "vitimaFatal": model.pessoaCrime.vitimaFatal,
            "naturalidade": model.pessoaCrime.naturalidade,
            "nacionalidade": model.pessoaCrime.nacionalidade,
            "sexo": model.pessoaCrime.sexo,
            "dataNascimento": model.pessoaCrime.dataNascimento,
            "idade": model.pessoaCrime.idade,
            "estadoCivil": model.pessoaCrime.estadoCivil,
            "profissao": model.pessoaCrime.profissao,
            "grauInstrucao": model.pessoaCrime.grauInstrucao,
            "corCutis": model.pessoaCrime.corCutis,
            "tipoVinculo": model.pessoaCrime.tipoVinculoPessoa,
            "relacionamento": model.pessoaCrime.relacionamento,
            "parentesco": model.pessoaCrime.parentesco,
        }
    )
    veiculo = (
        None
        if not model.veiculoCrimeId
        else {
            "id": model.veiculoCrime.id,
            "placa": model.veiculoCrime.placaVeiculo,
            "uf": model.veiculoCrime.ufVeiculo,
            "cidade": model.veiculoCrime.cidadeVeiculo,
            "cor": model.veiculoCrime.corVeiculo,
            "marca": model.veiculoCrime.marcaVeiculo,
            "anoFabricacao": model.veiculoCrime.anoFabricacaoVeiculo,
            "anoModelo": model.veiculoCrime.anoModeloVeiculo,
            "tipo": model.veiculoCrime.tipoVeiculo,
        }
    )

    celular = (
        None
        if not model.celularCrimeId
        else {
            "id": model.celularCrime.id,
            "quantidade": model.celularCrime.quantidadeCelular,
            "marca": model.celularCrime.marcaCelular,
        }
    )

    return {
        "id": model.id,
        "ano": model.ano,
        "numeroBO": model.numeroBO,
        "registroBO": model.registroBO,
        "dataOcorrencia": model.dataOcorrencia,
        "horaOcorrencia": model.horaOcorrencia,
        "periodoOcorrencia": model.periodoOcorrencia,
        "dataComunicacao": model.dataComunicacao,
        "dataElaboracao": model.dataElaboracao,
        "flagrante": model.flagrante,
        "endLogradouro": model.endLogradouro,
        "endNumero": model.endNumero,
        "endBairro": model.endBairro,
        "endCidade": model.endCidade,
        "endUf": model.endUf,
        "endDescricao": model.endDescricao,
        "latitude": model.latitude,
        "longitude": model.longitude,
        "solucao": model.solucao,
        "delegaciaNome": model.delegaciaNome,
        "delegaciaCircunscricao": model.delegaciaCircunscricao,
        "rubrica": model.rubrica,
        "desdobramento": model.desdobramento,
        "status": model.status,
        "naturezaVinculada": model.naturezaVinculada,
        "pessoa": pessoa,
        "veiculo": veiculo,
        "celular": celular,
    }


def CrimeLocationResponse(model):
    return {
        "id": model.id,
        "latitude": model.latitude,
        "longitude": model.longitude,
    }


def CrimeListResponse(list):
    response = []
    for crime in list:
        response.append(CrimeResponse(crime))
    return response


def CrimeLocationListResponse(list):
    response = []
    for crime in list:
        response.append(CrimeResponse(crime))
    return response
