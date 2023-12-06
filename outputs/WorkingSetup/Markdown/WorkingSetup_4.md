
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
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231201_215943-dj7m822y
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 4WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/dj7m822y
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 21:59:57,525] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7f55f784ca40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:00,841] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpoy0rvgks.py line 218 
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:05,778] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpoy0rvgks.py line 117 
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:06,334] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpoy0rvgks.py line 90 
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:06,488] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:07,138] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:09,468] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:10,629] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 22:00:11,753] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.005 MB uploadedwandb: / 0.005 MB of 0.005 MB uploadedwandb: - 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▄▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▅▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▆▅▃▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▃▂▂▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▄▂▂▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.00821
wandb:     train l1 loss 0.49343
wandb:        train_loss 0.00547
wandb:       val l1 loss 0.61311
wandb:          val loss 0.00821
wandb: 
wandb: 🚀 View run 4WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/dj7m822y
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231201_215943-dj7m822y/logs
Epoch [1/650], Train Loss: 0.0392, Train L1 Loss: 1.0097
Epoch [1/650], Validation Loss: 0.0138, Validation L1: 0.8395, Smoothed Validation Loss: 0.0138
Epoch [2/650], Train Loss: 0.0138, Train L1 Loss: 0.8407
Epoch [2/650], Validation Loss: 0.0125, Validation L1: 0.8037, Smoothed Validation Loss: 0.0137
Epoch [3/650], Train Loss: 0.0124, Train L1 Loss: 0.7989
Epoch [3/650], Validation Loss: 0.0109, Validation L1: 0.7571, Smoothed Validation Loss: 0.0134
Epoch [4/650], Train Loss: 0.0114, Train L1 Loss: 0.7667
Epoch [4/650], Validation Loss: 0.0105, Validation L1: 0.7337, Smoothed Validation Loss: 0.0131
Epoch [5/650], Train Loss: 0.0107, Train L1 Loss: 0.7404
Epoch [5/650], Validation Loss: 0.0098, Validation L1: 0.7110, Smoothed Validation Loss: 0.0128
Epoch [6/650], Train Loss: 0.0102, Train L1 Loss: 0.7185
Epoch [6/650], Validation Loss: 0.0099, Validation L1: 0.7006, Smoothed Validation Loss: 0.0125
Epoch [7/650], Train Loss: 0.0100, Train L1 Loss: 0.7098
Epoch [7/650], Validation Loss: 0.0100, Validation L1: 0.6969, Smoothed Validation Loss: 0.0123
Epoch [8/650], Train Loss: 0.0098, Train L1 Loss: 0.7022
Epoch [8/650], Validation Loss: 0.0099, Validation L1: 0.6945, Smoothed Validation Loss: 0.0120
Epoch [9/650], Train Loss: 0.0097, Train L1 Loss: 0.6973
Epoch [9/650], Validation Loss: 0.0100, Validation L1: 0.6971, Smoothed Validation Loss: 0.0118
Epoch [10/650], Train Loss: 0.0097, Train L1 Loss: 0.6950
Epoch [10/650], Validation Loss: 0.0100, Validation L1: 0.6899, Smoothed Validation Loss: 0.0116
Epoch [11/650], Train Loss: 0.0095, Train L1 Loss: 0.6892
Epoch [11/650], Validation Loss: 0.0097, Validation L1: 0.6843, Smoothed Validation Loss: 0.0114
Epoch [12/650], Train Loss: 0.0097, Train L1 Loss: 0.6978
Epoch [12/650], Validation Loss: 0.0096, Validation L1: 0.6804, Smoothed Validation Loss: 0.0113
Epoch [13/650], Train Loss: 0.0093, Train L1 Loss: 0.6828
Epoch [13/650], Validation Loss: 0.0096, Validation L1: 0.6749, Smoothed Validation Loss: 0.0111
Epoch [14/650], Train Loss: 0.0092, Train L1 Loss: 0.6768
Epoch [14/650], Validation Loss: 0.0094, Validation L1: 0.6705, Smoothed Validation Loss: 0.0109
Epoch [15/650], Train Loss: 0.0092, Train L1 Loss: 0.6726
Epoch [15/650], Validation Loss: 0.0092, Validation L1: 0.6630, Smoothed Validation Loss: 0.0108
Epoch [16/650], Train Loss: 0.0090, Train L1 Loss: 0.6679
Epoch [16/650], Validation Loss: 0.0090, Validation L1: 0.6529, Smoothed Validation Loss: 0.0106
Epoch [17/650], Train Loss: 0.0089, Train L1 Loss: 0.6638
Epoch [17/650], Validation Loss: 0.0089, Validation L1: 0.6497, Smoothed Validation Loss: 0.0104
Epoch [18/650], Train Loss: 0.0088, Train L1 Loss: 0.6598
Epoch [18/650], Validation Loss: 0.0088, Validation L1: 0.6462, Smoothed Validation Loss: 0.0102
Epoch [19/650], Train Loss: 0.0088, Train L1 Loss: 0.6556
Epoch [19/650], Validation Loss: 0.0091, Validation L1: 0.6475, Smoothed Validation Loss: 0.0101
Epoch [20/650], Train Loss: 0.0087, Train L1 Loss: 0.6522
Epoch [20/650], Validation Loss: 0.0089, Validation L1: 0.6436, Smoothed Validation Loss: 0.0100
Epoch [21/650], Train Loss: 0.0087, Train L1 Loss: 0.6526
Epoch [21/650], Validation Loss: 0.0088, Validation L1: 0.6389, Smoothed Validation Loss: 0.0099
Epoch [22/650], Train Loss: 0.0086, Train L1 Loss: 0.6456
Epoch [22/650], Validation Loss: 0.0087, Validation L1: 0.6397, Smoothed Validation Loss: 0.0098
Epoch [23/650], Train Loss: 0.0085, Train L1 Loss: 0.6439
Epoch [23/650], Validation Loss: 0.0088, Validation L1: 0.6387, Smoothed Validation Loss: 0.0097
Epoch [24/650], Train Loss: 0.0084, Train L1 Loss: 0.6410
Epoch [24/650], Validation Loss: 0.0088, Validation L1: 0.6352, Smoothed Validation Loss: 0.0096
Epoch [25/650], Train Loss: 0.0084, Train L1 Loss: 0.6387
Epoch [25/650], Validation Loss: 0.0086, Validation L1: 0.6301, Smoothed Validation Loss: 0.0095
Epoch [26/650], Train Loss: 0.0083, Train L1 Loss: 0.6349
Epoch [26/650], Validation Loss: 0.0087, Validation L1: 0.6392, Smoothed Validation Loss: 0.0094
Epoch [27/650], Train Loss: 0.0083, Train L1 Loss: 0.6339
Epoch [27/650], Validation Loss: 0.0087, Validation L1: 0.6379, Smoothed Validation Loss: 0.0093
Epoch [28/650], Train Loss: 0.0082, Train L1 Loss: 0.6312
Epoch [28/650], Validation Loss: 0.0087, Validation L1: 0.6376, Smoothed Validation Loss: 0.0093
Epoch [29/650], Train Loss: 0.0082, Train L1 Loss: 0.6295
Epoch [29/650], Validation Loss: 0.0087, Validation L1: 0.6372, Smoothed Validation Loss: 0.0092
Epoch [30/650], Train Loss: 0.0082, Train L1 Loss: 0.6278
Epoch [30/650], Validation Loss: 0.0088, Validation L1: 0.6368, Smoothed Validation Loss: 0.0092
Epoch [31/650], Train Loss: 0.0082, Train L1 Loss: 0.6277
Epoch [31/650], Validation Loss: 0.0087, Validation L1: 0.6344, Smoothed Validation Loss: 0.0091
Epoch [32/650], Train Loss: 0.0081, Train L1 Loss: 0.6252
Epoch [32/650], Validation Loss: 0.0087, Validation L1: 0.6437, Smoothed Validation Loss: 0.0091
Epoch [33/650], Train Loss: 0.0080, Train L1 Loss: 0.6220
Epoch [33/650], Validation Loss: 0.0085, Validation L1: 0.6335, Smoothed Validation Loss: 0.0090
Epoch [34/650], Train Loss: 0.0080, Train L1 Loss: 0.6216
Epoch [34/650], Validation Loss: 0.0086, Validation L1: 0.6282, Smoothed Validation Loss: 0.0090
Epoch [35/650], Train Loss: 0.0080, Train L1 Loss: 0.6206
Epoch [35/650], Validation Loss: 0.0086, Validation L1: 0.6302, Smoothed Validation Loss: 0.0089
Epoch [36/650], Train Loss: 0.0080, Train L1 Loss: 0.6188
Epoch [36/650], Validation Loss: 0.0086, Validation L1: 0.6336, Smoothed Validation Loss: 0.0089
Epoch [37/650], Train Loss: 0.0079, Train L1 Loss: 0.6167
Epoch [37/650], Validation Loss: 0.0090, Validation L1: 0.6456, Smoothed Validation Loss: 0.0089
Epoch [38/650], Train Loss: 0.0079, Train L1 Loss: 0.6176
Epoch [38/650], Validation Loss: 0.0087, Validation L1: 0.6367, Smoothed Validation Loss: 0.0089
Epoch [39/650], Train Loss: 0.0079, Train L1 Loss: 0.6155
Epoch [39/650], Validation Loss: 0.0088, Validation L1: 0.6417, Smoothed Validation Loss: 0.0089
Epoch [40/650], Train Loss: 0.0079, Train L1 Loss: 0.6134
Epoch [40/650], Validation Loss: 0.0085, Validation L1: 0.6298, Smoothed Validation Loss: 0.0089
Epoch [41/650], Train Loss: 0.0079, Train L1 Loss: 0.6141
Epoch [41/650], Validation Loss: 0.0087, Validation L1: 0.6357, Smoothed Validation Loss: 0.0088
Epoch [42/650], Train Loss: 0.0078, Train L1 Loss: 0.6119
Epoch [42/650], Validation Loss: 0.0089, Validation L1: 0.6459, Smoothed Validation Loss: 0.0088
Epoch [43/650], Train Loss: 0.0078, Train L1 Loss: 0.6132
Epoch [43/650], Validation Loss: 0.0086, Validation L1: 0.6318, Smoothed Validation Loss: 0.0088
Epoch [44/650], Train Loss: 0.0078, Train L1 Loss: 0.6118
Epoch [44/650], Validation Loss: 0.0084, Validation L1: 0.6253, Smoothed Validation Loss: 0.0088
Epoch [45/650], Train Loss: 0.0078, Train L1 Loss: 0.6101
Epoch [45/650], Validation Loss: 0.0086, Validation L1: 0.6366, Smoothed Validation Loss: 0.0088
Epoch [46/650], Train Loss: 0.0078, Train L1 Loss: 0.6089
Epoch [46/650], Validation Loss: 0.0086, Validation L1: 0.6297, Smoothed Validation Loss: 0.0088
Epoch [47/650], Train Loss: 0.0077, Train L1 Loss: 0.6081
Epoch [47/650], Validation Loss: 0.0091, Validation L1: 0.6466, Smoothed Validation Loss: 0.0088
Epoch [48/650], Train Loss: 0.0077, Train L1 Loss: 0.6073
Epoch [48/650], Validation Loss: 0.0090, Validation L1: 0.6415, Smoothed Validation Loss: 0.0088
Epoch [49/650], Train Loss: 0.0077, Train L1 Loss: 0.6053
Epoch [49/650], Validation Loss: 0.0086, Validation L1: 0.6300, Smoothed Validation Loss: 0.0088
Epoch [50/650], Train Loss: 0.0076, Train L1 Loss: 0.6039
Epoch [50/650], Validation Loss: 0.0086, Validation L1: 0.6279, Smoothed Validation Loss: 0.0088
Epoch [51/650], Train Loss: 0.0076, Train L1 Loss: 0.6037
Epoch [51/650], Validation Loss: 0.0090, Validation L1: 0.6423, Smoothed Validation Loss: 0.0088
Epoch [52/650], Train Loss: 0.0076, Train L1 Loss: 0.6023
Epoch [52/650], Validation Loss: 0.0091, Validation L1: 0.6433, Smoothed Validation Loss: 0.0088
Epoch 00052: reducing learning rate of group 0 to 5.0000e-04.
Epoch [53/650], Train Loss: 0.0072, Train L1 Loss: 0.5809
Epoch [53/650], Validation Loss: 0.0082, Validation L1: 0.6161, Smoothed Validation Loss: 0.0088
Epoch [54/650], Train Loss: 0.0070, Train L1 Loss: 0.5739
Epoch [54/650], Validation Loss: 0.0083, Validation L1: 0.6171, Smoothed Validation Loss: 0.0087
Epoch [55/650], Train Loss: 0.0070, Train L1 Loss: 0.5707
Epoch [55/650], Validation Loss: 0.0083, Validation L1: 0.6199, Smoothed Validation Loss: 0.0087
Epoch [56/650], Train Loss: 0.0069, Train L1 Loss: 0.5681
Epoch [56/650], Validation Loss: 0.0084, Validation L1: 0.6210, Smoothed Validation Loss: 0.0086
Epoch [57/650], Train Loss: 0.0069, Train L1 Loss: 0.5667
Epoch [57/650], Validation Loss: 0.0084, Validation L1: 0.6226, Smoothed Validation Loss: 0.0086
Epoch [58/650], Train Loss: 0.0068, Train L1 Loss: 0.5644
Epoch [58/650], Validation Loss: 0.0084, Validation L1: 0.6240, Smoothed Validation Loss: 0.0086
Epoch [59/650], Train Loss: 0.0068, Train L1 Loss: 0.5632
Epoch [59/650], Validation Loss: 0.0084, Validation L1: 0.6271, Smoothed Validation Loss: 0.0086
Epoch [60/650], Train Loss: 0.0068, Train L1 Loss: 0.5619
Epoch [60/650], Validation Loss: 0.0084, Validation L1: 0.6246, Smoothed Validation Loss: 0.0086
Epoch [61/650], Train Loss: 0.0095, Train L1 Loss: 0.6531
Epoch [61/650], Validation Loss: 0.0082, Validation L1: 0.6243, Smoothed Validation Loss: 0.0085
Epoch [62/650], Train Loss: 0.0074, Train L1 Loss: 0.5910
Epoch [62/650], Validation Loss: 0.0080, Validation L1: 0.6107, Smoothed Validation Loss: 0.0085
Epoch [63/650], Train Loss: 0.0070, Train L1 Loss: 0.5712
Epoch [63/650], Validation Loss: 0.0080, Validation L1: 0.6085, Smoothed Validation Loss: 0.0084
Epoch [64/650], Train Loss: 0.0068, Train L1 Loss: 0.5625
Epoch [64/650], Validation Loss: 0.0081, Validation L1: 0.6121, Smoothed Validation Loss: 0.0084
Epoch [65/650], Train Loss: 0.0067, Train L1 Loss: 0.5583
Epoch [65/650], Validation Loss: 0.0082, Validation L1: 0.6148, Smoothed Validation Loss: 0.0084
Epoch [66/650], Train Loss: 0.0067, Train L1 Loss: 0.5560
Epoch [66/650], Validation Loss: 0.0083, Validation L1: 0.6176, Smoothed Validation Loss: 0.0084
Epoch [67/650], Train Loss: 0.0066, Train L1 Loss: 0.5535
Epoch [67/650], Validation Loss: 0.0083, Validation L1: 0.6202, Smoothed Validation Loss: 0.0084
Epoch [68/650], Train Loss: 0.0066, Train L1 Loss: 0.5527
Epoch [68/650], Validation Loss: 0.0085, Validation L1: 0.6250, Smoothed Validation Loss: 0.0084
Epoch [69/650], Train Loss: 0.0065, Train L1 Loss: 0.5507
Epoch [69/650], Validation Loss: 0.0085, Validation L1: 0.6276, Smoothed Validation Loss: 0.0084
Epoch [70/650], Train Loss: 0.0065, Train L1 Loss: 0.5506
Epoch [70/650], Validation Loss: 0.0085, Validation L1: 0.6282, Smoothed Validation Loss: 0.0084
Epoch [71/650], Train Loss: 0.0065, Train L1 Loss: 0.5485
Epoch [71/650], Validation Loss: 0.0085, Validation L1: 0.6288, Smoothed Validation Loss: 0.0084
Epoch [72/650], Train Loss: 0.0065, Train L1 Loss: 0.5472
Epoch [72/650], Validation Loss: 0.0087, Validation L1: 0.6329, Smoothed Validation Loss: 0.0084
Epoch [73/650], Train Loss: 0.0064, Train L1 Loss: 0.5450
Epoch [73/650], Validation Loss: 0.0086, Validation L1: 0.6316, Smoothed Validation Loss: 0.0085
Epoch 00073: reducing learning rate of group 0 to 2.5000e-04.
Epoch [74/650], Train Loss: 0.0063, Train L1 Loss: 0.5377
Epoch [74/650], Validation Loss: 0.0084, Validation L1: 0.6262, Smoothed Validation Loss: 0.0085
Epoch [75/650], Train Loss: 0.0062, Train L1 Loss: 0.5319
Epoch [75/650], Validation Loss: 0.0085, Validation L1: 0.6278, Smoothed Validation Loss: 0.0085
Epoch [76/650], Train Loss: 0.0061, Train L1 Loss: 0.5290
Epoch [76/650], Validation Loss: 0.0085, Validation L1: 0.6283, Smoothed Validation Loss: 0.0085
Epoch [77/650], Train Loss: 0.0060, Train L1 Loss: 0.5270
Epoch [77/650], Validation Loss: 0.0086, Validation L1: 0.6293, Smoothed Validation Loss: 0.0085
Epoch [78/650], Train Loss: 0.0060, Train L1 Loss: 0.5250
Epoch [78/650], Validation Loss: 0.0086, Validation L1: 0.6301, Smoothed Validation Loss: 0.0085
Epoch [79/650], Train Loss: 0.0060, Train L1 Loss: 0.5234
Epoch [79/650], Validation Loss: 0.0086, Validation L1: 0.6321, Smoothed Validation Loss: 0.0085
Epoch 00079: reducing learning rate of group 0 to 1.2500e-04.
Epoch [80/650], Train Loss: 0.0061, Train L1 Loss: 0.5264
Epoch [80/650], Validation Loss: 0.0083, Validation L1: 0.6183, Smoothed Validation Loss: 0.0085
Epoch [81/650], Train Loss: 0.0060, Train L1 Loss: 0.5215
Epoch [81/650], Validation Loss: 0.0084, Validation L1: 0.6192, Smoothed Validation Loss: 0.0085
Epoch [82/650], Train Loss: 0.0059, Train L1 Loss: 0.5188
Epoch [82/650], Validation Loss: 0.0084, Validation L1: 0.6202, Smoothed Validation Loss: 0.0085
Epoch [83/650], Train Loss: 0.0059, Train L1 Loss: 0.5167
Epoch [83/650], Validation Loss: 0.0084, Validation L1: 0.6210, Smoothed Validation Loss: 0.0085
Epoch [84/650], Train Loss: 0.0058, Train L1 Loss: 0.5148
Epoch [84/650], Validation Loss: 0.0084, Validation L1: 0.6219, Smoothed Validation Loss: 0.0085
Epoch [85/650], Train Loss: 0.0058, Train L1 Loss: 0.5131
Epoch [85/650], Validation Loss: 0.0084, Validation L1: 0.6227, Smoothed Validation Loss: 0.0085
Epoch 00085: reducing learning rate of group 0 to 6.2500e-05.
Epoch [86/650], Train Loss: 0.0059, Train L1 Loss: 0.5172
Epoch [86/650], Validation Loss: 0.0083, Validation L1: 0.6232, Smoothed Validation Loss: 0.0084
Epoch [87/650], Train Loss: 0.0058, Train L1 Loss: 0.5148
Epoch [87/650], Validation Loss: 0.0083, Validation L1: 0.6217, Smoothed Validation Loss: 0.0084
Epoch [88/650], Train Loss: 0.0058, Train L1 Loss: 0.5125
Epoch [88/650], Validation Loss: 0.0084, Validation L1: 0.6227, Smoothed Validation Loss: 0.0084
Epoch [89/650], Train Loss: 0.0058, Train L1 Loss: 0.5111
Epoch [89/650], Validation Loss: 0.0084, Validation L1: 0.6227, Smoothed Validation Loss: 0.0084
Epoch [90/650], Train Loss: 0.0057, Train L1 Loss: 0.5097
Epoch [90/650], Validation Loss: 0.0084, Validation L1: 0.6233, Smoothed Validation Loss: 0.0084
Epoch [91/650], Train Loss: 0.0057, Train L1 Loss: 0.5085
Epoch [91/650], Validation Loss: 0.0084, Validation L1: 0.6238, Smoothed Validation Loss: 0.0084
Epoch 00091: reducing learning rate of group 0 to 3.1250e-05.
Epoch [92/650], Train Loss: 0.0058, Train L1 Loss: 0.5121
Epoch [92/650], Validation Loss: 0.0084, Validation L1: 0.6245, Smoothed Validation Loss: 0.0084
Epoch [93/650], Train Loss: 0.0058, Train L1 Loss: 0.5106
Epoch [93/650], Validation Loss: 0.0084, Validation L1: 0.6240, Smoothed Validation Loss: 0.0084
Epoch [94/650], Train Loss: 0.0058, Train L1 Loss: 0.5096
Epoch [94/650], Validation Loss: 0.0084, Validation L1: 0.6238, Smoothed Validation Loss: 0.0084
Epoch [95/650], Train Loss: 0.0057, Train L1 Loss: 0.5087
Epoch [95/650], Validation Loss: 0.0084, Validation L1: 0.6238, Smoothed Validation Loss: 0.0084
Epoch [96/650], Train Loss: 0.0057, Train L1 Loss: 0.5079
Epoch [96/650], Validation Loss: 0.0084, Validation L1: 0.6239, Smoothed Validation Loss: 0.0084
Epoch [97/650], Train Loss: 0.0057, Train L1 Loss: 0.5072
Epoch [97/650], Validation Loss: 0.0084, Validation L1: 0.6240, Smoothed Validation Loss: 0.0084
Epoch 00097: reducing learning rate of group 0 to 1.5625e-05.
Epoch [98/650], Train Loss: 0.0058, Train L1 Loss: 0.5098
Epoch [98/650], Validation Loss: 0.0082, Validation L1: 0.6176, Smoothed Validation Loss: 0.0084
Epoch [99/650], Train Loss: 0.0057, Train L1 Loss: 0.5084
Epoch [99/650], Validation Loss: 0.0082, Validation L1: 0.6172, Smoothed Validation Loss: 0.0084
Epoch [100/650], Train Loss: 0.0057, Train L1 Loss: 0.5078
Epoch [100/650], Validation Loss: 0.0082, Validation L1: 0.6170, Smoothed Validation Loss: 0.0084
Epoch [101/650], Train Loss: 0.0057, Train L1 Loss: 0.5072
Epoch [101/650], Validation Loss: 0.0082, Validation L1: 0.6169, Smoothed Validation Loss: 0.0083
Epoch [102/650], Train Loss: 0.0057, Train L1 Loss: 0.5067
Epoch [102/650], Validation Loss: 0.0082, Validation L1: 0.6168, Smoothed Validation Loss: 0.0083
Epoch [103/650], Train Loss: 0.0057, Train L1 Loss: 0.5063
Epoch [103/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [104/650], Train Loss: 0.0057, Train L1 Loss: 0.5058
Epoch [104/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [105/650], Train Loss: 0.0057, Train L1 Loss: 0.5054
Epoch [105/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [106/650], Train Loss: 0.0057, Train L1 Loss: 0.5050
Epoch [106/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [107/650], Train Loss: 0.0057, Train L1 Loss: 0.5046
Epoch [107/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [108/650], Train Loss: 0.0057, Train L1 Loss: 0.5042
Epoch [108/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [109/650], Train Loss: 0.0057, Train L1 Loss: 0.5038
Epoch [109/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [110/650], Train Loss: 0.0057, Train L1 Loss: 0.5034
Epoch [110/650], Validation Loss: 0.0082, Validation L1: 0.6167, Smoothed Validation Loss: 0.0083
Epoch [111/650], Train Loss: 0.0056, Train L1 Loss: 0.5031
Epoch [111/650], Validation Loss: 0.0082, Validation L1: 0.6168, Smoothed Validation Loss: 0.0083
Epoch [112/650], Train Loss: 0.0056, Train L1 Loss: 0.5027
Epoch [112/650], Validation Loss: 0.0082, Validation L1: 0.6168, Smoothed Validation Loss: 0.0083
Epoch [113/650], Train Loss: 0.0056, Train L1 Loss: 0.5024
Epoch [113/650], Validation Loss: 0.0082, Validation L1: 0.6168, Smoothed Validation Loss: 0.0083
Epoch [114/650], Train Loss: 0.0056, Train L1 Loss: 0.5020
Epoch [114/650], Validation Loss: 0.0083, Validation L1: 0.6169, Smoothed Validation Loss: 0.0083
Epoch [115/650], Train Loss: 0.0056, Train L1 Loss: 0.5017
Epoch [115/650], Validation Loss: 0.0083, Validation L1: 0.6169, Smoothed Validation Loss: 0.0083
Epoch [116/650], Train Loss: 0.0056, Train L1 Loss: 0.5014
Epoch [116/650], Validation Loss: 0.0083, Validation L1: 0.6170, Smoothed Validation Loss: 0.0083
Epoch [117/650], Train Loss: 0.0056, Train L1 Loss: 0.5010
Epoch [117/650], Validation Loss: 0.0083, Validation L1: 0.6170, Smoothed Validation Loss: 0.0083
Epoch [118/650], Train Loss: 0.0056, Train L1 Loss: 0.5007
Epoch [118/650], Validation Loss: 0.0083, Validation L1: 0.6171, Smoothed Validation Loss: 0.0083
Epoch [119/650], Train Loss: 0.0056, Train L1 Loss: 0.5004
Epoch [119/650], Validation Loss: 0.0083, Validation L1: 0.6172, Smoothed Validation Loss: 0.0083
Epoch [120/650], Train Loss: 0.0056, Train L1 Loss: 0.5001
Epoch [120/650], Validation Loss: 0.0083, Validation L1: 0.6172, Smoothed Validation Loss: 0.0083
Epoch [121/650], Train Loss: 0.0056, Train L1 Loss: 0.4998
Epoch [121/650], Validation Loss: 0.0083, Validation L1: 0.6173, Smoothed Validation Loss: 0.0083
Epoch [122/650], Train Loss: 0.0056, Train L1 Loss: 0.4995
Epoch [122/650], Validation Loss: 0.0083, Validation L1: 0.6174, Smoothed Validation Loss: 0.0083
Epoch [123/650], Train Loss: 0.0056, Train L1 Loss: 0.4992
Epoch [123/650], Validation Loss: 0.0083, Validation L1: 0.6175, Smoothed Validation Loss: 0.0083
Epoch 00123: reducing learning rate of group 0 to 7.8125e-06.
Epoch [124/650], Train Loss: 0.0056, Train L1 Loss: 0.5003
Epoch [124/650], Validation Loss: 0.0082, Validation L1: 0.6134, Smoothed Validation Loss: 0.0083
Epoch [125/650], Train Loss: 0.0056, Train L1 Loss: 0.4996
Epoch [125/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0083
Epoch [126/650], Train Loss: 0.0056, Train L1 Loss: 0.4993
Epoch [126/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0082
Epoch [127/650], Train Loss: 0.0056, Train L1 Loss: 0.4991
Epoch [127/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0082
Epoch [128/650], Train Loss: 0.0056, Train L1 Loss: 0.4989
Epoch [128/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0082
Epoch [129/650], Train Loss: 0.0056, Train L1 Loss: 0.4987
Epoch [129/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0082
Epoch [130/650], Train Loss: 0.0056, Train L1 Loss: 0.4985
Epoch [130/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0082
Epoch [131/650], Train Loss: 0.0056, Train L1 Loss: 0.4984
Epoch [131/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0082
Epoch [132/650], Train Loss: 0.0056, Train L1 Loss: 0.4982
Epoch [132/650], Validation Loss: 0.0082, Validation L1: 0.6133, Smoothed Validation Loss: 0.0082
Epoch [133/650], Train Loss: 0.0056, Train L1 Loss: 0.4980
Epoch [133/650], Validation Loss: 0.0082, Validation L1: 0.6134, Smoothed Validation Loss: 0.0082
Epoch [134/650], Train Loss: 0.0056, Train L1 Loss: 0.4978
Epoch [134/650], Validation Loss: 0.0082, Validation L1: 0.6134, Smoothed Validation Loss: 0.0082
Epoch [135/650], Train Loss: 0.0055, Train L1 Loss: 0.4977
Epoch [135/650], Validation Loss: 0.0082, Validation L1: 0.6134, Smoothed Validation Loss: 0.0082
Epoch [136/650], Train Loss: 0.0055, Train L1 Loss: 0.4975
Epoch [136/650], Validation Loss: 0.0082, Validation L1: 0.6134, Smoothed Validation Loss: 0.0082
Epoch [137/650], Train Loss: 0.0055, Train L1 Loss: 0.4973
Epoch [137/650], Validation Loss: 0.0082, Validation L1: 0.6135, Smoothed Validation Loss: 0.0082
Epoch [138/650], Train Loss: 0.0055, Train L1 Loss: 0.4972
Epoch [138/650], Validation Loss: 0.0082, Validation L1: 0.6135, Smoothed Validation Loss: 0.0082
Epoch [139/650], Train Loss: 0.0055, Train L1 Loss: 0.4970
Epoch [139/650], Validation Loss: 0.0082, Validation L1: 0.6135, Smoothed Validation Loss: 0.0082
Epoch [140/650], Train Loss: 0.0055, Train L1 Loss: 0.4968
Epoch [140/650], Validation Loss: 0.0082, Validation L1: 0.6136, Smoothed Validation Loss: 0.0082
Epoch [141/650], Train Loss: 0.0055, Train L1 Loss: 0.4967
Epoch [141/650], Validation Loss: 0.0082, Validation L1: 0.6136, Smoothed Validation Loss: 0.0082
Epoch [142/650], Train Loss: 0.0055, Train L1 Loss: 0.4965
Epoch [142/650], Validation Loss: 0.0082, Validation L1: 0.6137, Smoothed Validation Loss: 0.0082
Epoch [143/650], Train Loss: 0.0055, Train L1 Loss: 0.4964
Epoch [143/650], Validation Loss: 0.0082, Validation L1: 0.6137, Smoothed Validation Loss: 0.0082
Epoch [144/650], Train Loss: 0.0055, Train L1 Loss: 0.4962
Epoch [144/650], Validation Loss: 0.0082, Validation L1: 0.6137, Smoothed Validation Loss: 0.0082
Epoch [145/650], Train Loss: 0.0055, Train L1 Loss: 0.4961
Epoch [145/650], Validation Loss: 0.0082, Validation L1: 0.6138, Smoothed Validation Loss: 0.0082
Epoch [146/650], Train Loss: 0.0055, Train L1 Loss: 0.4959
Epoch [146/650], Validation Loss: 0.0082, Validation L1: 0.6138, Smoothed Validation Loss: 0.0082
Epoch 00146: reducing learning rate of group 0 to 3.9063e-06.
Epoch [147/650], Train Loss: 0.0055, Train L1 Loss: 0.4963
Epoch [147/650], Validation Loss: 0.0082, Validation L1: 0.6125, Smoothed Validation Loss: 0.0082
Epoch [148/650], Train Loss: 0.0055, Train L1 Loss: 0.4960
Epoch [148/650], Validation Loss: 0.0082, Validation L1: 0.6125, Smoothed Validation Loss: 0.0082
Epoch [149/650], Train Loss: 0.0055, Train L1 Loss: 0.4959
Epoch [149/650], Validation Loss: 0.0082, Validation L1: 0.6125, Smoothed Validation Loss: 0.0082
Epoch [150/650], Train Loss: 0.0055, Train L1 Loss: 0.4958
Epoch [150/650], Validation Loss: 0.0082, Validation L1: 0.6125, Smoothed Validation Loss: 0.0082
Epoch [151/650], Train Loss: 0.0055, Train L1 Loss: 0.4957
Epoch [151/650], Validation Loss: 0.0082, Validation L1: 0.6125, Smoothed Validation Loss: 0.0082
Epoch [152/650], Train Loss: 0.0055, Train L1 Loss: 0.4956
Epoch [152/650], Validation Loss: 0.0082, Validation L1: 0.6126, Smoothed Validation Loss: 0.0082
Epoch [153/650], Train Loss: 0.0055, Train L1 Loss: 0.4955
Epoch [153/650], Validation Loss: 0.0082, Validation L1: 0.6126, Smoothed Validation Loss: 0.0082
Epoch [154/650], Train Loss: 0.0055, Train L1 Loss: 0.4954
Epoch [154/650], Validation Loss: 0.0082, Validation L1: 0.6126, Smoothed Validation Loss: 0.0082
Epoch [155/650], Train Loss: 0.0055, Train L1 Loss: 0.4953
Epoch [155/650], Validation Loss: 0.0082, Validation L1: 0.6126, Smoothed Validation Loss: 0.0082
Epoch [156/650], Train Loss: 0.0055, Train L1 Loss: 0.4952
Epoch [156/650], Validation Loss: 0.0082, Validation L1: 0.6126, Smoothed Validation Loss: 0.0082
Epoch [157/650], Train Loss: 0.0055, Train L1 Loss: 0.4951
Epoch [157/650], Validation Loss: 0.0082, Validation L1: 0.6126, Smoothed Validation Loss: 0.0082
Epoch [158/650], Train Loss: 0.0055, Train L1 Loss: 0.4950
Epoch [158/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [159/650], Train Loss: 0.0055, Train L1 Loss: 0.4949
Epoch [159/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [160/650], Train Loss: 0.0055, Train L1 Loss: 0.4949
Epoch [160/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [161/650], Train Loss: 0.0055, Train L1 Loss: 0.4948
Epoch [161/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [162/650], Train Loss: 0.0055, Train L1 Loss: 0.4947
Epoch [162/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [163/650], Train Loss: 0.0055, Train L1 Loss: 0.4946
Epoch [163/650], Validation Loss: 0.0082, Validation L1: 0.6128, Smoothed Validation Loss: 0.0082
Epoch 00163: reducing learning rate of group 0 to 1.9531e-06.
Epoch [164/650], Train Loss: 0.0055, Train L1 Loss: 0.4945
Epoch [164/650], Validation Loss: 0.0082, Validation L1: 0.6126, Smoothed Validation Loss: 0.0082
Epoch [165/650], Train Loss: 0.0055, Train L1 Loss: 0.4945
Epoch [165/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [166/650], Train Loss: 0.0055, Train L1 Loss: 0.4944
Epoch [166/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [167/650], Train Loss: 0.0055, Train L1 Loss: 0.4944
Epoch [167/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [168/650], Train Loss: 0.0055, Train L1 Loss: 0.4943
Epoch [168/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [169/650], Train Loss: 0.0055, Train L1 Loss: 0.4943
Epoch [169/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [170/650], Train Loss: 0.0055, Train L1 Loss: 0.4942
Epoch [170/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch [171/650], Train Loss: 0.0055, Train L1 Loss: 0.4942
Epoch [171/650], Validation Loss: 0.0082, Validation L1: 0.6127, Smoothed Validation Loss: 0.0082
Epoch 00171: reducing learning rate of group 0 to 9.7656e-07.
Epoch [172/650], Train Loss: 0.0055, Train L1 Loss: 0.4940
Epoch [172/650], Validation Loss: 0.0082, Validation L1: 0.6128, Smoothed Validation Loss: 0.0082
Epoch [173/650], Train Loss: 0.0055, Train L1 Loss: 0.4940
Epoch [173/650], Validation Loss: 0.0082, Validation L1: 0.6128, Smoothed Validation Loss: 0.0082
Epoch [174/650], Train Loss: 0.0055, Train L1 Loss: 0.4940
Epoch [174/650], Validation Loss: 0.0082, Validation L1: 0.6128, Smoothed Validation Loss: 0.0082
Epoch [175/650], Train Loss: 0.0055, Train L1 Loss: 0.4939
Epoch [175/650], Validation Loss: 0.0082, Validation L1: 0.6128, Smoothed Validation Loss: 0.0082
Epoch [176/650], Train Loss: 0.0055, Train L1 Loss: 0.4939
Epoch [176/650], Validation Loss: 0.0082, Validation L1: 0.6128, Smoothed Validation Loss: 0.0082
Epoch [177/650], Train Loss: 0.0055, Train L1 Loss: 0.4939
Epoch [177/650], Validation Loss: 0.0082, Validation L1: 0.6128, Smoothed Validation Loss: 0.0082
Epoch 00177: reducing learning rate of group 0 to 4.8828e-07.
Epoch [178/650], Train Loss: 0.0055, Train L1 Loss: 0.4938
Epoch [178/650], Validation Loss: 0.0082, Validation L1: 0.6129, Smoothed Validation Loss: 0.0082
Epoch [179/650], Train Loss: 0.0055, Train L1 Loss: 0.4937
Epoch [179/650], Validation Loss: 0.0082, Validation L1: 0.6129, Smoothed Validation Loss: 0.0082
Epoch [180/650], Train Loss: 0.0055, Train L1 Loss: 0.4937
Epoch [180/650], Validation Loss: 0.0082, Validation L1: 0.6129, Smoothed Validation Loss: 0.0082
Epoch [181/650], Train Loss: 0.0055, Train L1 Loss: 0.4937
Epoch [181/650], Validation Loss: 0.0082, Validation L1: 0.6129, Smoothed Validation Loss: 0.0082
Epoch [182/650], Train Loss: 0.0055, Train L1 Loss: 0.4937
Epoch [182/650], Validation Loss: 0.0082, Validation L1: 0.6129, Smoothed Validation Loss: 0.0082
Epoch [183/650], Train Loss: 0.0055, Train L1 Loss: 0.4937
Epoch [183/650], Validation Loss: 0.0082, Validation L1: 0.6129, Smoothed Validation Loss: 0.0082
Epoch 00183: reducing learning rate of group 0 to 2.4414e-07.
Epoch [184/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [184/650], Validation Loss: 0.0082, Validation L1: 0.6129, Smoothed Validation Loss: 0.0082
Epoch [185/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [185/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [186/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [186/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [187/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [187/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [188/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [188/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [189/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [189/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch 00189: reducing learning rate of group 0 to 1.2207e-07.
Epoch [190/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [190/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [191/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [191/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [192/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [192/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [193/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [193/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [194/650], Train Loss: 0.0055, Train L1 Loss: 0.4936
Epoch [194/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [195/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [195/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch 00195: reducing learning rate of group 0 to 6.1035e-08.
Epoch [196/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [196/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [197/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [197/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [198/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [198/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [199/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [199/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [200/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [200/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [201/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [201/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch 00201: reducing learning rate of group 0 to 3.0518e-08.
Epoch [202/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [202/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [203/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [203/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [204/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [204/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [205/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [205/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [206/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [206/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [207/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [207/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch 00207: reducing learning rate of group 0 to 1.5259e-08.
Epoch [208/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [208/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [209/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [209/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [210/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [210/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [211/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [211/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [212/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [212/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [213/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [213/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [214/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [214/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [215/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [215/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [216/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [216/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [217/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [217/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [218/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [218/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [219/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [219/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [220/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [220/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [221/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [221/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [222/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [222/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [223/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [223/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [224/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [224/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [225/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [225/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [226/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [226/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [227/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [227/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [228/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [228/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [229/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [229/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [230/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [230/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [231/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [231/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [232/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [232/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [233/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [233/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [234/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [234/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [235/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [235/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [236/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [236/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [237/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [237/650], Validation Loss: 0.0082, Validation L1: 0.6130, Smoothed Validation Loss: 0.0082
Epoch [238/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [238/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [239/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [239/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [240/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [240/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [241/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [241/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [242/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [242/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [243/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [243/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [244/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [244/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [245/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [245/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [246/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [246/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [247/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [247/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [248/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [248/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [249/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [249/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [250/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [250/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [251/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [251/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [252/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [252/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [253/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [253/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [254/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [254/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [255/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [255/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [256/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [256/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [257/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [257/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [258/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [258/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [259/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [259/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [260/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [260/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [261/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [261/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [262/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [262/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [263/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [263/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [264/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [264/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [265/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [265/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [266/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [266/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [267/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [267/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [268/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [268/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [269/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [269/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [270/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [270/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [271/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [271/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [272/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [272/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [273/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [273/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [274/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [274/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [275/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [275/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [276/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [276/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [277/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [277/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [278/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [278/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [279/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [279/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [280/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [280/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [281/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [281/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [282/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [282/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [283/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [283/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [284/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [284/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [285/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [285/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [286/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [286/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [287/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [287/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [288/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [288/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [289/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [289/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [290/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [290/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [291/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [291/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [292/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [292/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [293/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [293/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [294/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [294/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [295/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [295/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [296/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [296/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [297/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [297/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [298/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [298/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [299/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [299/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [300/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [300/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [301/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [301/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [302/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [302/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [303/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [303/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [304/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [304/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [305/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [305/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [306/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [306/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [307/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [307/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [308/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [308/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [309/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [309/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [310/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [310/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [311/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [311/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [312/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [312/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [313/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [313/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [314/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [314/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [315/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [315/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [316/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [316/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [317/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [317/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [318/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [318/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [319/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [319/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [320/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [320/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [321/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [321/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [322/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [322/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [323/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [323/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [324/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [324/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [325/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [325/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [326/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [326/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [327/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [327/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [328/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [328/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [329/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [329/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [330/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [330/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [331/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [331/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [332/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [332/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [333/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [333/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [334/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [334/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [335/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [335/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [336/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [336/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [337/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [337/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [338/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [338/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [339/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [339/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [340/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [340/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [341/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [341/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [342/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [342/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [343/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [343/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [344/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [344/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [345/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [345/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [346/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [346/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [347/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [347/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [348/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [348/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [349/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [349/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [350/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [350/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [351/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [351/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [352/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [352/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [353/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [353/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [354/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [354/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [355/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [355/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [356/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [356/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [357/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [357/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [358/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [358/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [359/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [359/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [360/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [360/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [361/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [361/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [362/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [362/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [363/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [363/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [364/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [364/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [365/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [365/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [366/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [366/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [367/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [367/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [368/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [368/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [369/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [369/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [370/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [370/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [371/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [371/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [372/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [372/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [373/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [373/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [374/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [374/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [375/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [375/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [376/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [376/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [377/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [377/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [378/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [378/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [379/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [379/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [380/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [380/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [381/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [381/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [382/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [382/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [383/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [383/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [384/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [384/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [385/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [385/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [386/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [386/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [387/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [387/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [388/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [388/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [389/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [389/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [390/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [390/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [391/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [391/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [392/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [392/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [393/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [393/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [394/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [394/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [395/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [395/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [396/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [396/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [397/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [397/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [398/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [398/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [399/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [399/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [400/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [400/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [401/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [401/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [402/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [402/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [403/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [403/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [404/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [404/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [405/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [405/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [406/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [406/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [407/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [407/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [408/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [408/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [409/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [409/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [410/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [410/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [411/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [411/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [412/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [412/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [413/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [413/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [414/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [414/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [415/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [415/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [416/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [416/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [417/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [417/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [418/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [418/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [419/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [419/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [420/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [420/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [421/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [421/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [422/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [422/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [423/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [423/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [424/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [424/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [425/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [425/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [426/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [426/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [427/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [427/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [428/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [428/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [429/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [429/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [430/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [430/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [431/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [431/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [432/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [432/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [433/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [433/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [434/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [434/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [435/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [435/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [436/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [436/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [437/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [437/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [438/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [438/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [439/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [439/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [440/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [440/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [441/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [441/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [442/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [442/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [443/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [443/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [444/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [444/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [445/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [445/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [446/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [446/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [447/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [447/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [448/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [448/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [449/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [449/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [450/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [450/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [451/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [451/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [452/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [452/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [453/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [453/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [454/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [454/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [455/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [455/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [456/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [456/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [457/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [457/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [458/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [458/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [459/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [459/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [460/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [460/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [461/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [461/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [462/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [462/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [463/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [463/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [464/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [464/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [465/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [465/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [466/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [466/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [467/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [467/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [468/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [468/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [469/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [469/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [470/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [470/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [471/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [471/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [472/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [472/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [473/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [473/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [474/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [474/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [475/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [475/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [476/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [476/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [477/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [477/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [478/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [478/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [479/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [479/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [480/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [480/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [481/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [481/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [482/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [482/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [483/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [483/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [484/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [484/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [485/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [485/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [486/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [486/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [487/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [487/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [488/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [488/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [489/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [489/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [490/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [490/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [491/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [491/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [492/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [492/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [493/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [493/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [494/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [494/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [495/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [495/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [496/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [496/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [497/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [497/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [498/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [498/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [499/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [499/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [500/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [500/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [501/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [501/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [502/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [502/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [503/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [503/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [504/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [504/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [505/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [505/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [506/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [506/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [507/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [507/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [508/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [508/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [509/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [509/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [510/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [510/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [511/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [511/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [512/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [512/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [513/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [513/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [514/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [514/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [515/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [515/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [516/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [516/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [517/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [517/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [518/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [518/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [519/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [519/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [520/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [520/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [521/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [521/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [522/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [522/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [523/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [523/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [524/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [524/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [525/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [525/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [526/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [526/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [527/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [527/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [528/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [528/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [529/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [529/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [530/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [530/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [531/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [531/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [532/650], Train Loss: 0.0055, Train L1 Loss: 0.4935
Epoch [532/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [533/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [533/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [534/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [534/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [535/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [535/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [536/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [536/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [537/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [537/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [538/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [538/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [539/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [539/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [540/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [540/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [541/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [541/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [542/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [542/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [543/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [543/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [544/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [544/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [545/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [545/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [546/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [546/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [547/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [547/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [548/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [548/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [549/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [549/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [550/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [550/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [551/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [551/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [552/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [552/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [553/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [553/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [554/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [554/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [555/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [555/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [556/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [556/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [557/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [557/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [558/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [558/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [559/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [559/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [560/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [560/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [561/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [561/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [562/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [562/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [563/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [563/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [564/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [564/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [565/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [565/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [566/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [566/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [567/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [567/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [568/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [568/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [569/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [569/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [570/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [570/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [571/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [571/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [572/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [572/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [573/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [573/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [574/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [574/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [575/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [575/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [576/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [576/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [577/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [577/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [578/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [578/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [579/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [579/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [580/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [580/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [581/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [581/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [582/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [582/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [583/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [583/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [584/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [584/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [585/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [585/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [586/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [586/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [587/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [587/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [588/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [588/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [589/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [589/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [590/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [590/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [591/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [591/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [592/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [592/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [593/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [593/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [594/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [594/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [595/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [595/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [596/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [596/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [597/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [597/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [598/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [598/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [599/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [599/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [600/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [600/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [601/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [601/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [602/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [602/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [603/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [603/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [604/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [604/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [605/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [605/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [606/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [606/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [607/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [607/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [608/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [608/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [609/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [609/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [610/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [610/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [611/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [611/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [612/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [612/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [613/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [613/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [614/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [614/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [615/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [615/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [616/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [616/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [617/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [617/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [618/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [618/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [619/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [619/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [620/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [620/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [621/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [621/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [622/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [622/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [623/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [623/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [624/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [624/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [625/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [625/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [626/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [626/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [627/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [627/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [628/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [628/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [629/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [629/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [630/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [630/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [631/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [631/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [632/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [632/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [633/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [633/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [634/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [634/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [635/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [635/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [636/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [636/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [637/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [637/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [638/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [638/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [639/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [639/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [640/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [640/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [641/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [641/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [642/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [642/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [643/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [643/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [644/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [644/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [645/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [645/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [646/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [646/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [647/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [647/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [648/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [648/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [649/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [649/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
Epoch [650/650], Train Loss: 0.0055, Train L1 Loss: 0.4934
Epoch [650/650], Validation Loss: 0.0082, Validation L1: 0.6131, Smoothed Validation Loss: 0.0082
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19630797: <WorkingSetup_4> in cluster <dcc> Done

Job <WorkingSetup_4> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 13:59:44 2023
Job was executed on host(s) <4*n-62-18-12>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Fri Dec  1 21:58:19 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Fri Dec  1 21:58:19 2023
Terminated at Sat Dec  2 09:08:46 2023
Results reported at Sat Dec  2 09:08:46 2023

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

    CPU time :                                   40596.32 sec.
    Max Memory :                                 1940 MB
    Average Memory :                             1925.07 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63596.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   40226 sec.
    Turnaround time :                            155342 sec.

The output (if any) is above this job summary.

