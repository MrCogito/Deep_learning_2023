
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
| <c>name</c>       | <d>str</d>        | <j>"13WorkingSetup-0"</j> |
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
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231204_035834-gjfsib0h
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 13WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/gjfsib0h
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:40,327] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7f67d2c71a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:40,492] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpvn17ihul.py line 218 
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,212] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpvn17ihul.py line 117 
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,666] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpvn17ihul.py line 90 
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:42,800] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:43,310] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:43,548] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:44,056] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 03:58:44,989] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.117 MB uploadedwandb: / 0.005 MB of 0.117 MB uploadedwandb: - 0.005 MB of 0.117 MB uploadedwandb: \ 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▅▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▆▅▄▃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▄▆▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▄▆▁▃▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.00817
wandb:     train l1 loss 0.50095
wandb:        train_loss 0.0056
wandb:       val l1 loss 0.60921
wandb:          val loss 0.00817
wandb: 
wandb: 🚀 View run 13WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/gjfsib0h
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231204_035834-gjfsib0h/logs
Epoch [1/650], Train Loss: 0.0410, Train L1 Loss: 1.0117
Epoch [1/650], Validation Loss: 0.0139, Validation L1: 0.8402, Smoothed Validation Loss: 0.0139
Epoch [2/650], Train Loss: 0.0137, Train L1 Loss: 0.8384
Epoch [2/650], Validation Loss: 0.0121, Validation L1: 0.7966, Smoothed Validation Loss: 0.0138
Epoch [3/650], Train Loss: 0.0119, Train L1 Loss: 0.7851
Epoch [3/650], Validation Loss: 0.0107, Validation L1: 0.7438, Smoothed Validation Loss: 0.0134
Epoch [4/650], Train Loss: 0.0111, Train L1 Loss: 0.7562
Epoch [4/650], Validation Loss: 0.0107, Validation L1: 0.7287, Smoothed Validation Loss: 0.0132
Epoch [5/650], Train Loss: 0.0103, Train L1 Loss: 0.7232
Epoch [5/650], Validation Loss: 0.0097, Validation L1: 0.6957, Smoothed Validation Loss: 0.0128
Epoch [6/650], Train Loss: 0.0100, Train L1 Loss: 0.7113
Epoch [6/650], Validation Loss: 0.0096, Validation L1: 0.6842, Smoothed Validation Loss: 0.0125
Epoch [7/650], Train Loss: 0.0098, Train L1 Loss: 0.7045
Epoch [7/650], Validation Loss: 0.0100, Validation L1: 0.6946, Smoothed Validation Loss: 0.0123
Epoch [8/650], Train Loss: 0.0097, Train L1 Loss: 0.6979
Epoch [8/650], Validation Loss: 0.0098, Validation L1: 0.6892, Smoothed Validation Loss: 0.0120
Epoch [9/650], Train Loss: 0.0096, Train L1 Loss: 0.6934
Epoch [9/650], Validation Loss: 0.0096, Validation L1: 0.6845, Smoothed Validation Loss: 0.0118
Epoch [10/650], Train Loss: 0.0095, Train L1 Loss: 0.6890
Epoch [10/650], Validation Loss: 0.0094, Validation L1: 0.6715, Smoothed Validation Loss: 0.0115
Epoch [11/650], Train Loss: 0.0094, Train L1 Loss: 0.6843
Epoch [11/650], Validation Loss: 0.0093, Validation L1: 0.6706, Smoothed Validation Loss: 0.0113
Epoch [12/650], Train Loss: 0.0093, Train L1 Loss: 0.6800
Epoch [12/650], Validation Loss: 0.0092, Validation L1: 0.6668, Smoothed Validation Loss: 0.0111
Epoch [13/650], Train Loss: 0.0092, Train L1 Loss: 0.6748
Epoch [13/650], Validation Loss: 0.0090, Validation L1: 0.6590, Smoothed Validation Loss: 0.0109
Epoch [14/650], Train Loss: 0.0090, Train L1 Loss: 0.6697
Epoch [14/650], Validation Loss: 0.0089, Validation L1: 0.6557, Smoothed Validation Loss: 0.0107
Epoch [15/650], Train Loss: 0.0090, Train L1 Loss: 0.6675
Epoch [15/650], Validation Loss: 0.0089, Validation L1: 0.6573, Smoothed Validation Loss: 0.0105
Epoch [16/650], Train Loss: 0.0089, Train L1 Loss: 0.6614
Epoch [16/650], Validation Loss: 0.0089, Validation L1: 0.6516, Smoothed Validation Loss: 0.0104
Epoch [17/650], Train Loss: 0.0087, Train L1 Loss: 0.6555
Epoch [17/650], Validation Loss: 0.0089, Validation L1: 0.6514, Smoothed Validation Loss: 0.0102
Epoch [18/650], Train Loss: 0.0087, Train L1 Loss: 0.6526
Epoch [18/650], Validation Loss: 0.0088, Validation L1: 0.6436, Smoothed Validation Loss: 0.0101
Epoch [19/650], Train Loss: 0.0086, Train L1 Loss: 0.6505
Epoch [19/650], Validation Loss: 0.0088, Validation L1: 0.6424, Smoothed Validation Loss: 0.0099
Epoch [20/650], Train Loss: 0.0085, Train L1 Loss: 0.6458
Epoch [20/650], Validation Loss: 0.0093, Validation L1: 0.6540, Smoothed Validation Loss: 0.0099
Epoch [21/650], Train Loss: 0.0085, Train L1 Loss: 0.6442
Epoch [21/650], Validation Loss: 0.0089, Validation L1: 0.6428, Smoothed Validation Loss: 0.0098
Epoch [22/650], Train Loss: 0.0085, Train L1 Loss: 0.6429
Epoch [22/650], Validation Loss: 0.0088, Validation L1: 0.6458, Smoothed Validation Loss: 0.0097
Epoch [23/650], Train Loss: 0.0084, Train L1 Loss: 0.6392
Epoch [23/650], Validation Loss: 0.0086, Validation L1: 0.6354, Smoothed Validation Loss: 0.0096
Epoch [24/650], Train Loss: 0.0083, Train L1 Loss: 0.6366
Epoch [24/650], Validation Loss: 0.0088, Validation L1: 0.6417, Smoothed Validation Loss: 0.0095
Epoch [25/650], Train Loss: 0.0083, Train L1 Loss: 0.6354
Epoch [25/650], Validation Loss: 0.0084, Validation L1: 0.6305, Smoothed Validation Loss: 0.0094
Epoch [26/650], Train Loss: 0.0082, Train L1 Loss: 0.6324
Epoch [26/650], Validation Loss: 0.0085, Validation L1: 0.6317, Smoothed Validation Loss: 0.0093
Epoch [27/650], Train Loss: 0.0082, Train L1 Loss: 0.6323
Epoch [27/650], Validation Loss: 0.0084, Validation L1: 0.6292, Smoothed Validation Loss: 0.0092
Epoch [28/650], Train Loss: 0.0082, Train L1 Loss: 0.6291
Epoch [28/650], Validation Loss: 0.0084, Validation L1: 0.6263, Smoothed Validation Loss: 0.0091
Epoch [29/650], Train Loss: 0.0081, Train L1 Loss: 0.6259
Epoch [29/650], Validation Loss: 0.0084, Validation L1: 0.6311, Smoothed Validation Loss: 0.0091
Epoch [30/650], Train Loss: 0.0081, Train L1 Loss: 0.6241
Epoch [30/650], Validation Loss: 0.0084, Validation L1: 0.6328, Smoothed Validation Loss: 0.0090
Epoch [31/650], Train Loss: 0.0080, Train L1 Loss: 0.6229
Epoch [31/650], Validation Loss: 0.0085, Validation L1: 0.6325, Smoothed Validation Loss: 0.0089
Epoch [32/650], Train Loss: 0.0080, Train L1 Loss: 0.6230
Epoch [32/650], Validation Loss: 0.0087, Validation L1: 0.6303, Smoothed Validation Loss: 0.0089
Epoch [33/650], Train Loss: 0.0080, Train L1 Loss: 0.6193
Epoch [33/650], Validation Loss: 0.0084, Validation L1: 0.6247, Smoothed Validation Loss: 0.0089
Epoch [34/650], Train Loss: 0.0079, Train L1 Loss: 0.6178
Epoch [34/650], Validation Loss: 0.0084, Validation L1: 0.6232, Smoothed Validation Loss: 0.0088
Epoch [35/650], Train Loss: 0.0079, Train L1 Loss: 0.6151
Epoch [35/650], Validation Loss: 0.0085, Validation L1: 0.6296, Smoothed Validation Loss: 0.0088
Epoch [36/650], Train Loss: 0.0079, Train L1 Loss: 0.6145
Epoch [36/650], Validation Loss: 0.0088, Validation L1: 0.6337, Smoothed Validation Loss: 0.0088
Epoch [37/650], Train Loss: 0.0079, Train L1 Loss: 0.6143
Epoch [37/650], Validation Loss: 0.0088, Validation L1: 0.6399, Smoothed Validation Loss: 0.0088
Epoch [38/650], Train Loss: 0.0078, Train L1 Loss: 0.6127
Epoch [38/650], Validation Loss: 0.0087, Validation L1: 0.6400, Smoothed Validation Loss: 0.0088
Epoch [39/650], Train Loss: 0.0078, Train L1 Loss: 0.6103
Epoch [39/650], Validation Loss: 0.0087, Validation L1: 0.6328, Smoothed Validation Loss: 0.0088
Epoch [40/650], Train Loss: 0.0079, Train L1 Loss: 0.6150
Epoch [40/650], Validation Loss: 0.0091, Validation L1: 0.6604, Smoothed Validation Loss: 0.0088
Epoch [41/650], Train Loss: 0.0080, Train L1 Loss: 0.6176
Epoch [41/650], Validation Loss: 0.0085, Validation L1: 0.6279, Smoothed Validation Loss: 0.0088
Epoch [42/650], Train Loss: 0.0077, Train L1 Loss: 0.6074
Epoch [42/650], Validation Loss: 0.0087, Validation L1: 0.6364, Smoothed Validation Loss: 0.0088
Epoch [43/650], Train Loss: 0.0077, Train L1 Loss: 0.6062
Epoch [43/650], Validation Loss: 0.0086, Validation L1: 0.6371, Smoothed Validation Loss: 0.0088
Epoch [44/650], Train Loss: 0.0077, Train L1 Loss: 0.6073
Epoch [44/650], Validation Loss: 0.0085, Validation L1: 0.6295, Smoothed Validation Loss: 0.0087
Epoch [45/650], Train Loss: 0.0077, Train L1 Loss: 0.6053
Epoch [45/650], Validation Loss: 0.0085, Validation L1: 0.6317, Smoothed Validation Loss: 0.0087
Epoch [46/650], Train Loss: 0.0077, Train L1 Loss: 0.6064
Epoch [46/650], Validation Loss: 0.0085, Validation L1: 0.6283, Smoothed Validation Loss: 0.0087
Epoch [47/650], Train Loss: 0.0076, Train L1 Loss: 0.6013
Epoch [47/650], Validation Loss: 0.0084, Validation L1: 0.6224, Smoothed Validation Loss: 0.0087
Epoch [48/650], Train Loss: 0.0079, Train L1 Loss: 0.6142
Epoch [48/650], Validation Loss: 0.0104, Validation L1: 0.7212, Smoothed Validation Loss: 0.0088
Epoch [49/650], Train Loss: 0.0093, Train L1 Loss: 0.6795
Epoch [49/650], Validation Loss: 0.0089, Validation L1: 0.6495, Smoothed Validation Loss: 0.0088
Epoch [50/650], Train Loss: 0.0085, Train L1 Loss: 0.6436
Epoch [50/650], Validation Loss: 0.0086, Validation L1: 0.6356, Smoothed Validation Loss: 0.0088
Epoch [51/650], Train Loss: 0.0082, Train L1 Loss: 0.6290
Epoch [51/650], Validation Loss: 0.0083, Validation L1: 0.6229, Smoothed Validation Loss: 0.0088
Epoch [52/650], Train Loss: 0.0081, Train L1 Loss: 0.6248
Epoch [52/650], Validation Loss: 0.0084, Validation L1: 0.6223, Smoothed Validation Loss: 0.0087
Epoch [53/650], Train Loss: 0.0080, Train L1 Loss: 0.6171
Epoch [53/650], Validation Loss: 0.0084, Validation L1: 0.6288, Smoothed Validation Loss: 0.0087
Epoch 00053: reducing learning rate of group 0 to 5.0000e-04.
Epoch [54/650], Train Loss: 0.0074, Train L1 Loss: 0.5921
Epoch [54/650], Validation Loss: 0.0079, Validation L1: 0.6041, Smoothed Validation Loss: 0.0086
Epoch [55/650], Train Loss: 0.0073, Train L1 Loss: 0.5849
Epoch [55/650], Validation Loss: 0.0079, Validation L1: 0.6039, Smoothed Validation Loss: 0.0085
Epoch [56/650], Train Loss: 0.0072, Train L1 Loss: 0.5806
Epoch [56/650], Validation Loss: 0.0079, Validation L1: 0.6055, Smoothed Validation Loss: 0.0085
Epoch [57/650], Train Loss: 0.0071, Train L1 Loss: 0.5760
Epoch [57/650], Validation Loss: 0.0079, Validation L1: 0.6057, Smoothed Validation Loss: 0.0084
Epoch [58/650], Train Loss: 0.0070, Train L1 Loss: 0.5733
Epoch [58/650], Validation Loss: 0.0081, Validation L1: 0.6094, Smoothed Validation Loss: 0.0084
Epoch [59/650], Train Loss: 0.0070, Train L1 Loss: 0.5706
Epoch [59/650], Validation Loss: 0.0080, Validation L1: 0.6087, Smoothed Validation Loss: 0.0084
Epoch [60/650], Train Loss: 0.0069, Train L1 Loss: 0.5675
Epoch [60/650], Validation Loss: 0.0080, Validation L1: 0.6084, Smoothed Validation Loss: 0.0083
Epoch [61/650], Train Loss: 0.0069, Train L1 Loss: 0.5650
Epoch [61/650], Validation Loss: 0.0081, Validation L1: 0.6093, Smoothed Validation Loss: 0.0083
Epoch [62/650], Train Loss: 0.0068, Train L1 Loss: 0.5632
Epoch [62/650], Validation Loss: 0.0080, Validation L1: 0.6086, Smoothed Validation Loss: 0.0083
Epoch [63/650], Train Loss: 0.0068, Train L1 Loss: 0.5627
Epoch [63/650], Validation Loss: 0.0081, Validation L1: 0.6110, Smoothed Validation Loss: 0.0082
Epoch [64/650], Train Loss: 0.0068, Train L1 Loss: 0.5609
Epoch [64/650], Validation Loss: 0.0080, Validation L1: 0.6079, Smoothed Validation Loss: 0.0082
Epoch [65/650], Train Loss: 0.0067, Train L1 Loss: 0.5588
Epoch [65/650], Validation Loss: 0.0081, Validation L1: 0.6103, Smoothed Validation Loss: 0.0082
Epoch [66/650], Train Loss: 0.0067, Train L1 Loss: 0.5606
Epoch [66/650], Validation Loss: 0.0080, Validation L1: 0.6089, Smoothed Validation Loss: 0.0082
Epoch [67/650], Train Loss: 0.0067, Train L1 Loss: 0.5572
Epoch [67/650], Validation Loss: 0.0081, Validation L1: 0.6117, Smoothed Validation Loss: 0.0082
Epoch [68/650], Train Loss: 0.0066, Train L1 Loss: 0.5554
Epoch [68/650], Validation Loss: 0.0081, Validation L1: 0.6119, Smoothed Validation Loss: 0.0082
Epoch [69/650], Train Loss: 0.0066, Train L1 Loss: 0.5547
Epoch [69/650], Validation Loss: 0.0081, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [70/650], Train Loss: 0.0066, Train L1 Loss: 0.5537
Epoch [70/650], Validation Loss: 0.0081, Validation L1: 0.6142, Smoothed Validation Loss: 0.0082
Epoch [71/650], Train Loss: 0.0065, Train L1 Loss: 0.5519
Epoch [71/650], Validation Loss: 0.0083, Validation L1: 0.6193, Smoothed Validation Loss: 0.0082
Epoch [72/650], Train Loss: 0.0065, Train L1 Loss: 0.5509
Epoch [72/650], Validation Loss: 0.0083, Validation L1: 0.6213, Smoothed Validation Loss: 0.0082
Epoch [73/650], Train Loss: 0.0065, Train L1 Loss: 0.5504
Epoch [73/650], Validation Loss: 0.0083, Validation L1: 0.6180, Smoothed Validation Loss: 0.0082
Epoch [74/650], Train Loss: 0.0065, Train L1 Loss: 0.5496
Epoch [74/650], Validation Loss: 0.0084, Validation L1: 0.6233, Smoothed Validation Loss: 0.0082
Epoch [75/650], Train Loss: 0.0065, Train L1 Loss: 0.5490
Epoch [75/650], Validation Loss: 0.0083, Validation L1: 0.6199, Smoothed Validation Loss: 0.0082
Epoch [76/650], Train Loss: 0.0065, Train L1 Loss: 0.5495
Epoch [76/650], Validation Loss: 0.0083, Validation L1: 0.6187, Smoothed Validation Loss: 0.0082
Epoch 00076: reducing learning rate of group 0 to 2.5000e-04.
Epoch [77/650], Train Loss: 0.0064, Train L1 Loss: 0.5420
Epoch [77/650], Validation Loss: 0.0083, Validation L1: 0.6165, Smoothed Validation Loss: 0.0082
Epoch [78/650], Train Loss: 0.0062, Train L1 Loss: 0.5353
Epoch [78/650], Validation Loss: 0.0084, Validation L1: 0.6176, Smoothed Validation Loss: 0.0083
Epoch [79/650], Train Loss: 0.0061, Train L1 Loss: 0.5322
Epoch [79/650], Validation Loss: 0.0084, Validation L1: 0.6195, Smoothed Validation Loss: 0.0083
Epoch [80/650], Train Loss: 0.0061, Train L1 Loss: 0.5297
Epoch [80/650], Validation Loss: 0.0085, Validation L1: 0.6210, Smoothed Validation Loss: 0.0083
Epoch [81/650], Train Loss: 0.0060, Train L1 Loss: 0.5275
Epoch [81/650], Validation Loss: 0.0085, Validation L1: 0.6216, Smoothed Validation Loss: 0.0083
Epoch [82/650], Train Loss: 0.0060, Train L1 Loss: 0.5256
Epoch [82/650], Validation Loss: 0.0085, Validation L1: 0.6241, Smoothed Validation Loss: 0.0083
Epoch 00082: reducing learning rate of group 0 to 1.2500e-04.
Epoch [83/650], Train Loss: 0.0061, Train L1 Loss: 0.5270
Epoch [83/650], Validation Loss: 0.0083, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [84/650], Train Loss: 0.0060, Train L1 Loss: 0.5219
Epoch [84/650], Validation Loss: 0.0083, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [85/650], Train Loss: 0.0059, Train L1 Loss: 0.5191
Epoch [85/650], Validation Loss: 0.0083, Validation L1: 0.6172, Smoothed Validation Loss: 0.0083
Epoch [86/650], Train Loss: 0.0059, Train L1 Loss: 0.5170
Epoch [86/650], Validation Loss: 0.0083, Validation L1: 0.6176, Smoothed Validation Loss: 0.0083
Epoch [87/650], Train Loss: 0.0058, Train L1 Loss: 0.5151
Epoch [87/650], Validation Loss: 0.0083, Validation L1: 0.6181, Smoothed Validation Loss: 0.0083
Epoch [88/650], Train Loss: 0.0058, Train L1 Loss: 0.5134
Epoch [88/650], Validation Loss: 0.0083, Validation L1: 0.6187, Smoothed Validation Loss: 0.0083
Epoch 00088: reducing learning rate of group 0 to 6.2500e-05.
Epoch [89/650], Train Loss: 0.0059, Train L1 Loss: 0.5159
Epoch [89/650], Validation Loss: 0.0082, Validation L1: 0.6154, Smoothed Validation Loss: 0.0083
Epoch [90/650], Train Loss: 0.0058, Train L1 Loss: 0.5130
Epoch [90/650], Validation Loss: 0.0082, Validation L1: 0.6157, Smoothed Validation Loss: 0.0083
Epoch [91/650], Train Loss: 0.0058, Train L1 Loss: 0.5113
Epoch [91/650], Validation Loss: 0.0082, Validation L1: 0.6159, Smoothed Validation Loss: 0.0083
Epoch [92/650], Train Loss: 0.0057, Train L1 Loss: 0.5099
Epoch [92/650], Validation Loss: 0.0082, Validation L1: 0.6163, Smoothed Validation Loss: 0.0083
Epoch [93/650], Train Loss: 0.0057, Train L1 Loss: 0.5087
Epoch [93/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [94/650], Train Loss: 0.0057, Train L1 Loss: 0.5075
Epoch [94/650], Validation Loss: 0.0082, Validation L1: 0.6171, Smoothed Validation Loss: 0.0083
Epoch 00094: reducing learning rate of group 0 to 3.1250e-05.
Epoch [95/650], Train Loss: 0.0058, Train L1 Loss: 0.5103
Epoch [95/650], Validation Loss: 0.0082, Validation L1: 0.6136, Smoothed Validation Loss: 0.0083
Epoch [96/650], Train Loss: 0.0057, Train L1 Loss: 0.5084
Epoch [96/650], Validation Loss: 0.0082, Validation L1: 0.6136, Smoothed Validation Loss: 0.0083
Epoch [97/650], Train Loss: 0.0057, Train L1 Loss: 0.5074
Epoch [97/650], Validation Loss: 0.0082, Validation L1: 0.6137, Smoothed Validation Loss: 0.0082
Epoch [98/650], Train Loss: 0.0057, Train L1 Loss: 0.5066
Epoch [98/650], Validation Loss: 0.0082, Validation L1: 0.6138, Smoothed Validation Loss: 0.0082
Epoch [99/650], Train Loss: 0.0057, Train L1 Loss: 0.5058
Epoch [99/650], Validation Loss: 0.0082, Validation L1: 0.6139, Smoothed Validation Loss: 0.0082
Epoch [100/650], Train Loss: 0.0057, Train L1 Loss: 0.5051
Epoch [100/650], Validation Loss: 0.0082, Validation L1: 0.6141, Smoothed Validation Loss: 0.0082
Epoch 00100: reducing learning rate of group 0 to 1.5625e-05.
Epoch [101/650], Train Loss: 0.0057, Train L1 Loss: 0.5076
Epoch [101/650], Validation Loss: 0.0082, Validation L1: 0.6110, Smoothed Validation Loss: 0.0082
Epoch [102/650], Train Loss: 0.0057, Train L1 Loss: 0.5063
Epoch [102/650], Validation Loss: 0.0082, Validation L1: 0.6111, Smoothed Validation Loss: 0.0082
Epoch [103/650], Train Loss: 0.0057, Train L1 Loss: 0.5057
Epoch [103/650], Validation Loss: 0.0082, Validation L1: 0.6112, Smoothed Validation Loss: 0.0082
Epoch [104/650], Train Loss: 0.0057, Train L1 Loss: 0.5052
Epoch [104/650], Validation Loss: 0.0082, Validation L1: 0.6113, Smoothed Validation Loss: 0.0082
Epoch [105/650], Train Loss: 0.0057, Train L1 Loss: 0.5047
Epoch [105/650], Validation Loss: 0.0082, Validation L1: 0.6113, Smoothed Validation Loss: 0.0082
Epoch [106/650], Train Loss: 0.0057, Train L1 Loss: 0.5043
Epoch [106/650], Validation Loss: 0.0082, Validation L1: 0.6114, Smoothed Validation Loss: 0.0082
Epoch 00106: reducing learning rate of group 0 to 7.8125e-06.
Epoch [107/650], Train Loss: 0.0057, Train L1 Loss: 0.5055
Epoch [107/650], Validation Loss: 0.0082, Validation L1: 0.6098, Smoothed Validation Loss: 0.0082
Epoch [108/650], Train Loss: 0.0057, Train L1 Loss: 0.5046
Epoch [108/650], Validation Loss: 0.0082, Validation L1: 0.6098, Smoothed Validation Loss: 0.0082
Epoch [109/650], Train Loss: 0.0057, Train L1 Loss: 0.5043
Epoch [109/650], Validation Loss: 0.0082, Validation L1: 0.6098, Smoothed Validation Loss: 0.0082
Epoch [110/650], Train Loss: 0.0057, Train L1 Loss: 0.5040
Epoch [110/650], Validation Loss: 0.0082, Validation L1: 0.6099, Smoothed Validation Loss: 0.0082
Epoch [111/650], Train Loss: 0.0057, Train L1 Loss: 0.5037
Epoch [111/650], Validation Loss: 0.0082, Validation L1: 0.6099, Smoothed Validation Loss: 0.0082
Epoch [112/650], Train Loss: 0.0056, Train L1 Loss: 0.5034
Epoch [112/650], Validation Loss: 0.0082, Validation L1: 0.6100, Smoothed Validation Loss: 0.0082
Epoch 00112: reducing learning rate of group 0 to 3.9063e-06.
Epoch [113/650], Train Loss: 0.0057, Train L1 Loss: 0.5036
Epoch [113/650], Validation Loss: 0.0082, Validation L1: 0.6093, Smoothed Validation Loss: 0.0082
Epoch [114/650], Train Loss: 0.0056, Train L1 Loss: 0.5032
Epoch [114/650], Validation Loss: 0.0082, Validation L1: 0.6093, Smoothed Validation Loss: 0.0082
Epoch [115/650], Train Loss: 0.0056, Train L1 Loss: 0.5030
Epoch [115/650], Validation Loss: 0.0082, Validation L1: 0.6093, Smoothed Validation Loss: 0.0082
Epoch [116/650], Train Loss: 0.0056, Train L1 Loss: 0.5029
Epoch [116/650], Validation Loss: 0.0082, Validation L1: 0.6093, Smoothed Validation Loss: 0.0082
Epoch [117/650], Train Loss: 0.0056, Train L1 Loss: 0.5027
Epoch [117/650], Validation Loss: 0.0082, Validation L1: 0.6093, Smoothed Validation Loss: 0.0082
Epoch [118/650], Train Loss: 0.0056, Train L1 Loss: 0.5026
Epoch [118/650], Validation Loss: 0.0082, Validation L1: 0.6094, Smoothed Validation Loss: 0.0082
Epoch 00118: reducing learning rate of group 0 to 1.9531e-06.
Epoch [119/650], Train Loss: 0.0056, Train L1 Loss: 0.5024
Epoch [119/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [120/650], Train Loss: 0.0056, Train L1 Loss: 0.5023
Epoch [120/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [121/650], Train Loss: 0.0056, Train L1 Loss: 0.5022
Epoch [121/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [122/650], Train Loss: 0.0056, Train L1 Loss: 0.5021
Epoch [122/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [123/650], Train Loss: 0.0056, Train L1 Loss: 0.5020
Epoch [123/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [124/650], Train Loss: 0.0056, Train L1 Loss: 0.5020
Epoch [124/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch 00124: reducing learning rate of group 0 to 9.7656e-07.
Epoch [125/650], Train Loss: 0.0056, Train L1 Loss: 0.5017
Epoch [125/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [126/650], Train Loss: 0.0056, Train L1 Loss: 0.5017
Epoch [126/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [127/650], Train Loss: 0.0056, Train L1 Loss: 0.5017
Epoch [127/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [128/650], Train Loss: 0.0056, Train L1 Loss: 0.5016
Epoch [128/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [129/650], Train Loss: 0.0056, Train L1 Loss: 0.5016
Epoch [129/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [130/650], Train Loss: 0.0056, Train L1 Loss: 0.5016
Epoch [130/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch 00130: reducing learning rate of group 0 to 4.8828e-07.
Epoch [131/650], Train Loss: 0.0056, Train L1 Loss: 0.5014
Epoch [131/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [132/650], Train Loss: 0.0056, Train L1 Loss: 0.5014
Epoch [132/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [133/650], Train Loss: 0.0056, Train L1 Loss: 0.5014
Epoch [133/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [134/650], Train Loss: 0.0056, Train L1 Loss: 0.5014
Epoch [134/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [135/650], Train Loss: 0.0056, Train L1 Loss: 0.5013
Epoch [135/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [136/650], Train Loss: 0.0056, Train L1 Loss: 0.5013
Epoch [136/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch 00136: reducing learning rate of group 0 to 2.4414e-07.
Epoch [137/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [137/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [138/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [138/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [139/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [139/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [140/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [140/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [141/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [141/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [142/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [142/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch 00142: reducing learning rate of group 0 to 1.2207e-07.
Epoch [143/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [143/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [144/650], Train Loss: 0.0056, Train L1 Loss: 0.5012
Epoch [144/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [145/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [145/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [146/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [146/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [147/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [147/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [148/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [148/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch 00148: reducing learning rate of group 0 to 6.1035e-08.
Epoch [149/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [149/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [150/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [150/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [151/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [151/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [152/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [152/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [153/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [153/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [154/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [154/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch 00154: reducing learning rate of group 0 to 3.0518e-08.
Epoch [155/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [155/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [156/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [156/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [157/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [157/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [158/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [158/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [159/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [159/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [160/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [160/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch 00160: reducing learning rate of group 0 to 1.5259e-08.
Epoch [161/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [161/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [162/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [162/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [163/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [163/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [164/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [164/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [165/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [165/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [166/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [166/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [167/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [167/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [168/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [168/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [169/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [169/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [170/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [170/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [171/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [171/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [172/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [172/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [173/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [173/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [174/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [174/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [175/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [175/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [176/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [176/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [177/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [177/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [178/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [178/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [179/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [179/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [180/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [180/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [181/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [181/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [182/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [182/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [183/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [183/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [184/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [184/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [185/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [185/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [186/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [186/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [187/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [187/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [188/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [188/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [189/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [189/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [190/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [190/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [191/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [191/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [192/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [192/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [193/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [193/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [194/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [194/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [195/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [195/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [196/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [196/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [197/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [197/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [198/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [198/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [199/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [199/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [200/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [200/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [201/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [201/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [202/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [202/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [203/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [203/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [204/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [204/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [205/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [205/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [206/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [206/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [207/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [207/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [208/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [208/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [209/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [209/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [210/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [210/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [211/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [211/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [212/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [212/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [213/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [213/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [214/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [214/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [215/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [215/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [216/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [216/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [217/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [217/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [218/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [218/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [219/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [219/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [220/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [220/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [221/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [221/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [222/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [222/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [223/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [223/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [224/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [224/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [225/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [225/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [226/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [226/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [227/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [227/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [228/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [228/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [229/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [229/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [230/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [230/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [231/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [231/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [232/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [232/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [233/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [233/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [234/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [234/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [235/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [235/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [236/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [236/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [237/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [237/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [238/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [238/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [239/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [239/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [240/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [240/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [241/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [241/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [242/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [242/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [243/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [243/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [244/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [244/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [245/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [245/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [246/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [246/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [247/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [247/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [248/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [248/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [249/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [249/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [250/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [250/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [251/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [251/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [252/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [252/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [253/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [253/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [254/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [254/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [255/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [255/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [256/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [256/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [257/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [257/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [258/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [258/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [259/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [259/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [260/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [260/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [261/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [261/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [262/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [262/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [263/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [263/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [264/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [264/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [265/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [265/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [266/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [266/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [267/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [267/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [268/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [268/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [269/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [269/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [270/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [270/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [271/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [271/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [272/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [272/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [273/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [273/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [274/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [274/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [275/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [275/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [276/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [276/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [277/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [277/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [278/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [278/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [279/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [279/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [280/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [280/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [281/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [281/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [282/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [282/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [283/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [283/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [284/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [284/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [285/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [285/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [286/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [286/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [287/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [287/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [288/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [288/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [289/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [289/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [290/650], Train Loss: 0.0056, Train L1 Loss: 0.5011
Epoch [290/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [291/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [291/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [292/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [292/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [293/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [293/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [294/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [294/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [295/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [295/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [296/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [296/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [297/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [297/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [298/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [298/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [299/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [299/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [300/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [300/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [301/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [301/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [302/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [302/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [303/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [303/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [304/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [304/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [305/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [305/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [306/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [306/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [307/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [307/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [308/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [308/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [309/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [309/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [310/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [310/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [311/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [311/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [312/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [312/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [313/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [313/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [314/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [314/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [315/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [315/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [316/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [316/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [317/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [317/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [318/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [318/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [319/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [319/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [320/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [320/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [321/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [321/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [322/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [322/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [323/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [323/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [324/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [324/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [325/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [325/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [326/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [326/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [327/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [327/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [328/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [328/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [329/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [329/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [330/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [330/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [331/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [331/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [332/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [332/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [333/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [333/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [334/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [334/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [335/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [335/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [336/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [336/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [337/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [337/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [338/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [338/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [339/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [339/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [340/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [340/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [341/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [341/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [342/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [342/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [343/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [343/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [344/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [344/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [345/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [345/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [346/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [346/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [347/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [347/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [348/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [348/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [349/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [349/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [350/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [350/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [351/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [351/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [352/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [352/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [353/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [353/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [354/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [354/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [355/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [355/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [356/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [356/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [357/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [357/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [358/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [358/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [359/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [359/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [360/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [360/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [361/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [361/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [362/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [362/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [363/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [363/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [364/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [364/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [365/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [365/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [366/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [366/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [367/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [367/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [368/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [368/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [369/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [369/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [370/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [370/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [371/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [371/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [372/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [372/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [373/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [373/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [374/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [374/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [375/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [375/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [376/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [376/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [377/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [377/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [378/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [378/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [379/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [379/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [380/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [380/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [381/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [381/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [382/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [382/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [383/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [383/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [384/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [384/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [385/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [385/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [386/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [386/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [387/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [387/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [388/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [388/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [389/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [389/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [390/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [390/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [391/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [391/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [392/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [392/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [393/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [393/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [394/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [394/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [395/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [395/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [396/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [396/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [397/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [397/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [398/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [398/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [399/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [399/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [400/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [400/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [401/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [401/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [402/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [402/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [403/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [403/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [404/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [404/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [405/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [405/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [406/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [406/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [407/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [407/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [408/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [408/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [409/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [409/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [410/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [410/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [411/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [411/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [412/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [412/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [413/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [413/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [414/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [414/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [415/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [415/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [416/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [416/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [417/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [417/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [418/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [418/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [419/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [419/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [420/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [420/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [421/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [421/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [422/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [422/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [423/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [423/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [424/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [424/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [425/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [425/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [426/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [426/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [427/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [427/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [428/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [428/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [429/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [429/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [430/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [430/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [431/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [431/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [432/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [432/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [433/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [433/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [434/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [434/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [435/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [435/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [436/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [436/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [437/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [437/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [438/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [438/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [439/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [439/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [440/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [440/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [441/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [441/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [442/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [442/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [443/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [443/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [444/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [444/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [445/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [445/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [446/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [446/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [447/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [447/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [448/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [448/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [449/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [449/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [450/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [450/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [451/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [451/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [452/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [452/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [453/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [453/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [454/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [454/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [455/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [455/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [456/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [456/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [457/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [457/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [458/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [458/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [459/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [459/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [460/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [460/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [461/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [461/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [462/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [462/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [463/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [463/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [464/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [464/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [465/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [465/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [466/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [466/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [467/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [467/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [468/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [468/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [469/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [469/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [470/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [470/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [471/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [471/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [472/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [472/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [473/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [473/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [474/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [474/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [475/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [475/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [476/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [476/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [477/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [477/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [478/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [478/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [479/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [479/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [480/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [480/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [481/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [481/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [482/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [482/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [483/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [483/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [484/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [484/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [485/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [485/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [486/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [486/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [487/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [487/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [488/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [488/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [489/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [489/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [490/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [490/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [491/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [491/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [492/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [492/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [493/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [493/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [494/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [494/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [495/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [495/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [496/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [496/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [497/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [497/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [498/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [498/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [499/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [499/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [500/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [500/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [501/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [501/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [502/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [502/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [503/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [503/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [504/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [504/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [505/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [505/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [506/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [506/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [507/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [507/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [508/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [508/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [509/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [509/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [510/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [510/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [511/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [511/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [512/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [512/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [513/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [513/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [514/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [514/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [515/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [515/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [516/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [516/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [517/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [517/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [518/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [518/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [519/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [519/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [520/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [520/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [521/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [521/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [522/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [522/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [523/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [523/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [524/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [524/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [525/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [525/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [526/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [526/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [527/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [527/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [528/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [528/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [529/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [529/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [530/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [530/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [531/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [531/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [532/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [532/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [533/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [533/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [534/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [534/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [535/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [535/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [536/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [536/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [537/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [537/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [538/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [538/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [539/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [539/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [540/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [540/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [541/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [541/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [542/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [542/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [543/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [543/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [544/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [544/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [545/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [545/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [546/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [546/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [547/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [547/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [548/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [548/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [549/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [549/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [550/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [550/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [551/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [551/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [552/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [552/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [553/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [553/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [554/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [554/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [555/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [555/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [556/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [556/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [557/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [557/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [558/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [558/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [559/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [559/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [560/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [560/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [561/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [561/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [562/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [562/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [563/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [563/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [564/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [564/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [565/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [565/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [566/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [566/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [567/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [567/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [568/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [568/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [569/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [569/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [570/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [570/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [571/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [571/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [572/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [572/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [573/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [573/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [574/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [574/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [575/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [575/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [576/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [576/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [577/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [577/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [578/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [578/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [579/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [579/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [580/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [580/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [581/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [581/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [582/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [582/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [583/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [583/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [584/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [584/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [585/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [585/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [586/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [586/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [587/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [587/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [588/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [588/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [589/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [589/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [590/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [590/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [591/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [591/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [592/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [592/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [593/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [593/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [594/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [594/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [595/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [595/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [596/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [596/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [597/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [597/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [598/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [598/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [599/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [599/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [600/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [600/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [601/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [601/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [602/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [602/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [603/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [603/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [604/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [604/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [605/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [605/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [606/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [606/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [607/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [607/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [608/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [608/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [609/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [609/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [610/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [610/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [611/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [611/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [612/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [612/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [613/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [613/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [614/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [614/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [615/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [615/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [616/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [616/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [617/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [617/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [618/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [618/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [619/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [619/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [620/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [620/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [621/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [621/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [622/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [622/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [623/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [623/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [624/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [624/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [625/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [625/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [626/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [626/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [627/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [627/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [628/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [628/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [629/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [629/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [630/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [630/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [631/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [631/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [632/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [632/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [633/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [633/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [634/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [634/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [635/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [635/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [636/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [636/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [637/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [637/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [638/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [638/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [639/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [639/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [640/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [640/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [641/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [641/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [642/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [642/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [643/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [643/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [644/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [644/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [645/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [645/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [646/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [646/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [647/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [647/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [648/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [648/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [649/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [649/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
Epoch [650/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [650/650], Validation Loss: 0.0082, Validation L1: 0.6092, Smoothed Validation Loss: 0.0082
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19673447: <WorkingSetup_13> in cluster <dcc> Done

Job <WorkingSetup_13> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Sat Dec  2 18:17:09 2023
Job was executed on host(s) <4*n-62-18-13>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Mon Dec  4 03:58:22 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Mon Dec  4 03:58:22 2023
Terminated at Mon Dec  4 15:13:28 2023
Results reported at Mon Dec  4 15:13:28 2023

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

    CPU time :                                   40977.11 sec.
    Max Memory :                                 1943 MB
    Average Memory :                             1937.75 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63593.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   40506 sec.
    Turnaround time :                            161779 sec.

The output (if any) is above this job summary.

