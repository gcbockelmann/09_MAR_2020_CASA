### ACTUALIZA SERIE DE PRECIOS CORRIENTE HISTORICA
def update(ticker):
    ### Esta funcion actualiza la serie de precios corrientes historica de un ticker con la data nueva de bolsar
    ### El ticker se debe ingresar como una string
    global df
    filename2 = str ("SERIE_CORRIENTE_" + ticker)   
    #borrar print (filename2)       
    idata = open_excel(original_source +"\INPUT", ticker, ".xlsx")
    if isinstance(idata, pd.DataFrame) == False:
        print("La serie de " + str(ticker) + " no fue actualizada")
    else: 
        idata = serie_de_tiempo(idata)
        idata = formateo_input_bolsar_equity(idata)
        ispch = open_file_spch(original_source + "\SPCH", filename2 , ".xlsx")
        #Para checkear que las 2 listas de nombres son iguales > al devolver True.
        if list(ispch.columns) == list(idata.columns):
           #Esta funcion concatena dos dataframes (supongo que de igual cantidad y mismo nombre de columnas) y luego dropea las rows duplicadas
           #la matriz a grabar se pone en df para poder nutrir a la funcion de guardado
           df = pd.concat([ispch,idata]).drop_duplicates()
           df = df.sort_index()       
           df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
           #
           # Eliminacion de duplicados del indice
           #
           # 1. Reseteo el indice para poder operar sobre las columnas    
           df = df.reset_index()
           # 2. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
           df = df.drop_duplicates(subset='Fecha', keep='last')
           # 3. Vuelvo a establecer la columna fecha como indice
           df = df.set_index('Fecha', inplace=False)
           #
           equities_list = ['AGRO', 'ALUA', 'APBR', 'AUSO', 'BBAR', 'BHIP', 'BMA', 'BOLT', 'BPAT', 'BRIO6', 'BRIO', 'BYMA', 'CADO', 'CAPX', 'CARC', 'CECO2', 'CELU', 'CEPU', 'CGPA2', 'COME', 'CRES', 'CTIO', 'CVH', 'DGCU2', 'DOME', 'DYCA', 'EDN', 'FERR', 'FIPL', 'GAMI', 'GARO', 'GBAN', 'GCLA', 'GGAL', 'GRIM', 'HARG', 'HAVA', 'INDU', 'INTR', 'INVJ', 'IRCP', 'IRSA', 'LEDE', 'LOMA', 'LONG', 'METR', 'MIRG', 'MOLA5', 'MOLA', 'MOLI5', 'MOLI', 'MORI', 'OEST', 'PAMP', 'PATA', 'PATY', 'PGR', 'POLL', 'RICH', 'RIGO', 'ROSE', 'SAMI', 'SEMI', 'SUPV', 'TECO2', 'TGLT', 'TGNO4', 'TGSU2', 'TRAN', 'TS', 'TXAR', 'VALO', 'YPFD']
           #
           bonos_list = ['A2E2', 'A2E2C', 'A2E2D', 'A2E3', 'A2E3C', 'A2E3D', 'A2E7', 'A2E7C', 'A2E7D', 'A2E8', 'A2E8C', 'A2E8D', 'A2J9C', 'A2J9D', 'A2M2', 'A2M2C', 'AA17C', 'AA17D', 'AA19C', 'AA19D', 'AA21', 'AA21C', 'AA21D', 'AA22', 'AA22C', 'AA22D', 'AA25', 'AA25C', 'AA25D', 'AA26', 'AA26C', 'AA26D', 'AA37', 'AA37C', 'AA37D', 'AA46', 'AA46C', 'AA46D', 'AC17', 'AC17C', 'AC17D', 'AD16C', 'AD16D', 'AE14C', 'AE28', 'AE48', 'AE48C', 'AE48D', 'AF17C', 'AF17D', 'AF20', 'AF20C', 'AF20D', 'AL16D', 'AL28', 'AL28C', 'AL28D', 'AL36', 'AL36C', 'AL36D', 'AM18C', 'AM18D', 'AM20', 'AM20C', 'AM20D', 'AMX8D', 'AMX9C', 'AN18C', 'AN18D', 'AO16C', 'AO16D', 'AO17C', 'AO20', 'AO20C', 'AO20D', 'AS13C', 'AS13D', 'AS15C', 'AS17D', 'AY24', 'AY24C', 'AY24D', 'BACX1', 'BB2N9', 'BB2S9', 'BBA20', 'BBF20', 'BBN19', 'BBO19', 'BCD19', 'BCDF1', 'BCFD1', 'BCFM1', 'BCHD1', 'BCHD2', 'BCHD3', 'BCMR', 'BCN16', 'BD2C0', 'BD2C9', 'BD3C0', 'BDC20', 'BDC22', 'BDC24', 'BDC28', 'BDEDD', 'BGBX1', 'BNF21', 'BNS20', 'BOHI1', 'BORD1', 'BORN1', 'BP15C', 'BP18C', 'BP18D', 'BP21', 'BP21C', 'BP21D', 'BP28', 'BP28C', 'BP28D', 'BPLD', 'BPLDC', 'BPLDD', 'BPLE', 'BPLED', 'BPMD', 'BPMDD', 'BPME', 'BRD19', 'BRN20', 'BT02', 'BT03', 'BX92', 'CH24D', 'CHAQ', 'CHSG1', 'CO21D', 'CO24D', 'CO26', 'CO26D', 'CO27D', 'CUAP', 'DIA0', 'DIA0C', 'DIA0D', 'DICA', 'DICAC', 'DICAD', 'DICE', 'DICP', 'DICPC', 'DICPD', 'DICY', 'DICYC', 'DICYD', 'DIE0', 'DIP0', 'DISD', 'DIY0', 'DIY0D', 'EF07', 'ERF25', 'EY28', 'FERB1', 'FORM1', 'FORM2', 'FORM3', 'FRB', 'GA09', 'GD03', 'GD03C', 'GD05', 'GD08', 'GE17', 'GF12', 'GF19', 'GF20', 'GJ15', 'GJ17C', 'GJ17D', 'GJ18', 'GJ31', 'GL30', 'GM10', 'GO06', 'GPBX2', 'GPBX7', 'GS27', 'H27L6', 'JUS22', 'L2DN7', 'NDT11', 'NF18C', 'NO20', 'NRH2', 'NRH2C', 'PAA0', 'PAA0D', 'PAE0', 'PAP0', 'PARA', 'PARAC', 'PARAD', 'PARD', 'PARE', 'PARP', 'PARPC', 'PARPD', 'PARY', 'PARYC', 'PARYD', 'PAY0', 'PAY0D', 'PAY5', 'PBA25', 'PBD19', 'PBF23', 'PBJ21', 'PBJ27', 'PBM24', 'PBY22', 'PMJ21', 'PMY24', 'PR10', 'PR13', 'PR15', 'PR15C', 'PRE3', 'PRE4', 'PRE6', 'PRO1', 'PRO2', 'PRO3', 'PRO4', 'PRO5', 'PRO6', 'PRO8', 'PRO9', 'PUL26', 'PUM21', 'PUO19', 'PUY23', 'PX10', 'PX13', 'PX14', 'PX21', 'RA13D', 'RC21', 'RIF25', 'RN20', 'RNA21', 'RNG22', 'RNG23', 'RO15C', 'RO15D', 'RV05', 'S11O9', 'S13S9', 'S15N9', 'S28F0', 'S29Y0', 'S30A0', 'S30G9', 'S30S9', 'S31L0', 'S31O9', 'SA21', 'SA24D', 'SARH', 'SF07', 'SL02', 'TC20', 'TC20C', 'TC20D', 'TC21', 'TC21C', 'TC21D', 'TC23', 'TC23D', 'TC25P', 'TFU27', 'TJ20', 'TJ20C', 'TJ20D', 'TN20', 'TO21', 'TO21C', 'TO23', 'TO26', 'TO26C', 'TPMS', 'TS27', 'TSEX5', 'TTUX2', 'TUCS3', 'TUCU2', 'TVPA', 'TVPAC', 'TVPAD', 'TVPE', 'TVPED', 'TVPP', 'TVPPC', 'TVPPD', 'TVPY', 'TVPYC', 'TVPYD', 'TVY0', 'TVY0C', 'TVY0D', 'TY03', 'TY04', 'TY05', 'TY06', 'U11O9', 'U13S9', 'U14F0', 'U15N9', 'U17E0', 'U20D9', 'U25O9', 'U26L9', 'U27S9', 'U28F0', 'U29N9', 'U30G9', 'U31E0', 'V03O9', 'V04D9', 'V04S9', 'V05N9', 'VBL6', 'VE02', 'VEA2', 'VEF4', 'VEO2', 'VEY4', 'X2E2', 'X2E7', 'X30G9', 'X30S9', 'XA21', 'XA26', 'XA46', 'XL36', 'ZO03', 'ZO04']
           #
           cedears_list = ['GOLD', 'VALE'] 
           # Graba el archivo
           if ticker in equities_list:
              save_file_generico(df, original_source + "\OUTPUT\EQUITIES", "SERIE_CORRIENTE_", ticker, ".xlsx")
           elif ticker in bonos_list:
              save_file_generico(df, original_source +"\OUTPUT\BONOS", "SERIE_CORRIENTE_", ticker, ".xlsx")
           elif ticker in cedears_list:
              save_file_generico(df, original_source +"\OUTPUT\CEDEARS", "SERIE_CORRIENTE_", ticker, ".xlsx")
           else:
              print ("Problema la lista de nombres de columnas no coincide")
              print ("O ticker no incluido en la lista dentro de la funcion update")
        else:
           print
           print ("Serie Incorrecta")
           print (idata.columns)
           print ("Serie Correcta - SPCH")
           print (ispch.columns)
           print ("Problema en los nombres de las columnas. Los nombres de las columnas no coinciden")                    
        return





