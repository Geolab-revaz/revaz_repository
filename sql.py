import sqlite3

con = sqlite3.connect('pbase.db')
cur = con.cursor()

# production = [   
# ]    

# cur.execute("""
# insert into products (Product, Description, Price,Trademark), values ("Test, Satesto, 99,pirveli)
# """)


# con.commit()
# con.close()