#PROGRAMA EN PYTHON QUE PERMITA GESTIONAR UN PRESTANO TENIENDO EN CUENTA LO SIGUIENTE:
#Cliente:nombre,contacto
#prestamo:? -plazo:? (6(5%),12(10%),24(),36()meses)
#capa de desc: salario * 0.60
import os
var_nombreStr = input('Nombre')
var_contactoStr = input('Contacto')
var_salarioStr = float(input('Salario'))
var_plazoInt = int(input(' -- Plazo--\n\n1. 6 meses\n2. 12 meses\n3. 24 meses\n4. 36 meses\n->'))
var_capacidad_descuentoFlt = var_salarioStr * 0.60
var_montoFlt = float(input('Monto a prestar ->'))
if var_plazoInt == 1:
    var_interesesFlt = var_montoFlt * 0.05
    var_porcentajeStr = '5%'
    var_opcionInt =6
    
if var_plazoInt == 2:
    var_interesesFlt = var_montoFlt * 0.10
    var_porcentajeStr = '10%'
    var_opcionInt = 12
    
if var_plazoInt == 3:
    var_interesesFlt = var_montoFlt * 0.15
    var_porcentajeStr = '15%'
    var_opcionInt = 24
    
if var_plazoInt == 4:
    var_interesesFlt = var_montoFlt * 0.20
    var_porcentajeStr = '20%'
    var_opcionInt = 36
    
var_totalprestamoFlt = var_montoFlt + var_interesesFlt 
var_cuota = var_totalprestamoFlt / var_opcionInt 

os.system('cls')
print('<<<REPORTE DEL CRÉDITO>>>\n')
print('NOMBRE DEL CLIENTE..........',var_nombreStr)
print('CONTACTO....................',var_contactoStr)
print('CAPACIDAD DE DESCUENTO......',var_capacidad_descuentoFlt)
print('MONTO SOLICITADO............',var_montoFlt)
print('INTERSES....................',var_interesesFlt)
print('PLAZO.......................',var_opcionInt)
print('PORCENTAJE DE INTESES........',var_porcentajeStr)
print('CUOTA........................',var_cuota)
print('TOTAL A PAGAR................',var_totalprestamoFlt)
if var_cuota <= var_capacidad_descuentoFlt :
    print('tu credito ha sido aprobado')
else :
    print('tu credito no ha sido aprobado')
                          