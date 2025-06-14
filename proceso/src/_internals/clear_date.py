import pandas as pd


def clear_date(data, date, casino):
    data['Fecha'] = date
    data['Casino']= casino
    data["Fecha"] =  pd.to_datetime(data["Fecha"]).dt.date
    return data