#MANUAL UPDATE BOLSAR
#open_excel("C:\GCB_CAPITAL2\INPUT", "ALUA", ".xlsx")
#df = serie_de_tiempo(df)
#df2 = formateo_input_bolsar_equity(df)
#df = open_file_spch("C:\GCB_CAPITAL\SPCH", "SERIE_CORRIENTE_AGRO", ".xlsx")
#list(df.columns) == list(df2.columns)
#df = pd.concat([df,df2]).drop_duplicates()
#save_file("C:\GCB_CAPITAL\OUTPUT", "AGRO", ".xlsx")


#open_file_versatil("C:\GCB_CAPITAL\INPUT", "BOLT", ".xlsx")
#serie_de_tiempo(df)
#df2 = formateo_input_bolsar(df)
#df = open_file_spch("C:\GCB_CAPITAL\SPCH", "SERIE_CORRIENTE_BOLT", ".xlsx")
#list(df.columns) == list(df2.columns)
#df = pd.concat([df,df2]).drop_duplicates()
#df = df.sort_index()
#df.index.drop_duplicates()
#save_file("C:\GCB_CAPITAL\OUTPUT", "BOLT", ".xlsx")

#df = df.index.drop_duplicates(keep='first')
#df.reset_index().drop_duplicates(subset='Index', keep='last').set_index('Index')
#df4 = df.drop_duplicates(subset=df.index, keep='last')
#df = df.loc[df.index.duplicated(keep='first')]

