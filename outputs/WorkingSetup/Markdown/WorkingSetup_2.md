
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
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231201_062218-xg7prq77
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 2WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/xg7prq77
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:31,450] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7faaecc63a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:35,252] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpy9vxgxnp.py line 218 
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,231] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpy9vxgxnp.py line 117 
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,719] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpy9vxgxnp.py line 90 
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:41,832] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:42,392] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:44,783] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:45,741] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] 
[2023-12-01 06:22:46,756] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.007 MB uploadedwandb: / 0.005 MB of 0.007 MB uploadedwandb: - 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▅▅▄▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▆▅▄▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▅▃▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▄▂▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.00171
wandb:     train l1 loss 0.19708
wandb:        train_loss 0.00085
wandb:       val l1 loss 0.2692
wandb:          val loss 0.00171
wandb: 
wandb: 🚀 View run 2WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/xg7prq77
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231201_062218-xg7prq77/logs
Epoch [1/650], Train Loss: 0.0210, Train L1 Loss: 0.5784
Epoch [1/650], Validation Loss: 0.0064, Validation L1: 0.5746, Smoothed Validation Loss: 0.0064
Epoch [2/650], Train Loss: 0.0041, Train L1 Loss: 0.4272
Epoch [2/650], Validation Loss: 0.0066, Validation L1: 0.5970, Smoothed Validation Loss: 0.0064
Epoch [3/650], Train Loss: 0.0034, Train L1 Loss: 0.3875
Epoch [3/650], Validation Loss: 0.0045, Validation L1: 0.4759, Smoothed Validation Loss: 0.0062
Epoch [4/650], Train Loss: 0.0031, Train L1 Loss: 0.3731
Epoch [4/650], Validation Loss: 0.0042, Validation L1: 0.4561, Smoothed Validation Loss: 0.0060
Epoch [5/650], Train Loss: 0.0029, Train L1 Loss: 0.3607
Epoch [5/650], Validation Loss: 0.0033, Validation L1: 0.3961, Smoothed Validation Loss: 0.0057
Epoch [6/650], Train Loss: 0.0027, Train L1 Loss: 0.3513
Epoch [6/650], Validation Loss: 0.0030, Validation L1: 0.3689, Smoothed Validation Loss: 0.0055
Epoch [7/650], Train Loss: 0.0026, Train L1 Loss: 0.3455
Epoch [7/650], Validation Loss: 0.0026, Validation L1: 0.3373, Smoothed Validation Loss: 0.0052
Epoch [8/650], Train Loss: 0.0025, Train L1 Loss: 0.3386
Epoch [8/650], Validation Loss: 0.0026, Validation L1: 0.3421, Smoothed Validation Loss: 0.0049
Epoch [9/650], Train Loss: 0.0025, Train L1 Loss: 0.3332
Epoch [9/650], Validation Loss: 0.0025, Validation L1: 0.3361, Smoothed Validation Loss: 0.0047
Epoch [10/650], Train Loss: 0.0024, Train L1 Loss: 0.3294
Epoch [10/650], Validation Loss: 0.0023, Validation L1: 0.3211, Smoothed Validation Loss: 0.0044
Epoch [11/650], Train Loss: 0.0023, Train L1 Loss: 0.3249
Epoch [11/650], Validation Loss: 0.0023, Validation L1: 0.3178, Smoothed Validation Loss: 0.0042
Epoch [12/650], Train Loss: 0.0023, Train L1 Loss: 0.3217
Epoch [12/650], Validation Loss: 0.0022, Validation L1: 0.3078, Smoothed Validation Loss: 0.0040
Epoch [13/650], Train Loss: 0.0022, Train L1 Loss: 0.3180
Epoch [13/650], Validation Loss: 0.0021, Validation L1: 0.3066, Smoothed Validation Loss: 0.0038
Epoch [14/650], Train Loss: 0.0022, Train L1 Loss: 0.3158
Epoch [14/650], Validation Loss: 0.0021, Validation L1: 0.3032, Smoothed Validation Loss: 0.0036
Epoch [15/650], Train Loss: 0.0022, Train L1 Loss: 0.3124
Epoch [15/650], Validation Loss: 0.0021, Validation L1: 0.3063, Smoothed Validation Loss: 0.0035
Epoch [16/650], Train Loss: 0.0021, Train L1 Loss: 0.3097
Epoch [16/650], Validation Loss: 0.0021, Validation L1: 0.3012, Smoothed Validation Loss: 0.0034
Epoch [17/650], Train Loss: 0.0021, Train L1 Loss: 0.3078
Epoch [17/650], Validation Loss: 0.0020, Validation L1: 0.2942, Smoothed Validation Loss: 0.0032
Epoch [18/650], Train Loss: 0.0021, Train L1 Loss: 0.3055
Epoch [18/650], Validation Loss: 0.0020, Validation L1: 0.2953, Smoothed Validation Loss: 0.0031
Epoch [19/650], Train Loss: 0.0020, Train L1 Loss: 0.3037
Epoch [19/650], Validation Loss: 0.0020, Validation L1: 0.2946, Smoothed Validation Loss: 0.0030
Epoch [20/650], Train Loss: 0.0020, Train L1 Loss: 0.3028
Epoch [20/650], Validation Loss: 0.0022, Validation L1: 0.3154, Smoothed Validation Loss: 0.0029
Epoch [21/650], Train Loss: 0.0020, Train L1 Loss: 0.3010
Epoch [21/650], Validation Loss: 0.0021, Validation L1: 0.3094, Smoothed Validation Loss: 0.0028
Epoch [22/650], Train Loss: 0.0019, Train L1 Loss: 0.2979
Epoch [22/650], Validation Loss: 0.0022, Validation L1: 0.3185, Smoothed Validation Loss: 0.0028
Epoch [23/650], Train Loss: 0.0020, Train L1 Loss: 0.2983
Epoch [23/650], Validation Loss: 0.0022, Validation L1: 0.3196, Smoothed Validation Loss: 0.0027
Epoch [24/650], Train Loss: 0.0020, Train L1 Loss: 0.2975
Epoch [24/650], Validation Loss: 0.0021, Validation L1: 0.3131, Smoothed Validation Loss: 0.0026
Epoch [25/650], Train Loss: 0.0019, Train L1 Loss: 0.2939
Epoch [25/650], Validation Loss: 0.0020, Validation L1: 0.3038, Smoothed Validation Loss: 0.0026
Epoch [26/650], Train Loss: 0.0019, Train L1 Loss: 0.2928
Epoch [26/650], Validation Loss: 0.0019, Validation L1: 0.2993, Smoothed Validation Loss: 0.0025
Epoch [27/650], Train Loss: 0.0019, Train L1 Loss: 0.2920
Epoch [27/650], Validation Loss: 0.0020, Validation L1: 0.3018, Smoothed Validation Loss: 0.0025
Epoch [28/650], Train Loss: 0.0018, Train L1 Loss: 0.2894
Epoch [28/650], Validation Loss: 0.0020, Validation L1: 0.3091, Smoothed Validation Loss: 0.0024
Epoch [29/650], Train Loss: 0.0018, Train L1 Loss: 0.2888
Epoch [29/650], Validation Loss: 0.0020, Validation L1: 0.3062, Smoothed Validation Loss: 0.0024
Epoch [30/650], Train Loss: 0.0018, Train L1 Loss: 0.2874
Epoch [30/650], Validation Loss: 0.0020, Validation L1: 0.3030, Smoothed Validation Loss: 0.0023
Epoch [31/650], Train Loss: 0.0018, Train L1 Loss: 0.2874
Epoch [31/650], Validation Loss: 0.0019, Validation L1: 0.2960, Smoothed Validation Loss: 0.0023
Epoch [32/650], Train Loss: 0.0018, Train L1 Loss: 0.2865
Epoch [32/650], Validation Loss: 0.0020, Validation L1: 0.3048, Smoothed Validation Loss: 0.0023
Epoch [33/650], Train Loss: 0.0018, Train L1 Loss: 0.2853
Epoch [33/650], Validation Loss: 0.0020, Validation L1: 0.3089, Smoothed Validation Loss: 0.0022
Epoch [34/650], Train Loss: 0.0017, Train L1 Loss: 0.2834
Epoch [34/650], Validation Loss: 0.0019, Validation L1: 0.2980, Smoothed Validation Loss: 0.0022
Epoch [35/650], Train Loss: 0.0018, Train L1 Loss: 0.2842
Epoch [35/650], Validation Loss: 0.0019, Validation L1: 0.2964, Smoothed Validation Loss: 0.0022
Epoch [36/650], Train Loss: 0.0017, Train L1 Loss: 0.2824
Epoch [36/650], Validation Loss: 0.0019, Validation L1: 0.2948, Smoothed Validation Loss: 0.0022
Epoch [37/650], Train Loss: 0.0017, Train L1 Loss: 0.2803
Epoch [37/650], Validation Loss: 0.0019, Validation L1: 0.2946, Smoothed Validation Loss: 0.0021
Epoch [38/650], Train Loss: 0.0017, Train L1 Loss: 0.2811
Epoch [38/650], Validation Loss: 0.0019, Validation L1: 0.2992, Smoothed Validation Loss: 0.0021
Epoch [39/650], Train Loss: 0.0017, Train L1 Loss: 0.2825
Epoch [39/650], Validation Loss: 0.0019, Validation L1: 0.3020, Smoothed Validation Loss: 0.0021
Epoch [40/650], Train Loss: 0.0017, Train L1 Loss: 0.2794
Epoch [40/650], Validation Loss: 0.0019, Validation L1: 0.2901, Smoothed Validation Loss: 0.0021
Epoch [41/650], Train Loss: 0.0017, Train L1 Loss: 0.2775
Epoch [41/650], Validation Loss: 0.0019, Validation L1: 0.2970, Smoothed Validation Loss: 0.0021
Epoch [42/650], Train Loss: 0.0017, Train L1 Loss: 0.2800
Epoch [42/650], Validation Loss: 0.0018, Validation L1: 0.2908, Smoothed Validation Loss: 0.0020
Epoch [43/650], Train Loss: 0.0017, Train L1 Loss: 0.2784
Epoch [43/650], Validation Loss: 0.0020, Validation L1: 0.3065, Smoothed Validation Loss: 0.0020
Epoch [44/650], Train Loss: 0.0017, Train L1 Loss: 0.2769
Epoch [44/650], Validation Loss: 0.0018, Validation L1: 0.2897, Smoothed Validation Loss: 0.0020
Epoch [45/650], Train Loss: 0.0016, Train L1 Loss: 0.2755
Epoch [45/650], Validation Loss: 0.0019, Validation L1: 0.2965, Smoothed Validation Loss: 0.0020
Epoch [46/650], Train Loss: 0.0016, Train L1 Loss: 0.2746
Epoch [46/650], Validation Loss: 0.0020, Validation L1: 0.2998, Smoothed Validation Loss: 0.0020
Epoch [47/650], Train Loss: 0.0016, Train L1 Loss: 0.2738
Epoch [47/650], Validation Loss: 0.0019, Validation L1: 0.2966, Smoothed Validation Loss: 0.0020
Epoch [48/650], Train Loss: 0.0016, Train L1 Loss: 0.2740
Epoch [48/650], Validation Loss: 0.0019, Validation L1: 0.2979, Smoothed Validation Loss: 0.0020
Epoch [49/650], Train Loss: 0.0016, Train L1 Loss: 0.2729
Epoch [49/650], Validation Loss: 0.0019, Validation L1: 0.2952, Smoothed Validation Loss: 0.0020
Epoch [50/650], Train Loss: 0.0016, Train L1 Loss: 0.2727
Epoch [50/650], Validation Loss: 0.0019, Validation L1: 0.2986, Smoothed Validation Loss: 0.0020
Epoch [51/650], Train Loss: 0.0016, Train L1 Loss: 0.2717
Epoch [51/650], Validation Loss: 0.0018, Validation L1: 0.2930, Smoothed Validation Loss: 0.0020
Epoch [52/650], Train Loss: 0.0016, Train L1 Loss: 0.2713
Epoch [52/650], Validation Loss: 0.0019, Validation L1: 0.2978, Smoothed Validation Loss: 0.0020
Epoch [53/650], Train Loss: 0.0016, Train L1 Loss: 0.2715
Epoch [53/650], Validation Loss: 0.0019, Validation L1: 0.2949, Smoothed Validation Loss: 0.0019
Epoch [54/650], Train Loss: 0.0016, Train L1 Loss: 0.2709
Epoch [54/650], Validation Loss: 0.0019, Validation L1: 0.2987, Smoothed Validation Loss: 0.0019
Epoch [55/650], Train Loss: 0.0016, Train L1 Loss: 0.2706
Epoch [55/650], Validation Loss: 0.0020, Validation L1: 0.3026, Smoothed Validation Loss: 0.0019
Epoch [56/650], Train Loss: 0.0016, Train L1 Loss: 0.2699
Epoch [56/650], Validation Loss: 0.0020, Validation L1: 0.3024, Smoothed Validation Loss: 0.0020
Epoch [57/650], Train Loss: 0.0016, Train L1 Loss: 0.2731
Epoch [57/650], Validation Loss: 0.0019, Validation L1: 0.2994, Smoothed Validation Loss: 0.0019
Epoch [58/650], Train Loss: 0.0016, Train L1 Loss: 0.2707
Epoch [58/650], Validation Loss: 0.0019, Validation L1: 0.2955, Smoothed Validation Loss: 0.0019
Epoch [59/650], Train Loss: 0.0016, Train L1 Loss: 0.2678
Epoch [59/650], Validation Loss: 0.0018, Validation L1: 0.2887, Smoothed Validation Loss: 0.0019
Epoch [60/650], Train Loss: 0.0015, Train L1 Loss: 0.2668
Epoch [60/650], Validation Loss: 0.0020, Validation L1: 0.3050, Smoothed Validation Loss: 0.0019
Epoch [61/650], Train Loss: 0.0015, Train L1 Loss: 0.2676
Epoch [61/650], Validation Loss: 0.0018, Validation L1: 0.2881, Smoothed Validation Loss: 0.0019
Epoch [62/650], Train Loss: 0.0015, Train L1 Loss: 0.2678
Epoch [62/650], Validation Loss: 0.0019, Validation L1: 0.2982, Smoothed Validation Loss: 0.0019
Epoch [63/650], Train Loss: 0.0016, Train L1 Loss: 0.2675
Epoch [63/650], Validation Loss: 0.0019, Validation L1: 0.2989, Smoothed Validation Loss: 0.0019
Epoch [64/650], Train Loss: 0.0015, Train L1 Loss: 0.2665
Epoch [64/650], Validation Loss: 0.0018, Validation L1: 0.2902, Smoothed Validation Loss: 0.0019
Epoch [65/650], Train Loss: 0.0015, Train L1 Loss: 0.2666
Epoch [65/650], Validation Loss: 0.0018, Validation L1: 0.2819, Smoothed Validation Loss: 0.0019
Epoch [66/650], Train Loss: 0.0015, Train L1 Loss: 0.2658
Epoch [66/650], Validation Loss: 0.0019, Validation L1: 0.2940, Smoothed Validation Loss: 0.0019
Epoch [67/650], Train Loss: 0.0015, Train L1 Loss: 0.2648
Epoch [67/650], Validation Loss: 0.0019, Validation L1: 0.2906, Smoothed Validation Loss: 0.0019
Epoch [68/650], Train Loss: 0.0015, Train L1 Loss: 0.2649
Epoch [68/650], Validation Loss: 0.0019, Validation L1: 0.2968, Smoothed Validation Loss: 0.0019
Epoch [69/650], Train Loss: 0.0015, Train L1 Loss: 0.2646
Epoch [69/650], Validation Loss: 0.0019, Validation L1: 0.2890, Smoothed Validation Loss: 0.0019
Epoch [70/650], Train Loss: 0.0015, Train L1 Loss: 0.2638
Epoch [70/650], Validation Loss: 0.0019, Validation L1: 0.2919, Smoothed Validation Loss: 0.0019
Epoch [71/650], Train Loss: 0.0015, Train L1 Loss: 0.2628
Epoch [71/650], Validation Loss: 0.0019, Validation L1: 0.2946, Smoothed Validation Loss: 0.0019
Epoch [72/650], Train Loss: 0.0015, Train L1 Loss: 0.2619
Epoch [72/650], Validation Loss: 0.0019, Validation L1: 0.2942, Smoothed Validation Loss: 0.0019
Epoch [73/650], Train Loss: 0.0015, Train L1 Loss: 0.2623
Epoch [73/650], Validation Loss: 0.0018, Validation L1: 0.2843, Smoothed Validation Loss: 0.0019
Epoch [74/650], Train Loss: 0.0015, Train L1 Loss: 0.2615
Epoch [74/650], Validation Loss: 0.0019, Validation L1: 0.2890, Smoothed Validation Loss: 0.0019
Epoch [75/650], Train Loss: 0.0015, Train L1 Loss: 0.2638
Epoch [75/650], Validation Loss: 0.0018, Validation L1: 0.2869, Smoothed Validation Loss: 0.0019
Epoch [76/650], Train Loss: 0.0015, Train L1 Loss: 0.2618
Epoch [76/650], Validation Loss: 0.0019, Validation L1: 0.2948, Smoothed Validation Loss: 0.0019
Epoch [77/650], Train Loss: 0.0015, Train L1 Loss: 0.2619
Epoch [77/650], Validation Loss: 0.0018, Validation L1: 0.2841, Smoothed Validation Loss: 0.0019
Epoch [78/650], Train Loss: 0.0015, Train L1 Loss: 0.2666
Epoch [78/650], Validation Loss: 0.0018, Validation L1: 0.2833, Smoothed Validation Loss: 0.0019
Epoch [79/650], Train Loss: 0.0014, Train L1 Loss: 0.2599
Epoch [79/650], Validation Loss: 0.0018, Validation L1: 0.2874, Smoothed Validation Loss: 0.0019
Epoch [80/650], Train Loss: 0.0015, Train L1 Loss: 0.2615
Epoch [80/650], Validation Loss: 0.0018, Validation L1: 0.2889, Smoothed Validation Loss: 0.0019
Epoch [81/650], Train Loss: 0.0015, Train L1 Loss: 0.2609
Epoch [81/650], Validation Loss: 0.0018, Validation L1: 0.2838, Smoothed Validation Loss: 0.0019
Epoch [82/650], Train Loss: 0.0015, Train L1 Loss: 0.2605
Epoch [82/650], Validation Loss: 0.0019, Validation L1: 0.2948, Smoothed Validation Loss: 0.0019
Epoch [83/650], Train Loss: 0.0015, Train L1 Loss: 0.2612
Epoch [83/650], Validation Loss: 0.0018, Validation L1: 0.2863, Smoothed Validation Loss: 0.0019
Epoch [84/650], Train Loss: 0.0014, Train L1 Loss: 0.2598
Epoch [84/650], Validation Loss: 0.0019, Validation L1: 0.2904, Smoothed Validation Loss: 0.0019
Epoch [85/650], Train Loss: 0.0014, Train L1 Loss: 0.2587
Epoch [85/650], Validation Loss: 0.0018, Validation L1: 0.2865, Smoothed Validation Loss: 0.0019
Epoch [86/650], Train Loss: 0.0015, Train L1 Loss: 0.2598
Epoch [86/650], Validation Loss: 0.0020, Validation L1: 0.2934, Smoothed Validation Loss: 0.0019
Epoch [87/650], Train Loss: 0.0014, Train L1 Loss: 0.2594
Epoch [87/650], Validation Loss: 0.0020, Validation L1: 0.2948, Smoothed Validation Loss: 0.0019
Epoch 00087: reducing learning rate of group 0 to 5.0000e-04.
Epoch [88/650], Train Loss: 0.0013, Train L1 Loss: 0.2458
Epoch [88/650], Validation Loss: 0.0018, Validation L1: 0.2816, Smoothed Validation Loss: 0.0019
Epoch [89/650], Train Loss: 0.0012, Train L1 Loss: 0.2414
Epoch [89/650], Validation Loss: 0.0018, Validation L1: 0.2818, Smoothed Validation Loss: 0.0019
Epoch [90/650], Train Loss: 0.0012, Train L1 Loss: 0.2396
Epoch [90/650], Validation Loss: 0.0019, Validation L1: 0.2847, Smoothed Validation Loss: 0.0019
Epoch [91/650], Train Loss: 0.0012, Train L1 Loss: 0.2380
Epoch [91/650], Validation Loss: 0.0019, Validation L1: 0.2851, Smoothed Validation Loss: 0.0019
Epoch [92/650], Train Loss: 0.0012, Train L1 Loss: 0.2371
Epoch [92/650], Validation Loss: 0.0018, Validation L1: 0.2836, Smoothed Validation Loss: 0.0019
Epoch [93/650], Train Loss: 0.0012, Train L1 Loss: 0.2361
Epoch [93/650], Validation Loss: 0.0019, Validation L1: 0.2853, Smoothed Validation Loss: 0.0019
Epoch 00093: reducing learning rate of group 0 to 2.5000e-04.
Epoch [94/650], Train Loss: 0.0012, Train L1 Loss: 0.2330
Epoch [94/650], Validation Loss: 0.0016, Validation L1: 0.2694, Smoothed Validation Loss: 0.0018
Epoch [95/650], Train Loss: 0.0011, Train L1 Loss: 0.2293
Epoch [95/650], Validation Loss: 0.0016, Validation L1: 0.2695, Smoothed Validation Loss: 0.0018
Epoch [96/650], Train Loss: 0.0011, Train L1 Loss: 0.2273
Epoch [96/650], Validation Loss: 0.0017, Validation L1: 0.2701, Smoothed Validation Loss: 0.0018
Epoch [97/650], Train Loss: 0.0011, Train L1 Loss: 0.2258
Epoch [97/650], Validation Loss: 0.0017, Validation L1: 0.2708, Smoothed Validation Loss: 0.0018
Epoch [98/650], Train Loss: 0.0011, Train L1 Loss: 0.2246
Epoch [98/650], Validation Loss: 0.0017, Validation L1: 0.2711, Smoothed Validation Loss: 0.0018
Epoch [99/650], Train Loss: 0.0011, Train L1 Loss: 0.2234
Epoch [99/650], Validation Loss: 0.0017, Validation L1: 0.2715, Smoothed Validation Loss: 0.0018
Epoch [100/650], Train Loss: 0.0011, Train L1 Loss: 0.2227
Epoch [100/650], Validation Loss: 0.0017, Validation L1: 0.2716, Smoothed Validation Loss: 0.0018
Epoch [101/650], Train Loss: 0.0011, Train L1 Loss: 0.2217
Epoch [101/650], Validation Loss: 0.0017, Validation L1: 0.2726, Smoothed Validation Loss: 0.0018
Epoch [102/650], Train Loss: 0.0010, Train L1 Loss: 0.2211
Epoch [102/650], Validation Loss: 0.0017, Validation L1: 0.2736, Smoothed Validation Loss: 0.0018
Epoch [103/650], Train Loss: 0.0010, Train L1 Loss: 0.2200
Epoch [103/650], Validation Loss: 0.0017, Validation L1: 0.2743, Smoothed Validation Loss: 0.0018
Epoch [104/650], Train Loss: 0.0010, Train L1 Loss: 0.2192
Epoch [104/650], Validation Loss: 0.0017, Validation L1: 0.2743, Smoothed Validation Loss: 0.0017
Epoch [105/650], Train Loss: 0.0010, Train L1 Loss: 0.2186
Epoch [105/650], Validation Loss: 0.0018, Validation L1: 0.2769, Smoothed Validation Loss: 0.0018
Epoch [106/650], Train Loss: 0.0010, Train L1 Loss: 0.2180
Epoch [106/650], Validation Loss: 0.0018, Validation L1: 0.2765, Smoothed Validation Loss: 0.0018
Epoch [107/650], Train Loss: 0.0010, Train L1 Loss: 0.2176
Epoch [107/650], Validation Loss: 0.0018, Validation L1: 0.2790, Smoothed Validation Loss: 0.0018
Epoch [108/650], Train Loss: 0.0010, Train L1 Loss: 0.2166
Epoch [108/650], Validation Loss: 0.0018, Validation L1: 0.2785, Smoothed Validation Loss: 0.0018
Epoch [109/650], Train Loss: 0.0010, Train L1 Loss: 0.2158
Epoch [109/650], Validation Loss: 0.0018, Validation L1: 0.2800, Smoothed Validation Loss: 0.0018
Epoch [110/650], Train Loss: 0.0010, Train L1 Loss: 0.2156
Epoch [110/650], Validation Loss: 0.0018, Validation L1: 0.2808, Smoothed Validation Loss: 0.0018
Epoch 00110: reducing learning rate of group 0 to 1.2500e-04.
Epoch [111/650], Train Loss: 0.0010, Train L1 Loss: 0.2182
Epoch [111/650], Validation Loss: 0.0017, Validation L1: 0.2728, Smoothed Validation Loss: 0.0018
Epoch [112/650], Train Loss: 0.0010, Train L1 Loss: 0.2156
Epoch [112/650], Validation Loss: 0.0017, Validation L1: 0.2727, Smoothed Validation Loss: 0.0018
Epoch [113/650], Train Loss: 0.0010, Train L1 Loss: 0.2141
Epoch [113/650], Validation Loss: 0.0017, Validation L1: 0.2731, Smoothed Validation Loss: 0.0018
Epoch [114/650], Train Loss: 0.0010, Train L1 Loss: 0.2129
Epoch [114/650], Validation Loss: 0.0018, Validation L1: 0.2735, Smoothed Validation Loss: 0.0018
Epoch [115/650], Train Loss: 0.0010, Train L1 Loss: 0.2120
Epoch [115/650], Validation Loss: 0.0018, Validation L1: 0.2739, Smoothed Validation Loss: 0.0018
Epoch [116/650], Train Loss: 0.0010, Train L1 Loss: 0.2112
Epoch [116/650], Validation Loss: 0.0018, Validation L1: 0.2743, Smoothed Validation Loss: 0.0018
Epoch 00116: reducing learning rate of group 0 to 6.2500e-05.
Epoch [117/650], Train Loss: 0.0010, Train L1 Loss: 0.2131
Epoch [117/650], Validation Loss: 0.0017, Validation L1: 0.2705, Smoothed Validation Loss: 0.0018
Epoch [118/650], Train Loss: 0.0010, Train L1 Loss: 0.2115
Epoch [118/650], Validation Loss: 0.0017, Validation L1: 0.2705, Smoothed Validation Loss: 0.0018
Epoch [119/650], Train Loss: 0.0010, Train L1 Loss: 0.2106
Epoch [119/650], Validation Loss: 0.0017, Validation L1: 0.2705, Smoothed Validation Loss: 0.0017
Epoch [120/650], Train Loss: 0.0009, Train L1 Loss: 0.2098
Epoch [120/650], Validation Loss: 0.0017, Validation L1: 0.2706, Smoothed Validation Loss: 0.0017
Epoch [121/650], Train Loss: 0.0009, Train L1 Loss: 0.2092
Epoch [121/650], Validation Loss: 0.0017, Validation L1: 0.2707, Smoothed Validation Loss: 0.0017
Epoch [122/650], Train Loss: 0.0009, Train L1 Loss: 0.2086
Epoch [122/650], Validation Loss: 0.0017, Validation L1: 0.2708, Smoothed Validation Loss: 0.0017
Epoch [123/650], Train Loss: 0.0009, Train L1 Loss: 0.2081
Epoch [123/650], Validation Loss: 0.0017, Validation L1: 0.2710, Smoothed Validation Loss: 0.0017
Epoch [124/650], Train Loss: 0.0009, Train L1 Loss: 0.2076
Epoch [124/650], Validation Loss: 0.0017, Validation L1: 0.2711, Smoothed Validation Loss: 0.0017
Epoch [125/650], Train Loss: 0.0009, Train L1 Loss: 0.2071
Epoch [125/650], Validation Loss: 0.0017, Validation L1: 0.2713, Smoothed Validation Loss: 0.0017
Epoch [126/650], Train Loss: 0.0009, Train L1 Loss: 0.2067
Epoch [126/650], Validation Loss: 0.0017, Validation L1: 0.2715, Smoothed Validation Loss: 0.0017
Epoch [127/650], Train Loss: 0.0009, Train L1 Loss: 0.2062
Epoch [127/650], Validation Loss: 0.0017, Validation L1: 0.2716, Smoothed Validation Loss: 0.0017
Epoch [128/650], Train Loss: 0.0009, Train L1 Loss: 0.2058
Epoch [128/650], Validation Loss: 0.0017, Validation L1: 0.2720, Smoothed Validation Loss: 0.0017
Epoch [129/650], Train Loss: 0.0009, Train L1 Loss: 0.2054
Epoch [129/650], Validation Loss: 0.0017, Validation L1: 0.2719, Smoothed Validation Loss: 0.0017
Epoch [130/650], Train Loss: 0.0009, Train L1 Loss: 0.2049
Epoch [130/650], Validation Loss: 0.0017, Validation L1: 0.2724, Smoothed Validation Loss: 0.0017
Epoch [131/650], Train Loss: 0.0009, Train L1 Loss: 0.2046
Epoch [131/650], Validation Loss: 0.0017, Validation L1: 0.2723, Smoothed Validation Loss: 0.0017
Epoch [132/650], Train Loss: 0.0009, Train L1 Loss: 0.2042
Epoch [132/650], Validation Loss: 0.0017, Validation L1: 0.2726, Smoothed Validation Loss: 0.0017
Epoch [133/650], Train Loss: 0.0009, Train L1 Loss: 0.2038
Epoch [133/650], Validation Loss: 0.0017, Validation L1: 0.2728, Smoothed Validation Loss: 0.0017
Epoch [134/650], Train Loss: 0.0009, Train L1 Loss: 0.2035
Epoch [134/650], Validation Loss: 0.0017, Validation L1: 0.2729, Smoothed Validation Loss: 0.0017
Epoch [135/650], Train Loss: 0.0009, Train L1 Loss: 0.2031
Epoch [135/650], Validation Loss: 0.0017, Validation L1: 0.2731, Smoothed Validation Loss: 0.0017
Epoch 00135: reducing learning rate of group 0 to 3.1250e-05.
Epoch [136/650], Train Loss: 0.0009, Train L1 Loss: 0.2051
Epoch [136/650], Validation Loss: 0.0017, Validation L1: 0.2696, Smoothed Validation Loss: 0.0017
Epoch [137/650], Train Loss: 0.0009, Train L1 Loss: 0.2043
Epoch [137/650], Validation Loss: 0.0017, Validation L1: 0.2698, Smoothed Validation Loss: 0.0017
Epoch [138/650], Train Loss: 0.0009, Train L1 Loss: 0.2038
Epoch [138/650], Validation Loss: 0.0017, Validation L1: 0.2698, Smoothed Validation Loss: 0.0017
Epoch [139/650], Train Loss: 0.0009, Train L1 Loss: 0.2034
Epoch [139/650], Validation Loss: 0.0017, Validation L1: 0.2699, Smoothed Validation Loss: 0.0017
Epoch [140/650], Train Loss: 0.0009, Train L1 Loss: 0.2031
Epoch [140/650], Validation Loss: 0.0017, Validation L1: 0.2700, Smoothed Validation Loss: 0.0017
Epoch [141/650], Train Loss: 0.0009, Train L1 Loss: 0.2027
Epoch [141/650], Validation Loss: 0.0017, Validation L1: 0.2701, Smoothed Validation Loss: 0.0017
Epoch [142/650], Train Loss: 0.0009, Train L1 Loss: 0.2025
Epoch [142/650], Validation Loss: 0.0017, Validation L1: 0.2701, Smoothed Validation Loss: 0.0017
Epoch [143/650], Train Loss: 0.0009, Train L1 Loss: 0.2022
Epoch [143/650], Validation Loss: 0.0017, Validation L1: 0.2702, Smoothed Validation Loss: 0.0017
Epoch [144/650], Train Loss: 0.0009, Train L1 Loss: 0.2019
Epoch [144/650], Validation Loss: 0.0017, Validation L1: 0.2703, Smoothed Validation Loss: 0.0017
Epoch [145/650], Train Loss: 0.0009, Train L1 Loss: 0.2017
Epoch [145/650], Validation Loss: 0.0017, Validation L1: 0.2704, Smoothed Validation Loss: 0.0017
Epoch [146/650], Train Loss: 0.0009, Train L1 Loss: 0.2014
Epoch [146/650], Validation Loss: 0.0017, Validation L1: 0.2705, Smoothed Validation Loss: 0.0017
Epoch [147/650], Train Loss: 0.0009, Train L1 Loss: 0.2012
Epoch [147/650], Validation Loss: 0.0017, Validation L1: 0.2705, Smoothed Validation Loss: 0.0017
Epoch [148/650], Train Loss: 0.0009, Train L1 Loss: 0.2009
Epoch [148/650], Validation Loss: 0.0017, Validation L1: 0.2706, Smoothed Validation Loss: 0.0017
Epoch [149/650], Train Loss: 0.0009, Train L1 Loss: 0.2007
Epoch [149/650], Validation Loss: 0.0017, Validation L1: 0.2707, Smoothed Validation Loss: 0.0017
Epoch [150/650], Train Loss: 0.0009, Train L1 Loss: 0.2005
Epoch [150/650], Validation Loss: 0.0017, Validation L1: 0.2708, Smoothed Validation Loss: 0.0017
Epoch 00150: reducing learning rate of group 0 to 1.5625e-05.
Epoch [151/650], Train Loss: 0.0009, Train L1 Loss: 0.2021
Epoch [151/650], Validation Loss: 0.0017, Validation L1: 0.2700, Smoothed Validation Loss: 0.0017
Epoch [152/650], Train Loss: 0.0009, Train L1 Loss: 0.2016
Epoch [152/650], Validation Loss: 0.0017, Validation L1: 0.2700, Smoothed Validation Loss: 0.0017
Epoch [153/650], Train Loss: 0.0009, Train L1 Loss: 0.2013
Epoch [153/650], Validation Loss: 0.0017, Validation L1: 0.2699, Smoothed Validation Loss: 0.0017
Epoch [154/650], Train Loss: 0.0009, Train L1 Loss: 0.2011
Epoch [154/650], Validation Loss: 0.0017, Validation L1: 0.2699, Smoothed Validation Loss: 0.0017
Epoch [155/650], Train Loss: 0.0009, Train L1 Loss: 0.2009
Epoch [155/650], Validation Loss: 0.0017, Validation L1: 0.2700, Smoothed Validation Loss: 0.0017
Epoch [156/650], Train Loss: 0.0009, Train L1 Loss: 0.2007
Epoch [156/650], Validation Loss: 0.0017, Validation L1: 0.2700, Smoothed Validation Loss: 0.0017
Epoch 00156: reducing learning rate of group 0 to 7.8125e-06.
Epoch [157/650], Train Loss: 0.0009, Train L1 Loss: 0.2017
Epoch [157/650], Validation Loss: 0.0017, Validation L1: 0.2695, Smoothed Validation Loss: 0.0017
Epoch [158/650], Train Loss: 0.0009, Train L1 Loss: 0.2012
Epoch [158/650], Validation Loss: 0.0017, Validation L1: 0.2695, Smoothed Validation Loss: 0.0017
Epoch [159/650], Train Loss: 0.0009, Train L1 Loss: 0.2010
Epoch [159/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [160/650], Train Loss: 0.0009, Train L1 Loss: 0.2009
Epoch [160/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [161/650], Train Loss: 0.0009, Train L1 Loss: 0.2007
Epoch [161/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [162/650], Train Loss: 0.0009, Train L1 Loss: 0.2006
Epoch [162/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [163/650], Train Loss: 0.0009, Train L1 Loss: 0.2005
Epoch [163/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [164/650], Train Loss: 0.0009, Train L1 Loss: 0.2004
Epoch [164/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [165/650], Train Loss: 0.0009, Train L1 Loss: 0.2002
Epoch [165/650], Validation Loss: 0.0017, Validation L1: 0.2695, Smoothed Validation Loss: 0.0017
Epoch [166/650], Train Loss: 0.0009, Train L1 Loss: 0.2001
Epoch [166/650], Validation Loss: 0.0017, Validation L1: 0.2695, Smoothed Validation Loss: 0.0017
Epoch [167/650], Train Loss: 0.0009, Train L1 Loss: 0.2000
Epoch [167/650], Validation Loss: 0.0017, Validation L1: 0.2695, Smoothed Validation Loss: 0.0017
Epoch [168/650], Train Loss: 0.0009, Train L1 Loss: 0.1999
Epoch [168/650], Validation Loss: 0.0017, Validation L1: 0.2695, Smoothed Validation Loss: 0.0017
Epoch [169/650], Train Loss: 0.0009, Train L1 Loss: 0.1998
Epoch [169/650], Validation Loss: 0.0017, Validation L1: 0.2695, Smoothed Validation Loss: 0.0017
Epoch [170/650], Train Loss: 0.0009, Train L1 Loss: 0.1997
Epoch [170/650], Validation Loss: 0.0017, Validation L1: 0.2696, Smoothed Validation Loss: 0.0017
Epoch [171/650], Train Loss: 0.0009, Train L1 Loss: 0.1996
Epoch [171/650], Validation Loss: 0.0017, Validation L1: 0.2696, Smoothed Validation Loss: 0.0017
Epoch [172/650], Train Loss: 0.0009, Train L1 Loss: 0.1995
Epoch [172/650], Validation Loss: 0.0017, Validation L1: 0.2696, Smoothed Validation Loss: 0.0017
Epoch [173/650], Train Loss: 0.0009, Train L1 Loss: 0.1994
Epoch [173/650], Validation Loss: 0.0017, Validation L1: 0.2696, Smoothed Validation Loss: 0.0017
Epoch [174/650], Train Loss: 0.0009, Train L1 Loss: 0.1993
Epoch [174/650], Validation Loss: 0.0017, Validation L1: 0.2696, Smoothed Validation Loss: 0.0017
Epoch 00174: reducing learning rate of group 0 to 3.9063e-06.
Epoch [175/650], Train Loss: 0.0009, Train L1 Loss: 0.1997
Epoch [175/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [176/650], Train Loss: 0.0009, Train L1 Loss: 0.1994
Epoch [176/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [177/650], Train Loss: 0.0009, Train L1 Loss: 0.1993
Epoch [177/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [178/650], Train Loss: 0.0009, Train L1 Loss: 0.1992
Epoch [178/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [179/650], Train Loss: 0.0009, Train L1 Loss: 0.1992
Epoch [179/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [180/650], Train Loss: 0.0009, Train L1 Loss: 0.1991
Epoch [180/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [181/650], Train Loss: 0.0009, Train L1 Loss: 0.1990
Epoch [181/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [182/650], Train Loss: 0.0009, Train L1 Loss: 0.1990
Epoch [182/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [183/650], Train Loss: 0.0009, Train L1 Loss: 0.1989
Epoch [183/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [184/650], Train Loss: 0.0009, Train L1 Loss: 0.1989
Epoch [184/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [185/650], Train Loss: 0.0009, Train L1 Loss: 0.1988
Epoch [185/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [186/650], Train Loss: 0.0009, Train L1 Loss: 0.1988
Epoch [186/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [187/650], Train Loss: 0.0009, Train L1 Loss: 0.1987
Epoch [187/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [188/650], Train Loss: 0.0009, Train L1 Loss: 0.1987
Epoch [188/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [189/650], Train Loss: 0.0009, Train L1 Loss: 0.1986
Epoch [189/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [190/650], Train Loss: 0.0009, Train L1 Loss: 0.1986
Epoch [190/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [191/650], Train Loss: 0.0009, Train L1 Loss: 0.1985
Epoch [191/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [192/650], Train Loss: 0.0009, Train L1 Loss: 0.1985
Epoch [192/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [193/650], Train Loss: 0.0009, Train L1 Loss: 0.1984
Epoch [193/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch [194/650], Train Loss: 0.0009, Train L1 Loss: 0.1984
Epoch [194/650], Validation Loss: 0.0017, Validation L1: 0.2694, Smoothed Validation Loss: 0.0017
Epoch 00194: reducing learning rate of group 0 to 1.9531e-06.
Epoch [195/650], Train Loss: 0.0009, Train L1 Loss: 0.1984
Epoch [195/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [196/650], Train Loss: 0.0009, Train L1 Loss: 0.1983
Epoch [196/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [197/650], Train Loss: 0.0009, Train L1 Loss: 0.1982
Epoch [197/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [198/650], Train Loss: 0.0009, Train L1 Loss: 0.1982
Epoch [198/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [199/650], Train Loss: 0.0009, Train L1 Loss: 0.1982
Epoch [199/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [200/650], Train Loss: 0.0009, Train L1 Loss: 0.1981
Epoch [200/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [201/650], Train Loss: 0.0009, Train L1 Loss: 0.1981
Epoch [201/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [202/650], Train Loss: 0.0009, Train L1 Loss: 0.1981
Epoch [202/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [203/650], Train Loss: 0.0009, Train L1 Loss: 0.1981
Epoch [203/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [204/650], Train Loss: 0.0009, Train L1 Loss: 0.1980
Epoch [204/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [205/650], Train Loss: 0.0009, Train L1 Loss: 0.1980
Epoch [205/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [206/650], Train Loss: 0.0009, Train L1 Loss: 0.1980
Epoch [206/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [207/650], Train Loss: 0.0009, Train L1 Loss: 0.1980
Epoch [207/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [208/650], Train Loss: 0.0009, Train L1 Loss: 0.1979
Epoch [208/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [209/650], Train Loss: 0.0009, Train L1 Loss: 0.1979
Epoch [209/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [210/650], Train Loss: 0.0009, Train L1 Loss: 0.1979
Epoch [210/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [211/650], Train Loss: 0.0009, Train L1 Loss: 0.1979
Epoch [211/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [212/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [212/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [213/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [213/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [214/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [214/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [215/650], Train Loss: 0.0009, Train L1 Loss: 0.1978
Epoch [215/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch 00215: reducing learning rate of group 0 to 9.7656e-07.
Epoch [216/650], Train Loss: 0.0009, Train L1 Loss: 0.1977
Epoch [216/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [217/650], Train Loss: 0.0009, Train L1 Loss: 0.1977
Epoch [217/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [218/650], Train Loss: 0.0009, Train L1 Loss: 0.1977
Epoch [218/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [219/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [219/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [220/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [220/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [221/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [221/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [222/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [222/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [223/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [223/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [224/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [224/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [225/650], Train Loss: 0.0009, Train L1 Loss: 0.1976
Epoch [225/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [226/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [226/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [227/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [227/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [228/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [228/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [229/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [229/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [230/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [230/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [231/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [231/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [232/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [232/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [233/650], Train Loss: 0.0009, Train L1 Loss: 0.1975
Epoch [233/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [234/650], Train Loss: 0.0009, Train L1 Loss: 0.1974
Epoch [234/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [235/650], Train Loss: 0.0009, Train L1 Loss: 0.1974
Epoch [235/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [236/650], Train Loss: 0.0009, Train L1 Loss: 0.1974
Epoch [236/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [237/650], Train Loss: 0.0009, Train L1 Loss: 0.1974
Epoch [237/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch [238/650], Train Loss: 0.0009, Train L1 Loss: 0.1974
Epoch [238/650], Validation Loss: 0.0017, Validation L1: 0.2693, Smoothed Validation Loss: 0.0017
Epoch 00238: reducing learning rate of group 0 to 4.8828e-07.
Epoch [239/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [239/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [240/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [240/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [241/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [241/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [242/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [242/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [243/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [243/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [244/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [244/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [245/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [245/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [246/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [246/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [247/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [247/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [248/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [248/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [249/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [249/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [250/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [250/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [251/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [251/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [252/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [252/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [253/650], Train Loss: 0.0009, Train L1 Loss: 0.1973
Epoch [253/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [254/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [254/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch 00254: reducing learning rate of group 0 to 2.4414e-07.
Epoch [255/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [255/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [256/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [256/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [257/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [257/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [258/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [258/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [259/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [259/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [260/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [260/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [261/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [261/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [262/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [262/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [263/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [263/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [264/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [264/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [265/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [265/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [266/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [266/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [267/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [267/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [268/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [268/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [269/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [269/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [270/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [270/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [271/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [271/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [272/650], Train Loss: 0.0009, Train L1 Loss: 0.1972
Epoch [272/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch 00272: reducing learning rate of group 0 to 1.2207e-07.
Epoch [273/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [273/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [274/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [274/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [275/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [275/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [276/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [276/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [277/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [277/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [278/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [278/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [279/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [279/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [280/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [280/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [281/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [281/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [282/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [282/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [283/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [283/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch 00283: reducing learning rate of group 0 to 6.1035e-08.
Epoch [284/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [284/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [285/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [285/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [286/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [286/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [287/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [287/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [288/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [288/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [289/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [289/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [290/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [290/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [291/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [291/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [292/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [292/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [293/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [293/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [294/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [294/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [295/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [295/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch 00295: reducing learning rate of group 0 to 3.0518e-08.
Epoch [296/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [296/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [297/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [297/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [298/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [298/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [299/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [299/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [300/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [300/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [301/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [301/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch 00301: reducing learning rate of group 0 to 1.5259e-08.
Epoch [302/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [302/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [303/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [303/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [304/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [304/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [305/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [305/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [306/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [306/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [307/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [307/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [308/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [308/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [309/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [309/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [310/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [310/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [311/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [311/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [312/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [312/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [313/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [313/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [314/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [314/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [315/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [315/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [316/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [316/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [317/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [317/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [318/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [318/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [319/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [319/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [320/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [320/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [321/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [321/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [322/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [322/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [323/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [323/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [324/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [324/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [325/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [325/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [326/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [326/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [327/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [327/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [328/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [328/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [329/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [329/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [330/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [330/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [331/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [331/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [332/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [332/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [333/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [333/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [334/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [334/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [335/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [335/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [336/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [336/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [337/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [337/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [338/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [338/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [339/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [339/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [340/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [340/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [341/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [341/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [342/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [342/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [343/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [343/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [344/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [344/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [345/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [345/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [346/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [346/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [347/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [347/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [348/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [348/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [349/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [349/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [350/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [350/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [351/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [351/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [352/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [352/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [353/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [353/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [354/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [354/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [355/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [355/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [356/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [356/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [357/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [357/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [358/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [358/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [359/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [359/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [360/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [360/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [361/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [361/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [362/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [362/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [363/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [363/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [364/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [364/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [365/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [365/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [366/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [366/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [367/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [367/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [368/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [368/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [369/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [369/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [370/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [370/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [371/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [371/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [372/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [372/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [373/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [373/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [374/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [374/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [375/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [375/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [376/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [376/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [377/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [377/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [378/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [378/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [379/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [379/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [380/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [380/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [381/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [381/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [382/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [382/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [383/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [383/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [384/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [384/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [385/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [385/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [386/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [386/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [387/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [387/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [388/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [388/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [389/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [389/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [390/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [390/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [391/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [391/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [392/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [392/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [393/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [393/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [394/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [394/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [395/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [395/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [396/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [396/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [397/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [397/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [398/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [398/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [399/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [399/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [400/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [400/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [401/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [401/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [402/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [402/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [403/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [403/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [404/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [404/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [405/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [405/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [406/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [406/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [407/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [407/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [408/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [408/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [409/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [409/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [410/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [410/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [411/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [411/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [412/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [412/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [413/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [413/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [414/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [414/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [415/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [415/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [416/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [416/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [417/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [417/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [418/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [418/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [419/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [419/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [420/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [420/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [421/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [421/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [422/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [422/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [423/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [423/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [424/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [424/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [425/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [425/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [426/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [426/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [427/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [427/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [428/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [428/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [429/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [429/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [430/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [430/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [431/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [431/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [432/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [432/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [433/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [433/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [434/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [434/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [435/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [435/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [436/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [436/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [437/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [437/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [438/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [438/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [439/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [439/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [440/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [440/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [441/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [441/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [442/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [442/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [443/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [443/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [444/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [444/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [445/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [445/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [446/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [446/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [447/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [447/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [448/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [448/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [449/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [449/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [450/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [450/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [451/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [451/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [452/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [452/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [453/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [453/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [454/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [454/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [455/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [455/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [456/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [456/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [457/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [457/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [458/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [458/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [459/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [459/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [460/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [460/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [461/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [461/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [462/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [462/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [463/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [463/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [464/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [464/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [465/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [465/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [466/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [466/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [467/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [467/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [468/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [468/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [469/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [469/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [470/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [470/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [471/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [471/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [472/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [472/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [473/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [473/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [474/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [474/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [475/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [475/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [476/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [476/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [477/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [477/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [478/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [478/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [479/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [479/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [480/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [480/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [481/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [481/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [482/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [482/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [483/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [483/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [484/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [484/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [485/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [485/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [486/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [486/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [487/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [487/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [488/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [488/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [489/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [489/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [490/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [490/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [491/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [491/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [492/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [492/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [493/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [493/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [494/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [494/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [495/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [495/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [496/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [496/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [497/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [497/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [498/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [498/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [499/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [499/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [500/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [500/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [501/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [501/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [502/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [502/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [503/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [503/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [504/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [504/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [505/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [505/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [506/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [506/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [507/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [507/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [508/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [508/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [509/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [509/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [510/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [510/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [511/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [511/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [512/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [512/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [513/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [513/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [514/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [514/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [515/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [515/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [516/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [516/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [517/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [517/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [518/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [518/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [519/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [519/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [520/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [520/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [521/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [521/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [522/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [522/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [523/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [523/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [524/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [524/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [525/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [525/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [526/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [526/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [527/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [527/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [528/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [528/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [529/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [529/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [530/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [530/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [531/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [531/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [532/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [532/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [533/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [533/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [534/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [534/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [535/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [535/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [536/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [536/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [537/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [537/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [538/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [538/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [539/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [539/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [540/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [540/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [541/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [541/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [542/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [542/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [543/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [543/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [544/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [544/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [545/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [545/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [546/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [546/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [547/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [547/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [548/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [548/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [549/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [549/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [550/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [550/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [551/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [551/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [552/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [552/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [553/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [553/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [554/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [554/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [555/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [555/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [556/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [556/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [557/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [557/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [558/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [558/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [559/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [559/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [560/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [560/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [561/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [561/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [562/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [562/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [563/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [563/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [564/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [564/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [565/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [565/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [566/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [566/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [567/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [567/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [568/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [568/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [569/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [569/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [570/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [570/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [571/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [571/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [572/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [572/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [573/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [573/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [574/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [574/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [575/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [575/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [576/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [576/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [577/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [577/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [578/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [578/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [579/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [579/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [580/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [580/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [581/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [581/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [582/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [582/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [583/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [583/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [584/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [584/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [585/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [585/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [586/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [586/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [587/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [587/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [588/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [588/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [589/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [589/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [590/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [590/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [591/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [591/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [592/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [592/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [593/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [593/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [594/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [594/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [595/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [595/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [596/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [596/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [597/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [597/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [598/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [598/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [599/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [599/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [600/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [600/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [601/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [601/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [602/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [602/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [603/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [603/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [604/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [604/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [605/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [605/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [606/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [606/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [607/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [607/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [608/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [608/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [609/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [609/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [610/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [610/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [611/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [611/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [612/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [612/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [613/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [613/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [614/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [614/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [615/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [615/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [616/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [616/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [617/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [617/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [618/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [618/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [619/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [619/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [620/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [620/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [621/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [621/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [622/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [622/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [623/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [623/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [624/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [624/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [625/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [625/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [626/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [626/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [627/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [627/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [628/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [628/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [629/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [629/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [630/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [630/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [631/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [631/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [632/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [632/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [633/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [633/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [634/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [634/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [635/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [635/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [636/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [636/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [637/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [637/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [638/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [638/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [639/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [639/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [640/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [640/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [641/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [641/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [642/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [642/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [643/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [643/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [644/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [644/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [645/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [645/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [646/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [646/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [647/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [647/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [648/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [648/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [649/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [649/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
Epoch [650/650], Train Loss: 0.0009, Train L1 Loss: 0.1971
Epoch [650/650], Validation Loss: 0.0017, Validation L1: 0.2692, Smoothed Validation Loss: 0.0017
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19630795: <WorkingSetup_2> in cluster <dcc> Done

Job <WorkingSetup_2> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Thu Nov 30 13:59:43 2023
Job was executed on host(s) <4*n-62-18-8>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Fri Dec  1 06:20:30 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Fri Dec  1 06:20:30 2023
Terminated at Fri Dec  1 16:38:59 2023
Results reported at Fri Dec  1 16:38:59 2023

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

    CPU time :                                   37432.22 sec.
    Max Memory :                                 1970 MB
    Average Memory :                             1959.02 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63566.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   37110 sec.
    Turnaround time :                            95956 sec.

The output (if any) is above this job summary.

