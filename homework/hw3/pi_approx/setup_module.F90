module setup_module
 
#include "definition.h"
	
  use read_initFile_module
  implicit none

  real, save :: threshold
  integer, save :: maxIter
  character(len=MAX_STRING_LENGTH), save :: runName
  
contains

  subroutine setup_init()

    implicit none

    call read_initFileChar('pi_approx.init','run_name',runName)
    call read_initFileInt ('pi_approx.init', 'max_iter', maxIter)
    call read_initFileReal('pi_approx.init', 'threshold', threshold)
  end subroutine setup_init

  
end module setup_module