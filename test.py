import SQLazy

structure = {"USERNAME":"VARCHAR(20)","PASSWORD":"VARCHAR(20)","POINTS":"INTEGER"}
# Create a structure for the database. ^

vals      = {"USERNAME":"LukaIgrutinovic","PASSWORD":"isCool","POINTS":9001}
# Crate values to insert into the databae. ^

conn    = SQLazy.CreateDatabase("test.db")
# Create an empty database. ^

table   = SQLazy.CreateTable(conn,"testTable",structure)
# Create an empty table with the given structure. ^

SQLazy.InsertIntoTable(conn,table,vals)
# Populate the table with given values. ^

print("GOT -> ",SQLazy.SearchById(conn,"testTable",1))
# Test to see if the table has been populated with our given values. ^

SQLazy.UpdateWhereId(conn,"testTable",1,{"USERNAME":"Lukas"})
# Update the table with our given values. ^

print(SQLazy.SearchByValue(conn,"testTable","USERNAME","Lukas"))
# Test out the search by value feature.
