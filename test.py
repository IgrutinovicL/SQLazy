import SQLazy

structure = {"USERNAME":"VARCHAR(20)","PASSWORD":"VARCHAR(20)","POINTS":"INTEGER"}
vals      = {"USERNAME":"LukaIgrutinovic","PASSWORD":"isCool","POINTS":9001}

conn    = SQLazy.CreateDatabase("test.db")
table   = SQLazy.CreateTable(conn,"testTable",structure)
SQLazy.InsertIntoTable(conn,table,vals)
print("GOT -> ",SQLazy.SearchById(conn,"testTable",1))
SQLazy.UpdateWhereId(conn,"testTable",1,{"USERNAME":"Lukas"})
print(SQLazy.SearchByValue(conn,"testTable","USERNAME","Lukas"))
