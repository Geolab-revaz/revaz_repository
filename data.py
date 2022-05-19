import sqlite3
production = [ 
        {
            "Product":"Antibacterial Soap",
            "Description": "Green Apple, 500 gr",
            "Price":9,
            "Trademark": "Labline",
        },
        {
            "Product":"Antibacterial Soap",
            "Description": "Raspberry, 900 gr",
            "Price":12,
            "Trademark": "Labline",
        },
        {
            "Product":"Septomed",
            "Description": "Disinfectant, 1000 ml",
            "Price":16,
            "Trademark": "Labline",
        },
]

con = sqlite3.connect('project.db')
cur = con.cursor()

cur.execute("""
    create table work (
        Product TEXT,
        Description TEXT,
        Price TEXT,
        Trademark TEXT
    )
""")

con.commit()


for i in production:
    cur.execute(""" insert into production (Product, Description, Price, Trademark) values (?,?,?,?)""", 
    (i.get('Product'), i.get('Description'), i.get('Price'), i.get('Trademark')  ))
    con.commit()

con.close()