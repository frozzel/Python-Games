import prettytable as pt

def table():
    tb = pt.PrettyTable()
    tb.field_names = ["Name", "Age", "Gender"]
    tb.add_row(["Tom", 20, "Male"])
    tb.add_row(["Jerry", 22, "Male"])
    print(tb)
    
table()

def pokemon_table():
    tb = pt.PrettyTable()
    tb.align = "l"
    tb.field_names = ["Pokemon", "Type"]
    tb.add_row(["Pikachu", "Electric"])
    tb.add_row(["Squirtle", "Water"])
    tb.add_row(["Charmander", "Fire"])
    print(tb)
    
pokemon_table()

