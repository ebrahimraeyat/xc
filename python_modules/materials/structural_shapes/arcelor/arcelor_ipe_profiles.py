# -*- coding: utf-8 -*-
''' Arcelor IPE steel shapes.'''

# European I beams

# Ejes de la sección:

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

# XXX Repasar coeficientes de distorsión
#    alpha-> alphaZ,alphaY

IPEprofiles= {}

IPEprofiles['IPE_A_100']= {'nmb':'IPE_A_100', 'P':6.9, 'h':98e-3, 'b':55e-3, 'tw':3.6e-3, 'tf':4.7e-3, 'r':7e-3, 'A':8.78e-4, 'hi':88.6e-3, 'd':74.6e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.397, 'AG':57.57, 'Iz':141.2e-8, 'Wzel':28.81e-6, 'Wzpl':32.98e-6, 'iz':4.01e-2, 'Avy':4.44e-4, 'Iy':13.12e-8, 'Wyel':4.77e-6, 'Wypl':7.54e-6, 'iy':1.22e-2, 'Ss':21.2e-3, 'It':0.77e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_100']= {'nmb':'IPE_100', 'P':8.1, 'h':100e-3, 'b':55e-3, 'tw':4.1e-3, 'tf':5.7e-3, 'r':7e-3, 'A':10.32e-4, 'hi':88.6e-3, 'd':74.6e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.4, 'AG':49.33, 'Iz':171e-8, 'Wzel':34.2e-6, 'Wzpl':39.41e-6, 'iz':4.07e-2, 'Avy':5.08e-4, 'Iy':15.92e-8, 'Wyel':5.79e-6, 'Wypl':9.15e-6, 'iy':1.24e-2, 'Ss':23.7e-3, 'It':1.2e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_120']= {'nmb':'IPE_A_120', 'P':8.7, 'h':117.6e-3, 'b':64e-3, 'tw':3.8e-3, 'tf':5.1e-3, 'r':7e-3, 'A':11.03e-4, 'hi':107.4e-3, 'd':93.4e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.472, 'AG':54.47, 'Iz':257.4e-8, 'Wzel':43.77e-6, 'Wzpl':49.87e-6, 'iz':4.83e-2, 'Avy':5.41e-4, 'Iy':22.39e-8, 'Wyel':7e-6, 'Wypl':10.98e-6, 'iy':1.42e-2, 'Ss':22.2e-3, 'It':1.04e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_120']= {'nmb':'IPE_120', 'P':10.4, 'h':120e-3, 'b':64e-3, 'tw':4.4e-3, 'tf':6.3e-3, 'r':7e-3, 'A':13.21e-4, 'hi':107.4e-3, 'd':93.4e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.475, 'AG':45.82, 'Iz':317.8e-8, 'Wzel':52.96e-6, 'Wzpl':60.73e-6, 'iz':4.9e-2, 'Avy':6.31e-4, 'Iy':27.67e-8, 'Wyel':8.65e-6, 'Wypl':13.58e-6, 'iy':1.45e-2, 'Ss':25.2e-3, 'It':1.74e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_140']= {'nmb':'IPE_A_140', 'P':10.5, 'h':137.4e-3, 'b':73e-3, 'tw':3.8e-3, 'tf':5.6e-3, 'r':7e-3, 'A':13.39e-4, 'hi':126.2e-3, 'd':112.2e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.547, 'AG':52.05, 'Iz':434.9e-8, 'Wzel':63.3e-6, 'Wzpl':71.6e-6, 'iz':5.7e-2, 'Avy':6.21e-4, 'Iy':36.42e-8, 'Wyel':9.98e-6, 'Wypl':15.52e-6, 'iy':1.65e-2, 'Ss':23.2e-3, 'It':1.36e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_140']= {'nmb':'IPE_140', 'P':12.9, 'h':140e-3, 'b':73e-3, 'tw':4.7e-3, 'tf':6.9e-3, 'r':7e-3, 'A':16.43e-4, 'hi':126.2e-3, 'd':112.2e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.551, 'AG':42.7, 'Iz':541.2e-8, 'Wzel':77.32e-6, 'Wzpl':88.34e-6, 'iz':5.74e-2, 'Avy':7.64e-4, 'Iy':44.92e-8, 'Wyel':12.31e-6, 'Wypl':19.25e-6, 'iy':1.65e-2, 'Ss':26.7e-3, 'It':2.45e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_160']= {'nmb':'IPE_A_160', 'P':12.7, 'h':157e-3, 'b':82e-3, 'tw':4e-3, 'tf':5.9e-3, 'r':9e-3, 'A':16.18e-4, 'hi':145.2e-3, 'd':127.2e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.619, 'AG':48.7, 'Iz':689.3e-8, 'Wzel':87.81e-6, 'Wzpl':99.09e-6, 'iz':6.53e-2, 'Avy':7.8e-4, 'Iy':54.43e-8, 'Wyel':13.27e-6, 'Wypl':20.7e-6, 'iy':1.83e-2, 'Ss':26.34e-3, 'It':1.96e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_160']= {'nmb':'IPE_160', 'P':15.8, 'h':160e-3, 'b':82e-3, 'tw':5e-3, 'tf':7.4e-3, 'r':9e-3, 'A':20.09e-4, 'hi':145.2e-3, 'd':127.2e-3, 'FI':'-', 'Pmin':0e-3, 'Pmax':0e-3, 'AL':0.623, 'AG':39.47, 'Iz':869.3e-8, 'Wzel':108.7e-6, 'Wzpl':123.9e-6, 'iz':6.58e-2, 'Avy':9.66e-4, 'Iy':68.31e-8, 'Wyel':16.66e-6, 'Wypl':26.1e-6, 'iy':1.84e-2, 'Ss':30.34e-3, 'It':3.6e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_180']= {'nmb':'IPE_A_180', 'P':15.4, 'h':177e-3, 'b':91e-3, 'tw':4.3e-3, 'tf':6.5e-3, 'r':9e-3, 'A':19.58e-4, 'hi':164e-3, 'd':146e-3, 'FI':'M10', 'Pmin':48e-3, 'Pmax':48e-3, 'AL':0.694, 'AG':45.15, 'Iz':1063e-8, 'Wzel':120.1e-6, 'Wzpl':135.3e-6, 'iz':7.37e-2, 'Avy':9.2e-4, 'Iy':81.89e-8, 'Wyel':18e-6, 'Wypl':27.96e-6, 'iy':2.05e-2, 'Ss':27.84e-3, 'It':2.7e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_180']= {'nmb':'IPE_180', 'P':18.8, 'h':180e-3, 'b':91e-3, 'tw':5.3e-3, 'tf':8e-3, 'r':9e-3, 'A':23.95e-4, 'hi':164e-3, 'd':146e-3, 'FI':'M10', 'Pmin':48e-3, 'Pmax':48e-3, 'AL':0.698, 'AG':37.13, 'Iz':1317e-8, 'Wzel':146.3e-6, 'Wzpl':166.4e-6, 'iz':7.42e-2, 'Avy':11.25e-4, 'Iy':100.9e-8, 'Wyel':22.16e-6, 'Wypl':34.6e-6, 'iy':2.05e-2, 'Ss':31.84e-3, 'It':4.79e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_180+']= {'nmb':'IPE_O_180+', 'P':21.3, 'h':182e-3, 'b':92e-3, 'tw':6e-3, 'tf':9e-3, 'r':9e-3, 'A':27.1e-4, 'hi':164e-3, 'd':146e-3, 'FI':'M10', 'Pmin':50e-3, 'Pmax':50e-3, 'AL':0.705, 'AG':33.12, 'Iz':1505e-8, 'Wzel':165.4e-6, 'Wzpl':189.1e-6, 'iz':7.45e-2, 'Avy':12.7e-4, 'Iy':117.3e-8, 'Wyel':25.5e-6, 'Wypl':39.91e-6, 'iy':2.08e-2, 'Ss':34.54e-3, 'It':6.76e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_200']= {'nmb':'IPE_A_200', 'P':18.4, 'h':197e-3, 'b':100e-3, 'tw':4.5e-3, 'tf':7e-3, 'r':12e-3, 'A':23.47e-4, 'hi':183e-3, 'd':159e-3, 'FI':'M10', 'Pmin':54e-3, 'Pmax':58e-3, 'AL':0.764, 'AG':41.49, 'Iz':1591e-8, 'Wzel':161.6e-6, 'Wzpl':181.7e-6, 'iz':8.23e-2, 'Avy':11.47e-4, 'Iy':117.2e-8, 'Wyel':23.43e-6, 'Wypl':36.54e-6, 'iy':2.23e-2, 'Ss':32.56e-3, 'It':4.11e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_200']= {'nmb':'IPE_200', 'P':22.4, 'h':200e-3, 'b':100e-3, 'tw':5.6e-3, 'tf':8.5e-3, 'r':12e-3, 'A':28.48e-4, 'hi':183e-3, 'd':159e-3, 'FI':'M10', 'Pmin':54e-3, 'Pmax':58e-3, 'AL':0.768, 'AG':34.36, 'Iz':1943e-8, 'Wzel':194.3e-6, 'Wzpl':220.6e-6, 'iz':8.26e-2, 'Avy':14e-4, 'Iy':142.4e-8, 'Wyel':28.47e-6, 'Wypl':44.61e-6, 'iy':2.24e-2, 'Ss':36.66e-3, 'It':6.98e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_200+']= {'nmb':'IPE_O_200+', 'P':25.1, 'h':202e-3, 'b':102e-3, 'tw':6.2e-3, 'tf':9.5e-3, 'r':12e-3, 'A':31.96e-4, 'hi':183e-3, 'd':159e-3, 'FI':'M10', 'Pmin':56e-3, 'Pmax':60e-3, 'AL':0.779, 'AG':31.05, 'Iz':2211e-8, 'Wzel':218.9e-6, 'Wzpl':249.4e-6, 'iz':8.32e-2, 'Avy':15.45e-4, 'Iy':168.9e-8, 'Wyel':33.11e-6, 'Wypl':51.89e-6, 'iy':2.3e-2, 'Ss':39.26e-3, 'It':9.45e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_220']= {'nmb':'IPE_A_220', 'P':22.2, 'h':217e-3, 'b':110e-3, 'tw':5e-3, 'tf':7.7e-3, 'r':12e-3, 'A':28.26e-4, 'hi':201.6e-3, 'd':177.6e-3, 'FI':'M12', 'Pmin':60e-3, 'Pmax':62e-3, 'AL':0.843, 'AG':38.02, 'Iz':2317e-8, 'Wzel':213.5e-6, 'Wzpl':240.2e-6, 'iz':9.05e-2, 'Avy':13.55e-4, 'Iy':171.4e-8, 'Wyel':31.17e-6, 'Wypl':48.49e-6, 'iy':2.46e-2, 'Ss':34.46e-3, 'It':5.69e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_220']= {'nmb':'IPE_220', 'P':26.2, 'h':220e-3, 'b':110e-3, 'tw':5.9e-3, 'tf':9.2e-3, 'r':12e-3, 'A':33.37e-4, 'hi':201.6e-3, 'd':177.6e-3, 'FI':'M12', 'Pmin':60e-3, 'Pmax':62e-3, 'AL':0.848, 'AG':32.36, 'Iz':2772e-8, 'Wzel':252e-6, 'Wzpl':285.4e-6, 'iz':9.11e-2, 'Avy':15.88e-4, 'Iy':204.9e-8, 'Wyel':37.25e-6, 'Wypl':58.11e-6, 'iy':2.48e-2, 'Ss':38.36e-3, 'It':9.07e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_220+']= {'nmb':'IPE_O_220+', 'P':29.4, 'h':222e-3, 'b':112e-3, 'tw':6.6e-3, 'tf':10.2e-3, 'r':12e-3, 'A':37.39e-4, 'hi':201.6e-3, 'd':177.6e-3, 'FI':'M10', 'Pmin':58e-3, 'Pmax':66e-3, 'AL':0.858, 'AG':29.24, 'Iz':3134e-8, 'Wzel':282.3e-6, 'Wzpl':321.1e-6, 'iz':9.16e-2, 'Avy':17.66e-4, 'Iy':239.8e-8, 'Wyel':42.83e-6, 'Wypl':66.91e-6, 'iy':2.53e-2, 'Ss':41.06e-3, 'It':12.27e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_240']= {'nmb':'IPE_A_240', 'P':26.2, 'h':237e-3, 'b':120e-3, 'tw':5.2e-3, 'tf':8.3e-3, 'r':15e-3, 'A':33.31e-4, 'hi':220.4e-3, 'd':190.4e-3, 'FI':'M12', 'Pmin':64e-3, 'Pmax':68e-3, 'AL':0.918, 'AG':35.1, 'Iz':3290e-8, 'Wzel':277.7e-6, 'Wzpl':311.6e-6, 'iz':9.94e-2, 'Avy':16.31e-4, 'Iy':240.1e-8, 'Wyel':40.02e-6, 'Wypl':62.4e-6, 'iy':2.68e-2, 'Ss':39.37e-3, 'It':8.35e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_240']= {'nmb':'IPE_240', 'P':30.7, 'h':240e-3, 'b':120e-3, 'tw':6.2e-3, 'tf':9.8e-3, 'r':15e-3, 'A':39.12e-4, 'hi':220.4e-3, 'd':190.4e-3, 'FI':'M12', 'Pmin':66e-3, 'Pmax':68e-3, 'AL':0.922, 'AG':30.02, 'Iz':3892e-8, 'Wzel':324.3e-6, 'Wzpl':366.6e-6, 'iz':9.97e-2, 'Avy':19.14e-4, 'Iy':283.6e-8, 'Wyel':47.27e-6, 'Wypl':73.92e-6, 'iy':2.69e-2, 'Ss':43.37e-3, 'It':12.88e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_240+']= {'nmb':'IPE_O_240+', 'P':34.3, 'h':242e-3, 'b':122e-3, 'tw':7e-3, 'tf':10.8e-3, 'r':15e-3, 'A':43.71e-4, 'hi':220.4e-3, 'd':190.4e-3, 'FI':'M12', 'Pmin':66e-3, 'Pmax':70e-3, 'AL':0.932, 'AG':27.17, 'Iz':4369e-8, 'Wzel':361.1e-6, 'Wzpl':410.3e-6, 'iz':10e-2, 'Avy':21.36e-4, 'Iy':328.5e-8, 'Wyel':53.86e-6, 'Wypl':84.4e-6, 'iy':2.74e-2, 'Ss':46.17e-3, 'It':17.18e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_270']= {'nmb':'IPE_A_270', 'P':30.7, 'h':267e-3, 'b':135e-3, 'tw':5.5e-3, 'tf':8.7e-3, 'r':15e-3, 'A':39.15e-4, 'hi':249.6e-3, 'd':219.6e-3, 'FI':'M16', 'Pmin':70e-3, 'Pmax':72e-3, 'AL':1.037, 'AG':33.75, 'Iz':4917e-8, 'Wzel':368.3e-6, 'Wzpl':412.5e-6, 'iz':11.21e-2, 'Avy':18.75e-4, 'Iy':358e-8, 'Wyel':53.03e-6, 'Wypl':82.34e-6, 'iy':3.02e-2, 'Ss':40.47e-3, 'It':10.3e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_270']= {'nmb':'IPE_270', 'P':36.1, 'h':270e-3, 'b':135e-3, 'tw':6.6e-3, 'tf':10.2e-3, 'r':15e-3, 'A':45.95e-4, 'hi':249.6e-3, 'd':219.6e-3, 'FI':'M16', 'Pmin':72e-3, 'Pmax':72e-3, 'AL':1.041, 'AG':28.86, 'Iz':5790e-8, 'Wzel':428.9e-6, 'Wzpl':484e-6, 'iz':11.23e-2, 'Avy':22.14e-4, 'Iy':419.9e-8, 'Wyel':62.2e-6, 'Wypl':96.95e-6, 'iy':3.02e-2, 'Ss':44.57e-3, 'It':15.94e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_270+']= {'nmb':'IPE_O_270+', 'P':42.3, 'h':274e-3, 'b':136e-3, 'tw':7.5e-3, 'tf':12.2e-3, 'r':15e-3, 'A':53.84e-4, 'hi':249.6e-3, 'd':219.6e-3, 'FI':'M16', 'Pmin':72e-3, 'Pmax':72e-3, 'AL':1.051, 'AG':24.88, 'Iz':6947e-8, 'Wzel':507.1e-6, 'Wzpl':574.6e-6, 'iz':11.36e-2, 'Avy':25.23e-4, 'Iy':513.5e-8, 'Wyel':75.51e-6, 'Wypl':117.7e-6, 'iy':3.09e-2, 'Ss':49.47e-3, 'It':24.9e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_300']= {'nmb':'IPE_A_300', 'P':36.5, 'h':297e-3, 'b':150e-3, 'tw':6.1e-3, 'tf':9.2e-3, 'r':15e-3, 'A':46.53e-4, 'hi':278.6e-3, 'd':248.6e-3, 'FI':'M16', 'Pmin':72e-3, 'Pmax':86e-3, 'AL':1.156, 'AG':31.65, 'Iz':7173e-8, 'Wzel':483.1e-6, 'Wzpl':541.8e-6, 'iz':12.42e-2, 'Avy':22.25e-4, 'Iy':519e-8, 'Wyel':69.2e-6, 'Wypl':107.3e-6, 'iy':3.34e-2, 'Ss':42.07e-3, 'It':13.43e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_300']= {'nmb':'IPE_300', 'P':42.2, 'h':300e-3, 'b':150e-3, 'tw':7.1e-3, 'tf':10.7e-3, 'r':15e-3, 'A':53.81e-4, 'hi':278.6e-3, 'd':248.6e-3, 'FI':'M16', 'Pmin':72e-3, 'Pmax':86e-3, 'AL':1.16, 'AG':27.46, 'Iz':8356e-8, 'Wzel':557.1e-6, 'Wzpl':628.4e-6, 'iz':12.46e-2, 'Avy':25.68e-4, 'Iy':603.8e-8, 'Wyel':80.5e-6, 'Wypl':125.2e-6, 'iy':3.35e-2, 'Ss':46.07e-3, 'It':20.12e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_300+']= {'nmb':'IPE_O_300+', 'P':49.3, 'h':304e-3, 'b':152e-3, 'tw':8e-3, 'tf':12.7e-3, 'r':15e-3, 'A':62.83e-4, 'hi':278.6e-3, 'd':248.6e-3, 'FI':'M16', 'Pmin':74e-3, 'Pmax':88e-3, 'AL':1.174, 'AG':23.81, 'Iz':9994e-8, 'Wzel':657.5e-6, 'Wzpl':743.8e-6, 'iz':12.61e-2, 'Avy':29.05e-4, 'Iy':745.7e-8, 'Wyel':98.12e-6, 'Wypl':152.6e-6, 'iy':3.45e-2, 'Ss':50.97e-3, 'It':31.06e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_330']= {'nmb':'IPE_A_330', 'P':43, 'h':327e-3, 'b':160e-3, 'tw':6.5e-3, 'tf':10e-3, 'r':18e-3, 'A':54.74e-4, 'hi':307e-3, 'd':271e-3, 'FI':'M16', 'Pmin':78e-3, 'Pmax':96e-3, 'AL':1.25, 'AG':29.09, 'Iz':10230e-8, 'Wzel':625.7e-6, 'Wzpl':701.9e-6, 'iz':13.67e-2, 'Avy':26.99e-4, 'Iy':685.2e-8, 'Wyel':85.64e-6, 'Wypl':133.3e-6, 'iy':3.54e-2, 'Ss':47.59e-3, 'It':19.57e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_330']= {'nmb':'IPE_330', 'P':49.1, 'h':330e-3, 'b':160e-3, 'tw':7.5e-3, 'tf':11.5e-3, 'r':18e-3, 'A':62.61e-4, 'hi':307e-3, 'd':271e-3, 'FI':'M16', 'Pmin':78e-3, 'Pmax':96e-3, 'AL':1.254, 'AG':25.52, 'Iz':11770e-8, 'Wzel':713.1e-6, 'Wzpl':804.3e-6, 'iz':13.71e-2, 'Avy':30.81e-4, 'Iy':788.1e-8, 'Wyel':98.52e-6, 'Wypl':153.7e-6, 'iy':3.55e-2, 'Ss':51.59e-3, 'It':28.15e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_330+']= {'nmb':'IPE_O_330+', 'P':57, 'h':334e-3, 'b':162e-3, 'tw':8.5e-3, 'tf':13.5e-3, 'r':18e-3, 'A':72.62e-4, 'hi':307e-3, 'd':271e-3, 'FI':'M16', 'Pmin':80e-3, 'Pmax':98e-3, 'AL':1.268, 'AG':22.24, 'Iz':13910e-8, 'Wzel':833e-6, 'Wzpl':942.8e-6, 'iz':13.84e-2, 'Avy':34.88e-4, 'Iy':960.4e-8, 'Wyel':118.6e-6, 'Wypl':185e-6, 'iy':3.64e-2, 'Ss':56.59e-3, 'It':42.15e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_360']= {'nmb':'IPE_A_360', 'P':50.2, 'h':357.6e-3, 'b':170e-3, 'tw':6.6e-3, 'tf':11.5e-3, 'r':18e-3, 'A':63.96e-4, 'hi':334.6e-3, 'd':298.6e-3, 'FI':'M22', 'Pmin':86e-3, 'Pmax':88e-3, 'AL':1.351, 'AG':26.91, 'Iz':14520e-8, 'Wzel':811.8e-6, 'Wzpl':906.8e-6, 'iz':15.06e-2, 'Avy':29.76e-4, 'Iy':944.3e-8, 'Wyel':111.1e-6, 'Wypl':171.9e-6, 'iy':3.84e-2, 'Ss':50.69e-3, 'It':26.51e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_360']= {'nmb':'IPE_360', 'P':57.1, 'h':360e-3, 'b':170e-3, 'tw':8e-3, 'tf':12.7e-3, 'r':18e-3, 'A':72.73e-4, 'hi':334.6e-3, 'd':298.6e-3, 'FI':'M22', 'Pmin':88e-3, 'Pmax':88e-3, 'AL':1.353, 'AG':23.7, 'Iz':16270e-8, 'Wzel':903.6e-6, 'Wzpl':1019e-6, 'iz':14.95e-2, 'Avy':35.14e-4, 'Iy':1043e-8, 'Wyel':122.8e-6, 'Wypl':191.1e-6, 'iy':3.79e-2, 'Ss':54.49e-3, 'It':37.32e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_360+']= {'nmb':'IPE_O_360+', 'P':66, 'h':364e-3, 'b':172e-3, 'tw':9.2e-3, 'tf':14.7e-3, 'r':18e-3, 'A':84.13e-4, 'hi':334.6e-3, 'd':298.6e-3, 'FI':'M22', 'Pmin':90e-3, 'Pmax':90e-3, 'AL':1.367, 'AG':20.69, 'Iz':19050e-8, 'Wzel':1047e-6, 'Wzpl':1186e-6, 'iz':15.05e-2, 'Avy':40.21e-4, 'Iy':1251e-8, 'Wyel':145.5e-6, 'Wypl':226.9e-6, 'iy':3.86e-2, 'Ss':59.69e-3, 'It':55.76e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_400']= {'nmb':'IPE_A_400', 'P':57.4, 'h':397e-3, 'b':180e-3, 'tw':7e-3, 'tf':12e-3, 'r':21e-3, 'A':73.1e-4, 'hi':373e-3, 'd':331e-3, 'FI':'M22', 'Pmin':94e-3, 'Pmax':98e-3, 'AL':1.464, 'AG':25.51, 'Iz':20290e-8, 'Wzel':1022e-6, 'Wzpl':1144e-6, 'iz':16.66e-2, 'Avy':35.78e-4, 'Iy':1171e-8, 'Wyel':130.1e-6, 'Wypl':202.1e-6, 'iy':4e-2, 'Ss':55.6e-3, 'It':34.79e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_400']= {'nmb':'IPE_400', 'P':66.3, 'h':400e-3, 'b':180e-3, 'tw':8.6e-3, 'tf':13.5e-3, 'r':21e-3, 'A':84.46e-4, 'hi':373e-3, 'd':331e-3, 'FI':'M22', 'Pmin':96e-3, 'Pmax':98e-3, 'AL':1.467, 'AG':22.12, 'Iz':23130e-8, 'Wzel':1156e-6, 'Wzpl':1307e-6, 'iz':16.55e-2, 'Avy':42.69e-4, 'Iy':1318e-8, 'Wyel':146.4e-6, 'Wypl':229e-6, 'iy':3.95e-2, 'Ss':60.2e-3, 'It':51.08e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_400+']= {'nmb':'IPE_O_400+', 'P':75.7, 'h':404e-3, 'b':182e-3, 'tw':9.7e-3, 'tf':15.5e-3, 'r':21e-3, 'A':96.39e-4, 'hi':373e-3, 'd':331e-3, 'FI':'M22', 'Pmin':96e-3, 'Pmax':100e-3, 'AL':1.481, 'AG':19.57, 'Iz':26750e-8, 'Wzel':1324e-6, 'Wzpl':1502e-6, 'iz':16.66e-2, 'Avy':47.98e-4, 'Iy':1564e-8, 'Wyel':171.9e-6, 'Wypl':269.1e-6, 'iy':4.03e-2, 'Ss':65.3e-3, 'It':73.1e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_450']= {'nmb':'IPE_A_450', 'P':67.2, 'h':447e-3, 'b':190e-3, 'tw':7.6e-3, 'tf':13.1e-3, 'r':21e-3, 'A':85.55e-4, 'hi':420.8e-3, 'd':378.8e-3, 'FI':'M24', 'Pmin':100e-3, 'Pmax':102e-3, 'AL':1.603, 'AG':23.87, 'Iz':29760e-8, 'Wzel':1331e-6, 'Wzpl':1494e-6, 'iz':18.65e-2, 'Avy':42.26e-4, 'Iy':1502e-8, 'Wyel':158.1e-6, 'Wypl':245.7e-6, 'iy':4.19e-2, 'Ss':58.4e-3, 'It':45.67e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_450']= {'nmb':'IPE_450', 'P':77.6, 'h':450e-3, 'b':190e-3, 'tw':9.4e-3, 'tf':14.6e-3, 'r':21e-3, 'A':98.82e-4, 'hi':420.8e-3, 'd':378.8e-3, 'FI':'M24', 'Pmin':100e-3, 'Pmax':102e-3, 'AL':1.605, 'AG':20.69, 'Iz':33740e-8, 'Wzel':1500e-6, 'Wzpl':1702e-6, 'iz':18.48e-2, 'Avy':50.85e-4, 'Iy':1676e-8, 'Wyel':176.4e-6, 'Wypl':276.4e-6, 'iy':4.12e-2, 'Ss':63.2e-3, 'It':66.87e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_450+']= {'nmb':'IPE_O_450+', 'P':92.4, 'h':456e-3, 'b':192e-3, 'tw':11e-3, 'tf':17.6e-3, 'r':21e-3, 'A':117.7e-4, 'hi':420.8e-3, 'd':378.8e-3, 'FI':'M24', 'Pmin':102e-3, 'Pmax':104e-3, 'AL':1.622, 'AG':17.56, 'Iz':40920e-8, 'Wzel':1795e-6, 'Wzpl':2046e-6, 'iz':18.65e-2, 'Avy':59.4e-4, 'Iy':2085e-8, 'Wyel':217.2e-6, 'Wypl':341e-6, 'iy':4.21e-2, 'Ss':70.8e-3, 'It':109e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_500']= {'nmb':'IPE_A_500', 'P':79.4, 'h':497e-3, 'b':200e-3, 'tw':8.4e-3, 'tf':14.5e-3, 'r':21e-3, 'A':101.1e-4, 'hi':468e-3, 'd':426e-3, 'FI':'M24', 'Pmin':100e-3, 'Pmax':112e-3, 'AL':1.741, 'AG':21.94, 'Iz':42930e-8, 'Wzel':1728e-6, 'Wzpl':1946e-6, 'iz':20.61e-2, 'Avy':50.41e-4, 'Iy':1939e-8, 'Wyel':193.9e-6, 'Wypl':301.6e-6, 'iy':4.38e-2, 'Ss':62e-3, 'It':62.78e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_500']= {'nmb':'IPE_500', 'P':90.7, 'h':500e-3, 'b':200e-3, 'tw':10.2e-3, 'tf':16e-3, 'r':21e-3, 'A':115.5e-4, 'hi':468e-3, 'd':426e-3, 'FI':'M24', 'Pmin':102e-3, 'Pmax':112e-3, 'AL':1.744, 'AG':19.23, 'Iz':48200e-8, 'Wzel':1928e-6, 'Wzpl':2194e-6, 'iz':20.43e-2, 'Avy':59.87e-4, 'Iy':2142e-8, 'Wyel':214.2e-6, 'Wypl':335.9e-6, 'iy':4.31e-2, 'Ss':66.8e-3, 'It':89.29e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_500+']= {'nmb':'IPE_O_500+', 'P':107, 'h':506e-3, 'b':202e-3, 'tw':12e-3, 'tf':19e-3, 'r':21e-3, 'A':136.7e-4, 'hi':468e-3, 'd':426e-3, 'FI':'M24', 'Pmin':104e-3, 'Pmax':114e-3, 'AL':1.76, 'AG':16.4, 'Iz':57780e-8, 'Wzel':2284e-6, 'Wzpl':2613e-6, 'iz':20.56e-2, 'Avy':70.21e-4, 'Iy':2622e-8, 'Wyel':259.6e-6, 'Wypl':408.5e-6, 'iy':4.38e-2, 'Ss':74.6e-3, 'It':143.5e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_550']= {'nmb':'IPE_A_550', 'P':92.1, 'h':547e-3, 'b':210e-3, 'tw':9e-3, 'tf':15.7e-3, 'r':24e-3, 'A':117.3e-4, 'hi':515.6e-3, 'd':467.6e-3, 'FI':'M24', 'Pmin':106e-3, 'Pmax':122e-3, 'AL':1.875, 'AG':20.36, 'Iz':59980e-8, 'Wzel':2193e-6, 'Wzpl':2475e-6, 'iz':22.61e-2, 'Avy':60.3e-4, 'Iy':2432e-8, 'Wyel':231.6e-6, 'Wypl':361.5e-6, 'iy':4.55e-2, 'Ss':68.52e-3, 'It':86.53e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_550']= {'nmb':'IPE_550', 'P':106, 'h':550e-3, 'b':210e-3, 'tw':11.1e-3, 'tf':17.2e-3, 'r':24e-3, 'A':134.4e-4, 'hi':515.6e-3, 'd':467.6e-3, 'FI':'M24', 'Pmin':110e-3, 'Pmax':122e-3, 'AL':1.877, 'AG':17.78, 'Iz':67120e-8, 'Wzel':2441e-6, 'Wzpl':2787e-6, 'iz':22.35e-2, 'Avy':72.34e-4, 'Iy':2668e-8, 'Wyel':254.1e-6, 'Wypl':400.5e-6, 'iy':4.45e-2, 'Ss':73.62e-3, 'It':123.2e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_550+']= {'nmb':'IPE_O_550+', 'P':123, 'h':556e-3, 'b':212e-3, 'tw':12.7e-3, 'tf':20.2e-3, 'r':24e-3, 'A':156.1e-4, 'hi':515.6e-3, 'd':467.6e-3, 'FI':'M24', 'Pmin':110e-3, 'Pmax':122e-3, 'AL':1.893, 'AG':15.45, 'Iz':79160e-8, 'Wzel':2847e-6, 'Wzpl':3263e-6, 'iz':22.52e-2, 'Avy':82.69e-4, 'Iy':3224e-8, 'Wyel':304.2e-6, 'Wypl':480.5e-6, 'iy':4.55e-2, 'Ss':81.22e-3, 'It':187.5e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_A_600']= {'nmb':'IPE_A_600', 'P':108, 'h':597e-3, 'b':220e-3, 'tw':9.8e-3, 'tf':17.5e-3, 'r':24e-3, 'A':137e-4, 'hi':562e-3, 'd':514e-3, 'FI':'M27', 'Pmin':114e-3, 'Pmax':118e-3, 'AL':2.013, 'AG':18.72, 'Iz':82920e-8, 'Wzel':2778e-6, 'Wzpl':3141e-6, 'iz':24.6e-2, 'Avy':70.14e-4, 'Iy':3116e-8, 'Wyel':283.3e-6, 'Wypl':442.1e-6, 'iy':4.77e-2, 'Ss':72.92e-3, 'It':118.8e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_600']= {'nmb':'IPE_600', 'P':122, 'h':600e-3, 'b':220e-3, 'tw':12e-3, 'tf':19e-3, 'r':24e-3, 'A':156e-4, 'hi':562e-3, 'd':514e-3, 'FI':'M27', 'Pmin':116e-3, 'Pmax':118e-3, 'AL':2.015, 'AG':16.45, 'Iz':92080e-8, 'Wzel':3069e-6, 'Wzpl':3512e-6, 'iz':24.3e-2, 'Avy':83.78e-4, 'Iy':3387e-8, 'Wyel':307.9e-6, 'Wypl':485.6e-6, 'iy':4.66e-2, 'Ss':78.12e-3, 'It':165.4e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_O_600+']= {'nmb':'IPE_O_600+', 'P':154, 'h':610e-3, 'b':224e-3, 'tw':15e-3, 'tf':24e-3, 'r':24e-3, 'A':196.8e-4, 'hi':562e-3, 'd':514e-3, 'FI':'M27', 'Pmin':118e-3, 'Pmax':122e-3, 'AL':2.045, 'AG':13.24, 'Iz':118300e-8, 'Wzel':3879e-6, 'Wzpl':4471e-6, 'iz':24.52e-2, 'Avy':104.4e-4, 'Iy':4521e-8, 'Wyel':403.6e-6, 'Wypl':640.1e-6, 'iy':4.79e-2, 'Ss':91.12e-3, 'It':318.1e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_750x147']= {'nmb':'IPE_750x147', 'P':147, 'h':753e-3, 'b':265e-3, 'tw':13.2e-3, 'tf':17e-3, 'r':17e-3, 'A':187.5e-4, 'hi':719e-3, 'd':685e-3, 'FI':'M27', 'Pmin':104e-3, 'Pmax':164e-3, 'AL':2.51, 'AG':17.06, 'Iz':166100e-8, 'Wzel':4411e-6, 'Wzpl':5110e-6, 'iz':29.76e-2, 'Avy':105.4e-4, 'Iy':5289e-8, 'Wyel':399.2e-6, 'Wypl':630.8e-6, 'iy':5.31e-2, 'Ss':67.12e-3, 'It':161.5e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_750x173+']= {'nmb':'IPE_750x173+', 'P':173, 'h':762e-3, 'b':267e-3, 'tw':14.4e-3, 'tf':21.6e-3, 'r':17e-3, 'A':221.3e-4, 'hi':718.8e-3, 'd':684.8e-3, 'FI':'M27', 'Pmin':104e-3, 'Pmax':166e-3, 'AL':2.534, 'AG':14.58, 'Iz':205800e-8, 'Wzel':5402e-6, 'Wzpl':6218e-6, 'iz':30.49e-2, 'Avy':116.4e-4, 'Iy':6873e-8, 'Wyel':514.9e-6, 'Wypl':809.9e-6, 'iy':5.57e-2, 'Ss':77.52e-3, 'It':273.6e-8, 'E':2.1e+11, 'nu':0.3}
IPEprofiles['IPE_750x196+']= {'nmb':'IPE_750x196+', 'P':196, 'h':770e-3, 'b':268e-3, 'tw':15.6e-3, 'tf':25.4e-3, 'r':17e-3, 'A':250.8e-4, 'hi':719.2e-3, 'd':685.2e-3, 'FI':'M27', 'Pmin':106e-3, 'Pmax':166e-3, 'AL':2.552, 'AG':12.96, 'Iz':240300e-8, 'Wzel':6241e-6, 'Wzpl':7174e-6, 'iz':30.95e-2, 'Avy':127.3e-4, 'Iy':8175e-8, 'Wyel':610.1e-6, 'Wypl':958.8e-6, 'iy':5.71e-2, 'Ss':86.32e-3, 'It':408.9e-8, 'E':2.1e+11, 'nu':0.3}


