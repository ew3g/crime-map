create database if not exists crime_db;

use crime_db;

/*
drop table Crime;
drop table PessoaCrime;
drop table VeiculoCrime;
drop table CelularCrime;
*/





CREATE TABLE IF NOT EXISTS PessoaCrime(
    id int auto_increment primary key,
    tipoPessoa varchar(50),
    vitimaFatal boolean default false,
    naturalidade varchar(50),
    nacionalidade varchar(50),
    sexo varchar(1),
    dataNascimento date,
    idade int,
    estadoCivil varchar(50),
    profissao varchar(50),
    grauInstrucao varchar(50),
    corCutis varchar(50),
    tipoVinculoPessoa varchar(50),
    relacionamento varchar(50),
    parentesco varchar(50)
);

CREATE TABLE IF NOT EXISTS VeiculoCrime (
    id int auto_increment primary key,
    placaVeiculo varchar(50),
    ufVeiculo varchar(4),
    cidadeVeiculo varchar(50),
    corVeiculo varchar(50),
    marcaVeiculo varchar(50),
    anoFabricacaoVeiculo varchar(50),
    anoModeloVeiculo varchar(50),
    tipoVeiculo varchar(50)
);

CREATE TABLE IF NOT EXISTS CelularCrime (
    id int auto_increment primary key,
    quantidadeCelular int,
    marcaCelular varchar(50)
);

create table if not exists Crime (
	id int auto_increment primary key,
    ano int,
    numeroBO int unique,
    registroBO datetime,
    dataOcorrencia date,
    horaOcorrencia time,
    periodoOcorrencia varchar(50),
    dataComunicacao date,
    dataElaboracao datetime,
    flagrante boolean default false,
    endLogradouro varchar(200),
    endNumero varchar(50),
    endBairro varchar(100),
    endCidade varchar(50),
    endUf varchar(4),
    endDescricao varchar(50),
    latitude text,
    longitude text, 
    solucao varchar(200),
    delegaciaNome varchar(50),
    delegaciaCircunscricao varchar(50),
    rubrica varchar(100),
    desdobramento varchar(100),
    status varchar(50),
    naturezaVinculada varchar(200),
    pessoaCrimeId int,
    veiculoCrimeId int,
    celularCrimeId int,
    FOREIGN KEY (pessoaCrimeId) references PessoaCrime(id),
    FOREIGN KEY (veiculoCrimeId) references VeiculoCrime(id),
    FOREIGN KEY (celularCrimeId) references CelularCrime(id)
);