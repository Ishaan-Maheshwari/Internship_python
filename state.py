import json

state_code = {"ANDAMAN & NICOBAR" : "AN", "ANDHRA  PRADESH" : "AP", "ARUNACHAL PRADESH" : "AR", "ASSAM" : "AS", "BIHAR" : "BR", "CHANDIGARH" : "CH", "DAMAN & DIU" : "DD", "DELHI" : "DL", "DADRA & NAGAR HAVELI" : "DH", "GOA" : "GA", "GUJARAT" : "GJ", "HIMACHAL PRADESH" : "HP", "HARYANA" : "HR", "JAMMU & KASHMIR" : "JK", "KERALA" : "KL", "KARNATAKA" : "KA", "LAKSHADWEEP" : "LD", "MEGHALAYA" : "ML", "MAHARASHTRA" : "MH", "MANIPUR" : "MN", "MADHYA PRADESH" : "MP", "MIZORAM" : "MZ", "NAGALAND" : "NL", "ODISHA" : "OR", "PUNJAB" : "PB", "PUDUCHERRY" : "PY", "RAJASTHAN" : "RJ", "SIKKIM" : "SK", "TAMIL NADU" : "TN", "TRIPURA" : "TR", "UTTAR PRADESH" : "UP", "WEST BENGAL" : "WB", "CHHATTISGARH" : "CG", "JHARKHAND" : "JH", "UTTARAKHAND" : "UK", "TELANGANA" : "TS"}
f = open('states_master.json','r')
mydic = json.loads(f.read())
for state_detail in mydic:
    sname = state_detail['name']
    state_detail["state_code"] = state_code[sname]

json_object = json.dumps(mydic, indent = 4)
with open("states_master_withcode.json", "w") as outfile:
    outfile.write(json_object)
