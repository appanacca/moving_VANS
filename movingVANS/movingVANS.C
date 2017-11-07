/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | Copyright (C) 2011-2013 OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Application
    icoFoam

Description
    Transient solver for incompressible, laminar flow of Newtonian fluids.

\*---------------------------------------------------------------------------*/

//#include "kdtree.H"
#include "eulerClass.H"


#include "fvCFD.H"
#include "pisoControl.H"


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

int main(int argc, char *argv[])
{

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
    int nSamples = 1778498;
	int dimx = 4;
	int dimy = 3;

	Eigen::Matrix<double, Dynamic, Dynamic>  mat(nSamples, dimx);
	Eigen::Matrix<double, Dynamic, Dynamic>  maty(nSamples, dimy);

	char* res = "result.dat";
	read_file(mat, maty, res);

	KDTreeEigenMatrixAdaptor< Eigen::Matrix<double,Dynamic,Dynamic>,nanoflann::metric_L2> mat_index(mat, 20 );

	kdtree_build<double>(mat_index, nSamples /* samples */, dimx /* dim */, dimy);

	// Query point:  points in wich we will ask for NN in the kdtree
	std::vector<double> query_pt(4);


    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    #include "setRootCase.H"

    #include "createTime.H"
    #include "createMesh.H"

    pisoControl piso(mesh);

    #include "createFields.H"
    #include "initContinuityErrs.H"

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    Info << "creates canopy.." << endl;
    Euler canopy(mesh, U, mat_index, maty);
    canopy.initialize_solid_phase();


    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    Info<< "\nStarting time loop\n" << endl;

    while (runTime.loop())
    {
        Info<< "Time = " << runTime.timeName() << nl << endl;


        #include "CourantNo.H"


scalar old_t(runTime.times()[runTime.times().size()-1].value());
word old_t_word = name(old_t);
//Info << "this is my old time-step: " << old_t_word << endl;



//	cout << "nn: " << "(" << mat(a,0) << ", " << mat(a,1) << ", " << mat(a,2) << ", " << mat(a,3) << ")" << endl;
//	cout << "K: " << "(" << maty(a,0) << ", " << maty(a,1) << ", " << maty(a,2)  << ")" << endl;

scalar flag_k_update = readScalar(transportProperties.lookup("k_update"));

if (flag_k_update == 1){ 

forAll(K, j){
    if( K[j].xx() != 0){

        if(U[j][0]>0 && U[j][1]>0){
           angleUV_k[j] = 90 -angleS[j] -angleUV[j];
        }
        else if(U[j][0]<0 && U[j][1]>0){
           angleUV_k[j] = 90 +angleS[j] -angleUV[j];
        }
        else if(U[j][0]<0 && U[j][1]<0){
           angleUV_k[j] = 90 -angleS[j] -angleUV[j];
        }
        else if(U[j][0]>0 && U[j][1]<0){
           angleUV_k[j] = 90 -angleS[j] +angleUV[j];
        }
    }
}

forAll(K, j){
    if( K[j].xx() != 0)
    {
        if(std::fabs(angleUV[j]) > 45){
            double th = std::fabs(angleUV[j]);
    		query_pt[0] = th; 
    		query_pt[1] = std::fabs(angleUW_k[j]); 
    		query_pt[2] = reynolds[j]; 
    		query_pt[3] = por[j]; 

            double a = kdtree_search<double>(mat_index, query_pt);
	        K[j].xx() = maty(a,1);
            K[j].yy() = maty(a,2);
            K[j].zz() = maty(a,0);
        }

    	query_pt[0] = std::fabs(angleUV[j]); 
    	query_pt[1] = std::fabs(angleUW_k[j]); 
    	query_pt[2] = reynolds[j]; 
    	query_pt[3] = por[j]; 

        double a = kdtree_search<double>(mat_index, query_pt);   
	    K[j].xx() = maty(a,0);
        K[j].yy() = maty(a,2);
        K[j].zz() = maty(a,1);
    }
}

}
else{ Info << "Not updating K" << endl;}




volVectorField KU = K & (U-Us);

volVectorField porU = por * U;

volVectorField gradPorgradU = (fvc::grad(U) & fvc::grad(por) );



//volVectorField laplacianPorU = (fvc::laplacian(por) * U);

        fvVectorMatrix UEqn
        (
            fvm::ddt(U)
          + (1/por)*fvm::div(phi*phiPor, U)
          - fvm::laplacian(nu, U)
          - (nu/por)* (fvc::grad(U) & fvc::grad(por)) //gradPorgradU
          - (nu/por)*fvc::laplacian(por) * U
	  + fvc::Sp(por*nu*(1/(LenRef*LenRef)),KU)

        );

        if (piso.momentumPredictor())
        {
            solve(UEqn == -fvc::grad(p));
        }

        // --- PISO loop
        while (piso.correct())
        {
            volScalarField rAU(1.0/UEqn.A());

            volVectorField HbyA("HbyA", U);
            HbyA = rAU*UEqn.H();
            surfaceScalarField phiHbyA
            (
                "phiHbyA",
                (fvc::interpolate(HbyA) & mesh.Sf())
              + fvc::interpolate(rAU)*fvc::ddtCorr(U, phi)
            );

            adjustPhi(phiHbyA, U, p);

            // Non-orthogonal pressure corrector loop
            while (piso.correctNonOrthogonal())
            {
                // Pressure corrector

                fvScalarMatrix pEqn
                (
                    fvm::laplacian(rAU, p) == fvc::div(phiHbyA)
                );

                pEqn.setReference(pRefCell, pRefValue);

                pEqn.solve(mesh.solver(p.select(piso.finalInnerIter())));

                if (piso.finalNonOrthogonalIter())
                {
                    phi = phiHbyA - pEqn.flux();
                }
            }

            #include "continuityErrs.H"

            U = HbyA - rAU*fvc::grad(p);
            U.correctBoundaryConditions();

	/////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////
scalar flag_canopy_update = readScalar(transportProperties.lookup("canopy_update"));

if (flag_canopy_update == 1){ 

scalar temps = runTime.value();

Info << temps << endl;

  int plo,i;
  plo=0;
  i=0;

  canopy.spread_solid_fraction();
  //canopy.update_flowfield();
  while (canopy.get_time() < temps){

    canopy.nextShapes(temps);
    canopy.spread_solid_fraction();    

    canopy.incrTime_updateTimeSteps();
    canopy.broadcast_orientation_to_childrens();

    plo++;
    if (plo > 50){
      //canopy.show_all();
      canopy.plotting_block();
      plo=0;
      };
    i++;
    
    }


  int m,n;
  forAll(U, iuv){
    //Info <<  "writing cell : "<< iuv << endl;
    canopy.solid_coordinates(iuv, &m, &n); //finds nearest elementary beam
    angleS[iuv] = canopy.local_solid_orientation(m, n); //returns
    Us[iuv][0] = canopy.local_solid_velocity(m, n, 0); //returns
    Us[iuv][1] = canopy.local_solid_velocity(m, n, 1); //returns
    por[iuv] = 1. - canopy.local_solid_fraction(iuv); //finds nearest point of the mesh used to compute the solid fraction and returns
    
   // Info << Us[iuv] << endl;
   // std::cout << canopy.local_solid_velocity(m, n, 0)  << std::endl;
  }

Us.write();
angleS.write();

}
else{ Info << "Not moving canopy" << endl;}

/////////////////////////////////////////////////////////////////////////////////

	dimensionedScalar tolerance
	(
	"tolerance",
	dimensionSet(0,1,-1,0,0,0,0),
	SMALL
	); 


	angleUV = atan(U.component(1) / (U.component(0) + tolerance)) *(180.0 /constant::mathematical::pi);
	angleUW = atan(U.component(2) / (U.component(0) + tolerance)) *(180.0 / constant::mathematical::pi);
	reynolds = (mag(U)*LenRef)/nu;


	////////////////////////////////
        }

        runTime.write();

        Info<< "ExecutionTime = " << runTime.elapsedCpuTime() << " s"
            << "  ClockTime = " << runTime.elapsedClockTime() << " s"
            << nl << endl;
    }

    Info<< "End\n" << endl;

    return 0;
}


// ************************************************************************* //
