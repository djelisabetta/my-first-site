import MySQLdb

def convertTuple(tup):
    str =  ''.join(tup)
    return str

# lista_seriali_for = ['636554','032445','000298','636689','023985','027057','048189','026664','016193','029851','042113','042114','043028','043604','045162','046873','030779','047507','047611','048098','049263','049290']

# lista_seriali_for = ['023184','025923','027493','023979','638046', '000277','000472','000477','047509','048190',
# '636554','032445','000298','636689','023985','027057','048189','026664','016193',
#                      '029851','042113','042114','043028','043604']
lista_seriali_for = ['023184','025923','027493','023979','638046', '000277','000472','000477','047509','048190']

for i in lista_seriali_for:
    # lettura db PREPROD SERVIZI
    supplier_serial=i
    db = MySQLdb.connect("172.21.102.22", "tenancy", "e3i48d.9wGfdsyjwnò", "aci-global-spa-7a94482383c641a9b")
    cursor = db.cursor()
    sql = "SELECT suppliers.*, supplier_legal_entities.serial FROM suppliers INNER JOIN supplier_legal_entities ON suppliers.supplier_legal_entity_id=supplier_legal_entities.id where suppliers.serial="+i+";"

    cursor.execute(sql)
    ris = cursor.fetchall()
    print(sql)
    print(str(ris))
    supplier_id=str(ris[0][0])
    # stampa supplier_id
    print("PREPROD SERVIZI id_supplier & serial: " + supplier_id + " & " + supplier_serial)

    # stampa supplier_legal_entities.serial
    # print("PREPROD SERVIZI supplier_legal_entities.serial "+ris[0][len(ris[0])-1])
    # sql = "SELECT * FROM supplier_legal_entities where serial='"+ str(ris[0][len(ris[0])-1]) +"';"
    # cursor.execute(sql)
    # entita = cursor.fetchall()
    # print("entità legale PREPROD SERVIZI "+str(entita[0]))

    # nb la seguente lista non ritorna records
    # sql = "SELECT * FROM supplier_categories where supplier_id='" + supplier_id + "';"
    # cursor.execute(sql)
    # supplier_categories = cursor.fetchall()
    # # print(supplier_categories[0])
    # lista_supplier_categories = list(supplier_categories)
    # print("PREPROD SERVIZI lista supplier_categories "+str(lista_supplier_categories))

    sql = "SELECT * FROM supplier_operating_hours where supplier_id='" + supplier_id + "';"
    cursor.execute(sql)
    supplier_operating_hours = cursor.fetchall()
    lista_supplier_operating_hours = list(supplier_operating_hours)
    print("PREPROD SERVIZI lista supplier_operating_hours " + str(lista_supplier_operating_hours))

    sql = "SELECT * FROM supplier_operating_roads where supplier_id='" + supplier_id + "';"
    cursor.execute(sql)
    supplier_operating_roads = cursor.fetchall()
    lista_supplier_operating_roads = list(supplier_operating_roads)
    print("PREPROD SERVIZI lista supplier_operating_roads " + str(lista_supplier_operating_roads))

    sql = "SELECT * FROM supplier_phones where supplier_id='" + supplier_id + "';"
    cursor.execute(sql)
    supplier_phones = cursor.fetchall()
    lista_supplier_phones = list(supplier_phones)
    print("PREPROD SERVIZI lista supplier_phones " + str(lista_supplier_phones))

    sql = "SELECT * FROM supplier_services where supplier_id='" + supplier_id + "';"
    cursor.execute(sql)
    supplier_services = cursor.fetchall()
    lista_supplier_services = list(supplier_services)
    #
    # nb il seguente ciclo non ritorna records
    # for supplier_service_item in lista_supplier_services:
    #     print("supplier_service_item id " + str(supplier_service_item[0]))
    #     sql = "SELECT * FROM supplier_service_costs where supplier_service_id=" + str(supplier_service_item[0]) + ";"
    #     cursor.execute(sql)
    #     supplier_service_costs = cursor.fetchall()
    #     lista_supplier_service_costs = list(supplier_service_costs)
    #     print("PREPROD SERVIZI lista supplier_service_costs " + str(lista_supplier_service_costs))

    # nb la seguente lista non ritorna records
    # sql = "SELECT * FROM supplier_staff where supplier_id='" + supplier_id + "';"
    # cursor.execute(sql)
    # supplier_staff = cursor.fetchall()
    # lista_supplier_staff = list(supplier_staff)
    # print("PREPROD SERVIZI lista supplier_staff " + str(lista_supplier_staff))

    db.close()


    # lista_id_fee = list(ris)
    # lettura db PREPROD IH
    db = MySQLdb.connect("172.21.102.22", "tenancy", "e3i48d.9wGfdsyjwnò", "aci-global-servi-30176b68fc46467")
    cursor = db.cursor()

    # entita_serial=str(ris[0][len(ris[0])-1])
    # sql = "SELECT id FROM supplier_legal_entities where serial=" + entita_serial + ";"
    # cursor.execute(sql)
    # ris1 = cursor.fetchall()
    # print(ris1)
    # if len(ris1)==0:
    #     sql = "INSERT INTO supplier_legal_entities(serial, name, vat_number, fiscal_code, address, city, province, cap, phone," \
    #           " email, bank_code, bank_agency_code, bank_agency_description, bank_account) VALUES('" + str(entita[0][2]) + "','" \
    #           + str(entita[0][3]) + "','" + str(entita[0][4]) + "','" + str(entita[0][5]) + "','" + str(entita[0][6]) + "','" \
    #           + str(entita[0][7]) + "','" + str(entita[0][8]) + "','" + str(entita[0][9]) + "','" + str(entita[0][10]) + "','" \
    #           + str(entita[0][11]) + "','" + str(entita[0][12]) + "','" + str(entita[0][13]) + "','" + str(entita[0][14]) + "','" \
    #           + str(entita[0][15]) + "')"
    #     print(sql)
    #     try:
    #         cursor.execute(sql)
    #         print("INSERITA ")
    #         db.commit()
    #     except:
    #         db.rollback()
    #         print(db.error())
    #
    # sql = "SELECT id FROM supplier_legal_entities where serial=" + entita_serial + ";"
    # cursor.execute(sql)
    # id_entita = cursor.fetchall()
    # print("IH id entità legale "+id_entita[0][0])

    sql = "SELECT * FROM suppliers where serial=" + supplier_serial + ";"
    cursor.execute(sql)
    ris = cursor.fetchall()
    ih_supplier_id = str(ris[0][0])
    print("IH id_supplier & serial: " + ih_supplier_id + " & " + supplier_serial)

    for soh_item in lista_supplier_operating_hours:
        sql = "INSERT INTO supplier_operating_hours(supplier_id, weekday_morning_opening, weekday_morning_closing, weekday_afternoon_opening, weekday_afternoon_closing, saturday_morning_opening, saturday_morning_closing, saturday_afternoon_opening, saturday_afternoon_closing," \
              " sunday_morning_opening, sunday_morning_closing, sunday_afternoon_opening, sunday_afternoon_closing) VALUES('" + ih_supplier_id + "','" \
              + str(soh_item[2]) + "','" + str(soh_item[3]) + "','" + str(soh_item[4]) + "','" + str(soh_item[5]) + "','" \
              + str(soh_item[6]) + "','" + str(soh_item[7]) + "','" + str(soh_item[8]) + "','" + str(soh_item[9]) + "','" \
              + str(soh_item[10]) + "','" + str(soh_item[11]) + "','" + str(soh_item[12]) + "','" + str(soh_item[13]) + "')"
        print(sql)
        try:
            cursor.execute(sql)
            print("INSERITA ")
            db.commit()
        except:
            db.rollback()
            print(db.error())


    for soh_item in lista_supplier_operating_roads:
        sql = "INSERT INTO supplier_operating_roads(supplier_id, light_motorway, heavy_motorway, light_ordinary, heavy_ordinary) VALUES('" + ih_supplier_id + "','" \
              + str(soh_item[2]) + "','" + str(soh_item[3]) + "','" + str(soh_item[4]) + "','" + str(soh_item[5])  + "')"
        print(sql)
        try:
            cursor.execute(sql)
            print("INSERITA ")
            db.commit()
        except:
            db.rollback()
            print(db.error())


    for soh_item in lista_supplier_phones:
        sql = "INSERT INTO supplier_phones(supplier_id, phone, note) VALUES('" + ih_supplier_id + "','" \
              + str(soh_item[2]) + "','" + str(soh_item[3])  + "')"
        print(sql)
        try:
            cursor.execute(sql)
            print("INSERITA ")
            db.commit()
        except:
            db.rollback()
            print(db.error())

    for soh_item in lista_supplier_services:
        sql = "INSERT INTO supplier_services(supplier_id, service_id) VALUES('" + ih_supplier_id + "','" \
              + str(soh_item[2])  + "')"
        print(sql)
        try:
            cursor.execute(sql)
            print("INSERITA ")
            db.commit()
        except:
            db.rollback()
            print(db.error())