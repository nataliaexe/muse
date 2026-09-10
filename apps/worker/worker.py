import os
import asyncio
import redis
import json
from datetime import datetime

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

STREAMS = [
    "user_events",
    "style_events",
    "recommendation_events",
    "trend_events"
]

class Worker:
    def __init__(self):
        self.running = True
        
    async def process_event(self, event_data):
        """Process event from stream"""
        event_type = event_data.get("event_type", "UNKNOWN")
        user_id = event_data.get("user_id")
        data = event_data.get("data", {})
        
        print(f"[{datetime.now()}] Processing event: {event_type} for user: {user_id}")
        
        # Route event to appropriate processor
        if event_type.startswith("USER_"):
            await self.process_user_event(event_type, user_id, data)
        elif event_type.startswith("STYLE_"):
            await self.process_style_event(event_type, user_id, data)
        elif event_type.startswith("TREND_"):
            await self.process_trend_event(event_type, user_id, data)
        elif event_type.startswith("RECOMMENDATION_"):
            await self.process_recommendation_event(event_type, user_id, data)
        
    async def process_user_event(self, event_type, user_id, data):
        """Process user-related events"""
        # Update user behavior model
        if event_type == "USER_LIKED_POST":
            # Update preferences
            pass
        elif event_type == "USER_SAVED_LOOK":
            # Update saved items
            pass
        elif event_type == "USER_VIEWED_PRODUCT":
            # Update viewed products
            pass
            
    async def process_style_event(self, event_type, user_id, data):
        """Process style-related events"""
        # Update style intelligence
        pass
        
    async def process_trend_event(self, event_type, user_id, data):
        """Process trend-related events"""
        # Update trend intelligence
        pass
        
    async def process_recommendation_event(self, event_type, user_id, data):
        """Process recommendation-related events"""
        # Update recommendation model
        pass
        
    async def run(self):
        """Main worker loop"""
        print("MUSE Worker started")
        print(f"Listening to streams: {', '.join(STREAMS)}")
        
        while self.running:
            try:
                # Read from all streams
                for stream in STREAMS:
                    events = redis_client.xread({stream: '0'}, count=10, block=1000)
                    
                    for stream_name, event_list in events:
                        for event_id, event_data in event_list:
                            await self.process_event(event_data)
                            
                            # Acknowledge event
                            redis_client.xdel(stream_name, event_id)
                            
            except Exception as e:
                print(f"Error in worker loop: {e}")
                await asyncio.sleep(5)
                
    def stop(self):
        self.running = False

if __name__ == "__main__":
    worker = Worker()
    try:
        asyncio.run(worker.run())
    except KeyboardInterrupt:
        print("\nShutting down worker...")
        worker.stop()
