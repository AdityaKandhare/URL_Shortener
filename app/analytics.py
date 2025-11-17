from datetime import datetime

def update_analytics(db_obj):
    db_obj.clicks += 1
    db_obj.last_accessed = datetime.utcnow()
