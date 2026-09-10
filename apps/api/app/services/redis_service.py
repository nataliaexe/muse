import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def cache_set(key: str, value: str, expiration: int = 3600):
    """Set a cache value with expiration in seconds"""
    return redis_client.setex(key, expiration, value)

def cache_get(key: str):
    """Get a cache value"""
    return redis_client.get(key)

def cache_delete(key: str):
    """Delete a cache value"""
    return redis_client.delete(key)

def add_to_stream(stream_name: str, data: dict):
    """Add event to Redis stream"""
    return redis_client.xadd(stream_name, data)
