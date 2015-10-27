//----------------------------------------------------------------------------
//  programa XC; cálculo mediante el método de los elementos finitos orientado
//  a la solución de problemas estructurales.
//
//  Copyright (C)  Luis Claudio Pérez Tato
//
//  El programa deriva del denominado OpenSees <http://opensees.berkeley.edu>
//  desarrollado por el «Pacific earthquake engineering research center».
//
//  Salvo las restricciones que puedan derivarse del copyright del
//  programa original (ver archivo copyright_opensees.txt) este
//  software es libre: usted puede redistribuirlo y/o modificarlo 
//  bajo los términos de la Licencia Pública General GNU publicada 
//  por la Fundación para el Software Libre, ya sea la versión 3 
//  de la Licencia, o (a su elección) cualquier versión posterior.
//
//  Este software se distribuye con la esperanza de que sea útil, pero 
//  SIN GARANTÍA ALGUNA; ni siquiera la garantía implícita
//  MERCANTIL o de APTITUD PARA UN PROPÓSITO DETERMINADO. 
//  Consulte los detalles de la Licencia Pública General GNU para obtener 
//  una información más detallada. 
//
// Debería haber recibido una copia de la Licencia Pública General GNU 
// junto a este programa. 
// En caso contrario, consulte <http://www.gnu.org/licenses/>.
//----------------------------------------------------------------------------
//SetFilaJ.h

#ifndef SETFILAJ_H
#define SETFILAJ_H

#include "SetFila.h"
#include "preprocessor/cad/matrices/TritrizPtrNod.h"
#include "preprocessor/cad/matrices/TritrizPtrElem.h"

class RangoIndice;

namespace XC {

class EntMdlr;

//!  \ingroup Set
//! 
//!  \brief Conjunto de objetos.
//! 
//!  Un objeto SetFilaJ contiene un conjunto de 0 o más:
//!  - Nodos.
//!  - Elementos finitos.
//!  que corresponden a una fila_j de un objeto EntMdlr.
class SetFilaJ: public SetFila<TritrizPtrNod::var_ref_fila_j,TritrizPtrElem::var_ref_fila_j>
  {
  public:
    typedef TritrizPtrNod::var_ref_fila_j tfilanod;
    typedef TritrizPtrElem::var_ref_fila_j tfilaelem;
    SetFilaJ(EntMdlr &e,const size_t &f=1,const size_t &c=1,const std::string &nmb="",Preprocessor *preprocessor= NULL);
    SetFilaJ(EntMdlr &e,const size_t &capa,const RangoIndice &,const size_t &c,const std::string &nmb="",Preprocessor *preprocessor= NULL);  };
} //fin namespace XC
#endif
