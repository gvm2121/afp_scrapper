

extraido = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n\n<html>\n<head>\n<title>Superintendencia de Pensiones - Valores de Cuota y del Patrimonio Fondo Tipo A</title>\n<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">\n<link type="text/css" rel="stylesheet" href="/css/appscreen.css">\n<script type="text/javascript" src="/javascript/functions.js"></script>\n\n\n</head>\n\n\n\n<div class="col-sm-8 col-sm-offset-1 col-xs-9">\n  <h1 class="page_header">Valores de Cuota y del Patrimonio Fondo Tipo A<br /></h1>\n</div>\n<script type="text/javascript" src="/css/proxy_js_frag_v12.php?context=bootstrap&frag=header_nav&title=Valores de Cuota y del Patrimonio Fondo Tipo A<br />&miga=sp_ef_effp_ef"></script>\n\n<style>\nbody\t{\n   font-size: 14px;\n}\n\na:link\t{\n   text-decoration: none;\n   color: #417AC2;\n}\n\n#menu_selector_menu li {\n   display: inline;\n   list-style-type: none;\n   padding-right: 20px;\n}\n\n#menu_selector_menu li.selected\n{\n   background-color: #FFFFCC;\n}\n</style>\n\n\n\n<br>\n<table width="500">\n<tbody>\n<tr>\n<td><span><b>Valores de Cuota y Fondo</b></span></td>\n<td align="right"><div id="divid"><a href="/apps/vMonetarios.php"><b>Valores Monetarios</b></a></div>\n</td>\n</tr>\n</tbody>\n</table>\n<br />\n\n\n\n<form>\n<div class="col-sm-12 col-xs-3 text-left">\n\t<button class="btn btn-default" value=\'A\' name=\'A\' type="button" onclick="javascript:window.open(\'vcfAFP.php?tf=A\', \'_self\');">\n\t\t<span class="hidden-xxs">Tipo A</span>\n\t<button class="btn btn-default" value=\'B\' name=\'B\' type="button" onclick="javascript:window.open(\'vcfAFP.php?tf=B\', \'_self\');">\n\t\t<span class="hidden-xxs">Tipo B</span>\n\t<button class="btn btn-default" value=\'C\' name=\'C\' type="button" onclick="javascript:window.open(\'vcfAFP.php?tf=C\', \'_self\');">\n\t\t<span class="hidden-xxs">Tipo C</span>\n\t<button class="btn btn-default" value=\'D\' name=\'D\' type="button" onclick="javascript:window.open(\'vcfAFP.php?tf=D\', \'_self\');">\n\t\t<span class="hidden-xxs">Tipo D</span>\n\t<button class="btn btn-default" value=\'E\' name=\'E\' type="button" onclick="javascript:window.open(\'vcfAFP.php?tf=E\', \'_self\');">\n\t\t<span class="hidden-xxs">Tipo E</span>\n\t<button class="btn btn-default" value=\'FC\' name=\'fc\' type="button" onclick="javascript:window.open(\'vcfAFC.php\', \'_self\');">\n\t\t<span class="hidden-xxs">Fondos de Cesant&iacute;a</span>\n</div>\n</form>\n<br> </br>\n\n\n<script language=\'JavaScript\'>\nfunction generaXLS()\n{\n   aaaaini = document.genxls.aaaaini[document.genxls.aaaaini.selectedIndex].value;\n   aaaafin = document.genxls.aaaafin[document.genxls.aaaafin.selectedIndex].value;\n\n   if ( aaaaini > aaaafin ) {\n      alert( "A??o de inicio debe ser anterior al de t??rmino" );\n      return;\n   }\n\n   getParams="aaaaini="+aaaaini+"&aaaafin="+aaaafin+"&tf=A&fecconf=20220228"\n   document.location.href="vcfAFPxls.php?"+getParams;\n}\nfunction busca_dias(objeto)\n{\n  ann = document.vcf.aaaa.value;\n  mm = objeto.value;\n  dd = diasmes(mm,ann);\n // alert(dd);\n  document.vcf.dd.length = dd;\n  j = 1;\n  for (i=0;i<dd;i++)\n  {\n    if(j<10)\n       num = \'0\'+j;\n    else  \n       num = j;\n     document.vcf.dd.options[i].text = num;\n    j++;\n  }\n  document.vcf.dd.selectedIndex = 0;\n}\n\nfunction diasmes(mm, ann) \n{\n  return new Date(ann || new Date().getFullYear(), mm, 0).getDate();\n}\n</script>\n\n\n<br>\n\n   <form  name="vcf" method="post" action="vcfAFP.php?tf=A" >\n   <table class="table table-striped table-hover table-bordered table-condensed">\n   <tr >\n   <th  colspan="2" ><center>Valores de Cuota y del Patrimonio Fondo Tipo A</center></th>\n   </tr>\n\n   <tr>\n   <th><center>Confirmados hasta</center></th>\n   <th><center>Disponibles hasta</center></th>\n   </tr>\n\n   <tr>\n   <th><center>28-FEB-2022</center></th>\n   <th><center>07-MAR-2022</center></th>\n   </tr>\n\n   <tr>\n   <td colspan=\'2\'><center>\n      <table border=\'0\'>\n      <tr>\n      <td align=\'left\'>&nbsp;&nbsp;<INPUT  type="submit" value="<<" name="btn" class="btn btn-default"><span class="fa fa-angle-right"></span></td>\n      <td align=\'center\'>\n         <select  name="aaaa" size="1"\n             onChange="document.getElementById(\'anofin\').innerHTML=this.value;\n                       document.genxls.aaaafin.selectedIndex = document.vcf.aaaa.selectedIndex; ">\n         <option value="2022" selected="selected">2022</option>\n<option value="2021">2021</option>\n<option value="2020">2020</option>\n<option value="2019">2019</option>\n<option value="2018">2018</option>\n<option value="2017">2017</option>\n<option value="2016">2016</option>\n<option value="2015">2015</option>\n<option value="2014">2014</option>\n<option value="2013">2013</option>\n<option value="2012">2012</option>\n<option value="2011">2011</option>\n<option value="2010">2010</option>\n<option value="2009">2009</option>\n<option value="2008">2008</option>\n<option value="2007">2007</option>\n<option value="2006">2006</option>\n<option value="2005">2005</option>\n<option value="2004">2004</option>\n<option value="2003">2003</option>\n<option value="2002">2002</option>\n\n         </select>\n         <select name="mm" size="1" onchange="busca_dias(this);">\n         <option value="01">Enero</option>\n<option value="02">Febrero</option>\n<option value="03" selected="selected">Marzo</option>\n<option value="04">Abril</option>\n<option value="05">Mayo</option>\n<option value="06">Junio</option>\n<option value="07">Julio</option>\n<option value="08">Agosto</option>\n<option value="09">Septiembre</option>\n<option value="10">Octubre</option>\n<option value="11">Noviembre</option>\n<option value="12">Diciembre</option>\n\n         </select>\n\n         <select name="dd" sise="1" >\n         <option value="01">01</option>\n<option value="02">02</option>\n<option value="03">03</option>\n<option value="04">04</option>\n<option value="05">05</option>\n<option value="06">06</option>\n<option value="07" selected="selected">07</option>\n<option value="08">08</option>\n<option value="09">09</option>\n<option value="10">10</option>\n<option value="11">11</option>\n<option value="12">12</option>\n<option value="13">13</option>\n<option value="14">14</option>\n<option value="15">15</option>\n<option value="16">16</option>\n<option value="17">17</option>\n<option value="18">18</option>\n<option value="19">19</option>\n<option value="20">20</option>\n<option value="21">21</option>\n<option value="22">22</option>\n<option value="23">23</option>\n<option value="24">24</option>\n<option value="25">25</option>\n<option value="26">26</option>\n<option value="27">27</option>\n<option value="28">28</option>\n<option value="29">29</option>\n<option value="30">30</option>\n<option value="31">31</option>\n\n         </select>\n         <INPUT  type="submit" value="Buscar" name="btn" class="btn btn-default btn-sm pull-center" >\n      </td>\n      <td align=\'right\'>&nbsp;&nbsp;<INPUT  type="submit" value="&gt;&gt;" name="btn" class="btn btn-default"><span class="fa fa-angle-left"></span></td>\n      </tr>\n      </table>\n   </center></td>\n   </tr>\n   </table>\n   </form>\n</td>\n</tr>\n</table>\n\n\t<table class="table table-striped table-hover table-bordered table-condensed">\n\n       <tr >\n       <th colspan="3" ><center>07-Marzo-2022\n       <br>Valores Provisorios - Sujetos a Confirmaci&oacute;n\t   </center>\n       </th>\n       </tr>\n\n       <tr >\n       <th ><center>A.F.P.</center></th>\n       <th ><center>Valor Cuota&nbsp;</center></th>\n       <th ><center>Valor del Patrimonio&nbsp;</center></th>\n       </tr>\n\n                        <tr>\n\t  \t     \t            <td class="alignLeft">CAPITAL</td>\n          <td align="right">(*)&nbsp;</td>\n          <td align="right">(*)&nbsp;</td>\n          </tr>\n                 <tr>\n\t  \t     \t            <td class="alignLeft">CUPRUM</td>\n          <td align="right">(*)&nbsp;</td>\n          <td align="right">(*)&nbsp;</td>\n          </tr>\n                 <tr>\n\t            <td class="alignLeft">HABITAT</td>\n          <td align="right">58.588,65&nbsp;</td>\n          <td align="right">6.542.437.025.867&nbsp;</td>\n          </tr>\n                 <tr>\n\t            <td class="alignLeft">MODELO</td>\n          <td align="right">56.064,76&nbsp;</td>\n          <td align="right">1.275.007.939.277&nbsp;</td>\n          </tr>\n                 <tr>\n\t  \t     \t            <td class="alignLeft">PLANVITAL</td>\n          <td align="right">(*)&nbsp;</td>\n          <td align="right">(*)&nbsp;</td>\n          </tr>\n                 <tr>\n\t  \t     \t            <td class="alignLeft">PROVIDA</td>\n          <td align="right">(*)&nbsp;</td>\n          <td align="right">(*)&nbsp;</td>\n          </tr>\n                 <tr>\n\t  \t     \t            <td class="alignLeft">UNO</td>\n          <td align="right">(*)&nbsp;</td>\n          <td align="right">(*)&nbsp;</td>\n          </tr>\n       \n                 <tr>\n          <td colspan=\'2\' align="right"><strong>TOTAL</strong></td>\n          <td align="right" ><strong>7.817.444.965.144&nbsp;<strong></td>\n          </tr>\n          <tr>\n   <td colspan=\'3\' align=\'center\' valign=\'middle\'>\n      <table width=\'90%\' border=\'0\' cellspacing="0" cellpadding="0">\n      <form name=\'genxls\'>\n      <tr>\n      <td align=\'center\'>\n         <select  name="aaaaini" size="1" class="CONTENIDOtres"\n            onChange="document.getElementById(\'anoini\').innerHTML=this.value;">\n         <option label="" value="0000" SELECTED></option>\n         <option value="2022">2022</option>\n<option value="2021">2021</option>\n<option value="2020">2020</option>\n<option value="2019">2019</option>\n<option value="2018">2018</option>\n<option value="2017">2017</option>\n<option value="2016">2016</option>\n<option value="2015">2015</option>\n<option value="2014">2014</option>\n<option value="2013">2013</option>\n<option value="2012">2012</option>\n<option value="2011">2011</option>\n<option value="2010">2010</option>\n<option value="2009">2009</option>\n<option value="2008">2008</option>\n<option value="2007">2007</option>\n<option value="2006">2006</option>\n<option value="2005">2005</option>\n<option value="2004">2004</option>\n<option value="2003">2003</option>\n<option value="2002">2002</option>\n\n         </select>\n      </td>\n      <td align=\'center\' width=\'40\'><div class=\'CONTENIDOdos\' id=\'anoini\'>&nbsp;</td>\n\n      <td align=\'center\' width=\'22\'>\n      <A HREF="javascript:generaXLS();"\n         TITLE="Genera archivo en formato CSV con los valores correspondientes al rango de a&ntilde;os seleccionado"><img src=\'/apps/images/xls.gif\' valign=\'top\' border=\'0\'></A>\n      </td>\n\n      <td align=\'center\' width=\'40\'><span class=\'CONTENIDOdos\' id=\'anofin\'>2022</span></td>\n\n      <td align=\'center\'>\n         <select  name="aaaafin" size="1" class="CONTENIDOtres"\n            onChange="document.getElementById(\'anofin\').innerHTML=this.value;">\n         <option value="2022" selected="selected">2022</option>\n<option value="2021">2021</option>\n<option value="2020">2020</option>\n<option value="2019">2019</option>\n<option value="2018">2018</option>\n<option value="2017">2017</option>\n<option value="2016">2016</option>\n<option value="2015">2015</option>\n<option value="2014">2014</option>\n<option value="2013">2013</option>\n<option value="2012">2012</option>\n<option value="2011">2011</option>\n<option value="2010">2010</option>\n<option value="2009">2009</option>\n<option value="2008">2008</option>\n<option value="2007">2007</option>\n<option value="2006">2006</option>\n<option value="2005">2005</option>\n<option value="2004">2004</option>\n<option value="2003">2003</option>\n<option value="2002">2002</option>\n\n         </select>\n      </td>\n      </tr>\n      </form>\n      </table>\n   </td>\n   </tr>\n</table>\n<br > </br>\n<span>\n       Archivos en formato CSV: genera un archivo con los valores correspondiente al rango de a&ntilde;os\n       especificado, considerando las AFP vigentes al primer d&iacute;a de cada mes.\n</span>\n\n<br></br>\n(*) Las AFP tienen plazo para enviar a esta Superintendencia el Informe Diario de los Fondos de Pensiones, el cual entre otra informaci&oacute;n contiene el valor de la cuota y de los fondos, hasta las 24 horas del d&iacute;a h&aacute;bil siguiente, una vez recepcionado el Informe en forma correcta, el valor cuota queda disponible en el sitio Web de la Superintendencia. Por ejemplo, el Informe Diario correspondiente al d&iacute;a jueves 01 de marzo de 2018 es recepcionado hasta las 24 horas del d&iacute;a viernes 02 de marzo de 2018. Libro IV, T&iacute;tulo VIII, Cap&iacute;tulo III, n&uacute;mero 2 del Compendio de Pensiones.\n\n<br > </br>\n<span>\n<A HREF="./grafAFP.php" class="contenidos">\nGr&aacute;ficos de Evoluci&oacute;n del Valor Nominal de la Cuota</A>\n</A>\n</span>\n\n\n<br > </br>\n<span>\n  Sr. Usuario: Si usted desea conocer la forma en que se calcula diariamente el Valor Cuota de su Fondo de Pensiones, favor presionar el siguiente\n  <A HREF="/apps/valoresCuotaFondo/calculaCuofon.php" class="contenidos">\n  link</A>. En &eacute;l, se indica paso a paso la forma de c&aacute;lculo, present&aacute;ndole adem&aacute;s, el valor de cada uno de los conceptos que participan en la determinaci&oacute;n de dicho valor cuota.\n</span>\n<hr>\n<div class="col-sm-12 col-xs-3 text-right">\n<button class="btn btn-default btn-sm pull-right" type="button" onclick="window.history.back();">\n<span class="fa fa-arrow-left"></span> <span class="hidden-xxs">Volver</span>\n</button>\n</div>\n\n<script type="text/javascript" src=\'/css/proxy_js_frag_v11.php?context=bootstrap&frag=footer\'></script>\n\n</body>\n</html>\n'

import psycopg2
import requests
from psycopg2.extensions import AsIs
from bs4 import BeautifulSoup as b
import re
import datetime as dt

#s = b(extraido,"html.parser")
# segunda idea.
# hay que hacer 2 cronJobs, 1 que inicialize el d??a(Insert) y otro que llene los datos (Update)
# se segundo cron buscar??, dentro de la base de datos y del dia, algun false. Si lo encuentra corre el update otra vez, cada 2 o 4 hrs. Si no 
# encuentra ningun false, no hace nada porque se entiende que todos los datos ya est??n dentro y correctos.

#buscamos si la fecha est?? en la base de datos
conn = psycopg2.connect("host = localhost dbname=afp_scrapper_db user=gonzalo password=gonzalovera26")
cur  = conn.cursor()
#fecha_en_la_base = cur.execute()
cur.execute("""SELECT * FROM capital ca,cuprum cu ,habitat ha ,modelo mo ,planvital pl,provida pr ,uno u where ca.status=False OR cu.status = False OR ha.status = False OR mo.status = False OR pl.status = False OR pr.status = False OR u.status = False; """)


hay_falsos = True if False in cur.fetchone() else False

cur.close()

if hay_falsos:
    fondos = ['A','B','C','D','E']
    for f in fondos:
        url = 'https://www.spensiones.cl/apps/valoresCuotaFondo/vcfAFP.php?tf=' + f
        extraido = requests.get(url)
        s = b(extraido.text,"html.parser")
        #s = b(extraido,"html.parser")

        tablas = s.find_all('table')
        tabla_con_datos = tablas[3]
        tds = tabla_con_datos.find_all("td")

        #ac?? hay que sacar las otras afps y los valoes cuotas y patrimonios
        primer_afp = tds[0].get_text()

        meses = {
            'Enero':'01',
            'Febrero':'02',
            'Marzo':'03',
            'Abril':'04',
            'Mayo':'05',
            'Junio':'06',
            'julio':'07',
            'Agosto':'08',
            'Septiembre':'09',
            'Octubre':'10',
            'Noviembre':'11',
            'Diciembre':'12',
            }



        fecha = tabla_con_datos.th
        fecha_texto = fecha.get_text()
        fecha_final = re.search('\d{2}-\D+-\d{4}',fecha_texto)[0]
        mes = fecha_final.split('-')[1]
        f1 = fecha_final.replace(mes,meses[mes])
        dt_1 = dt.datetime.strptime(f1,"%d-%m-%Y")
        for i in range(0,19,3):
            AFP = tds[i].get_text()
            AFP_val_cuota = tds[i+1].get_text() if tds[i+1].get_text() !='(*)??' else '0'
            AFP_pat = tds[i+2].get_text() if tds[i+1].get_text() !='(*)??' else '0'
            AFP_val_cuota = AFP_val_cuota.replace('.','').replace(',','.').replace(u'\xa0',u'')
            AFP_pat = AFP_pat.replace('.','').replace(',','.').replace(u'\xa0',u'')
            status_aux = False if AFP_val_cuota == '0' or AFP_pat == '0' else True
            #cur.execute("INSERT INTO %s(fecha, val_cuota, val_pat,status,fondo) VALUES (%s,%s,%s,%s,%s)",(AsIs(AFP.lower()),dt_1,float(AFP_val_cuota),int(AFP_pat),status_aux,f))
            conn.commit()


    cur.close()
    conn.close()







