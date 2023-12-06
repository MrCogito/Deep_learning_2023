
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
| <c>name</c>       | <d>str</d>        | <j>"11WorkingSetup-0"</j> |
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
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231203_145317-2p7wv8km
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 11WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/2p7wv8km
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:32,330] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7fdd16a5ca40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:36,262] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpn7kosy45.py line 218 
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:43,564] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpn7kosy45.py line 117 
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,114] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpn7kosy45.py line 90 
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,264] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:44,887] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:47,333] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:48,492] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] 
[2023-12-03 14:53:49,644] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.007 MB uploadedwandb: / 0.006 MB of 0.117 MB uploadedwandb: - 0.006 MB of 0.117 MB uploadedwandb: \ 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▅▃▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▅▅▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▄▅▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▃▅▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.00168
wandb:     train l1 loss 0.19627
wandb:        train_loss 0.00085
wandb:       val l1 loss 0.26731
wandb:          val loss 0.00168
wandb: 
wandb: 🚀 View run 11WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/2p7wv8km
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231203_145317-2p7wv8km/logs
Epoch [1/650], Train Loss: 0.0401, Train L1 Loss: 0.6424
Epoch [1/650], Validation Loss: 0.0063, Validation L1: 0.5663, Smoothed Validation Loss: 0.0063
Epoch [2/650], Train Loss: 0.0043, Train L1 Loss: 0.4368
Epoch [2/650], Validation Loss: 0.0068, Validation L1: 0.6030, Smoothed Validation Loss: 0.0064
Epoch [3/650], Train Loss: 0.0040, Train L1 Loss: 0.4215
Epoch [3/650], Validation Loss: 0.0065, Validation L1: 0.5928, Smoothed Validation Loss: 0.0064
Epoch [4/650], Train Loss: 0.0035, Train L1 Loss: 0.3932
Epoch [4/650], Validation Loss: 0.0050, Validation L1: 0.5100, Smoothed Validation Loss: 0.0062
Epoch [5/650], Train Loss: 0.0031, Train L1 Loss: 0.3731
Epoch [5/650], Validation Loss: 0.0040, Validation L1: 0.4416, Smoothed Validation Loss: 0.0060
Epoch [6/650], Train Loss: 0.0029, Train L1 Loss: 0.3586
Epoch [6/650], Validation Loss: 0.0028, Validation L1: 0.3565, Smoothed Validation Loss: 0.0057
Epoch [7/650], Train Loss: 0.0026, Train L1 Loss: 0.3459
Epoch [7/650], Validation Loss: 0.0024, Validation L1: 0.3306, Smoothed Validation Loss: 0.0054
Epoch [8/650], Train Loss: 0.0025, Train L1 Loss: 0.3395
Epoch [8/650], Validation Loss: 0.0023, Validation L1: 0.3221, Smoothed Validation Loss: 0.0051
Epoch [9/650], Train Loss: 0.0025, Train L1 Loss: 0.3353
Epoch [9/650], Validation Loss: 0.0023, Validation L1: 0.3192, Smoothed Validation Loss: 0.0048
Epoch [10/650], Train Loss: 0.0024, Train L1 Loss: 0.3300
Epoch [10/650], Validation Loss: 0.0022, Validation L1: 0.3124, Smoothed Validation Loss: 0.0045
Epoch [11/650], Train Loss: 0.0024, Train L1 Loss: 0.3263
Epoch [11/650], Validation Loss: 0.0023, Validation L1: 0.3150, Smoothed Validation Loss: 0.0043
Epoch [12/650], Train Loss: 0.0023, Train L1 Loss: 0.3239
Epoch [12/650], Validation Loss: 0.0023, Validation L1: 0.3165, Smoothed Validation Loss: 0.0041
Epoch [13/650], Train Loss: 0.0023, Train L1 Loss: 0.3204
Epoch [13/650], Validation Loss: 0.0022, Validation L1: 0.3135, Smoothed Validation Loss: 0.0039
Epoch [14/650], Train Loss: 0.0022, Train L1 Loss: 0.3151
Epoch [14/650], Validation Loss: 0.0020, Validation L1: 0.3015, Smoothed Validation Loss: 0.0037
Epoch [15/650], Train Loss: 0.0021, Train L1 Loss: 0.3113
Epoch [15/650], Validation Loss: 0.0020, Validation L1: 0.3015, Smoothed Validation Loss: 0.0036
Epoch [16/650], Train Loss: 0.0021, Train L1 Loss: 0.3096
Epoch [16/650], Validation Loss: 0.0021, Validation L1: 0.3044, Smoothed Validation Loss: 0.0034
Epoch [17/650], Train Loss: 0.0021, Train L1 Loss: 0.3070
Epoch [17/650], Validation Loss: 0.0020, Validation L1: 0.2952, Smoothed Validation Loss: 0.0033
Epoch [18/650], Train Loss: 0.0020, Train L1 Loss: 0.3030
Epoch [18/650], Validation Loss: 0.0020, Validation L1: 0.2940, Smoothed Validation Loss: 0.0031
Epoch [19/650], Train Loss: 0.0020, Train L1 Loss: 0.3015
Epoch [19/650], Validation Loss: 0.0019, Validation L1: 0.2924, Smoothed Validation Loss: 0.0030
Epoch [20/650], Train Loss: 0.0020, Train L1 Loss: 0.3024
Epoch [20/650], Validation Loss: 0.0019, Validation L1: 0.2882, Smoothed Validation Loss: 0.0029
Epoch [21/650], Train Loss: 0.0020, Train L1 Loss: 0.2978
Epoch [21/650], Validation Loss: 0.0019, Validation L1: 0.2910, Smoothed Validation Loss: 0.0028
Epoch [22/650], Train Loss: 0.0019, Train L1 Loss: 0.2950
Epoch [22/650], Validation Loss: 0.0019, Validation L1: 0.2917, Smoothed Validation Loss: 0.0027
Epoch [23/650], Train Loss: 0.0019, Train L1 Loss: 0.2929
Epoch [23/650], Validation Loss: 0.0018, Validation L1: 0.2846, Smoothed Validation Loss: 0.0026
Epoch [24/650], Train Loss: 0.0019, Train L1 Loss: 0.2919
Epoch [24/650], Validation Loss: 0.0019, Validation L1: 0.2920, Smoothed Validation Loss: 0.0025
Epoch [25/650], Train Loss: 0.0019, Train L1 Loss: 0.2911
Epoch [25/650], Validation Loss: 0.0019, Validation L1: 0.2899, Smoothed Validation Loss: 0.0025
Epoch [26/650], Train Loss: 0.0018, Train L1 Loss: 0.2891
Epoch [26/650], Validation Loss: 0.0019, Validation L1: 0.2996, Smoothed Validation Loss: 0.0024
Epoch [27/650], Train Loss: 0.0018, Train L1 Loss: 0.2879
Epoch [27/650], Validation Loss: 0.0019, Validation L1: 0.2918, Smoothed Validation Loss: 0.0024
Epoch [28/650], Train Loss: 0.0018, Train L1 Loss: 0.2892
Epoch [28/650], Validation Loss: 0.0019, Validation L1: 0.2896, Smoothed Validation Loss: 0.0023
Epoch [29/650], Train Loss: 0.0018, Train L1 Loss: 0.2862
Epoch [29/650], Validation Loss: 0.0018, Validation L1: 0.2880, Smoothed Validation Loss: 0.0023
Epoch [30/650], Train Loss: 0.0018, Train L1 Loss: 0.2835
Epoch [30/650], Validation Loss: 0.0019, Validation L1: 0.2877, Smoothed Validation Loss: 0.0022
Epoch [31/650], Train Loss: 0.0018, Train L1 Loss: 0.2835
Epoch [31/650], Validation Loss: 0.0019, Validation L1: 0.2928, Smoothed Validation Loss: 0.0022
Epoch [32/650], Train Loss: 0.0017, Train L1 Loss: 0.2826
Epoch [32/650], Validation Loss: 0.0019, Validation L1: 0.2876, Smoothed Validation Loss: 0.0022
Epoch [33/650], Train Loss: 0.0017, Train L1 Loss: 0.2809
Epoch [33/650], Validation Loss: 0.0019, Validation L1: 0.2887, Smoothed Validation Loss: 0.0021
Epoch [34/650], Train Loss: 0.0017, Train L1 Loss: 0.2807
Epoch [34/650], Validation Loss: 0.0019, Validation L1: 0.2959, Smoothed Validation Loss: 0.0021
Epoch [35/650], Train Loss: 0.0017, Train L1 Loss: 0.2799
Epoch [35/650], Validation Loss: 0.0019, Validation L1: 0.2955, Smoothed Validation Loss: 0.0021
Epoch [36/650], Train Loss: 0.0017, Train L1 Loss: 0.2787
Epoch [36/650], Validation Loss: 0.0019, Validation L1: 0.2870, Smoothed Validation Loss: 0.0021
Epoch [37/650], Train Loss: 0.0017, Train L1 Loss: 0.2781
Epoch [37/650], Validation Loss: 0.0019, Validation L1: 0.2947, Smoothed Validation Loss: 0.0021
Epoch [38/650], Train Loss: 0.0017, Train L1 Loss: 0.2781
Epoch [38/650], Validation Loss: 0.0018, Validation L1: 0.2816, Smoothed Validation Loss: 0.0020
Epoch [39/650], Train Loss: 0.0017, Train L1 Loss: 0.2766
Epoch [39/650], Validation Loss: 0.0021, Validation L1: 0.3158, Smoothed Validation Loss: 0.0020
Epoch [40/650], Train Loss: 0.0017, Train L1 Loss: 0.2785
Epoch [40/650], Validation Loss: 0.0020, Validation L1: 0.2984, Smoothed Validation Loss: 0.0020
Epoch [41/650], Train Loss: 0.0017, Train L1 Loss: 0.2785
Epoch [41/650], Validation Loss: 0.0021, Validation L1: 0.3169, Smoothed Validation Loss: 0.0020
Epoch [42/650], Train Loss: 0.0016, Train L1 Loss: 0.2738
Epoch [42/650], Validation Loss: 0.0020, Validation L1: 0.3057, Smoothed Validation Loss: 0.0020
Epoch [43/650], Train Loss: 0.0016, Train L1 Loss: 0.2732
Epoch [43/650], Validation Loss: 0.0020, Validation L1: 0.3081, Smoothed Validation Loss: 0.0020
Epoch [44/650], Train Loss: 0.0016, Train L1 Loss: 0.2740
Epoch [44/650], Validation Loss: 0.0023, Validation L1: 0.3282, Smoothed Validation Loss: 0.0021
Epoch 00044: reducing learning rate of group 0 to 5.0000e-04.
Epoch [45/650], Train Loss: 0.0015, Train L1 Loss: 0.2579
Epoch [45/650], Validation Loss: 0.0018, Validation L1: 0.2837, Smoothed Validation Loss: 0.0020
Epoch [46/650], Train Loss: 0.0014, Train L1 Loss: 0.2546
Epoch [46/650], Validation Loss: 0.0019, Validation L1: 0.2877, Smoothed Validation Loss: 0.0020
Epoch [47/650], Train Loss: 0.0014, Train L1 Loss: 0.2531
Epoch [47/650], Validation Loss: 0.0019, Validation L1: 0.2875, Smoothed Validation Loss: 0.0020
Epoch [48/650], Train Loss: 0.0014, Train L1 Loss: 0.2516
Epoch [48/650], Validation Loss: 0.0019, Validation L1: 0.2859, Smoothed Validation Loss: 0.0020
Epoch [49/650], Train Loss: 0.0014, Train L1 Loss: 0.2503
Epoch [49/650], Validation Loss: 0.0019, Validation L1: 0.2884, Smoothed Validation Loss: 0.0020
Epoch [50/650], Train Loss: 0.0013, Train L1 Loss: 0.2493
Epoch [50/650], Validation Loss: 0.0018, Validation L1: 0.2839, Smoothed Validation Loss: 0.0020
Epoch [51/650], Train Loss: 0.0013, Train L1 Loss: 0.2484
Epoch [51/650], Validation Loss: 0.0018, Validation L1: 0.2802, Smoothed Validation Loss: 0.0020
Epoch [52/650], Train Loss: 0.0013, Train L1 Loss: 0.2472
Epoch [52/650], Validation Loss: 0.0018, Validation L1: 0.2805, Smoothed Validation Loss: 0.0019
Epoch [53/650], Train Loss: 0.0013, Train L1 Loss: 0.2470
Epoch [53/650], Validation Loss: 0.0018, Validation L1: 0.2796, Smoothed Validation Loss: 0.0019
Epoch [54/650], Train Loss: 0.0013, Train L1 Loss: 0.2454
Epoch [54/650], Validation Loss: 0.0018, Validation L1: 0.2801, Smoothed Validation Loss: 0.0019
Epoch [55/650], Train Loss: 0.0013, Train L1 Loss: 0.2452
Epoch [55/650], Validation Loss: 0.0018, Validation L1: 0.2808, Smoothed Validation Loss: 0.0019
Epoch [56/650], Train Loss: 0.0013, Train L1 Loss: 0.2461
Epoch [56/650], Validation Loss: 0.0018, Validation L1: 0.2784, Smoothed Validation Loss: 0.0019
Epoch [57/650], Train Loss: 0.0013, Train L1 Loss: 0.2438
Epoch [57/650], Validation Loss: 0.0018, Validation L1: 0.2814, Smoothed Validation Loss: 0.0019
Epoch [58/650], Train Loss: 0.0013, Train L1 Loss: 0.2431
Epoch [58/650], Validation Loss: 0.0018, Validation L1: 0.2821, Smoothed Validation Loss: 0.0019
Epoch [59/650], Train Loss: 0.0013, Train L1 Loss: 0.2424
Epoch [59/650], Validation Loss: 0.0018, Validation L1: 0.2829, Smoothed Validation Loss: 0.0019
Epoch [60/650], Train Loss: 0.0013, Train L1 Loss: 0.2422
Epoch [60/650], Validation Loss: 0.0018, Validation L1: 0.2812, Smoothed Validation Loss: 0.0019
Epoch [61/650], Train Loss: 0.0013, Train L1 Loss: 0.2421
Epoch [61/650], Validation Loss: 0.0018, Validation L1: 0.2787, Smoothed Validation Loss: 0.0018
Epoch [62/650], Train Loss: 0.0012, Train L1 Loss: 0.2418
Epoch [62/650], Validation Loss: 0.0018, Validation L1: 0.2784, Smoothed Validation Loss: 0.0018
Epoch [63/650], Train Loss: 0.0012, Train L1 Loss: 0.2415
Epoch [63/650], Validation Loss: 0.0018, Validation L1: 0.2789, Smoothed Validation Loss: 0.0018
Epoch [64/650], Train Loss: 0.0012, Train L1 Loss: 0.2408
Epoch [64/650], Validation Loss: 0.0018, Validation L1: 0.2797, Smoothed Validation Loss: 0.0018
Epoch [65/650], Train Loss: 0.0012, Train L1 Loss: 0.2405
Epoch [65/650], Validation Loss: 0.0018, Validation L1: 0.2786, Smoothed Validation Loss: 0.0018
Epoch [66/650], Train Loss: 0.0012, Train L1 Loss: 0.2393
Epoch [66/650], Validation Loss: 0.0018, Validation L1: 0.2809, Smoothed Validation Loss: 0.0018
Epoch [67/650], Train Loss: 0.0012, Train L1 Loss: 0.2404
Epoch [67/650], Validation Loss: 0.0018, Validation L1: 0.2804, Smoothed Validation Loss: 0.0018
Epoch [68/650], Train Loss: 0.0012, Train L1 Loss: 0.2386
Epoch [68/650], Validation Loss: 0.0018, Validation L1: 0.2812, Smoothed Validation Loss: 0.0018
Epoch [69/650], Train Loss: 0.0012, Train L1 Loss: 0.2381
Epoch [69/650], Validation Loss: 0.0018, Validation L1: 0.2789, Smoothed Validation Loss: 0.0018
Epoch [70/650], Train Loss: 0.0012, Train L1 Loss: 0.2393
Epoch [70/650], Validation Loss: 0.0018, Validation L1: 0.2774, Smoothed Validation Loss: 0.0018
Epoch [71/650], Train Loss: 0.0012, Train L1 Loss: 0.2388
Epoch [71/650], Validation Loss: 0.0018, Validation L1: 0.2802, Smoothed Validation Loss: 0.0018
Epoch [72/650], Train Loss: 0.0012, Train L1 Loss: 0.2374
Epoch [72/650], Validation Loss: 0.0018, Validation L1: 0.2775, Smoothed Validation Loss: 0.0018
Epoch [73/650], Train Loss: 0.0012, Train L1 Loss: 0.2364
Epoch [73/650], Validation Loss: 0.0018, Validation L1: 0.2774, Smoothed Validation Loss: 0.0018
Epoch [74/650], Train Loss: 0.0012, Train L1 Loss: 0.2372
Epoch [74/650], Validation Loss: 0.0018, Validation L1: 0.2805, Smoothed Validation Loss: 0.0018
Epoch [75/650], Train Loss: 0.0012, Train L1 Loss: 0.2378
Epoch [75/650], Validation Loss: 0.0018, Validation L1: 0.2787, Smoothed Validation Loss: 0.0018
Epoch [76/650], Train Loss: 0.0012, Train L1 Loss: 0.2368
Epoch [76/650], Validation Loss: 0.0019, Validation L1: 0.2838, Smoothed Validation Loss: 0.0018
Epoch [77/650], Train Loss: 0.0012, Train L1 Loss: 0.2360
Epoch [77/650], Validation Loss: 0.0019, Validation L1: 0.2846, Smoothed Validation Loss: 0.0018
Epoch [78/650], Train Loss: 0.0012, Train L1 Loss: 0.2369
Epoch [78/650], Validation Loss: 0.0020, Validation L1: 0.2934, Smoothed Validation Loss: 0.0018
Epoch [79/650], Train Loss: 0.0012, Train L1 Loss: 0.2356
Epoch [79/650], Validation Loss: 0.0019, Validation L1: 0.2861, Smoothed Validation Loss: 0.0018
Epoch 00079: reducing learning rate of group 0 to 2.5000e-04.
Epoch [80/650], Train Loss: 0.0011, Train L1 Loss: 0.2319
Epoch [80/650], Validation Loss: 0.0017, Validation L1: 0.2747, Smoothed Validation Loss: 0.0018
Epoch [81/650], Train Loss: 0.0011, Train L1 Loss: 0.2279
Epoch [81/650], Validation Loss: 0.0017, Validation L1: 0.2754, Smoothed Validation Loss: 0.0018
Epoch [82/650], Train Loss: 0.0011, Train L1 Loss: 0.2258
Epoch [82/650], Validation Loss: 0.0017, Validation L1: 0.2757, Smoothed Validation Loss: 0.0018
Epoch [83/650], Train Loss: 0.0011, Train L1 Loss: 0.2245
Epoch [83/650], Validation Loss: 0.0017, Validation L1: 0.2757, Smoothed Validation Loss: 0.0018
Epoch [84/650], Train Loss: 0.0011, Train L1 Loss: 0.2233
Epoch [84/650], Validation Loss: 0.0017, Validation L1: 0.2758, Smoothed Validation Loss: 0.0018
Epoch [85/650], Train Loss: 0.0011, Train L1 Loss: 0.2223
Epoch [85/650], Validation Loss: 0.0017, Validation L1: 0.2759, Smoothed Validation Loss: 0.0018
Epoch [86/650], Train Loss: 0.0010, Train L1 Loss: 0.2216
Epoch [86/650], Validation Loss: 0.0017, Validation L1: 0.2760, Smoothed Validation Loss: 0.0018
Epoch [87/650], Train Loss: 0.0010, Train L1 Loss: 0.2209
Epoch [87/650], Validation Loss: 0.0017, Validation L1: 0.2759, Smoothed Validation Loss: 0.0018
Epoch [88/650], Train Loss: 0.0010, Train L1 Loss: 0.2206
Epoch [88/650], Validation Loss: 0.0017, Validation L1: 0.2765, Smoothed Validation Loss: 0.0018
Epoch [89/650], Train Loss: 0.0010, Train L1 Loss: 0.2198
Epoch [89/650], Validation Loss: 0.0017, Validation L1: 0.2764, Smoothed Validation Loss: 0.0018
Epoch [90/650], Train Loss: 0.0010, Train L1 Loss: 0.2195
Epoch [90/650], Validation Loss: 0.0018, Validation L1: 0.2771, Smoothed Validation Loss: 0.0018
Epoch [91/650], Train Loss: 0.0010, Train L1 Loss: 0.2190
Epoch [91/650], Validation Loss: 0.0017, Validation L1: 0.2771, Smoothed Validation Loss: 0.0018
Epoch [92/650], Train Loss: 0.0010, Train L1 Loss: 0.2187
Epoch [92/650], Validation Loss: 0.0018, Validation L1: 0.2786, Smoothed Validation Loss: 0.0018
Epoch [93/650], Train Loss: 0.0010, Train L1 Loss: 0.2184
Epoch [93/650], Validation Loss: 0.0018, Validation L1: 0.2792, Smoothed Validation Loss: 0.0018
Epoch [94/650], Train Loss: 0.0010, Train L1 Loss: 0.2180
Epoch [94/650], Validation Loss: 0.0018, Validation L1: 0.2782, Smoothed Validation Loss: 0.0018
Epoch [95/650], Train Loss: 0.0010, Train L1 Loss: 0.2172
Epoch [95/650], Validation Loss: 0.0018, Validation L1: 0.2796, Smoothed Validation Loss: 0.0018
Epoch [96/650], Train Loss: 0.0010, Train L1 Loss: 0.2164
Epoch [96/650], Validation Loss: 0.0018, Validation L1: 0.2799, Smoothed Validation Loss: 0.0018
Epoch [97/650], Train Loss: 0.0010, Train L1 Loss: 0.2163
Epoch [97/650], Validation Loss: 0.0018, Validation L1: 0.2794, Smoothed Validation Loss: 0.0018
Epoch 00097: reducing learning rate of group 0 to 1.2500e-04.
Epoch [98/650], Train Loss: 0.0010, Train L1 Loss: 0.2190
Epoch [98/650], Validation Loss: 0.0017, Validation L1: 0.2760, Smoothed Validation Loss: 0.0018
Epoch [99/650], Train Loss: 0.0010, Train L1 Loss: 0.2163
Epoch [99/650], Validation Loss: 0.0017, Validation L1: 0.2760, Smoothed Validation Loss: 0.0018
Epoch [100/650], Train Loss: 0.0010, Train L1 Loss: 0.2146
Epoch [100/650], Validation Loss: 0.0017, Validation L1: 0.2761, Smoothed Validation Loss: 0.0018
Epoch [101/650], Train Loss: 0.0010, Train L1 Loss: 0.2134
Epoch [101/650], Validation Loss: 0.0017, Validation L1: 0.2766, Smoothed Validation Loss: 0.0018
Epoch [102/650], Train Loss: 0.0010, Train L1 Loss: 0.2125
Epoch [102/650], Validation Loss: 0.0018, Validation L1: 0.2767, Smoothed Validation Loss: 0.0018
Epoch [103/650], Train Loss: 0.0010, Train L1 Loss: 0.2118
Epoch [103/650], Validation Loss: 0.0018, Validation L1: 0.2772, Smoothed Validation Loss: 0.0018
Epoch [104/650], Train Loss: 0.0010, Train L1 Loss: 0.2111
Epoch [104/650], Validation Loss: 0.0018, Validation L1: 0.2772, Smoothed Validation Loss: 0.0018
Epoch [105/650], Train Loss: 0.0009, Train L1 Loss: 0.2104
Epoch [105/650], Validation Loss: 0.0018, Validation L1: 0.2777, Smoothed Validation Loss: 0.0018
Epoch [106/650], Train Loss: 0.0009, Train L1 Loss: 0.2098
Epoch [106/650], Validation Loss: 0.0018, Validation L1: 0.2776, Smoothed Validation Loss: 0.0018
Epoch [107/650], Train Loss: 0.0009, Train L1 Loss: 0.2092
Epoch [107/650], Validation Loss: 0.0018, Validation L1: 0.2781, Smoothed Validation Loss: 0.0018
Epoch [108/650], Train Loss: 0.0009, Train L1 Loss: 0.2087
Epoch [108/650], Validation Loss: 0.0018, Validation L1: 0.2781, Smoothed Validation Loss: 0.0018
Epoch 00108: reducing learning rate of group 0 to 6.2500e-05.
Epoch [109/650], Train Loss: 0.0010, Train L1 Loss: 0.2124
Epoch [109/650], Validation Loss: 0.0017, Validation L1: 0.2722, Smoothed Validation Loss: 0.0018
Epoch [110/650], Train Loss: 0.0010, Train L1 Loss: 0.2108
Epoch [110/650], Validation Loss: 0.0017, Validation L1: 0.2718, Smoothed Validation Loss: 0.0018
Epoch [111/650], Train Loss: 0.0009, Train L1 Loss: 0.2099
Epoch [111/650], Validation Loss: 0.0017, Validation L1: 0.2718, Smoothed Validation Loss: 0.0018
Epoch [112/650], Train Loss: 0.0009, Train L1 Loss: 0.2091
Epoch [112/650], Validation Loss: 0.0017, Validation L1: 0.2718, Smoothed Validation Loss: 0.0017
Epoch [113/650], Train Loss: 0.0009, Train L1 Loss: 0.2085
Epoch [113/650], Validation Loss: 0.0017, Validation L1: 0.2719, Smoothed Validation Loss: 0.0017
Epoch [114/650], Train Loss: 0.0009, Train L1 Loss: 0.2079
Epoch [114/650], Validation Loss: 0.0017, Validation L1: 0.2719, Smoothed Validation Loss: 0.0017
Epoch [115/650], Train Loss: 0.0009, Train L1 Loss: 0.2074
Epoch [115/650], Validation Loss: 0.0017, Validation L1: 0.2721, Smoothed Validation Loss: 0.0017
Epoch [116/650], Train Loss: 0.0009, Train L1 Loss: 0.2069
Epoch [116/650], Validation Loss: 0.0017, Validation L1: 0.2722, Smoothed Validation Loss: 0.0017
Epoch [117/650], Train Loss: 0.0009, Train L1 Loss: 0.2064
Epoch [117/650], Validation Loss: 0.0017, Validation L1: 0.2724, Smoothed Validation Loss: 0.0017
Epoch [118/650], Train Loss: 0.0009, Train L1 Loss: 0.2060
Epoch [118/650], Validation Loss: 0.0017, Validation L1: 0.2725, Smoothed Validation Loss: 0.0017
Epoch [119/650], Train Loss: 0.0009, Train L1 Loss: 0.2056
Epoch [119/650], Validation Loss: 0.0017, Validation L1: 0.2727, Smoothed Validation Loss: 0.0017
Epoch [120/650], Train Loss: 0.0009, Train L1 Loss: 0.2052
Epoch [120/650], Validation Loss: 0.0017, Validation L1: 0.2728, Smoothed Validation Loss: 0.0017
Epoch [121/650], Train Loss: 0.0009, Train L1 Loss: 0.2048
Epoch [121/650], Validation Loss: 0.0017, Validation L1: 0.2731, Smoothed Validation Loss: 0.0017
Epoch [122/650], Train Loss: 0.0009, Train L1 Loss: 0.2044
Epoch [122/650], Validation Loss: 0.0017, Validation L1: 0.2732, Smoothed Validation Loss: 0.0017
Epoch [123/650], Train Loss: 0.0009, Train L1 Loss: 0.2041
Epoch [123/650], Validation Loss: 0.0018, Validation L1: 0.2734, Smoothed Validation Loss: 0.0017
Epoch [124/650], Train Loss: 0.0009, Train L1 Loss: 0.2037
Epoch [124/650], Validation Loss: 0.0018, Validation L1: 0.2736, Smoothed Validation Loss: 0.0017
Epoch 00124: reducing learning rate of group 0 to 3.1250e-05.
Epoch [125/650], Train Loss: 0.0009, Train L1 Loss: 0.2068
Epoch [125/650], Validation Loss: 0.0017, Validation L1: 0.2723, Smoothed Validation Loss: 0.0017
Epoch [126/650], Train Loss: 0.0009, Train L1 Loss: 0.2059
Epoch [126/650], Validation Loss: 0.0017, Validation L1: 0.2718, Smoothed Validation Loss: 0.0017
Epoch [127/650], Train Loss: 0.0009, Train L1 Loss: 0.2053
Epoch [127/650], Validation Loss: 0.0017, Validation L1: 0.2716, Smoothed Validation Loss: 0.0017
Epoch [128/650], Train Loss: 0.0009, Train L1 Loss: 0.2049
Epoch [128/650], Validation Loss: 0.0017, Validation L1: 0.2715, Smoothed Validation Loss: 0.0017
Epoch [129/650], Train Loss: 0.0009, Train L1 Loss: 0.2045
Epoch [129/650], Validation Loss: 0.0017, Validation L1: 0.2715, Smoothed Validation Loss: 0.0017
Epoch [130/650], Train Loss: 0.0009, Train L1 Loss: 0.2041
Epoch [130/650], Validation Loss: 0.0017, Validation L1: 0.2714, Smoothed Validation Loss: 0.0017
Epoch [131/650], Train Loss: 0.0009, Train L1 Loss: 0.2038
Epoch [131/650], Validation Loss: 0.0017, Validation L1: 0.2714, Smoothed Validation Loss: 0.0017
Epoch [132/650], Train Loss: 0.0009, Train L1 Loss: 0.2035
Epoch [132/650], Validation Loss: 0.0017, Validation L1: 0.2714, Smoothed Validation Loss: 0.0017
Epoch [133/650], Train Loss: 0.0009, Train L1 Loss: 0.2032
Epoch [133/650], Validation Loss: 0.0017, Validation L1: 0.2714, Smoothed Validation Loss: 0.0017
Epoch [134/650], Train Loss: 0.0009, Train L1 Loss: 0.2029
Epoch [134/650], Validation Loss: 0.0017, Validation L1: 0.2714, Smoothed Validation Loss: 0.0017
Epoch [135/650], Train Loss: 0.0009, Train L1 Loss: 0.2026
Epoch [135/650], Validation Loss: 0.0017, Validation L1: 0.2714, Smoothed Validation Loss: 0.0017
Epoch [136/650], Train Loss: 0.0009, Train L1 Loss: 0.2024
Epoch [136/650], Validation Loss: 0.0017, Validation L1: 0.2714, Smoothed Validation Loss: 0.0017
Epoch [137/650], Train Loss: 0.0009, Train L1 Loss: 0.2021
Epoch [137/650], Validation Loss: 0.0017, Validation L1: 0.2715, Smoothed Validation Loss: 0.0017
Epoch [138/650], Train Loss: 0.0009, Train L1 Loss: 0.2019
Epoch [138/650], Validation Loss: 0.0017, Validation L1: 0.2715, Smoothed Validation Loss: 0.0017
Epoch [139/650], Train Loss: 0.0009, Train L1 Loss: 0.2016
Epoch [139/650], Validation Loss: 0.0017, Validation L1: 0.2716, Smoothed Validation Loss: 0.0017
Epoch [140/650], Train Loss: 0.0009, Train L1 Loss: 0.2014
Epoch [140/650], Validation Loss: 0.0017, Validation L1: 0.2716, Smoothed Validation Loss: 0.0017
Epoch [141/650], Train Loss: 0.0009, Train L1 Loss: 0.2012
Epoch [141/650], Validation Loss: 0.0017, Validation L1: 0.2717, Smoothed Validation Loss: 0.0017
Epoch [142/650], Train Loss: 0.0009, Train L1 Loss: 0.2009
Epoch [142/650], Validation Loss: 0.0017, Validation L1: 0.2717, Smoothed Validation Loss: 0.0017
Epoch 00142: reducing learning rate of group 0 to 1.5625e-05.
Epoch [143/650], Train Loss: 0.0009, Train L1 Loss: 0.2031
Epoch [143/650], Validation Loss: 0.0017, Validation L1: 0.2690, Smoothed Validation Loss: 0.0017
Epoch [144/650], Train Loss: 0.0009, Train L1 Loss: 0.2027
Epoch [144/650], Validation Loss: 0.0017, Validation L1: 0.2688, Smoothed Validation Loss: 0.0017
Epoch [145/650], Train Loss: 0.0009, Train L1 Loss: 0.2024
Epoch [145/650], Validation Loss: 0.0017, Validation L1: 0.2687, Smoothed Validation Loss: 0.0017
Epoch [146/650], Train Loss: 0.0009, Train L1 Loss: 0.2021
Epoch [146/650], Validation Loss: 0.0017, Validation L1: 0.2686, Smoothed Validation Loss: 0.0017
Epoch [147/650], Train Loss: 0.0009, Train L1 Loss: 0.2019
Epoch [147/650], Validation Loss: 0.0017, Validation L1: 0.2686, Smoothed Validation Loss: 0.0017
Epoch [148/650], Train Loss: 0.0009, Train L1 Loss: 0.2017
Epoch [148/650], Validation Loss: 0.0017, Validation L1: 0.2685, Smoothed Validation Loss: 0.0017
Epoch [149/650], Train Loss: 0.0009, Train L1 Loss: 0.2015
Epoch [149/650], Validation Loss: 0.0017, Validation L1: 0.2685, Smoothed Validation Loss: 0.0017
Epoch [150/650], Train Loss: 0.0009, Train L1 Loss: 0.2013
Epoch [150/650], Validation Loss: 0.0017, Validation L1: 0.2685, Smoothed Validation Loss: 0.0017
Epoch [151/650], Train Loss: 0.0009, Train L1 Loss: 0.2012
Epoch [151/650], Validation Loss: 0.0017, Validation L1: 0.2685, Smoothed Validation Loss: 0.0017
Epoch [152/650], Train Loss: 0.0009, Train L1 Loss: 0.2010
Epoch [152/650], Validation Loss: 0.0017, Validation L1: 0.2685, Smoothed Validation Loss: 0.0017
Epoch [153/650], Train Loss: 0.0009, Train L1 Loss: 0.2008
Epoch [153/650], Validation Loss: 0.0017, Validation L1: 0.2685, Smoothed Validation Loss: 0.0017
Epoch [154/650], Train Loss: 0.0009, Train L1 Loss: 0.2007
Epoch [154/650], Validation Loss: 0.0017, Validation L1: 0.2686, Smoothed Validation Loss: 0.0017
Epoch [155/650], Train Loss: 0.0009, Train L1 Loss: 0.2005
Epoch [155/650], Validation Loss: 0.0017, Validation L1: 0.2686, Smoothed Validation Loss: 0.0017
Epoch [156/650], Train Loss: 0.0009, Train L1 Loss: 0.2004
Epoch [156/650], Validation Loss: 0.0017, Validation L1: 0.2686, Smoothed Validation Loss: 0.0017
Epoch [157/650], Train Loss: 0.0009, Train L1 Loss: 0.2003
Epoch [157/650], Validation Loss: 0.0017, Validation L1: 0.2686, Smoothed Validation Loss: 0.0017
Epoch [158/650], Train Loss: 0.0009, Train L1 Loss: 0.2001
Epoch [158/650], Validation Loss: 0.0017, Validation L1: 0.2687, Smoothed Validation Loss: 0.0017
Epoch [159/650], Train Loss: 0.0009, Train L1 Loss: 0.2000
Epoch [159/650], Validation Loss: 0.0017, Validation L1: 0.2687, Smoothed Validation Loss: 0.0017
Epoch [160/650], Train Loss: 0.0009, Train L1 Loss: 0.1999
Epoch [160/650], Validation Loss: 0.0017, Validation L1: 0.2687, Smoothed Validation Loss: 0.0017
Epoch [161/650], Train Loss: 0.0009, Train L1 Loss: 0.1997
Epoch [161/650], Validation Loss: 0.0017, Validation L1: 0.2688, Smoothed Validation Loss: 0.0017
Epoch [162/650], Train Loss: 0.0009, Train L1 Loss: 0.1996
Epoch [162/650], Validation Loss: 0.0017, Validation L1: 0.2688, Smoothed Validation Loss: 0.0017
Epoch [163/650], Train Loss: 0.0009, Train L1 Loss: 0.1995
Epoch [163/650], Validation Loss: 0.0017, Validation L1: 0.2689, Smoothed Validation Loss: 0.0017
Epoch [164/650], Train Loss: 0.0009, Train L1 Loss: 0.1994
Epoch [164/650], Validation Loss: 0.0017, Validation L1: 0.2689, Smoothed Validation Loss: 0.0017
Epoch [165/650], Train Loss: 0.0009, Train L1 Loss: 0.1992
Epoch [165/650], Validation Loss: 0.0017, Validation L1: 0.2689, Smoothed Validation Loss: 0.0017
Epoch [166/650], Train Loss: 0.0009, Train L1 Loss: 0.1991
Epoch [166/650], Validation Loss: 0.0017, Validation L1: 0.2690, Smoothed Validation Loss: 0.0017
Epoch [167/650], Train Loss: 0.0009, Train L1 Loss: 0.1990
Epoch [167/650], Validation Loss: 0.0017, Validation L1: 0.2690, Smoothed Validation Loss: 0.0017
Epoch [168/650], Train Loss: 0.0009, Train L1 Loss: 0.1989
Epoch [168/650], Validation Loss: 0.0017, Validation L1: 0.2691, Smoothed Validation Loss: 0.0017
Epoch [169/650], Train Loss: 0.0009, Train L1 Loss: 0.1988
Epoch [169/650], Validation Loss: 0.0017, Validation L1: 0.2691, Smoothed Validation Loss: 0.0017
Epoch 00169: reducing learning rate of group 0 to 7.8125e-06.
Epoch [170/650], Train Loss: 0.0009, Train L1 Loss: 0.2001
Epoch [170/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [171/650], Train Loss: 0.0009, Train L1 Loss: 0.1997
Epoch [171/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [172/650], Train Loss: 0.0009, Train L1 Loss: 0.1995
Epoch [172/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [173/650], Train Loss: 0.0009, Train L1 Loss: 0.1994
Epoch [173/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [174/650], Train Loss: 0.0009, Train L1 Loss: 0.1993
Epoch [174/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [175/650], Train Loss: 0.0009, Train L1 Loss: 0.1992
Epoch [175/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [176/650], Train Loss: 0.0009, Train L1 Loss: 0.1991
Epoch [176/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [177/650], Train Loss: 0.0009, Train L1 Loss: 0.1990
Epoch [177/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [178/650], Train Loss: 0.0009, Train L1 Loss: 0.1989
Epoch [178/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [179/650], Train Loss: 0.0009, Train L1 Loss: 0.1988
Epoch [179/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [180/650], Train Loss: 0.0009, Train L1 Loss: 0.1987
Epoch [180/650], Validation Loss: 0.0017, Validation L1: 0.2679, Smoothed Validation Loss: 0.0017
Epoch [181/650], Train Loss: 0.0009, Train L1 Loss: 0.1987
Epoch [181/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [182/650], Train Loss: 0.0009, Train L1 Loss: 0.1986
Epoch [182/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [183/650], Train Loss: 0.0009, Train L1 Loss: 0.1985
Epoch [183/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [184/650], Train Loss: 0.0009, Train L1 Loss: 0.1984
Epoch [184/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [185/650], Train Loss: 0.0009, Train L1 Loss: 0.1984
Epoch [185/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [186/650], Train Loss: 0.0009, Train L1 Loss: 0.1983
Epoch [186/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [187/650], Train Loss: 0.0009, Train L1 Loss: 0.1982
Epoch [187/650], Validation Loss: 0.0017, Validation L1: 0.2680, Smoothed Validation Loss: 0.0017
Epoch [188/650], Train Loss: 0.0009, Train L1 Loss: 0.1982
Epoch [188/650], Validation Loss: 0.0017, Validation L1: 0.2681, Smoothed Validation Loss: 0.0017
Epoch [189/650], Train Loss: 0.0009, Train L1 Loss: 0.1981
Epoch [189/650], Validation Loss: 0.0017, Validation L1: 0.2681, Smoothed Validation Loss: 0.0017
Epoch [190/650], Train Loss: 0.0009, Train L1 Loss: 0.1980
Epoch [190/650], Validation Loss: 0.0017, Validation L1: 0.2681, Smoothed Validation Loss: 0.0017
Epoch [191/650], Train Loss: 0.0009, Train L1 Loss: 0.1980
Epoch [191/650], Validation Loss: 0.0017, Validation L1: 0.2681, Smoothed Validation Loss: 0.0017
Epoch [192/650], Train Loss: 0.0009, Train L1 Loss: 0.1979
Epoch [192/650], Validation Loss: 0.0017, Validation L1: 0.2681, Smoothed Validation Loss: 0.0017
Epoch [193/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [193/650], Validation Loss: 0.0017, Validation L1: 0.2682, Smoothed Validation Loss: 0.0017
Epoch [194/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [194/650], Validation Loss: 0.0017, Validation L1: 0.2682, Smoothed Validation Loss: 0.0017
Epoch [195/650], Train Loss: 0.0009, Train L1 Loss: 0.1977
Epoch [195/650], Validation Loss: 0.0017, Validation L1: 0.2682, Smoothed Validation Loss: 0.0017
Epoch 00195: reducing learning rate of group 0 to 3.9063e-06.
Epoch [196/650], Train Loss: 0.0009, Train L1 Loss: 0.1982
Epoch [196/650], Validation Loss: 0.0017, Validation L1: 0.2678, Smoothed Validation Loss: 0.0017
Epoch [197/650], Train Loss: 0.0009, Train L1 Loss: 0.1980
Epoch [197/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [198/650], Train Loss: 0.0009, Train L1 Loss: 0.1979
Epoch [198/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [199/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [199/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [200/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [200/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [201/650], Train Loss: 0.0009, Train L1 Loss: 0.1977
Epoch [201/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [202/650], Train Loss: 0.0009, Train L1 Loss: 0.1977
Epoch [202/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [203/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [203/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [204/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [204/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [205/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [205/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [206/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [206/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [207/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [207/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [208/650], Train Loss: 0.0009, Train L1 Loss: 0.1974
Epoch [208/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [209/650], Train Loss: 0.0009, Train L1 Loss: 0.1974
Epoch [209/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [210/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [210/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [211/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [211/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [212/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [212/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [213/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [213/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [214/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [214/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [215/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [215/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [216/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [216/650], Validation Loss: 0.0017, Validation L1: 0.2677, Smoothed Validation Loss: 0.0017
Epoch [217/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [217/650], Validation Loss: 0.0017, Validation L1: 0.2678, Smoothed Validation Loss: 0.0017
Epoch [218/650], Train Loss: 0.0009, Train L1 Loss: 0.1970
Epoch [218/650], Validation Loss: 0.0017, Validation L1: 0.2678, Smoothed Validation Loss: 0.0017
Epoch 00218: reducing learning rate of group 0 to 1.9531e-06.
Epoch [219/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [219/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [220/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [220/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [221/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [221/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [222/650], Train Loss: 0.0009, Train L1 Loss: 0.1970
Epoch [222/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [223/650], Train Loss: 0.0009, Train L1 Loss: 0.1970
Epoch [223/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [224/650], Train Loss: 0.0009, Train L1 Loss: 0.1970
Epoch [224/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [225/650], Train Loss: 0.0009, Train L1 Loss: 0.1970
Epoch [225/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [226/650], Train Loss: 0.0009, Train L1 Loss: 0.1969
Epoch [226/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [227/650], Train Loss: 0.0009, Train L1 Loss: 0.1969
Epoch [227/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [228/650], Train Loss: 0.0009, Train L1 Loss: 0.1969
Epoch [228/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [229/650], Train Loss: 0.0009, Train L1 Loss: 0.1969
Epoch [229/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [230/650], Train Loss: 0.0009, Train L1 Loss: 0.1969
Epoch [230/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [231/650], Train Loss: 0.0009, Train L1 Loss: 0.1968
Epoch [231/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [232/650], Train Loss: 0.0009, Train L1 Loss: 0.1968
Epoch [232/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [233/650], Train Loss: 0.0009, Train L1 Loss: 0.1968
Epoch [233/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [234/650], Train Loss: 0.0009, Train L1 Loss: 0.1968
Epoch [234/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [235/650], Train Loss: 0.0009, Train L1 Loss: 0.1967
Epoch [235/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [236/650], Train Loss: 0.0009, Train L1 Loss: 0.1967
Epoch [236/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [237/650], Train Loss: 0.0008, Train L1 Loss: 0.1967
Epoch [237/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [238/650], Train Loss: 0.0008, Train L1 Loss: 0.1967
Epoch [238/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch [239/650], Train Loss: 0.0008, Train L1 Loss: 0.1967
Epoch [239/650], Validation Loss: 0.0017, Validation L1: 0.2674, Smoothed Validation Loss: 0.0017
Epoch 00239: reducing learning rate of group 0 to 9.7656e-07.
Epoch [240/650], Train Loss: 0.0008, Train L1 Loss: 0.1967
Epoch [240/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [241/650], Train Loss: 0.0008, Train L1 Loss: 0.1966
Epoch [241/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [242/650], Train Loss: 0.0008, Train L1 Loss: 0.1966
Epoch [242/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [243/650], Train Loss: 0.0008, Train L1 Loss: 0.1966
Epoch [243/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [244/650], Train Loss: 0.0008, Train L1 Loss: 0.1966
Epoch [244/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [245/650], Train Loss: 0.0008, Train L1 Loss: 0.1966
Epoch [245/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [246/650], Train Loss: 0.0008, Train L1 Loss: 0.1966
Epoch [246/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [247/650], Train Loss: 0.0008, Train L1 Loss: 0.1966
Epoch [247/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [248/650], Train Loss: 0.0008, Train L1 Loss: 0.1965
Epoch [248/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [249/650], Train Loss: 0.0008, Train L1 Loss: 0.1965
Epoch [249/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [250/650], Train Loss: 0.0008, Train L1 Loss: 0.1965
Epoch [250/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [251/650], Train Loss: 0.0008, Train L1 Loss: 0.1965
Epoch [251/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch 00251: reducing learning rate of group 0 to 4.8828e-07.
Epoch [252/650], Train Loss: 0.0008, Train L1 Loss: 0.1965
Epoch [252/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [253/650], Train Loss: 0.0008, Train L1 Loss: 0.1965
Epoch [253/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [254/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [254/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [255/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [255/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [256/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [256/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [257/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [257/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch 00257: reducing learning rate of group 0 to 2.4414e-07.
Epoch [258/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [258/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [259/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [259/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [260/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [260/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [261/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [261/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [262/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [262/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [263/650], Train Loss: 0.0008, Train L1 Loss: 0.1964
Epoch [263/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch 00263: reducing learning rate of group 0 to 1.2207e-07.
Epoch [264/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [264/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [265/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [265/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [266/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [266/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [267/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [267/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [268/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [268/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [269/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [269/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch 00269: reducing learning rate of group 0 to 6.1035e-08.
Epoch [270/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [270/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [271/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [271/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [272/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [272/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [273/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [273/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [274/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [274/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [275/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [275/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch 00275: reducing learning rate of group 0 to 3.0518e-08.
Epoch [276/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [276/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [277/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [277/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [278/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [278/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [279/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [279/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [280/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [280/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [281/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [281/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch 00281: reducing learning rate of group 0 to 1.5259e-08.
Epoch [282/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [282/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [283/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [283/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [284/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [284/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [285/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [285/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [286/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [286/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [287/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [287/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [288/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [288/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [289/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [289/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [290/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [290/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [291/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [291/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [292/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [292/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [293/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [293/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [294/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [294/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [295/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [295/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [296/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [296/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [297/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [297/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [298/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [298/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [299/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [299/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [300/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [300/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [301/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [301/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [302/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [302/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [303/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [303/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [304/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [304/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [305/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [305/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [306/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [306/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [307/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [307/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [308/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [308/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [309/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [309/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [310/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [310/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [311/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [311/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [312/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [312/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [313/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [313/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [314/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [314/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [315/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [315/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [316/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [316/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [317/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [317/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [318/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [318/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [319/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [319/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [320/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [320/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [321/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [321/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [322/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [322/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [323/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [323/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [324/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [324/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [325/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [325/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [326/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [326/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [327/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [327/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [328/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [328/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [329/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [329/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [330/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [330/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [331/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [331/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [332/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [332/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [333/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [333/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [334/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [334/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [335/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [335/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [336/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [336/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [337/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [337/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [338/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [338/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [339/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [339/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [340/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [340/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [341/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [341/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [342/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [342/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [343/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [343/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [344/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [344/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [345/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [345/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [346/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [346/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [347/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [347/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [348/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [348/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [349/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [349/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [350/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [350/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [351/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [351/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [352/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [352/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [353/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [353/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [354/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [354/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [355/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [355/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [356/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [356/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [357/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [357/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [358/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [358/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [359/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [359/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [360/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [360/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [361/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [361/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [362/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [362/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [363/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [363/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [364/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [364/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [365/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [365/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [366/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [366/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [367/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [367/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [368/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [368/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [369/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [369/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [370/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [370/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [371/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [371/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [372/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [372/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [373/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [373/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [374/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [374/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [375/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [375/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [376/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [376/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [377/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [377/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [378/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [378/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [379/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [379/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [380/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [380/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [381/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [381/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [382/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [382/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [383/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [383/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [384/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [384/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [385/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [385/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [386/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [386/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [387/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [387/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [388/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [388/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [389/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [389/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [390/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [390/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [391/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [391/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [392/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [392/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [393/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [393/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [394/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [394/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [395/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [395/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [396/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [396/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [397/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [397/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [398/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [398/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [399/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [399/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [400/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [400/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [401/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [401/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [402/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [402/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [403/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [403/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [404/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [404/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [405/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [405/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [406/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [406/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [407/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [407/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [408/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [408/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [409/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [409/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [410/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [410/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [411/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [411/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [412/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [412/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [413/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [413/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [414/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [414/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [415/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [415/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [416/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [416/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [417/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [417/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [418/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [418/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [419/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [419/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [420/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [420/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [421/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [421/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [422/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [422/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [423/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [423/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [424/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [424/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [425/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [425/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [426/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [426/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [427/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [427/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [428/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [428/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [429/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [429/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [430/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [430/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [431/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [431/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [432/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [432/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [433/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [433/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [434/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [434/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [435/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [435/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [436/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [436/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [437/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [437/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [438/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [438/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [439/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [439/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [440/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [440/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [441/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [441/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [442/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [442/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [443/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [443/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [444/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [444/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [445/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [445/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [446/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [446/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [447/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [447/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [448/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [448/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [449/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [449/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [450/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [450/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [451/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [451/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [452/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [452/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [453/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [453/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [454/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [454/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [455/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [455/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [456/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [456/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [457/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [457/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [458/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [458/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [459/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [459/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [460/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [460/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [461/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [461/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [462/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [462/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [463/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [463/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [464/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [464/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [465/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [465/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [466/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [466/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [467/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [467/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [468/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [468/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [469/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [469/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [470/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [470/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [471/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [471/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [472/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [472/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [473/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [473/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [474/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [474/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [475/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [475/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [476/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [476/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [477/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [477/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [478/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [478/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [479/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [479/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [480/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [480/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [481/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [481/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [482/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [482/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [483/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [483/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [484/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [484/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [485/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [485/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [486/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [486/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [487/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [487/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [488/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [488/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [489/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [489/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [490/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [490/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [491/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [491/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [492/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [492/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [493/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [493/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [494/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [494/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [495/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [495/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [496/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [496/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [497/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [497/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [498/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [498/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [499/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [499/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [500/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [500/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [501/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [501/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [502/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [502/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [503/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [503/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [504/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [504/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [505/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [505/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [506/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [506/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [507/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [507/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [508/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [508/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [509/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [509/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [510/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [510/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [511/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [511/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [512/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [512/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [513/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [513/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [514/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [514/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [515/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [515/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [516/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [516/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [517/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [517/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [518/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [518/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [519/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [519/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [520/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [520/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [521/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [521/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [522/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [522/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [523/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [523/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [524/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [524/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [525/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [525/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [526/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [526/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [527/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [527/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [528/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [528/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [529/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [529/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [530/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [530/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [531/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [531/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [532/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [532/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [533/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [533/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [534/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [534/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [535/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [535/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [536/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [536/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [537/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [537/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [538/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [538/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [539/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [539/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [540/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [540/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [541/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [541/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [542/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [542/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [543/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [543/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [544/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [544/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [545/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [545/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [546/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [546/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [547/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [547/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [548/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [548/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [549/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [549/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [550/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [550/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [551/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [551/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [552/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [552/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [553/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [553/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [554/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [554/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [555/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [555/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [556/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [556/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [557/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [557/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [558/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [558/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [559/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [559/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [560/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [560/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [561/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [561/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [562/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [562/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [563/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [563/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [564/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [564/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [565/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [565/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [566/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [566/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [567/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [567/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [568/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [568/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [569/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [569/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [570/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [570/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [571/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [571/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [572/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [572/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [573/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [573/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [574/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [574/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [575/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [575/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [576/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [576/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [577/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [577/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [578/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [578/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [579/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [579/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [580/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [580/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [581/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [581/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [582/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [582/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [583/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [583/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [584/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [584/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [585/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [585/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [586/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [586/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [587/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [587/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [588/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [588/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [589/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [589/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [590/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [590/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [591/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [591/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [592/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [592/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [593/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [593/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [594/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [594/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [595/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [595/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [596/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [596/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [597/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [597/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [598/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [598/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [599/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [599/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [600/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [600/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [601/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [601/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [602/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [602/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [603/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [603/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [604/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [604/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [605/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [605/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [606/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [606/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [607/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [607/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [608/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [608/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [609/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [609/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [610/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [610/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [611/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [611/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [612/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [612/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [613/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [613/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [614/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [614/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [615/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [615/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [616/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [616/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [617/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [617/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [618/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [618/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [619/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [619/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [620/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [620/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [621/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [621/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [622/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [622/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [623/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [623/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [624/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [624/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [625/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [625/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [626/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [626/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [627/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [627/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [628/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [628/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [629/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [629/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [630/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [630/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [631/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [631/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [632/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [632/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [633/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [633/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [634/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [634/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [635/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [635/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [636/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [636/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [637/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [637/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [638/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [638/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [639/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [639/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [640/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [640/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [641/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [641/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [642/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [642/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [643/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [643/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [644/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [644/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [645/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [645/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [646/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [646/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [647/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [647/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [648/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [648/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [649/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [649/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
Epoch [650/650], Train Loss: 0.0008, Train L1 Loss: 0.1963
Epoch [650/650], Validation Loss: 0.0017, Validation L1: 0.2673, Smoothed Validation Loss: 0.0017
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19673445: <WorkingSetup_11> in cluster <dcc> Done

Job <WorkingSetup_11> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Sat Dec  2 18:17:09 2023
Job was executed on host(s) <4*n-62-18-12>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Sun Dec  3 14:51:10 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Sun Dec  3 14:51:10 2023
Terminated at Mon Dec  4 00:59:22 2023
Results reported at Mon Dec  4 00:59:22 2023

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

    CPU time :                                   36786.88 sec.
    Max Memory :                                 1947 MB
    Average Memory :                             1936.41 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63589.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   36493 sec.
    Turnaround time :                            110533 sec.

The output (if any) is above this job summary.

