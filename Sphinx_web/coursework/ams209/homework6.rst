AMS 209 - Homework 6: Connecting Python and Fortran
======================================================

For the most part we have focused on writing code this quarter that solves a problem. However, at times we must test the code with different inputs. Rather than running each individual test case separately, we can create a python script that creates different files for the inputs, compiles, executes code and plots results. Therefore not requiring the user to start the runs for all cases and returning once everything is done. Click `here <https://users.soe.ucsc.edu/~dongwook/wp-content/uploads/2017/ams209/lectureNote/_build/html/hw/hw6/hw6.html>`_.

############################
Python Code
############################ 

This is the Python code that drives the different test cases for Newton's method. The Fortran code for Newton's method was written by Professor Dongwook Lee and can be `seen here <https://users.soe.ucsc.edu/~dongwook/wp-content/uploads/2017/ams209/lectureNote/_build/html/chapters/chapt02/ch02_fortran_example.html#ch02-fortran-example>`_. The report for this project can be downloaded: :download:`hw6_report.pdf <./hw6/hw6_report.pdf>`.




.. literalinclude:: ./hw6/pyRun/pyRun_rootFinder.py
					:language: python
					:linenos:


