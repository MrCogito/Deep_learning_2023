
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
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231130_170029-iaantizl
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 1WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/iaantizl
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:00:45,568] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7f4d0d7daa40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:00:50,560] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpo6zmqqwy.py line 218 
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:01,481] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpo6zmqqwy.py line 117 
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,014] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpo6zmqqwy.py line 90 
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,181] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:02,830] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:05,489] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:06,907] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] 
[2023-11-30 17:01:08,026] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.005 MB uploadedwandb: / 0.005 MB of 0.005 MB uploadedwandb: - 0.008 MB of 0.120 MB uploadedwandb: \ 0.008 MB of 0.120 MB uploadedwandb: | 0.120 MB of 0.120 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▄▃▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▇▇▅▄▄▃▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▇▇▄▃▃▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▆█▇▄▃▂▂▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▆▇▆▃▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.02211
wandb:     train l1 loss 0.77384
wandb:        train_loss 0.01356
wandb:       val l1 loss 0.94354
wandb:          val loss 0.02211
wandb: 
wandb: 🚀 View run 1WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/iaantizl
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231130_170029-iaantizl/logs
Epoch [1/650], Train Loss: 0.1746, Train L1 Loss: 1.9826
Epoch [1/650], Validation Loss: 0.0714, Validation L1: 1.7551, Smoothed Validation Loss: 0.0714
Epoch [2/650], Train Loss: 0.0586, Train L1 Loss: 1.5459
Epoch [2/650], Validation Loss: 0.0697, Validation L1: 1.7230, Smoothed Validation Loss: 0.0713
Epoch [3/650], Train Loss: 0.0547, Train L1 Loss: 1.4923
Epoch [3/650], Validation Loss: 0.1037, Validation L1: 2.3174, Smoothed Validation Loss: 0.0745
Epoch [4/650], Train Loss: 0.0512, Train L1 Loss: 1.4402
Epoch [4/650], Validation Loss: 0.0650, Validation L1: 1.6939, Smoothed Validation Loss: 0.0735
Epoch [5/650], Train Loss: 0.0487, Train L1 Loss: 1.4010
Epoch [5/650], Validation Loss: 0.0463, Validation L1: 1.3748, Smoothed Validation Loss: 0.0708
Epoch [6/650], Train Loss: 0.0468, Train L1 Loss: 1.3704
Epoch [6/650], Validation Loss: 0.0410, Validation L1: 1.2801, Smoothed Validation Loss: 0.0678
Epoch [7/650], Train Loss: 0.0449, Train L1 Loss: 1.3401
Epoch [7/650], Validation Loss: 0.0379, Validation L1: 1.2400, Smoothed Validation Loss: 0.0649
Epoch [8/650], Train Loss: 0.0430, Train L1 Loss: 1.3091
Epoch [8/650], Validation Loss: 0.0367, Validation L1: 1.2211, Smoothed Validation Loss: 0.0620
Epoch [9/650], Train Loss: 0.0417, Train L1 Loss: 1.2897
Epoch [9/650], Validation Loss: 0.0410, Validation L1: 1.2927, Smoothed Validation Loss: 0.0599
Epoch [10/650], Train Loss: 0.0404, Train L1 Loss: 1.2712
Epoch [10/650], Validation Loss: 0.0366, Validation L1: 1.2316, Smoothed Validation Loss: 0.0576
Epoch [11/650], Train Loss: 0.0390, Train L1 Loss: 1.2513
Epoch [11/650], Validation Loss: 0.0343, Validation L1: 1.1808, Smoothed Validation Loss: 0.0553
Epoch [12/650], Train Loss: 0.0385, Train L1 Loss: 1.2457
Epoch [12/650], Validation Loss: 0.0325, Validation L1: 1.1461, Smoothed Validation Loss: 0.0530
Epoch [13/650], Train Loss: 0.0368, Train L1 Loss: 1.2216
Epoch [13/650], Validation Loss: 0.0313, Validation L1: 1.1288, Smoothed Validation Loss: 0.0508
Epoch [14/650], Train Loss: 0.0392, Train L1 Loss: 1.2598
Epoch [14/650], Validation Loss: 0.0338, Validation L1: 1.1726, Smoothed Validation Loss: 0.0491
Epoch [15/650], Train Loss: 0.0361, Train L1 Loss: 1.2083
Epoch [15/650], Validation Loss: 0.0322, Validation L1: 1.1392, Smoothed Validation Loss: 0.0474
Epoch [16/650], Train Loss: 0.0372, Train L1 Loss: 1.2212
Epoch [16/650], Validation Loss: 0.0330, Validation L1: 1.1436, Smoothed Validation Loss: 0.0460
Epoch [17/650], Train Loss: 0.0352, Train L1 Loss: 1.1801
Epoch [17/650], Validation Loss: 0.0314, Validation L1: 1.1243, Smoothed Validation Loss: 0.0445
Epoch [18/650], Train Loss: 0.0353, Train L1 Loss: 1.1891
Epoch [18/650], Validation Loss: 0.0327, Validation L1: 1.1575, Smoothed Validation Loss: 0.0433
Epoch [19/650], Train Loss: 0.0366, Train L1 Loss: 1.2100
Epoch [19/650], Validation Loss: 0.0336, Validation L1: 1.1613, Smoothed Validation Loss: 0.0424
Epoch [20/650], Train Loss: 0.0368, Train L1 Loss: 1.2225
Epoch [20/650], Validation Loss: 0.0327, Validation L1: 1.1693, Smoothed Validation Loss: 0.0414
Epoch [21/650], Train Loss: 0.0385, Train L1 Loss: 1.2252
Epoch [21/650], Validation Loss: 0.0318, Validation L1: 1.1446, Smoothed Validation Loss: 0.0404
Epoch [22/650], Train Loss: 0.0343, Train L1 Loss: 1.1646
Epoch [22/650], Validation Loss: 0.0314, Validation L1: 1.1308, Smoothed Validation Loss: 0.0395
Epoch [23/650], Train Loss: 0.0343, Train L1 Loss: 1.1668
Epoch [23/650], Validation Loss: 0.0296, Validation L1: 1.1089, Smoothed Validation Loss: 0.0385
Epoch [24/650], Train Loss: 0.0370, Train L1 Loss: 1.2087
Epoch [24/650], Validation Loss: 0.0330, Validation L1: 1.1451, Smoothed Validation Loss: 0.0380
Epoch [25/650], Train Loss: 0.0344, Train L1 Loss: 1.1721
Epoch [25/650], Validation Loss: 0.0307, Validation L1: 1.1270, Smoothed Validation Loss: 0.0373
Epoch [26/650], Train Loss: 0.0333, Train L1 Loss: 1.1546
Epoch [26/650], Validation Loss: 0.0306, Validation L1: 1.1208, Smoothed Validation Loss: 0.0366
Epoch [27/650], Train Loss: 0.0333, Train L1 Loss: 1.1495
Epoch [27/650], Validation Loss: 0.0298, Validation L1: 1.1096, Smoothed Validation Loss: 0.0359
Epoch [28/650], Train Loss: 0.0323, Train L1 Loss: 1.1432
Epoch [28/650], Validation Loss: 0.0295, Validation L1: 1.1351, Smoothed Validation Loss: 0.0353
Epoch [29/650], Train Loss: 0.0327, Train L1 Loss: 1.1429
Epoch [29/650], Validation Loss: 0.0292, Validation L1: 1.0972, Smoothed Validation Loss: 0.0347
Epoch [30/650], Train Loss: 0.0338, Train L1 Loss: 1.1662
Epoch [30/650], Validation Loss: 0.0320, Validation L1: 1.1631, Smoothed Validation Loss: 0.0344
Epoch [31/650], Train Loss: 0.0367, Train L1 Loss: 1.1957
Epoch [31/650], Validation Loss: 0.0289, Validation L1: 1.1277, Smoothed Validation Loss: 0.0338
Epoch [32/650], Train Loss: 0.0326, Train L1 Loss: 1.1434
Epoch [32/650], Validation Loss: 0.0295, Validation L1: 1.1192, Smoothed Validation Loss: 0.0334
Epoch [33/650], Train Loss: 0.0326, Train L1 Loss: 1.1490
Epoch [33/650], Validation Loss: 0.0294, Validation L1: 1.1175, Smoothed Validation Loss: 0.0330
Epoch [34/650], Train Loss: 0.0322, Train L1 Loss: 1.1477
Epoch [34/650], Validation Loss: 0.0297, Validation L1: 1.1277, Smoothed Validation Loss: 0.0327
Epoch [35/650], Train Loss: 0.0376, Train L1 Loss: 1.2167
Epoch [35/650], Validation Loss: 0.0385, Validation L1: 1.2757, Smoothed Validation Loss: 0.0333
Epoch [36/650], Train Loss: 0.0369, Train L1 Loss: 1.2236
Epoch [36/650], Validation Loss: 0.0306, Validation L1: 1.1668, Smoothed Validation Loss: 0.0330
Epoch [37/650], Train Loss: 0.0314, Train L1 Loss: 1.1352
Epoch [37/650], Validation Loss: 0.0290, Validation L1: 1.1279, Smoothed Validation Loss: 0.0326
Epoch [38/650], Train Loss: 0.0321, Train L1 Loss: 1.1525
Epoch [38/650], Validation Loss: 0.0333, Validation L1: 1.1961, Smoothed Validation Loss: 0.0327
Epoch [39/650], Train Loss: 0.0445, Train L1 Loss: 1.2474
Epoch [39/650], Validation Loss: 0.0393, Validation L1: 1.2818, Smoothed Validation Loss: 0.0333
Epoch [40/650], Train Loss: 0.0406, Train L1 Loss: 1.2613
Epoch [40/650], Validation Loss: 0.0341, Validation L1: 1.2213, Smoothed Validation Loss: 0.0334
Epoch [41/650], Train Loss: 0.0368, Train L1 Loss: 1.2045
Epoch [41/650], Validation Loss: 0.0325, Validation L1: 1.1919, Smoothed Validation Loss: 0.0333
Epoch [42/650], Train Loss: 0.0370, Train L1 Loss: 1.2114
Epoch [42/650], Validation Loss: 0.0359, Validation L1: 1.2375, Smoothed Validation Loss: 0.0336
Epoch [43/650], Train Loss: 0.0361, Train L1 Loss: 1.1911
Epoch [43/650], Validation Loss: 0.0333, Validation L1: 1.2246, Smoothed Validation Loss: 0.0335
Epoch 00043: reducing learning rate of group 0 to 5.0000e-04.
Epoch [44/650], Train Loss: 0.0316, Train L1 Loss: 1.1201
Epoch [44/650], Validation Loss: 0.0294, Validation L1: 1.1324, Smoothed Validation Loss: 0.0331
Epoch [45/650], Train Loss: 0.0317, Train L1 Loss: 1.1301
Epoch [45/650], Validation Loss: 0.0327, Validation L1: 1.1928, Smoothed Validation Loss: 0.0331
Epoch [46/650], Train Loss: 0.0311, Train L1 Loss: 1.1070
Epoch [46/650], Validation Loss: 0.0302, Validation L1: 1.1787, Smoothed Validation Loss: 0.0328
Epoch [47/650], Train Loss: 0.0295, Train L1 Loss: 1.0873
Epoch [47/650], Validation Loss: 0.0319, Validation L1: 1.1982, Smoothed Validation Loss: 0.0327
Epoch [48/650], Train Loss: 0.0304, Train L1 Loss: 1.0949
Epoch [48/650], Validation Loss: 0.0305, Validation L1: 1.1988, Smoothed Validation Loss: 0.0325
Epoch [49/650], Train Loss: 0.0282, Train L1 Loss: 1.0741
Epoch [49/650], Validation Loss: 0.0306, Validation L1: 1.1927, Smoothed Validation Loss: 0.0323
Epoch [50/650], Train Loss: 0.0303, Train L1 Loss: 1.0977
Epoch [50/650], Validation Loss: 0.0303, Validation L1: 1.1702, Smoothed Validation Loss: 0.0321
Epoch [51/650], Train Loss: 0.0277, Train L1 Loss: 1.0639
Epoch [51/650], Validation Loss: 0.0309, Validation L1: 1.1995, Smoothed Validation Loss: 0.0320
Epoch [52/650], Train Loss: 0.0271, Train L1 Loss: 1.0597
Epoch [52/650], Validation Loss: 0.0318, Validation L1: 1.1769, Smoothed Validation Loss: 0.0320
Epoch [53/650], Train Loss: 0.0294, Train L1 Loss: 1.0849
Epoch [53/650], Validation Loss: 0.0314, Validation L1: 1.2040, Smoothed Validation Loss: 0.0319
Epoch [54/650], Train Loss: 0.0286, Train L1 Loss: 1.0729
Epoch [54/650], Validation Loss: 0.0276, Validation L1: 1.1085, Smoothed Validation Loss: 0.0315
Epoch [55/650], Train Loss: 0.0258, Train L1 Loss: 1.0423
Epoch [55/650], Validation Loss: 0.0319, Validation L1: 1.1549, Smoothed Validation Loss: 0.0315
Epoch [56/650], Train Loss: 0.0256, Train L1 Loss: 1.0428
Epoch [56/650], Validation Loss: 0.0315, Validation L1: 1.1847, Smoothed Validation Loss: 0.0315
Epoch [57/650], Train Loss: 0.0252, Train L1 Loss: 1.0365
Epoch [57/650], Validation Loss: 0.0315, Validation L1: 1.2100, Smoothed Validation Loss: 0.0315
Epoch [58/650], Train Loss: 0.0256, Train L1 Loss: 1.0410
Epoch [58/650], Validation Loss: 0.0297, Validation L1: 1.1693, Smoothed Validation Loss: 0.0313
Epoch [59/650], Train Loss: 0.0270, Train L1 Loss: 1.0401
Epoch [59/650], Validation Loss: 0.0278, Validation L1: 1.1228, Smoothed Validation Loss: 0.0310
Epoch [60/650], Train Loss: 0.0271, Train L1 Loss: 1.0557
Epoch [60/650], Validation Loss: 0.0271, Validation L1: 1.0770, Smoothed Validation Loss: 0.0306
Epoch [61/650], Train Loss: 0.0249, Train L1 Loss: 1.0305
Epoch [61/650], Validation Loss: 0.0285, Validation L1: 1.0918, Smoothed Validation Loss: 0.0304
Epoch [62/650], Train Loss: 0.0246, Train L1 Loss: 1.0226
Epoch [62/650], Validation Loss: 0.0280, Validation L1: 1.1097, Smoothed Validation Loss: 0.0301
Epoch [63/650], Train Loss: 0.0247, Train L1 Loss: 1.0209
Epoch [63/650], Validation Loss: 0.0338, Validation L1: 1.1042, Smoothed Validation Loss: 0.0305
Epoch [64/650], Train Loss: 0.0247, Train L1 Loss: 1.0208
Epoch [64/650], Validation Loss: 0.0271, Validation L1: 1.0971, Smoothed Validation Loss: 0.0302
Epoch [65/650], Train Loss: 0.0308, Train L1 Loss: 1.0967
Epoch [65/650], Validation Loss: 0.0280, Validation L1: 1.0833, Smoothed Validation Loss: 0.0299
Epoch [66/650], Train Loss: 0.0268, Train L1 Loss: 1.0473
Epoch [66/650], Validation Loss: 0.0258, Validation L1: 1.0448, Smoothed Validation Loss: 0.0295
Epoch [67/650], Train Loss: 0.0261, Train L1 Loss: 1.0229
Epoch [67/650], Validation Loss: 0.0255, Validation L1: 1.0532, Smoothed Validation Loss: 0.0291
Epoch [68/650], Train Loss: 0.0238, Train L1 Loss: 1.0116
Epoch [68/650], Validation Loss: 0.0297, Validation L1: 1.1536, Smoothed Validation Loss: 0.0292
Epoch [69/650], Train Loss: 0.0235, Train L1 Loss: 1.0012
Epoch [69/650], Validation Loss: 0.0278, Validation L1: 1.1117, Smoothed Validation Loss: 0.0290
Epoch [70/650], Train Loss: 0.0278, Train L1 Loss: 1.0493
Epoch [70/650], Validation Loss: 0.0252, Validation L1: 1.0357, Smoothed Validation Loss: 0.0287
Epoch [71/650], Train Loss: 0.0249, Train L1 Loss: 1.0148
Epoch [71/650], Validation Loss: 0.0257, Validation L1: 1.0520, Smoothed Validation Loss: 0.0284
Epoch [72/650], Train Loss: 0.0228, Train L1 Loss: 0.9929
Epoch [72/650], Validation Loss: 0.0270, Validation L1: 1.0674, Smoothed Validation Loss: 0.0282
Epoch [73/650], Train Loss: 0.0235, Train L1 Loss: 0.9962
Epoch [73/650], Validation Loss: 0.0272, Validation L1: 1.1097, Smoothed Validation Loss: 0.0281
Epoch [74/650], Train Loss: 0.0242, Train L1 Loss: 0.9965
Epoch [74/650], Validation Loss: 0.0255, Validation L1: 1.0390, Smoothed Validation Loss: 0.0279
Epoch [75/650], Train Loss: 0.0231, Train L1 Loss: 0.9921
Epoch [75/650], Validation Loss: 0.0275, Validation L1: 1.0479, Smoothed Validation Loss: 0.0278
Epoch [76/650], Train Loss: 0.0235, Train L1 Loss: 1.0018
Epoch [76/650], Validation Loss: 0.0272, Validation L1: 1.0914, Smoothed Validation Loss: 0.0278
Epoch [77/650], Train Loss: 0.0222, Train L1 Loss: 0.9793
Epoch [77/650], Validation Loss: 0.0258, Validation L1: 1.0591, Smoothed Validation Loss: 0.0276
Epoch [78/650], Train Loss: 0.0268, Train L1 Loss: 1.0333
Epoch [78/650], Validation Loss: 0.0247, Validation L1: 1.0255, Smoothed Validation Loss: 0.0273
Epoch [79/650], Train Loss: 0.0229, Train L1 Loss: 0.9892
Epoch [79/650], Validation Loss: 0.0252, Validation L1: 1.0380, Smoothed Validation Loss: 0.0271
Epoch [80/650], Train Loss: 0.0226, Train L1 Loss: 0.9867
Epoch [80/650], Validation Loss: 0.0270, Validation L1: 1.0728, Smoothed Validation Loss: 0.0271
Epoch [81/650], Train Loss: 0.0227, Train L1 Loss: 0.9849
Epoch [81/650], Validation Loss: 0.0257, Validation L1: 1.0645, Smoothed Validation Loss: 0.0269
Epoch [82/650], Train Loss: 0.0230, Train L1 Loss: 0.9814
Epoch [82/650], Validation Loss: 0.0247, Validation L1: 1.0303, Smoothed Validation Loss: 0.0267
Epoch [83/650], Train Loss: 0.0238, Train L1 Loss: 1.0025
Epoch [83/650], Validation Loss: 0.0279, Validation L1: 1.1063, Smoothed Validation Loss: 0.0268
Epoch [84/650], Train Loss: 0.0240, Train L1 Loss: 1.0076
Epoch [84/650], Validation Loss: 0.0254, Validation L1: 1.0229, Smoothed Validation Loss: 0.0267
Epoch [85/650], Train Loss: 0.0222, Train L1 Loss: 0.9807
Epoch [85/650], Validation Loss: 0.0241, Validation L1: 1.0095, Smoothed Validation Loss: 0.0264
Epoch [86/650], Train Loss: 0.0245, Train L1 Loss: 1.0050
Epoch [86/650], Validation Loss: 0.0251, Validation L1: 1.0236, Smoothed Validation Loss: 0.0263
Epoch [87/650], Train Loss: 0.0230, Train L1 Loss: 0.9911
Epoch [87/650], Validation Loss: 0.0242, Validation L1: 1.0059, Smoothed Validation Loss: 0.0261
Epoch [88/650], Train Loss: 0.0222, Train L1 Loss: 0.9763
Epoch [88/650], Validation Loss: 0.0247, Validation L1: 1.0181, Smoothed Validation Loss: 0.0259
Epoch [89/650], Train Loss: 0.0234, Train L1 Loss: 0.9858
Epoch [89/650], Validation Loss: 0.0260, Validation L1: 1.0554, Smoothed Validation Loss: 0.0259
Epoch [90/650], Train Loss: 0.0234, Train L1 Loss: 0.9740
Epoch [90/650], Validation Loss: 0.0247, Validation L1: 1.0196, Smoothed Validation Loss: 0.0258
Epoch [91/650], Train Loss: 0.0224, Train L1 Loss: 0.9702
Epoch [91/650], Validation Loss: 0.0245, Validation L1: 1.0251, Smoothed Validation Loss: 0.0257
Epoch [92/650], Train Loss: 0.0221, Train L1 Loss: 0.9720
Epoch [92/650], Validation Loss: 0.0246, Validation L1: 1.0165, Smoothed Validation Loss: 0.0256
Epoch [93/650], Train Loss: 0.0224, Train L1 Loss: 0.9766
Epoch [93/650], Validation Loss: 0.0327, Validation L1: 1.2143, Smoothed Validation Loss: 0.0263
Epoch [94/650], Train Loss: 0.0227, Train L1 Loss: 0.9879
Epoch [94/650], Validation Loss: 0.0249, Validation L1: 1.0266, Smoothed Validation Loss: 0.0261
Epoch [95/650], Train Loss: 0.0229, Train L1 Loss: 0.9877
Epoch [95/650], Validation Loss: 0.0244, Validation L1: 1.0001, Smoothed Validation Loss: 0.0260
Epoch [96/650], Train Loss: 0.0220, Train L1 Loss: 0.9753
Epoch [96/650], Validation Loss: 0.0246, Validation L1: 1.0157, Smoothed Validation Loss: 0.0258
Epoch [97/650], Train Loss: 0.0209, Train L1 Loss: 0.9564
Epoch [97/650], Validation Loss: 0.0254, Validation L1: 1.0437, Smoothed Validation Loss: 0.0258
Epoch [98/650], Train Loss: 0.0218, Train L1 Loss: 0.9680
Epoch [98/650], Validation Loss: 0.0244, Validation L1: 1.0107, Smoothed Validation Loss: 0.0257
Epoch 00098: reducing learning rate of group 0 to 2.5000e-04.
Epoch [99/650], Train Loss: 0.0215, Train L1 Loss: 0.9447
Epoch [99/650], Validation Loss: 0.0231, Validation L1: 0.9916, Smoothed Validation Loss: 0.0254
Epoch [100/650], Train Loss: 0.0201, Train L1 Loss: 0.9240
Epoch [100/650], Validation Loss: 0.0229, Validation L1: 0.9829, Smoothed Validation Loss: 0.0252
Epoch [101/650], Train Loss: 0.0192, Train L1 Loss: 0.9158
Epoch [101/650], Validation Loss: 0.0228, Validation L1: 0.9831, Smoothed Validation Loss: 0.0249
Epoch [102/650], Train Loss: 0.0190, Train L1 Loss: 0.9109
Epoch [102/650], Validation Loss: 0.0231, Validation L1: 0.9864, Smoothed Validation Loss: 0.0247
Epoch [103/650], Train Loss: 0.0188, Train L1 Loss: 0.9082
Epoch [103/650], Validation Loss: 0.0229, Validation L1: 0.9807, Smoothed Validation Loss: 0.0246
Epoch [104/650], Train Loss: 0.0186, Train L1 Loss: 0.9043
Epoch [104/650], Validation Loss: 0.0229, Validation L1: 0.9854, Smoothed Validation Loss: 0.0244
Epoch [105/650], Train Loss: 0.0186, Train L1 Loss: 0.9036
Epoch [105/650], Validation Loss: 0.0232, Validation L1: 0.9879, Smoothed Validation Loss: 0.0243
Epoch [106/650], Train Loss: 0.0186, Train L1 Loss: 0.9030
Epoch [106/650], Validation Loss: 0.0232, Validation L1: 0.9943, Smoothed Validation Loss: 0.0242
Epoch [107/650], Train Loss: 0.0185, Train L1 Loss: 0.9007
Epoch [107/650], Validation Loss: 0.0233, Validation L1: 0.9917, Smoothed Validation Loss: 0.0241
Epoch [108/650], Train Loss: 0.0182, Train L1 Loss: 0.8963
Epoch [108/650], Validation Loss: 0.0231, Validation L1: 0.9882, Smoothed Validation Loss: 0.0240
Epoch [109/650], Train Loss: 0.0180, Train L1 Loss: 0.8930
Epoch [109/650], Validation Loss: 0.0233, Validation L1: 0.9918, Smoothed Validation Loss: 0.0239
Epoch [110/650], Train Loss: 0.0181, Train L1 Loss: 0.8938
Epoch [110/650], Validation Loss: 0.0235, Validation L1: 0.9970, Smoothed Validation Loss: 0.0239
Epoch [111/650], Train Loss: 0.0181, Train L1 Loss: 0.8930
Epoch [111/650], Validation Loss: 0.0237, Validation L1: 0.9972, Smoothed Validation Loss: 0.0239
Epoch [112/650], Train Loss: 0.0180, Train L1 Loss: 0.8906
Epoch [112/650], Validation Loss: 0.0235, Validation L1: 0.9951, Smoothed Validation Loss: 0.0238
Epoch [113/650], Train Loss: 0.0178, Train L1 Loss: 0.8871
Epoch [113/650], Validation Loss: 0.0237, Validation L1: 0.9979, Smoothed Validation Loss: 0.0238
Epoch [114/650], Train Loss: 0.0177, Train L1 Loss: 0.8859
Epoch [114/650], Validation Loss: 0.0235, Validation L1: 0.9952, Smoothed Validation Loss: 0.0238
Epoch [115/650], Train Loss: 0.0177, Train L1 Loss: 0.8847
Epoch [115/650], Validation Loss: 0.0238, Validation L1: 1.0000, Smoothed Validation Loss: 0.0238
Epoch [116/650], Train Loss: 0.0176, Train L1 Loss: 0.8830
Epoch [116/650], Validation Loss: 0.0236, Validation L1: 0.9981, Smoothed Validation Loss: 0.0238
Epoch [117/650], Train Loss: 0.0176, Train L1 Loss: 0.8830
Epoch [117/650], Validation Loss: 0.0238, Validation L1: 0.9990, Smoothed Validation Loss: 0.0238
Epoch [118/650], Train Loss: 0.0175, Train L1 Loss: 0.8805
Epoch [118/650], Validation Loss: 0.0237, Validation L1: 1.0002, Smoothed Validation Loss: 0.0238
Epoch [119/650], Train Loss: 0.0173, Train L1 Loss: 0.8772
Epoch [119/650], Validation Loss: 0.0237, Validation L1: 0.9975, Smoothed Validation Loss: 0.0237
Epoch [120/650], Train Loss: 0.0173, Train L1 Loss: 0.8771
Epoch [120/650], Validation Loss: 0.0236, Validation L1: 0.9973, Smoothed Validation Loss: 0.0237
Epoch [121/650], Train Loss: 0.0172, Train L1 Loss: 0.8749
Epoch [121/650], Validation Loss: 0.0237, Validation L1: 0.9980, Smoothed Validation Loss: 0.0237
Epoch [122/650], Train Loss: 0.0172, Train L1 Loss: 0.8738
Epoch [122/650], Validation Loss: 0.0236, Validation L1: 0.9952, Smoothed Validation Loss: 0.0237
Epoch [123/650], Train Loss: 0.0171, Train L1 Loss: 0.8724
Epoch [123/650], Validation Loss: 0.0237, Validation L1: 0.9974, Smoothed Validation Loss: 0.0237
Epoch [124/650], Train Loss: 0.0170, Train L1 Loss: 0.8704
Epoch [124/650], Validation Loss: 0.0236, Validation L1: 0.9955, Smoothed Validation Loss: 0.0237
Epoch [125/650], Train Loss: 0.0169, Train L1 Loss: 0.8685
Epoch [125/650], Validation Loss: 0.0238, Validation L1: 0.9977, Smoothed Validation Loss: 0.0237
Epoch [126/650], Train Loss: 0.0170, Train L1 Loss: 0.8695
Epoch [126/650], Validation Loss: 0.0237, Validation L1: 0.9974, Smoothed Validation Loss: 0.0237
Epoch [127/650], Train Loss: 0.0170, Train L1 Loss: 0.8694
Epoch [127/650], Validation Loss: 0.0238, Validation L1: 0.9967, Smoothed Validation Loss: 0.0237
Epoch [128/650], Train Loss: 0.0168, Train L1 Loss: 0.8649
Epoch [128/650], Validation Loss: 0.0239, Validation L1: 1.0000, Smoothed Validation Loss: 0.0237
Epoch [129/650], Train Loss: 0.0167, Train L1 Loss: 0.8635
Epoch [129/650], Validation Loss: 0.0238, Validation L1: 0.9970, Smoothed Validation Loss: 0.0237
Epoch [130/650], Train Loss: 0.0167, Train L1 Loss: 0.8631
Epoch [130/650], Validation Loss: 0.0239, Validation L1: 0.9988, Smoothed Validation Loss: 0.0238
Epoch 00130: reducing learning rate of group 0 to 1.2500e-04.
Epoch [131/650], Train Loss: 0.0165, Train L1 Loss: 0.8559
Epoch [131/650], Validation Loss: 0.0226, Validation L1: 0.9583, Smoothed Validation Loss: 0.0236
Epoch [132/650], Train Loss: 0.0162, Train L1 Loss: 0.8485
Epoch [132/650], Validation Loss: 0.0226, Validation L1: 0.9604, Smoothed Validation Loss: 0.0235
Epoch [133/650], Train Loss: 0.0161, Train L1 Loss: 0.8456
Epoch [133/650], Validation Loss: 0.0226, Validation L1: 0.9610, Smoothed Validation Loss: 0.0234
Epoch [134/650], Train Loss: 0.0160, Train L1 Loss: 0.8437
Epoch [134/650], Validation Loss: 0.0226, Validation L1: 0.9614, Smoothed Validation Loss: 0.0234
Epoch [135/650], Train Loss: 0.0159, Train L1 Loss: 0.8421
Epoch [135/650], Validation Loss: 0.0226, Validation L1: 0.9618, Smoothed Validation Loss: 0.0233
Epoch [136/650], Train Loss: 0.0159, Train L1 Loss: 0.8406
Epoch [136/650], Validation Loss: 0.0226, Validation L1: 0.9623, Smoothed Validation Loss: 0.0232
Epoch [137/650], Train Loss: 0.0158, Train L1 Loss: 0.8392
Epoch [137/650], Validation Loss: 0.0226, Validation L1: 0.9628, Smoothed Validation Loss: 0.0232
Epoch [138/650], Train Loss: 0.0158, Train L1 Loss: 0.8378
Epoch [138/650], Validation Loss: 0.0226, Validation L1: 0.9634, Smoothed Validation Loss: 0.0231
Epoch [139/650], Train Loss: 0.0157, Train L1 Loss: 0.8365
Epoch [139/650], Validation Loss: 0.0226, Validation L1: 0.9639, Smoothed Validation Loss: 0.0231
Epoch [140/650], Train Loss: 0.0157, Train L1 Loss: 0.8352
Epoch [140/650], Validation Loss: 0.0226, Validation L1: 0.9645, Smoothed Validation Loss: 0.0230
Epoch [141/650], Train Loss: 0.0156, Train L1 Loss: 0.8340
Epoch [141/650], Validation Loss: 0.0226, Validation L1: 0.9648, Smoothed Validation Loss: 0.0230
Epoch [142/650], Train Loss: 0.0156, Train L1 Loss: 0.8327
Epoch [142/650], Validation Loss: 0.0226, Validation L1: 0.9655, Smoothed Validation Loss: 0.0229
Epoch [143/650], Train Loss: 0.0155, Train L1 Loss: 0.8316
Epoch [143/650], Validation Loss: 0.0226, Validation L1: 0.9656, Smoothed Validation Loss: 0.0229
Epoch [144/650], Train Loss: 0.0155, Train L1 Loss: 0.8304
Epoch [144/650], Validation Loss: 0.0227, Validation L1: 0.9664, Smoothed Validation Loss: 0.0229
Epoch [145/650], Train Loss: 0.0154, Train L1 Loss: 0.8294
Epoch [145/650], Validation Loss: 0.0227, Validation L1: 0.9659, Smoothed Validation Loss: 0.0229
Epoch [146/650], Train Loss: 0.0154, Train L1 Loss: 0.8282
Epoch [146/650], Validation Loss: 0.0227, Validation L1: 0.9671, Smoothed Validation Loss: 0.0229
Epoch [147/650], Train Loss: 0.0154, Train L1 Loss: 0.8273
Epoch [147/650], Validation Loss: 0.0227, Validation L1: 0.9663, Smoothed Validation Loss: 0.0228
Epoch [148/650], Train Loss: 0.0153, Train L1 Loss: 0.8261
Epoch [148/650], Validation Loss: 0.0227, Validation L1: 0.9678, Smoothed Validation Loss: 0.0228
Epoch [149/650], Train Loss: 0.0153, Train L1 Loss: 0.8252
Epoch [149/650], Validation Loss: 0.0227, Validation L1: 0.9667, Smoothed Validation Loss: 0.0228
Epoch [150/650], Train Loss: 0.0152, Train L1 Loss: 0.8240
Epoch [150/650], Validation Loss: 0.0228, Validation L1: 0.9683, Smoothed Validation Loss: 0.0228
Epoch [151/650], Train Loss: 0.0152, Train L1 Loss: 0.8232
Epoch [151/650], Validation Loss: 0.0227, Validation L1: 0.9671, Smoothed Validation Loss: 0.0228
Epoch [152/650], Train Loss: 0.0152, Train L1 Loss: 0.8220
Epoch [152/650], Validation Loss: 0.0228, Validation L1: 0.9688, Smoothed Validation Loss: 0.0228
Epoch [153/650], Train Loss: 0.0151, Train L1 Loss: 0.8212
Epoch [153/650], Validation Loss: 0.0228, Validation L1: 0.9674, Smoothed Validation Loss: 0.0228
Epoch [154/650], Train Loss: 0.0151, Train L1 Loss: 0.8200
Epoch [154/650], Validation Loss: 0.0228, Validation L1: 0.9691, Smoothed Validation Loss: 0.0228
Epoch [155/650], Train Loss: 0.0151, Train L1 Loss: 0.8192
Epoch [155/650], Validation Loss: 0.0228, Validation L1: 0.9676, Smoothed Validation Loss: 0.0228
Epoch [156/650], Train Loss: 0.0150, Train L1 Loss: 0.8180
Epoch [156/650], Validation Loss: 0.0229, Validation L1: 0.9695, Smoothed Validation Loss: 0.0228
Epoch [157/650], Train Loss: 0.0150, Train L1 Loss: 0.8174
Epoch [157/650], Validation Loss: 0.0228, Validation L1: 0.9678, Smoothed Validation Loss: 0.0228
Epoch [158/650], Train Loss: 0.0150, Train L1 Loss: 0.8161
Epoch [158/650], Validation Loss: 0.0229, Validation L1: 0.9697, Smoothed Validation Loss: 0.0228
Epoch [159/650], Train Loss: 0.0149, Train L1 Loss: 0.8156
Epoch [159/650], Validation Loss: 0.0229, Validation L1: 0.9679, Smoothed Validation Loss: 0.0228
Epoch 00159: reducing learning rate of group 0 to 6.2500e-05.
Epoch [160/650], Train Loss: 0.0150, Train L1 Loss: 0.8178
Epoch [160/650], Validation Loss: 0.0227, Validation L1: 0.9684, Smoothed Validation Loss: 0.0228
Epoch [161/650], Train Loss: 0.0149, Train L1 Loss: 0.8149
Epoch [161/650], Validation Loss: 0.0227, Validation L1: 0.9680, Smoothed Validation Loss: 0.0228
Epoch [162/650], Train Loss: 0.0148, Train L1 Loss: 0.8130
Epoch [162/650], Validation Loss: 0.0227, Validation L1: 0.9682, Smoothed Validation Loss: 0.0228
Epoch [163/650], Train Loss: 0.0148, Train L1 Loss: 0.8115
Epoch [163/650], Validation Loss: 0.0227, Validation L1: 0.9682, Smoothed Validation Loss: 0.0228
Epoch [164/650], Train Loss: 0.0148, Train L1 Loss: 0.8103
Epoch [164/650], Validation Loss: 0.0227, Validation L1: 0.9684, Smoothed Validation Loss: 0.0228
Epoch [165/650], Train Loss: 0.0147, Train L1 Loss: 0.8092
Epoch [165/650], Validation Loss: 0.0227, Validation L1: 0.9685, Smoothed Validation Loss: 0.0228
Epoch [166/650], Train Loss: 0.0147, Train L1 Loss: 0.8083
Epoch [166/650], Validation Loss: 0.0227, Validation L1: 0.9687, Smoothed Validation Loss: 0.0228
Epoch [167/650], Train Loss: 0.0147, Train L1 Loss: 0.8074
Epoch [167/650], Validation Loss: 0.0227, Validation L1: 0.9688, Smoothed Validation Loss: 0.0228
Epoch [168/650], Train Loss: 0.0146, Train L1 Loss: 0.8066
Epoch [168/650], Validation Loss: 0.0228, Validation L1: 0.9691, Smoothed Validation Loss: 0.0228
Epoch [169/650], Train Loss: 0.0146, Train L1 Loss: 0.8057
Epoch [169/650], Validation Loss: 0.0228, Validation L1: 0.9692, Smoothed Validation Loss: 0.0228
Epoch [170/650], Train Loss: 0.0146, Train L1 Loss: 0.8049
Epoch [170/650], Validation Loss: 0.0228, Validation L1: 0.9694, Smoothed Validation Loss: 0.0228
Epoch [171/650], Train Loss: 0.0145, Train L1 Loss: 0.8042
Epoch [171/650], Validation Loss: 0.0228, Validation L1: 0.9696, Smoothed Validation Loss: 0.0228
Epoch [172/650], Train Loss: 0.0145, Train L1 Loss: 0.8034
Epoch [172/650], Validation Loss: 0.0228, Validation L1: 0.9698, Smoothed Validation Loss: 0.0228
Epoch [173/650], Train Loss: 0.0145, Train L1 Loss: 0.8027
Epoch [173/650], Validation Loss: 0.0228, Validation L1: 0.9699, Smoothed Validation Loss: 0.0228
Epoch [174/650], Train Loss: 0.0145, Train L1 Loss: 0.8020
Epoch [174/650], Validation Loss: 0.0228, Validation L1: 0.9701, Smoothed Validation Loss: 0.0228
Epoch 00174: reducing learning rate of group 0 to 3.1250e-05.
Epoch [175/650], Train Loss: 0.0145, Train L1 Loss: 0.8043
Epoch [175/650], Validation Loss: 0.0225, Validation L1: 0.9530, Smoothed Validation Loss: 0.0227
Epoch [176/650], Train Loss: 0.0145, Train L1 Loss: 0.8024
Epoch [176/650], Validation Loss: 0.0225, Validation L1: 0.9525, Smoothed Validation Loss: 0.0227
Epoch [177/650], Train Loss: 0.0144, Train L1 Loss: 0.8012
Epoch [177/650], Validation Loss: 0.0224, Validation L1: 0.9522, Smoothed Validation Loss: 0.0227
Epoch [178/650], Train Loss: 0.0144, Train L1 Loss: 0.8003
Epoch [178/650], Validation Loss: 0.0224, Validation L1: 0.9520, Smoothed Validation Loss: 0.0227
Epoch [179/650], Train Loss: 0.0144, Train L1 Loss: 0.7995
Epoch [179/650], Validation Loss: 0.0224, Validation L1: 0.9519, Smoothed Validation Loss: 0.0226
Epoch [180/650], Train Loss: 0.0144, Train L1 Loss: 0.7987
Epoch [180/650], Validation Loss: 0.0224, Validation L1: 0.9518, Smoothed Validation Loss: 0.0226
Epoch [181/650], Train Loss: 0.0143, Train L1 Loss: 0.7981
Epoch [181/650], Validation Loss: 0.0224, Validation L1: 0.9517, Smoothed Validation Loss: 0.0226
Epoch [182/650], Train Loss: 0.0143, Train L1 Loss: 0.7975
Epoch [182/650], Validation Loss: 0.0224, Validation L1: 0.9517, Smoothed Validation Loss: 0.0226
Epoch [183/650], Train Loss: 0.0143, Train L1 Loss: 0.7969
Epoch [183/650], Validation Loss: 0.0224, Validation L1: 0.9516, Smoothed Validation Loss: 0.0226
Epoch [184/650], Train Loss: 0.0143, Train L1 Loss: 0.7963
Epoch [184/650], Validation Loss: 0.0224, Validation L1: 0.9516, Smoothed Validation Loss: 0.0226
Epoch [185/650], Train Loss: 0.0143, Train L1 Loss: 0.7958
Epoch [185/650], Validation Loss: 0.0224, Validation L1: 0.9516, Smoothed Validation Loss: 0.0225
Epoch [186/650], Train Loss: 0.0143, Train L1 Loss: 0.7953
Epoch [186/650], Validation Loss: 0.0224, Validation L1: 0.9516, Smoothed Validation Loss: 0.0225
Epoch [187/650], Train Loss: 0.0142, Train L1 Loss: 0.7948
Epoch [187/650], Validation Loss: 0.0224, Validation L1: 0.9516, Smoothed Validation Loss: 0.0225
Epoch [188/650], Train Loss: 0.0142, Train L1 Loss: 0.7943
Epoch [188/650], Validation Loss: 0.0224, Validation L1: 0.9516, Smoothed Validation Loss: 0.0225
Epoch [189/650], Train Loss: 0.0142, Train L1 Loss: 0.7939
Epoch [189/650], Validation Loss: 0.0224, Validation L1: 0.9516, Smoothed Validation Loss: 0.0225
Epoch [190/650], Train Loss: 0.0142, Train L1 Loss: 0.7934
Epoch [190/650], Validation Loss: 0.0224, Validation L1: 0.9517, Smoothed Validation Loss: 0.0225
Epoch [191/650], Train Loss: 0.0142, Train L1 Loss: 0.7930
Epoch [191/650], Validation Loss: 0.0225, Validation L1: 0.9517, Smoothed Validation Loss: 0.0225
Epoch [192/650], Train Loss: 0.0142, Train L1 Loss: 0.7925
Epoch [192/650], Validation Loss: 0.0225, Validation L1: 0.9517, Smoothed Validation Loss: 0.0225
Epoch [193/650], Train Loss: 0.0141, Train L1 Loss: 0.7921
Epoch [193/650], Validation Loss: 0.0225, Validation L1: 0.9518, Smoothed Validation Loss: 0.0225
Epoch [194/650], Train Loss: 0.0141, Train L1 Loss: 0.7917
Epoch [194/650], Validation Loss: 0.0225, Validation L1: 0.9518, Smoothed Validation Loss: 0.0225
Epoch [195/650], Train Loss: 0.0141, Train L1 Loss: 0.7912
Epoch [195/650], Validation Loss: 0.0225, Validation L1: 0.9519, Smoothed Validation Loss: 0.0225
Epoch [196/650], Train Loss: 0.0141, Train L1 Loss: 0.7908
Epoch [196/650], Validation Loss: 0.0225, Validation L1: 0.9519, Smoothed Validation Loss: 0.0225
Epoch [197/650], Train Loss: 0.0141, Train L1 Loss: 0.7904
Epoch [197/650], Validation Loss: 0.0225, Validation L1: 0.9519, Smoothed Validation Loss: 0.0225
Epoch [198/650], Train Loss: 0.0141, Train L1 Loss: 0.7900
Epoch [198/650], Validation Loss: 0.0225, Validation L1: 0.9520, Smoothed Validation Loss: 0.0225
Epoch [199/650], Train Loss: 0.0141, Train L1 Loss: 0.7896
Epoch [199/650], Validation Loss: 0.0225, Validation L1: 0.9521, Smoothed Validation Loss: 0.0225
Epoch [200/650], Train Loss: 0.0140, Train L1 Loss: 0.7892
Epoch [200/650], Validation Loss: 0.0225, Validation L1: 0.9521, Smoothed Validation Loss: 0.0225
Epoch [201/650], Train Loss: 0.0140, Train L1 Loss: 0.7888
Epoch [201/650], Validation Loss: 0.0225, Validation L1: 0.9521, Smoothed Validation Loss: 0.0225
Epoch [202/650], Train Loss: 0.0140, Train L1 Loss: 0.7884
Epoch [202/650], Validation Loss: 0.0225, Validation L1: 0.9522, Smoothed Validation Loss: 0.0225
Epoch 00202: reducing learning rate of group 0 to 1.5625e-05.
Epoch [203/650], Train Loss: 0.0141, Train L1 Loss: 0.7904
Epoch [203/650], Validation Loss: 0.0224, Validation L1: 0.9498, Smoothed Validation Loss: 0.0225
Epoch [204/650], Train Loss: 0.0140, Train L1 Loss: 0.7894
Epoch [204/650], Validation Loss: 0.0224, Validation L1: 0.9497, Smoothed Validation Loss: 0.0225
Epoch [205/650], Train Loss: 0.0140, Train L1 Loss: 0.7888
Epoch [205/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0225
Epoch [206/650], Train Loss: 0.0140, Train L1 Loss: 0.7884
Epoch [206/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [207/650], Train Loss: 0.0140, Train L1 Loss: 0.7880
Epoch [207/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [208/650], Train Loss: 0.0140, Train L1 Loss: 0.7876
Epoch [208/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [209/650], Train Loss: 0.0140, Train L1 Loss: 0.7872
Epoch [209/650], Validation Loss: 0.0224, Validation L1: 0.9495, Smoothed Validation Loss: 0.0224
Epoch [210/650], Train Loss: 0.0140, Train L1 Loss: 0.7869
Epoch [210/650], Validation Loss: 0.0224, Validation L1: 0.9495, Smoothed Validation Loss: 0.0224
Epoch [211/650], Train Loss: 0.0140, Train L1 Loss: 0.7866
Epoch [211/650], Validation Loss: 0.0224, Validation L1: 0.9495, Smoothed Validation Loss: 0.0224
Epoch [212/650], Train Loss: 0.0139, Train L1 Loss: 0.7863
Epoch [212/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [213/650], Train Loss: 0.0139, Train L1 Loss: 0.7860
Epoch [213/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [214/650], Train Loss: 0.0139, Train L1 Loss: 0.7857
Epoch [214/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [215/650], Train Loss: 0.0139, Train L1 Loss: 0.7854
Epoch [215/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [216/650], Train Loss: 0.0139, Train L1 Loss: 0.7852
Epoch [216/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [217/650], Train Loss: 0.0139, Train L1 Loss: 0.7849
Epoch [217/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [218/650], Train Loss: 0.0139, Train L1 Loss: 0.7846
Epoch [218/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [219/650], Train Loss: 0.0139, Train L1 Loss: 0.7844
Epoch [219/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [220/650], Train Loss: 0.0139, Train L1 Loss: 0.7841
Epoch [220/650], Validation Loss: 0.0224, Validation L1: 0.9496, Smoothed Validation Loss: 0.0224
Epoch [221/650], Train Loss: 0.0139, Train L1 Loss: 0.7839
Epoch [221/650], Validation Loss: 0.0224, Validation L1: 0.9497, Smoothed Validation Loss: 0.0224
Epoch [222/650], Train Loss: 0.0139, Train L1 Loss: 0.7836
Epoch [222/650], Validation Loss: 0.0224, Validation L1: 0.9497, Smoothed Validation Loss: 0.0224
Epoch [223/650], Train Loss: 0.0139, Train L1 Loss: 0.7834
Epoch [223/650], Validation Loss: 0.0224, Validation L1: 0.9497, Smoothed Validation Loss: 0.0224
Epoch [224/650], Train Loss: 0.0138, Train L1 Loss: 0.7831
Epoch [224/650], Validation Loss: 0.0224, Validation L1: 0.9497, Smoothed Validation Loss: 0.0224
Epoch [225/650], Train Loss: 0.0138, Train L1 Loss: 0.7829
Epoch [225/650], Validation Loss: 0.0224, Validation L1: 0.9497, Smoothed Validation Loss: 0.0224
Epoch [226/650], Train Loss: 0.0138, Train L1 Loss: 0.7827
Epoch [226/650], Validation Loss: 0.0224, Validation L1: 0.9498, Smoothed Validation Loss: 0.0224
Epoch [227/650], Train Loss: 0.0138, Train L1 Loss: 0.7824
Epoch [227/650], Validation Loss: 0.0224, Validation L1: 0.9498, Smoothed Validation Loss: 0.0224
Epoch [228/650], Train Loss: 0.0138, Train L1 Loss: 0.7822
Epoch [228/650], Validation Loss: 0.0224, Validation L1: 0.9498, Smoothed Validation Loss: 0.0224
Epoch [229/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [229/650], Validation Loss: 0.0224, Validation L1: 0.9498, Smoothed Validation Loss: 0.0224
Epoch [230/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [230/650], Validation Loss: 0.0224, Validation L1: 0.9499, Smoothed Validation Loss: 0.0224
Epoch 00230: reducing learning rate of group 0 to 7.8125e-06.
Epoch [231/650], Train Loss: 0.0139, Train L1 Loss: 0.7833
Epoch [231/650], Validation Loss: 0.0223, Validation L1: 0.9502, Smoothed Validation Loss: 0.0224
Epoch [232/650], Train Loss: 0.0138, Train L1 Loss: 0.7825
Epoch [232/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0224
Epoch [233/650], Train Loss: 0.0138, Train L1 Loss: 0.7822
Epoch [233/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0224
Epoch [234/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [234/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [235/650], Train Loss: 0.0138, Train L1 Loss: 0.7818
Epoch [235/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [236/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [236/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [237/650], Train Loss: 0.0138, Train L1 Loss: 0.7814
Epoch [237/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [238/650], Train Loss: 0.0138, Train L1 Loss: 0.7813
Epoch [238/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [239/650], Train Loss: 0.0138, Train L1 Loss: 0.7811
Epoch [239/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [240/650], Train Loss: 0.0138, Train L1 Loss: 0.7809
Epoch [240/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [241/650], Train Loss: 0.0138, Train L1 Loss: 0.7808
Epoch [241/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [242/650], Train Loss: 0.0138, Train L1 Loss: 0.7806
Epoch [242/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [243/650], Train Loss: 0.0138, Train L1 Loss: 0.7804
Epoch [243/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [244/650], Train Loss: 0.0138, Train L1 Loss: 0.7803
Epoch [244/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [245/650], Train Loss: 0.0138, Train L1 Loss: 0.7801
Epoch [245/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [246/650], Train Loss: 0.0137, Train L1 Loss: 0.7800
Epoch [246/650], Validation Loss: 0.0223, Validation L1: 0.9500, Smoothed Validation Loss: 0.0223
Epoch [247/650], Train Loss: 0.0137, Train L1 Loss: 0.7799
Epoch [247/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [248/650], Train Loss: 0.0137, Train L1 Loss: 0.7797
Epoch [248/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [249/650], Train Loss: 0.0137, Train L1 Loss: 0.7796
Epoch [249/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [250/650], Train Loss: 0.0137, Train L1 Loss: 0.7794
Epoch [250/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [251/650], Train Loss: 0.0137, Train L1 Loss: 0.7793
Epoch [251/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [252/650], Train Loss: 0.0137, Train L1 Loss: 0.7792
Epoch [252/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [253/650], Train Loss: 0.0137, Train L1 Loss: 0.7790
Epoch [253/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [254/650], Train Loss: 0.0137, Train L1 Loss: 0.7789
Epoch [254/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [255/650], Train Loss: 0.0137, Train L1 Loss: 0.7788
Epoch [255/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [256/650], Train Loss: 0.0137, Train L1 Loss: 0.7786
Epoch [256/650], Validation Loss: 0.0223, Validation L1: 0.9501, Smoothed Validation Loss: 0.0223
Epoch [257/650], Train Loss: 0.0137, Train L1 Loss: 0.7785
Epoch [257/650], Validation Loss: 0.0223, Validation L1: 0.9502, Smoothed Validation Loss: 0.0223
Epoch [258/650], Train Loss: 0.0137, Train L1 Loss: 0.7784
Epoch [258/650], Validation Loss: 0.0223, Validation L1: 0.9502, Smoothed Validation Loss: 0.0223
Epoch [259/650], Train Loss: 0.0137, Train L1 Loss: 0.7782
Epoch [259/650], Validation Loss: 0.0223, Validation L1: 0.9502, Smoothed Validation Loss: 0.0223
Epoch 00259: reducing learning rate of group 0 to 3.9063e-06.
Epoch [260/650], Train Loss: 0.0137, Train L1 Loss: 0.7792
Epoch [260/650], Validation Loss: 0.0222, Validation L1: 0.9484, Smoothed Validation Loss: 0.0223
Epoch [261/650], Train Loss: 0.0137, Train L1 Loss: 0.7787
Epoch [261/650], Validation Loss: 0.0222, Validation L1: 0.9483, Smoothed Validation Loss: 0.0223
Epoch [262/650], Train Loss: 0.0137, Train L1 Loss: 0.7786
Epoch [262/650], Validation Loss: 0.0222, Validation L1: 0.9482, Smoothed Validation Loss: 0.0223
Epoch [263/650], Train Loss: 0.0137, Train L1 Loss: 0.7784
Epoch [263/650], Validation Loss: 0.0222, Validation L1: 0.9482, Smoothed Validation Loss: 0.0223
Epoch [264/650], Train Loss: 0.0137, Train L1 Loss: 0.7783
Epoch [264/650], Validation Loss: 0.0222, Validation L1: 0.9482, Smoothed Validation Loss: 0.0222
Epoch [265/650], Train Loss: 0.0137, Train L1 Loss: 0.7782
Epoch [265/650], Validation Loss: 0.0222, Validation L1: 0.9482, Smoothed Validation Loss: 0.0222
Epoch [266/650], Train Loss: 0.0137, Train L1 Loss: 0.7781
Epoch [266/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [267/650], Train Loss: 0.0137, Train L1 Loss: 0.7780
Epoch [267/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [268/650], Train Loss: 0.0137, Train L1 Loss: 0.7779
Epoch [268/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [269/650], Train Loss: 0.0137, Train L1 Loss: 0.7778
Epoch [269/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [270/650], Train Loss: 0.0137, Train L1 Loss: 0.7778
Epoch [270/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [271/650], Train Loss: 0.0137, Train L1 Loss: 0.7777
Epoch [271/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [272/650], Train Loss: 0.0137, Train L1 Loss: 0.7776
Epoch [272/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [273/650], Train Loss: 0.0137, Train L1 Loss: 0.7775
Epoch [273/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [274/650], Train Loss: 0.0137, Train L1 Loss: 0.7774
Epoch [274/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [275/650], Train Loss: 0.0137, Train L1 Loss: 0.7773
Epoch [275/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [276/650], Train Loss: 0.0137, Train L1 Loss: 0.7773
Epoch [276/650], Validation Loss: 0.0222, Validation L1: 0.9481, Smoothed Validation Loss: 0.0222
Epoch [277/650], Train Loss: 0.0137, Train L1 Loss: 0.7772
Epoch [277/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [278/650], Train Loss: 0.0137, Train L1 Loss: 0.7771
Epoch [278/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [279/650], Train Loss: 0.0137, Train L1 Loss: 0.7770
Epoch [279/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [280/650], Train Loss: 0.0137, Train L1 Loss: 0.7769
Epoch [280/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [281/650], Train Loss: 0.0137, Train L1 Loss: 0.7769
Epoch [281/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [282/650], Train Loss: 0.0137, Train L1 Loss: 0.7768
Epoch [282/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [283/650], Train Loss: 0.0136, Train L1 Loss: 0.7767
Epoch [283/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [284/650], Train Loss: 0.0136, Train L1 Loss: 0.7766
Epoch [284/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [285/650], Train Loss: 0.0136, Train L1 Loss: 0.7766
Epoch [285/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [286/650], Train Loss: 0.0136, Train L1 Loss: 0.7765
Epoch [286/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [287/650], Train Loss: 0.0136, Train L1 Loss: 0.7764
Epoch [287/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch [288/650], Train Loss: 0.0136, Train L1 Loss: 0.7763
Epoch [288/650], Validation Loss: 0.0222, Validation L1: 0.9480, Smoothed Validation Loss: 0.0222
Epoch 00288: reducing learning rate of group 0 to 1.9531e-06.
Epoch [289/650], Train Loss: 0.0136, Train L1 Loss: 0.7767
Epoch [289/650], Validation Loss: 0.0222, Validation L1: 0.9459, Smoothed Validation Loss: 0.0222
Epoch [290/650], Train Loss: 0.0136, Train L1 Loss: 0.7764
Epoch [290/650], Validation Loss: 0.0222, Validation L1: 0.9458, Smoothed Validation Loss: 0.0222
Epoch [291/650], Train Loss: 0.0136, Train L1 Loss: 0.7763
Epoch [291/650], Validation Loss: 0.0222, Validation L1: 0.9458, Smoothed Validation Loss: 0.0222
Epoch [292/650], Train Loss: 0.0136, Train L1 Loss: 0.7763
Epoch [292/650], Validation Loss: 0.0222, Validation L1: 0.9458, Smoothed Validation Loss: 0.0222
Epoch [293/650], Train Loss: 0.0136, Train L1 Loss: 0.7762
Epoch [293/650], Validation Loss: 0.0222, Validation L1: 0.9458, Smoothed Validation Loss: 0.0222
Epoch [294/650], Train Loss: 0.0136, Train L1 Loss: 0.7762
Epoch [294/650], Validation Loss: 0.0222, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [295/650], Train Loss: 0.0136, Train L1 Loss: 0.7761
Epoch [295/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [296/650], Train Loss: 0.0136, Train L1 Loss: 0.7761
Epoch [296/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [297/650], Train Loss: 0.0136, Train L1 Loss: 0.7760
Epoch [297/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [298/650], Train Loss: 0.0136, Train L1 Loss: 0.7760
Epoch [298/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [299/650], Train Loss: 0.0136, Train L1 Loss: 0.7759
Epoch [299/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [300/650], Train Loss: 0.0136, Train L1 Loss: 0.7759
Epoch [300/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [301/650], Train Loss: 0.0136, Train L1 Loss: 0.7758
Epoch [301/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [302/650], Train Loss: 0.0136, Train L1 Loss: 0.7758
Epoch [302/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [303/650], Train Loss: 0.0136, Train L1 Loss: 0.7758
Epoch [303/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [304/650], Train Loss: 0.0136, Train L1 Loss: 0.7757
Epoch [304/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [305/650], Train Loss: 0.0136, Train L1 Loss: 0.7757
Epoch [305/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [306/650], Train Loss: 0.0136, Train L1 Loss: 0.7756
Epoch [306/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [307/650], Train Loss: 0.0136, Train L1 Loss: 0.7756
Epoch [307/650], Validation Loss: 0.0221, Validation L1: 0.9457, Smoothed Validation Loss: 0.0222
Epoch [308/650], Train Loss: 0.0136, Train L1 Loss: 0.7755
Epoch [308/650], Validation Loss: 0.0221, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch [309/650], Train Loss: 0.0136, Train L1 Loss: 0.7755
Epoch [309/650], Validation Loss: 0.0221, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch [310/650], Train Loss: 0.0136, Train L1 Loss: 0.7755
Epoch [310/650], Validation Loss: 0.0221, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch [311/650], Train Loss: 0.0136, Train L1 Loss: 0.7754
Epoch [311/650], Validation Loss: 0.0221, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch [312/650], Train Loss: 0.0136, Train L1 Loss: 0.7754
Epoch [312/650], Validation Loss: 0.0222, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch [313/650], Train Loss: 0.0136, Train L1 Loss: 0.7753
Epoch [313/650], Validation Loss: 0.0222, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch [314/650], Train Loss: 0.0136, Train L1 Loss: 0.7753
Epoch [314/650], Validation Loss: 0.0222, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch [315/650], Train Loss: 0.0136, Train L1 Loss: 0.7753
Epoch [315/650], Validation Loss: 0.0222, Validation L1: 0.9456, Smoothed Validation Loss: 0.0222
Epoch 00315: reducing learning rate of group 0 to 9.7656e-07.
Epoch [316/650], Train Loss: 0.0136, Train L1 Loss: 0.7754
Epoch [316/650], Validation Loss: 0.0221, Validation L1: 0.9444, Smoothed Validation Loss: 0.0222
Epoch [317/650], Train Loss: 0.0136, Train L1 Loss: 0.7752
Epoch [317/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [318/650], Train Loss: 0.0136, Train L1 Loss: 0.7751
Epoch [318/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [319/650], Train Loss: 0.0136, Train L1 Loss: 0.7751
Epoch [319/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [320/650], Train Loss: 0.0136, Train L1 Loss: 0.7750
Epoch [320/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [321/650], Train Loss: 0.0136, Train L1 Loss: 0.7750
Epoch [321/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [322/650], Train Loss: 0.0136, Train L1 Loss: 0.7750
Epoch [322/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [323/650], Train Loss: 0.0136, Train L1 Loss: 0.7750
Epoch [323/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [324/650], Train Loss: 0.0136, Train L1 Loss: 0.7749
Epoch [324/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [325/650], Train Loss: 0.0136, Train L1 Loss: 0.7749
Epoch [325/650], Validation Loss: 0.0221, Validation L1: 0.9443, Smoothed Validation Loss: 0.0221
Epoch [326/650], Train Loss: 0.0136, Train L1 Loss: 0.7749
Epoch [326/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [327/650], Train Loss: 0.0136, Train L1 Loss: 0.7749
Epoch [327/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [328/650], Train Loss: 0.0136, Train L1 Loss: 0.7749
Epoch [328/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [329/650], Train Loss: 0.0136, Train L1 Loss: 0.7748
Epoch [329/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [330/650], Train Loss: 0.0136, Train L1 Loss: 0.7748
Epoch [330/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [331/650], Train Loss: 0.0136, Train L1 Loss: 0.7748
Epoch [331/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [332/650], Train Loss: 0.0136, Train L1 Loss: 0.7748
Epoch [332/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [333/650], Train Loss: 0.0136, Train L1 Loss: 0.7747
Epoch [333/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [334/650], Train Loss: 0.0136, Train L1 Loss: 0.7747
Epoch [334/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [335/650], Train Loss: 0.0136, Train L1 Loss: 0.7747
Epoch [335/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [336/650], Train Loss: 0.0136, Train L1 Loss: 0.7747
Epoch [336/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [337/650], Train Loss: 0.0136, Train L1 Loss: 0.7747
Epoch [337/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [338/650], Train Loss: 0.0136, Train L1 Loss: 0.7746
Epoch [338/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch [339/650], Train Loss: 0.0136, Train L1 Loss: 0.7746
Epoch [339/650], Validation Loss: 0.0221, Validation L1: 0.9442, Smoothed Validation Loss: 0.0221
Epoch 00339: reducing learning rate of group 0 to 4.8828e-07.
Epoch [340/650], Train Loss: 0.0136, Train L1 Loss: 0.7746
Epoch [340/650], Validation Loss: 0.0221, Validation L1: 0.9438, Smoothed Validation Loss: 0.0221
Epoch [341/650], Train Loss: 0.0136, Train L1 Loss: 0.7745
Epoch [341/650], Validation Loss: 0.0221, Validation L1: 0.9438, Smoothed Validation Loss: 0.0221
Epoch [342/650], Train Loss: 0.0136, Train L1 Loss: 0.7745
Epoch [342/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [343/650], Train Loss: 0.0136, Train L1 Loss: 0.7745
Epoch [343/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [344/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [344/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [345/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [345/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [346/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [346/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [347/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [347/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [348/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [348/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [349/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [349/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [350/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [350/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [351/650], Train Loss: 0.0136, Train L1 Loss: 0.7744
Epoch [351/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [352/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [352/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [353/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [353/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [354/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [354/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [355/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [355/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [356/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [356/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [357/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [357/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [358/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [358/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [359/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [359/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [360/650], Train Loss: 0.0136, Train L1 Loss: 0.7743
Epoch [360/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [361/650], Train Loss: 0.0136, Train L1 Loss: 0.7742
Epoch [361/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [362/650], Train Loss: 0.0136, Train L1 Loss: 0.7742
Epoch [362/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch 00362: reducing learning rate of group 0 to 2.4414e-07.
Epoch [363/650], Train Loss: 0.0136, Train L1 Loss: 0.7742
Epoch [363/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [364/650], Train Loss: 0.0136, Train L1 Loss: 0.7742
Epoch [364/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [365/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [365/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [366/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [366/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [367/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [367/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [368/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [368/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [369/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [369/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [370/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [370/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [371/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [371/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [372/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [372/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [373/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [373/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [374/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [374/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [375/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [375/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [376/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [376/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [377/650], Train Loss: 0.0136, Train L1 Loss: 0.7741
Epoch [377/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch 00377: reducing learning rate of group 0 to 1.2207e-07.
Epoch [378/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [378/650], Validation Loss: 0.0221, Validation L1: 0.9437, Smoothed Validation Loss: 0.0221
Epoch [379/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [379/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [380/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [380/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [381/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [381/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [382/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [382/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [383/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [383/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [384/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [384/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [385/650], Train Loss: 0.0136, Train L1 Loss: 0.7740
Epoch [385/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch 00385: reducing learning rate of group 0 to 6.1035e-08.
Epoch [386/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [386/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [387/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [387/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [388/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [388/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [389/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [389/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [390/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [390/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [391/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [391/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [392/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [392/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [393/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [393/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [394/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [394/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch 00394: reducing learning rate of group 0 to 3.0518e-08.
Epoch [395/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [395/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [396/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [396/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [397/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [397/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [398/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [398/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [399/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [399/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [400/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [400/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch 00400: reducing learning rate of group 0 to 1.5259e-08.
Epoch [401/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [401/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [402/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [402/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [403/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [403/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [404/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [404/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [405/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [405/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [406/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [406/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [407/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [407/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [408/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [408/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [409/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [409/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [410/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [410/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [411/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [411/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [412/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [412/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [413/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [413/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [414/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [414/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [415/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [415/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [416/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [416/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [417/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [417/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [418/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [418/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [419/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [419/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [420/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [420/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [421/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [421/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [422/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [422/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [423/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [423/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [424/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [424/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [425/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [425/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [426/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [426/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [427/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [427/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [428/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [428/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [429/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [429/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [430/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [430/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [431/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [431/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [432/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [432/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [433/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [433/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [434/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [434/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [435/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [435/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [436/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [436/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [437/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [437/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [438/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [438/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [439/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [439/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [440/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [440/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [441/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [441/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [442/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [442/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [443/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [443/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [444/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [444/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [445/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [445/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [446/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [446/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [447/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [447/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [448/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [448/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [449/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [449/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [450/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [450/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [451/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [451/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [452/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [452/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [453/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [453/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [454/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [454/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [455/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [455/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [456/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [456/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [457/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [457/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [458/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [458/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [459/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [459/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [460/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [460/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [461/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [461/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [462/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [462/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [463/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [463/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [464/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [464/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [465/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [465/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [466/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [466/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [467/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [467/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [468/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [468/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [469/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [469/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [470/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [470/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [471/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [471/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [472/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [472/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [473/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [473/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [474/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [474/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [475/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [475/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [476/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [476/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [477/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [477/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [478/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [478/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [479/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [479/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [480/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [480/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [481/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [481/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [482/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [482/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [483/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [483/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [484/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [484/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [485/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [485/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [486/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [486/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [487/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [487/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [488/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [488/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [489/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [489/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [490/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [490/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [491/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [491/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [492/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [492/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [493/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [493/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [494/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [494/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [495/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [495/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [496/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [496/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [497/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [497/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [498/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [498/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [499/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [499/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [500/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [500/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [501/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [501/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [502/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [502/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [503/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [503/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [504/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [504/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [505/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [505/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [506/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [506/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [507/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [507/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [508/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [508/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [509/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [509/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [510/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [510/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [511/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [511/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [512/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [512/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [513/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [513/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [514/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [514/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [515/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [515/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [516/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [516/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [517/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [517/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [518/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [518/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [519/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [519/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [520/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [520/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [521/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [521/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [522/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [522/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [523/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [523/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [524/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [524/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [525/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [525/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [526/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [526/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [527/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [527/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [528/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [528/650], Validation Loss: 0.0221, Validation L1: 0.9436, Smoothed Validation Loss: 0.0221
Epoch [529/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [529/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [530/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [530/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [531/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [531/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [532/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [532/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [533/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [533/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [534/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [534/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [535/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [535/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [536/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [536/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [537/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [537/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [538/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [538/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [539/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [539/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [540/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [540/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [541/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [541/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [542/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [542/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [543/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [543/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [544/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [544/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [545/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [545/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [546/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [546/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [547/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [547/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [548/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [548/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [549/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [549/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [550/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [550/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [551/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [551/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [552/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [552/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [553/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [553/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [554/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [554/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [555/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [555/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [556/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [556/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [557/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [557/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [558/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [558/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [559/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [559/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [560/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [560/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [561/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [561/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [562/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [562/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [563/650], Train Loss: 0.0136, Train L1 Loss: 0.7739
Epoch [563/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [564/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [564/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [565/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [565/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [566/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [566/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [567/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [567/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [568/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [568/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [569/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [569/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [570/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [570/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [571/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [571/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [572/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [572/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [573/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [573/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [574/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [574/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [575/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [575/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [576/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [576/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [577/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [577/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [578/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [578/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [579/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [579/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [580/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [580/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [581/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [581/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [582/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [582/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [583/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [583/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [584/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [584/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [585/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [585/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [586/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [586/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [587/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [587/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [588/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [588/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [589/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [589/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [590/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [590/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [591/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [591/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [592/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [592/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [593/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [593/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [594/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [594/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [595/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [595/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [596/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [596/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [597/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [597/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [598/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [598/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [599/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [599/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [600/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [600/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [601/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [601/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [602/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [602/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [603/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [603/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [604/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [604/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [605/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [605/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [606/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [606/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [607/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [607/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [608/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [608/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [609/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [609/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [610/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [610/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [611/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [611/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [612/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [612/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [613/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [613/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [614/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [614/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [615/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [615/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [616/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [616/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [617/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [617/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [618/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [618/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [619/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [619/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [620/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [620/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [621/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [621/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [622/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [622/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [623/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [623/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [624/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [624/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [625/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [625/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [626/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [626/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [627/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [627/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [628/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [628/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [629/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [629/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [630/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [630/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [631/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [631/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [632/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [632/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [633/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [633/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [634/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [634/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [635/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [635/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [636/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [636/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [637/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [637/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [638/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [638/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [639/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [639/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [640/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [640/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [641/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [641/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [642/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [642/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [643/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [643/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [644/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [644/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [645/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [645/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [646/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [646/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [647/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [647/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [648/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [648/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [649/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [649/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
Epoch [650/650], Train Loss: 0.0136, Train L1 Loss: 0.7738
Epoch [650/650], Validation Loss: 0.0221, Validation L1: 0.9435, Smoothed Validation Loss: 0.0221
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19630794: <WorkingSetup_0> in cluster <dcc> Done

Job <WorkingSetup_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 13:59:43 2023
Job was executed on host(s) <4*n-62-18-11>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Thu Nov 30 16:58:59 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Thu Nov 30 16:58:59 2023
Terminated at Fri Dec  1 04:27:09 2023
Results reported at Fri Dec  1 04:27:09 2023

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

Successfully completed.

Resource usage summary:

    CPU time :                                   41665.84 sec.
    Max Memory :                                 1956 MB
    Average Memory :                             1940.46 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63580.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   41291 sec.
    Turnaround time :                            52046 sec.

The output (if any) is above this job summary.

