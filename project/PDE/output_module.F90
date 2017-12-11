!!------------------------------------------------------------------
!! A Fortran example code for finding a root of a user-defined 
!! function f(x) = 0.
!! 
!! This code is written by Prof. Dongwook Lee for AMS 209.
!!
!! This module has one subroutine which writes an output 
!! to a file whose name is also defined by users.
!! Users can specify a custom file name, 'runName', in
!! rootFinder.init
!!
!!------------------------------------------------------------------

module output_module
	use pde_solver_module, only : frameTime
	implicit none

contains

  subroutine write_data(length,x,f,t)
    implicit none
    integer, intent(IN) :: length
    real, dimension(:), intent(IN) :: x,f
    integer :: i
	real, intent(IN)   :: t
    character(len=35)  :: ofile
	!! character(len=10)  :: frameTimeString
	character(len=10)  :: timeString
	
	
	!! Converting real to string
	!! write(frameTimeString,'(F5.2)')frameTime
	write(timeString,'(F5.2)')t

    !! File name for ascii output
    ofile = './results/output_'//trim(adjustl(timeString))//'.dat'

    !! File open
    open(unit=20,file=ofile,status='unknown')
    
    !! Write into a file:
    !!   iteration number, search result x, function value f(x), and residual
    do i=1,length
       write(20,920)i,x(i),f(i)
    end do

    !! Output format specifiers
920 format(1x, i5, f16.8, 1x, f16.8)
    
    !! File close
    close(20)

  end subroutine write_data
  
end module output_module
