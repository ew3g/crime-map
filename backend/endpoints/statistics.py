from fastapi import APIRouter, HTTPException
from models.response import CrimeResponse, CrimeListResponse, CrimeLocationListResponse
from models.models import Crime
from db.database import Database
from sqlalchemy import and_, or_
from fastapi.responses import FileResponse, StreamingResponse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"],
    responses={404: {"description": "Not Found"}},
)

database = Database()
engine = database.get_db_connection()


@router.get(
    "/bar/common-crimes/city/{city}", responses={200: {"content": {"image/png": {}}}}
)
async def get_bar_common_crimes(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["rubrica"] = df["rubrica"].str.replace("Furto (art. 155) - ", "")
    df["rubrica"].value_counts().nlargest(5).plot(kind="bar")

    plt.title("Bairros com mais crimes registrados")
    plt.xlabel("Bairro")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/pie/common-crimes/city/{city}", responses={200: {"content": {"image/png": {}}}}
)
async def get_pie_common_crimes(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["rubrica"] = df["rubrica"].str.replace("Furto (art. 155) - ", "")
    df["rubrica"].value_counts().nlargest(5).plot.pie(autopct="%1.1f%%")

    plt.title("Bairros com mais crimes registrados")
    plt.ylabel("Proporção")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/bar/common-neighborhoods/city/{city}",
    responses={200: {"content": {"image/png": {}}}},
)
async def get_bar_common_neighborhoods(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["endBairro"].value_counts().nlargest(10).plot(kind="bar")

    plt.title("Bairros com mais crimes registrados")
    plt.xlabel("Bairro")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/pie/common-neighborhoods/city/{city}",
    responses={200: {"content": {"image/png": {}}}},
)
async def get_pie_common_neighborhoods(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["endBairro"].value_counts().nlargest(10).plot.pie(autopct="%1.1f%%")

    plt.title("Bairros com mais crimes registrados")
    plt.ylabel("Proporção")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/bar/common-solutions/city/{city}", responses={200: {"content": {"image/png": {}}}}
)
async def get_bar_common_solutions(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["solucao"].value_counts().plot(kind="bar")

    plt.title("Soluções mais comuns")
    plt.xlabel("Solução")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.clf()
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/pie/common-solutions/city/{city}", responses={200: {"content": {"image/png": {}}}}
)
async def get_pie_common_solutions(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["solucao"].value_counts().plot.pie(autopct="%1.1f%%")

    plt.title("Soluções mais comuns")
    plt.ylabel("Proporção")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/bar/common-police-departments/city/{city}",
    responses={200: {"content": {"image/png": {}}}},
)
async def get_bar_common_police_departments(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["delegaciaCircunscricao"].value_counts().plot(kind="bar")

    plt.title("Delegacias com crimes registrados")
    plt.xlabel("Delegacia")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/pie/common-police-departments/city/{city}",
    responses={200: {"content": {"image/png": {}}}},
)
async def get_pie_common_police_departments(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["delegaciaCircunscricao"].value_counts().nlargest(5).plot.pie(autopct="%1.1f%%")

    plt.title("Delegacias com mais crimes registrados")
    plt.ylabel("Proporção")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/bar/common-day-period/city/{city}",
    responses={200: {"content": {"image/png": {}}}},
)
async def get_bar_common_day_period(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["periodoOcorrencia"].value_counts().plot(kind="bar")

    plt.title("Total de  ocorrências por período do dia")
    plt.xlabel("Período do dia")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


@router.get(
    "/pie/common-day-period/city/{city}",
    responses={200: {"content": {"image/png": {}}}},
)
async def get_pie_common_day_period(city: str, year: int = None):
    session = database.get_db_session(engine)
    df = pd.read_sql(
        session.query(Crime)
        .filter(
            and_(Crime.endCidade == city, Crime.latitude != "", Crime.longitude != ""),
            or_(Crime.ano == year, year == None),
        )
        .statement,
        session.bind,
    )

    df["periodoOcorrencia"].value_counts().plot.pie(autopct="%1.1f%%")

    plt.title("Total de  ocorrências por período do dia")
    plt.ylabel("Proporção")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.clf()
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")


# id                                 int64
# ano                                int64
# numeroBO                           int64
# registroBO                datetime64[ns]
# dataOcorrencia                    object
# horaOcorrencia                    object
# periodoOcorrencia                 object
# dataComunicacao                   object
# dataElaboracao            datetime64[ns]
# flagrante                           bool
# endLogradouro                     object
# endNumero                         object
# endBairro                         object
# endCidade                         object
# endUf                             object
# endDescricao                      object
# latitude                          object
# longitude                         object
# solucao                           object
# delegaciaNome                     object
# delegaciaCircunscricao            object
# rubrica                           object
# desdobramento                     object
# status                            object
# naturezaVinculada                 object
# pessoaCrimeId                      int64
# veiculoCrimeId                     int64
# celularCrimeId                     int64
