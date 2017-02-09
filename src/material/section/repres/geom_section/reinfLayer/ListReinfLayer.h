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
//ListReinfLayer.h

#ifndef ListReinfLayer_h 
#define ListReinfLayer_h 

#include <list>
#include "material/section/repres/SeccionInerte.h"

class Pos2d;
class Poligono2d;
class Semiplano2d;

namespace XC {

class ReinfLayer;
class CircReinfLayer;
class StraightReinfLayer;
class BarraSuelta;
class MaterialLoader;
class Vector;
class Matrix;
class GeomSection;

//! @ingroup MATSCCArmaduras
//
//! @brief Contenedor (lista) de capas de armadura.
class ListReinfLayer: public std::list<ReinfLayer *>, public SeccionInerte
  {
  public:
    typedef std::list<ReinfLayer *> l_reg;
    typedef l_reg::reference reference;
    typedef l_reg::const_reference const_reference;
    typedef l_reg::iterator iterator;
    typedef l_reg::const_iterator const_iterator;
  private:
    void libera(void);
    void libera(const size_t i);
    void copia(const ListReinfLayer &otra);
  protected:

    MaterialLoader *material_loader; //!< Material definition handler (searching,...).

    friend class GeomSection;
    ListReinfLayer(GeomSection *,MaterialLoader *ml);
    ListReinfLayer(const ListReinfLayer  &otro);
    ListReinfLayer &operator=(const ListReinfLayer  &otro);
  public:
   ~ListReinfLayer(void);

    ReinfLayer *push_back(const ReinfLayer &reg);

    void clear(void);

    const GeomSection *getGeomSection(void) const;
    double getRecubrimiento(void) const;

    StraightReinfLayer *newStraightReinfLayer(const std::string &);
    CircReinfLayer *newCircReinfLayer(const std::string &);
    BarraSuelta *newReinfBar(const std::string &);


    size_t getNumReinfBars(void) const;

    //void Cumplen(const std::string &,ListReinfLayer &,bool );
    void getBarrasIn(const Poligono2d &,ListReinfLayer &,bool );
    void getBarrasIn(const Semiplano2d &,ListReinfLayer &,bool );

    double getAreaSeccBruta(void) const;
    Vector getCdgSeccBruta(void) const;
    double getIySeccBruta(void) const;
    double getIzSeccBruta(void) const;
    double getPyzSeccBruta(void) const;

    Vector getCdgSeccHomogeneizada(const double &E0) const;
    double getAreaSeccHomogeneizada(const double &E0) const;
    double getIySeccHomogeneizada(const double &E0) const;
    double getIzSeccHomogeneizada(const double &E0) const;
    double getPyzSeccHomogeneizada(const double &E0) const;

    void Print(std::ostream &s) const;
  };

} // end of XC namespace


#endif
