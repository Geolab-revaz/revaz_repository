import sqlite3

con = sqlite3.connect('pbase.db')
cur = con.cursor()

production = [   
    ["Test", "Satesto", 99, "Pirveli"],
    ["Test", "Satesto", 99, "Meore"],
    ["Test", "Satesto", 99, "Mesame"],
]    
for i in production:
    cur.execute(f"""
    insert into products (Product, Description, Price,Trademark), values ("{i[0]}", "{i[1]}", {i[2]}, "{i[3]}")
    """)


con.commit()
con.close()