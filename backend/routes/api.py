from fastapi import APIRouter
from endpoints import crime

router = APIRouter()
# router.include_router(tamanhoBuraco.router)
# router.include_router(usuario.router)
# router.include_router(buraco.router)
# router.include_router(auth.router)
# router.include_router(questao.router)
router.include_router(crime.router)
# https: // www.tutorialsbuddy.com/create-rest-api-to-perform-crud-operations-using-fastapi-and -mysql
