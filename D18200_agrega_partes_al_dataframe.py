
#################################################################################################

### AGREGA BALANCE SHEET

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_balance_sheet)==len(show_nombres_conceptos_estandarizados_balance_sheet):
   #Ahora que las 2 (vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_balance_sheet)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_balance_sheet)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   #ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = 2   #ultimo_celda_con_datos + 1
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:180]

#################################################################################################

### AGREGA ESTADO DE RESULTADOS

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_estado_de_resultado)==len(show_nombres_conceptos_estandarizados_estado_de_resultado):
   #Ahora que las 2 (vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_estado_de_resultado)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_estado_de_resultado)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 2
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:320]

#################################################################################################

### AGREGA ESTADO DE FLUJO DE EFECTIVO - CASH FLOW

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_cash_flow)==len(show_nombres_conceptos_estandarizados_cash_flow):
   #Ahora que las 2 (vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_cash_flow)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_cash_flow)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 2
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:320]


#################################################################################################

### AGREGA NON DEPRECIATING ASSETS

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_global_non_depreciating_assets)==len(show_nombres_conceptos_estandarizados_global_non_depreciating_assets):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_global_non_depreciating_assets)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_global_non_depreciating_assets)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 2
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:510]


#################################################################################################

### AGREGA DEPRECIATING ASSETS

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_global_depreciating_assets)==len(show_nombres_conceptos_estandarizados_global_depreciating_assets): 
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_global_depreciating_assets)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_global_depreciating_assets)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   #
   # Agrega a las series el index correcto para el dataframe
   #a_cargar_en_codigo.index += 502
   #a_cargar_en_concepto.index += 502
   # Termina en 584
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)


#df_show[:600]

#################################################################################################

### AGREGA CFROI AUDIT AND VALUATION

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_cfroi_audit_and_valuation)==len(show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_cfroi_audit_and_valuation)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   #
   # Agrega a las series el index correcto para el dataframe
   #a_cargar_en_codigo.index += 585
   #a_cargar_en_concepto.index += 585
   # Termina en 655
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:670]

#################################################################################################

### AGREGA GLOBAL INFLATION ADJUSTED CASH FLOW

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)==len(show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   #
   # Agrega a las series el index correcto para el dataframe
   #a_cargar_en_codigo.index += 656
   #a_cargar_en_concepto.index += 656
   # Termina en 726
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:740]

#################################################################################################

### AGREGA GROSS PLANT LIFE

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_gross_plant_life)==len(show_nombres_conceptos_estandarizados_gross_plant_life):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_gross_plant_life)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_gross_plant_life)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   #
   # Agrega a las series el index correcto para el dataframe
   #a_cargar_en_codigo.index += 730
   #a_cargar_en_concepto.index += 730
   # Termina en 783
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:790]

#################################################################################################

### AGREGA PROJECT LIFE

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_project_life)==len(show_nombres_conceptos_estandarizados_project_life):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_project_life)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_project_life)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 817
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:830]


#################################################################################################

### AGREGA INTANGIBLES FIX FACTSHEET

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_intangibles_fix_factsheet)==len(show_nombres_conceptos_estandarizados_intangibles_fix_factsheet):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_intangibles_fix_factsheet)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_intangibles_fix_factsheet)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 897
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:900]

#################################################################################################

### AGREGA INFLATION ADJUSTMENTS FOR EMERGING MARKETS

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)==len(show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 7
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:920]

#################################################################################################

### AGREGA NORMALIZED GROWTH RATE 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_normalized_growth_rate)==len(show_nombres_conceptos_estandarizados_normalized_growth_rate):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_normalized_growth_rate)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_normalized_growth_rate)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 987
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1000]

#################################################################################################

### AGREGA BOUNDED HISTORIC GROWTH RATE 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_bounded_historic_growth_rate)==len(show_nombres_conceptos_estandarizados_bounded_historic_growth_rate):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_bounded_historic_growth_rate)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_bounded_historic_growth_rate)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1066
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1080]

#################################################################################################

### AGREGA DEBT AUDIT 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_debt_audit)==len(show_nombres_conceptos_estandarizados_debt_audit):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_debt_audit)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_debt_audit)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1136
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1150]

#################################################################################################

### AGREGA ECAP AUDIT 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_estandarizados_eCap_audit)==len(show_nombres_conceptos_estandarizados_eCap_audit):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_estandarizados_eCap_audit)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_estandarizados_eCap_audit)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1158
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1170]


#################################################################################################

### AGREGA MINORITY INTEREST VALUATION 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_minority_interest_valuation)==len(show_nombres_conceptos_minority_interest_valuation):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_minority_interest_valuation)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_minority_interest_valuation)
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1167
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1180]

#################################################################################################

### AGREGA OPERATING LEASES 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_operating_leases)==len(show_nombres_conceptos_operating_leases):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_operating_leases)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_operating_leases)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1200]

#################################################################################################

### AGREGA SYSTEM CONSTANTS 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_system_constants)==len(show_nombres_conceptos_system_constants):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_system_constants)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_system_constants)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1200]

#################################################################################################

### AGREGA DISCOUNT RATE 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_discount_rate)==len(show_nombres_conceptos_discount_rate):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_discount_rate)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_discount_rate)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1200]

#################################################################################################

### AGREGA ADICIONALES 

# Verifica que las listas sean iguales de longitud antes de armar las series
if len(show_conceptos_adicionales)==len(show_nombres_conceptos_adicionales):
   #global a_cargar_en_codigo, a_cargar_en_concepto, df_show
   #
   #
   #Ahora que las 2 ( vectores show) o listas son iguales vamos a ponerlas en el dataframe
   a_cargar_en_codigo = pd.Series(show_conceptos_adicionales)
   a_cargar_en_concepto = pd.Series(show_nombres_conceptos_adicionales)
   #
   #
   # Se fija donde termina el df_show['Concepto'].dropna().index[-1]
   ultimo_celda_con_datos = df_show['Concepto'].dropna().index[-1]
   comienzo_a_pegar = ultimo_celda_con_datos + 5
   #
   # Agrega a las series el index correcto para el dataframe
   a_cargar_en_codigo.index += comienzo_a_pegar
   a_cargar_en_concepto.index += comienzo_a_pegar
   # Termina en 1193
   df_show['Codigo'].update(a_cargar_en_codigo)
   df_show['Concepto'].update(a_cargar_en_concepto)

#df_show[:1200]

############################################################################################
#  TERMINADO DE ARMAR LOS CONCEPTOS
###########################################################################################

# Cambia de nombre el df para poder grabarlo
#df = df_show
# Graba el dataframe df en el path especificado
#save_file_generico(df, "C:\GCB_CAPITAL3", "GENERICO_", "", ".xlsx")

df_show['Concepto'].dropna()

df_show['Concepto'].dropna().index[-1]