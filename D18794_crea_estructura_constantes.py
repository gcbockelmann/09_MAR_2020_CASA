

### CREA VECTOR ESTRUCTURA CONSTANTES

####################################################################
#Crea el vector estructura_constantes
estructura_constantes= { 'Year':0, 
'H1101':0,
'H1102':0,
'H1106':0,
#Plant Inflation Adjustment Trigger Override
#'H1394':0, 
#Land Inflation Adjustment Trigger Override
'H1395':0,
#GNP Land Inflation Adjustment Trigger Override
'H1502GDP':0,
# Variable agregada por German para trackear el GDP de ese pais
'H1502ADD':0,
#
#FIFO Profits Trigger Override
'H1389':0,
'CCLASS':0,
} 


# Toma el vector generico y lo inicializa
#estructura_constantes = constantes2018
for r in estructura_constantes.keys():
    estructura_constantes[r] = 0