for item in IPEprofiles:
  profile= IPEprofiles[item]
  Avy= profile['Avy']
  A= profile['A']
  E= profile['E']
  nu= profile['nu']
  b= profile['b']
  d= profile['d']
  h= profile['h']
  hi= profile['hi']
  tf= profile['tf']
  tw= profile['tw']
  r= profile['r']
  profile['Iw']= tf*((h+hi)/2.0)**2*b**3/24.0
  profile['alpha']= Avy/A
  profile['G']= E/(2*(1+nu))
  profile['AreaQy']= A-2*b*tf+(tw+2*r)*tf
  profile['AreaQz']= A-hi*tw

import math
import xc_base
import geom
from materials import structural_steel

class IPEProfile(structural_steel.SteelProfile):
  def __init__(self,steel,name):
    super(IPEProfile,self).__init__(steel,name,IPEprofiles)
    self.bHalf= self.get('b')/2.0 #Half flange width
    self.hHalf= self.get('h')/2.0 #Half section height
    self.hiHalf= self.get('hi')/2.0 #Half section interior height.
    self.twHalf= self.get('tw')/2.0 #Half web thickness
    self.tileSize= 0.01 #Size of tiles
  def b(self):
    return self.get('b')
  def h(self):
    return self.get('h')
  def tf(self):
    return self.get('tf')
  def tw(self):
    return self.get('tw')
  def hw(self):
    return self.h()-2*self.tf()
  def getRho(self):
    ''' Returns mass per unit lenght. '''
    return self.get('P')
  def getProfileRegions(self):
    ''' Returns regions valid for fiber section model creation. '''
    retval= list()
    #Lower flange
    p0= geom.Pos2d(-self.hHalf,-self.bHalf)
    p1= geom.Pos2d(-self.hiHalf,self.bHalf)
    retval.append([p0,p1])
    #Web
    p2= geom.Pos2d(-self.hiHalf,-self.twHalf)
    p3= geom.Pos2d(self.hiHalf,self.twHalf)
    retval.append([p2,p3])
    #Upper flange
    p4= geom.Pos2d(self.hiHalf,-self.bHalf,)
    p5= geom.Pos2d(self.hHalf,self.bHalf)
    retval.append([p4,p5])
    return retval

  def discretization(self,preprocessor,matModelName):
    self.sectionGeometryName= 'gm'+self.get('nmb')
    self.gm= preprocessor.getMaterialLoader.newSectionGeometry(self.sectionGeometryName)
    regions= self.gm.getRegions
    for r in self.getProfileRegions():
      reg= regions.newQuadRegion(matModelName)
      reg.pMin= r[0]
      reg.pMax= r[1]
      numberOfTiles= reg.setTileSize(self.tileSize,self.tileSize)
    return self.gm

  def getFiberSection3d(self,preprocessor,matModelName):
    reg= self.discretization(preprocessor,matModelName)
    self.fiberSection3dName= 'fs3d'+self.get('nmb')
    self.fiberSection3d= preprocessor.getMaterialLoader.newMaterial("fiber_section_3d",self.fiberSection3dName)
    fiberSectionRepr= self.fiberSection3d.getFiberSectionRepr()
    fiberSectionRepr.setGeomNamed(self.sectionGeometryName)
    self.fiberSection3d.setupFibers()
    fibras= self.fiberSection3d.getFibers()
    return self.fiberSection3d
