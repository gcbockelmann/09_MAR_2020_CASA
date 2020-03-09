

# SOBREESCRIBE ARCHIVOS DE EXCEL DE SPCH

###FALTA DE HACER COPIA DE SEGURIDAD



def sobre_escribe(ticker, fecha_del_ultimo_dato_para_actualizar):
    equities_list = ['AGRO', 'ALUA', 'APBR', 'AUSO', 'BBAR', 'BHIP', 'BMA', 'BOLT', 'BPAT', 'BRIO6', 'BRIO', 'BYMA', 'CADO', 'CAPX', 'CARC', 'CECO2', 'CELU', 'CEPU', 'CGPA2', 'COME', 'CRES', 'CTIO', 'CVH', 'DGCU2', 'DOME', 'DYCA', 'EDN', 'FERR', 'FIPL', 'GAMI', 'GARO', 'GBAN', 'GCLA', 'GGAL', 'GRIM', 'HARG', 'HAVA', 'INDU', 'INTR', 'INVJ', 'IRCP', 'IRSA', 'LEDE', 'LOMA', 'LONG', 'METR', 'MIRG', 'MOLA5', 'MOLA', 'MOLI5', 'MOLI', 'MORI', 'OEST', 'PAMP', 'PATA', 'PATY', 'PGR', 'POLL', 'RICH', 'RIGO', 'ROSE', 'SAMI', 'SEMI', 'SUPV', 'TECO2', 'TGLT', 'TGNO4', 'TGSU2', 'TRAN', 'TS', 'TXAR', 'VALO', 'YPFD']
    #
    bonos_list = ['A2E2', 'A2E2C', 'A2E2D', 'A2E3', 'A2E3C', 'A2E3D', 'A2E7', 'A2E7C', 'A2E7D', 'A2E8', 'A2E8C', 'A2E8D', 'A2J9C', 'A2J9D', 'A2M2', 'A2M2C', 'AA17C', 'AA17D', 'AA19C', 'AA19D', 'AA21', 'AA21C', 'AA21D', 'AA22', 'AA22C', 'AA22D', 'AA25', 'AA25C', 'AA25D', 'AA26', 'AA26C', 'AA26D', 'AA37', 'AA37C', 'AA37D', 'AA46', 'AA46C', 'AA46D', 'AC17', 'AC17C', 'AC17D', 'AD16C', 'AD16D', 'AE14C', 'AE28', 'AE48', 'AE48C', 'AE48D', 'AF17C', 'AF17D', 'AF20', 'AF20C', 'AF20D', 'AL16D', 'AL28', 'AL28C', 'AL28D', 'AL36', 'AL36C', 'AL36D', 'AM18C', 'AM18D', 'AM20', 'AM20C', 'AM20D', 'AMX8D', 'AMX9C', 'AN18C', 'AN18D', 'AO16C', 'AO16D', 'AO17C', 'AO20', 'AO20C', 'AO20D', 'AS13C', 'AS13D', 'AS15C', 'AS17D', 'AY24', 'AY24C', 'AY24D', 'BACX1', 'BB2N9', 'BB2S9', 'BBA20', 'BBF20', 'BBN19', 'BBO19', 'BCD19', 'BCDF1', 'BCFD1', 'BCFM1', 'BCHD1', 'BCHD2', 'BCHD3', 'BCMR', 'BCN16', 'BD2C0', 'BD2C9', 'BD3C0', 'BDC20', 'BDC22', 'BDC24', 'BDC28', 'BDEDD', 'BGBX1', 'BNF21', 'BNS20', 'BOHI1', 'BORD1', 'BORN1', 'BP15C', 'BP18C', 'BP18D', 'BP21', 'BP21C', 'BP21D', 'BP28', 'BP28C', 'BP28D', 'BPLD', 'BPLDC', 'BPLDD', 'BPLE', 'BPLED', 'BPMD', 'BPMDD', 'BPME', 'BRD19', 'BRN20', 'BT02', 'BT03', 'BX92', 'CH24D', 'CHAQ', 'CHSG1', 'CO21D', 'CO24D', 'CO26', 'CO26D', 'CO27D', 'CUAP', 'DIA0', 'DIA0C', 'DIA0D', 'DICA', 'DICAC', 'DICAD', 'DICE', 'DICP', 'DICPC', 'DICPD', 'DICY', 'DICYC', 'DICYD', 'DIE0', 'DIP0', 'DISD', 'DIY0', 'DIY0D', 'EF07', 'ERF25', 'EY28', 'FERB1', 'FORM1', 'FORM2', 'FORM3', 'FRB', 'GA09', 'GD03', 'GD03C', 'GD05', 'GD08', 'GE17', 'GF12', 'GF19', 'GF20', 'GJ15', 'GJ17C', 'GJ17D', 'GJ18', 'GJ31', 'GL30', 'GM10', 'GO06', 'GPBX2', 'GPBX7', 'GS27', 'H27L6', 'JUS22', 'L2DN7', 'NDT11', 'NF18C', 'NO20', 'NRH2', 'NRH2C', 'PAA0', 'PAA0D', 'PAE0', 'PAP0', 'PARA', 'PARAC', 'PARAD', 'PARD', 'PARE', 'PARP', 'PARPC', 'PARPD', 'PARY', 'PARYC', 'PARYD', 'PAY0', 'PAY0D', 'PAY5', 'PBA25', 'PBD19', 'PBF23', 'PBJ21', 'PBJ27', 'PBM24', 'PBY22', 'PMJ21', 'PMY24', 'PR10', 'PR13', 'PR15', 'PR15C', 'PRE3', 'PRE4', 'PRE6', 'PRO1', 'PRO2', 'PRO3', 'PRO4', 'PRO5', 'PRO6', 'PRO8', 'PRO9', 'PUL26', 'PUM21', 'PUO19', 'PUY23', 'PX10', 'PX13', 'PX14', 'PX21', 'RA13D', 'RC21', 'RIF25', 'RN20', 'RNA21', 'RNG22', 'RNG23', 'RO15C', 'RO15D', 'RV05', 'S11O9', 'S13S9', 'S15N9', 'S28F0', 'S29Y0', 'S30A0', 'S30G9', 'S30S9', 'S31L0', 'S31O9', 'SA21', 'SA24D', 'SARH', 'SF07', 'SL02', 'TC20', 'TC20C', 'TC20D', 'TC21', 'TC21C', 'TC21D', 'TC23', 'TC23D', 'TC25P', 'TFU27', 'TJ20', 'TJ20C', 'TJ20D', 'TN20', 'TO21', 'TO21C', 'TO23', 'TO26', 'TO26C', 'TPMS', 'TS27', 'TSEX5', 'TTUX2', 'TUCS3', 'TUCU2', 'TVPA', 'TVPAC', 'TVPAD', 'TVPE', 'TVPED', 'TVPP', 'TVPPC', 'TVPPD', 'TVPY', 'TVPYC', 'TVPYD', 'TVY0', 'TVY0C', 'TVY0D', 'TY03', 'TY04', 'TY05', 'TY06', 'U11O9', 'U13S9', 'U14F0', 'U15N9', 'U17E0', 'U20D9', 'U25O9', 'U26L9', 'U27S9', 'U28F0', 'U29N9', 'U30G9', 'U31E0', 'V03O9', 'V04D9', 'V04S9', 'V05N9', 'VBL6', 'VE02', 'VEA2', 'VEF4', 'VEO2', 'VEY4', 'X2E2', 'X2E7', 'X30G9', 'X30S9', 'XA21', 'XA26', 'XA46', 'XL36', 'ZO03', 'ZO04']
    #
    cedears_list = ['GOLD', 'VALE'] 
    #
    #
    filename = "SERIE_CORRIENTE_" + str(ticker)
    #
    import os
    import shutil
    #
    if ticker in equities_list:
       exists = os.path.isfile(original_source + "/OUTPUT/EQUITIES/SERIE_CORRIENTE_" +str(ticker)+".xlsx")
       if exists:
          open_file_spch(original_source + "\OUTPUT\EQUITIES", filename , ".xlsx")
       else:
          return
    elif ticker in bonos_list:
       exists = os.path.isfile(original_source + "/OUTPUT/BONOS/SERIE_CORRIENTE_" +str(ticker)+".xlsx")
       if exists:
          open_file_spch(original_source + "\OUTPUT\BONOS", filename , ".xlsx") 
       else:
          return        
    elif ticker in cedears_list:
       exists = os.path.isfile(original_source + "/OUTPUT/CEDEARS/SERIE_CORRIENTE_" +str(ticker)+".xlsx")
       if exists:
          open_file_spch(original_source + "\OUTPUT\CEDEARS", filename , ".xlsx") 
       else:
          return        
    else:
       print ("No esta en la lista de securities o hay otro problema")
    #
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    if fecha_del_ultimo_dato_para_actualizar == b:
       if ticker in equities_list:       
          old_path = original_source + "/OUTPUT/EQUITIES/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
          nuevo_path = original_source + "/SPCH/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
          newPath = shutil.copy(old_path, nuevo_path)
       elif ticker in bonos_list:
            old_path = original_source + "/OUTPUT/BONOS/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
            nuevo_path = original_source + "/SPCH/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
            newPath = shutil.copy(old_path, nuevo_path) 
       elif ticker in cedears_list:
            old_path = original_source + "/OUTPUT/CEDEARS/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
            nuevo_path = original_source + "/SPCH/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
            newPath = shutil.copy(old_path, nuevo_path) 
       else:
            pass        
    else:
       print("no escribe")
    #     
    return


