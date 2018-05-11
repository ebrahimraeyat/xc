# -*- coding: utf-8 -*-

def printShearVerificationListingHeader(archivo, nmbSecc):
  '''Prints the header of the shear verification listing.'''
  archivo.write("\\begin{center}\n")
  archivo.write("\\begin{footnotesize}\n")
  archivo.write("\\tablefirsthead{%\n")
  archivo.write("\\hline\n")
  archivo.write("\\multicolumn{12}{|c|}{\\textbf{",nmbArch,"}}\\\\\n")
  archivo.write("\\multicolumn{12}{|c|}{Comprobación de la sección ",toLaTex(nmbSecc),"}\\\\\n")
  archivo.write("\\hline\n")
  archivo.write("Elem. & Hip. & $N$  & $V_y$ & $V_z$ & $V_{u1}$ & $\\theta$              & $V_{cu}$ & $V_{su}$  & $V_{u2}$ & $V_u$ & FC \\\\\n")
  archivo.write("      &      & (kN) & (kN)  & (kN)  & (kN)     & (\\textsuperscript{o}) & (kN)     & (kN)      & (kN)     & (kN)  &    \\\\\n")
  archivo.write("\\hline}\n")
  archivo.write("\\tablehead{%\n")
  archivo.write("\\hline\n")
  archivo.write("\\multicolumn{12}{|l|}{\small\sl \ldots continúa}\\\\\n")
  archivo.write("\\hline\n")
  archivo.write("\\multicolumn{12}{|c|}{\\textbf{",nmbArch,"}}\\\\\n")
  archivo.write("\\multicolumn{12}{|c|}{Comprobación de la sección ",toLaTex(nmbSecc),"}\\\\\n")
  archivo.write("\\hline\n")
  archivo.write("Elem. & Hip. & $N$  & $V_y$ & $V_z$ & $V_{u1}$ & $\\theta$              & $V_{cu}$ & $V_{su}$  & $V_{u2}$ & $V_u$ & FC \\\\\n")
  archivo.write("      &      & (kN) & (kN)  & (kN)  & (kN)     & (\\textsuperscript{o}) & (kN)     & (kN)      & (kN)     & (kN)  &    \\\\\n")
  archivo.write("\\hline}\n")
  archivo.write("\\tabletail{%\n")
  archivo.write("\\hline\n")
  archivo.write("\\multicolumn{12}{|r|}{\small\sl continúa\ldots}\\\\\n")
  archivo.write("\\hline}\n")
  archivo.write("\\tablelasttail{\hline}\n")
  archivo.write("\\begin{supertabular}{|l|r|r|r|r|r|r|r|r|r|r|r|}\n")


def printShearVerificationListingFoot(archivo):
  '''Print the shear verification listing foot.'''
  archivo.write("\\end{supertabular}\n")
  archivo.write("\\end{footnotesize}\n")
  archivo.write("\\end{center}\n")

