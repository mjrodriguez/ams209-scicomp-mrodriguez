module pi_errorCheck
	
	 use setup_module, only : threshold
	
contains
	
	subroutine errorCheck(pi_true, piApprox, error, done)
		
		implicit none
		real, intent(IN)  :: pi_true, piApprox
		real, intent(OUT) :: error
		integer, intent(OUT) :: done
		
		error = abs(pi_true - piApprox)
		if (error < threshold) then 
			done = 1
	    end if 
		
		
		
	end subroutine errorCheck
	
	
	
	
end module pi_errorCheck