#sobre_escribe("AGRO", '2019-10-12')

def copia_spch(fecha):
    equities_list = ['AGRO', 'ALUA', 'APBR', 'AUSO', 'BBAR', 'BHIP', 'BMA', 'BOLT', 'BPAT', 'BRIO6', 'BRIO', 'BYMA', 'CADO', 'CAPX', 'CARC', 'CECO2', 'CELU', 'CEPU', 'CGPA2', 'COME', 'CRES', 'CTIO', 'CVH', 'DGCU2', 'DOME', 'DYCA', 'EDN', 'FERR', 'FIPL', 'GAMI', 'GARO', 'GBAN', 'GCLA', 'GGAL', 'GRIM', 'HARG', 'HAVA', 'INDU', 'INTR', 'INVJ', 'IRCP', 'IRSA', 'LEDE', 'LOMA', 'LONG', 'METR', 'MIRG', 'MOLA5', 'MOLA', 'MOLI5', 'MOLI', 'MORI', 'OEST', 'PAMP', 'PATA', 'PATY', 'PGR', 'POLL', 'RICH', 'RIGO', 'ROSE', 'SAMI', 'SEMI', 'SUPV', 'TECO2', 'TGLT', 'TGNO4', 'TGSU2', 'TRAN', 'TS', 'TXAR', 'VALO', 'YPFD']
    #
    bonos_list = ['A2E2', 'A2E2C', 'A2E2D', 'A2E3', 'A2E3C', 'A2E3D', 'A2E7', 'A2E7C', 'A2E7D', 'A2E8', 'A2E8C', 'A2E8D', 'A2J9C', 'A2J9D', 'A2M2', 'A2M2C', 'AA17C', 'AA17D', 'AA19C', 'AA19D', 'AA21', 'AA21C', 'AA21D', 'AA22', 'AA22C', 'AA22D', 'AA25', 'AA25C', 'AA25D', 'AA26', 'AA26C', 'AA26D', 'AA37', 'AA37C', 'AA37D', 'AA46', 'AA46C', 'AA46D', 'AC17', 'AC17C', 'AC17D', 'AD16C', 'AD16D', 'AE14C', 'AE28', 'AE48', 'AE48C', 'AE48D', 'AF17C', 'AF17D', 'AF20', 'AF20C', 'AF20D', 'AL16D', 'AL28', 'AL28C', 'AL28D', 'AL36', 'AL36C', 'AL36D', 'AM18C', 'AM18D', 'AM20', 'AM20C', 'AM20D', 'AMX8D', 'AMX9C', 'AN18C', 'AN18D', 'AO16C', 'AO16D', 'AO17C', 'AO20', 'AO20C', 'AO20D', 'AS13C', 'AS13D', 'AS15C', 'AS17D', 'AY24', 'AY24C', 'AY24D', 'BACX1', 'BB2N9', 'BB2S9', 'BBA20', 'BBF20', 'BBN19', 'BBO19', 'BCD19', 'BCDF1', 'BCFD1', 'BCFM1', 'BCHD1', 'BCHD2', 'BCHD3', 'BCMR', 'BCN16', 'BD2C0', 'BD2C9', 'BD3C0', 'BDC20', 'BDC22', 'BDC24', 'BDC28', 'BDEDD', 'BGBX1', 'BNF21', 'BNS20', 'BOHI1', 'BORD1', 'BORN1', 'BP15C', 'BP18C', 'BP18D', 'BP21', 'BP21C', 'BP21D', 'BP28', 'BP28C', 'BP28D', 'BPLD', 'BPLDC', 'BPLDD', 'BPLE', 'BPLED', 'BPMD', 'BPMDD', 'BPME', 'BRD19', 'BRN20', 'BT02', 'BT03', 'BX92', 'CH24D', 'CHAQ', 'CHSG1', 'CO21D', 'CO24D', 'CO26', 'CO26D', 'CO27D', 'CUAP', 'DIA0', 'DIA0C', 'DIA0D', 'DICA', 'DICAC', 'DICAD', 'DICE', 'DICP', 'DICPC', 'DICPD', 'DICY', 'DICYC', 'DICYD', 'DIE0', 'DIP0', 'DISD', 'DIY0', 'DIY0D', 'EF07', 'ERF25', 'EY28', 'FERB1', 'FORM1', 'FORM2', 'FORM3', 'FRB', 'GA09', 'GD03', 'GD03C', 'GD05', 'GD08', 'GE17', 'GF12', 'GF19', 'GF20', 'GJ15', 'GJ17C', 'GJ17D', 'GJ18', 'GJ31', 'GL30', 'GM10', 'GO06', 'GPBX2', 'GPBX7', 'GS27', 'H27L6', 'JUS22', 'L2DN7', 'NDT11', 'NF18C', 'NO20', 'NRH2', 'NRH2C', 'PAA0', 'PAA0D', 'PAE0', 'PAP0', 'PARA', 'PARAC', 'PARAD', 'PARD', 'PARE', 'PARP', 'PARPC', 'PARPD', 'PARY', 'PARYC', 'PARYD', 'PAY0', 'PAY0D', 'PAY5', 'PBA25', 'PBD19', 'PBF23', 'PBJ21', 'PBJ27', 'PBM24', 'PBY22', 'PMJ21', 'PMY24', 'PR10', 'PR13', 'PR15', 'PR15C', 'PRE3', 'PRE4', 'PRE6', 'PRO1', 'PRO2', 'PRO3', 'PRO4', 'PRO5', 'PRO6', 'PRO8', 'PRO9', 'PUL26', 'PUM21', 'PUO19', 'PUY23', 'PX10', 'PX13', 'PX14', 'PX21', 'RA13D', 'RC21', 'RIF25', 'RN20', 'RNA21', 'RNG22', 'RNG23', 'RO15C', 'RO15D', 'RV05', 'S11O9', 'S13S9', 'S15N9', 'S28F0', 'S29Y0', 'S30A0', 'S30G9', 'S30S9', 'S31L0', 'S31O9', 'SA21', 'SA24D', 'SARH', 'SF07', 'SL02', 'TC20', 'TC20C', 'TC20D', 'TC21', 'TC21C', 'TC21D', 'TC23', 'TC23D', 'TC25P', 'TFU27', 'TJ20', 'TJ20C', 'TJ20D', 'TN20', 'TO21', 'TO21C', 'TO23', 'TO26', 'TO26C', 'TPMS', 'TS27', 'TSEX5', 'TTUX2', 'TUCS3', 'TUCU2', 'TVPA', 'TVPAC', 'TVPAD', 'TVPE', 'TVPED', 'TVPP', 'TVPPC', 'TVPPD', 'TVPY', 'TVPYC', 'TVPYD', 'TVY0', 'TVY0C', 'TVY0D', 'TY03', 'TY04', 'TY05', 'TY06', 'U11O9', 'U13S9', 'U14F0', 'U15N9', 'U17E0', 'U20D9', 'U25O9', 'U26L9', 'U27S9', 'U28F0', 'U29N9', 'U30G9', 'U31E0', 'V03O9', 'V04D9', 'V04S9', 'V05N9', 'VBL6', 'VE02', 'VEA2', 'VEF4', 'VEO2', 'VEY4', 'X2E2', 'X2E7', 'X30G9', 'X30S9', 'XA21', 'XA26', 'XA46', 'XL36', 'ZO03', 'ZO04']
    #
    cedears_list = ['GOLD', 'VALE'] 
    #
    lista_total = []
    lista_total.append(equities_list)
    lista_total.append(bonos_list)
    lista_total.append(cedears_list)
    for security in equities_list:    
        sobre_escribe(security, fecha) 
    for security in bonos_list:    
        sobre_escribe(security, fecha) 
    for security in cedears_list:    
        sobre_escribe(security, fecha)  
    return

