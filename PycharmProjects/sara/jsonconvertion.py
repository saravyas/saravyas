import json
f = open("loann.txt", 'w')
f1 = open("loans.txt", 'r')
data = json.loads(f1)
f.write(json.dumps(data, indent=1))
f.close()
