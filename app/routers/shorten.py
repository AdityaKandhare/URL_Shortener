from app.schemas import URLRequest, URLResponse
from app.utils import generate_short_url
from app.cache import cache_set
from app.database import get_db
from app.models import URL
from app.rate_limit import rate_limit
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.config import settings




router = APIRouter()

@router.post("/shorten", response_model=URLResponse)
def shorten_url(request: Request, data: URLRequest, db: Session = Depends(get_db)):
    # generate short code
    short = generate_short_url(str(data.url))

    # save to database
    db_url = URL(short=short, long=str(data.url))   # <-- FIX HERE
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return {"short_url": f"{request.base_url}{short}"}

