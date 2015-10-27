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
//Reflexion.h

#ifndef REFLEXION_H
#define REFLEXION_H

#include "TrfGeom.h"
#include "xc_utils/src/geom/trf/Reflexion3d.h"

namespace XC {

//! \ingroup CadTrf
//!
//! \brief Aplica una transformación "reflexión".
class Reflexion: public TrfGeom
  {
    Reflexion3d rf; //!< Reflexion.
  protected:
    virtual bool procesa_comando(CmdStatus &status);
  public:
    //! @brief Constructor.
    Reflexion(Preprocessor *m)
      : TrfGeom(m), rf() {}
    void setPlane(const Plano3d &p)
      { rf= Reflexion3d(p); }
    virtual Pos3d Transforma(const Pos3d &p) const;
    virtual Vector3d Transforma(const Vector3d &v) const;
  };
} //fin namespace XC

#endif
