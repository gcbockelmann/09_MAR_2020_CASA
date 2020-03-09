
#### PENDIENTES ####
# SPGC
# VALE
# GOLD
#COSTOS DE GOLD
#INGRESO DE TENENCIA
#ARME EL PORTFOLIO A PARTIR DE INFO DE BMB
#CALCULE PORTAFOLIOS
#CALCULE COSTOS Y ARME VALORIZACIONES A UNA FECHA DETERMINADA
#CALCULE RENTABILIDADES

# EL MODELO DE VALUACION
#MODELO DE VALUACION TIPO HOLT
#MODELO DE VALUACION PROPIO 

#MACRO
#TASAS DE INTERES
#TASA REAL
#
#POLITICA MONETARIA
#DOLAR
#DOLAR DE CONVERTIBILIDAD
#DOLAR DE PARIDAD
#DOLAR MULTILATERAL
#RESERVAS INTERNACIONALES NETAS

#FLUJOS
#POLITICA FISCAL
#BALANZA COMERCIAL
#CUENTA CORRIENTE
#BALANCE FISCAL
#CUENTA DE CAPITAL

#MACRO DE USA
#Tablero de control:
#Securities Held Outright
#Job openings.
#Gross domestic investment. Es muy importante pero es trimestral.
#Jobless claims es high frequency
#INDUSTRIAL AND COMMERCIAl LOANS
#M2, M3 
#CCC 


#BAJAR DE BOLSAR/BYMA
#Acciones
#Panel General
#Titulos Publicos
#Cedears
#Grabar en un archivo en directorio BOLSAR. en fomato .xlsx -FORMATO SIN MACROS-

#LISTA TOTAL
original_source = "C:\GCB_CAPITAL3\\"

###########################################################################################################################
############################MODULO SERIES HISTORICAS   ####################################################################
###########################################################################################################################

#LISTA DE ARCHIVOS MODULO SERIES HISTORICAS
exec(open(original_source+"D0010_importacion_modulos.py").read())
exec(open(original_source+"D0020_apertura_excel_generico.py").read())
exec(open(original_source+"D0060_convierte_en_serie_de_tiempo.py").read())
exec(open(original_source+"D0062_borra_archivos_de_un_subdirectorio.py").read())
exec(open(original_source+"D0063_borra_subdirectorio.py").read())
exec(open(original_source+"D0065_secciona_tab_de_equities.py").read())
exec(open(original_source+"D0066_formateo_input_bolsar_equity.py").read())
exec(open(original_source+"D0070_save_file_generico.py").read())
exec(open(original_source+"D0080_inicializa_equity.py").read())
exec(open(original_source+"D0090_actualiza_spch.py").read())
exec(open(original_source+"D0100_open_file_spch.py").read())
exec(open(original_source+"D2000_modulo_indec.py").read())
exec(open(original_source+"D0150_backup.py").read())
exec(open(original_source+"D0095_sobrescribe_archivos_de_excel.py").read())
exec(open(original_source+"D0170_actualiza_modulo_spch.py").read())
exec(open(original_source+"D0200_calculo_del_market_cap_ars.py").read())
exec(open(original_source+"D0300_MODULO_CURRENCIES.py").read())
exec(open(original_source+"D0350_mkt_cap_usd.py").read())
exec(open(original_source+"D0400_mkt_cap_usdars_ppp.py").read())
exec(open(original_source+"D0990_MODULO_SERIES_HISTORICAS.py").read())

#EJECUTABLE MODULO SERIES HISTORICAS
#actualiza_series_historicas("2020-03-06")


################################################################################################################
################################################################################################################
################################################################################################################

#MODULO INDICES - HISTORICO

#LISTA DE ARCHIVOS MODULO INDICES
exec(open(original_source+"D0068_secciona_tab_de_indices.py").read())
exec(open(original_source+"D0069_formateo_input_bolsar_indice.py").read())
exec(open(original_source+"D0500_indice_bolsar.py").read())
exec(open(original_source+"D0510_sobreescribe_spch_indice.py").read())
exec(open(original_source+"D0520_indice_bolsar_usd.py").read())
exec(open(original_source+"D0530_indice_bolsar_usdppp.py").read())
exec(open(original_source+"D0540_corre_modulo_indices.py").read())

