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

#include "DqPtrsNode.h"
#include "domain/mesh/node/Node.h"
#include "preprocessor/cad/trf/TrfGeom.h"
#include "xc_basic/src/funciones/algebra/ExprAlgebra.h"

void XC::DqPtrsNode::crea_arbol(void)
  {
    kdtreeNodos.clear();
    for(iterator i= begin();i!=end();i++)
      {
        Node *nPtr= *i;
        assert(nPtr);
        kdtreeNodos.insert(*nPtr);
      }
  }

//! @brief Constructor.
XC::DqPtrsNode::DqPtrsNode(void)
  : DqPtrs<Node>() {}

//! @brief Constructor de copia.
XC::DqPtrsNode::DqPtrsNode(const DqPtrsNode &otro)
  : DqPtrs<Node>(otro)
  { crea_arbol(); }

//! @brief Constructor de copia.
XC::DqPtrsNode::DqPtrsNode(const std::deque<Node *> &ts)
  : DqPtrs<Node>(ts)
  { crea_arbol(); }

//! @brief Constructor de copia.
XC::DqPtrsNode::DqPtrsNode(const std::set<const Node *> &st)
  : DqPtrs<Node>()
  {
    std::set<const Node *>::const_iterator k;
    k= st.begin();
    for(;k!=st.end();k++)
      push_back(const_cast<Node *>(*k));
  }

//! @brief Operator asignación.
XC::DqPtrsNode &XC::DqPtrsNode::operator=(const DqPtrsNode &otro)
  {
    DqPtrs<Node>::operator=(otro);
    kdtreeNodos= otro.kdtreeNodos;
    return *this;
  }

//! @brief Agrega a ésta lista los elementos de la que se le pasa como parámetro.
void XC::DqPtrsNode::agrega(const DqPtrsNode &otro)
  {
    for(register const_iterator i= otro.begin();i!=otro.end();i++)
      push_back(*i);
  }

//! @brief Agrega a ésta lista los elementos de la que se le pasa como parámetro,
//! si cumplen la condición.
void XC::DqPtrsNode::agrega_cond(const DqPtrsNode &otro,const std::string &cond)
  {
    bool result= false;
    for(register const_iterator i= otro.begin();i!=otro.end();i++)
      {
        result= (*i)->interpretaBool(cond);
        if(result)
	  push_back(*i);
      }
  }

//! @brief Vacía la lista de punteros y elimina las propiedades que pudiera tener el objeto.
void XC::DqPtrsNode::clearAll(void)
  {
    DqPtrs<Node>::clear();
    kdtreeNodos.clear();
  }

bool XC::DqPtrsNode::push_back(Node *n)
  {
    bool retval= DqPtrs<Node>::push_back(n);
    if(retval)
      kdtreeNodos.insert(*n);
    return retval;
  }

bool XC::DqPtrsNode::push_front(Node *n)
  {
    bool retval= DqPtrs<Node>::push_front(n);
    if(retval)
      kdtreeNodos.insert(*n);
    return retval;
  }

//! @brief Devuelve el nodo más próximo al punto que se pasa como parámetro.
XC::Node *XC::DqPtrsNode::getNearestNode(const Pos3d &p)
  {
    Node *retval= const_cast<Node *>(kdtreeNodos.getNearestNode(p));
    return retval;
  }

//! @brief Devuelve el nodo más próximo al punto que se pasa como parámetro.
const XC::Node *XC::DqPtrsNode::getNearestNode(const Pos3d &p) const
  {
    DqPtrsNode *this_no_const= const_cast<DqPtrsNode *>(this);
    return this_no_const->getNearestNode(p);
  }

//! @brief Desplaza los nodos del conjunto.
void XC::DqPtrsNode::mueve(const std::vector<ExprAlgebra> &desplaz)
  {
    for(iterator i= begin();i!=end();i++)
      (*i)->Mueve(desplaz);
    crea_arbol();
  }

//! @brief Aplica la transformación a los elementos del conjunto.
void XC::DqPtrsNode::transforma(const TrfGeom &trf)
  {
    //Transforma 
    for(iterator i= begin();i!=end();i++)
      (*i)->Transforma(trf);
    crea_arbol();
  }

//! @brief Devuelve, si lo encuentra, un puntero al nodo
//! cuyo tag se pasa como parámetro.
XC::Node *XC::DqPtrsNode::buscaNodo(const int &tag)
  {
    Node *retval= nullptr;
    Node *tmp= nullptr;
    for(iterator i= begin();i!=end();i++)
      {
        tmp= *i;
        if(tmp)
          {
            if(tag == tmp->getTag())
              {
                retval= tmp;
                break;
              }
          }
      }
    return retval;
  }

//! @brief Devuelve, si lo encuentra, un puntero al nodo
//! cuyo tag se pasa como parámetro.
const XC::Node *XC::DqPtrsNode::buscaNodo(const int &tag) const
  {
    const Node *retval= nullptr;
    const Node *tmp= nullptr;
    for(const_iterator i= begin();i!=end();i++)
      {
        tmp= *i;
        if(tmp)
          {
            if(tag == tmp->getTag())
              {
                retval= tmp;
                break;
              }
          }
      }
    return retval;
  }

//! @brief Devuelve el número de nods del conjunto que están activos.
size_t XC::DqPtrsNode::getNumLiveNodes(void) const
  {
    size_t retval= 0;
    const Node *tmp= nullptr;
    for(const_iterator i= begin();i!=end();i++)
      {
        tmp= *i;
        if(tmp)
          if(tmp->isAlive()) retval++;
      }
    return retval;
  }

//! @brief Devuelve el número de nodos del conjunto que están inactivos.
size_t XC::DqPtrsNode::getNumDeadNodes(void) const
  {
    size_t retval= 0;
    const Node *tmp= nullptr;
    for(const_iterator i= begin();i!=end();i++)
      {
        tmp= *i;
        if(tmp)
          if(tmp->isDead()) retval++;
      }
    return retval;
  }

//!  @brief Asigna índices a los objetos de la lista para poder emplearlos en VTK.
void XC::DqPtrsNode::numera(void)
  {
    size_t idx= 0;
    for(iterator i= begin();i!=end();i++,idx++)
      {
	Node *ptr= *i;
        ptr->set_indice(idx);
      }
  }

//! @brief Devuelve verdadero si el nodo, cuyo tag se
//! pasa como parámetro, pertenece al conjunto.
bool XC::DqPtrsNode::InNodeTag(const int tag_nodo) const
  {
    for(const_iterator i= begin();i!=end();i++)
      if(tag_nodo == (*i)->getTag()) return true;
    return false;
  }

//! @brief Devuelve verdadero si todos los nodos, cuyos tags se
//! pasan como parámetro, pertenecen al conjunto.
bool XC::DqPtrsNode::InNodeTags(const ID &tag_nodos) const
  {
    const int sz= tag_nodos.Size();
    for(int i=0;i<sz;i++)
      if(!InNodeTag(tag_nodos(i))) return false;
    return true;
  }

//! @brief Devuelve los tags de los nodos.
std::set<int> XC::DqPtrsNode::getTags(void) const
  {
    std::set<int> retval;
    for(const_iterator i= begin();i!=end();i++)
      retval.insert((*i)->getTag());
    return retval;
  }
