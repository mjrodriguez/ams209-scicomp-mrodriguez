program buggy_code_2
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
  real (kind = 8), allocatable :: x(:)

  n = 10
  !! DO NOT CHANGE BETWEEN LINE 25 AND LINE 29 ----
  
  allocate(x(n-1))
  print*, x(10)
  deallocate(x)



  
  !! DO NOT CHANGE BELOW THIS LINE ----------------
end program buggy_code_2