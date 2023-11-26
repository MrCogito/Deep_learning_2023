python: can't open file '/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py': [Errno 2] No such file or directory

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19545289: <NewGPUfix_0> in cluster <dcc> Exited

Job <NewGPUfix_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Sat Nov 25 15:17:36 2023
Job was executed on host(s) <4*n-62-18-10>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Sat Nov 25 19:45:34 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Sat Nov 25 19:45:34 2023
Terminated at Sat Nov 25 19:45:37 2023
Results reported at Sat Nov 25 19:45:37 2023

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpua100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu80gb]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 2.

Resource usage summary:

    CPU time :                                   0.66 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   4 sec.
    Turnaround time :                            16081 sec.

The output (if any) is above this job summary.

