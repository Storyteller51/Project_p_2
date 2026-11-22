logs = [ 
("alice", True), 
("bob", False), 
("alice", True), 
("alice", False), 
("bob", True), 
("charlie", False), 
]

def analyze_logins(logs) :
   #success = 0
   #fail = 0
   #result = {}
    #result.setdefault(a, {"success": 0, "failed": 0})
    result = {}
    for a,b in logs:
        result.setdefault(a, {"success": 0, "failed": 0})   
        if b == True:
            result[a]["success"] += 1
        else:
            result[a]["failed"] += 1
    print(result)          

analyze_logins(logs)