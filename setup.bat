call python -m pip install redis -y
call docker run -d -p 6379:6379 --name redis-server redis
call python redis_setget.py
@pause