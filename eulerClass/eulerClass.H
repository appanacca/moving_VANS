#ifndef EULER_H
#define EULER_H

#include <iostream>
#include <Eigen/Dense>
#include <math.h>

/*
#include "argList.H"
#include "fvMesh.H"
#include "volFields.H"
#include "surfaceFields.H"
#include "dictionary.H"
#include "IOstreams.H"
#include "IOobject.H"
#include "IFstream.H"

#  include "setRootCase.H"
#   include "createTime.H"*/
#include "dictionary.H"
#include "IOstreams.H"
#include "IOobject.H"
#include "IFstream.H"
#include "fvc.H"

  //  #include "setRootCase.H"

   // #include "createTime.H"
    //#include "createMesh.H"

    
    //#include "createFields.H"

//using namespace Foam;

#include <nanoflann.hpp>
#include "kdtree.H"


using namespace nanoflann;

using namespace Eigen;
using namespace std;

class Euler{
public:
  Euler(const Foam::fvMesh&, const Foam::volVectorField&, KDTreeEigenMatrixAdaptor< Eigen::Matrix<double,Dynamic,Dynamic>,nanoflann::metric_L2> &, Eigen::Matrix<double, Dynamic, Dynamic>&);   // This is the constructor declaration
  ~Euler();  // This is the destructor: declaration
  void show();
  void broadcast_orientation_to_childrens();
  void macro_fields();
  void spread_solid_fraction();
  void initialize_solid_phase();
  void draw_hairs();
  void draw_childrens();
//  void update_flowfield(VectorXf &a,VectorXf &b);
  void incrTime_updateTimeSteps();
  void plotting_block();
  void nextShapes(float);
  void show_all();
  float local_solid_fraction(int i);
  float local_solid_velocity(int m,int n,int vi);
  void solid_coordinates(int i,int *M,int *N);
  float local_solid_orientation(int m,int n);
  float get_time();


  
//  void set_fluid_mesh(VectorXf &a, VectorXf &b);

private:
  //template <typename num_t> double kdtree_search(KDTreeEigenMatrixAdaptor< Eigen::Matrix<double,Dynamic,Dynamic>,nanoflann::metric_L2>& mat_index, std::vector<num_t>& query_pt);

  float xFDPoints_uv(int i);
  float yFDPoints_uv(int i);
  float u(int i);
  float v(int i);
  void setInterp_past();
  void update_childrens();
  float shear_elem(int scheme,int k,int hair,int n);
  bool dtpasok();
  void explicit_scheme(int nhair);
  float implicit_scheme(int nhair);
  void update_rotules_position();
  void update_relative_velocities();
  void update_sub_block();
  void draw_fiber();
  void kernel(int kx, int ky);
  void test_maxmin(float xcenter,float ycenter,float &xmin,float &xmax,float &ymin,float &ymax,float angle,float Dx,float Dy);
  void fill_square(float xcenter,float ycenter,float angle);
  void write_sf();
  float distance(float x1,float y1,float x2,float y2);
  void setCInterp();
  void setInterp();
  float interpolent(float x,float xR,float xL,float yR,float yL);
  float time_scale, S_time, Cd,nu,rhob,mu, Lx,Ly, dx_uv,dy_uv,H,d,rhos,solid_fraction_0,lx_,ly_,dh,limangle,coef,DS,dx_,dy_,l_canopy,dt,dt_Old,dmax;
  int nuv,nh,nimplocit,nx,ny,discr,Nhair,Nchild,plo,length;
  bool adjustableTimeStep;
  MatrixXf XFD_uv,YFD_uv,new_theta,theta,theta_past,X,Y,new_X,new_Y,xInterp_past,yInterp_past,xInterp,yInterp,uXY,fX,us,vXY,fY,vs,XFD, YFD,solid_fraction,solid_fraction_K;
  VectorXf B,dissip_const;
  //VectorXf yFDPoints_uv,xFDPoints_uv
  VectorXf profile,yFDPoints,xFDPoints;
  MatrixXf cXInterp, cYInterp, cT, cX, cY;
  const Foam::fvMesh &maille;
  const Foam::volVectorField &U;
  //VectorXf u, v;
};
 
#endif