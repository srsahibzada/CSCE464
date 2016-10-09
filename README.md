1. Generate the config files.
  -In any server (or even on your machine) download seedfile.txt and filemaker.py.
   Run filemaker.py as : python filemaker.py
   Copy these config files to lens-comp5.
  2. Perform the glomosim install and copy the config files to ~/glomosim-2.03/glomosim/bin.
  3. ./runner.sh to create the output directory (this is the one that will have your glomo.stat files).
    -If runner.sh gives you permission problems, type chmod u+x runner.sh .
    -You should now have an output directory.
  4. In the output directory, save the out2.sh script. Run as follows: ./out2.sh
    -If you get a permission error, type chmod u+x out2.sh
  5. You should now have a directory called delays with all of the end-to-end delays. Copy these
      back to your local machine or your chosen server (copy the whole directory to make it easier).
  6. Wherever you have copied these files, run averager.py. This should ask you for 
    your directory name, preventing naming conflicts. Pipe the output to a text file 
    called avgs.txt.
  7. [OPTIONAL] You can sift through these by hand to separate them since there aren't
  that many, but if you prefer, you can sort them by running run.sh after downloading fff1.py.
  This has the disadvantage that you have to type 
  
  These scripts aren't well-named-- sorry!
