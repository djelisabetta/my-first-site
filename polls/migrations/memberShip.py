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

#
# for i in lista_id_fee:
#     db = MySQLdb.connect("172.21.102.22", "tenancy", "e3i48d.9wGfdsyjwnò", "aci-global-servi-30176b68fc46467")
#     cursor = db.cursor()
#     sql = "INSERT INTO fee_validity_dates(fee_id, date_start, date_end, flag_disabled) VALUES('" + str(i) + "','2019-01-01','2020-12-31','0')"
#     print(sql)
#     try:
#         cursor.execute(sql)
#         print("INSERITA ")
#         db.commit()
#     except:
#         db.rollback()
#         print(db.error())
#     db.close()
#
#
# for a in lista_id_fee:
#     db = MySQLdb.connect("172.21.102.22", "tenancy", "e3i48d.9wGfdsyjwnò", "aci-global-servi-30176b68fc46467")
#     cursor = db.cursor()
#     sql = "SELECT id FROM fee_validity_dates WHERE fee_id=" + str(a) + " LIMIT 1"
#     cursor.execute(sql)
#     ris = cursor.fetchall()
#     db.close()
#     #print(ris)
#     lista_id_fee_validity_dates = list(ris)
#     for i in range(len(lista_id_fee_validity_dates)):
#         lista_id_fee_validity_dates[i]=str(lista_id_fee_validity_dates[i])
#         lista_id_fee_validity_dates[i]=lista_id_fee_validity_dates[i].replace(",", "")
#         lista_id_fee_validity_dates[i]=lista_id_fee_validity_dates[i].replace("(", "")
#         lista_id_fee_validity_dates[i]=lista_id_fee_validity_dates[i].replace(")", "")
#         lista_id_fee_validity_dates1.append(lista_id_fee_validity_dates[i])
#         #txt.replace("bananas", "apples")
#     #print(a,lista_id_fee_validity_dates)
# print(lista_id_fee_validity_dates1)
#
# for a in lista_id_fee:
#     print(a)
#     db = MySQLdb.connect("172.21.102.22", "tenancy", "e3i48d.9wGfdsyjwnò", "aci-global-servi-30176b68fc46467")
#     mycursor = db.cursor()
#     sql = "UPDATE fee_services SET fee_validity_date_id = (SELECT id FROM fee_validity_dates WHERE fee_id=" + str(a) + " LIMIT 1 ) WHERE fee_id=" + str(a) + ""
#     mycursor.execute(sql)
#     db.commit()
#     db.close()
