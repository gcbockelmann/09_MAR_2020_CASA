#LISTA DE PRECIOS ONLINE MKT CAP USD

lista_de_securities=["AGRO",
"ALUA",
"AUSO",
"BBAR",
"BHIP",
"BMA",
"BOLT",
"BPAT",
"BRIO",
"BYMA",
"CADO",
"CAPX",
"CEPU",
"COME",
"CRES",
"CTIO",
"CVH",
"DGCU2",
"EDN",
"FERR",
"GCLA",
"GGAL",
"HARG",
"INTR",
"INVJ",
"LEDE",
"LOMA",
"METR",
"MIRG",
"MOLA",
"MOLI",
"OEST",
"PAMP",
"PATA",
"RICH",
"SAMI",
"SUPV",
"TECO2",
"TGNO4",
"TGSU2",
"TRAN",
"TXAR",
"VALO",
"YPFD"]

#update_online_mkt_cap_usd("TXAR")

def corre_update_online_mkt_cap_usd(lista):
    for ticker in lista:
        update_online_mkt_cap_usd(ticker)


corre_update_online_mkt_cap_usd(lista_de_securities)

