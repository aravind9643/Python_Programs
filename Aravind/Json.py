import json

x = '{"name": "Aravind","age": "22"}'

print x

y = json.loads(x)

z = json.dumps(y, indent=2, sort_keys=True)

print z