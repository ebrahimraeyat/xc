# -*- coding: utf-8 -*-
''' Arcelor square hollow tubes.'''
# Cross section axis:

#    ARCELOR          XC

#                     ^ Y                    
#                     |

#     -----         -----
#       |             | 
#       | -> Y        | -> Z
#       |             |
#     -----         -----

#       |
#       v Z


# The axis used in Arcelor documentation are different from those used in XC
# (strong axis parallel to z axis) in other words: values for Y and Z axis 
# are swapped with respect to those in the catalog.

# En este caso al ser secciones con tensor de inercia esférico en su 
# plano los valores en
# ambos ejes son iguales y no es necesario intercambiarlos.


SHSprofiles={}

'''
XXX Repasar coeficientes de distorsión
   alpha-> alphaZ,alphaY
'''
SHSprofiles['SHS50x50x2_5']= {'nmb':'SHS50x50x2.5', 'b':0.05, 'h':0.05, 'e':2.5e-3, 'P':3.54, 'A':4.51e-4, 'Iz':17.9e-8, 'Iy':17.9e-8, 'Wzel':7.16e-6, 'Wzpl':8.47e-6, 'iz':1.99e-2, 'iy':1.99e-2, 'It':26.8e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS50x50x3']= {'nmb':'SHS50x50x3', 'b':0.05, 'h':0.05, 'e':3e-3, 'P':4.22, 'A':5.37e-4, 'Iz':20.8e-8, 'Iy':20.8e-8, 'Wzel':8.34e-6, 'Wzpl':9.95e-6, 'iz':1.97e-2, 'iy':1.97e-2, 'It':31.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS50x50x4']= {'nmb':'SHS50x50x4', 'b':0.05, 'h':0.05, 'e':4e-3, 'P':5.52, 'A':7.03e-4, 'Iz':26.2e-8, 'Iy':26.2e-8, 'Wzel':10.46e-6, 'Wzpl':12.73e-6, 'iz':1.93e-2, 'iy':1.93e-2, 'It':38.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS50x50x5']= {'nmb':'SHS50x50x5', 'b':0.05, 'h':0.05, 'e':5e-3, 'P':6.78, 'A':8.64e-4, 'Iz':30.8e-8, 'Iy':30.8e-8, 'Wzel':12.3e-6, 'Wzpl':15.25e-6, 'iz':1.89e-2, 'iy':1.89e-2, 'It':45.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS60x60x2']= {'nmb':'SHS60x60x2', 'b':0.06, 'h':0.06, 'e':2e-3, 'P':3.6, 'A':4.58e-4, 'Iz':26e-8, 'Iy':26e-8, 'Wzel':8.68e-6, 'Wzpl':10.1e-6, 'iz':2.38e-2, 'iy':2.38e-2, 'It':39e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS60x60x3']= {'nmb':'SHS60x60x3', 'b':0.06, 'h':0.06, 'e':3e-3, 'P':5.32, 'A':6.78e-4, 'Iz':37.1e-8, 'Iy':37.1e-8, 'Wzel':12.38e-6, 'Wzpl':14.63e-6, 'iz':2.34e-2, 'iy':2.34e-2, 'It':55.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS60x60x4']= {'nmb':'SHS60x60x4', 'b':0.06, 'h':0.06, 'e':4e-3, 'P':7, 'A':8.92e-4, 'Iz':47.1e-8, 'Iy':47.1e-8, 'Wzel':15.69e-6, 'Wzpl':18.85e-6, 'iz':2.3e-2, 'iy':2.3e-2, 'It':70.2e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS60x60x5']= {'nmb':'SHS60x60x5', 'b':0.06, 'h':0.06, 'e':5e-3, 'P':8.63, 'A':10.99e-4, 'Iz':55.9e-8, 'Iy':55.9e-8, 'Wzel':18.64e-6, 'Wzpl':22.75e-6, 'iz':2.26e-2, 'iy':2.26e-2, 'It':83.2e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS70x70x2']= {'nmb':'SHS70x70x2', 'b':0.07, 'h':0.07, 'e':2e-3, 'P':4.34, 'A':5.53e-4, 'Iz':42e-8, 'Iy':42e-8, 'Wzel':11.99e-6, 'Wzpl':13.88e-6, 'iz':2.76e-2, 'iy':2.76e-2, 'It':62.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS70x70x3']= {'nmb':'SHS70x70x3', 'b':0.07, 'h':0.07, 'e':3e-3, 'P':6.43, 'A':8.2e-4, 'Iz':60.3e-8, 'Iy':60.3e-8, 'Wzel':17.22e-6, 'Wzpl':20.21e-6, 'iz':2.71e-2, 'iy':2.71e-2, 'It':90.2e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS70x70x4']= {'nmb':'SHS70x70x4', 'b':0.07, 'h':0.07, 'e':4e-3, 'P':8.48, 'A':10.8e-4, 'Iz':76.9e-8, 'Iy':76.9e-8, 'Wzel':21.98e-6, 'Wzpl':26.17e-6, 'iz':2.67e-2, 'iy':2.67e-2, 'It':115e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS70x70x5']= {'nmb':'SHS70x70x5', 'b':0.07, 'h':0.07, 'e':5e-3, 'P':10.48, 'A':13.35e-4, 'Iz':92.1e-8, 'Iy':92.1e-8, 'Wzel':26.31e-6, 'Wzpl':31.75e-6, 'iz':2.63e-2, 'iy':2.63e-2, 'It':137.3e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS75x75x2']= {'nmb':'SHS75x75x2', 'b':0.075, 'h':0.075, 'e':2e-3, 'P':4.54, 'A':5.78e-4, 'Iz':51.9e-8, 'Iy':51.9e-8, 'Wzel':13.84e-6, 'Wzpl':15.99e-6, 'iz':3e-2, 'iy':3e-2, 'It':77.8e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS75x75x3']= {'nmb':'SHS75x75x3', 'b':0.075, 'h':0.075, 'e':3e-3, 'P':6.73, 'A':8.57e-4, 'Iz':74.8e-8, 'Iy':74.8e-8, 'Wzel':19.94e-6, 'Wzpl':23.34e-6, 'iz':2.95e-2, 'iy':2.95e-2, 'It':112e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS75x75x4']= {'nmb':'SHS75x75x4', 'b':0.075, 'h':0.075, 'e':4e-3, 'P':8.87, 'A':11.3e-4, 'Iz':95.7e-8, 'Iy':95.7e-8, 'Wzel':25.53e-6, 'Wzpl':30.28e-6, 'iz':2.91e-2, 'iy':2.91e-2, 'It':143.2e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS75x75x5']= {'nmb':'SHS75x75x5', 'b':0.075, 'h':0.075, 'e':5e-3, 'P':10.97, 'A':13.97e-4, 'Iz':114.9e-8, 'Iy':114.9e-8, 'Wzel':30.64e-6, 'Wzpl':36.81e-6, 'iz':2.87e-2, 'iy':2.87e-2, 'It':171.5e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS80x80x2']= {'nmb':'SHS80x80x2', 'b':0.08, 'h':0.08, 'e':2e-3, 'P':4.83, 'A':6.15e-4, 'Iz':63.3e-8, 'Iy':63.3e-8, 'Wzel':15.83e-6, 'Wzpl':18.26e-6, 'iz':3.21e-2, 'iy':3.21e-2, 'It':94.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS80x80x3']= {'nmb':'SHS80x80x3', 'b':0.08, 'h':0.08, 'e':3e-3, 'P':7.17, 'A':9.14e-4, 'Iz':91.4e-8, 'Iy':91.4e-8, 'Wzel':22.86e-6, 'Wzpl':26.69e-6, 'iz':3.16e-2, 'iy':3.16e-2, 'It':137e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS80x80x4']= {'nmb':'SHS80x80x4', 'b':0.08, 'h':0.08, 'e':4e-3, 'P':9.47, 'A':12.06e-4, 'Iz':117.4e-8, 'Iy':117.4e-8, 'Wzel':29.35e-6, 'Wzpl':34.69e-6, 'iz':3.12e-2, 'iy':3.12e-2, 'It':175.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS80x80x5']= {'nmb':'SHS80x80x5', 'b':0.08, 'h':0.08, 'e':5e-3, 'P':11.71, 'A':14.92e-4, 'Iz':141.3e-8, 'Iy':141.3e-8, 'Wzel':35.31e-6, 'Wzpl':42.25e-6, 'iz':3.08e-2, 'iy':3.08e-2, 'It':210.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS80x80x6']= {'nmb':'SHS80x80x6', 'b':0.08, 'h':0.08, 'e':6e-3, 'P':13.9, 'A':17.71e-4, 'Iz':163.2e-8, 'Iy':163.2e-8, 'Wzel':40.79e-6, 'Wzpl':49.39e-6, 'iz':3.04e-2, 'iy':3.04e-2, 'It':243.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS90x90x2']= {'nmb':'SHS90x90x2', 'b':0.09, 'h':0.09, 'e':2e-3, 'P':5.57, 'A':7.1e-4, 'Iz':90.9e-8, 'Iy':90.9e-8, 'Wzel':20.2e-6, 'Wzpl':23.24e-6, 'iz':3.58e-2, 'iy':3.58e-2, 'It':136.3e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS90x90x3']= {'nmb':'SHS90x90x3', 'b':0.09, 'h':0.09, 'e':3e-3, 'P':8.28, 'A':10.55e-4, 'Iz':131.9e-8, 'Iy':131.9e-8, 'Wzel':29.3e-6, 'Wzpl':34.07e-6, 'iz':3.54e-2, 'iy':3.54e-2, 'It':197.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS90x90x4']= {'nmb':'SHS90x90x4', 'b':0.09, 'h':0.09, 'e':4e-3, 'P':10.94, 'A':13.94e-4, 'Iz':170e-8, 'Iy':170e-8, 'Wzel':37.77e-6, 'Wzpl':44.41e-6, 'iz':3.49e-2, 'iy':3.49e-2, 'It':254.4e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS90x90x5']= {'nmb':'SHS90x90x5', 'b':0.09, 'h':0.09, 'e':5e-3, 'P':13.56, 'A':17.27e-4, 'Iz':205.4e-8, 'Iy':205.4e-8, 'Wzel':45.65e-6, 'Wzpl':54.25e-6, 'iz':3.45e-2, 'iy':3.45e-2, 'It':307.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS90x90x6']= {'nmb':'SHS90x90x6', 'b':0.09, 'h':0.09, 'e':6e-3, 'P':16.12, 'A':20.54e-4, 'Iz':238.3e-8, 'Iy':238.3e-8, 'Wzel':52.95e-6, 'Wzpl':63.61e-6, 'iz':3.41e-2, 'iy':3.41e-2, 'It':355.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS100x100x3']= {'nmb':'SHS100x100x3', 'b':0.1, 'h':0.1, 'e':3e-3, 'P':9.02, 'A':11.49e-4, 'Iz':182.7e-8, 'Iy':182.7e-8, 'Wzel':36.54e-6, 'Wzpl':42.35e-6, 'iz':3.99e-2, 'iy':3.99e-2, 'It':273.8e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS100x100x4']= {'nmb':'SHS100x100x4', 'b':0.1, 'h':0.1, 'e':4e-3, 'P':11.93, 'A':15.2e-4, 'Iz':236.3e-8, 'Iy':236.3e-8, 'Wzel':47.27e-6, 'Wzpl':55.33e-6, 'iz':3.94e-2, 'iy':3.94e-2, 'It':353.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS100x100x5']= {'nmb':'SHS100x100x5', 'b':0.1, 'h':0.1, 'e':5e-3, 'P':14.79, 'A':18.84e-4, 'Iz':286.6e-8, 'Iy':286.6e-8, 'Wzel':57.32e-6, 'Wzpl':67.75e-6, 'iz':3.9e-2, 'iy':3.9e-2, 'It':428.7e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS100x100x6']= {'nmb':'SHS100x100x6', 'b':0.1, 'h':0.1, 'e':6e-3, 'P':17.6, 'A':22.42e-4, 'Iz':333.6e-8, 'Iy':333.6e-8, 'Wzel':66.72e-6, 'Wzpl':79.63e-6, 'iz':3.86e-2, 'iy':3.86e-2, 'It':498.4e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS100x100x7']= {'nmb':'SHS100x100x7', 'b':0.1, 'h':0.1, 'e':7e-3, 'P':20.36, 'A':25.94e-4, 'Iz':377.5e-8, 'Iy':377.5e-8, 'Wzel':75.5e-6, 'Wzpl':90.99e-6, 'iz':3.82e-2, 'iy':3.82e-2, 'It':563e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS110x110x3']= {'nmb':'SHS110x110x3', 'b':0.11, 'h':0.11, 'e':3e-3, 'P':9.76, 'A':12.43e-4, 'Iz':245.2e-8, 'Iy':245.2e-8, 'Wzel':44.58e-6, 'Wzpl':51.53e-6, 'iz':4.44e-2, 'iy':4.44e-2, 'It':367.5e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS110x110x4']= {'nmb':'SHS110x110x4', 'b':0.11, 'h':0.11, 'e':4e-3, 'P':12.92, 'A':16.45e-4, 'Iz':318.1e-8, 'Iy':318.1e-8, 'Wzel':57.83e-6, 'Wzpl':67.45e-6, 'iz':4.4e-2, 'iy':4.4e-2, 'It':476.4e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS110x110x5']= {'nmb':'SHS110x110x5', 'b':0.11, 'h':0.11, 'e':5e-3, 'P':16.02, 'A':20.41e-4, 'Iz':386.8e-8, 'Iy':386.8e-8, 'Wzel':70.32e-6, 'Wzpl':82.75e-6, 'iz':4.35e-2, 'iy':4.35e-2, 'It':578.8e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS110x110x6']= {'nmb':'SHS110x110x6', 'b':0.11, 'h':0.11, 'e':6e-3, 'P':19.08, 'A':24.3e-4, 'Iz':451.4e-8, 'Iy':451.4e-8, 'Wzel':82.08e-6, 'Wzpl':97.45e-6, 'iz':4.31e-2, 'iy':4.31e-2, 'It':674.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS110x110x7']= {'nmb':'SHS110x110x7', 'b':0.11, 'h':0.11, 'e':7e-3, 'P':22.09, 'A':28.13e-4, 'Iz':512.3e-8, 'Iy':512.3e-8, 'Wzel':93.14e-6, 'Wzpl':111.57e-6, 'iz':4.27e-2, 'iy':4.27e-2, 'It':764.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS120x120x3']= {'nmb':'SHS120x120x3', 'b':0.12, 'h':0.12, 'e':3e-3, 'P':10.87, 'A':13.85e-4, 'Iz':320.5e-8, 'Iy':320.5e-8, 'Wzel':53.42e-6, 'Wzpl':61.61e-6, 'iz':4.81e-2, 'iy':4.81e-2, 'It':480.5e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS120x120x4']= {'nmb':'SHS120x120x4', 'b':0.12, 'h':0.12, 'e':4e-3, 'P':14.4, 'A':18.34e-4, 'Iz':416.7e-8, 'Iy':416.7e-8, 'Wzel':69.46e-6, 'Wzpl':80.77e-6, 'iz':4.77e-2, 'iy':4.77e-2, 'It':624.4e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS120x120x5']= {'nmb':'SHS120x120x5', 'b':0.12, 'h':0.12, 'e':5e-3, 'P':17.87, 'A':22.77e-4, 'Iz':507.9e-8, 'Iy':507.9e-8, 'Wzel':84.65e-6, 'Wzpl':99.25e-6, 'iz':4.72e-2, 'iy':4.72e-2, 'It':760.4e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS120x120x6']= {'nmb':'SHS120x120x6', 'b':0.12, 'h':0.12, 'e':6e-3, 'P':21.3, 'A':27.13e-4, 'Iz':594.3e-8, 'Iy':594.3e-8, 'Wzel':99.04e-6, 'Wzpl':117.07e-6, 'iz':4.68e-2, 'iy':4.68e-2, 'It':888.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS120x120x7']= {'nmb':'SHS120x120x7', 'b':0.12, 'h':0.12, 'e':7e-3, 'P':24.67, 'A':31.43e-4, 'Iz':675.9e-8, 'Iy':675.9e-8, 'Wzel':112.66e-6, 'Wzpl':134.25e-6, 'iz':4.64e-2, 'iy':4.64e-2, 'It':1010e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS125x125x3']= {'nmb':'SHS125x125x3', 'b':0.125, 'h':0.125, 'e':3e-3, 'P':11.24, 'A':14.32e-4, 'Iz':363.4e-8, 'Iy':363.4e-8, 'Wzel':58.14e-6, 'Wzpl':66.99e-6, 'iz':5.04e-2, 'iy':5.04e-2, 'It':544.8e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS125x125x4']= {'nmb':'SHS125x125x4', 'b':0.125, 'h':0.125, 'e':4e-3, 'P':14.89, 'A':18.97e-4, 'Iz':472.9e-8, 'Iy':472.9e-8, 'Wzel':75.67e-6, 'Wzpl':87.88e-6, 'iz':4.99e-2, 'iy':4.99e-2, 'It':708.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS125x125x5']= {'nmb':'SHS125x125x5', 'b':0.125, 'h':0.125, 'e':5e-3, 'P':18.49, 'A':23.55e-4, 'Iz':577e-8, 'Iy':577e-8, 'Wzel':92.32e-6, 'Wzpl':108.06e-6, 'iz':4.95e-2, 'iy':4.95e-2, 'It':864e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS125x125x6']= {'nmb':'SHS125x125x6', 'b':0.125, 'h':0.125, 'e':6e-3, 'P':22.04, 'A':28.07e-4, 'Iz':675.8e-8, 'Iy':675.8e-8, 'Wzel':108.12e-6, 'Wzpl':127.56e-6, 'iz':4.91e-2, 'iy':4.91e-2, 'It':1011.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS125x125x7']= {'nmb':'SHS125x125x7', 'b':0.125, 'h':0.125, 'e':7e-3, 'P':25.54, 'A':32.53e-4, 'Iz':769.4e-8, 'Iy':769.4e-8, 'Wzel':123.11e-6, 'Wzpl':146.37e-6, 'iz':4.86e-2, 'iy':4.86e-2, 'It':1150.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS127x127x3']= {'nmb':'SHS127x127x3', 'b':0.127, 'h':0.127, 'e':3e-3, 'P':11.54, 'A':14.7e-4, 'Iz':381.5e-8, 'Iy':381.5e-8, 'Wzel':60.09e-6, 'Wzpl':69.21e-6, 'iz':5.1e-2, 'iy':5.1e-2, 'It':572e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS127x127x4']= {'nmb':'SHS127x127x4', 'b':0.127, 'h':0.127, 'e':4e-3, 'P':15.28, 'A':19.47e-4, 'Iz':496.8e-8, 'Iy':496.8e-8, 'Wzel':78.23e-6, 'Wzpl':90.81e-6, 'iz':5.05e-2, 'iy':5.05e-2, 'It':744.3e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS127x127x5']= {'nmb':'SHS127x127x5', 'b':0.127, 'h':0.127, 'e':5e-3, 'P':18.98, 'A':24.18e-4, 'Iz':606.3e-8, 'Iy':606.3e-8, 'Wzel':95.48e-6, 'Wzpl':111.69e-6, 'iz':5.01e-2, 'iy':5.01e-2, 'It':907.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS127x127x6']= {'nmb':'SHS127x127x6', 'b':0.127, 'h':0.127, 'e':6e-3, 'P':22.63, 'A':28.83e-4, 'Iz':710.4e-8, 'Iy':710.4e-8, 'Wzel':111.87e-6, 'Wzpl':131.88e-6, 'iz':4.96e-2, 'iy':4.96e-2, 'It':1062.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS127x127x7']= {'nmb':'SHS127x127x7', 'b':0.127, 'h':0.127, 'e':7e-3, 'P':26.23, 'A':33.41e-4, 'Iz':809.1e-8, 'Iy':809.1e-8, 'Wzel':127.42e-6, 'Wzpl':151.37e-6, 'iz':4.92e-2, 'iy':4.92e-2, 'It':1209.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS135x135x3']= {'nmb':'SHS135x135x3', 'b':0.135, 'h':0.135, 'e':3e-3, 'P':11.98, 'A':15.26e-4, 'Iz':460.2e-8, 'Iy':460.2e-8, 'Wzel':68.18e-6, 'Wzpl':78.42e-6, 'iz':5.49e-2, 'iy':5.49e-2, 'It':690e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS135x135x4']= {'nmb':'SHS135x135x4', 'b':0.135, 'h':0.135, 'e':4e-3, 'P':15.87, 'A':20.22e-4, 'Iz':600e-8, 'Iy':600e-8, 'Wzel':88.9e-6, 'Wzpl':103e-6, 'iz':5.45e-2, 'iy':5.45e-2, 'It':899.2e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS135x135x5']= {'nmb':'SHS135x135x5', 'b':0.135, 'h':0.135, 'e':5e-3, 'P':19.72, 'A':25.12e-4, 'Iz':733.4e-8, 'Iy':733.4e-8, 'Wzel':108.65e-6, 'Wzpl':126.81e-6, 'iz':5.4e-2, 'iy':5.4e-2, 'It':1098.5e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS135x135x6']= {'nmb':'SHS135x135x6', 'b':0.135, 'h':0.135, 'e':6e-3, 'P':23.52, 'A':29.96e-4, 'Iz':860.5e-8, 'Iy':860.5e-8, 'Wzel':127.49e-6, 'Wzpl':149.88e-6, 'iz':5.36e-2, 'iy':5.36e-2, 'It':1288e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS135x135x7']= {'nmb':'SHS135x135x7', 'b':0.135, 'h':0.135, 'e':7e-3, 'P':27.26, 'A':34.73e-4, 'Iz':981.6e-8, 'Iy':981.6e-8, 'Wzel':145.42e-6, 'Wzpl':172.2e-6, 'iz':5.32e-2, 'iy':5.32e-2, 'It':1468e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS140x140x4']= {'nmb':'SHS140x140x4', 'b':0.14, 'h':0.14, 'e':4e-3, 'P':16.86, 'A':21.48e-4, 'Iz':671.4e-8, 'Iy':671.4e-8, 'Wzel':95.91e-6, 'Wzpl':111.01e-6, 'iz':5.59e-2, 'iy':5.59e-2, 'It':1006.2e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS140x140x5']= {'nmb':'SHS140x140x5', 'b':0.14, 'h':0.14, 'e':5e-3, 'P':20.95, 'A':26.69e-4, 'Iz':821.3e-8, 'Iy':821.3e-8, 'Wzel':117.32e-6, 'Wzpl':136.75e-6, 'iz':5.55e-2, 'iy':5.55e-2, 'It':1230.2e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS140x140x6']= {'nmb':'SHS140x140x6', 'b':0.14, 'h':0.14, 'e':6e-3, 'P':25, 'A':31.84e-4, 'Iz':964.4e-8, 'Iy':964.4e-8, 'Wzel':137.77e-6, 'Wzpl':161.71e-6, 'iz':5.5e-2, 'iy':5.5e-2, 'It':1443.7e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS140x140x7']= {'nmb':'SHS140x140x7', 'b':0.14, 'h':0.14, 'e':7e-3, 'P':28.99, 'A':36.93e-4, 'Iz':1100.9e-8, 'Iy':1100.9e-8, 'Wzel':157.28e-6, 'Wzpl':185.91e-6, 'iz':5.46e-2, 'iy':5.46e-2, 'It':1646.8e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS140x140x8']= {'nmb':'SHS140x140x8', 'b':0.14, 'h':0.14, 'e':8e-3, 'P':32.93, 'A':41.95e-4, 'Iz':1231.2e-8, 'Iy':1231.2e-8, 'Wzel':175.88e-6, 'Wzpl':209.34e-6, 'iz':5.42e-2, 'iy':5.42e-2, 'It':1840e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS150x150x4']= {'nmb':'SHS150x150x4', 'b':0.15, 'h':0.15, 'e':4e-3, 'P':18.14, 'A':23.11e-4, 'Iz':830.5e-8, 'Iy':830.5e-8, 'Wzel':110.74e-6, 'Wzpl':127.93e-6, 'iz':5.99e-2, 'iy':5.99e-2, 'It':1244.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS150x150x5']= {'nmb':'SHS150x150x5', 'b':0.15, 'h':0.15, 'e':5e-3, 'P':22.55, 'A':28.73e-4, 'Iz':1017.4e-8, 'Iy':1017.4e-8, 'Wzel':135.66e-6, 'Wzpl':157.75e-6, 'iz':5.95e-2, 'iy':5.95e-2, 'It':1524.3e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS150x150x6']= {'nmb':'SHS150x150x6', 'b':0.15, 'h':0.15, 'e':6e-3, 'P':26.92, 'A':34.29e-4, 'Iz':1196.5e-8, 'Iy':1196.5e-8, 'Wzel':159.53e-6, 'Wzpl':186.73e-6, 'iz':5.91e-2, 'iy':5.91e-2, 'It':1791.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS150x150x7']= {'nmb':'SHS150x150x7', 'b':0.15, 'h':0.15, 'e':7e-3, 'P':31.23, 'A':39.78e-4, 'Iz':1367.9e-8, 'Iy':1367.9e-8, 'Wzel':182.39e-6, 'Wzpl':214.89e-6, 'iz':5.86e-2, 'iy':5.86e-2, 'It':2046.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS150x150x8']= {'nmb':'SHS150x150x8', 'b':0.15, 'h':0.15, 'e':8e-3, 'P':35.5, 'A':45.22e-4, 'Iz':1531.9e-8, 'Iy':1531.9e-8, 'Wzel':204.26e-6, 'Wzpl':242.22e-6, 'iz':5.82e-2, 'iy':5.82e-2, 'It':2290.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS160x160x4']= {'nmb':'SHS160x160x4', 'b':0.16, 'h':0.16, 'e':4e-3, 'P':19.33, 'A':24.62e-4, 'Iz':1013e-8, 'Iy':1013e-8, 'Wzel':126.63e-6, 'Wzpl':146.05e-6, 'iz':6.41e-2, 'iy':6.41e-2, 'It':1518.6e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS160x160x5']= {'nmb':'SHS160x160x5', 'b':0.16, 'h':0.16, 'e':5e-3, 'P':24.03, 'A':30.62e-4, 'Iz':1242.6e-8, 'Iy':1242.6e-8, 'Wzel':155.32e-6, 'Wzpl':180.25e-6, 'iz':6.37e-2, 'iy':6.37e-2, 'It':1861.9e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS160x160x6']= {'nmb':'SHS160x160x6', 'b':0.16, 'h':0.16, 'e':6e-3, 'P':28.69, 'A':36.55e-4, 'Iz':1463.1e-8, 'Iy':1463.1e-8, 'Wzel':182.89e-6, 'Wzpl':213.55e-6, 'iz':6.33e-2, 'iy':6.33e-2, 'It':2191.4e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS160x160x7']= {'nmb':'SHS160x160x7', 'b':0.16, 'h':0.16, 'e':7e-3, 'P':33.3, 'A':42.42e-4, 'Iz':1674.9e-8, 'Iy':1674.9e-8, 'Wzel':209.36e-6, 'Wzpl':245.97e-6, 'iz':6.28e-2, 'iy':6.28e-2, 'It':2507.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS160x160x8']= {'nmb':'SHS160x160x8', 'b':0.16, 'h':0.16, 'e':8e-3, 'P':37.86, 'A':48.23e-4, 'Iz':1878.2e-8, 'Iy':1878.2e-8, 'Wzel':234.77e-6, 'Wzpl':277.5e-6, 'iz':6.24e-2, 'iy':6.24e-2, 'It':2809.4e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS175x175x5']= {'nmb':'SHS175x175x5', 'b':0.175, 'h':0.175, 'e':5e-3, 'P':26.39, 'A':33.61e-4, 'Iz':1639.1e-8, 'Iy':1639.1e-8, 'Wzel':187.32e-6, 'Wzpl':216.81e-6, 'iz':6.98e-2, 'iy':6.98e-2, 'It':2456.5e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS175x175x6']= {'nmb':'SHS175x175x6', 'b':0.175, 'h':0.175, 'e':6e-3, 'P':31.52, 'A':40.15e-4, 'Iz':1933.2e-8, 'Iy':1933.2e-8, 'Wzel':220.93e-6, 'Wzpl':257.16e-6, 'iz':6.94e-2, 'iy':6.94e-2, 'It':2896.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS175x175x7']= {'nmb':'SHS175x175x7', 'b':0.175, 'h':0.175, 'e':7e-3, 'P':36.6, 'A':46.62e-4, 'Iz':2216.6e-8, 'Iy':2216.6e-8, 'Wzel':253.33e-6, 'Wzpl':296.52e-6, 'iz':6.9e-2, 'iy':6.9e-2, 'It':3319.1e-8, 'E':210000e6, 'nu':0.3}
SHSprofiles['SHS175x175x8']= {'nmb':'SHS175x175x8', 'b':0.175, 'h':0.175, 'e':8e-3, 'P':41.63, 'A':53.03e-4, 'Iz':2489.7e-8, 'Iy':2489.7e-8, 'Wzel':284.53e-6, 'Wzpl':334.92e-6, 'iz':6.85e-2, 'iy':6.85e-2, 'It':3726e-8, 'E':210000e6, 'nu':0.3}

for item in SHSprofiles:
  profile= SHSprofiles[item]
  A= profile['A']
  E= profile['E']
  nu= profile['nu']
  b= profile['b']
  h= profile['h']
  e= profile['e']
  profile['alpha']= 0.5*5/6.0
  profile['G']= E/(2*(1+nu))
  profile['AreaQy']= 2*0.7*h*e
  profile['AreaQz']= 2*0.7*b*e
  profile['Wyel']= profile['Wzel']
  profile['Wypl']= profile['Wzpl']
