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
//Pnt.cc

#include "Pnt.h"
#include "Edge.h"
#include "preprocessor/cad/trf/TrfGeom.h"
#include "preprocessor/Preprocessor.h"
#include "preprocessor/set_mgmt/Set.h"
#include "xc_utils/src/geom/pos_vec/Vector3d.h"
#include "xc_utils/src/geom/d3/BND3d.h"
#include "xc_utils/src/base/CmdStatus.h"
#include "xc_basic/src/texto/cadena_carac.h"
#include "xc_utils/src/geom/pos_vec/MatrizPos3d.h"
#include "xc_utils/src/geom/pos_vec/TritrizPos3d.h"
#include "domain/mesh/node/Node.h"
#include "domain/mesh/element/Element.h"
#include "preprocessor/cad/SisRef.h"
#include "xc_utils/src/base/any_const_ptr.h"

//! @brief Constructor.
XC::Pnt::Pnt(Preprocessor *m,const Pos3d &pto)
  : EntMdlr(m), p(pto) {}

//! @brief Constructor.
XC::Pnt::Pnt(const std::string &nombre, Preprocessor *m,const Pos3d &pto)
  : EntMdlr(nombre,0,m), p(pto) {}

//! @brief Constructor virtual.
XC::SetEstruct *XC::Pnt::getCopy(void) const
  { return new Pnt(*this); }

//! Inserta la línea que se pasa como parámetro en la lista
//! de líneas que tocan al punto.
void XC::Pnt::inserta_linea(Edge *l) const
  { lineas_pt.insert(l); }

//! Borra la línea que se pasa como parámetro de la lista
//! de líneas que tocan al punto.
void XC::Pnt::borra_linea(Edge *l) const
  {
    std::set<const Edge *>::iterator i= lineas_pt.find(l);
    if(i!= lineas_pt.end()) //La ha encontrado.
      lineas_pt.erase(i);
  }
//! Devuelve el vector de posición del punto.
Vector3d XC::Pnt::VectorPos(void) const
  { return p.VectorPos();  }

//! @brief Lee un objeto Pnt desde el archivo de entrada.
//!
//! Soporta los comandos:
//!
//! - pos: Lee las coordenadas del punto.
bool XC::Pnt::procesa_comando(CmdStatus &status)
  {
    const std::string cmd= deref_cmd(status.Cmd());
    if(verborrea>2)
      std::clog << "(Pnt) Procesando comando: " << cmd << std::endl;
    if(cmd == "pos")
      {
        p.LeeCmd(status);
        return true;
      }
    else if(cmd == "set_pos")
      {
        const Pos3d pt= interpretaPos3d(status.GetString());
        this->p= pt;
        return true;
      }
    else if(cmd == "copia_pos")
      {
        const MapPuntos::Indice id_punto= interpretaSize_t(status.GetString());
        const Pnt *tmp= BuscaPnt(id_punto);
	if(!tmp)
	  std::cerr << "Pnt; " << cmd << " , no se encontró el punto: '" 
                    << id_punto << "' \n";
        this->p= tmp->p;
        return true;
      }
    else if(cmd == "nodo")
      {
        Node *nod= GetNodo();
        if(nod)
          nod->LeeCmd(status);
        else
          {
            const std::string posLectura= get_ptr_status()->getPosicionLecturaActual();
	    std::cerr << "Pnt; " << cmd << " , el punto: '" << GetNombre()
                      << "' no posee nodo (no se ha mallado)." << posLectura << std::endl;
          }
        return true;
      }
    else
      return EntMdlr::procesa_comando(status);
  }

//! @brief Actualiza la topología.
void XC::Pnt::actualiza_topologia(void)
  {}

//! @brief Devuelve el BND del objeto.
BND3d XC::Pnt::Bnd(void) const
  { return BND3d(p,p);  }

//! @brief Devuelve las líneas que comienzan o acaban en este punto.
std::set<const XC::Edge *> XC::Pnt::EdgesExtremo(void) const
  {
    std::set<const Edge *> retval;
    if(!lineas_pt.empty())
      {
        std::set<const Edge *>::const_iterator i= lineas_pt.begin();
        for(;i!=lineas_pt.end();i++)
          {
            const Edge *l= *i;
            if(Extremo(*l))
              retval.insert(l);
          }
      }
    return retval;
  }

//! @brief Devuelve los nombres de las lineas que tocan al punto.
const std::string &XC::Pnt::NombresEdgesTocan(void) const
  {
    static std::string retval;
    retval= "";
    if(!lineas_pt.empty())
      {
        std::set<const Edge *>::const_iterator i= lineas_pt.begin();
        retval+= (*i)->GetNombre();
        for(;i!=lineas_pt.end();i++)
          retval+= "," + (*i)->GetNombre();
      }
    return retval;
  }

