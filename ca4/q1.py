class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.group = None

def main():
    inp = get_input()
    out = solve(inp)
    print_output(out)
    
def solve(inp):
    neighbor_list = create_neighbor_list(inp)
    is_possible = bind_group(neighbor_list)
    return {"is_possible":is_possible ,"neighbor_list": neighbor_list}

def print_output(out):
    if not out["is_possible"]:
        print(-1)
        return
    team1 = create_list_team_1(out["neighbor_list"])
    print(len(team1))
    print(*team1)

def create_list_team_1(neighbor_list):
    out = list()
    for i in neighbor_list.keys():
        if neighbor_list[i]["self"].group == 1:
            out.append(neighbor_list[i]["self"].value)
    return out

def bind_group(neighbor_list):
    for i in neighbor_list.keys():
        if neighbor_list[i]["self"].group == None:
            bind_group_for_none(i, neighbor_list)
        else:
            flag = bind_group_for_other(i, neighbor_list)
            if flag:
                print(neighbor_list[i]["self"].value)
                return False
        
    return True

def bind_group_for_other(i, neighbor_list):
    '''if not ok return true'''
    opposite_group = {1:2,2:1}
    out = True
    for j in neighbor_list[i]["n"].keys():
        if neighbor_list[i]["n"][j].group == None:
            neighbor_list[i]["n"][j].group = opposite_group[neighbor_list[i]["self"].group]
            return False
        elif neighbor_list[i]["n"][j].group == opposite_group[neighbor_list[i]["self"].group]:
            out = False
    return out
        
def bind_group_for_none(i, neighbor_list):
    opposite_group = {1:2,2:1}
    for j in neighbor_list[i]["n"].keys():
        if neighbor_list[i]["n"][j].group != None:
            neighbor_list[i]["self"].group = opposite_group[neighbor_list[i]["n"][j].group]
            return
    neighbor_list[i]["self"].group = 1
    if len(neighbor_list[i]["n"]) != 0:
        first_neighbor = list(neighbor_list[i]["n"].keys())[0]
        neighbor_list[i]["n"][first_neighbor].group = 2

def create_neighbor_list(inp):
    output = {i+1:{"self":Node(i+1) ,"n":dict()} for i in range(inp["V_count"])}
    for edge in inp["E"]:
        output[edge[0]]["n"][edge[1]] = output[edge[1]]["self"]
        output[edge[1]]["n"][edge[0]] = output[edge[0]]["self"]
    return output

def get_input():
    output = dict()
    output["V_count"], output["E_count"] = map(int, input().split())

    output["E"] = list()
    for _ in range(output["E_count"]):
        new_e = list(map(int, input().split()))
        output["E"].append(new_e)
        
    return output
    
    
if __name__ == "__main__":
    main()