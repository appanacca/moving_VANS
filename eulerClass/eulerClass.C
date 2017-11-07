#include "eulerClass.H"


Euler::~Euler() {
}

Euler::Euler(const Foam::fvMesh& maille, const Foam::volVectorField& U, KDTreeEigenMatrixAdaptor< Eigen::Matrix<double,Dynamic,Dynamic>,nanoflann::metric_L2> & mat, Eigen::Matrix<double, Dynamic, Dynamic>& mat_k) : maille(maille), U(U) {

Foam::dictionary porousSolidProperties(Foam::IFstream("constant/porousSolidProperties")());

Foam::dictionary transportProperties(Foam::IFstream("constant/transportProperties")());

Foam::dictionary controlDict(Foam::IFstream("system/controlDict")());


Cd = Foam::readScalar(porousSolidProperties.lookup("Cd")); //drag coefficient
Foam::dimensionedScalar nu_foam(transportProperties.lookup("nu")); //the value of fluid kinematic viscosity
nu = nu_foam.value();
rhob = Foam::readScalar(porousSolidProperties.lookup("rhob")); //the value of fluid density
mu = nu*rhob;
nh = Foam::readScalar(porousSolidProperties.lookup("nh")); //# the beam is discretized in nh-1 elements
rhos = Foam::readScalar(porousSolidProperties.lookup("rhos")); //the value of solid density
double por = Foam::readScalar(porousSolidProperties.lookup("porosity")); // porosity
solid_fraction_0 = 1.-por; // solidfraction

nuv = U.size();

//################################################### BEAM
Lx = Foam::readScalar(porousSolidProperties.lookup("Lx"));
Ly = Foam::readScalar(porousSolidProperties.lookup("Ly"));
H = Foam::readScalar(porousSolidProperties.lookup("H"));
dh = H/(nh-1); //# size of an infinitesimal beam
Nhair = Foam::readScalar(porousSolidProperties.lookup("Nhair")); //# number of hairs
Nchild = Foam::readScalar(porousSolidProperties.lookup("Nchild")); //# paire

l_canopy = Lx - 2.*H;
DS = l_canopy/(Nhair*(1+Nchild)-1);
//REV
lx_ = DS;
ly_ = H/(nh-1);
d = solid_fraction_0*sqrt(pow(DS,2)/(M_PI/4.)); //beam diameter
discr = 5*round(Lx/lx_);
nx = round(Lx/Ly)*discr+1;
ny = discr+1;
dx_ = Lx/(nx-1);
dy_ = Ly/(ny-1);
coef = 16./(M_PI*pow(d,4)*rhos);

S_time = Foam::readScalar(controlDict.lookup("startTime"));

xFDPoints = VectorXf::LinSpaced(nx,-0.5*Lx,0.5*Lx);//MESH FOR SOLID FIELDS
yFDPoints = VectorXf::LinSpaced(ny,0.,Ly);

new_theta = MatrixXf::Zero(Nhair,nh-1);
theta = MatrixXf::Zero(Nhair,nh-1);
theta_past = MatrixXf::Zero(Nhair,nh-1);
X = MatrixXf::Zero(Nhair,nh);
Y = MatrixXf::Zero(Nhair,nh);
new_X = MatrixXf::Zero(Nhair,nh);
new_Y = MatrixXf::Zero(Nhair,nh);
xInterp_past = MatrixXf::Zero(Nhair,nh-1);
yInterp_past = MatrixXf::Zero(Nhair,nh-1);
xInterp = MatrixXf::Zero(Nhair,nh-1);
yInterp = MatrixXf::Zero(Nhair,nh-1);

cXInterp = MatrixXf::Zero(Nchild*Nhair,nh-1);
cYInterp = MatrixXf::Zero(Nchild*Nhair,nh-1);
cT = MatrixXf::Zero(Nchild*Nhair,nh-1);
cX = MatrixXf::Zero(Nchild*Nhair,nh);
cY = MatrixXf::Zero(Nchild*Nhair,nh);

uXY = MatrixXf::Zero(Nhair,nh-1);
vXY = MatrixXf::Zero(Nhair,nh-1);
us = MatrixXf::Zero(Nhair,nh-1);
vs = MatrixXf::Zero(Nhair,nh-1);
solid_fraction = MatrixXf::Zero(ny,nx);
solid_fraction_K = MatrixXf::Zero(ny,nx);

float B_bending = Foam::readScalar(porousSolidProperties.lookup("B_bending")); //# paire


B = VectorXf::Constant(nh-2, B_bending );
dissip_const = VectorXf::Constant(nh-2, 0.1*sqrt(4*B.maxCoeff()/coef)); // #critical damping
// options
adjustableTimeStep = true;
nimplocit = 50;
limangle = M_PI/180.;
time_scale = 0.1 * sqrt(pow(dh,2)/B.maxCoeff()*(M_PI*pow(d,4)*rhos)/4);

plo = 0;
dt = time_scale;
dt_Old = time_scale;

//////////////////////////////////////////////////////////////////////

  std::vector<double> query_pt(4);
        query_pt[0] = 0; // 0
        query_pt[1] = 0; // angleUV_k
        query_pt[2] = 0;  //Re
        query_pt[3] = 0.4; //por
double a = kdtree_search<double>(mat, query_pt);

std::cout <<"THIS IS THE POINT: " << a << std::endl;


std::cout <<"THIS IS THE K: " << mat_k(a,0) << mat_k(a, 1) << mat_k(a, 2) << std::endl;

//////////////////////////////////////////////////////////////////////

}

