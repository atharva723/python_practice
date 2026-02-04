import pickle
data="python is easy\n"
binary=pickle.dumps(data)
with open("B-file.txt",'wb+') as file:
    file.write(binary)
    file.seek(0)
    file_binary=file.read()
    decode=pickle.loads(file_binary)
    print(decode)

import json
data_j={"username":"ATHARVA.20","PASS":201843}
encoded=json.dumps(data_j)
with open('JSON_P.txt',"w+") as file:
    file.write(encoded)
    file.seek(0)
    print(type(file.read()))
    print(type(json.loads(encoded)))
