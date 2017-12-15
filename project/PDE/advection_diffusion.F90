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
	use pde_solver_module,   only : dt, error, cfl, compute_time_step, bc, diffuse_update, advect_update, check_error
	use output_module,       only : write_data
	
	implicit none
	
	!! Initializing Variables
	real, allocatable, dimension(:) :: x, uold, unew
	real    :: t
	integer :: frameNumber
	logical :: writeOutput, runningOutTheClock
	
	!! Setting up runtime parameters
	call setup_init()
	
	!! allocating memory for x, uold, and unew
	allocate(   x(N+2))
	allocate(uold(N+2))
	allocate(unew(N+2))
	
	
	!! Initializing grid and initial conditions
	call initialize_simulation(x, uold)
	
	!! Initialize time and local variables
	t = 0.0
	writeOutput = .TRUE.
	runningOutTheClock = .FALSE.
	frameNumber = 1
	call cfl()
	
	
	print*, 'current time = ',t
	print*, 'maximum time = ', tmax
	
	
	
	!! PDE SOLVER LOOP for tmax
	do while (t < tmax)
		
		!! Write output if it is true, it is inialized as true.
		if (writeOutput) then
			call write_data(N+2, x, uold, t)
			writeOutput = .false.
			print*, 'Writing data, Frame Number = ', frameNumber
		end if
		
		!! In compute time step we compute the time step switch writOutput logical
		if (t > 1.e-4) then
			call compute_time_step(t, frameNumber, writeOutput)
		end if

		!! Note: Boundary Conditions are updated inside the update subroutines
		if (simulationType == 'diffusion') then
			call diffuse_update(uold, unew)
			
			!! Check error
			call check_error(uold, unew)
			if (error < threshold .AND. .NOT. runningOutTheClock) then
				print*, '#----------------------------------------#'
				print*, '# Final Time = ', t 
				print*, '#----------------------------------------#'
				!! Writing the last unew
				call write_data(N+2, x, unew, t)
				exit
				!! runningOutTheClock = .False.
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
	
	!! Just making usre the last unew is written
	if (simulationType == 'advection' .or. simulationType == 'advection_diffusion') then
		call write_data(N+2, x, unew, t)
	end if
	
	
	
	
	deallocate(   x)
	deallocate(uold)
	deallocate(unew)
	
end program advection_diffusion