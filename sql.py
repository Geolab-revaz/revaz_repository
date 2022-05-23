import sqlite3

con = sqlite3.connect('pbase.db')
cur = con.cursor()

                                    # product = [   
                                    #     ["Test1", 99,"Satesto1", "Pirveli"],
                                    #     ["Test2", 99, "Satesto2", "Meore"],
                                    #     ["Test3", 99, "Satesto3", "Mesame"],
                                    # ]

                                    # cur.execute("""
                                    #     insert into product (pname, price, trademark,description), values (?, ?, ?,?)
                                    #     """, ("Test4", 80, "Satesto5", "Mexute"))

                                    # con.commit()

production = [
    ["Test1", "Satesto1", 99, "Pirveli"],
    ["Test2", "Satesto2", 99,  "Meore"],
    ["Test3", "Satesto3", 99, "Mesame"],
]

cur.execute("""
    insert into production (Product, Description, Price, Trademark), values (?, ?, ?, ?)
    """, ("Test4", "Satesto4", 80, "Meotxe"))

con.commit()


# for i in product:
#     Product = i[0]
#     Description = i[1]
#     Price = i[2]
#     Trademark = i[3]



# cur.execute(""" delete from production where Product=?""", ("Test1",))


# cur.executemany(""" insert into production (Product, Description, Price,Trademark), values (?, ?, ?, ?) """, production)


# cur.execute(f""" update production where Price=? where Trademark=?""", (20,"Testline"))
# con.commit()

# con.close()

# q=cur.execute("""select.count(*) from production wgere prie = 99""")
# print(q.fetchall())

con.close()