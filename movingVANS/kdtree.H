/***********************************************************************
 * Software License Agreement (BSD License)
 *
 * Copyright 2011-2016 Jose Luis Blanco (joseluisblancoc@gmail.com).
 *   All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 * THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *************************************************************************/

#include <nanoflann.hpp>


#include <iostream>
#include <fstream>

#include <Eigen/Dense>

using namespace Eigen;
using namespace std;
using namespace nanoflann;

//const int SAMPLES_DIM = 4;


template <typename Der>
void read_file(Eigen::MatrixBase<Der> &mat, Eigen::MatrixBase<Der> &maty, const char* file= "test.dat")
{
	double th(0), ph(0), re(0), po(0), h11(0), h22(0), h33(0);
	ifstream infile;
	infile.open(file, ios_base::in);

	int i = 0;
   	while( i<mat.rows())
   	{
   		infile >>th >> ph >> re >> po >> h11 >> h22 >> h33;
     	mat(i,0) = th;
     	mat(i,1) = ph;
     	mat(i,2) = re;
     	mat(i,3) = po;
     	maty(i,0) = h11;
     	maty(i,1) = h22;
     	maty(i,2) = h33;
      	++i;
    }
    infile.close();

//  cout << mat(0,0) << " " << mat(2,6) << endl;
}


template <typename num_t>
void kdtree_build(KDTreeEigenMatrixAdaptor< Eigen::Matrix<num_t,Dynamic,Dynamic>,nanoflann::metric_L2> &mat_index, const size_t nSamples, const size_t dimx,  const size_t dimy)
{


	//cout << mat << endl;
	//cout << maty << endl;

	// Generate points:  points used for the tree generation
	//generateRandomPointCloud(mat, nSamples, dim, max_range);


	// ------------------------------------------------------------
	// construct a kd-tree index:
	//    Some of the different possibilities (uncomment just one)
	// ------------------------------------------------------------
	// Dimensionality set at run-time (default: L2)
//	typedef KDTreeEigenMatrixAdaptor< Eigen::Matrix<num_t, Dynamic, Dynamic> >  my_kd_tree_t;

	// Dimensionality set at compile-time
//	typedef KDTreeEigenMatrixAdaptor< Eigen::Matrix<num_t,Dynamic,Dynamic> >  my_kd_tree_t;

//KDTreeEigenMatrixAdaptor< Eigen::Matrix<num_t,Dynamic,Dynamic>,nanoflann::metric_L2> my_kd_tree_t;

	// Dimensionality set at compile-time: Explicit selection of the distance metric: L2_simple
//	typedef KDTreeEigenMatrixAdaptor< Eigen::Matrix<num_t,Dynamic,Dynamic>,nanoflann::metric_L2_Simple>  my_kd_tree_t;

	// Dimensionality set at compile-time: Explicit selection of the distance metric: L1
//	typedef KDTreeEigenMatrixAdaptor< Eigen::Matrix<num_t,Dynamic,Dynamic>,nanoflann::metric_L1>  my_kd_tree_t;

	//KDTreeEigenMatrixAdaptor< Eigen::Matrix<num_t,Dynamic,Dynamic>,nanoflann::metric_L2> mat_index(mat, 20 /* max leaf */ );
	mat_index.index->buildIndex();

}


template <typename num_t>
double kdtree_search(KDTreeEigenMatrixAdaptor< Eigen::Matrix<double,Dynamic,Dynamic>,nanoflann::metric_L2>& mat_index, std::vector<num_t>& query_pt)
{

	int dimx = 4;

	// do a knn search
	const size_t num_results = 1;  // number of neareset neigbour that I want in return for each point in the query
	vector<size_t> ret_indexes(num_results);    // vector containing the indices of the results
	vector<num_t> out_dists_sqr(num_results);    // vector containig the distances

	nanoflann::KNNResultSet<num_t> resultSet(num_results);


	resultSet.init(&ret_indexes[0], &out_dists_sqr[0] );  // inizialize the results with the 
	mat_index.index->findNeighbors(resultSet, &query_pt[0], nanoflann::SearchParams(10));

	/*std::cout << "knnSearch(nn="<<num_results<<"): \n";
	for (size_t i=0; i<num_results; i++)
	{
		std::cout << "ret_index["<<i<<"]=" << ret_indexes[i] << " out_dist_sqr=" << out_dists_sqr[i] << endl;

		//cout << "nn: " << "(" << mat(ret_indexes[i],0) << ", " << mat(ret_indexes[i],1) << ", " << mat(ret_indexes[i],2) << ", " << mat(ret_indexes[i],3) << ")" << endl;
		//cout << "K: " << "(" << maty(ret_indexes[i],0) << ", " << maty(ret_indexes[i],1) << ", " << maty(ret_indexes[i],2)  << ")" << endl;

	}*/

	return ret_indexes[0];

}
