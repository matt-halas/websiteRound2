# Validation of reactingRhoPimpleCentralFoam solver

<img src="static/website/CFD_images/combustor_gif.gif" alt="" width="80%"/>
<p style="text-align: center;"><i>Figure 1: Coarse mesh combustion in Volvo Afterburner</i></p>

## Introduction

For my capstone project (or senior design project), my team and I were tasked with developing an accurate computational fluid dynamics (CFD) analysis of a novel unmanned aerial vehicle (UAV) design. We broke the simulation of the UAV into four parts; the external aerodynamics, intake, combustion, and nozzle. Having the UAV broken down into these four components made it easier to troubleshoot and ensure each component was giving accurate results.

An important part of ensuring the CFD analysis is accurate is validating the results of the CFD with similar experimental cases. This is done by recreating an experimental setup in the CFD solver and comparing the results of the simulation to experimental results.
 
My focus for this project was on the engine of the UAV. For this analysis, we used a simple cylindrical engine with a flame holder blocking 40% of the combustor area. This geometry is very similar to the Volvo Afterburner common research model. The geometry for this experimental case is shown in figure 1.

<img src="static/website/CFD_images/geometry.PNG" alt="" width="80%"/>
<p style="text-align: center;"><i>Figure 2: Volvo Afterburner Geometry</i></p>


## Background

