import yfinance as yf
import pandas as pd

# Liste des symboles d'actifs que vous souhaitez récupérer
actif_symbols = ['AIR.PA', 'MC.PA', 'RNO.PA', 'AI.PA', 'BNP.PA', 'OR.PA', 'CAP.PA', 'CA.PA',
    'ACA.PA', 'VIE.PA', 'GLE.PA', 'KER.PA', 'LOREAL.PA', 'SGO.PA', 'SU.PA', 'SAN.PA',
    'HO.PA', 'MCRO.PA', 'RMS.PA', 'VIV.PA', 'DG.PA', 'ENGI.PA', 'EN.PA', 'DSY.PA',
    'FTI.PA', 'EL.PA', 'FR.PA', 'UG.PA', 'KER.PA', 'SAF.PA', 'PUB.PA', 'ATO.PA', 'BN.PA',
    'RXL.PA', 'FP.PA', 'SW.PA', 'DS.PA', 'WLN.PA', 'IPN.PA', 'NOKIA.PA', 'GOVT', 'TLT', 'SPY']

# Plage de dates
start_date = '2020-01-01'
end_date = '2022-12-31'

# Création d'un DataFrame Pandas vide pour stocker les données
data = pd.DataFrame()

# Boucle sur les symboles d'actifs pour récupérer les données
for symbol in actif_symbols:
    asset_data = yf.download(symbol, start=start_date, end=end_date)
    data[symbol] = asset_data['Adj Close']  # Prix ajusté en clôture
    data[f'{symbol}_Volume'] = asset_data['Volume']
    data[f'{symbol}_Returns'] = asset_data['Adj Close'].pct_change()
    data[f'{symbol}_Market_Cap'] = yf.Ticker(symbol).info['marketCap'] if 'marketCap' in yf.Ticker(symbol).info else None
    data[f'{symbol}_PE_Ratio'] = yf.Ticker(symbol).info['trailingPE'] if 'trailingPE' in yf.Ticker(symbol).info else None
    data[f'{symbol}_SMA_50'] = asset_data['Adj Close'].rolling(window=50).mean()  # Moyenne mobile sur 50 jours
    data[f'{symbol}_SMA_200'] = asset_data['Adj Close'].rolling(window=200).mean()  # Moyenne mobile sur 200 jours

# Affichage des premières lignes du DataFrame
print(data.head())
