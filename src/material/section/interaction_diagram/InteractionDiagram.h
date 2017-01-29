//----------------------------------------------------------------------------
//  XC program; finite element analysis code
//  for structural analysis and design.
//
//  Copyright (C)  Luis Claudio Pérez Tato
//
//  This program derives from OpenSees <http://opensees.berkeley.edu>
//  developed by the  «Pacific earthquake engineering research center».
//
//  Except for the restrictions that may arise from the copyright
//  of the original program (see copyright_opensees.txt)
//  XC is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or 
//  (at your option) any later version.
//
//  This software is distributed in the hope that it will be useful, but 
//  WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details. 
//
//
// You should have received a copy of the GNU General Public License 
// along with this program.
// If not, see <http://www.gnu.org/licenses/>.
//----------------------------------------------------------------------------
//InteractionDiagram.h

#ifndef INTERACTION_DIAGRAM_H
#define INTERACTION_DIAGRAM_H

#include "xc_utils/src/geom/d2/Triedro3d.h"
#include <set>
#include <deque>
#include "ClosedTriangleMesh.h"

class Triang3dMesh;

namespace XC {

class Vector;
class FiberSectionBase;
class InteractionDiagramData;

//! \@ingroup MATSCCDiagInt
//
//! @brief Interaction diagram (N,Mx,My) for a cross section.
class InteractionDiagram: public ClosedTriangleMesh
  {
  protected:
    typedef std::set<const Triedro3d *> set_ptr_triedros;

    
    set_ptr_triedros triedros_cuadrante[8];

    void clasifica_triedro(const Triedro3d &tdro);
    void clasifica_triedros(void);
    void setMatrizPosiciones(const Matrix &);
    GeomObj::list_Pos3d get_interseccion(const Pos3d &p) const;
  public:
    InteractionDiagram(void);
    InteractionDiagram(const Pos3d &org,const Triang3dMesh &mll);
    InteractionDiagram(const InteractionDiagram &otro);
    InteractionDiagram &operator=(const InteractionDiagram &otro);
    virtual InteractionDiagram *clon(void) const;

    const Triedro3d *BuscaPtrTriedro(const Pos3d &p) const;
    Pos3d getIntersection(const Pos3d &) const;
    double FactorCapacidad(const Pos3d &) const;
    Vector FactorCapacidad(const GeomObj::list_Pos3d &) const;

    void Print(std::ostream &os) const;
  };

InteractionDiagram calc_interaction_diagram(const FiberSectionBase &scc,const InteractionDiagramData &datos);

} // end of XC namespace

#endif
