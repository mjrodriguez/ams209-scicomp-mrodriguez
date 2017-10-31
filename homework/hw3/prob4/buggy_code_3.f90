program buggy_code_3
  !!
  !! You are going to use this template to write:
  !! 
  !! 1. buggy_code_1.f90
  !!     (that has an issue with memory leak
  !!      whose buggy line number(s) is(are) detectable by Valgrind)
  !! 
  !! 2. buggy_code_2.f90
  !!     (that has an issue with uninitialization
  !!      whose buggy line number(s) is(are) detectable by Valgrind)
  !!
  !! 3. buggy_code_3.f90
  !!     (that has an issue with reading/writing memory errors after free'd
  !!      whose buggy line number(s) is(are) detectable by Valgrind)
  !!     
  !! 3. buggy_code_4.f90
  !!     (that has any potential issue(s)
  !!      whose buggy line number(s) is(are) NOT detectable by Valgrind)
  !!
  !! Make sure you use useful Fortran dubugging flags
  !! to compile your source code before running Valgrind.


  !! DO NOT CHANGE BETWEEN LINE 25 AND LINE 29 ----
  implicit none
  integer ( kind = 4 ) :: n
  real (kind = 8), allocatable :: x(:), y(:)
  

  n = 10
  !! DO NOT CHANGE BETWEEN LINE 25 AND LINE 29 ----
  
  
  allocate(x(n))
  	x(1) = 1; x(2) = 2; x(3) = 3; x(4) = 4; x(5) = 4;
  	x(6) = 6; x(7) = 7; x(8) = 8; x(9) = 9; x(10) = 10;
  deallocate(x)
  
  
  y = x



  
  !! DO NOT CHANGE BELOW THIS LINE ----------------
end program buggy_code_3