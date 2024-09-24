import redis

r = redis.Redis(host='localhost', port=6379, db=1)

r.set('mykey', 'myvalue')

value = r.get('mykey')
print(value) # Should return b'myvalue'

r.delete('mykey') 

print(r.get('mykey')) # Should now return None

