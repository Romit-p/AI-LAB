Rooms={"A":"Dirty Room","B":"Clean Room"}
position="A"
memory=[]
while not (Rooms["A"] == Rooms["B"] == "Clean Room"):
    other="B" if position=="A" else "A"
    if Rooms[position]=="Dirty Room":
        Rooms[position]="Clean Room"
        action="Suck In "+position
    elif Rooms[other]=="Dirty Room":
        position=other
        action="Move to "+position
    memory.append((len(memory) + 1, position, action, Rooms["A"], Rooms["B"]))
print("Index | Position | Action | A | B")
for row in memory:
    print(" | ".join(map(str, row)))
print("Both Rooms Clean")
