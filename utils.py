import os
# import json
from yaml import safe_load
from tkinter.filedialog import askopenfilename

def get_fname(msg):
    fname = askopenfilename(
        initialdir=os.getcwd(),
        title=msg)
    return fname

# TODO: maybe make it a class PREPROCESSOR with methods?
def unit_conversion(df, mode='mass to moles'):
    '''
    converts units in dataframe
    :param df: pandas dataframe
    :param mode: 'mass to moles' # TODO: add other modes
    :return:
    '''
    if mode == 'mass to moles':
        df['O2 uM'] = df['Oxygen (ml/L)'] * 1000 / 22.391
        df['SiO2 uM'] = df['SiO2 (mg/l)'] * 1000 / 60.08
        df['PO4 uM'] = df['PO4-P (µg/l)'] / 94.97
        df['NO3 uM'] = df['NO3-N (µg/l)'] / 62

    return df


def identify_season(x):
    if x in [4,5,6,7,8,9,10]:
        season = 'summer'
    else:
        season = 'winter'
    return season


def make_season(df, datename):
    df['season'] = df[datename].dt.month.apply(identify_season)
    return df


def read_all_vars(ds):
    l = list(ds.keys())
    l = [x for x in l if "sink:" not in x]
    l = [x for x in l if "fick:" not in x]
    l = [x for x in l if x not in ["z", "z2", "time", "Ux"]]
    return l


def load_config(filename):
    # deprecated option
    # with open(filename, 'r') as file:
    #     config = json.load(file)
    with open(filename, "r") as yamlfile:
        config = safe_load(yamlfile)
    return config

def integrate_column(idxs, variable, data):

    import xarray as xr

    if variable.startswith("fick:") or variable.startswith("sink:"):
        weights = xr.DataArray(
            data["z2"][idxs[0]:idxs[1]].data
            - data["z2"][idxs[0] + 1 : idxs[1] + 1].data,
            dims=("z2",)
        )
        var_data = data["fick:Alk"].rolling(z2=2).mean().dropna("z2")
        weighted_var = var_data.isel(z2=slice(*idxs)).weighted(weights)
        return weighted_var.sum(dim="z2").values
    else:
        print(f"case _: {variable}")
        weights = xr.DataArray(
            data["z2"][idxs[0]:idxs[1]].data
            - data["z2"][idxs[0] + 1 : idxs[1] + 1].data,
            dims=("z",)
        )
        weighted_var = data[variable].isel(z=slice(*idxs)).weighted(weights)
        return weighted_var.sum(dim="z").values
