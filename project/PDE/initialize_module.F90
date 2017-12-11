!!------------------------------------------------------------------
!!
!! AMS 209 - Foundations of Scientific Computing
!! Project - Linear Advection-Diffusion PDE
!! Fall 2017
!! 
!! This code is (for sure) written by Martin Rodriguez.
!!
!! initialize_module.F90
!!
!! This module has one subroutine which initializes the grid, 
!! diffusion initial condition, and advection initial condition 
!!
!!------------------------------------------------------------------



module initialize_module
	

	use setup_module,  only : xMin, xMax, N, pi, simulationType
	
	implicit none
	
	real, save :: dx
	
contains

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	subroutine grid_init(x)
		
		integer :: i 
		real, dimension(:), intent(out) :: x
		!! Computing grid spacing
		dx = (xmax - xMin)/N
		
		!! Initializing spatial Grid
		x(1) = -dx/2.0
		do i=2,N+1
			x(i) = xMin + ((i-1)-0.5)*dx
		end do
		x(N+2) = ( N + 0.5 )*dx
		
	end subroutine grid_init
	
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	subroutine diffuse_init(uold)
		
		integer :: i
		real, dimension(:), intent(out) :: uold
		
		!! setting the initial condition for diffusion equation
		do i=1,N+1
			uold(i) = 0
		end do
		uold(N+2) = 100
		
		
	end subroutine diffuse_init
	
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
	subroutine advect_init(x, uold)
		
		real, dimension(:), intent(in)  :: x
		real, dimension(:), intent(out) :: uold
		integer :: i
		
		do i=1,N+2
			uold(i) = sin(2*pi*x(i))
		end do
	end subroutine advect_init
	
	
	
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!	
	
	
	
	
	subroutine initialize_simulation(x, uold)
		
		real, dimension(:), intent(out) :: x
		real, dimension(:), intent(out) :: uold
		
		call grid_init(x)
		if (simulationType == 'diffusion') then
			call diffuse_init(uold)
		elseif (simulationType == 'advection' .or. simulationType == 'advection_diffusion') then
			call advect_init(x, uold)
		end if
				
		
	end subroutine initialize_simulation
	
end module initialize_module