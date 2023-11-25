wandb: Currently logged in as: chessproject65. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231124_143910-1dm6u6x4
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Test_new-0
wandb: ⭐️ View project at https://wandb.ai/chessproject65/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/chessproject65/deeplearning_painn/runs/1dm6u6x4

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19531216: <Test_new_0> in cluster <dcc> Exited

Job <Test_new_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Fri Nov 24 13:56:40 2023
Job was executed on host(s) <4*n-62-18-13>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Fri Nov 24 14:38:33 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Fri Nov 24 14:38:33 2023
Terminated at Sat Nov 25 00:26:39 2023
Results reported at Sat Nov 25 00:26:39 2023

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

TERM_OWNER: job killed by owner.
Exited with exit code 143.

Resource usage summary:

    CPU time :                                   35633.00 sec.
    Max Memory :                                 1831 MB
    Average Memory :                             1716.69 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63705.00 MB
    Max Swap :                                   2 MB
    Max Processes :                              6
    Max Threads :                                35
    Run time :                                   35287 sec.
    Turnaround time :                            37799 sec.

The output (if any) is above this job summary.

