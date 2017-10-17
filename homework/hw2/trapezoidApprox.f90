! module trapezoidApprox includes two implementations,
! one in function and the other one in subroutine

module trapezoidApprox

contains


	! --------------------------!
	! [0] f                     !
	! --------------------------!
	
	real function f(x)
		implicit none
		
		real, intent(in) :: x
		f = x**2 + 1
		
	end function f
	
  ! -------------------------!
  ! [1] FUNCTION             !
  ! -------------------------!
  real function trapezoidFunc(a,b,N)
	  
	  implicit none
	  
	  ! -------------------------------------!
	  ! Input variables for trapezoidFunc()  !
	  ! -------------------------------------!
	  
	  real, intent(in) :: a, b
	  integer, intent(in) :: N
	  
	  real :: dx, sum
	  real, external :: f
	  
	  integer :: i
	  
	  dx = (b-a)/N
	  
	  sum = 0.0
	  do i = 1,N
		  sum = sum + ( f( (i-1)*dx ) + f(i*dx) )*dx/2.0 
	  end do
	  
	  
  end function trapezoidFunc


!   ! -------------------------!
!   ! [2] SUBROUTINE           !
!   ! -------------------------!
!   subroutine trapezoidSub(...)
!
!   end subroutine trapezoidSub
!
!

  ! -------------------------!
  ! [3] EXACT                !
  ! -------------------------!
  subroutine trapezoidExact(a,b,I)
	  implicit none
	  real, intent(in) :: a, b
	  real, intent(out) :: I
	  I = b**3.0/3.0 + b - (a**3.0/3.0 + a)

  end subroutine trapezoidExact

end module trapezoidApprox




! -------------------------!
! Driver routine           !
! -------------------------!
program compute_integration
	
	use trapezoidApprox
	
	implicit none
	real :: a, b, I_exact, I_sub
	real, external :: I_func
	integer :: N
	
	! Integral bounds and subdivisions
	a = 0
	b = 1
	N = 25
	
	
	call trapezoidExact(a, b, I)
    I_fun = trapezoidFunc(a, b, N)
	
	
	
	
	
    print*, "[1] Trapezoidal in function   =", I_func
    ! print*, "[2] Trapezoidal in subroutine =", trapezoidSub result
    print*, "[3] Exact integration         =", I
    ! print*, "[4] Error in function         =", trapezoidExact - trapezoidFunc result
    ! print*, "[5] Error in subroutine       =", trapezoidExact - trapezoidSub result

end program compute_integration