float Euler::xFDPoints_uv(int i){
return maille.C()[i][0];
}
float Euler::yFDPoints_uv(int i){
return maille.C()[i][1];
}
float Euler::u(int i){
return U[i][0];
}
float Euler::v(int i){
return U[i][1];
}

void Euler::setInterp(){
  int n,m;
  for (m=0; m<nh-1; m++){
    for (n=0; n<Nhair; n++){
      xInterp(n,m) = (X(n,m)+X(n,m+1))/2.;
      yInterp(n,m) = (Y(n,m)+Y(n,m+1))/2.;
      }
    }
  }

void Euler::setInterp_past(){
  int etage,hair;
  for (etage=0;etage<nh-1;etage++){
      for (hair=0;hair<Nhair;hair++){
        xInterp_past(hair,etage) = xInterp(hair,etage);
        yInterp_past(hair,etage) = yInterp(hair,etage);
        }
      }
  }

void Euler::setCInterp(){
  int n,i,m;
  for (m=0; m<nh-1; m++){
    for (n=0; n<Nhair; n++){
    for (i=0; i<Nchild; i++){
        cXInterp(n*Nchild+i,m) = (cX(n*Nchild+i,m)+cX(n*Nchild+i,m+1))/2.;
        cYInterp(n*Nchild+i,m) = (cY(n*Nchild+i,m)+cY(n*Nchild+i,m+1))/2.;
        }
      }
    }
  }

void Euler::broadcast_orientation_to_childrens(){
int n,j,m;
for (n=1; n<nh-1; n++){
  for (m=0; m<Nchild/2; m++){
    cT(m,n) = theta(0,n);
    }
  for (m=Nchild/2; m<Nchild; m++){
    cT((Nhair-1)*Nchild+m,n) = theta(Nhair-1,n);
    }
  }
for (n=0;n<Nhair-1;n++){
  for (m=1;m<nh-1;m++){
    for (j=Nchild/2;j<Nchild;j++){
      cT(n*Nchild+j,m) = interpolent(cX(n*Nchild+j,0),X(n,0),X(n+1,0),theta(n,m),theta(n+1,m));
      }
    for (j=0;j<Nchild/2;j++){
      cT((n+1)*Nchild+j,m) = interpolent(cX((n+1)*Nchild+j,0),X(n,0),X(n+1,0),theta(n,m),theta(n+1,m));
      }
    }
  }
}

void Euler::draw_hairs(){
int n,m;
for (n=0;n<Nhair;n++){
for (m=1;m<nh;m++){
  X(n,m) = X(n,m-1) + dh*sin(theta(n,m-1));
  Y(n,m) = Y(n,m-1) + dh*cos(theta(n,m-1));
  }
}
}

