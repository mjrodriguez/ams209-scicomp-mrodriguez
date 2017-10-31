!!------------------------------------------------------------------
!! A Fortran example code for finding a root of a user-defined 
!! function f(x) = 0.
!! 
!! This code is written by Prof. Dongwook Lee for AMS 209.
!! Modified by Martin Rodriguez for AMS 209 - Homework 3
!! To be used in pi_driver.F90
!!
!! This module has one subroutine which writes an output 
!! to a file whose name is also defined by users.
!! Users can specify a custom file name, 'runName', in
!! pi_approx.init
!!
!!------------------------------------------------------------------

module output_module

  use setup_module, only : runName
  implicit none

contains

  subroutine output_write(length,pi,error)
    implicit none
    integer, intent(IN) :: length
    real, dimension(:), intent(IN) :: pi,error
	
	
	
	
    integer :: i
    character(len=35) :: ofile

    !! File name for ascii output
    ofile = 'pi_approx_'//trim(runName)//'.dat'

    !! File open
    open(unit=20,file=ofile,status='unknown')
    
    !! Write into a file:
    !!   iteration number, search result x, function value f(x), and residual
    do i=0,length-1
       write(20,920)i,pi(i),error(i)
    end do

    !! Output format specifiers
920 format(1x, i5, 1x, f16.8, 1x, f16.12)
    
    !! File close
    close(20)

  end subroutine output_write
  
end module output_module
