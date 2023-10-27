create database if not exists crime_db;

use crime_db;

/*
drop table PessoaCrime;
drop table VeiculoCrime;
drop table CelularCrime;
drop table Crime;
*/





CREATE TABLE IF NOT EXISTS PessoaCrime(
    id int auto_increment primary key,
    tipoPessoa varchar(50),
    vitimaFatal boolean default false,
    naturalidade varchar(50),
    nacionalidade varchar(50),
    sexo varchar(1),
    dataNascimento datetime,
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
    ano int not null,
    numeroBO int not null,
    registroBO datetime not null,
    dataOcorrencia date,
    horaOcorrencia time,
    periodoOcorrencia varchar(50),
    dataComunicacao date,
    dataElaboracao datetime,
    flagrante boolean default false,
    endLogradouro varchar(200),
    endNumero varchar(9),
    endBairro varchar(100),
    endCidade varchar(50),
    endUf varchar(4),
    endDescricao varchar(50),
    latitude text,
    longitute text, 
    solucao varchar(200),
    delegaciaNome varchar(50),
    delegaciaCircunscricao varchar(50),
    rubrica varchar(100),
    desdobramento varchar(100),
    status varchar(50),
    naturezaVinculada varchar(50),
    pessoaCrimeId int,
    veiculoCrimeId int,
    celularCrimeId int,
    FOREIGN KEY (pessoaCrimeId) references PessoaCrime(id),
    FOREIGN KEY (veiculoCrimeId) references VeiculoCrime(id),
    FOREIGN KEY (celularCrimeId) references CelularCrime(id)
);



-- drop table usuario
create table if not exists usuario (
	id int auto_increment primary key,
    nomeUsuario varchar(50) not null,
    email varchar(150) not null unique,
    senha varchar(50) not null,
    ativo boolean,
    apagado boolean default false,
    adm boolean
);

-- drop table questaoUsuario;
create table if not exists questaoUsuario (
    id int auto_increment primary key,
    pergunta varchar(100) not null
);

-- drop table questaoUsuarioResposta;
create table if not exists questaoUsuarioResposta (
    id int auto_increment primary key,
    idQuestaoUsuario int not null,
    idUsuario int not null,
    resposta varchar(50) not null,
    constraint fk_resposta_questao foreign key (idQuestaoUsuario) references questaoUsuario(id),
    constraint fk_resposta_usuario foreign key (idUsuario) references usuario(id) 
);

-- drop table buraco
create table if not exists buraco (
	id int auto_increment primary key,
    latitude text not null,
    longitude text not null,
    idTamanhoBuraco int not null,
    idUsuario int not null,
    votos int default 0,
    apagado boolean default false,
    constraint fk_buraco_tamanhoBuraco foreign key (idTamanhoBuraco) references tamanhoBuraco(id),
    constraint fk_buraco_usuario foreign key (idUsuario) references usuario(id) 
);