void Euler::draw_childrens(){
int n,j,m;
for (n=0;n<Nhair;n++){
for (j=0;j<Nchild;j++){
for (m=1;m<nh;m++){
  cX(n*Nchild+j,m) = cX(n*Nchild+j,m-1) + dh*sin(cT(n*Nchild+j,m-1));
  cY(n*Nchild+j,m) = cY(n*Nchild+j,m-1) + dh*cos(cT(n*Nchild+j,m-1));
  }
}
}
}

float Euler::interpolent(float x,float xR,float xL,float yR,float yL){
  float dydx,interp_value;
  dydx = ( yR - yL ) / ( xR - xL );
  interp_value = yL + dydx * ( x - xL );
  return interp_value;
}

void Euler::initialize_solid_phase(){
int m,n;
if (Nhair>1){
  for (n=0; n<Nhair; n++){
    X(n,0) = n*(Nchild+1)*DS - 0.5*l_canopy+0.5*Nchild*DS;
    }
  }
for (n=0; n<Nhair; n++){
  for (m=0; m<Nchild/2; m++){
  cX(n*Nchild+m,0) = X(n,0) - (Nchild/2 - m)*DS;
  }
  for (m=Nchild/2; m<Nchild; m++){
  cX(n*Nchild+m,0) = X(n,0) + (1 - Nchild/2 + m)*DS;
  }
}
  draw_hairs();
  setInterp();
  setInterp_past();
  update_childrens();

  for (n=0; n<Nhair; n++){
    for (m=0; m<nh; m++){
      new_X(n,m) = X(n,m);
      new_Y(n,m) = Y(n,m);
      }
    }
}

void Euler::show_all(){
  std::cout << "X" << std::endl;
  std::cout << X << std::endl;
  std::cout << "Y" << std::endl;  
  std::cout << Y << std::endl;
  std::cout << "theta" << std::endl;
  std::cout << theta << std::endl;
  std::cout << "cT" << std::endl;  
  std::cout << cT << std::endl;
  std::cout << "cX" << std::endl;  
  std::cout << cX << std::endl;
  std::cout << "cY" << std::endl;  
  std::cout << cY << std::endl;
  std::cout << "new_X" << std::endl;  
  std::cout << new_X << std::endl;
  std::cout << "new_Y" << std::endl;  
  std::cout << new_Y << std::endl;
  std::cout << "xInterp_past" << std::endl;  
  std::cout << xInterp_past << std::endl;
  std::cout << "yInterp_past" << std::endl;  
  std::cout << yInterp_past << std::endl;
  std::cout << "xInterp" << std::endl;  
  std::cout << xInterp << std::endl;
  std::cout << "yInterp" << std::endl;  
  std::cout << yInterp << std::endl;
  std::cout << "cXInterp" << std::endl;  
  std::cout << cXInterp << std::endl;
  std::cout << "cYInterp" << std::endl;
  std::cout << cYInterp << std::endl;
}
float Euler::local_solid_velocity(int m,int n,int vi){
  if (vi==0){
  return us(n,m);
  }
  else if (vi==1){
  return vs(n,m);
  }
  else{
  std::cout << "should be 0 or 1 !!!" << std::endl;
  return 0.;
  }
  }
float Euler::local_solid_orientation(int m,int n){
  return theta(n,m);
}

void Euler::solid_coordinates(int i,int *M,int *N){
  int m,n;
  float dist_test, dmin;
  m=0;
  n=0;
  dmin = distance(xFDPoints_uv(i),yFDPoints_uv(i),xInterp(n,m),yInterp(n,m));
  for (n=0;n<Nhair;n++){
    for (m=0;m<nh-1;m++){
      dist_test = distance(xFDPoints_uv(i),yFDPoints_uv(i),xInterp(n,m),yInterp(n,m));
      if (dist_test < dmin){
        dmin = dist_test;
        (*M) = m;
        (*N) = n;
        }
      }
    }
  }

