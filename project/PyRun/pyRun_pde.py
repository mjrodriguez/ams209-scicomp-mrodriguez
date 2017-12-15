"""
Template file for hw6:

Directory structure:

   hw6/
       |-- newton_rootFinder/RootFinder.F90
       |                     findRootMethod_module.F90
       |                     makefile
       |                     read_initFile_module.F90
       |                     definition.h
       |                     ftn_module.F90
       |                     output_module.F90
       |                     setup_module.F90
       |                     (excluding rootFinder.init)
       |
       |-- pyRun/pyRun_rootFinder.py
       

"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt 


def make_make():
    # 1. Compile the Fortran code if has not been compiled
    #    (i.e., if 'rootFinder.exe' does not exists yet);
    #
    # 2. Otherwise do "make clean" first and then "make".
    #
    # 3. You need to change your directory from "pyRun/" to
    #    "newton_rootFinder/" to compile the Fortran code.
    
    doesExecutableExist = os.path.exists('../PDE/advection_diffusion.exe')
    if not doesExecutableExist:
        os.chdir('../PDE')
        makeIt = 'make'
        os.system(makeIt)
        os.system('rm pde.init*')
        #os.system('rm *.dat.*')
    else:
        os.chdir('../PDE')
        makeCleanMake = 'make clean && make'
        os.system(makeCleanMake)
        os.system('rm pde.init*')
        #os.system('rm *.dat.*')
    
    # os.chdir('../pyRun/')
    
    
def runtimeParameters_init(simulationType, discretizationType, N, xMin, xMax, threshold, a, kappa, Ca, tmax):
    
    # 1. Implement a routine that generates a new "rootFinder.init"
    #    runtime parameter file. Use a proper set of
    #    input arguments to produce a new rootFinder.init
    #    which has all the necessary input parameters to run the Fortran code.
    #    For instance, the first few lines can look like:
    #      run_name     (... and some space ...) 'newton'
    #      method_type  (... and some space ...) 'newton'
    #      ...
    # 2. When writing a new "rootFinder.init", check if there is an old one already.
    #    If so, rename the old one to, say, "rootFinder.init.1" before
    #    creating a new "rootFinder.init". You would end up with having multiple
    #    of them, e.g., "rootFinder.init.1", "rootFinder.init.2", etc.,
    #    along with "rootFinder.init" which is the active runtime parameter file in use.
    
    
    os.chdir('../PDE')
    if os.path.exists('./pde.init'):
        # popen command runs the terminal command and saves output
        # running os.system(command) will save a 0
        commandLine = os.popen('ls ./pde.init* | wc -l')
        numberOfInitFiles = commandLine.readline()
        commandLine.close()
        
        newFileName = 'pde.init.'+str(numberOfInitFiles).lstrip()
        renamingFile = 'mv ./pde.init ./'+newFileName
        os.system(renamingFile)
        
        
        #         call read_initFileChar('pde.init','simulation_type',simulationType)
        #         call read_initFileChar('pde.init','discretization_type', discretizationType)
        # call read_initFileInt ('pde.init','grid_size', N)
        #         call read_initFileReal('pde.init', 'x_min', xMin)
        #         call read_initFileReal('pde.init', 'x_max', xMax)
        #         call read_initFileReal('pde.init', 'threshold', threshold)
        #         call read_initFileReal('pde.init', 'advection_speed', a)
        # call read_initFileReal('pde.init', 'diffusion_constant', kappa)
        # call read_initFileReal('pde.init', 'cfl_constant', Ca)
        
        # Creating New File pde.init
        f=open('pde.init', 'w')
        f.write('simulation_type       '+simulationType+"     # [char] Specify advection, diffusion, or advection_diffusion\n")
        f.write('discretization_type       '+discretizationType+"     # [char] Specify 'center' or 'upwind'\n")
        f.write('grid_size    '+str(N)+"     # [int] Choose number of elements in spatial domain'\n")
        f.write('x_min          '+str(xMin)+"     # [real] minimum value of domain\n")
        f.write('x_max          '+str(xMax)+"     # [real] maximum value of domain\n")
        f.write('threshold      '+str(threshold)+"     # [real] Threshold value for solution convergence\n")
        f.write('advection_speed      '+str(a)+"     # [real]  Speed of traveling wave\n")
        f.write('diffusion_constant     '+str(kappa)+"     # [real] the diffusion constant\n")
        f.write('cfl_constant   '+str(Ca)+"        # [real]  Constant for CFL condition\n")
        f.write('max_time       '+str(tmax)+"       # [real] maximum time, may be more than it takes to reach steady state")
        f.close()
        
    else:
        # Creating New File pde.init
        f=open('pde.init', 'w')
        f.write('simulation_type       '+simulationType+"     # [char] Specify advection, diffusion, or advection_diffusion\n")
        f.write('discretization_type       '+discretizationType+"     # [char] Specify 'center' or 'upwind'\n")
        f.write('grid_size    '+str(N)+"     # [int] Choose number of elements in spatial domain'\n")
        f.write('x_min          '+str(xMin)+"     # [real] minimum value of domain\n")
        f.write('x_max          '+str(xMax)+"     # [real] maximum value of domain\n")
        f.write('threshold      '+str(threshold)+"     # [real] Threshold value for solution convergence\n")
        f.write('advection_speed      '+str(a)+"     # [real]  Speed of traveling wave\n")
        f.write('diffusion_constant     '+str(kappa)+"     # [real] the diffusion constant\n")
        f.write('cfl_constant   '+str(Ca)+"        # [real]  Constant for CFL condition\n")
        f.write('max_time       '+str(tmax)+"       # [real] maximum time, may be more than it takes to reach steady state")
        f.close()
    
    
def run_pde():
    # This one executes the Fortran excutable, "rootFinder.exe"
    # using "rootFinder.init" you just created.
    os.chdir('../PDE')
    os.system('./advection_diffusion.exe')
      

########################################################################################


def save_datFile(run_name):
    # popen command runs the terminal command and saves output
    # running os.system(command) will save a 0
    os.chdir('../PDE')
    if os.path.exists('./rootFinder_'+run_name.strip("'")+'.dat'):
        commandLine = os.popen('ls ./rootFinder_'+run_name+'.dat* | wc -l')
        numberOfDatFiles = commandLine.readline()
        commandLine.close()
    
        newFileName = 'rootFinder_'+run_name+'.dat.'+str(numberOfDatFiles).lstrip()
        renamingFile = 'mv ./rootFinder_'+run_name+'.dat ./'+newFileName
        os.system(renamingFile)


########################################################################################


def plot_data(N, simulationType, discretizationType, plotFilename, t):
    # 1. This function produces two figures:
    #     (1) solution (y-axis) vs. iteration number (x-axis), and
    #     (2) error (y-axis) vs. iteration number (x-axis).
    #
    # 2. You can plot the two as either subfigures or two separate figures.
    #
    # 3. In each figure, you need to have at least:
    #    xlabel, ylabel, title, line plot with reasonable choices of linestyle and marker.
    #    (see for instance, http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html)
    #
    # 4. Your plots need to have big enough x and y ranges so that your solution and error
    #    graphs are properly fit in the figures.
    #    Make sure that you use one same y-range for solutions and errors, respectively,
    #    so that ALL plots of three different threshold values have the same respective scales in y.
    #
    # 5. You need to plot your results to BOTH screen and png files.
    #    The png file names should bear information on ftn_type, threshold values at least, e.g.,
    #    the file name "result_2_1e-08.png" implies ftn_type = 2, threshold value = 1.e-8.
    #    Do not hardwire three different file names, but use string manipulations in naming them
    #    in your implementation.
    #
    # 6. After plotting, you save the data file "rootFinder_newton.dat"
    #    to a new name, e.g.., "rootFinder_newton.dat.1", etc..
    #    At the end of running three runs for three different threshold values,
    #    you should have collected "rootFinder_newton.dat.1", "rootFinder_newton.dat.2",
    #    as well as the latest data file "rootFinder_newton.dat".
    
    print os.getcwd()
    os.chdir('../PDE')    
    #plotFilename = 'output_'+str(t)+'.dat'
    
    
    
    print plotFilename
    
    figureFolder = './figures/'+simulationType.strip("'")+'_'+str(N)+'_'+discretizationType.strip("'")
    if not os.path.exists( figureFolder ):
        os.system('mkdir '+figureFolder)

    
    
    
    figure_name = figureFolder+'/result_'+simulationType.strip("'")+'_'+str(N)+'_'+discretizationType.strip("'")+'_'+str(t)+'.png'
    
    data = np.loadtxt('./results/'+plotFilename)
    fig = plt.figure()
    plt.plot(data[:,1],data[:,2],'o-')
    plt.ylabel('$u$')
    plt.grid(True)
    if (simulationType == "'diffusion'"):
        plt.ylim(0,100)
        plt.title('Diffusion PDE')
    elif (simulationType == "'advection'"):
        plt.title(discretizationType.strip("'").title()+' Advection PDE, Time = '+str(t))
        plt.ylim(-1,1)
    else:
        plt.title(discretizationType.strip("'").title()+' Advection-Diffusion PDE, Time = '+str(t))
        plt.ylim(-1,1)
        
    fig.savefig(figure_name)
    #
    # plt.subplot(212)
    # plt.plot(data[:,0],data[:,3])
    # plt.xlabel('Iteration')
    # plt.ylabel('Error')
    # plt.grid(True)
    # plt.show()
    # 
    #
    



def plot_data_g(N, simulationType, discretizationType, plotFilename, t):
    # 1. This function produces two figures:
    #     (1) solution (y-axis) vs. iteration number (x-axis), and
    #     (2) error (y-axis) vs. iteration number (x-axis).
    #
    # 2. You can plot the two as either subfigures or two separate figures.
    #
    # 3. In each figure, you need to have at least:
    #    xlabel, ylabel, title, line plot with reasonable choices of linestyle and marker.
    #    (see for instance, http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html)
    #
    # 4. Your plots need to have big enough x and y ranges so that your solution and error
    #    graphs are properly fit in the figures.
    #    Make sure that you use one same y-range for solutions and errors, respectively,
    #    so that ALL plots of three different threshold values have the same respective scales in y.
    #
    # 5. You need to plot your results to BOTH screen and png files.
    #    The png file names should bear information on ftn_type, threshold values at least, e.g.,
    #    the file name "result_2_1e-08.png" implies ftn_type = 2, threshold value = 1.e-8.
    #    Do not hardwire three different file names, but use string manipulations in naming them
    #    in your implementation.
    #
    # 6. After plotting, you save the data file "rootFinder_newton.dat"
    #    to a new name, e.g.., "rootFinder_newton.dat.1", etc..
    #    At the end of running three runs for three different threshold values,
    #    you should have collected "rootFinder_newton.dat.1", "rootFinder_newton.dat.2",
    #    as well as the latest data file "rootFinder_newton.dat".
    
    print os.getcwd()
    os.chdir('../PDE')    

    print plotFilename

    figure_name = './figures/plotsforh/result_'+simulationType.strip("'")+'_'+str(N)+'_'+discretizationType.strip("'")+'_'+str(t)+'.png'
    
    data = np.loadtxt('./results/'+plotFilename)
    fig = plt.figure()
    plt.plot(data[:,1],data[:,2],'o-')
    plt.ylabel('$u$')
    plt.grid(True)
    plt.title(discretizationType.strip("'").title()+' Advection PDE, Time = 1.0')
    plt.ylim(-1,1)
    plt.show()
    fig.savefig(figure_name)
    #
    # plt.subplot(212)
    # plt.plot(data[:,0],data[:,3])
    # plt.xlabel('Iteration')
    # plt.ylabel('Error')
    # plt.grid(True)
    # plt.show()
    # 
    #
   
   
def plot_data_h(N, simulationType, discretizationType, plotFilename, t):
  # 1. This function produces two figures:
  #     (1) solution (y-axis) vs. iteration number (x-axis), and
  #     (2) error (y-axis) vs. iteration number (x-axis).
  #
  # 2. You can plot the two as either subfigures or two separate figures.
  #
  # 3. In each figure, you need to have at least:
  #    xlabel, ylabel, title, line plot with reasonable choices of linestyle and marker.
  #    (see for instance, http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html)
  #
  # 4. Your plots need to have big enough x and y ranges so that your solution and error
  #    graphs are properly fit in the figures.
  #    Make sure that you use one same y-range for solutions and errors, respectively,
  #    so that ALL plots of three different threshold values have the same respective scales in y.
  #
  # 5. You need to plot your results to BOTH screen and png files.
  #    The png file names should bear information on ftn_type, threshold values at least, e.g.,
  #    the file name "result_2_1e-08.png" implies ftn_type = 2, threshold value = 1.e-8.
  #    Do not hardwire three different file names, but use string manipulations in naming them
  #    in your implementation.
  #
  # 6. After plotting, you save the data file "rootFinder_newton.dat"
  #    to a new name, e.g.., "rootFinder_newton.dat.1", etc..
  #    At the end of running three runs for three different threshold values,
  #    you should have collected "rootFinder_newton.dat.1", "rootFinder_newton.dat.2",
  #    as well as the latest data file "rootFinder_newton.dat".
    print os.getcwd()
    os.chdir('../PDE')    

    print plotFilename

    figure_name = './figures/plotsforh/result_'+simulationType.strip("'")+'_'+str(N)+'_'+discretizationType.strip("'")+'_'+str(t)+'.png'

    data = np.loadtxt('./results/'+plotFilename)
    fig = plt.figure()
    plt.plot(data[:,1],data[:,2],'o-')
    plt.ylabel('$u$')
    plt.grid(True)
    plt.title(discretizationType.strip("'").title()+' Advection-Diffusion PDE, Time = 1.0')
    plt.ylim(-1,1)
    plt.show()
    fig.savefig(figure_name)
  #
  # plt.subplot(212)
  # plt.plot(data[:,0],data[:,3])
  # plt.xlabel('Iteration')
  # plt.ylabel('Error')
  # plt.grid(True)
  # plt.show()
  # 



if __name__ == '__main__':
    
    # Defining the runtime parameters
    #simulationType     = "'diffusion'"
    simulationType     = "'advection_diffusion'"
    #simulationType     = "'advection'"
    #discretizationType = "'upwind'"
    discretizationType = "'center'"
    N = 32
    xMin = 0.0
    xMax = 1.0
    threshold = 1.e-4
    a = 1.0
    kappa = 1.156 #0.01
    Ca = 1.0
    tmax = 1.0
    
    # Creating filename list
    filenameList = []
    
    make_make()
    runtimeParameters_init(simulationType, discretizationType, N, xMin, xMax, threshold, a, kappa, Ca, tmax)
    run_pde()
    
    
    #

    # # Finding the filenames in directory
    for filename in os.listdir('../PDE/results'):
        filenameList.append(filename)


    print filenameList
    
    # # Plotting the files from directory
    for i in range(0,len(filenameList)):
        plot_data_h(N, simulationType, discretizationType, filenameList[i], i)



    # # Plotting the files from directory
    # for i in range(0,len(filenameList)):
    #     plot_data(N, simulationType, discretizationType, filenameList[i], i)

        # save_datFile(run_name)
        
    