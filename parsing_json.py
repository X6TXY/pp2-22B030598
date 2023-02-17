import json

with open('sample-data.json') as file:
    json_data = json.load(file)





print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

iamdata=json_data["imdata"]

for item in iamdata:
    nt_item = item["l1PhysIf"]
    att = nt_item["attributes"]
    dn = att["dn"]
    speed = att["speed"]
    mtu = att["mtu"]
    output = ""
    if(len(dn)==42):
        output+=dn + " "*30  +speed+"   "+ mtu
    else:
        output += dn + " "*31 + speed + "   " + mtu
    print(output)