float Euler::local_solid_fraction(int i){
  int m,n;
  float dist_test, dmin, solid_fraction_xy;
    m=0;
    n=0;
    dmin = distance(xFDPoints_uv(i),yFDPoints_uv(i),xFDPoints(n),yFDPoints(m));
    solid_fraction_xy = solid_fraction_K(m,n);
    for (n=0;n<nx;n++){
      for (m=0;m<ny;m++){
        dist_test = distance(xFDPoints_uv(i),yFDPoints_uv(i),xFDPoints(n),yFDPoints(m));
        if (dist_test < dmin){
          dmin = dist_test;
          solid_fraction_xy = solid_fraction_K(m,n);
          }
        }
      }
  return solid_fraction_xy;
  }

void Euler::spread_solid_fraction(){
  int i,j;
  for (i=0; i<nx; i++){
    for (j=0; j<ny; j++){
      solid_fraction(j,i)=0.;
      }
    }
  write_sf();
  //smooth solid fraction
  int nREVx,nREVy;
  nREVx = round(0.5*lx_/dx_);
  nREVy = round(0.5*ly_/dy_);
  kernel(nREVx,nREVy);
}

void Euler::kernel(int kx, int ky){
  int i,j,ii,jj,ii_,jj_;
  for (i=0; i<nx; i++){
    for (j=0; j<ny; j++){
      solid_fraction_K(j,i)=0.;
      for (ii=i-kx; ii<i+kx+1; ii++){
        for (jj=j-ky; jj<j+ky+1; jj++){
          //symmetry
          if (ii < 0) ii_ = -ii;
          else if (ii > nx-1) ii_ = 2*(nx-1)-ii;
          else ii_ = ii;
          if (jj < 0) jj_ = -jj;
          else if (jj > ny-1) jj_ = 2*(ny-1)-jj;
          else jj_ = jj;
          solid_fraction_K(j,i) += solid_fraction(jj_,ii_);
          }
        }
      solid_fraction_K(j,i) /= (2*kx+1)*(2*ky+1);
      }
    }
  }

void Euler::fill_square(float xcenter,float ycenter,float angle){
        int i,j;
        float xmin,xmax,ymin,ymax,Dx,Dy;
        //calcul bornes
        Dx = -0.5*lx_;
        Dy = -0.5*ly_;
        xmin = xcenter + cos(angle)*Dx + sin(angle)*Dy;
        xmax = xcenter + cos(angle)*Dx + sin(angle)*Dy;
        ymin = ycenter + sin(angle)*Dx + cos(angle)*Dy;
        ymax = ycenter + sin(angle)*Dx + cos(angle)*Dy;
        //test_maxmin(xcenter,ycenter,xmin,xmax,ymin,ymax,angle,Dx,Dy);
        Dx = -0.5*lx_;
        Dy = +0.5*ly_;
        test_maxmin(xcenter,ycenter,xmin,xmax,ymin,ymax,angle,Dx,Dy);
        Dx = +0.5*lx_;
        Dy = -0.5*ly_;
        test_maxmin(xcenter,ycenter,xmin,xmax,ymin,ymax,angle,Dx,Dy);
        Dx = +0.5*lx_;
        Dy = +0.5*ly_;
        test_maxmin(xcenter,ycenter,xmin,xmax,ymin,ymax,angle,Dx,Dy);
        //recherche des points dans le REV
        i=0;
        while (xFDPoints(i)<xmin) i++;
        while (xFDPoints(i)<xmax){
          j=0;
          while (yFDPoints(j)<ymin) j++;
          while (yFDPoints(j)<ymax){            
            solid_fraction(j,i) += solid_fraction_0;
            j++;
            }
          i++;
          }
}

void Euler::test_maxmin(float xcenter,float ycenter,float &xmin,float &xmax,float &ymin,float &ymax,float angle,float Dx,float Dy){
        float xcoin,ycoin;
        xcoin = xcenter + cos(angle)*Dx + sin(angle)*Dy;
        ycoin = ycenter + sin(angle)*Dx + cos(angle)*Dy;
        if (xcoin<xmin) xmin = xcoin;
        if (xcoin>xmax) xmax = xcoin;
        if (ycoin<ymin) ymin = ycoin;
        if (ycoin>ymax) ymax = ycoin;
}

