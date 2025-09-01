import itertools

k=int(input("Enter value of k from 1 to 10:"))
Pokedex = { 
"Pikachu": ("Electric",), 
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"), 
"Machamp": ("Fighting",), 
"Mewtwo": ("Psychic", "Fighting"), 
"Hoopa": ("Psychic", "Ghost", "Dark"), 
"Lugia": ("Psychic", "Flying", "Water"),  
"Squirtle": ("Water",), 
"Gengar": ("Ghost", "Poison"), 
"Onix": ("Rock", "Ground") 
}

possible_combinations=()
maxx=0
items = list(["Pikachu","Charizard","Lapras","Machamp","Mewtwo","Hoopa","Lugia","Squirtle","Gengar","Onix"])
combinations = list(itertools.combinations(items,k))

for comb in combinations:
    tpl=tuple()
    for j in comb:
        tpl=tpl+tuple(Pokedex[j])
    st=set(tpl)
    tpl=tuple(st)
    length=len(tpl)
    if length>maxx:
        maxx=length
        max_features=tpl
        pokemon_list=comb
print(maxx)
print(max_features)
print(pokemon_list)