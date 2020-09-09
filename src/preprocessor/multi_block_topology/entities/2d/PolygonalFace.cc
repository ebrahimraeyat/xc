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
//PolygonalFace.cc

#include "PolygonalFace.h"
#include "preprocessor/multi_block_topology/entities/0d/Pnt.h"
#include "preprocessor/multi_block_topology/MultiBlockTopology.h"
#include "xc_utils/src/geom/pos_vec/Vector3d.h"
#include "domain/mesh/node/Node.h"
#include "domain/mesh/element/Element.h"
#include "preprocessor/Preprocessor.h"
#include "utility/paving/Paver.h"

//! @brief Constructor.
XC::PolygonalFace::PolygonalFace(Preprocessor *m)
  : Face(m,0,0) {}

//! @brief Virtual constructor.
XC::SetEstruct *XC::PolygonalFace::getCopy(void) const
  { return new PolygonalFace(*this); }


void XC::PolygonalFace::addHole(PolygonalFace *pFace)
  { holes.push_back(pFace); }

//! @brief Creates and inserts the lines from the points identified
//! by the indexes being passed as parameter.
void XC::PolygonalFace::setPoints(const ID &point_indexes)
  {
    const size_t np= point_indexes.Size(); //Number of indexes.
    if(np<3)
      std::cerr << getClassName() << "::" << __FUNCTION__
	        << "; surface definition needs "
                << 3 << " points or more, we got: " << np << ".\n";
    else
      {
        if(getNumberOfEdges()>0)
          std::cerr << getClassName() << "::" << __FUNCTION__
	            << "; warning redefinition of surface: '"
                    << getName() << "'.\n";

	Face::addPoints(point_indexes);
        close();
      }
    int tagV1= getVertex(1)->getTag();
    if(tagV1!=point_indexes(0))
      std::cerr << getClassName() << "::" << __FUNCTION__
		<< "; surface: " << getTag()
                << "is inverted." << std::endl;
    ref= getPolygon().getRef();
    
  }

//! @brief Returns a vector in the direction of the local
//! X axis.
Vector3d XC::PolygonalFace::getIVector(void) const
  { return ref.GetI(); }

//! @brief Returns a vector in the direction of the local
//! Y axis.
Vector3d XC::PolygonalFace::getJVector(void) const
  { return ref.GetJ(); }

//! @brief Triggers node creation on the edges.
void XC::PolygonalFace::create_line_nodes(void)
  {
    // Create nodes on face contour.
    Face::create_line_nodes();
    
    // Create nodes on holes.
    for(std::deque<PolygonalFace *>::const_iterator i= holes.begin(); i!= holes.end(); i++)
      (*i)->create_line_nodes();
  }

//! @brief Creates surface nodes.
void XC::PolygonalFace::create_nodes(Paver &paver)
  {
    if(ttzNodes.Null())
      {
	// Create perimeter nodes.
        create_line_nodes();

	// Prepare perimeters node positions.
	std::deque<Node *> perimeterNodes;
	GeomObj::list_Pos3d contourPositions;

	//// Exterior contour.
	const size_t numSides= getNumberOfEdges();
	for(size_t i= 0;i<numSides; i++)
	  {
	    Side &side= lines[i];
	    Edge *edge= side.getEdge();
	    const size_t nNodesEdge= edge->getNumberOfNodes();
	    for(size_t j= 0;j<nNodesEdge-1;j++)
	      {
		Node *nn= side.getNode(j+1);
	        perimeterNodes.push_back(nn);
  	        contourPositions.push_back(nn->getInitialPosition3d());
	      }
	  }

	//// Holes.
	size_t nHolePositions= 0;
        std::deque<Polygon3d> holePolygons;
	for(std::deque<PolygonalFace *>::iterator i= holes.begin(); i!= holes.end(); i++)
	  {
	    PolygonalFace *hole= *i;
  	    GeomObj::list_Pos3d holePositions;
	    const size_t numSides= hole->getNumberOfEdges();
	    for(size_t j= 0;j<numSides; j++)
	      {
		Side &side= hole->lines[j];
		Edge *edge= side.getEdge();
		const size_t nNodesEdge= edge->getNumberOfNodes();
		for(size_t k= 0;k<nNodesEdge-1;k++)
		  {
		    Node *nn= side.getNode(k+1);
		    perimeterNodes.push_back(nn);
  	            holePositions.push_back(nn->getInitialPosition3d());
		  }
	      }
	    Polygon3d holePlg= Polygon3d(holePositions);
	    nHolePositions+= holePlg.GetNumVertices();
	    holePolygons.push_back(holePlg);
	  }

	// Call paving routines.
	const size_t nPerimeterNodes= perimeterNodes.size();
        paver.mesh(Polygon3d(contourPositions), holePolygons);

	// Populate node array.
	const std::vector<Pos3d> &nodePositions= paver.getNodePositions();
	const size_t nNodes= nodePositions.size();
	
        ttzNodes= NodePtrArray3d(1,1,nNodes);

	//// Put perimeter nodes (they exist already)
	size_t count= 0;
	const size_t numPerimeterNodes= perimeterNodes.size();
	for(size_t i= 0;i<numPerimeterNodes;i++, count++)
	  {
	    Node *nn= perimeterNodes[i];
	    size_t index= i;
	    const Pos3d nodePos= nodePositions[index];
	    const Pos3d nP= nn->getInitialPosition3d();
	    const double d2= dist2(nodePos, nP);
	    if(d2>1e-8)
	      {
		index= paver.getIndexNearestPosition(nP,numPerimeterNodes);
	      }
	    ttzNodes(1,1,index+1)= nn;
	  }

	//// Create new nodes.
	for(size_t k= count;k<nNodes;k++, count++)
	  {
	    const Pos3d nodePos= nodePositions[count];
	    create_node(nodePos,1,1,k+1);
	  }
	for(size_t k= 0; k<nNodes;k++)
	  { Node *nn= ttzNodes(1,1,k+1); }
      }
    else
      if(verbosity>2)
        std::clog << getClassName() << "::" << __FUNCTION__
	          << "; nodes of entity: '" << getName()
		  << "' already exist." << std::endl; 
  }

