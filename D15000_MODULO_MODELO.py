#MODULO MODELO

#INSTALACION
#ARMAR UN DIRECTORIO
#MODELO/ESCENARIOS
#ESCENARIOS
#Aca se cargan los inputs
#MODELO
#MODELO/OUTPUT
#Aca esta el output del modelo armado


#LISTA TOTAL
original_source = "C:\GCB_CAPITAL2\\"
#LISTA DE ARCHIVOS MODULO MODELO
exec(open(original_source+"D0010_importacion_modulos.py").read())


def open_file_versatil(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path2 = (location + "\\" + filename + extension)
    print (path2)
    # importa el modulo os.path, para verificar antes que el file exista
    import os.path    
    from os import path
    if path.exists(path2):
       df = pd.read_excel(path2)
       return (df)
    else:
       df = 0
       return print ("File Not Found")

### EJEMPLOS
#open_file_versatil("C:\GCB_CAPITAL\INPUT", "AGRO", ".xlsx")
#open_file_versatil("C:\GCB_CAPITAL\INPUT", "ALUA", ".xlsx")
#open_file_versatil("C:\GCB_CAPITAL\CURRENCIES", "USDARS_PPP", ".xlsx")
#open_file_versatil("C:\GCB_CAPITAL\CURRENCIES", "USDARS_LIBRE", ".xlsx")
#open_file_versatil("C:\GCB_CAPITAL\CPI", "CPI_ARG", ".xlsx")
#open_file_versatil("C:\GCB_CAPITAL\CPI", "CPI_USA", ".xlsx")




exec(open(original_source+"D15001_arma_bs.py").read())
exec(open(original_source+"D15002_arma_is.py").read())
exec(open(original_source+"D15003_arma_cf.py").read())
exec(open(original_source+"D15005_crea_diccionario_general.py").read())
exec(open(original_source+"D15100_arma_non_depreciating_assets.py").read())
exec(open(original_source+"D15110_arma_depreciating_assets.py").read())
exec(open(original_source+"D15120_arma_cfroi_audit.py").read())
exec(open(original_source+"D15130_arma_global_inflation_adjusted_cash_flow.py").read())
exec(open(original_source+"D15140_arma_gross_plant_life.py").read())
exec(open(original_source+"D15150_arma_project_life.py").read())
exec(open(original_source+"D15160_arma_intangibles_fix.py").read())
exec(open(original_source+"D15170_arma_emerging_markets.py").read())
exec(open(original_source+"D15180_arma_normalized_growth_rate.py").read())
exec(open(original_source+"D15190_arma_bounded_historic_growth_rate.py").read())
exec(open(original_source+"D15200_arma_debt_audit.py").read())
exec(open(original_source+"D15210_arma_ecap_audit.py").read())
exec(open(original_source+"D15220_arma_minority_interest_valuation.py").read())
exec(open(original_source+"D15230_arma_operating_leases.py").read())
exec(open(original_source+"D15240_arma_system_constants.py").read())
exec(open(original_source+"D15250_arma_discount_rate.py").read())
exec(open(original_source+"D15260_arma_adicionales.py").read())
exec(open(original_source+"D15300_crea_estructura.py").read())
exec(open(original_source+"D15350_agrega_partes_al_dataframe.py").read())

exec(open(original_source+"D15400_gdp_msci_and_inflation.py").read())
exec(open(original_source+"D15500_funcion_boton_calculate.py").read())

exec(open(original_source+'D17793_crea_columna_generica.py').read())
exec(open(original_source+'D17794_crea_estructura_constantes.py').read())

exec(open(original_source+'D17797_carga_nads_generico.py').read())

open_equity("MIRG")

exec(open(original_source+'D17795_carga_datos_empresa.py').read())

exec(open(original_source+'D17798_arma_vectores.py').read())

#en este orden grabo una matriz en el subdirectorio MODELO



#exec(open(original_source+'D17790_carga_nads_DEPRECATED.py').read())
#exec(open(original_source+'D17791_carga_nads_generico.py').read())





