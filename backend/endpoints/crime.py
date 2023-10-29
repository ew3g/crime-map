from fastapi import APIRouter, HTTPException
from models.response import CrimeResponse, CrimeListResponse
from models.models import Crime
from db.database import Database
from sqlalchemy import and_

router = APIRouter(
    prefix="/crime", tags=["Crime"], responses={404: {"description": "Not Found"}}
)

database = Database()
engine = database.get_db_connection()

@router.get("/")
async def read_all_crime():
    session = database.get_db_session(engine)
    data = session.query(Crime).all()
    return CrimeListResponse(data)

@router.get("/{crime_id}", status_code=200)
async def read_crime(crime_id: str):
    crime_existent = get_crime(crime_id)
    if not crime_existent:
        raise HTTPException(status_code=404, detail="Crime não encontrado")
    return CrimeResponse(crime_existent)

@router.get("/city/{city}", status_code=200)
async def read_crime_by_city(city: str):
    session = database.get_db_session(engine)
    data = session.query(Crime).filter(Crime.endCidade == city).all()
    return CrimeListResponse(data)

def get_crime(id):
    session = database.get_db_session(engine)
    try:
        return (
            session.query(Crime)
            .filter(
                and_(
                    Crime.id == id
                )
            )
            .one()
        )
    except:
        return None