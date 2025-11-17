import redis
from app.config import settings


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

def cache_set(short: str, long: str):
    r.set(short, long, ex=86400)  # 24-hour TTL

def cache_get(short: str):
    return r.get(short)

def increment_click(short: str):
    r.incr(f"clicks:{short}")
