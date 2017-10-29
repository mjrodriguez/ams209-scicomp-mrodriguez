# Gnuplot script file for plotting data in file f(x) = (x-1)*(x-2)
# This file is called   problem2_3.p

set terminal postscript
set output "problem2_3.ps"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set title "f(x) = (x-1)*(x-2)" 
set xlabel "x"
set ylabel "y"
set xrange [0:3]
plot (x-1.0)*(x-2.0), \
	"root.dat" using 1:2 title 'Roots' with points pointtype 16, \
	"initGuess.dat" using 1:2 title 'Initial Guess' with points pointtype 2
	