//! @brief Devuelve verdadero si el punto toca a la línea.
bool XC::Pnt::Toca(const Edge &l) const
  {
    std::set<const Edge *>::const_iterator i= lineas_pt.find(&l);
    return (i!=lineas_pt.end());
  }

//! @brief Devuelve verdadero si el punto es un extremo de la línea.
bool XC::Pnt::Extremo(const Edge &l) const
  { return l.Extremo(*this); }

//! @brief Devuelve verdadero si el punto toca a la superficie.
bool XC::Pnt::Toca(const Face &s) const
  {
    for(std::set<const Edge *>::const_iterator i= lineas_pt.begin(); i!=lineas_pt.end();i++)
      { if((*i)->Toca(s)) return true; }
    return false;
  }

//! @brief Devuelve verdadero si el punto toca al cuerpo.
bool XC::Pnt::Toca(const Body &b) const
  {
    for(std::set<const Edge *>::const_iterator i= lineas_pt.begin(); i!=lineas_pt.end();i++)
      { if((*i)->Toca(b)) return true; }
    return false;
  }

//! @brief Devuelve el cuadrado de la distancia a la posición que se pasa como parámetro.
double XC::Pnt::DistanciaA2(const Pos3d &pt) const
  { return dist2(p,pt);  }

//! @brief Crea los nodos de la malla.
void XC::Pnt::crea_nodos(void)
  {
    if(getGenMalla() && (NumNodos()==0))
      {
        MatrizPos3d tmp(1,1,GetPos());
        TritrizPos3d ptos(1,tmp);
        EntMdlr::crea_nodos(ptos);
      }
  }

//! @brief Crea la malla.
void XC::Pnt::Malla(dir_mallado dm)
  {
    crea_nodos();
  }

//! @brief Devuelve verdadero si el punto posee nodo (se ha mallado).
bool XC::Pnt::tieneNodo(void) const
  {
    bool retval= false;
    if(NumNodos()>0)
      retval= (GetNodo()!= nullptr);
    return retval;      
  }

//! @brief Return node's tag.
int XC::Pnt::getTagNode(void) const
  {
    int retval= -1;
    const Node *nod= GetNodo();
    if(nod)
      retval= nod->getTag();
    else
      std::cerr << "Pnt::GetProp; el punto: '" << GetNombre()
                << "' no posee nodo (no se ha mallado)." << std::endl;
    return retval;
  }


//! @brief Return point's node.
XC::Node *XC::Pnt::getNode(void)
  {
    Node *nod= GetNodo();
    if(!nod)
      std::cerr << "Pnt::GetProp; el punto: '" << GetNombre()
                << "' no posee nodo (no se ha mallado)." << std::endl;
    return nod;
  }

//! @brief Devuelve los conjuntos a los que pertenece este punto.
std::set<XC::SetBase *> XC::Pnt::get_sets(void) const
  {
    std::set<SetBase *> retval;
    const Preprocessor *preprocessor= GetPreprocessor();
    if(preprocessor)
      {
        MapSet &sets= const_cast<MapSet &>(preprocessor->get_sets());
        retval= sets.get_sets(this);
      }
    else
      std::cerr << "Pnt::get_sets; no se ha definido el modelador." << std::endl;
    return retval;
  }

//! @brief Agrega el punto a los conjuntos que se pasan como parámetro.
void XC::Pnt::add_to_sets(std::set<SetBase *> &sets)
  {
    for(std::set<SetBase *>::iterator i= sets.begin();i!= sets.end();i++)
      {
        Set *s= dynamic_cast<Set *>(*i);
        if(s) s->GetPuntos().push_back(this);
      }
  }

//! Devuelve la propiedad del objeto cuyo código se pasa
//! como parámetro.
//!
//! Soporta las propiedades:
//! -nlineas: Devuelve el número de líneas que empiezan o acaban en este punto.
any_const_ptr XC::Pnt::GetProp(const std::string &cod) const
  {
    if(cod=="pos")
      return any_const_ptr(GetPos());
    else if(cod=="tieneNodo")
      {
        tmp_gp_bool= tieneNodo();
        return any_const_ptr(tmp_gp_bool);
      }
    else if(cod=="tag_nodo")
      {
        tmp_gp_int= getTagNode();
        return any_const_ptr(tmp_gp_int);
      }
    else if(cod=="nlineas")
      {
        tmp_gp_szt= getNLines();
        return any_const_ptr(tmp_gp_szt);
      }
    else
      return EntMdlr::GetProp(cod);
  }

//! @brief Desplaza la posición del punto (sólo esta previsto que se use desde Set).
void XC::Pnt::Mueve(const std::vector<ExprAlgebra> &desplaz)
  {
    Vector3d d(0,0,0);
    const size_t sz= desplaz.size();
    if(sz>0) d.SetX(desplaz[0].ToNum());
    if(sz>1) d.SetY(desplaz[1].ToNum());
    if(sz>2) d.SetZ(desplaz[2].ToNum());
    p+=d;
    return;
  }

