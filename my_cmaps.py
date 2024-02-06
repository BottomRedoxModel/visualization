from matplotlib import colors
from matplotlib import cm
import colormaps as cmaps

mp_palette = ['#0d3b66', '#faf0ca', '#f4d35e', '#ee964b', 'crimson', 'darkred']
mp = colors.LinearSegmentedColormap.from_list('mp_colormap', mp_palette, N=256)

phy_palette = ['0.92', '#b7e4c7', '#95d5b2', '#74c69d',
               '#52b788', '#40916c', '#2d6a4f', '#1b4332', '#081c15']
phy = colors.LinearSegmentedColormap.from_list('phy_colormap', phy_palette, N=256)

het_palette = ['0.92',"#c9cba3","#ffe1a8","#e26d5c","#723d46","#472d30"]
het = colors.LinearSegmentedColormap.from_list('het_colormap', het_palette, N=256)

pom_palette = ['0.92', '0.8',"#005f73","#0a9396","#94d2bd", #"#e9d8a6",
              # "#ee9b00", "#ca6702","#bb3e03","#ae2012","#9b2226"]
               "#ee9b00", "#ca6702", "#ae2012","#9b2226"]
pom = colors.LinearSegmentedColormap.from_list('om_colormap', pom_palette, N=256)

dom_palette = ['0.92','#9DAFAE',"#04395e","#70a288", "#dab785","#d5896f",'#ad2e24',"#540804"]
dom = colors.LinearSegmentedColormap.from_list('dom_colormap', dom_palette, N=256)

cmap = cm.get_cmap('plasma', 96)
cmap_hex = [colors.rgb2hex(cmap(i)) for i in range(cmap.N)]
oxy_palette = ['0.92']*3 + cmap_hex
oxy = colors.LinearSegmentedColormap.from_list('oxy_colormap', oxy_palette, N=256)

ph_palette = ["#001427","#708d81", "#efe9ae", "#f3ffbd",
              "#f4d58d", "#ee964b", "#f35b04", "#bf0603", "#231942"]
ph = colors.LinearSegmentedColormap.from_list('ph_colormap', ph_palette, N=256)
# ph = 'turbo'

cmap_dict = {'MP_free': mp, 'MP_biof': mp,
             'MP_het': mp, 'MP_det': mp,
             'MP_TOT': mp, 'MP_TOT_items': mp,
             'Oxy': oxy, 'Phy': phy, 'Het': het,
             'POM': pom, 'DOM': dom, 'NUT': cmaps.amp,
             'T': 'RdYlBu_r', 'S': cmaps.haline,
             'pH': cmaps.bilbao, 'pCO2': cmaps.lapaz_r,
             'Om_Ar': cmaps.savanna_r, 'DIC': cmaps.tokyo_r,
             'Alk': cmaps.buda_r, 'CO3': cmaps.turku_r,
}