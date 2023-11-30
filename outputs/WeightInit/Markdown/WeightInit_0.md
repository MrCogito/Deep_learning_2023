
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
| <c>name</c>       | <d>str</d>        | <j>"WeightInit-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>1000</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>32</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |

# Output

```
wandb: Currently logged in as: chessproject65. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231129_110443-4auhl76b
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run WeightInit-0
wandb: ⭐️ View project at https://wandb.ai/chessproject65/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/chessproject65/deeplearning_painn/runs/4auhl76b
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:04:57,788] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7f2d3d217a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:02,925] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmp__c82z33.py line 218 
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:09,399] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmp__c82z33.py line 117 
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:09,940] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmp__c82z33.py line 90 
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:10,075] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:10,610] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:13,240] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:14,310] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] 
[2023-11-29 11:05:15,440] torch._dynamo.convert_frame: [WARNING] 
User defined signal 2

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19591965: <WeightInit_0> in cluster <dcc> Exited

Job <WeightInit_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Tue Nov 28 19:17:27 2023
Job was executed on host(s) <4*n-62-18-13>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Wed Nov 29 11:02:54 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Wed Nov 29 11:02:54 2023
Terminated at Thu Nov 30 11:03:35 2023
Results reported at Thu Nov 30 11:03:35 2023

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

TERM_RUNLIMIT: job killed after reaching LSF run time limit.
Exited with exit code 140.

Resource usage summary:

    CPU time :                                   87241.00 sec.
    Max Memory :                                 1953 MB
    Average Memory :                             1932.04 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63583.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   86442 sec.
    Turnaround time :                            143168 sec.

The output (if any) is above this job summary.