//! @brief Aplica al punto la transformación cuyo índice se pasa como parámetro.
void XC::Pnt::Transforma(const TrfGeom &trf)
  { p= trf.Transforma(p); }

//! @brief Aplica al punto la transformación cuyo índice se pasa como parámetro.
void XC::Pnt::Transforma(const size_t &indice_trf)
  {
    TrfGeom *trf= get_modelador()->getCad().getTransformacionesGeometricas().busca(indice_trf);
    if(trf)
      Transforma(*trf);
  }

XC::Vector &XC::operator-(const Pnt &b,const Pnt &a)
  {
    static Vector retval(3);
    const Pos3d A= a.GetPos();
    const Pos3d B= b.GetPos();
    retval[0]= B.x()-A.x();
    retval[1]= B.y()-A.y();
    retval[2]= B.z()-A.z();
    return retval;
  }

//! @brief Busca una línea que conecta los puntos que se pasan como parámetro.
const XC::Edge *XC::busca_edge_const_ptr_toca(const Pnt &pA,const Pnt &pB)
  {
    const Edge *retval= nullptr;
    const std::set<const Edge *> lineasPA= pA.EdgesTocan();
    for(std::set<const Edge *>::const_iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Toca(**i))
        {
          retval= *i;
          break;
        }
    return retval;
  }

//! @brief Busca una línea que conecta los puntos que se pasan como parámetro.
const XC::Edge *XC::busca_edge_const_ptr_toca(const Pnt &pA,const Pnt &pB, const Pnt &pC)
  {
    const Edge *retval= nullptr;
    const std::set<const Edge *> lineasPA= pA.EdgesTocan();
    for(std::set<const Edge *>::const_iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Toca(**i) && pC.Toca(**i))
        {
          retval= *i;
          break;
        }
    return retval;
  }

//! @brief Busca una línea que conecta los puntos que se pasan como parámetro.
XC::Edge *XC::busca_edge_ptr_toca(const Pnt &pA,const Pnt &pB)
  {
    Edge *retval= nullptr;
    std::set<const Edge *> lineasPA= pA.EdgesTocan();
    for(std::set<const Edge *>::iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Toca(**i))
        {
          retval= const_cast<Edge *>(*i);
          break;
        }
    return retval;
  }

//! @brief Busca una línea que conecta los puntos que se pasan como parámetro.
XC::Edge *XC::busca_edge_ptr_toca(const Pnt &pA,const Pnt &pB, const Pnt &pC)
  {
    Edge *retval= nullptr;
    std::set<const Edge *> lineasPA= pA.EdgesTocan();
    for(std::set<const Edge *>::iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Toca(**i) && pC.Toca(**i))
        {
          retval= const_cast<Edge *>(*i);
          break;
        }
    return retval;
  }

//! @brief Busca una línea cuyos extremos son los puntos que se pasan como parámetro.
XC::Edge *XC::busca_edge_ptr_extremos(const Pnt &pA,const Pnt &pB)
  {
    Edge *retval= nullptr;
    std::set<const Edge *> lineasPA= pA.EdgesExtremo();
    for(std::set<const Edge *>::iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Extremo(**i))
        {
          retval= const_cast<Edge *>(*i);
          break;
        }
    return retval;
  }

//! @brief Busca una línea que conecta los puntos que se pasan como parámetro.
XC::Edge *XC::busca_edge_ptr_extremos(const Pnt &pA,const Pnt &pB, const Pnt &pC)
  {
    Edge *retval= nullptr;
    std::set<const Edge *> lineasPA= pA.EdgesExtremo();
    for(std::set<const Edge *>::iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Toca(**i) && pC.Extremo(**i))
        {
          retval= const_cast<Edge *>(*i);
          break;
        }
    return retval;
  }

//! @brief Busca una línea cuyos extremos son los puntos que se pasan como parámetro.
const XC::Edge *XC::busca_edge_const_ptr_extremos(const Pnt &pA,const Pnt &pB)
  {
    const Edge *retval= nullptr;
    std::set<const Edge *> lineasPA= pA.EdgesExtremo();
    for(std::set<const Edge *>::iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Extremo(**i))
        {
          retval= *i;
          break;
        }
    return retval;
  }

//! @brief Busca una línea que conecta los puntos que se pasan como parámetro.
const XC::Edge *XC::busca_edge_const_ptr_extremos(const Pnt &pA,const Pnt &pB, const Pnt &pC)
  {
    const Edge *retval= nullptr;
    std::set<const Edge *> lineasPA= pA.EdgesExtremo();
    for(std::set<const Edge *>::iterator i= lineasPA.begin();i!=lineasPA.end();i++)
      if(pB.Toca(**i) && pC.Extremo(**i))
        {
          retval= (*i);
          break;
        }
    return retval;
  }