More information about this validation case can be found [here](https://community.apan.org/cfs-file/__key/widgetcontainerfiles/3fc3f82483d14ec485ef92e206116d49-g-_2D00_tM6tEO4PkenM5KsnY8ctg-page-0cases/MVP2_5F00_Validation_5F00_Case_5F00_Final.pdf). The report covers the boundary conditions, domain, and experimental data for this case.

### Mesh

The geometry was recreated and meshed using ANSA. The meshed geometry is shown in figure 3. A half geometry with symmetry on the bottom wall was used to save on computing resources. The combustor was approximated to be 2-D. Additionally, instead of refining the mesh near the walls, wall functions were used to approximate no-slip conditions on the walls. This method was also more compatible with the solver used for this validation. The solver uses local time stepping, which may give issues when transient effects are present, such as in the beginning of combustion.

<img src="static/website/CFD_images/mesh.jpg" alt="" width="40%"/>
<p style="text-align: center;"><i>Figure 3: Close-up of flame holder on meshed geometry</i></p>

### Solver

The reactingPimpleCentralFoam solver was used for this validation. Reacting was required for the combustion and 'pimple' combines the PISO and SIMPLE algorithms to solve the governing equaitons. This is a compressible solver, which is not necessarily required for the low velocity in the combustor, but it is required for the other components of the UAV where flow velocities closer to or at M=1 are encountered. The governing equations for this solver are the Navier-Stokes equations in conservative form. More information about the solver can be found on the OPENFoam documentation.

<!--
<img style="background-color: white; border: 10px solid #FFFFFF;" src="https://latex.codecogs.com/svg.image?\bg{white}\frac{\partial&space;\rho}{\partial&space;t}&plus;\nabla\cdot&space;(\rho&space;\overrightarrow{U})=0" alt=""/>

<img style="background-color: white; border: 10px solid #FFFFFF;" src="https://latex.codecogs.com/svg.image?\bg{white}\frac{\partial(\rho\vec{U})}{\partial&space;t}&space;&plus;&space;\nabla&space;\cdot&space;\left&space;[\vec{U}&space;(\rho\vec{U})&space;\right]&space;&plus;&space;\nabla&space;p&space;-&space;\nabla&space;\cdot&space;\tau&space;=&space;0" alt=""/>

<img style="background-color: white; border: 10px solid #FFFFFF;" src="https://latex.codecogs.com/svg.image?\bg{white}\frac{\partial&space;\rho&space;E}{\partial&space;t}&space;&plus;&space;\nabla&space;\cdot&space;(\vec{U}(\rho&space;E))&space;&plus;&space;\nabla\cdot[\vec{U}p]-\nabla\cdot(\tau\cdot\vec{U})&plus;\nabla\cdot&space;j&space;=&space;0" alt=""/>
-->

### Boundary conditions

The boundary conditions used for this simulation are summarized in table 1.

<p style="text-align: center;"><i>Table 1: Boundary conditions</i></p>
<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 20%"></th>
        <th style="width: 20%">Inlet</th>
        <th style="width: 20%">Outlet</th>
        <th style="width: 20%">Walls/Flameholder</th>
        <th style="width: 20%">Front/Back</th>
    </tr>
    <tr>
        <td>Velocity</td>
        <td>17.36668 m/s</td>
        <td>zeroGradient</td>
        <td>noSlip</td>
        <td>empty</td>
    </tr>
    <tr>
        <td>Pressure</td>
        <td>100 kPa</td>
        <td>zeroGradient</td>
        <td>zeroGradient</td>
        <td>empty</td>
    </tr>
    <tr>
        <td>Temperature</td>
        <td>288 K</td>
        <td>zeroGradient</td>
        <td>zeroGradient*</td>
        <td>empty</td>
    </tr>
    <tr>
        <td>Turbulence Kinetic Energy (k)</td>
        <td>TurbIntensity
        KineticEnergyInlet: 0% intensity </td>
        <td>zeroGradient</td>
        <td>kLowReWallFunc </td>
        <td>empty</td>
    </tr>
    <tr>
        <td>Specific Rate of Dissapation (&omega;)</td>
        <td>0</td>
        <td>zeroGradient</td>
        <td>omegaWallFunction</td>
        <td>empty</td>
    </tr>
    <tr>
        <td>Turbulence Viscosity (&nu;<sub>t</sub>)</td>
        <td>0</td>
        <td>zeroGradient</td>
        <td>nutWallFunction</td>
        <td>empty</td>
    </tr>
    <tr>
        <td>Turbulent Diffusivity (&alpha;<sub>t</sub>)</td>
        <td>calculated</td>
        <td>calculated</td>
        <td>AlphaJayatilleke
        WallFunction</td>
        <td>empty</td>
    </tr>
    <tr>
        <td>C3H8</td>
        <td>0.0382</td>
        <td>zeroGradient</td>
        <td>zeroGradient</td>
        <td>empty</td>
    </tr>
    <tr>
        <td>AIR</td>
        <td>0.9618</td>
        <td>zeroGradient</td>
        <td>zeroGradient</td>
        <td>empty</td>
    </tr>
</table>

*The temperature of the flame holder was set to 1000 K to initiate the combustion and was set to zeroGradient after

### Combustion model

The eddy dissipation concept (EDC) model was used for the combustion in this simulation. This model is valid for premixed combustion and has been used and verified for bluff body stabilized flames.

Selecting the correct combustion mechanism proved to be difficult for this case. The overall reaction of propane with oxygen is:

<img style="background-color: white; border: 10px solid #FFFFFF;" src="https://latex.codecogs.com/svg.image?C_3H_8&plus;5O_2\rightarrow&space;3CO_2&plus;4H_2O" alt=""/>

In reality, the reaction between propane and oxygen involves many intermediate products. The complexity of these models varies greatly, with one detailed propane/air combustion mechanism involving 107 reactions and 31 species. Using a mechanism of this complexity would greatly increase the computational time required to run the solver, so a simpler mechanism was used. A single step mechanism often overpredicts the flame temperature as it assumes all propane reacts fully, so a compromise was to use a two step mechanism. More details on the reaction mechanism used and the available reaction mechanisms can be found on the [Cerfacs website](https://www.cerfacs.fr/cantera/mechanisms/prop.php)[newtab].

In addition to the combustion mechanisms, the data found on the Cerfacs website included transport and thermodynamic properties for each of the species involved in the reaction.

## Analysis

Three progressively finer meshes were created and simulated in OPENFoam. The number of cells in each mesh is shown in table 2.

<p style="text-align: center;"><i>Table 2: Mesh sizes used</i></p>
<table style="width: 50%; table-layout: fixed; justify-content: center; margin-left:auto; margin-right:auto;">
    <colgroup>
       <col style="width: 50%">
       <col style="width: 50%">
    </colgroup>
    <tbody>
        <tr>
            <th>Case Name</th>
            <th>Mesh Size</th>
        </tr>
        <tr>
            <td>Volvo 40</td>
            <td>2 mm</td>
        </tr>
        <tr>
            <td>Volvo 45</td>
            <td>1 mm</td>
        </tr>
        <tr>
            <td>Volvo 47</td>
            <td>0.5 mm</td>
        </tr>
    </tbody>
</table>

The flame holder boundary condition was set to 1000K until a flame stabilized behind the flame holder, after which, the boundary was returned to zeroGradient. The solver was then run until residuals stabilized. Experimental values for axial velocity and temperature were given along several points downstream of the flame holder. The distances downstream of the flame holder are given in terms of it's length (D=4 cm), i.e. 1.5D is 6 cm from the back of the flame holder.

The results of the simulations vs the experimental data is shown in figures 4 to 11. Note that typical axes convention is not used in the followng figures. Because the data points are taken at several locations vertically along the combustor, the y coordinate is represented on the y axis to stay consistent with the orientation of the combustor, while the velocity and temperature data is displayed on the x axis.

<img src="static/website/CFD_images/tempAtx=3.75D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 4: Temperature vs normalized Y coordinate at x = 3.75D</i></p>

<img src="static/website/CFD_images/tempAtx=8.75D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 5: Temperature vs normalized Y coordinate at x = 8.75D</i></p>

<img src="static/website/CFD_images/tempAtx=13.75D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 6: Temperature vs normalized Y coordinate at x = 13.75D</i></p>

The temperature profile of the simulations is generally less diffused than the temperature profile from the experimental data. The thermal diffusion decreases as the mesh size is refined. This discrepancy may be due to the limitations of either the half mesh used, or the turbulence model. The half mesh does not properly capture vortex shedding, which may be preventing the temperature distribution from diffusing properly. Additionally, the rans turbulence model may be underpredicting the amount of turbulent mixing occurring in the wake of the flame holder, which would prevent the temperature distribution from diffusing over the entire profile of the combustor.

<img src="static/website/CFD_images/velAtx=0.375D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 7: Velocity vs normalized Y coordinate at x = 0.375D</i></p>

<img src="static/website/CFD_images/velAtx=0.95D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 8: Velocity vs normalized Y coordinate at x = 0.95D</i></p>

<img src="static/website/CFD_images/velAtx=1.53D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 9: Velocity vs normalized Y coordinate at x = 1.53D</i></p>

<img src="static/website/CFD_images/velAtx=3.75D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 10: Velocity vs normalized Y coordinate at x = 3.75D</i></p>

<img src="static/website/CFD_images/velAtx=9.4D.png" alt="" width="50%"/>
<p style="text-align: center;"><i>Figure 11: Velocity vs normalized Y coordinate at x = 9.4D</i></p>

The refined mesh (Volvo 47) shows the best agreement with experimental velocity data at points near the flame holder, but deviates from the experimental data at the very last velocity point. The exact reasoning for this is unclear, but it may also be caused by the half geometry not capturing vortex shedding.

## Conclusion

The temperature and velocity profiles of the simulation show some agreement with the experimental data, but improvements could be made to the simulation to ensure the solver and combustion models used accurately represent what occurs in the combustor. The simulation should be redone with a full geometry to capture asymmetrical effects like vortex shedding. This may solve the issue of the temperature profile of the simulation being less diffused than that of the experiment.