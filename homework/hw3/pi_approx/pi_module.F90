!!------------------------------------------------------------------
!! A Fortran example code for approximating pi
!! 
!! This code is written by Maritn Rodriguez for AMS 209 - Homework 3
!! It is based on the code provided by Prof. Dongwook Lee
!!
!! This module has three subroutines:
!! (1) nTerm         - computes the current term in the sums
!! (2) pi_summation  - This subroutine adds the current term to the sum
!! (3) pi_errorCheck - This checks if the convergence criteria has been met
!!
!!------------------------------------------------------------------

module pi_module
	
	use setup_module, only : threshold
	
contains
	
	!! This subroutine computes the nth term of the pi approximation sum
	subroutine nTerm(n,currentTerm)
		implicit none
		integer, intent(in) :: n
		real, intent(out) :: currentTerm
		
		currentTerm = (  4.0/(8.0*n+1.0) - 2.0/(8.0*n+4.0) - 1.0/(8.0*n+5.0) - 1.0/(8.0*n+6.0)  ) / 16.0**n
	end subroutine nTerm
	
	!! This subroutine adds the nth term of the sume to the current approximation
	subroutine pi_summation(currentTerm,piApprox)
		implicit none
		
		real, intent(in)  :: currentTerm
		real, intent(out) :: piApprox
		
		piApprox = piApprox + currentTerm
	end subroutine pi_summation
	
	
	!! This subroutine checks if the tolerance has been reached
	subroutine pi_errorCheck(pi_true, piApprox, error, done)
		
		implicit none
		real, intent(IN)  :: pi_true, piApprox
		real, intent(OUT) :: error
		integer, intent(OUT) :: done
		
		error = abs(pi_true - piApprox)
		if (error < threshold) then 
			done = 1
	    end if 
		
		
		
	end subroutine pi_errorCheck
	
	
end module pi_module