#a= df.index.drop_duplicates(keep='first')

#df = df.reset_index()
#df = df.drop_duplicates(subset='Fecha', keep='last')
#df = df.set_index('Fecha', inplace=False)


#update("AY24")
#update("AY24D")


#PRUEBA    
#update("AGRO")
#update("ALUA")
#MISSING update("APBR")
#update("AUSO")
#update("BBAR")
#update("BHIP")
#update("BMA")
#update("BOLT")
#update("BPAT")
#update("BRIO")
#update("BYMA")
#update("CADO")
#update("CAPX")
#update("CARC")
#update("CECO2")
#update("CELU")
#update("CEPU")
#update("CGPA2")
#update("COME")
#update("CRES")
#update("CTIO")
#update("CVH")
#update("DGCU2")
#update("DOME")
#update("DYCA")
#update("EDLH")
#update("EDN")
#update("EDSH")
#update("EMDE")
#update("ESME")
#update("FERR")
#update("FIPL")
#update("GAMI")
#update("GARO")
#update("GBAN")
#update("GCLA")
#update("GGAL")
#update("GRIM")
#update("HARG")
#update("HAVA")
#update("INDU")
#update("INTR")
#update("INVJ")
#update("IRCP")
#update("IRSA")
#update("LEDE")
#update("LOMA")
#update("LONG")
#update("METR")
#update("MIRG")
#update("MOLA")
#update("MOLI")
#update("MORI")
#update("OEST")
#update("PAMP")
#update("PATA")
#update("PATY")
#update("PGR")
#update("POLL")
#update("RICH")
#update("RIGO")
#update("ROSE")
#update("SAMI")
#update("SEMI")
#update("SUPV")
#update("TECO2")
#update("TGLT")
#update("TGNO4")
#update("TGSU2")
#update("TRAN")
#MISSING update("TS")
#update("TXAR")
#update("VALO")
#update("YPFD")
