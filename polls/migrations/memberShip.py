import MySQLdb

def convertTuple(tup):
    str =  ''.join(tup)
    return str

lista_id_fee = []
lista_id_fee_validity_dates = []
lista_id_fee_validity_dates1 = []

db = MySQLdb.connect("172.21.102.22", "tenancy", "e3i48d.9wGfdsyjwnò", "aci-global-spa-7a94482383c641a9b")
cursor = db.cursor()
sql = "SELECT suppliers.serial FROM suppliers INNER JOIN network_memberships ON suppliers.id=network_memberships.supplier_id where network_id=422;"

cursor.execute(sql)
ris = cursor.fetchall()
db.close()


lista_id_fee = list(ris)
db = MySQLdb.connect("172.21.102.22", "tenancy", "e3i48d.9wGfdsyjwnò", "aci-global-servi-30176b68fc46467")
cursor = db.cursor()
for i in lista_id_fee:
    str1 = convertTuple(i)
    sql = "SELECT id FROM suppliers where serial=" + str1 + ";"
    cursor.execute(sql)
    ris1 = cursor.fetchall()


    if len(ris1) == 0:
        print("Seriale non trovato " + str1)
    else:
        sql = "SELECT id FROM network_memberships where network_id=422 AND supplier_id='" + str(ris1[0][0]) + "';"
        cursor.execute(sql)
        ris2 = cursor.fetchall()

        if len(ris2) == 0:
            sql = "INSERT INTO network_memberships(network_id,supplier_id) VALUES('422'," + str(ris1[0][0]) + ")"
            try:
                cursor.execute(sql)
                # print("inserito "+str(ris1[0][0]))
                db.commit()
            except:
                print("errore " + str(ris1[0][0]))
                db.rollback()

db.close()


