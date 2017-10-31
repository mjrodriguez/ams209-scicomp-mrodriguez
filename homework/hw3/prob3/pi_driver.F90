!!------------------------------------------
!! MODULAR PI APPROXIMATION
!! Martin Rodriguez
!! AMS 209 - Fall 2017
!! 
!! This is the driver file
!!------------------------------------------

program pi_approx
	
    !! include a C-type header file:
    !! this is why the file extensions are .F90, instead of .f90
  	!#include "definition.h"
	
	
    !! Begining of the real implementation of the driver
    !! define usages of module variables and subroutines 
	use setup_module,    only : setup_init, maxIter, threshold, runName
	use pi_module,       only : nTerm, pi_summation, pi_errorCheck
	use output_module,   only : output_write
	
	implicit none
	
    !! These are local variables whose scopes are within pi_driver.F90
    integer :: nIter, done
    real    :: error, piApprox, pi_true, newTerm
	
    !! Define allocatable arrays
    real, allocatable, dimension(:) :: pi_history,error_history
	
	!! Initializing Local Variables
	pi_true = acos(-1.d0)
	error = 1.0
	piApprox = 0.
	newTerm =0.0
	done = 0
	
    !! Call setup_init to initialize the runtime parameters
    call setup_init()
	
	!! allocate arrays with size of a user-defined integer value, maxIter
    allocate(   pi_history(maxIter))
    allocate(error_history(maxIter))
	
	!! This is the loop where the nth terms get computed and sum
	do nIter = 0, maxIter 
		
		
		call nTerm(nIter,newTerm)
		
		!! feeds current nth term pi sum and returns the total sum up to that nth term
		call pi_summation(newTerm, piApprox) 
		call pi_errorCheck(pi_true, piApprox, error, done)
		
		pi_history(nIter)    = piApprox
		error_history(nIter) = error
		
		if (done == 1) then
			print*, 'PI = ', piApprox
			call output_write(nIter, pi_history, error_history)
			EXIT
		end if
		
	end do
	
	
	!! Deallocate arrays with size of a user-defined integer value, maxIter
    deallocate(    pi_history )
    deallocate( error_history )
	
	
	
end program pi_approx