#copia_spch('2020-01-21')



##################################
#############3
############### CODIGO A BORRAR

##### SOBREESCRIBE LOS ARCHIVOS DE LA SPCH
#BONOS
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/BONOS/SERIE_CORRIENTE_AY24.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_AY24.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/BONOS/SERIE_CORRIENTE_AY24D.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_AY24D.xlsx')
#CEDEARS
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/CEDEARS/SERIE_CORRIENTE_GOLD.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_GOLD.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/CEDEARS/SERIE_CORRIENTE_VALE.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_VALE.xlsx')
#EQUITIES
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_AGRO.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_AGRO.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_ALUA.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_ALUA.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_AUSO.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_AUSO.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_BBAR.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_BBAR.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_BHIP.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_BHIP.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_BMA.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_BMA.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_BOLT.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_BOLT.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_BPAT.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_BPAT.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_BRIO.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_BRIO.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_BYMA.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_BYMA.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CADO.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CADO.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CAPX.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CAPX.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CEPU.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CEPU.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CGPA2.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CGPA2.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_COME.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_COME.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CEPU.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CEPU.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CRES.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CRES.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CTIO.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CTIO.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_CVH.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_CVH.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_DGCU2.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_DGCU2.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_EDN.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_EDN.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_FERR.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_FERR.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_GCLA.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_GCLA.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_GGAL.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_GGAL.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_HARG.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_HARG.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_INTR.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_INTR.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_INVJ.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_INVJ.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_LEDE.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_LEDE.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_LOMA.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_LOMA.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_METR.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_METR.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_MIRG.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_MIRG.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_MOLA.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_MOLA.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_MOLI.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_MOLI.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_OEST.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_OEST.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_PAMP.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_PAMP.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_PATA.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_PATA.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_RICH.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_RICH.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_SAMI.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_SAMI.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_SUPV.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_SUPV.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_TECO2.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_TECO2.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_TGNO4.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_TGNO4.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_TGSU2.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_TGSU2.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_TRAN.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_TRAN.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_TXAR.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_TXAR.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_VALO.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_VALO.xlsx')
#newPath = shutil.copy('C:/GCB_CAPITAL/OUTPUT/EQUITIES/SERIE_CORRIENTE_YPFD.xlsx', 'C:/GCB_CAPITAL/SPCH/SERIE_CORRIENTE_YPFD.xlsx')



##################EJEMPLOS#
import shutil
#newPath = shutil.copy('sample1.txt', 'C:/GCB_CAPITAL')
#newPath = shutil.copy('TXAR.xlsx', 'C:/GCB_CAPITAL')
#newPath = shutil.copy('C:/GCB_CAPITAL/TXAR.xlsx', 'C:/GCB_CAPITAL/OUTPUT/TXAR.xlsx')
#ispch = open_file_spch("C:\GCB_CAPITAL\OUTPUT\BONOS", filename2 , ".xlsx")

# Abre los archivos
#open_file_spch("C:\GCB_CAPITAL\OUTPUT\BONOS", "SERIE_CORRIENTE_AY24" , ".xlsx")
#open_file_spch("C:\GCB_CAPITAL\OUTPUT\EQUITIES", "SERIE_CORRIENTE_AGRO" , ".xlsx")
#open_file_spch("C:\GCB_CAPITAL\OUTPUT\CEDEARS", "SERIE_CORRIENTE_VALE" , ".xlsx")
#open_file_spch("C:\GCB_CAPITAL\OUTPUT\CURRENCIES", "USDARS_MEP" , ".xlsx")