#EJECUTABLE MODULO INDICES:
#corre_modulo_indice_merval("2020-03-06_TODO")

###########################################################################################################################
###########################################################################################################################
###########################################################################################################################

#EXPORTAR EQUITIES A METASTOCK PRO V11.

#ARCHIVOS MODULO EXPORTAR EQUITIES A METASTOCK PRO V11.
exec(open(original_source+"D0900_paratxt.py").read())

#EJECUTABLE MODULO EXPORTAR EQUITIES A METASTOCK PRO V11.
#exec(open(original_source+"D0910_lista_de_securities_txt_ARS.py").read())
#exec(open(original_source+"D0920_lista_de_securities_txt_mkt_cap_ARS.py").read())
#exec(open(original_source+"D0930_lista_de_securities_txt_mkt_cap_USD.py").read())
#exec(open(original_source+"D0940_lista_de_securities_txt_mkt_cap_USDPPP.py").read())
#exec(open(original_source+"D0950_lista_de_securities_txt_currencies.py").read())


###########################################################################################################################
###########################################################################################################################
###########################################################################################################################

#EXPORTAR INDICES A METASTOCK PRO V11.

#ARCHIVOS MODULO EXPORTAR INDICES A METASTOCK PRO V11.
exec(open(original_source+"D0900_paratxt.py").read())

#EJECUTABLE MODULO EXPORTAR INDICES A METASTOCK PRO V11.
#txt_indice_ars("^MERV")
#txt_indice_usd("^MERV")
#txt_indice_usdppp("^MERV")

################################################################################################################
################################################################################################################
################################################################################################################

# PRECIOS ONLINE

#ARCHIVOS MODULO PRECIOS ONLINE 
exec(open(original_source+"D1000_precios_online.py").read())
exec(open(original_source+"D2000_modulo_indec.py").read())

#EJECUTABLE MODULO PRECIOS ONLINE
#inicializa_un_nuevo_dia_online_spch()
#inicializa_un_nuevo_dia_online_currencies()
exec(open(original_source+"D1001_lista_precios_online.py").read())
exec(open(original_source+"D1002_lista_precios_online_mkt_cap_ars.py").read())
exec(open(original_source+"D1003_online_actualiza_dolar_libre.py").read())
exec(open(original_source+"D1004_lista_precios_online_mkt_cap_usd.py").read())
prepara_serie_online_diaria_de_tipo_de_cambio_ppp("USD", "ARS", "2020-02-20")
exec(open(original_source+"D1006_lista_precios_online_mkt_cap_usdars_ppp.py").read())


#update_last_price("TXAR")
#update_online_mkt_cap_ars("TXAR", original_source + "\ONLINE\SPCH", original_source + "\ONLINE\MKT_CAP_ARS")
# PARA CCL y DOLAR LIBRE
#update_last_price("GGAL")
#update_online_mercado_americano("GGAL","2020-02-05")
#update_ccl_equities_online("GGAL", original_source + "\ONLINE\SPCH_AMERICANO", "AMERICANO_"+ "GGAL",  ".xlsx", original_source + "ONLINE\SPCH", "SERIE_CORRIENTE_"+ "GGAL", ".xlsx")
#update_ccl_equity_online("GGAL")
#actualiza_dolar_libre_online("GGAL")
# PARA MKT CAP USD
#update_online_mkt_cap_usd("TXAR")
# UPDATEAR MANUALMENTE EL USDARS_PPP
#update_online_mkt_cap_usdppp("TXAR")


### MUY UTIL
#https://stackoverflow.com/questions/34855859/is-there-a-way-in-pandas-to-use-previous-row-value-in-dataframe-apply-when-previ

################################################################################################################
################################################################################################################
################################################################################################################

