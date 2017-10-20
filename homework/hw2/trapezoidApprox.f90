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
	  
	  ! -------------------------------------!
	  ! Grid variables                       !
	  ! -------------------------------------!
	  real :: dx, xk, xkm1, fk, fkm1
	  integer :: i
	  dx = (b-a)/N   ! Grid spacing
	  
	  ! -----------------------------------!
	  ! INTEGRATION LOOP                   !
	  ! -----------------------------------!
	  trapezoidFunc = 0.0
	  do i = 1,N
		  ! computing xk minus 1 and xk
		  xkm1 = a + (i-1)*dx
		  xk = a + i*dx
		  
		  ! computing fk minus 1 and fk
		  fkm1 = f(xkm1)
		  fk = f(xk)
		  
		  trapezoidFunc = trapezoidFunc + ( fkm1 + fk )*dx/2.0 
	  end do
	  
  end function trapezoidFunc


  ! -------------------------!
  ! [2] SUBROUTINE           !
  ! -------------------------!
  subroutine trapezoidSub(a,b,N,I_sub)
	  implicit none
	  
	  ! -------------------------------------!
	  ! Input variables for trapezoidFunc()  !
	  ! -------------------------------------!
	  real, intent(in) :: a, b
	  integer, intent(in) :: N
	  real, intent(out) :: I_sub
	  
	  ! -------------------------------------!
	  ! Grid variables                       !
	  ! -------------------------------------!
	  real :: dx, xk, xkm1, fk, fkm1
	  integer :: i
	  dx = (b-a)/N     ! Grid spacing
	  
	  ! -----------------------------------!
	  ! INTEGRATION LOOP                   !
	  ! -----------------------------------!
	  I_sub = 0.0
	  do i = 1,N
		  ! computing xk minus 1 and xk
		  xkm1 = a + (i-1)*dx
		  xk = a + i*dx
		  
		  ! computing fk minus 1 and fk
		  fkm1 = f(xkm1)
		  fk = f(xk)
		  
		  I_sub = I_sub + ( fkm1 + fk )*dx/2.0 
	  end do
	  
  end subroutine trapezoidSub



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
	real :: a, b, I_exact, I_sub, I_func
	integer :: N
	
	! Integral bounds and subdivisions
	a = 0
	b = 1
	N = 400
	
	
	call trapezoidExact(a, b, I_exact)
    I_func = trapezoidFunc(a, b, N)
	call trapezoidSub(a, b, N, I_sub)
	
	print*, "[0] Number of Elements        =", N
    print*, "[1] Trapezoidal in function   =", I_func
    print*, "[2] Trapezoidal in subroutine =", I_sub
    print*, "[3] Exact integration         =", I_exact
    print*, "[4] Error in function         =", abs(I_exact - I_func)
    print*, "[5] Error in subroutine       =", abs(I_exact - I_sub)

end program compute_integration