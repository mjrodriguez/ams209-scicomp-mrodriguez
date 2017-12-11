!!------------------------------------------------------------------
!!
!! AMS 209 - Foundations of Scientific Computing
!! Project - Linear Advection-Diffusion PDE
!! Fall 2017
!! 
!! This code is (kinda) written by Martin Rodriguez. Based off
!! Dongwook's code.
!!
!! setup_module.F90
!!
!! This module has one subroutine which initialize your setup
!! by reading in runtime parameters from 'pde.init' file.
!! The setup_init subroutine calls read_initFile*** subroutines
!! that are implemented as subroutines in read_initFile_module. 
!!
!!------------------------------------------------------------------


module setup_module

  use read_initFile_module
  
  implicit none

  real, save :: xMin,xMax    !! Spatial Domain
  real, save :: threshold    !! L1(u_new,u_old) < threshold
  real, save :: a            !! Advection speed
  real, save :: kappa        !! Diffusion constant
  real, save :: Ca           !! CFL Constant
  real, save :: pi			 !! apple
  integer, save :: N         !! Grid size
  real, save :: tmax         !! maximum time, might be way more than it takes to reach steady state
  character(len=80), save :: simulationType, discretizationType
  
contains

  subroutine setup_init()

    implicit none

    call read_initFileChar('pde.init','simulation_type',simulationType)
    call read_initFileChar('pde.init','discretization_type', discretizationType)
	call read_initFileInt('pde.init','grid_size', N)
    call read_initFileReal('pde.init', 'x_min', xMin)
    call read_initFileReal('pde.init', 'x_max', xMax)
    call read_initFileReal('pde.init', 'threshold', threshold)
    call read_initFileReal('pde.init', 'advection_speed', a)
	call read_initFileReal('pde.init', 'diffusion_constant', kappa)
	call read_initFileReal('pde.init', 'cfl_constant', Ca)
	call read_initFileReal('pde.init', 'max_time', tmax)
	
	pi = acos(-1.d0)
	 
	print*, tmax
	
	
!
! 	print*, '--------------------------------------------'
! 	print*, '- PRINTING VARIABLES                       -'
! 	print*, 'simulation_type     = ', simulationType
! 	print*, 'discretization_type = ', discretizationType
! 	print*, 'grid_size           = ', N
! 	print*, 'x_min               = ', xMin
! 	print*, 'x_max               = ', xMax
! 	print*, 'threshold           = ', threshold
! 	print*, 'advection_speed     = ', a
! 	print*, 'diffusion_constant  = ', kappa
! 	print*, 'cfl_constant        = ', Ca
! 	print*, '-----------------------------------------------'
!
!
	 
	
    
  end subroutine setup_init

  
end module setup_module
