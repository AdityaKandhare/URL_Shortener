from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.cache import cache_get, increment_click
from app.database import get_db
from app.models import URL
from app.analytics import update_analytics

router = APIRouter()

@router.get("/{short}")
def redirect(short: str, db: Session = Depends(get_db)):

    # 1. Check Redis cache first
    long_url = cache_get(short)
    if long_url:
        # Update analytics in DB
        db_obj = db.query(URL).filter(URL.short == short).first()
        if db_obj:
            update_analytics(db_obj)
            db.commit()

        increment_click(short)
        return RedirectResponse(long_url, status_code=307)

    # 2. If not in cache, check Postgres
    db_url = db.query(URL).filter(URL.short == short).first()

    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")

    update_analytics(db_url)
    db.commit()

    increment_click(short)

    return RedirectResponse(db_url.long, status_code=307)
