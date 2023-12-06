
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
| <c>name</c>       | <d>str</d>        | <j>"12WorkingSetup-0"</j> |
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
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231204_014333-tlcb6up1
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 12WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/tlcb6up1
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:47,275] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7fd17bd28a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:51,149] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpq6yaxxcl.py line 218 
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:56,518] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpq6yaxxcl.py line 117 
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,049] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpq6yaxxcl.py line 90 
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,188] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:43:57,840] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:00,329] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:01,522] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 01:44:02,655] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.117 MB uploadedwandb: / 0.005 MB of 0.117 MB uploadedwandb: - 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▄▂▁▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▅▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▆▅▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▄▂▂▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▃▂▁▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.00745
wandb:     train l1 loss 0.45487
wandb:        train_loss 0.00472
wandb:       val l1 loss 0.57148
wandb:          val loss 0.00745
wandb: 
wandb: 🚀 View run 12WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/tlcb6up1
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231204_014333-tlcb6up1/logs
Epoch [1/650], Train Loss: 0.0286, Train L1 Loss: 0.8675
Epoch [1/650], Validation Loss: 0.0104, Validation L1: 0.7362, Smoothed Validation Loss: 0.0104
Epoch [2/650], Train Loss: 0.0105, Train L1 Loss: 0.7461
Epoch [2/650], Validation Loss: 0.0101, Validation L1: 0.7320, Smoothed Validation Loss: 0.0104
Epoch [3/650], Train Loss: 0.0101, Train L1 Loss: 0.7278
Epoch [3/650], Validation Loss: 0.0095, Validation L1: 0.7089, Smoothed Validation Loss: 0.0103
Epoch [4/650], Train Loss: 0.0095, Train L1 Loss: 0.7023
Epoch [4/650], Validation Loss: 0.0091, Validation L1: 0.6860, Smoothed Validation Loss: 0.0102
Epoch [5/650], Train Loss: 0.0092, Train L1 Loss: 0.6874
Epoch [5/650], Validation Loss: 0.0090, Validation L1: 0.6845, Smoothed Validation Loss: 0.0101
Epoch [6/650], Train Loss: 0.0090, Train L1 Loss: 0.6800
Epoch [6/650], Validation Loss: 0.0089, Validation L1: 0.6756, Smoothed Validation Loss: 0.0100
Epoch [7/650], Train Loss: 0.0089, Train L1 Loss: 0.6729
Epoch [7/650], Validation Loss: 0.0089, Validation L1: 0.6761, Smoothed Validation Loss: 0.0098
Epoch [8/650], Train Loss: 0.0087, Train L1 Loss: 0.6656
Epoch [8/650], Validation Loss: 0.0088, Validation L1: 0.6668, Smoothed Validation Loss: 0.0097
Epoch [9/650], Train Loss: 0.0086, Train L1 Loss: 0.6585
Epoch [9/650], Validation Loss: 0.0088, Validation L1: 0.6619, Smoothed Validation Loss: 0.0097
Epoch [10/650], Train Loss: 0.0084, Train L1 Loss: 0.6510
Epoch [10/650], Validation Loss: 0.0086, Validation L1: 0.6505, Smoothed Validation Loss: 0.0095
Epoch [11/650], Train Loss: 0.0082, Train L1 Loss: 0.6410
Epoch [11/650], Validation Loss: 0.0084, Validation L1: 0.6422, Smoothed Validation Loss: 0.0094
Epoch [12/650], Train Loss: 0.0081, Train L1 Loss: 0.6344
Epoch [12/650], Validation Loss: 0.0083, Validation L1: 0.6344, Smoothed Validation Loss: 0.0093
Epoch [13/650], Train Loss: 0.0080, Train L1 Loss: 0.6285
Epoch [13/650], Validation Loss: 0.0083, Validation L1: 0.6338, Smoothed Validation Loss: 0.0092
Epoch [14/650], Train Loss: 0.0079, Train L1 Loss: 0.6226
Epoch [14/650], Validation Loss: 0.0082, Validation L1: 0.6286, Smoothed Validation Loss: 0.0091
Epoch [15/650], Train Loss: 0.0078, Train L1 Loss: 0.6178
Epoch [15/650], Validation Loss: 0.0080, Validation L1: 0.6232, Smoothed Validation Loss: 0.0090
Epoch [16/650], Train Loss: 0.0077, Train L1 Loss: 0.6149
Epoch [16/650], Validation Loss: 0.0080, Validation L1: 0.6231, Smoothed Validation Loss: 0.0089
Epoch [17/650], Train Loss: 0.0077, Train L1 Loss: 0.6108
Epoch [17/650], Validation Loss: 0.0080, Validation L1: 0.6195, Smoothed Validation Loss: 0.0088
Epoch [18/650], Train Loss: 0.0076, Train L1 Loss: 0.6073
Epoch [18/650], Validation Loss: 0.0080, Validation L1: 0.6223, Smoothed Validation Loss: 0.0087
Epoch [19/650], Train Loss: 0.0075, Train L1 Loss: 0.6038
Epoch [19/650], Validation Loss: 0.0078, Validation L1: 0.6152, Smoothed Validation Loss: 0.0086
Epoch [20/650], Train Loss: 0.0075, Train L1 Loss: 0.6012
Epoch [20/650], Validation Loss: 0.0079, Validation L1: 0.6177, Smoothed Validation Loss: 0.0086
Epoch [21/650], Train Loss: 0.0074, Train L1 Loss: 0.5976
Epoch [21/650], Validation Loss: 0.0078, Validation L1: 0.6135, Smoothed Validation Loss: 0.0085
Epoch [22/650], Train Loss: 0.0074, Train L1 Loss: 0.5966
Epoch [22/650], Validation Loss: 0.0079, Validation L1: 0.6092, Smoothed Validation Loss: 0.0084
Epoch [23/650], Train Loss: 0.0073, Train L1 Loss: 0.5941
Epoch [23/650], Validation Loss: 0.0077, Validation L1: 0.6041, Smoothed Validation Loss: 0.0084
Epoch [24/650], Train Loss: 0.0073, Train L1 Loss: 0.5925
Epoch [24/650], Validation Loss: 0.0077, Validation L1: 0.6081, Smoothed Validation Loss: 0.0083
Epoch [25/650], Train Loss: 0.0072, Train L1 Loss: 0.5900
Epoch [25/650], Validation Loss: 0.0077, Validation L1: 0.6069, Smoothed Validation Loss: 0.0082
Epoch [26/650], Train Loss: 0.0072, Train L1 Loss: 0.5882
Epoch [26/650], Validation Loss: 0.0076, Validation L1: 0.5974, Smoothed Validation Loss: 0.0082
Epoch [27/650], Train Loss: 0.0072, Train L1 Loss: 0.5873
Epoch [27/650], Validation Loss: 0.0076, Validation L1: 0.5985, Smoothed Validation Loss: 0.0081
Epoch [28/650], Train Loss: 0.0072, Train L1 Loss: 0.5857
Epoch [28/650], Validation Loss: 0.0076, Validation L1: 0.5988, Smoothed Validation Loss: 0.0081
Epoch [29/650], Train Loss: 0.0071, Train L1 Loss: 0.5841
Epoch [29/650], Validation Loss: 0.0077, Validation L1: 0.5991, Smoothed Validation Loss: 0.0080
Epoch [30/650], Train Loss: 0.0071, Train L1 Loss: 0.5820
Epoch [30/650], Validation Loss: 0.0077, Validation L1: 0.6025, Smoothed Validation Loss: 0.0080
Epoch [31/650], Train Loss: 0.0071, Train L1 Loss: 0.5811
Epoch [31/650], Validation Loss: 0.0076, Validation L1: 0.6003, Smoothed Validation Loss: 0.0080
Epoch [32/650], Train Loss: 0.0070, Train L1 Loss: 0.5787
Epoch [32/650], Validation Loss: 0.0077, Validation L1: 0.5950, Smoothed Validation Loss: 0.0079
Epoch [33/650], Train Loss: 0.0070, Train L1 Loss: 0.5781
Epoch [33/650], Validation Loss: 0.0075, Validation L1: 0.5889, Smoothed Validation Loss: 0.0079
Epoch [34/650], Train Loss: 0.0071, Train L1 Loss: 0.5803
Epoch [34/650], Validation Loss: 0.0077, Validation L1: 0.6007, Smoothed Validation Loss: 0.0079
Epoch [35/650], Train Loss: 0.0070, Train L1 Loss: 0.5781
Epoch [35/650], Validation Loss: 0.0075, Validation L1: 0.5968, Smoothed Validation Loss: 0.0078
Epoch [36/650], Train Loss: 0.0069, Train L1 Loss: 0.5741
Epoch [36/650], Validation Loss: 0.0076, Validation L1: 0.5899, Smoothed Validation Loss: 0.0078
Epoch [37/650], Train Loss: 0.0069, Train L1 Loss: 0.5723
Epoch [37/650], Validation Loss: 0.0074, Validation L1: 0.5844, Smoothed Validation Loss: 0.0078
Epoch [38/650], Train Loss: 0.0069, Train L1 Loss: 0.5728
Epoch [38/650], Validation Loss: 0.0077, Validation L1: 0.5950, Smoothed Validation Loss: 0.0078
Epoch [39/650], Train Loss: 0.0069, Train L1 Loss: 0.5724
Epoch [39/650], Validation Loss: 0.0076, Validation L1: 0.5827, Smoothed Validation Loss: 0.0077
Epoch [40/650], Train Loss: 0.0069, Train L1 Loss: 0.5711
Epoch [40/650], Validation Loss: 0.0076, Validation L1: 0.5896, Smoothed Validation Loss: 0.0077
Epoch [41/650], Train Loss: 0.0068, Train L1 Loss: 0.5684
Epoch [41/650], Validation Loss: 0.0078, Validation L1: 0.5976, Smoothed Validation Loss: 0.0077
Epoch [42/650], Train Loss: 0.0068, Train L1 Loss: 0.5680
Epoch [42/650], Validation Loss: 0.0075, Validation L1: 0.5899, Smoothed Validation Loss: 0.0077
Epoch [43/650], Train Loss: 0.0068, Train L1 Loss: 0.5682
Epoch [43/650], Validation Loss: 0.0075, Validation L1: 0.5875, Smoothed Validation Loss: 0.0077
Epoch [44/650], Train Loss: 0.0068, Train L1 Loss: 0.5658
Epoch [44/650], Validation Loss: 0.0074, Validation L1: 0.5890, Smoothed Validation Loss: 0.0077
Epoch [45/650], Train Loss: 0.0067, Train L1 Loss: 0.5643
Epoch [45/650], Validation Loss: 0.0074, Validation L1: 0.5800, Smoothed Validation Loss: 0.0076
Epoch [46/650], Train Loss: 0.0067, Train L1 Loss: 0.5631
Epoch [46/650], Validation Loss: 0.0074, Validation L1: 0.5863, Smoothed Validation Loss: 0.0076
Epoch [47/650], Train Loss: 0.0067, Train L1 Loss: 0.5640
Epoch [47/650], Validation Loss: 0.0075, Validation L1: 0.5830, Smoothed Validation Loss: 0.0076
Epoch [48/650], Train Loss: 0.0067, Train L1 Loss: 0.5626
Epoch [48/650], Validation Loss: 0.0074, Validation L1: 0.5813, Smoothed Validation Loss: 0.0076
Epoch [49/650], Train Loss: 0.0067, Train L1 Loss: 0.5619
Epoch [49/650], Validation Loss: 0.0074, Validation L1: 0.5827, Smoothed Validation Loss: 0.0076
Epoch [50/650], Train Loss: 0.0067, Train L1 Loss: 0.5612
Epoch [50/650], Validation Loss: 0.0074, Validation L1: 0.5902, Smoothed Validation Loss: 0.0076
Epoch [51/650], Train Loss: 0.0066, Train L1 Loss: 0.5606
Epoch [51/650], Validation Loss: 0.0076, Validation L1: 0.5903, Smoothed Validation Loss: 0.0076
Epoch [52/650], Train Loss: 0.0066, Train L1 Loss: 0.5598
Epoch [52/650], Validation Loss: 0.0075, Validation L1: 0.5870, Smoothed Validation Loss: 0.0075
Epoch [53/650], Train Loss: 0.0066, Train L1 Loss: 0.5571
Epoch [53/650], Validation Loss: 0.0074, Validation L1: 0.5805, Smoothed Validation Loss: 0.0075
Epoch [54/650], Train Loss: 0.0066, Train L1 Loss: 0.5573
Epoch [54/650], Validation Loss: 0.0074, Validation L1: 0.5790, Smoothed Validation Loss: 0.0075
Epoch [55/650], Train Loss: 0.0066, Train L1 Loss: 0.5594
Epoch [55/650], Validation Loss: 0.0074, Validation L1: 0.5790, Smoothed Validation Loss: 0.0075
Epoch [56/650], Train Loss: 0.0066, Train L1 Loss: 0.5559
Epoch [56/650], Validation Loss: 0.0075, Validation L1: 0.5830, Smoothed Validation Loss: 0.0075
Epoch [57/650], Train Loss: 0.0065, Train L1 Loss: 0.5540
Epoch [57/650], Validation Loss: 0.0075, Validation L1: 0.5833, Smoothed Validation Loss: 0.0075
Epoch [58/650], Train Loss: 0.0065, Train L1 Loss: 0.5537
Epoch [58/650], Validation Loss: 0.0075, Validation L1: 0.5837, Smoothed Validation Loss: 0.0075
Epoch [59/650], Train Loss: 0.0066, Train L1 Loss: 0.5564
Epoch [59/650], Validation Loss: 0.0075, Validation L1: 0.5834, Smoothed Validation Loss: 0.0075
Epoch [60/650], Train Loss: 0.0065, Train L1 Loss: 0.5542
Epoch [60/650], Validation Loss: 0.0074, Validation L1: 0.5782, Smoothed Validation Loss: 0.0075
Epoch [61/650], Train Loss: 0.0065, Train L1 Loss: 0.5516
Epoch [61/650], Validation Loss: 0.0076, Validation L1: 0.5831, Smoothed Validation Loss: 0.0075
Epoch [62/650], Train Loss: 0.0065, Train L1 Loss: 0.5522
Epoch [62/650], Validation Loss: 0.0076, Validation L1: 0.5873, Smoothed Validation Loss: 0.0075
Epoch [63/650], Train Loss: 0.0065, Train L1 Loss: 0.5511
Epoch [63/650], Validation Loss: 0.0075, Validation L1: 0.5827, Smoothed Validation Loss: 0.0075
Epoch [64/650], Train Loss: 0.0064, Train L1 Loss: 0.5501
Epoch [64/650], Validation Loss: 0.0074, Validation L1: 0.5766, Smoothed Validation Loss: 0.0075
Epoch [65/650], Train Loss: 0.0064, Train L1 Loss: 0.5497
Epoch [65/650], Validation Loss: 0.0075, Validation L1: 0.5803, Smoothed Validation Loss: 0.0075
Epoch [66/650], Train Loss: 0.0065, Train L1 Loss: 0.5525
Epoch [66/650], Validation Loss: 0.0075, Validation L1: 0.5817, Smoothed Validation Loss: 0.0075
Epoch 00066: reducing learning rate of group 0 to 5.0000e-04.
Epoch [67/650], Train Loss: 0.0061, Train L1 Loss: 0.5316
Epoch [67/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0075
Epoch [68/650], Train Loss: 0.0059, Train L1 Loss: 0.5234
Epoch [68/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0075
Epoch [69/650], Train Loss: 0.0059, Train L1 Loss: 0.5191
Epoch [69/650], Validation Loss: 0.0075, Validation L1: 0.5726, Smoothed Validation Loss: 0.0075
Epoch [70/650], Train Loss: 0.0058, Train L1 Loss: 0.5159
Epoch [70/650], Validation Loss: 0.0076, Validation L1: 0.5774, Smoothed Validation Loss: 0.0075
Epoch [71/650], Train Loss: 0.0057, Train L1 Loss: 0.5139
Epoch [71/650], Validation Loss: 0.0077, Validation L1: 0.5847, Smoothed Validation Loss: 0.0075
Epoch [72/650], Train Loss: 0.0057, Train L1 Loss: 0.5133
Epoch [72/650], Validation Loss: 0.0078, Validation L1: 0.5916, Smoothed Validation Loss: 0.0075
Epoch [73/650], Train Loss: 0.0057, Train L1 Loss: 0.5119
Epoch [73/650], Validation Loss: 0.0079, Validation L1: 0.5943, Smoothed Validation Loss: 0.0076
Epoch [74/650], Train Loss: 0.0057, Train L1 Loss: 0.5105
Epoch [74/650], Validation Loss: 0.0078, Validation L1: 0.5945, Smoothed Validation Loss: 0.0076
Epoch [75/650], Train Loss: 0.0056, Train L1 Loss: 0.5095
Epoch [75/650], Validation Loss: 0.0077, Validation L1: 0.5881, Smoothed Validation Loss: 0.0076
Epoch 00075: reducing learning rate of group 0 to 2.5000e-04.
Epoch [76/650], Train Loss: 0.0056, Train L1 Loss: 0.5061
Epoch [76/650], Validation Loss: 0.0076, Validation L1: 0.5796, Smoothed Validation Loss: 0.0076
Epoch [77/650], Train Loss: 0.0055, Train L1 Loss: 0.4997
Epoch [77/650], Validation Loss: 0.0076, Validation L1: 0.5849, Smoothed Validation Loss: 0.0076
Epoch [78/650], Train Loss: 0.0054, Train L1 Loss: 0.4966
Epoch [78/650], Validation Loss: 0.0077, Validation L1: 0.5828, Smoothed Validation Loss: 0.0076
Epoch [79/650], Train Loss: 0.0053, Train L1 Loss: 0.4922
Epoch [79/650], Validation Loss: 0.0077, Validation L1: 0.5848, Smoothed Validation Loss: 0.0076
Epoch [80/650], Train Loss: 0.0053, Train L1 Loss: 0.4895
Epoch [80/650], Validation Loss: 0.0078, Validation L1: 0.5872, Smoothed Validation Loss: 0.0076
Epoch [81/650], Train Loss: 0.0052, Train L1 Loss: 0.4874
Epoch [81/650], Validation Loss: 0.0078, Validation L1: 0.5893, Smoothed Validation Loss: 0.0077
Epoch 00081: reducing learning rate of group 0 to 1.2500e-04.
Epoch [82/650], Train Loss: 0.0053, Train L1 Loss: 0.4903
Epoch [82/650], Validation Loss: 0.0075, Validation L1: 0.5792, Smoothed Validation Loss: 0.0076
Epoch [83/650], Train Loss: 0.0052, Train L1 Loss: 0.4853
Epoch [83/650], Validation Loss: 0.0076, Validation L1: 0.5790, Smoothed Validation Loss: 0.0076
Epoch [84/650], Train Loss: 0.0052, Train L1 Loss: 0.4821
Epoch [84/650], Validation Loss: 0.0076, Validation L1: 0.5795, Smoothed Validation Loss: 0.0076
Epoch [85/650], Train Loss: 0.0051, Train L1 Loss: 0.4798
Epoch [85/650], Validation Loss: 0.0076, Validation L1: 0.5800, Smoothed Validation Loss: 0.0076
Epoch [86/650], Train Loss: 0.0051, Train L1 Loss: 0.4777
Epoch [86/650], Validation Loss: 0.0076, Validation L1: 0.5805, Smoothed Validation Loss: 0.0076
Epoch [87/650], Train Loss: 0.0050, Train L1 Loss: 0.4757
Epoch [87/650], Validation Loss: 0.0077, Validation L1: 0.5813, Smoothed Validation Loss: 0.0076
Epoch 00087: reducing learning rate of group 0 to 6.2500e-05.
Epoch [88/650], Train Loss: 0.0051, Train L1 Loss: 0.4796
Epoch [88/650], Validation Loss: 0.0074, Validation L1: 0.5720, Smoothed Validation Loss: 0.0076
Epoch [89/650], Train Loss: 0.0051, Train L1 Loss: 0.4763
Epoch [89/650], Validation Loss: 0.0074, Validation L1: 0.5718, Smoothed Validation Loss: 0.0076
Epoch [90/650], Train Loss: 0.0050, Train L1 Loss: 0.4744
Epoch [90/650], Validation Loss: 0.0075, Validation L1: 0.5721, Smoothed Validation Loss: 0.0076
Epoch [91/650], Train Loss: 0.0050, Train L1 Loss: 0.4727
Epoch [91/650], Validation Loss: 0.0075, Validation L1: 0.5724, Smoothed Validation Loss: 0.0076
Epoch [92/650], Train Loss: 0.0050, Train L1 Loss: 0.4713
Epoch [92/650], Validation Loss: 0.0075, Validation L1: 0.5729, Smoothed Validation Loss: 0.0076
Epoch [93/650], Train Loss: 0.0050, Train L1 Loss: 0.4699
Epoch [93/650], Validation Loss: 0.0075, Validation L1: 0.5734, Smoothed Validation Loss: 0.0076
Epoch 00093: reducing learning rate of group 0 to 3.1250e-05.
Epoch [94/650], Train Loss: 0.0050, Train L1 Loss: 0.4736
Epoch [94/650], Validation Loss: 0.0074, Validation L1: 0.5696, Smoothed Validation Loss: 0.0075
Epoch [95/650], Train Loss: 0.0050, Train L1 Loss: 0.4717
Epoch [95/650], Validation Loss: 0.0074, Validation L1: 0.5695, Smoothed Validation Loss: 0.0075
Epoch [96/650], Train Loss: 0.0050, Train L1 Loss: 0.4705
Epoch [96/650], Validation Loss: 0.0074, Validation L1: 0.5696, Smoothed Validation Loss: 0.0075
Epoch [97/650], Train Loss: 0.0050, Train L1 Loss: 0.4695
Epoch [97/650], Validation Loss: 0.0074, Validation L1: 0.5697, Smoothed Validation Loss: 0.0075
Epoch [98/650], Train Loss: 0.0050, Train L1 Loss: 0.4686
Epoch [98/650], Validation Loss: 0.0074, Validation L1: 0.5699, Smoothed Validation Loss: 0.0075
Epoch [99/650], Train Loss: 0.0049, Train L1 Loss: 0.4677
Epoch [99/650], Validation Loss: 0.0074, Validation L1: 0.5702, Smoothed Validation Loss: 0.0075
Epoch [100/650], Train Loss: 0.0049, Train L1 Loss: 0.4669
Epoch [100/650], Validation Loss: 0.0074, Validation L1: 0.5704, Smoothed Validation Loss: 0.0075
Epoch [101/650], Train Loss: 0.0049, Train L1 Loss: 0.4661
Epoch [101/650], Validation Loss: 0.0074, Validation L1: 0.5707, Smoothed Validation Loss: 0.0075
Epoch [102/650], Train Loss: 0.0049, Train L1 Loss: 0.4653
Epoch [102/650], Validation Loss: 0.0074, Validation L1: 0.5710, Smoothed Validation Loss: 0.0075
Epoch [103/650], Train Loss: 0.0049, Train L1 Loss: 0.4646
Epoch [103/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0075
Epoch [104/650], Train Loss: 0.0049, Train L1 Loss: 0.4639
Epoch [104/650], Validation Loss: 0.0074, Validation L1: 0.5716, Smoothed Validation Loss: 0.0075
Epoch [105/650], Train Loss: 0.0049, Train L1 Loss: 0.4632
Epoch [105/650], Validation Loss: 0.0074, Validation L1: 0.5719, Smoothed Validation Loss: 0.0074
Epoch [106/650], Train Loss: 0.0048, Train L1 Loss: 0.4625
Epoch [106/650], Validation Loss: 0.0075, Validation L1: 0.5722, Smoothed Validation Loss: 0.0074
Epoch [107/650], Train Loss: 0.0048, Train L1 Loss: 0.4618
Epoch [107/650], Validation Loss: 0.0075, Validation L1: 0.5725, Smoothed Validation Loss: 0.0075
Epoch [108/650], Train Loss: 0.0048, Train L1 Loss: 0.4612
Epoch [108/650], Validation Loss: 0.0075, Validation L1: 0.5728, Smoothed Validation Loss: 0.0075
Epoch [109/650], Train Loss: 0.0048, Train L1 Loss: 0.4605
Epoch [109/650], Validation Loss: 0.0075, Validation L1: 0.5731, Smoothed Validation Loss: 0.0075
Epoch [110/650], Train Loss: 0.0048, Train L1 Loss: 0.4599
Epoch [110/650], Validation Loss: 0.0075, Validation L1: 0.5735, Smoothed Validation Loss: 0.0075
Epoch [111/650], Train Loss: 0.0048, Train L1 Loss: 0.4593
Epoch [111/650], Validation Loss: 0.0075, Validation L1: 0.5738, Smoothed Validation Loss: 0.0075
Epoch 00111: reducing learning rate of group 0 to 1.5625e-05.
Epoch [112/650], Train Loss: 0.0048, Train L1 Loss: 0.4616
Epoch [112/650], Validation Loss: 0.0075, Validation L1: 0.5734, Smoothed Validation Loss: 0.0075
Epoch [113/650], Train Loss: 0.0048, Train L1 Loss: 0.4610
Epoch [113/650], Validation Loss: 0.0075, Validation L1: 0.5733, Smoothed Validation Loss: 0.0075
Epoch [114/650], Train Loss: 0.0048, Train L1 Loss: 0.4605
Epoch [114/650], Validation Loss: 0.0075, Validation L1: 0.5733, Smoothed Validation Loss: 0.0075
Epoch [115/650], Train Loss: 0.0048, Train L1 Loss: 0.4600
Epoch [115/650], Validation Loss: 0.0075, Validation L1: 0.5734, Smoothed Validation Loss: 0.0075
Epoch [116/650], Train Loss: 0.0048, Train L1 Loss: 0.4595
Epoch [116/650], Validation Loss: 0.0075, Validation L1: 0.5735, Smoothed Validation Loss: 0.0075
Epoch [117/650], Train Loss: 0.0048, Train L1 Loss: 0.4591
Epoch [117/650], Validation Loss: 0.0075, Validation L1: 0.5736, Smoothed Validation Loss: 0.0075
Epoch 00117: reducing learning rate of group 0 to 7.8125e-06.
Epoch [118/650], Train Loss: 0.0048, Train L1 Loss: 0.4609
Epoch [118/650], Validation Loss: 0.0074, Validation L1: 0.5718, Smoothed Validation Loss: 0.0075
Epoch [119/650], Train Loss: 0.0048, Train L1 Loss: 0.4602
Epoch [119/650], Validation Loss: 0.0074, Validation L1: 0.5716, Smoothed Validation Loss: 0.0075
Epoch [120/650], Train Loss: 0.0048, Train L1 Loss: 0.4599
Epoch [120/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0075
Epoch [121/650], Train Loss: 0.0048, Train L1 Loss: 0.4596
Epoch [121/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0075
Epoch [122/650], Train Loss: 0.0048, Train L1 Loss: 0.4593
Epoch [122/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0075
Epoch [123/650], Train Loss: 0.0048, Train L1 Loss: 0.4590
Epoch [123/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0075
Epoch 00123: reducing learning rate of group 0 to 3.9063e-06.
Epoch [124/650], Train Loss: 0.0048, Train L1 Loss: 0.4597
Epoch [124/650], Validation Loss: 0.0074, Validation L1: 0.5706, Smoothed Validation Loss: 0.0075
Epoch [125/650], Train Loss: 0.0048, Train L1 Loss: 0.4592
Epoch [125/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [126/650], Train Loss: 0.0048, Train L1 Loss: 0.4590
Epoch [126/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [127/650], Train Loss: 0.0048, Train L1 Loss: 0.4588
Epoch [127/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [128/650], Train Loss: 0.0048, Train L1 Loss: 0.4586
Epoch [128/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [129/650], Train Loss: 0.0048, Train L1 Loss: 0.4585
Epoch [129/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [130/650], Train Loss: 0.0048, Train L1 Loss: 0.4584
Epoch [130/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [131/650], Train Loss: 0.0048, Train L1 Loss: 0.4582
Epoch [131/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [132/650], Train Loss: 0.0048, Train L1 Loss: 0.4581
Epoch [132/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [133/650], Train Loss: 0.0048, Train L1 Loss: 0.4579
Epoch [133/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [134/650], Train Loss: 0.0048, Train L1 Loss: 0.4578
Epoch [134/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [135/650], Train Loss: 0.0048, Train L1 Loss: 0.4577
Epoch [135/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [136/650], Train Loss: 0.0048, Train L1 Loss: 0.4575
Epoch [136/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [137/650], Train Loss: 0.0048, Train L1 Loss: 0.4574
Epoch [137/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [138/650], Train Loss: 0.0048, Train L1 Loss: 0.4573
Epoch [138/650], Validation Loss: 0.0074, Validation L1: 0.5705, Smoothed Validation Loss: 0.0074
Epoch [139/650], Train Loss: 0.0048, Train L1 Loss: 0.4572
Epoch [139/650], Validation Loss: 0.0074, Validation L1: 0.5706, Smoothed Validation Loss: 0.0074
Epoch [140/650], Train Loss: 0.0048, Train L1 Loss: 0.4571
Epoch [140/650], Validation Loss: 0.0074, Validation L1: 0.5706, Smoothed Validation Loss: 0.0074
Epoch [141/650], Train Loss: 0.0048, Train L1 Loss: 0.4569
Epoch [141/650], Validation Loss: 0.0074, Validation L1: 0.5706, Smoothed Validation Loss: 0.0074
Epoch [142/650], Train Loss: 0.0047, Train L1 Loss: 0.4568
Epoch [142/650], Validation Loss: 0.0074, Validation L1: 0.5706, Smoothed Validation Loss: 0.0074
Epoch [143/650], Train Loss: 0.0047, Train L1 Loss: 0.4567
Epoch [143/650], Validation Loss: 0.0074, Validation L1: 0.5707, Smoothed Validation Loss: 0.0074
Epoch [144/650], Train Loss: 0.0047, Train L1 Loss: 0.4566
Epoch [144/650], Validation Loss: 0.0074, Validation L1: 0.5707, Smoothed Validation Loss: 0.0074
Epoch [145/650], Train Loss: 0.0047, Train L1 Loss: 0.4565
Epoch [145/650], Validation Loss: 0.0074, Validation L1: 0.5707, Smoothed Validation Loss: 0.0074
Epoch [146/650], Train Loss: 0.0047, Train L1 Loss: 0.4563
Epoch [146/650], Validation Loss: 0.0074, Validation L1: 0.5707, Smoothed Validation Loss: 0.0074
Epoch 00146: reducing learning rate of group 0 to 1.9531e-06.
Epoch [147/650], Train Loss: 0.0047, Train L1 Loss: 0.4564
Epoch [147/650], Validation Loss: 0.0074, Validation L1: 0.5707, Smoothed Validation Loss: 0.0074
Epoch [148/650], Train Loss: 0.0047, Train L1 Loss: 0.4562
Epoch [148/650], Validation Loss: 0.0074, Validation L1: 0.5708, Smoothed Validation Loss: 0.0074
Epoch [149/650], Train Loss: 0.0047, Train L1 Loss: 0.4561
Epoch [149/650], Validation Loss: 0.0074, Validation L1: 0.5708, Smoothed Validation Loss: 0.0074
Epoch [150/650], Train Loss: 0.0047, Train L1 Loss: 0.4560
Epoch [150/650], Validation Loss: 0.0074, Validation L1: 0.5708, Smoothed Validation Loss: 0.0074
Epoch [151/650], Train Loss: 0.0047, Train L1 Loss: 0.4559
Epoch [151/650], Validation Loss: 0.0074, Validation L1: 0.5708, Smoothed Validation Loss: 0.0074
Epoch [152/650], Train Loss: 0.0047, Train L1 Loss: 0.4559
Epoch [152/650], Validation Loss: 0.0074, Validation L1: 0.5708, Smoothed Validation Loss: 0.0074
Epoch 00152: reducing learning rate of group 0 to 9.7656e-07.
Epoch [153/650], Train Loss: 0.0047, Train L1 Loss: 0.4557
Epoch [153/650], Validation Loss: 0.0074, Validation L1: 0.5710, Smoothed Validation Loss: 0.0074
Epoch [154/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [154/650], Validation Loss: 0.0074, Validation L1: 0.5710, Smoothed Validation Loss: 0.0074
Epoch [155/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [155/650], Validation Loss: 0.0074, Validation L1: 0.5710, Smoothed Validation Loss: 0.0074
Epoch [156/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [156/650], Validation Loss: 0.0074, Validation L1: 0.5710, Smoothed Validation Loss: 0.0074
Epoch [157/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [157/650], Validation Loss: 0.0074, Validation L1: 0.5710, Smoothed Validation Loss: 0.0074
Epoch [158/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [158/650], Validation Loss: 0.0074, Validation L1: 0.5710, Smoothed Validation Loss: 0.0074
Epoch 00158: reducing learning rate of group 0 to 4.8828e-07.
Epoch [159/650], Train Loss: 0.0047, Train L1 Loss: 0.4553
Epoch [159/650], Validation Loss: 0.0074, Validation L1: 0.5712, Smoothed Validation Loss: 0.0074
Epoch [160/650], Train Loss: 0.0047, Train L1 Loss: 0.4553
Epoch [160/650], Validation Loss: 0.0074, Validation L1: 0.5712, Smoothed Validation Loss: 0.0074
Epoch [161/650], Train Loss: 0.0047, Train L1 Loss: 0.4553
Epoch [161/650], Validation Loss: 0.0074, Validation L1: 0.5712, Smoothed Validation Loss: 0.0074
Epoch [162/650], Train Loss: 0.0047, Train L1 Loss: 0.4553
Epoch [162/650], Validation Loss: 0.0074, Validation L1: 0.5712, Smoothed Validation Loss: 0.0074
Epoch [163/650], Train Loss: 0.0047, Train L1 Loss: 0.4553
Epoch [163/650], Validation Loss: 0.0074, Validation L1: 0.5712, Smoothed Validation Loss: 0.0074
Epoch [164/650], Train Loss: 0.0047, Train L1 Loss: 0.4553
Epoch [164/650], Validation Loss: 0.0074, Validation L1: 0.5712, Smoothed Validation Loss: 0.0074
Epoch 00164: reducing learning rate of group 0 to 2.4414e-07.
Epoch [165/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [165/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0074
Epoch [166/650], Train Loss: 0.0047, Train L1 Loss: 0.4552
Epoch [166/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0074
Epoch [167/650], Train Loss: 0.0047, Train L1 Loss: 0.4552
Epoch [167/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0074
Epoch [168/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [168/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0074
Epoch [169/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [169/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0074
Epoch [170/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [170/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0074
Epoch 00170: reducing learning rate of group 0 to 1.2207e-07.
Epoch [171/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [171/650], Validation Loss: 0.0074, Validation L1: 0.5713, Smoothed Validation Loss: 0.0074
Epoch [172/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [172/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [173/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [173/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [174/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [174/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [175/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [175/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [176/650], Train Loss: 0.0047, Train L1 Loss: 0.4551
Epoch [176/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch 00176: reducing learning rate of group 0 to 6.1035e-08.
Epoch [177/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [177/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [178/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [178/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [179/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [179/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [180/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [180/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [181/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [181/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [182/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [182/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch 00182: reducing learning rate of group 0 to 3.0518e-08.
Epoch [183/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [183/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [184/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [184/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [185/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [185/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [186/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [186/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [187/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [187/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [188/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [188/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch 00188: reducing learning rate of group 0 to 1.5259e-08.
Epoch [189/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [189/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [190/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [190/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [191/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [191/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [192/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [192/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [193/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [193/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [194/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [194/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [195/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [195/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [196/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [196/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [197/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [197/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [198/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [198/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [199/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [199/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [200/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [200/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [201/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [201/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [202/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [202/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [203/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [203/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [204/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [204/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [205/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [205/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [206/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [206/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [207/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [207/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [208/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [208/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [209/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [209/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [210/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [210/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [211/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [211/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [212/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [212/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [213/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [213/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [214/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [214/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [215/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [215/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [216/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [216/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [217/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [217/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [218/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [218/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [219/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [219/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [220/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [220/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [221/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [221/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [222/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [222/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [223/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [223/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [224/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [224/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [225/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [225/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [226/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [226/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [227/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [227/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [228/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [228/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [229/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [229/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [230/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [230/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [231/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [231/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [232/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [232/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [233/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [233/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [234/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [234/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [235/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [235/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [236/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [236/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [237/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [237/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [238/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [238/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [239/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [239/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [240/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [240/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [241/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [241/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [242/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [242/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [243/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [243/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [244/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [244/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [245/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [245/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [246/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [246/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [247/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [247/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [248/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [248/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [249/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [249/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [250/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [250/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [251/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [251/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [252/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [252/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [253/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [253/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [254/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [254/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [255/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [255/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [256/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [256/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [257/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [257/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [258/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [258/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [259/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [259/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [260/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [260/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [261/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [261/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [262/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [262/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [263/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [263/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [264/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [264/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [265/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [265/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [266/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [266/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [267/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [267/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [268/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [268/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [269/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [269/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [270/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [270/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [271/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [271/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [272/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [272/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [273/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [273/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [274/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [274/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [275/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [275/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [276/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [276/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [277/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [277/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [278/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [278/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [279/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [279/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [280/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [280/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [281/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [281/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [282/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [282/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [283/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [283/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [284/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [284/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [285/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [285/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [286/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [286/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [287/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [287/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [288/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [288/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [289/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [289/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [290/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [290/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [291/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [291/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [292/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [292/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [293/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [293/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [294/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [294/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [295/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [295/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [296/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [296/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [297/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [297/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [298/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [298/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [299/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [299/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [300/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [300/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [301/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [301/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [302/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [302/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [303/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [303/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [304/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [304/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [305/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [305/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [306/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [306/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [307/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [307/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [308/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [308/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [309/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [309/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [310/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [310/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [311/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [311/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [312/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [312/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [313/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [313/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [314/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [314/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [315/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [315/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [316/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [316/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [317/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [317/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [318/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [318/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [319/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [319/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [320/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [320/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [321/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [321/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [322/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [322/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [323/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [323/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [324/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [324/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [325/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [325/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [326/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [326/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [327/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [327/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [328/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [328/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [329/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [329/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [330/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [330/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [331/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [331/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [332/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [332/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [333/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [333/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [334/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [334/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [335/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [335/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [336/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [336/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [337/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [337/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [338/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [338/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [339/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [339/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [340/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [340/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [341/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [341/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [342/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [342/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [343/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [343/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [344/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [344/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [345/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [345/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [346/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [346/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [347/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [347/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [348/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [348/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [349/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [349/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [350/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [350/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [351/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [351/650], Validation Loss: 0.0074, Validation L1: 0.5714, Smoothed Validation Loss: 0.0074
Epoch [352/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [352/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [353/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [353/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [354/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [354/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [355/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [355/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [356/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [356/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [357/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [357/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [358/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [358/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [359/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [359/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [360/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [360/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [361/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [361/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [362/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [362/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [363/650], Train Loss: 0.0047, Train L1 Loss: 0.4550
Epoch [363/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [364/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [364/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [365/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [365/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [366/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [366/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [367/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [367/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [368/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [368/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [369/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [369/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [370/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [370/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [371/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [371/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [372/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [372/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [373/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [373/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [374/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [374/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [375/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [375/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [376/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [376/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [377/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [377/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [378/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [378/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [379/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [379/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [380/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [380/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [381/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [381/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [382/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [382/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [383/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [383/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [384/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [384/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [385/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [385/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [386/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [386/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [387/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [387/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [388/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [388/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [389/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [389/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [390/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [390/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [391/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [391/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [392/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [392/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [393/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [393/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [394/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [394/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [395/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [395/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [396/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [396/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [397/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [397/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [398/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [398/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [399/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [399/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [400/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [400/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [401/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [401/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [402/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [402/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [403/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [403/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [404/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [404/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [405/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [405/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [406/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [406/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [407/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [407/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [408/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [408/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [409/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [409/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [410/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [410/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [411/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [411/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [412/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [412/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [413/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [413/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [414/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [414/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [415/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [415/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [416/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [416/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [417/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [417/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [418/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [418/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [419/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [419/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [420/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [420/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [421/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [421/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [422/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [422/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [423/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [423/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [424/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [424/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [425/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [425/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [426/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [426/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [427/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [427/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [428/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [428/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [429/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [429/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [430/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [430/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [431/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [431/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [432/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [432/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [433/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [433/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [434/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [434/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [435/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [435/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [436/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [436/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [437/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [437/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [438/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [438/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [439/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [439/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [440/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [440/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [441/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [441/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [442/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [442/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [443/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [443/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [444/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [444/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [445/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [445/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [446/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [446/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [447/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [447/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [448/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [448/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [449/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [449/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [450/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [450/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [451/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [451/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [452/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [452/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [453/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [453/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [454/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [454/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [455/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [455/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [456/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [456/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [457/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [457/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [458/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [458/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [459/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [459/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [460/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [460/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [461/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [461/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [462/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [462/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [463/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [463/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [464/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [464/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [465/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [465/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [466/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [466/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [467/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [467/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [468/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [468/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [469/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [469/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [470/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [470/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [471/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [471/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [472/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [472/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [473/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [473/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [474/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [474/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [475/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [475/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [476/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [476/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [477/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [477/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [478/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [478/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [479/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [479/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [480/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [480/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [481/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [481/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [482/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [482/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [483/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [483/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [484/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [484/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [485/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [485/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [486/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [486/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [487/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [487/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [488/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [488/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [489/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [489/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [490/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [490/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [491/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [491/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [492/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [492/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [493/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [493/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [494/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [494/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [495/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [495/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [496/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [496/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [497/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [497/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [498/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [498/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [499/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [499/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [500/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [500/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [501/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [501/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [502/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [502/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [503/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [503/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [504/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [504/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [505/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [505/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [506/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [506/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [507/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [507/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [508/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [508/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [509/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [509/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [510/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [510/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [511/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [511/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [512/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [512/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [513/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [513/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [514/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [514/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [515/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [515/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [516/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [516/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [517/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [517/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [518/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [518/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [519/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [519/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [520/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [520/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [521/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [521/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [522/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [522/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [523/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [523/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [524/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [524/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [525/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [525/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [526/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [526/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [527/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [527/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [528/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [528/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [529/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [529/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [530/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [530/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [531/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [531/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [532/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [532/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [533/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [533/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [534/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [534/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [535/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [535/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [536/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [536/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [537/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [537/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [538/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [538/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [539/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [539/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [540/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [540/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [541/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [541/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [542/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [542/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [543/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [543/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [544/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [544/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [545/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [545/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [546/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [546/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [547/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [547/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [548/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [548/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [549/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [549/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [550/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [550/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [551/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [551/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [552/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [552/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [553/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [553/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [554/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [554/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [555/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [555/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [556/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [556/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [557/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [557/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [558/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [558/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [559/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [559/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [560/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [560/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [561/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [561/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [562/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [562/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [563/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [563/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [564/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [564/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [565/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [565/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [566/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [566/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [567/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [567/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [568/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [568/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [569/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [569/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [570/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [570/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [571/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [571/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [572/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [572/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [573/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [573/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [574/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [574/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [575/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [575/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [576/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [576/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [577/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [577/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [578/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [578/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [579/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [579/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [580/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [580/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [581/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [581/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [582/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [582/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [583/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [583/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [584/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [584/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [585/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [585/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [586/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [586/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [587/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [587/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [588/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [588/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [589/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [589/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [590/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [590/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [591/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [591/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [592/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [592/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [593/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [593/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [594/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [594/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [595/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [595/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [596/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [596/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [597/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [597/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [598/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [598/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [599/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [599/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [600/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [600/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [601/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [601/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [602/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [602/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [603/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [603/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [604/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [604/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [605/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [605/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [606/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [606/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [607/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [607/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [608/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [608/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [609/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [609/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [610/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [610/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [611/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [611/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [612/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [612/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [613/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [613/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [614/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [614/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [615/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [615/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [616/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [616/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [617/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [617/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [618/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [618/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [619/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [619/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [620/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [620/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [621/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [621/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [622/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [622/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [623/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [623/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [624/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [624/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [625/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [625/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [626/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [626/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [627/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [627/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [628/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [628/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [629/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [629/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [630/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [630/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [631/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [631/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [632/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [632/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [633/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [633/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [634/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [634/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [635/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [635/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [636/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [636/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [637/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [637/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [638/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [638/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [639/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [639/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [640/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [640/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [641/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [641/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [642/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [642/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [643/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [643/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [644/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [644/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [645/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [645/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [646/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [646/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [647/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [647/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [648/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [648/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [649/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [649/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
Epoch [650/650], Train Loss: 0.0047, Train L1 Loss: 0.4549
Epoch [650/650], Validation Loss: 0.0074, Validation L1: 0.5715, Smoothed Validation Loss: 0.0074
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19673446: <WorkingSetup_12> in cluster <dcc> Done

Job <WorkingSetup_12> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Sat Dec  2 18:17:09 2023
Job was executed on host(s) <4*n-62-18-13>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Mon Dec  4 01:42:00 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Mon Dec  4 01:42:00 2023
Terminated at Mon Dec  4 12:57:56 2023
Results reported at Mon Dec  4 12:57:56 2023

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

    CPU time :                                   40988.39 sec.
    Max Memory :                                 1947 MB
    Average Memory :                             1933.70 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63589.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   40556 sec.
    Turnaround time :                            153647 sec.

The output (if any) is above this job summary.

