
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
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231201_202402-9fvx4xaq
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 3WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/9fvx4xaq
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:15,635] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7f3ca2153a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:19,487] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpw9hctanw.py line 218 
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:25,690] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpw9hctanw.py line 117 
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,180] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpw9hctanw.py line 90 
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,306] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:26,859] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:29,616] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:30,783] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 20:24:31,789] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.006 MB uploadedwandb: | 0.005 MB of 0.117 MB uploadedwandb: / 0.005 MB of 0.117 MB uploadedwandb: - 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▄▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▅▄▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▆▅▄▄▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▄▃▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▃▂▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.00734
wandb:     train l1 loss 0.45549
wandb:        train_loss 0.00472
wandb:       val l1 loss 0.56712
wandb:          val loss 0.00734
wandb: 
wandb: 🚀 View run 3WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/9fvx4xaq
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231201_202402-9fvx4xaq/logs
Epoch [1/650], Train Loss: 0.0311, Train L1 Loss: 0.8707
Epoch [1/650], Validation Loss: 0.0104, Validation L1: 0.7376, Smoothed Validation Loss: 0.0104
Epoch [2/650], Train Loss: 0.0106, Train L1 Loss: 0.7483
Epoch [2/650], Validation Loss: 0.0101, Validation L1: 0.7351, Smoothed Validation Loss: 0.0104
Epoch [3/650], Train Loss: 0.0103, Train L1 Loss: 0.7351
Epoch [3/650], Validation Loss: 0.0097, Validation L1: 0.7164, Smoothed Validation Loss: 0.0103
Epoch [4/650], Train Loss: 0.0097, Train L1 Loss: 0.7092
Epoch [4/650], Validation Loss: 0.0092, Validation L1: 0.6930, Smoothed Validation Loss: 0.0102
Epoch [5/650], Train Loss: 0.0092, Train L1 Loss: 0.6905
Epoch [5/650], Validation Loss: 0.0090, Validation L1: 0.6821, Smoothed Validation Loss: 0.0101
Epoch [6/650], Train Loss: 0.0090, Train L1 Loss: 0.6819
Epoch [6/650], Validation Loss: 0.0090, Validation L1: 0.6780, Smoothed Validation Loss: 0.0100
Epoch [7/650], Train Loss: 0.0089, Train L1 Loss: 0.6748
Epoch [7/650], Validation Loss: 0.0089, Validation L1: 0.6720, Smoothed Validation Loss: 0.0099
Epoch [8/650], Train Loss: 0.0088, Train L1 Loss: 0.6689
Epoch [8/650], Validation Loss: 0.0090, Validation L1: 0.6724, Smoothed Validation Loss: 0.0098
Epoch [9/650], Train Loss: 0.0087, Train L1 Loss: 0.6619
Epoch [9/650], Validation Loss: 0.0088, Validation L1: 0.6612, Smoothed Validation Loss: 0.0097
Epoch [10/650], Train Loss: 0.0086, Train L1 Loss: 0.6563
Epoch [10/650], Validation Loss: 0.0088, Validation L1: 0.6565, Smoothed Validation Loss: 0.0096
Epoch [11/650], Train Loss: 0.0084, Train L1 Loss: 0.6487
Epoch [11/650], Validation Loss: 0.0086, Validation L1: 0.6500, Smoothed Validation Loss: 0.0095
Epoch [12/650], Train Loss: 0.0084, Train L1 Loss: 0.6461
Epoch [12/650], Validation Loss: 0.0087, Validation L1: 0.6523, Smoothed Validation Loss: 0.0094
Epoch [13/650], Train Loss: 0.0081, Train L1 Loss: 0.6349
Epoch [13/650], Validation Loss: 0.0084, Validation L1: 0.6424, Smoothed Validation Loss: 0.0093
Epoch [14/650], Train Loss: 0.0080, Train L1 Loss: 0.6282
Epoch [14/650], Validation Loss: 0.0084, Validation L1: 0.6438, Smoothed Validation Loss: 0.0092
Epoch [15/650], Train Loss: 0.0079, Train L1 Loss: 0.6226
Epoch [15/650], Validation Loss: 0.0085, Validation L1: 0.6424, Smoothed Validation Loss: 0.0091
Epoch [16/650], Train Loss: 0.0078, Train L1 Loss: 0.6180
Epoch [16/650], Validation Loss: 0.0083, Validation L1: 0.6361, Smoothed Validation Loss: 0.0091
Epoch [17/650], Train Loss: 0.0077, Train L1 Loss: 0.6138
Epoch [17/650], Validation Loss: 0.0082, Validation L1: 0.6347, Smoothed Validation Loss: 0.0090
Epoch [18/650], Train Loss: 0.0077, Train L1 Loss: 0.6107
Epoch [18/650], Validation Loss: 0.0085, Validation L1: 0.6468, Smoothed Validation Loss: 0.0089
Epoch [19/650], Train Loss: 0.0076, Train L1 Loss: 0.6067
Epoch [19/650], Validation Loss: 0.0080, Validation L1: 0.6230, Smoothed Validation Loss: 0.0088
Epoch [20/650], Train Loss: 0.0075, Train L1 Loss: 0.6032
Epoch [20/650], Validation Loss: 0.0082, Validation L1: 0.6359, Smoothed Validation Loss: 0.0088
Epoch [21/650], Train Loss: 0.0074, Train L1 Loss: 0.6004
Epoch [21/650], Validation Loss: 0.0080, Validation L1: 0.6246, Smoothed Validation Loss: 0.0087
Epoch [22/650], Train Loss: 0.0074, Train L1 Loss: 0.5981
Epoch [22/650], Validation Loss: 0.0079, Validation L1: 0.6197, Smoothed Validation Loss: 0.0086
Epoch [23/650], Train Loss: 0.0074, Train L1 Loss: 0.5972
Epoch [23/650], Validation Loss: 0.0079, Validation L1: 0.6186, Smoothed Validation Loss: 0.0085
Epoch [24/650], Train Loss: 0.0073, Train L1 Loss: 0.5950
Epoch [24/650], Validation Loss: 0.0078, Validation L1: 0.6145, Smoothed Validation Loss: 0.0085
Epoch [25/650], Train Loss: 0.0073, Train L1 Loss: 0.5937
Epoch [25/650], Validation Loss: 0.0080, Validation L1: 0.6246, Smoothed Validation Loss: 0.0084
Epoch [26/650], Train Loss: 0.0073, Train L1 Loss: 0.5923
Epoch [26/650], Validation Loss: 0.0078, Validation L1: 0.6120, Smoothed Validation Loss: 0.0084
Epoch [27/650], Train Loss: 0.0073, Train L1 Loss: 0.5913
Epoch [27/650], Validation Loss: 0.0077, Validation L1: 0.6079, Smoothed Validation Loss: 0.0083
Epoch [28/650], Train Loss: 0.0072, Train L1 Loss: 0.5889
Epoch [28/650], Validation Loss: 0.0078, Validation L1: 0.6093, Smoothed Validation Loss: 0.0082
Epoch [29/650], Train Loss: 0.0072, Train L1 Loss: 0.5865
Epoch [29/650], Validation Loss: 0.0078, Validation L1: 0.6038, Smoothed Validation Loss: 0.0082
Epoch [30/650], Train Loss: 0.0072, Train L1 Loss: 0.5864
Epoch [30/650], Validation Loss: 0.0078, Validation L1: 0.6081, Smoothed Validation Loss: 0.0082
Epoch [31/650], Train Loss: 0.0072, Train L1 Loss: 0.5853
Epoch [31/650], Validation Loss: 0.0077, Validation L1: 0.6003, Smoothed Validation Loss: 0.0081
Epoch [32/650], Train Loss: 0.0071, Train L1 Loss: 0.5841
Epoch [32/650], Validation Loss: 0.0077, Validation L1: 0.5982, Smoothed Validation Loss: 0.0081
Epoch [33/650], Train Loss: 0.0071, Train L1 Loss: 0.5824
Epoch [33/650], Validation Loss: 0.0078, Validation L1: 0.6060, Smoothed Validation Loss: 0.0080
Epoch [34/650], Train Loss: 0.0071, Train L1 Loss: 0.5802
Epoch [34/650], Validation Loss: 0.0077, Validation L1: 0.5991, Smoothed Validation Loss: 0.0080
Epoch [35/650], Train Loss: 0.0071, Train L1 Loss: 0.5801
Epoch [35/650], Validation Loss: 0.0079, Validation L1: 0.6040, Smoothed Validation Loss: 0.0080
Epoch [36/650], Train Loss: 0.0070, Train L1 Loss: 0.5786
Epoch [36/650], Validation Loss: 0.0076, Validation L1: 0.5962, Smoothed Validation Loss: 0.0080
Epoch [37/650], Train Loss: 0.0070, Train L1 Loss: 0.5757
Epoch [37/650], Validation Loss: 0.0076, Validation L1: 0.5914, Smoothed Validation Loss: 0.0079
Epoch [38/650], Train Loss: 0.0070, Train L1 Loss: 0.5753
Epoch [38/650], Validation Loss: 0.0075, Validation L1: 0.5946, Smoothed Validation Loss: 0.0079
Epoch [39/650], Train Loss: 0.0070, Train L1 Loss: 0.5749
Epoch [39/650], Validation Loss: 0.0076, Validation L1: 0.5912, Smoothed Validation Loss: 0.0079
Epoch [40/650], Train Loss: 0.0069, Train L1 Loss: 0.5732
Epoch [40/650], Validation Loss: 0.0076, Validation L1: 0.5969, Smoothed Validation Loss: 0.0078
Epoch [41/650], Train Loss: 0.0069, Train L1 Loss: 0.5714
Epoch [41/650], Validation Loss: 0.0074, Validation L1: 0.5838, Smoothed Validation Loss: 0.0078
Epoch [42/650], Train Loss: 0.0069, Train L1 Loss: 0.5715
Epoch [42/650], Validation Loss: 0.0076, Validation L1: 0.5890, Smoothed Validation Loss: 0.0078
Epoch [43/650], Train Loss: 0.0068, Train L1 Loss: 0.5685
Epoch [43/650], Validation Loss: 0.0075, Validation L1: 0.5878, Smoothed Validation Loss: 0.0077
Epoch [44/650], Train Loss: 0.0068, Train L1 Loss: 0.5680
Epoch [44/650], Validation Loss: 0.0076, Validation L1: 0.5898, Smoothed Validation Loss: 0.0077
Epoch [45/650], Train Loss: 0.0068, Train L1 Loss: 0.5670
Epoch [45/650], Validation Loss: 0.0075, Validation L1: 0.5865, Smoothed Validation Loss: 0.0077
Epoch [46/650], Train Loss: 0.0068, Train L1 Loss: 0.5654
Epoch [46/650], Validation Loss: 0.0075, Validation L1: 0.5877, Smoothed Validation Loss: 0.0077
Epoch [47/650], Train Loss: 0.0067, Train L1 Loss: 0.5645
Epoch [47/650], Validation Loss: 0.0075, Validation L1: 0.5852, Smoothed Validation Loss: 0.0077
Epoch [48/650], Train Loss: 0.0067, Train L1 Loss: 0.5642
Epoch [48/650], Validation Loss: 0.0075, Validation L1: 0.5870, Smoothed Validation Loss: 0.0077
Epoch [49/650], Train Loss: 0.0067, Train L1 Loss: 0.5637
Epoch [49/650], Validation Loss: 0.0075, Validation L1: 0.5902, Smoothed Validation Loss: 0.0076
Epoch [50/650], Train Loss: 0.0067, Train L1 Loss: 0.5629
Epoch [50/650], Validation Loss: 0.0075, Validation L1: 0.5921, Smoothed Validation Loss: 0.0076
Epoch [51/650], Train Loss: 0.0067, Train L1 Loss: 0.5617
Epoch [51/650], Validation Loss: 0.0075, Validation L1: 0.5863, Smoothed Validation Loss: 0.0076
Epoch [52/650], Train Loss: 0.0067, Train L1 Loss: 0.5611
Epoch [52/650], Validation Loss: 0.0075, Validation L1: 0.5896, Smoothed Validation Loss: 0.0076
Epoch [53/650], Train Loss: 0.0068, Train L1 Loss: 0.5650
Epoch [53/650], Validation Loss: 0.0074, Validation L1: 0.5833, Smoothed Validation Loss: 0.0076
Epoch [54/650], Train Loss: 0.0066, Train L1 Loss: 0.5589
Epoch [54/650], Validation Loss: 0.0073, Validation L1: 0.5803, Smoothed Validation Loss: 0.0076
Epoch [55/650], Train Loss: 0.0066, Train L1 Loss: 0.5581
Epoch [55/650], Validation Loss: 0.0073, Validation L1: 0.5808, Smoothed Validation Loss: 0.0075
Epoch [56/650], Train Loss: 0.0066, Train L1 Loss: 0.5585
Epoch [56/650], Validation Loss: 0.0075, Validation L1: 0.5922, Smoothed Validation Loss: 0.0075
Epoch [57/650], Train Loss: 0.0066, Train L1 Loss: 0.5577
Epoch [57/650], Validation Loss: 0.0074, Validation L1: 0.5849, Smoothed Validation Loss: 0.0075
Epoch [58/650], Train Loss: 0.0066, Train L1 Loss: 0.5557
Epoch [58/650], Validation Loss: 0.0073, Validation L1: 0.5780, Smoothed Validation Loss: 0.0075
Epoch [59/650], Train Loss: 0.0065, Train L1 Loss: 0.5529
Epoch [59/650], Validation Loss: 0.0074, Validation L1: 0.5843, Smoothed Validation Loss: 0.0075
Epoch [60/650], Train Loss: 0.0066, Train L1 Loss: 0.5548
Epoch [60/650], Validation Loss: 0.0073, Validation L1: 0.5809, Smoothed Validation Loss: 0.0075
Epoch [61/650], Train Loss: 0.0065, Train L1 Loss: 0.5544
Epoch [61/650], Validation Loss: 0.0074, Validation L1: 0.5883, Smoothed Validation Loss: 0.0075
Epoch [62/650], Train Loss: 0.0065, Train L1 Loss: 0.5543
Epoch [62/650], Validation Loss: 0.0074, Validation L1: 0.5850, Smoothed Validation Loss: 0.0075
Epoch [63/650], Train Loss: 0.0065, Train L1 Loss: 0.5514
Epoch [63/650], Validation Loss: 0.0074, Validation L1: 0.5844, Smoothed Validation Loss: 0.0074
Epoch [64/650], Train Loss: 0.0065, Train L1 Loss: 0.5512
Epoch [64/650], Validation Loss: 0.0073, Validation L1: 0.5786, Smoothed Validation Loss: 0.0074
Epoch [65/650], Train Loss: 0.0065, Train L1 Loss: 0.5532
Epoch [65/650], Validation Loss: 0.0075, Validation L1: 0.5947, Smoothed Validation Loss: 0.0074
Epoch [66/650], Train Loss: 0.0065, Train L1 Loss: 0.5515
Epoch [66/650], Validation Loss: 0.0074, Validation L1: 0.5799, Smoothed Validation Loss: 0.0074
Epoch [67/650], Train Loss: 0.0065, Train L1 Loss: 0.5516
Epoch [67/650], Validation Loss: 0.0074, Validation L1: 0.5878, Smoothed Validation Loss: 0.0074
Epoch [68/650], Train Loss: 0.0064, Train L1 Loss: 0.5504
Epoch [68/650], Validation Loss: 0.0074, Validation L1: 0.5825, Smoothed Validation Loss: 0.0074
Epoch [69/650], Train Loss: 0.0064, Train L1 Loss: 0.5494
Epoch [69/650], Validation Loss: 0.0074, Validation L1: 0.5820, Smoothed Validation Loss: 0.0074
Epoch [70/650], Train Loss: 0.0065, Train L1 Loss: 0.5501
Epoch [70/650], Validation Loss: 0.0075, Validation L1: 0.5786, Smoothed Validation Loss: 0.0074
Epoch [71/650], Train Loss: 0.0064, Train L1 Loss: 0.5473
Epoch [71/650], Validation Loss: 0.0076, Validation L1: 0.5825, Smoothed Validation Loss: 0.0074
Epoch [72/650], Train Loss: 0.0064, Train L1 Loss: 0.5471
Epoch [72/650], Validation Loss: 0.0074, Validation L1: 0.5873, Smoothed Validation Loss: 0.0074
Epoch [73/650], Train Loss: 0.0064, Train L1 Loss: 0.5469
Epoch [73/650], Validation Loss: 0.0075, Validation L1: 0.5843, Smoothed Validation Loss: 0.0074
Epoch [74/650], Train Loss: 0.0064, Train L1 Loss: 0.5466
Epoch [74/650], Validation Loss: 0.0077, Validation L1: 0.5893, Smoothed Validation Loss: 0.0075
Epoch [75/650], Train Loss: 0.0064, Train L1 Loss: 0.5459
Epoch [75/650], Validation Loss: 0.0075, Validation L1: 0.5813, Smoothed Validation Loss: 0.0075
Epoch 00075: reducing learning rate of group 0 to 5.0000e-04.
Epoch [76/650], Train Loss: 0.0060, Train L1 Loss: 0.5272
Epoch [76/650], Validation Loss: 0.0073, Validation L1: 0.5698, Smoothed Validation Loss: 0.0075
Epoch [77/650], Train Loss: 0.0059, Train L1 Loss: 0.5193
Epoch [77/650], Validation Loss: 0.0073, Validation L1: 0.5694, Smoothed Validation Loss: 0.0074
Epoch [78/650], Train Loss: 0.0058, Train L1 Loss: 0.5156
Epoch [78/650], Validation Loss: 0.0074, Validation L1: 0.5729, Smoothed Validation Loss: 0.0074
Epoch [79/650], Train Loss: 0.0057, Train L1 Loss: 0.5128
Epoch [79/650], Validation Loss: 0.0075, Validation L1: 0.5762, Smoothed Validation Loss: 0.0074
Epoch [80/650], Train Loss: 0.0057, Train L1 Loss: 0.5119
Epoch [80/650], Validation Loss: 0.0075, Validation L1: 0.5778, Smoothed Validation Loss: 0.0075
Epoch [81/650], Train Loss: 0.0057, Train L1 Loss: 0.5107
Epoch [81/650], Validation Loss: 0.0077, Validation L1: 0.5806, Smoothed Validation Loss: 0.0075
Epoch 00081: reducing learning rate of group 0 to 2.5000e-04.
Epoch [82/650], Train Loss: 0.0056, Train L1 Loss: 0.5043
Epoch [82/650], Validation Loss: 0.0074, Validation L1: 0.5731, Smoothed Validation Loss: 0.0075
Epoch [83/650], Train Loss: 0.0055, Train L1 Loss: 0.4981
Epoch [83/650], Validation Loss: 0.0074, Validation L1: 0.5742, Smoothed Validation Loss: 0.0075
Epoch [84/650], Train Loss: 0.0054, Train L1 Loss: 0.4952
Epoch [84/650], Validation Loss: 0.0075, Validation L1: 0.5751, Smoothed Validation Loss: 0.0075
Epoch [85/650], Train Loss: 0.0054, Train L1 Loss: 0.4935
Epoch [85/650], Validation Loss: 0.0075, Validation L1: 0.5751, Smoothed Validation Loss: 0.0075
Epoch [86/650], Train Loss: 0.0053, Train L1 Loss: 0.4908
Epoch [86/650], Validation Loss: 0.0075, Validation L1: 0.5765, Smoothed Validation Loss: 0.0075
Epoch [87/650], Train Loss: 0.0053, Train L1 Loss: 0.4880
Epoch [87/650], Validation Loss: 0.0076, Validation L1: 0.5792, Smoothed Validation Loss: 0.0075
Epoch 00087: reducing learning rate of group 0 to 1.2500e-04.
Epoch [88/650], Train Loss: 0.0053, Train L1 Loss: 0.4893
Epoch [88/650], Validation Loss: 0.0075, Validation L1: 0.5744, Smoothed Validation Loss: 0.0075
Epoch [89/650], Train Loss: 0.0052, Train L1 Loss: 0.4848
Epoch [89/650], Validation Loss: 0.0075, Validation L1: 0.5749, Smoothed Validation Loss: 0.0075
Epoch [90/650], Train Loss: 0.0052, Train L1 Loss: 0.4821
Epoch [90/650], Validation Loss: 0.0075, Validation L1: 0.5759, Smoothed Validation Loss: 0.0075
Epoch [91/650], Train Loss: 0.0051, Train L1 Loss: 0.4800
Epoch [91/650], Validation Loss: 0.0076, Validation L1: 0.5770, Smoothed Validation Loss: 0.0075
Epoch [92/650], Train Loss: 0.0051, Train L1 Loss: 0.4781
Epoch [92/650], Validation Loss: 0.0076, Validation L1: 0.5781, Smoothed Validation Loss: 0.0075
Epoch [93/650], Train Loss: 0.0051, Train L1 Loss: 0.4764
Epoch [93/650], Validation Loss: 0.0076, Validation L1: 0.5792, Smoothed Validation Loss: 0.0075
Epoch 00093: reducing learning rate of group 0 to 6.2500e-05.
Epoch [94/650], Train Loss: 0.0051, Train L1 Loss: 0.4794
Epoch [94/650], Validation Loss: 0.0074, Validation L1: 0.5725, Smoothed Validation Loss: 0.0075
Epoch [95/650], Train Loss: 0.0051, Train L1 Loss: 0.4764
Epoch [95/650], Validation Loss: 0.0074, Validation L1: 0.5724, Smoothed Validation Loss: 0.0075
Epoch [96/650], Train Loss: 0.0051, Train L1 Loss: 0.4746
Epoch [96/650], Validation Loss: 0.0074, Validation L1: 0.5726, Smoothed Validation Loss: 0.0075
Epoch [97/650], Train Loss: 0.0050, Train L1 Loss: 0.4730
Epoch [97/650], Validation Loss: 0.0075, Validation L1: 0.5729, Smoothed Validation Loss: 0.0075
Epoch [98/650], Train Loss: 0.0050, Train L1 Loss: 0.4717
Epoch [98/650], Validation Loss: 0.0075, Validation L1: 0.5733, Smoothed Validation Loss: 0.0075
Epoch [99/650], Train Loss: 0.0050, Train L1 Loss: 0.4704
Epoch [99/650], Validation Loss: 0.0075, Validation L1: 0.5737, Smoothed Validation Loss: 0.0075
Epoch 00099: reducing learning rate of group 0 to 3.1250e-05.
Epoch [100/650], Train Loss: 0.0050, Train L1 Loss: 0.4727
Epoch [100/650], Validation Loss: 0.0073, Validation L1: 0.5692, Smoothed Validation Loss: 0.0075
Epoch [101/650], Train Loss: 0.0050, Train L1 Loss: 0.4708
Epoch [101/650], Validation Loss: 0.0073, Validation L1: 0.5691, Smoothed Validation Loss: 0.0075
Epoch [102/650], Train Loss: 0.0050, Train L1 Loss: 0.4697
Epoch [102/650], Validation Loss: 0.0073, Validation L1: 0.5692, Smoothed Validation Loss: 0.0075
Epoch [103/650], Train Loss: 0.0050, Train L1 Loss: 0.4687
Epoch [103/650], Validation Loss: 0.0073, Validation L1: 0.5694, Smoothed Validation Loss: 0.0074
Epoch [104/650], Train Loss: 0.0049, Train L1 Loss: 0.4678
Epoch [104/650], Validation Loss: 0.0074, Validation L1: 0.5697, Smoothed Validation Loss: 0.0074
Epoch [105/650], Train Loss: 0.0049, Train L1 Loss: 0.4670
Epoch [105/650], Validation Loss: 0.0074, Validation L1: 0.5699, Smoothed Validation Loss: 0.0074
Epoch 00105: reducing learning rate of group 0 to 1.5625e-05.
Epoch [106/650], Train Loss: 0.0050, Train L1 Loss: 0.4681
Epoch [106/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0074
Epoch [107/650], Train Loss: 0.0049, Train L1 Loss: 0.4670
Epoch [107/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0074
Epoch [108/650], Train Loss: 0.0049, Train L1 Loss: 0.4664
Epoch [108/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0074
Epoch [109/650], Train Loss: 0.0049, Train L1 Loss: 0.4658
Epoch [109/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0074
Epoch [110/650], Train Loss: 0.0049, Train L1 Loss: 0.4653
Epoch [110/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0074
Epoch [111/650], Train Loss: 0.0049, Train L1 Loss: 0.4649
Epoch [111/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0074
Epoch [112/650], Train Loss: 0.0049, Train L1 Loss: 0.4644
Epoch [112/650], Validation Loss: 0.0073, Validation L1: 0.5672, Smoothed Validation Loss: 0.0074
Epoch [113/650], Train Loss: 0.0049, Train L1 Loss: 0.4640
Epoch [113/650], Validation Loss: 0.0073, Validation L1: 0.5673, Smoothed Validation Loss: 0.0074
Epoch [114/650], Train Loss: 0.0049, Train L1 Loss: 0.4636
Epoch [114/650], Validation Loss: 0.0073, Validation L1: 0.5674, Smoothed Validation Loss: 0.0074
Epoch [115/650], Train Loss: 0.0049, Train L1 Loss: 0.4632
Epoch [115/650], Validation Loss: 0.0073, Validation L1: 0.5675, Smoothed Validation Loss: 0.0074
Epoch [116/650], Train Loss: 0.0049, Train L1 Loss: 0.4628
Epoch [116/650], Validation Loss: 0.0073, Validation L1: 0.5676, Smoothed Validation Loss: 0.0073
Epoch [117/650], Train Loss: 0.0049, Train L1 Loss: 0.4624
Epoch [117/650], Validation Loss: 0.0073, Validation L1: 0.5678, Smoothed Validation Loss: 0.0073
Epoch [118/650], Train Loss: 0.0048, Train L1 Loss: 0.4620
Epoch [118/650], Validation Loss: 0.0073, Validation L1: 0.5679, Smoothed Validation Loss: 0.0073
Epoch [119/650], Train Loss: 0.0048, Train L1 Loss: 0.4617
Epoch [119/650], Validation Loss: 0.0073, Validation L1: 0.5680, Smoothed Validation Loss: 0.0073
Epoch [120/650], Train Loss: 0.0048, Train L1 Loss: 0.4613
Epoch [120/650], Validation Loss: 0.0073, Validation L1: 0.5682, Smoothed Validation Loss: 0.0073
Epoch [121/650], Train Loss: 0.0048, Train L1 Loss: 0.4610
Epoch [121/650], Validation Loss: 0.0073, Validation L1: 0.5683, Smoothed Validation Loss: 0.0073
Epoch [122/650], Train Loss: 0.0048, Train L1 Loss: 0.4606
Epoch [122/650], Validation Loss: 0.0074, Validation L1: 0.5684, Smoothed Validation Loss: 0.0073
Epoch [123/650], Train Loss: 0.0048, Train L1 Loss: 0.4603
Epoch [123/650], Validation Loss: 0.0074, Validation L1: 0.5686, Smoothed Validation Loss: 0.0073
Epoch [124/650], Train Loss: 0.0048, Train L1 Loss: 0.4599
Epoch [124/650], Validation Loss: 0.0074, Validation L1: 0.5687, Smoothed Validation Loss: 0.0073
Epoch [125/650], Train Loss: 0.0048, Train L1 Loss: 0.4596
Epoch [125/650], Validation Loss: 0.0074, Validation L1: 0.5689, Smoothed Validation Loss: 0.0073
Epoch [126/650], Train Loss: 0.0048, Train L1 Loss: 0.4592
Epoch [126/650], Validation Loss: 0.0074, Validation L1: 0.5690, Smoothed Validation Loss: 0.0074
Epoch 00126: reducing learning rate of group 0 to 7.8125e-06.
Epoch [127/650], Train Loss: 0.0048, Train L1 Loss: 0.4599
Epoch [127/650], Validation Loss: 0.0073, Validation L1: 0.5672, Smoothed Validation Loss: 0.0073
Epoch [128/650], Train Loss: 0.0048, Train L1 Loss: 0.4593
Epoch [128/650], Validation Loss: 0.0073, Validation L1: 0.5672, Smoothed Validation Loss: 0.0073
Epoch [129/650], Train Loss: 0.0048, Train L1 Loss: 0.4591
Epoch [129/650], Validation Loss: 0.0073, Validation L1: 0.5672, Smoothed Validation Loss: 0.0073
Epoch [130/650], Train Loss: 0.0048, Train L1 Loss: 0.4589
Epoch [130/650], Validation Loss: 0.0073, Validation L1: 0.5673, Smoothed Validation Loss: 0.0073
Epoch [131/650], Train Loss: 0.0048, Train L1 Loss: 0.4587
Epoch [131/650], Validation Loss: 0.0073, Validation L1: 0.5673, Smoothed Validation Loss: 0.0073
Epoch [132/650], Train Loss: 0.0048, Train L1 Loss: 0.4585
Epoch [132/650], Validation Loss: 0.0073, Validation L1: 0.5674, Smoothed Validation Loss: 0.0073
Epoch 00132: reducing learning rate of group 0 to 3.9063e-06.
Epoch [133/650], Train Loss: 0.0048, Train L1 Loss: 0.4587
Epoch [133/650], Validation Loss: 0.0073, Validation L1: 0.5665, Smoothed Validation Loss: 0.0073
Epoch [134/650], Train Loss: 0.0048, Train L1 Loss: 0.4583
Epoch [134/650], Validation Loss: 0.0073, Validation L1: 0.5664, Smoothed Validation Loss: 0.0073
Epoch [135/650], Train Loss: 0.0048, Train L1 Loss: 0.4582
Epoch [135/650], Validation Loss: 0.0073, Validation L1: 0.5664, Smoothed Validation Loss: 0.0073
Epoch [136/650], Train Loss: 0.0048, Train L1 Loss: 0.4580
Epoch [136/650], Validation Loss: 0.0073, Validation L1: 0.5665, Smoothed Validation Loss: 0.0073
Epoch [137/650], Train Loss: 0.0048, Train L1 Loss: 0.4579
Epoch [137/650], Validation Loss: 0.0073, Validation L1: 0.5665, Smoothed Validation Loss: 0.0073
Epoch [138/650], Train Loss: 0.0048, Train L1 Loss: 0.4578
Epoch [138/650], Validation Loss: 0.0073, Validation L1: 0.5665, Smoothed Validation Loss: 0.0073
Epoch [139/650], Train Loss: 0.0048, Train L1 Loss: 0.4577
Epoch [139/650], Validation Loss: 0.0073, Validation L1: 0.5666, Smoothed Validation Loss: 0.0073
Epoch [140/650], Train Loss: 0.0048, Train L1 Loss: 0.4576
Epoch [140/650], Validation Loss: 0.0073, Validation L1: 0.5666, Smoothed Validation Loss: 0.0073
Epoch [141/650], Train Loss: 0.0048, Train L1 Loss: 0.4575
Epoch [141/650], Validation Loss: 0.0073, Validation L1: 0.5666, Smoothed Validation Loss: 0.0073
Epoch [142/650], Train Loss: 0.0048, Train L1 Loss: 0.4574
Epoch [142/650], Validation Loss: 0.0073, Validation L1: 0.5667, Smoothed Validation Loss: 0.0073
Epoch [143/650], Train Loss: 0.0048, Train L1 Loss: 0.4573
Epoch [143/650], Validation Loss: 0.0073, Validation L1: 0.5667, Smoothed Validation Loss: 0.0073
Epoch [144/650], Train Loss: 0.0048, Train L1 Loss: 0.4572
Epoch [144/650], Validation Loss: 0.0073, Validation L1: 0.5667, Smoothed Validation Loss: 0.0073
Epoch [145/650], Train Loss: 0.0048, Train L1 Loss: 0.4571
Epoch [145/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch [146/650], Train Loss: 0.0048, Train L1 Loss: 0.4570
Epoch [146/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch [147/650], Train Loss: 0.0048, Train L1 Loss: 0.4569
Epoch [147/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch 00147: reducing learning rate of group 0 to 1.9531e-06.
Epoch [148/650], Train Loss: 0.0047, Train L1 Loss: 0.4568
Epoch [148/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch [149/650], Train Loss: 0.0047, Train L1 Loss: 0.4567
Epoch [149/650], Validation Loss: 0.0073, Validation L1: 0.5667, Smoothed Validation Loss: 0.0073
Epoch [150/650], Train Loss: 0.0047, Train L1 Loss: 0.4566
Epoch [150/650], Validation Loss: 0.0073, Validation L1: 0.5667, Smoothed Validation Loss: 0.0073
Epoch [151/650], Train Loss: 0.0047, Train L1 Loss: 0.4565
Epoch [151/650], Validation Loss: 0.0073, Validation L1: 0.5667, Smoothed Validation Loss: 0.0073
Epoch [152/650], Train Loss: 0.0047, Train L1 Loss: 0.4565
Epoch [152/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch [153/650], Train Loss: 0.0047, Train L1 Loss: 0.4564
Epoch [153/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch [154/650], Train Loss: 0.0047, Train L1 Loss: 0.4564
Epoch [154/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch [155/650], Train Loss: 0.0047, Train L1 Loss: 0.4563
Epoch [155/650], Validation Loss: 0.0073, Validation L1: 0.5668, Smoothed Validation Loss: 0.0073
Epoch 00155: reducing learning rate of group 0 to 9.7656e-07.
Epoch [156/650], Train Loss: 0.0047, Train L1 Loss: 0.4561
Epoch [156/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0073
Epoch [157/650], Train Loss: 0.0047, Train L1 Loss: 0.4561
Epoch [157/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0073
Epoch [158/650], Train Loss: 0.0047, Train L1 Loss: 0.4561
Epoch [158/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0073
Epoch [159/650], Train Loss: 0.0047, Train L1 Loss: 0.4560
Epoch [159/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0073
Epoch [160/650], Train Loss: 0.0047, Train L1 Loss: 0.4560
Epoch [160/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0073
Epoch [161/650], Train Loss: 0.0047, Train L1 Loss: 0.4560
Epoch [161/650], Validation Loss: 0.0073, Validation L1: 0.5669, Smoothed Validation Loss: 0.0073
Epoch 00161: reducing learning rate of group 0 to 4.8828e-07.
Epoch [162/650], Train Loss: 0.0047, Train L1 Loss: 0.4558
Epoch [162/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch [163/650], Train Loss: 0.0047, Train L1 Loss: 0.4558
Epoch [163/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch [164/650], Train Loss: 0.0047, Train L1 Loss: 0.4558
Epoch [164/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch [165/650], Train Loss: 0.0047, Train L1 Loss: 0.4558
Epoch [165/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch [166/650], Train Loss: 0.0047, Train L1 Loss: 0.4558
Epoch [166/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch [167/650], Train Loss: 0.0047, Train L1 Loss: 0.4558
Epoch [167/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch 00167: reducing learning rate of group 0 to 2.4414e-07.
Epoch [168/650], Train Loss: 0.0047, Train L1 Loss: 0.4557
Epoch [168/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch [169/650], Train Loss: 0.0047, Train L1 Loss: 0.4557
Epoch [169/650], Validation Loss: 0.0073, Validation L1: 0.5670, Smoothed Validation Loss: 0.0073
Epoch [170/650], Train Loss: 0.0047, Train L1 Loss: 0.4557
Epoch [170/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [171/650], Train Loss: 0.0047, Train L1 Loss: 0.4557
Epoch [171/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [172/650], Train Loss: 0.0047, Train L1 Loss: 0.4557
Epoch [172/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [173/650], Train Loss: 0.0047, Train L1 Loss: 0.4557
Epoch [173/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch 00173: reducing learning rate of group 0 to 1.2207e-07.
Epoch [174/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [174/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [175/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [175/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [176/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [176/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [177/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [177/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [178/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [178/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [179/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [179/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch 00179: reducing learning rate of group 0 to 6.1035e-08.
Epoch [180/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [180/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [181/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [181/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [182/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [182/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [183/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [183/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [184/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [184/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [185/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [185/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch 00185: reducing learning rate of group 0 to 3.0518e-08.
Epoch [186/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [186/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [187/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [187/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [188/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [188/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [189/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [189/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [190/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [190/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [191/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [191/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch 00191: reducing learning rate of group 0 to 1.5259e-08.
Epoch [192/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [192/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [193/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [193/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [194/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [194/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [195/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [195/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [196/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [196/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [197/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [197/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [198/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [198/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [199/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [199/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [200/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [200/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [201/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [201/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [202/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [202/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [203/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [203/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [204/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [204/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [205/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [205/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [206/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [206/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [207/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [207/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [208/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [208/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [209/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [209/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [210/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [210/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [211/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [211/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [212/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [212/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [213/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [213/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [214/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [214/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [215/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [215/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [216/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [216/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [217/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [217/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [218/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [218/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [219/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [219/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [220/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [220/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [221/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [221/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [222/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [222/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [223/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [223/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [224/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [224/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [225/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [225/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [226/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [226/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [227/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [227/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [228/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [228/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [229/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [229/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [230/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [230/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [231/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [231/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [232/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [232/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [233/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [233/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [234/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [234/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [235/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [235/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [236/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [236/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [237/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [237/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [238/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [238/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [239/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [239/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [240/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [240/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [241/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [241/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [242/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [242/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [243/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [243/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [244/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [244/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [245/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [245/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [246/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [246/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [247/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [247/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [248/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [248/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [249/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [249/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [250/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [250/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [251/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [251/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [252/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [252/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [253/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [253/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [254/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [254/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [255/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [255/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [256/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [256/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [257/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [257/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [258/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [258/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [259/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [259/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [260/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [260/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [261/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [261/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [262/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [262/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [263/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [263/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [264/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [264/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [265/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [265/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [266/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [266/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [267/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [267/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [268/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [268/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [269/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [269/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [270/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [270/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [271/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [271/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [272/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [272/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [273/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [273/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [274/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [274/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [275/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [275/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [276/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [276/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [277/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [277/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [278/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [278/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [279/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [279/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [280/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [280/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [281/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [281/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [282/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [282/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [283/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [283/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [284/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [284/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [285/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [285/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [286/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [286/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [287/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [287/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [288/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [288/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [289/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [289/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [290/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [290/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [291/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [291/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [292/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [292/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [293/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [293/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [294/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [294/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [295/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [295/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [296/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [296/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [297/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [297/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [298/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [298/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [299/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [299/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [300/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [300/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [301/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [301/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [302/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [302/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [303/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [303/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [304/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [304/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [305/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [305/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [306/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [306/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [307/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [307/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [308/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [308/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [309/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [309/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [310/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [310/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [311/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [311/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [312/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [312/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [313/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [313/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [314/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [314/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [315/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [315/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [316/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [316/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [317/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [317/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [318/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [318/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [319/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [319/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [320/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [320/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [321/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [321/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [322/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [322/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [323/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [323/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [324/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [324/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [325/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [325/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [326/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [326/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [327/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [327/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [328/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [328/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [329/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [329/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [330/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [330/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [331/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [331/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [332/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [332/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [333/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [333/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [334/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [334/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [335/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [335/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [336/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [336/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [337/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [337/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [338/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [338/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [339/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [339/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [340/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [340/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [341/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [341/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [342/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [342/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [343/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [343/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [344/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [344/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [345/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [345/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [346/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [346/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [347/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [347/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [348/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [348/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [349/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [349/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [350/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [350/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [351/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [351/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [352/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [352/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [353/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [353/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [354/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [354/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [355/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [355/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [356/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [356/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [357/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [357/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [358/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [358/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [359/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [359/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [360/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [360/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [361/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [361/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [362/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [362/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [363/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [363/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [364/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [364/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [365/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [365/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [366/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [366/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [367/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [367/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [368/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [368/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [369/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [369/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [370/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [370/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [371/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [371/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [372/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [372/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [373/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [373/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [374/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [374/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [375/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [375/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [376/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [376/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [377/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [377/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [378/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [378/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [379/650], Train Loss: 0.0047, Train L1 Loss: 0.4556
Epoch [379/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [380/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [380/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [381/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [381/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [382/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [382/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [383/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [383/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [384/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [384/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [385/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [385/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [386/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [386/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [387/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [387/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [388/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [388/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [389/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [389/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [390/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [390/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [391/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [391/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [392/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [392/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [393/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [393/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [394/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [394/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [395/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [395/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [396/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [396/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [397/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [397/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [398/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [398/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [399/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [399/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [400/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [400/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [401/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [401/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [402/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [402/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [403/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [403/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [404/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [404/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [405/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [405/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [406/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [406/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [407/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [407/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [408/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [408/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [409/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [409/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [410/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [410/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [411/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [411/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [412/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [412/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [413/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [413/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [414/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [414/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [415/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [415/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [416/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [416/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [417/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [417/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [418/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [418/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [419/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [419/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [420/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [420/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [421/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [421/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [422/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [422/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [423/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [423/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [424/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [424/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [425/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [425/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [426/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [426/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [427/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [427/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [428/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [428/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [429/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [429/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [430/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [430/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [431/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [431/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [432/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [432/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [433/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [433/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [434/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [434/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [435/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [435/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [436/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [436/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [437/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [437/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [438/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [438/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [439/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [439/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [440/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [440/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [441/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [441/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [442/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [442/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [443/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [443/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [444/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [444/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [445/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [445/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [446/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [446/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [447/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [447/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [448/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [448/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [449/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [449/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [450/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [450/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [451/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [451/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [452/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [452/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [453/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [453/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [454/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [454/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [455/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [455/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [456/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [456/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [457/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [457/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [458/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [458/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [459/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [459/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [460/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [460/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [461/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [461/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [462/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [462/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [463/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [463/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [464/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [464/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [465/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [465/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [466/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [466/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [467/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [467/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [468/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [468/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [469/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [469/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [470/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [470/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [471/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [471/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [472/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [472/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [473/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [473/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [474/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [474/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [475/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [475/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [476/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [476/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [477/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [477/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [478/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [478/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [479/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [479/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [480/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [480/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [481/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [481/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [482/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [482/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [483/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [483/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [484/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [484/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [485/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [485/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [486/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [486/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [487/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [487/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [488/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [488/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [489/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [489/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [490/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [490/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [491/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [491/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [492/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [492/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [493/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [493/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [494/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [494/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [495/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [495/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [496/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [496/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [497/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [497/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [498/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [498/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [499/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [499/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [500/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [500/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [501/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [501/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [502/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [502/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [503/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [503/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [504/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [504/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [505/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [505/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [506/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [506/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [507/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [507/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [508/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [508/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [509/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [509/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [510/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [510/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [511/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [511/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [512/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [512/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [513/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [513/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [514/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [514/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [515/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [515/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [516/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [516/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [517/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [517/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [518/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [518/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [519/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [519/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [520/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [520/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [521/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [521/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [522/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [522/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [523/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [523/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [524/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [524/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [525/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [525/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [526/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [526/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [527/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [527/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [528/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [528/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [529/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [529/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [530/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [530/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [531/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [531/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [532/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [532/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [533/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [533/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [534/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [534/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [535/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [535/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [536/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [536/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [537/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [537/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [538/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [538/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [539/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [539/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [540/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [540/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [541/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [541/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [542/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [542/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [543/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [543/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [544/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [544/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [545/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [545/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [546/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [546/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [547/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [547/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [548/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [548/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [549/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [549/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [550/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [550/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [551/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [551/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [552/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [552/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [553/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [553/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [554/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [554/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [555/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [555/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [556/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [556/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [557/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [557/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [558/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [558/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [559/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [559/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [560/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [560/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [561/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [561/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [562/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [562/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [563/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [563/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [564/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [564/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [565/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [565/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [566/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [566/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [567/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [567/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [568/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [568/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [569/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [569/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [570/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [570/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [571/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [571/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [572/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [572/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [573/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [573/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [574/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [574/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [575/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [575/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [576/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [576/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [577/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [577/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [578/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [578/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [579/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [579/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [580/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [580/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [581/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [581/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [582/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [582/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [583/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [583/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [584/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [584/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [585/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [585/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [586/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [586/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [587/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [587/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [588/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [588/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [589/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [589/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [590/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [590/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [591/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [591/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [592/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [592/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [593/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [593/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [594/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [594/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [595/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [595/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [596/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [596/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [597/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [597/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [598/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [598/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [599/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [599/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [600/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [600/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [601/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [601/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [602/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [602/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [603/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [603/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [604/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [604/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [605/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [605/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [606/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [606/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [607/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [607/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [608/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [608/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [609/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [609/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [610/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [610/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [611/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [611/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [612/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [612/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [613/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [613/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [614/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [614/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [615/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [615/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [616/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [616/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [617/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [617/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [618/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [618/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [619/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [619/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [620/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [620/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [621/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [621/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [622/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [622/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [623/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [623/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [624/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [624/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [625/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [625/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [626/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [626/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [627/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [627/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [628/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [628/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [629/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [629/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [630/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [630/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [631/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [631/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [632/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [632/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [633/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [633/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [634/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [634/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [635/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [635/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [636/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [636/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [637/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [637/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [638/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [638/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [639/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [639/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [640/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [640/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [641/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [641/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [642/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [642/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [643/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [643/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [644/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [644/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [645/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [645/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [646/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [646/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [647/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [647/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [648/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [648/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [649/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [649/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
Epoch [650/650], Train Loss: 0.0047, Train L1 Loss: 0.4555
Epoch [650/650], Validation Loss: 0.0073, Validation L1: 0.5671, Smoothed Validation Loss: 0.0073
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19630796: <WorkingSetup_3> in cluster <dcc> Done

Job <WorkingSetup_3> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 13:59:43 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Fri Dec  1 20:22:17 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Fri Dec  1 20:22:17 2023
Terminated at Sat Dec  2 06:21:04 2023
Results reported at Sat Dec  2 06:21:04 2023

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

    CPU time :                                   36180.98 sec.
    Max Memory :                                 1926 MB
    Average Memory :                             1914.99 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63610.00 MB
    Max Swap :                                   -
    Max Processes :                              11
    Max Threads :                                49
    Run time :                                   35930 sec.
    Turnaround time :                            145281 sec.

The output (if any) is above this job summary.

