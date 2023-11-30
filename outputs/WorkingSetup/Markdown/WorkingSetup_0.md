
<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"1WorkingSetup-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>650</f>        |
| <c>batch_size</c> | <d>int</d>        | <f>80</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |
| <c>param</c>      | <d>int</d>        | <f>1</f>          |
| <c>path</c>       | <d>str</d>        | <j>"/zhome/59/9/198225/Desktop/Deep_learning_2023/models/"</j> |

# Output

```
Traceback (most recent call last):
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 98, in <module>
    Defaults.start()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 47, in run
    if not exists(folder): mkdir(folder)
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/1WorkingSetup/1WorkingSetup-0/'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19629902: <WorkingSetup_0> in cluster <dcc> Exited

Job <WorkingSetup_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 11:34:38 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Thu Nov 30 13:23:37 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Thu Nov 30 13:23:37 2023
Terminated at Thu Nov 30 13:26:16 2023
Results reported at Thu Nov 30 13:26:16 2023

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   8.39 sec.
    Max Memory :                                 264 MB
    Average Memory :                             212.75 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65272.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   159 sec.
    Turnaround time :                            6698 sec.

The output (if any) is above this job summary.


<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"2WorkingSetup-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>650</f>        |
| <c>batch_size</c> | <d>int</d>        | <f>80</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |
| <c>param</c>      | <d>int</d>        | <f>2</f>          |
| <c>path</c>       | <d>str</d>        | <j>"/zhome/59/9/198225/Desktop/Deep_learning_2023/models/"</j> |

# Output

```
Traceback (most recent call last):
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 98, in <module>
    Defaults.start()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 47, in run
    if not exists(folder): mkdir(folder)
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/2WorkingSetup/2WorkingSetup-0/'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19629903: <WorkingSetup_0> in cluster <dcc> Exited

Job <WorkingSetup_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 11:34:39 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Thu Nov 30 13:29:54 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Thu Nov 30 13:29:54 2023
Terminated at Thu Nov 30 13:30:09 2023
Results reported at Thu Nov 30 13:30:09 2023

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   5.82 sec.
    Max Memory :                                 267 MB
    Average Memory :                             267.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65269.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   17 sec.
    Turnaround time :                            6930 sec.

The output (if any) is above this job summary.


<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"3WorkingSetup-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>650</f>        |
| <c>batch_size</c> | <d>int</d>        | <f>80</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |
| <c>param</c>      | <d>int</d>        | <f>3</f>          |
| <c>path</c>       | <d>str</d>        | <j>"/zhome/59/9/198225/Desktop/Deep_learning_2023/models/"</j> |

# Output

```
Traceback (most recent call last):
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 98, in <module>
    Defaults.start()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 47, in run
    if not exists(folder): mkdir(folder)
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/3WorkingSetup/3WorkingSetup-0/'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19629904: <WorkingSetup_0> in cluster <dcc> Exited

Job <WorkingSetup_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 11:34:39 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Thu Nov 30 13:30:10 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Thu Nov 30 13:30:10 2023
Terminated at Thu Nov 30 13:30:25 2023
Results reported at Thu Nov 30 13:30:25 2023

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   6.04 sec.
    Max Memory :                                 266 MB
    Average Memory :                             266.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65270.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   16 sec.
    Turnaround time :                            6946 sec.

The output (if any) is above this job summary.


<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"4WorkingSetup-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>650</f>        |
| <c>batch_size</c> | <d>int</d>        | <f>80</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |
| <c>param</c>      | <d>int</d>        | <f>4</f>          |
| <c>path</c>       | <d>str</d>        | <j>"/zhome/59/9/198225/Desktop/Deep_learning_2023/models/"</j> |

# Output

```
Traceback (most recent call last):
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 98, in <module>
    Defaults.start()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 47, in run
    if not exists(folder): mkdir(folder)
FileNotFoundError: [Errno 2] No such file or directory: 'outputs/4WorkingSetup/4WorkingSetup-0/'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19629905: <WorkingSetup_0> in cluster <dcc> Exited

Job <WorkingSetup_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 11:34:39 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Thu Nov 30 13:30:27 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Thu Nov 30 13:30:27 2023
Terminated at Thu Nov 30 13:30:42 2023
Results reported at Thu Nov 30 13:30:42 2023

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   5.90 sec.
    Max Memory :                                 264 MB
    Average Memory :                             264.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65272.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   17 sec.
    Turnaround time :                            6963 sec.

The output (if any) is above this job summary.

