from currency import Currency


currency = Currency('BTC')
top_10_cryptos = currency.api_call()
if top_10_cryptos is not None:
    for crypto in top_10_cryptos:
        print(crypto['name'], crypto['symbol'], crypto['quote']['USD']['price'])
else:
    print("Hubo un error al realizar la solicitud.")