//! @brief Creates elements on the nodes created
//! in create_nodes.
bool XC::PolygonalFace::create_elements(const Paver &paver)
  {
    bool retval= false;
    if(!ttzNodes.empty())
      {
        if(ttzNodes.HasNull())
          std::cerr << getClassName() << "::" << __FUNCTION__
	            << "; there are null pointers."
                    << " Elements were not created." << std::endl;
        else
          if(ttzElements.Null())
            {
              if(getPreprocessor())
                {
                  if(verbosity>4)
                    std::clog << "Creating elements of entity: '"
			      << getName() << "'...";   
                  const Element *seed= getPreprocessor()->getElementHandler().get_seed_element();
                  if(seed)
                    {
                      const std::deque<std::vector<int> > &quads= paver.getQuads();
		      const size_t numElements= quads.size();
		      ttzElements= ElemPtrArray3d(1,1,numElements);
		      for(size_t i= 0;i<numElements;i++)
			{
			  std::vector<int> nodeIndexes= quads[i];
			  const size_t nNodes= nodeIndexes.size();
			  if(nNodes>0)
			    {
			      ID nTags(nNodes);
			      for(size_t j= 0; j<nNodes; j++)
				{
				  const Node *n= ttzNodes(1,1,nodeIndexes[j]+1);
				  const int nTag= n->getTag();
				  nTags[j]= nTag;
				}
			      Element *tmp= seed->getCopy();
			      tmp->setIdNodes(nTags);
			      ttzElements(1,1,i+1)= tmp;
			    }
			  else
			    std::cerr << getClassName() << "::" << __FUNCTION__
			              << "; empty quad at position: " << i
			              << std::endl;
			}
                      add_elements(ttzElements);
                      retval= true;
                    }
                  else if(verbosity>0)
                    std::clog << getClassName() << "::" << __FUNCTION__
		              << "; seed element not set." << std::endl;
                  if(verbosity>4)
                    std::clog << "created." << std::endl;
                }
              else
                std::cerr << getClassName() << "::" << __FUNCTION__
		          << "; preprocessor undefined." << std::endl;
            }
      }
    else
      std::cerr << getClassName() << "::" << __FUNCTION__
		<< "; there is no nodes for the elements." << std::endl;
    const size_t numElements= ttzElements.NumPtrs();
    if(numElements==0 && verbosity>0)
      std::clog << getClassName() << "::" << __FUNCTION__
	        << "; warning 0 elements created for entity: " << getName()
	        << std::endl;
    return retval;
  }

//! @brief Triggers mesh creation.
void XC::PolygonalFace::genMesh(meshing_dir dm)
  {
    Paver paver;
    if(verbosity>3)
      std::clog << "Meshing polygonal surface...("
		<< getName() << ")...";
    create_nodes(paver);
    if(ttzElements.Null())
      create_elements(paver);
    else
      if(verbosity>2)
        std::clog << getClassName() << "::" << __FUNCTION__
	          << "; elements for surface: '" << getName()
		  << "' already exist." << std::endl;      
    if(verbosity>3)
      std::clog << "done." << std::endl;
  }