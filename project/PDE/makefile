########################################################################################
#                       Makefile for advection_diffusion code
#                Written by Prof. Dongwook Lee, AMS 209, UCSC
#				 Modified by Martine Rodriguez, AMS 209 Project
########################################################################################

FC	= gfortran

FFLAGS_DEBUG = -Wall -Wextra -Wimplicit-interface -fPIC -fmax-errors=1 -g -fcheck=all -fbacktrace

FFLAGS_OPT = -ggdb -O3 -fdefault-real-8 -fdefault-double-8 -ffree-line-length-none -Wuninitialized

EXE_FILE = advection_diffusion.exe

OBJS  = advection_diffusion.o \
	read_initFile_module.o\
	initialize_module.o  \
	setup_module.o \
	pde_solver_module.o\
	output_module.o

.PHONY: clean
########################################################################################
#COMPILING AND LINKING USING GENERIC SUFFIX RULE FOR F90

$(EXE_FILE) : $(OBJS)
	@$(FC) $(FFLAGS_OPT) $(OBJS) -o $(EXE_FILE)
	@echo "code is now linking..."

#LET'S APPLY GENERIC SUFFIX RULE HERE FOR FORTRAN 90

# method 1 using generic suffix rule
#.SUFFIXES: 
#.SUFFIXES: .F90 .o
#.F90.o:
#	$(FC) $(FFLAGS_OPT) -c $<

# method 2 using inference rule
%.o: %.F90
	$(FC) $(FFLAGS_OPT) -c $<

#######################################################################################
#SOME USEFUL COMMANDS
clean:
	@rm -f *.o *.mod *~ advection_diffusion.exe *.dat

# debug: clean
debug: FFLAGS_OPT = $(FFLAGS_DEBUG)
debug: $(EXE_FILE)

#######################################################################################
#LET'S DEFINE SOME MODULE DEPENDENCIES!
advection_diffusion.o: setup_module.o initialize_module.o pde_solver_module.o output_module.o

setup_module.o : read_initFile_module.o

initialize_module.o : setup_module.o

pde_solver_module.o : setup_module.o initialize_module.o

output_module.o : pde_solver_module.o

#######################################################################################