# MODULO DE GUARDADO O IMPRESION DE CHARTS
exec(open(original_source+"D3200_chart_spch.py").read())
#exec(open(original_source+"D3220_lista_chart_spch.py").read())
exec(open(original_source+"D3230_chart_mkt_cap_ars.py").read())
#exec(open(original_source+"D3240_lista_chart_mkt_cap_ars.py").read())
exec(open(original_source+"D3250_chart_mkt_cap_usdars.py").read())
#exec(open(original_source+"D3260_lista_chart_mkt_cap_usdars.py").read())
exec(open(original_source+"D3270_chart_mkt_cap_usdars_serie_larga.py").read())
#exec(open(original_source+"D3280_lista_chart_mkt_cap_usdars_serie_larga.py").read())
exec(open(original_source+"D3330_chart_mkt_cap_usdars_ppp.py").read())
#exec(open(original_source+"D3340_lista_chart_mkt_cap_usdars_ppp.py").read())

exec(open(original_source+"D3400_ratio_comparacion_mkt_cap_usdars.py").read())

exec(open(original_source+"D3410_chart_index.py").read())
exec(open(original_source+"D3420_chart_index_usdars.py").read())
exec(open(original_source+"D3430_chart_index_usdars_ppp.py").read())



exec(open(original_source+"D3460_compara_series_mkt_cap_usd_porcentaje.py").read())
exec(open(original_source+"D3461_compara_series_mkt_cap_and_div_ars.py").read())
exec(open(original_source+"D3470_chart_currency.py").read())
exec(open(original_source+"D3480_compara_currencies.py").read())
exec(open(original_source+"D3485_diferencial_currency.py").read())

exec(open(original_source+"D3590_candlestick_chart.py").read())
exec(open(original_source+"D3591_no_ejecutable_candlestick_original.py").read())


#MODULO ARMADO DE LISTAS DE TODOS LOS SECURITIES - DE MKT CAP - ORDENA DE MAYOR A MENOR, ETC
#exec(open(original_source+"D4000_lista_de_mkt_cap_actual_en_M_USD.py").read())
#exec(open(original_source+"D4001_lista_de_mkt_cap_actual_en_M_USDPPP.py").read())
#exec(open(original_source+"D4002_lista_de_mkt_cap_actual_en_M_USDPPP_variacion.py").read())


#MODULO ARMADO DE UN BALANCE SHEET
#exec(open(original_source+"D5010_estado_de_resultados.py").read())
#exec(open(original_source+"D5720_open_excel_tab.py").read())
#exec(open(original_source+"D5730_excel_txar.py").read())

################################################################################################################
################################################################################################################
################################################################################################################

#MODULO GRAFICADOR DE SERIES
exec(open(original_source+"D6000_MODULO_GRAFICADOR_DE_SERIES.py").read())

################################################################################################################
################################################################################################################
################################################################################################################

#MODULO PORTAFOLIO
#ARCHIVOS MODULO PORTAFOLIO
exec(open(original_source+"D10000_MODULO_PORTFOLIO_TRACKER.py").read())
exec(open(original_source+"D12000_MODULO_CONTABILIDAD.py").read())

#EJECUTABLE MODULO PORTAFOLIO

#exec(open(original_source+"D12100_GCB_CAPITAL_PORTFOLIO.py").read())



################################################################################################################
################################################################################################################
#############################################################################################################

#MODULO MODELO HOLT

#ARCHIVOS MODULO MODELO HOLT

### NUEVO ARMADOR DE MODELOS
exec(open(original_source+"D18000_inicia_dataframe.py").read())
exec(open(original_source+"D18100_arma_paginas.py").read())
exec(open(original_source+"D18200_agrega_partes_al_dataframe.py").read())

exec(open(original_source+"D18400_gdp_msci_and_inflation.py").read())
exec(open(original_source+"D18500_funcion_boton_calculate.py").read())
exec(open(original_source+'D18793_crea_columna_generica.py').read())
exec(open(original_source+'D18794_crea_estructura_constantes.py').read())
# Define el ticker
exec(open(original_source+'D18795_carga_datos_empresa.py').read())
# Prepara para leer el archivo de excel
exec(open(original_source+'D18797_carga_nads_generico.py').read())


#EJECUTABLE MODULO MODELO HOLT
# Ejecuta la apertura de un archivo de excel y carga de datos de un ticker
open_equity("MIRG")
#Ejecuta carga de vectores en el dataframe - Esta seria el ultimo archivo a correr
exec(open(original_source+'D18798_arma_vectores.py').read())


#TXAR
open_equity("TXAR")
exec(open(original_source+'D18798_arma_vectores.py').read())
