# PARA ACTUALIZAR ONLINE CCL y DOLAR LIBRE

#update_last_price("GGAL")
#update_online_mercado_americano("GGAL","2020-02-05")
#update_ccl_equities_online("GGAL", original_source + "\ONLINE\SPCH_AMERICANO", "AMERICANO_"+ "GGAL",  ".xlsx", original_source + "ONLINE\SPCH", "SERIE_CORRIENTE_"+ "GGAL", ".xlsx")
#update_ccl_equity_online("GGAL")
#actualiza_dolar_libre_online("GGAL")

#from datetime import date
#today = date.today()
#print("Today's date:", today)

#today.strftime("%Y/%m/%d")

def corre_online_actualiza_dolar_libre():
    #
    #
    from datetime import date
    from datetime import timedelta
    from datetime import datetime
    #
    #today = date.today()
    #
    #hoy = today.strftime("%Y/%m/%d")
    #
    Today_plus_1 = date.today()+timedelta(days=1)
    # 
    hoy_mas_uno = Today_plus_1.strftime("%Y/%m/%d")
    #
    print(hoy_mas_uno)
    #
    # Arma el input bajado del mercado americano y actualiza la serie SPCH_AMERICANO GGAL en el subdirectorio ONLINE
    update_online_mercado_americano("GGAL",hoy_mas_uno)
    #
    # Me parece que esta funcion esta demas porque con el update ccl_equiti llama a esta otra para actualizar el ccl online
    #update_ccl_equities_online("GGAL", original_source + "\ONLINE\SPCH_AMERICANO", "AMERICANO_"+ "GGAL",  ".xlsx", original_source + "ONLINE\SPCH", "SERIE_CORRIENTE_"+ "GGAL", ".xlsx") 
    update_ccl_equity_online("GGAL")
    #
    actualiza_dolar_libre_online("GGAL")

corre_online_actualiza_dolar_libre()