void Euler::write_sf(){
      int hair,child,etage;
      for (etage=0;etage<nh-1;etage++){
        for (hair=0;hair<Nhair;hair++){
          fill_square(xInterp(hair,etage),yInterp(hair,etage),theta(hair,etage));
          for (child=0;child<Nchild;child++){
            fill_square(cXInterp(hair*Nchild+child,etage),cYInterp(hair*Nchild+child,etage),cT(hair*Nchild+child,etage));
            }
          }
        }
}

float Euler::distance(float x1,float y1,float x2,float y2){
  return sqrt(pow(x1-x2,2) + pow(y1-y2,2));
}

void Euler::nextShapes(float max_time){
    // solid centers
    int etage,hair,nite;
    float err;    
    // solid velocity
    for (etage=0;etage<nh-1;etage++){
      for (hair=0;hair<Nhair;hair++){
        us(hair,etage) = (xInterp(hair,etage) - xInterp_past(hair,etage))/dt_Old;
        vs(hair,etage) = (yInterp(hair,etage) - yInterp_past(hair,etage))/dt_Old;
        }
      }
    update_relative_velocities();
    setInterp_past();

    // explicit step   
    for (hair=0;hair<Nhair;hair++) explicit_scheme(hair);
    if (adjustableTimeStep){
      while (not dtpasok() and dt<time_scale){
        dt *= 2.;
        for (hair=0;hair<Nhair;hair++) explicit_scheme(hair);
        }
      dt=std::min(max_time, std::min(time_scale, dt));
      while (dtpasok()){
        dt *= .5;
        for (hair=0;hair<Nhair;hair++) explicit_scheme(hair);
        }      
      }
    update_sub_block();
    nite=0;
    err = 1e6;
    while (err > 1e-6 and nite < nimplocit){
      for (hair=0;hair<Nhair;hair++) err = implicit_scheme(hair);
      update_sub_block();
      nite+=1;
      }

    //update geometry
    for (etage=0;etage<nh-1;etage++){
      for (hair=0;hair<Nhair;hair++){
        theta_past(hair,etage) = theta(hair,etage);
        theta(hair,etage) = new_theta(hair,etage);
        X(hair,etage+1) = new_X(hair,etage+1); // no need to update the lowest since always the same
        Y(hair,etage+1) = new_Y(hair,etage+1);
        }
      }
  update_childrens();
}

void Euler::explicit_scheme(int hair){
  float shear,interm,a,b;
  int k,n;
  for (n=1;n<nh-2;n++){
    interm = coef*B[n]*(theta(hair,n+1) - 2*theta(hair,n) + theta(hair,n-1));
    // dissipation term
    interm+= coef*dissip_const(n)*((theta(hair,n+1) - 2*theta(hair,n) + theta(hair,n-1))-(theta_past(hair,n+1) - 2*theta_past(hair,n) + theta_past(hair,n-1)))/dt_Old;

    interm/= pow(dh,2);

    // shearing force computation   
    shear = 0.;
    for (k=n;k<nh-1;k++) shear += shear_elem(0,k,hair,n);
    shear *= 1./2.*rhob*Cd*d*dh*coef;

    interm += shear;
    a=interm;
    b=(theta(hair,n) - theta_past(hair,n))/dt_Old;
    interm = b*dt+a*pow(dt,2);

    new_theta(hair,n) = interm + theta(hair,n);
    }
  //update for Neumann BC
  new_theta(hair,nh-2) = new_theta(hair,nh-3);
}

float Euler::implicit_scheme(int hair){
  float shear,interm,a,b,result;
  int k,n;
  result = 0.;
  for (n=1;n<nh-2;n++){
    interm = coef*B[n]*(new_theta(hair,n+1) - 2*new_theta(hair,n) + new_theta(hair,n-1));
    // dissipation term
    interm+= coef*dissip_const(n)*((new_theta(hair,n+1) - 2*new_theta(hair,n) + new_theta(hair,n-1))-(theta(hair,n+1) - 2*theta(hair,n) + theta(hair,n-1)))/dt;    
//    interm+= coef*gamma(n)*((theta(hair,n+1) - 2*theta(hair,n) + theta(hair,n-1))-(theta_past(hair,n+1) - 2*theta_past(hair,n) + theta_past(hair,n-1)))/dt_Old;

    interm/= pow(dh,2);

    // shearing force computation   
    shear = 0.;
    for (k=n;k<nh-1;k++) {shear += shear_elem(1,k,hair,n);}
    shear *= 1./2.*rhob*Cd*d*dh*coef;

    interm += shear;
    a=interm;
    b=(theta(hair,n) - theta_past(hair,n))/dt_Old;
    interm = b*dt+a*pow(dt,2);

    result = max(abs(new_theta(hair,n) - (interm + theta(hair,n))),result);

    new_theta(hair,n) = interm + theta(hair,n);
    }
  //update for Neumann BC
  new_theta(hair,nh-2) = new_theta(hair,nh-3);

  return result;
}

