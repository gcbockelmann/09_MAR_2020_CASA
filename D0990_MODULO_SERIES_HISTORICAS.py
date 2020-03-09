

#MODULO SERIES HISTORICAS

def actualiza_series_historicas(fecha_ultimo_dato_del_excel):
    print("")
    print("")
    actualizacion_modulo_spch(fecha_ultimo_dato_del_excel)
    print("")
    print("")
    exec(open(original_source+"D0210_z_lista_de_securities_calculo_mkt_cap.py").read())
    corre_modulo_usd_libre("GGAL", fecha_ultimo_dato_del_excel)
    print("")
    print("")
    exec(open(original_source+"D0360_z_lista_de_securities_calcula_mkt_cap_usd.py").read())
    # FALTA ACTUALIZAR EL USDARS_PPP
    # ARMA EL USDARS_PPP con ano base en 2002
    genera_tipo_de_cambio_de_paridad("ARG", "USA", "2002-01-31")
    #
    print("")
    print("")
    prepara_USDARS_a_partir_del_USDARS_LIBRE()
    print("")
    print("")
    prepara_serie_diaria_de_tipo_de_cambio_ppp("USD", "ARS", fecha_ultimo_dato_del_excel)
    print("")
    print("")
    exec(open(original_source+"D0410_z_lista_de_securities_calcula_mkt_cap_usdarsppp.py").read())


#actualiza_series_historicas("2020-02-06")

