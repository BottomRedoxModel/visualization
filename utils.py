import os
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
        df['O2 uM'] = df['Oksygen (ml/L)'] * 1000 / 22.391
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