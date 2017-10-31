# Gnuplot script file for plotting data in file 
# This file is called   problem2_3.p

set terminal postscript
set output "pi_value.ps"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set title "Values of Pi" 
set xlabel "N"
set ylabel "PI Approximation"
plot "pi_approx_test.dat" using 1:2 title 'Approximate Pi - Value' with linespoints

set terminal postscript
set output "error.ps"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set title "Error in Pi Approximation" 
set xlabel "N"
set ylabel "Error"
plot "pi_approx_test.dat" using 1:3 title 'Approximate Pi - Error' with linespoints
	
