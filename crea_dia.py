import psycopg2
from psycopg2.extensions import AsIs
import datetime

dia = datetime.timedelta(days = 1)
conn = psycopg2.connect("host = localhost dbname=afp_scrapper_db user=gonzalo password=gonzalovera26")
cur1  = conn.cursor()

cur1.execute(""" Select fecha from cuprum limit 1;""") #podría haber sido cualquiera
fecha = cur1.fetchone()
#import pdb;pdb.set_trace()
dia_siguiente = fecha[0] + dia


cur1.close()

cur2 = conn.cursor()
fondos = ['A','B','C','D','E']
for f in fondos:
    for afp in ['capital','cuprum','habitat','modelo','planvital','provida','uno']:
        cur2.execute("INSERT INTO %s(fecha, val_cuota, val_pat,status,fondo) VALUES (%s,0,0,False,%s)",(AsIs(afp.lower()),dia_siguiente,f))

conn.commit()
cur2.close()
conn.close()

