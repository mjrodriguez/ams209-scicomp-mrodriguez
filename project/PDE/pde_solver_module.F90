!!------------------------------------------------------------------
!!
!! AMS 209 - Foundations of Scientific Computing
!! Project - Linear Advection-Diffusion PDE
!! Fall 2017
!! 
!! This code is (for sure) written by Martin Rodriguez.
!!
!! pde_solver_module.F90
!!
!! This module contains all the contains all the components to solve 
!! the PDE.
!! 		-- diffusion_update
!!		-- advect_update
!!		-- cfl
!!		-- bc (boundary condition)
!!		-- check_error
!!
!!------------------------------------------------------------------

module pde_solver_module
	
	use setup_module,      only : N, kappa, a, Ca, tmax, simulationType, discretizationType
	use initialize_module, only : dx
	
	implicit none
	
	real, save :: dt
	real, save :: error
	real, save :: frameTime
	
contains
	
	!!---------------------------------------------------------!!
	!! CFL CONDITION                                           !!
	!!---------------------------------------------------------!!
	
	subroutine cfl()
		if (simulationType == 'diffusion') then
			dt = Ca*dx**2/(2*kappa)
		elseif (simulationType == 'advection') then
			dt = Ca*dx/abs(a)
		elseif (simulationType == 'advection_diffusion') then
			dt = Ca*min(dx/abs(a),dx**2/(2*kappa))	
		end if
		frameTime = 0.0
	end subroutine cfl
	
	
	
	!!---------------------------------------------------------!!
	!! COMPUTE TIME STEP                                       !!
	!!---------------------------------------------------------!!	
	!! We compute the frameTime at which we need to pull data
	!! from. If the t+dt is larger then frameTime then we
	!! make dt = frameTime - t and switch the write logical
	!! to TRUE. Then it writes after.
	!!---------------------------------------------------------!!
	subroutine compute_time_step(t, frameNumber, writeOutput)
		real, intent(in)       :: t
		integer, intent(inout) :: frameNumber
		logical, intent(inout) :: writeOutput

		call cfl()
		frameTime = frameNumber*tmax/10.0
		if ( dt > frameTime - t ) then
			dt = frameTime - t
			writeOutput = .TRUE.
			frameNumber = frameNumber + 1
		end if
		
	end subroutine compute_time_step
	
	
	
	
	!!---------------------------------------------------------!!
	!! SET BOUNDARY CONDITIONS                                 !!
	!!---------------------------------------------------------!!
	subroutine bc(unew)
		real, dimension(:), intent(out) :: unew
		if (simulationType == 'diffusion') then
			unew(1)   = 0
			unew(N+2) = 100
		elseif (simulationType == 'advection' .or. simulationType == 'advection_diffusion') then
			unew(1) = unew(N+1)
			unew(N+2) = unew(2)
		end if
	end subroutine bc
	
	
	
	!!---------------------------------------------------------!!
	!! DIFFUSION UPDATE                                        !!
	!!---------------------------------------------------------!!
	subroutine diffuse_update(uold, unew)
		integer :: i
		real, dimension(:), intent(in)  :: uold
		real, dimension(:), intent(out) :: unew
		
		!! Compute nodes in between
		do i = 2,N+1
			unew(i) = uold(i) + kappa*dt*(uold(i+1) - 2*uold(i) + uold(i-1))/dx**2
		end do
		!! update Boundary conditions
		call bc(unew)
		
	end subroutine diffuse_update
	
	!!---------------------------------------------------------!!
	!! ADVECTION UPDATE                                        !!
	!!---------------------------------------------------------!!
	subroutine advect_update(uold, unew)
		real, dimension(:), intent(in)  :: uold
		real, dimension(:), intent(out) :: unew
		integer :: i
		
		!! Compute values of unew in inner nodes using either upwind or center difference
		if (discretizationType == 'upwind') then
			do i = 2,N+1
				unew(i) = uold(i) - a*dt*(uold(i) - uold(i-1))/dx
			end do
		elseif (discretizationType == 'center') then
			do i = 2,N+1
				unew(i) = uold(i) - a*dt*(uold(i+1) - uold(i-1))/(2*dx)	
			end do
		end if
		
		!! update boundary conditions
		call bc(unew)
	end subroutine advect_update
	
	!!---------------------------------------------------------!!
	!! CHECK_ERROR                                             !!
	!!---------------------------------------------------------!!
	subroutine check_error(uold,unew)
		real, dimension(:), intent(in)  :: uold
		real, dimension(:), intent(in) :: unew
		integer :: i
		! Initializing error
		error = 0.0
		
		! Computing error with the L1 metric
		do i = 2,N+1
			error = error + dx*abs(unew(i) - uold(i))
		end do
				
	end subroutine check_error
	
end module pde_solver_module