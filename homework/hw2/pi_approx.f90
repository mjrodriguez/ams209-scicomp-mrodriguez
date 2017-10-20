! /hw2/ams209_hw2_prob2.f90

! Martin Rodriguez
! ID: 1151332
! AMS 209
! Fall 2017

!----------------------------------------------
!
! APROXIMATING PI
!
!---------------------------------------------




program approxpi

  implicit none
  integer :: n,nmax
  real :: threshold, diff, pi_appx, pi_true 
  

  nmax = 1000
  pi_true = acos(-1.d0)
  pi_appx = 0. ! Initializing the pi approximation
  threshold = 1.e-16
  
 
  do n = 0,nmax
     
     pi_appx = pi_appx +  (  4.0/(8.0*n+1.0) - 2.0/(8.0*n+4.0) - 1.0/(8.0*n+5.0) - 1.0/(8.0*n+6.0)  ) / 16.0**n 
     diff = abs(pi_appx - pi_true)
     
     if (diff < threshold) then
		print *, "Difference abs(pi_true - pi_appx) = ", diff
        print *, "Number of N = ", n
        EXIT
     end if
  end do


end program approxpi

