import redis
from fastapi import HTTPException

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def rate_limit(ip: str):
    key = f"rate:{ip}"
    current = r.get(key)

    if current and int(current) >= 20:  # 20 requests per minute
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    r.incr(key)
    r.expire(key, 60)