void Euler::update_childrens(){
  broadcast_orientation_to_childrens();
  draw_childrens();
  setCInterp();
}

void Euler::update_sub_block(){
    update_rotules_position();
    // solid centers
    int hair,etage;
    for (etage=0;etage<nh-1;etage++){
      for (hair=0;hair<Nhair;hair++){
      xInterp(hair,etage) = (new_X(hair,etage+1)+new_X(hair,etage))/2.;
      yInterp(hair,etage) = (new_Y(hair,etage+1)+new_Y(hair,etage))/2.;
      }
      }
    update_relative_velocities();
}

void Euler::update_rotules_position(){
  int etage,hair;
  for (etage=1;etage<nh;etage++){
    for (hair=0;hair<Nhair;hair++){
      new_X(hair,etage) = new_X(hair,etage-1) + dh*sin(new_theta(hair,etage-1));
      new_Y(hair,etage) = new_Y(hair,etage-1) + dh*cos(new_theta(hair,etage-1));
      }
    }
}
void Euler::update_relative_velocities(){
  //interpolate flow at centers of elementary beams
  int i,m,n;
  float dist_test,dmin,fX,fY;
  for (n=0;n<Nhair;n++){
    for (m=0;m<nh-1;m++){
      i=0;
      fX = u(i);
      fY = v(i);
      dmin = distance(xFDPoints_uv(i),yFDPoints_uv(i),xInterp(n,m),yInterp(n,m));;
      for (i=1; i<nuv; i++){
        dist_test = distance(xFDPoints_uv(i),yFDPoints_uv(i),xInterp(n,m),yInterp(n,m));
        if (dist_test < dmin){
          dmin = dist_test;
          fX = u(i);
          fY = v(i);
          }
        }
      uXY(n,m) = fX - us(n,m);
      vXY(n,m) = fY - vs(n,m);
      }
    }
  }


bool Euler::dtpasok(){
  int n,m;
  float result;
  result = 0.;
  for (n=0;n<Nhair;n++){
    for (m=1;m<nh-2;m++){
      result = max(abs(new_theta(n,m+1) - 2*new_theta(n,m) + new_theta(n,m-1)-(theta(n,m+1) - 2*theta(n,m) + theta(n,m-1))),result);
      }
    }
return result > limangle;
}

float Euler::shear_elem(int scheme,int k,int hair,int n){
  float result;
  // quadratic drag
  if (scheme == 0){
    result = uXY(hair,k)*abs(uXY(hair,k))*pow(cos(theta(hair,k)),2);
    result-= vXY(hair,k)*abs(vXY(hair,k))*pow(sin(theta(hair,k)),2);
    result*= cos(theta(hair,k)-theta(hair,n));
    return result;
    }
  else if (scheme == 1){
    result = uXY(hair,k)*abs(uXY(hair,k))*pow(cos(new_theta(hair,k)),2);
    result-= vXY(hair,k)*abs(vXY(hair,k))*pow(sin(new_theta(hair,k)),2);
    result*= cos(new_theta(hair,k)-new_theta(hair,n));
    }
  else {
    result = 0.;
    std::cout<< "invalid option scheme" <<std::endl;
  }
  return result;
}

void Euler::incrTime_updateTimeSteps(){
  S_time += dt;
  dt_Old = dt;
}

void Euler::plotting_block(){
  std::cout << "elapsed time : " << S_time << " s , dt = " << dt << " s." << std::endl;
  }

float Euler::get_time(){

return  S_time;
}
