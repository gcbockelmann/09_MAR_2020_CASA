

    
### ARMA LA EESTRUCTURA DE UN ESTADO DE RESULTADOS

df= pd.DataFrame()

# ESTADO DE RESULTADOS

df = df.append({'Conceptos': 'Fecha_de_cierre', '2017FY': "2017-08-26"}, ignore_index=True) 
df = df.append({'Conceptos': 'Fecha_de_publicacion', '2017FY': "2017-08-26"}, ignore_index=True) 

df = df.append({'Conceptos': 'Ventas_netas', '2017FY': 38230.31}, ignore_index=True) 
df = df.append({'Conceptos': 'Costo_de_ventas', '2017FY': 28073.33}, ignore_index=True) 

df = df.append({'Conceptos': 'Margen_bruto', '2017FY': 0}, ignore_index=True) 


#df['Conceptos']['2017FY']

df = df.append({'Conceptos': 'Gastos_de_comercializacion,_generales_y_de_administracion', '2017FY': 4128.15}, ignore_index=True) 
df = df.append({'Conceptos': 'Total_de_otros_ingresos_y_(egresos)_operativos', '2017FY': 24.74}, ignore_index=True) 


df = df.append({'Conceptos': 'Resultado_operativo_antes_de_depreciacion_y_amortizacion', '2017FY': 6053.57}, ignore_index=True) 

df = df.append({'Conceptos': 'Depreciacion_y_amortizacion', '2017FY': 883.68}, ignore_index=True) 
df = df.append({'Conceptos': 'Costos_por_intereses_y_financiacion--Brutos', '2017FY': 1246.28}, ignore_index=True) 

df = df.append({'Conceptos': 'Ingresos_y_(Egresos)_No-Opdferativos', '2017FY': 2705.20}, ignore_index=True) 
df = df.append({'Conceptos': 'Cuestiones_Especiales', '2017FY': 0}, ignore_index=True) 
df = df.append({'Conceptos': 'Resultado_Pre-impositivo', '2017FY': 6628.81}, ignore_index=True) 
df = df.append({'Conceptos': 'Impuesto_a_las_ganancias', '2017FY': 1059.03}, ignore_index=True) 
df = df.append({'Conceptos': 'Interes_minoritario', '2017FY': 0.02}, ignore_index=True) 
df = df.append({'Conceptos': 'Resultado_Neto_despues_del_Interes_minoritario', '2017FY': 5569.76}, ignore_index=True) 

# ESTADO DE SITUACION PATRIMONIAL
df = df.append({'Conceptos': 'Efectivo_e_inversiones_de_corto-plazo', '2017FY': 3033.40}, ignore_index=True)
df = df.append({'Conceptos': 'Deudores_por_ventas_(comerciales)', '2017FY': 1719.09}, ignore_index=True) 
df = df.append({'Conceptos': 'Inventarios', '2017FY': 11878.90}, ignore_index=True) 
df = df.append({'Conceptos': 'Otros_activos_corrientes', '2017FY': 3686.97}, ignore_index=True)
df = df.append({'Conceptos': 'Total_de_activos_corrientes', '2017FY': 20318.36}, ignore_index=True)

df = df.set_index('Conceptos')


#ELIMINAR????
#df = df.append({'Conceptos': 'Margen_bruto', '2017FY': 0}, ignore_index=True) 

#df = df.append({'Conceptos': 'Gastos_de_administracion', '2017FY': 0}, ignore_index=True) 
#df = df.append({'Conceptos': 'Gastos_de_comercializacion', '2017FY': 0}, ignore_index=True) 
#df = df.append({'Conceptos': 'Otros_ingresos_operativos', '2017FY': 0}, ignore_index=True) 
#df = df.append({'Conceptos': 'Otros_egresos_operativos', '2017FY': 0}, ignore_index=True) 

#OPERANDO
#df['Conceptos']['2017FY']

# Calcula el Margen Bruto
#df.loc['Margen_bruto']['2017FY'] = (df.loc['Ventas_netas']['2017FY'])-(df.loc['Costo_de_ventas']['2017FY'])