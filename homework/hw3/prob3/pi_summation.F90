!!--------------------------------------------------
!! pi_summation.F90 Code
!! This code sums the terms in the series
!!--------------------------------------------------

module pi_summation
	
contains
	
	!! This subroutine computes the nth term of the pi approximation sum
	subroutine nTerm(n,currentTerm)
		implicit none
		integer, intent(in) :: n
		real, intent(out) :: currentTerm
		
		currentTerm = 16**(-n)*( 4/(8*n+1) - 2/(8*n+4) - 1/(8*n+5) - 1/(8*n+6) )
	end subroutine nTerm
	
	!! This subroutine adds the nth term of the sume to the current approximation
	subroutine piSummation(currentTerm,piApprox)
		implicit none
		
		real, intent(in)  :: currentTerm
		real, intent(out) :: piApprox
		
		piApprox = piApprox + currentTerm
		
	end subroutine piSummation

	
end module pi_summation
