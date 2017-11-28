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
    else:
        os.chdir('../newton_rootFinder')
        makeCleanMake = 'make clean && make'
        os.system(makeCleanMake)
    
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
    


if __name__ == '__main__':
    
    # Setting the runtime parameters
    run_name     = "'newton'"
    method_type  = "'newton'"
    x_beg        = -10.0
    x_end        = 10.0 
    max_iter     = 1000
    threshold    = [1.e-4, 1.e-6, 1.e-8]
    ftn_type     = 2
    init_guess   = 1.5
    multiplicity = 2
    
    
    make_make()
    for i in range(0,len(threshold)):
        runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold[i], ftn_type, init_guess, multiplicity)
        
        
    