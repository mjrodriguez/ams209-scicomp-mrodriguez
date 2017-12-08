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
    
    doesExecutableExist = os.path.exists('../newton_rootFinder/rootFinder.exe')
    if not doesExecutableExist:
        os.chdir('../newton_rootFinder')
        makeIt = 'make'
        os.system(makeIt)
        os.system('rm rootFinder.init*')
        os.system('rm *.dat.*')
    else:
        os.chdir('../newton_rootFinder')
        makeCleanMake = 'make clean && make'
        os.system(makeCleanMake)
        os.system('rm rootFinder.init*')
        os.system('rm *.dat.*')
    
    # os.chdir('../pyRun/')
    
    
def runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold, ftn_type, init_guess, multiplicity):
    
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
    
    
    os.chdir('../newton_rootFinder')
    if os.path.exists('./rootFinder.init'):
        # popen command runs the terminal command and saves output
        # running os.system(command) will save a 0
        commandLine = os.popen('ls ./rootFinder.init* | wc -l')
        numberOfInitFiles = commandLine.readline()
        commandLine.close()
        
        newFileName = 'rootFinder.init.'+str(numberOfInitFiles).lstrip()
        renamingFile = 'mv ./rootFinder.init ./'+newFileName
        os.system(renamingFile)
        
        # Creating New File rootFinder.init
        f=open('rootFinder.init', 'w')
        f.write('run_name       '+run_name+"     # [char] Specify your output file name, e.g., 'rootFinder_[run_name].dat'\n")
        f.write('method_type    '+method_type+"     # [char] Choose a search method between 'newton' and 'modified_newton'\n")
        f.write('x_beg          '+str(x_beg)+"     # [real] Setting up the search domain\n")
        f.write('x_end          '+str(x_end)+"     # [real] Setting up the search domain\n")
        f.write('max_iter       '+str(max_iter)+"     # [int]  Maximum number of iteration\n")
        f.write('threshold      '+str(threshold)+"     # [real] Threshold value for solution convergence\n")
        f.write('ftn_type       '+str(ftn_type)+"     # [int]  Types of function -- either 1 or 2\n")
        f.write('init_guess     '+str(init_guess)+"     # [real] Initial guess for root search. Users are responsible to pick a good one.\n")
        f.write('multiplicity   '+str(multiplicity)+"        # [int]  The multiplicity of the root when using the modified newton method\n")
        f.close()
        
    else:
        # Creating New File rootFinder.init
        f=open('rootFinder.init', 'w')
        f.write('run_name       '+run_name+"     # [char] Specify your output file name, e.g., 'rootFinder_[run_name].dat'\n")
        f.write('method_type    '+method_type+"     # [char] Choose a search method between 'newton' and 'modified_newton'\n")
        f.write('x_beg          '+str(x_beg)+"     # [real] Setting up the search domain\n")
        f.write('x_end          '+str(x_end)+"     # [real] Setting up the search domain\n")
        f.write('max_iter       '+str(max_iter)+"     # [int]  Maximum number of iteration\n")
        f.write('threshold      '+str(threshold)+"     # [real] Threshold value for solution convergence\n")
        f.write('ftn_type       '+str(ftn_type)+"     # [int]  Types of function -- either 1 or 2\n")
        f.write('init_guess     '+str(init_guess)+"     # [real] Initial guess for root search. Users are responsible to pick a good one.\n")
        f.write('multiplicity   '+str(multiplicity)+"        # [int]  The multiplicity of the root when using the modified newton method\n")
        f.close()
    
    
def run_rootFinder():
    # This one executes the Fortran excutable, "rootFinder.exe"
    # using "rootFinder.init" you just created.
    os.chdir('../newton_rootFinder')
    os.system('./rootFinder.exe')
      

########################################################################################


def save_datFile(run_name):
    # popen command runs the terminal command and saves output
    # running os.system(command) will save a 0
    os.chdir('../newton_rootFinder')
    if os.path.exists('./rootFinder_'+run_name.strip("'")+'.dat'):
        commandLine = os.popen('ls ./rootFinder_'+run_name+'.dat* | wc -l')
        numberOfDatFiles = commandLine.readline()
        commandLine.close()
    
        newFileName = 'rootFinder_'+run_name+'.dat.'+str(numberOfDatFiles).lstrip()
        renamingFile = 'mv ./rootFinder_'+run_name+'.dat ./'+newFileName
        os.system(renamingFile)


########################################################################################


def plot_data(run_name, method_type, ftn_type, init_guess, threshold):
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
    
    
    os.chdir('../newton_rootFinder')
    plotFilename = 'rootFinder_'+run_name.strip("'")+'.dat'
    figure_name = 'result_'+str(ftn_type)+'_'+str(threshold)+'.png'
    
    data = np.loadtxt(plotFilename)
    fig = plt.figure()
    plt.subplot(211)
    plt.plot(data[:,0],data[:,1])
    plt.ylabel('$x_n$')
    plt.title('Convergence of Function '+str(ftn_type)+' Using '+str(method_type)+'\n $x_0$ = '+str(init_guess)+' , Threshold = '+str(threshold))
    plt.grid(True)
    
    plt.subplot(212)
    plt.plot(data[:,0],data[:,3])
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.grid(True)
    plt.show()
    fig.savefig(figure_name)
    
    
    
    







if __name__ == '__main__':
    
    # Setting the runtime parameters
    run_name     = "'newton'"
    method_type  = "'newton'"
    #method_type  = "'modified_newton'"
    x_beg        = -10.0
    x_end        = 10.0 
    max_iter     = 1000
    threshold    = [1.e-4, 1.e-6, 1.e-8]
    ftn_type     = 2
    init_guess   = 0.0001
    multiplicity = 2 
    
    
    make_make()
    for i in range(0,len(threshold)):
        runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold[i], ftn_type, init_guess, multiplicity)
        run_rootFinder()
        plot_data(run_name, method_type, ftn_type, init_guess, threshold[i])
        save_datFile(run_name)
        
    