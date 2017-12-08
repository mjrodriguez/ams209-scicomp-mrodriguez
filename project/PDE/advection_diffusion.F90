!!------------------------------------------------------------------
!!
!! AMS 209 - Foundations of Scientific Computing
!! Project - Linear Advection-Diffusion PDE
!! Fall 2017
!! 
!! Written by Martin Rodriguez
!!
!! advection_diffusion.F90
!!
!! This is the main driver of the simulation.
!!
!!------------------------------------------------------------------- 

program advection_diffusion
	
	!! Delaring modules that will be used in this driver
	use setup_module,        only : xMin, xMax, tmax, N, threshold, a, kappa, Ca, simulationType, discretizationType, setup_init
	use initialize_module,   only : initialize_simulation, grid_init, advect_init, diffuse_init
	use pde_solver_module,   only : dt, error, cfl, bc, diffuse_update, advect_update, check_error
	
	implicit none
	
	!! Initializing Variables
	real, allocatable, dimension(:) :: x, uold, unew
	real :: t
	
	
	!! Setting up runtime parameters
	call setup_init()
	
	!! allocating memory for x, uold, and unew
	allocate(   x(N+2))
	allocate(uold(N+2))
	allocate(unew(N+2))
	
	
	!! Initializing grid and initial conditions
	call initialize_simulation(x, uold)
	
	!! Compute time step and initialize time
	call cfl()
	t = 0.0
	
	!! PDE SOLVER LOOP for tmax
	do while (t < tmax)
		
		!! Note: Boundary Conditions are updated inside the update subroutines
		if (simulationType == 'diffusion') then
			call diffuse_update(uold, unew)
			
			!! Check error
			call check_error(uold, unew)
			if (error < threshold) then
				print*, '#----------------------------------------#'
				print*, '# Final Time = ', t 
				print*, '#----------------------------------------#'         
				exit
			end if
		elseif(simulationType == 'advection') then
			call advect_update(uold, unew)
		elseif (simulationType == 'advection_diffusion') then
			call advect_update(uold, unew)
			call diffuse_update(unew, unew)
		end if
		
		
		
		!! update time
		t = t+dt
		
		!! Update u
		uold = unew
		
	end do
	
	
	
	
	
	
	deallocate(   x)
	deallocate(uold)
	deallocate(unew)
	
end program advection_diffusion