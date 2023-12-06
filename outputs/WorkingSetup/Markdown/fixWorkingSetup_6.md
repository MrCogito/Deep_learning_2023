
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
| <c>name</c>       | <d>str</d>        | <j>"6fixWorkingSetup-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>650</f>        |
| <c>batch_size</c> | <d>int</d>        | <f>80</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |
| <c>param</c>      | <d>int</d>        | <f>6</f>          |
| <c>path</c>       | <d>str</d>        | <j>"/zhome/59/9/198225/Desktop/Deep_learning_2023/models/"</j> |

# Output

```
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231204_181115-kpqtvosw
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 6fixWorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/kpqtvosw
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:33,308] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7faae725aa40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:37,883] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpsis734zj.py line 218 
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,131] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpsis734zj.py line 117 
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,712] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpsis734zj.py line 90 
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:49,861] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:50,495] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:53,881] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:55,396] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] 
[2023-12-04 18:11:56,498] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.117 MB uploadedwandb: | 0.005 MB of 0.117 MB uploadedwandb: / 0.005 MB of 0.117 MB uploadedwandb: - 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▅▃▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▄▄▄▃▃▃▃▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▅▄▃▃▃▃▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▆▅▄▃▃▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▅▄▄▃▂▂▂▂▂▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 1e-05
wandb:     train l1 loss 0.0199
wandb:        train_loss 1e-05
wandb:       val l1 loss 0.02303
wandb:          val loss 1e-05
wandb: 
wandb: 🚀 View run 6fixWorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/kpqtvosw
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231204_181115-kpqtvosw/logs
Epoch [1/650], Train Loss: 0.0212, Train L1 Loss: 0.1813
Epoch [1/650], Validation Loss: 0.0000, Validation L1: 0.0361, Smoothed Validation Loss: 0.0000
Epoch [2/650], Train Loss: 0.0000, Train L1 Loss: 0.0364
Epoch [2/650], Validation Loss: 0.0000, Validation L1: 0.0386, Smoothed Validation Loss: 0.0000
Epoch [3/650], Train Loss: 0.0000, Train L1 Loss: 0.0387
Epoch [3/650], Validation Loss: 0.0001, Validation L1: 0.0546, Smoothed Validation Loss: 0.0000
Epoch [4/650], Train Loss: 0.0000, Train L1 Loss: 0.0481
Epoch [4/650], Validation Loss: 0.0001, Validation L1: 0.0605, Smoothed Validation Loss: 0.0000
Epoch [5/650], Train Loss: 0.0001, Train L1 Loss: 0.0514
Epoch [5/650], Validation Loss: 0.0000, Validation L1: 0.0509, Smoothed Validation Loss: 0.0000
Epoch [6/650], Train Loss: 0.0001, Train L1 Loss: 0.0507
Epoch [6/650], Validation Loss: 0.0000, Validation L1: 0.0453, Smoothed Validation Loss: 0.0000
Epoch [7/650], Train Loss: 0.0000, Train L1 Loss: 0.0467
Epoch [7/650], Validation Loss: 0.0001, Validation L1: 0.0581, Smoothed Validation Loss: 0.0000
Epoch 00007: reducing learning rate of group 0 to 5.0000e-04.
Epoch [8/650], Train Loss: 0.0000, Train L1 Loss: 0.0368
Epoch [8/650], Validation Loss: 0.0000, Validation L1: 0.0334, Smoothed Validation Loss: 0.0000
Epoch [9/650], Train Loss: 0.0000, Train L1 Loss: 0.0398
Epoch [9/650], Validation Loss: 0.0000, Validation L1: 0.0350, Smoothed Validation Loss: 0.0000
Epoch [10/650], Train Loss: 0.0000, Train L1 Loss: 0.0396
Epoch [10/650], Validation Loss: 0.0000, Validation L1: 0.0347, Smoothed Validation Loss: 0.0000
Epoch [11/650], Train Loss: 0.0000, Train L1 Loss: 0.0386
Epoch [11/650], Validation Loss: 0.0000, Validation L1: 0.0334, Smoothed Validation Loss: 0.0000
Epoch [12/650], Train Loss: 0.0004, Train L1 Loss: 0.0552
Epoch [12/650], Validation Loss: 0.0000, Validation L1: 0.0340, Smoothed Validation Loss: 0.0000
Epoch [13/650], Train Loss: 0.0000, Train L1 Loss: 0.0344
Epoch [13/650], Validation Loss: 0.0000, Validation L1: 0.0376, Smoothed Validation Loss: 0.0000
Epoch 00013: reducing learning rate of group 0 to 2.5000e-04.
Epoch [14/650], Train Loss: 0.0000, Train L1 Loss: 0.0336
Epoch [14/650], Validation Loss: 0.0000, Validation L1: 0.0354, Smoothed Validation Loss: 0.0000
Epoch [15/650], Train Loss: 0.0000, Train L1 Loss: 0.0348
Epoch [15/650], Validation Loss: 0.0000, Validation L1: 0.0335, Smoothed Validation Loss: 0.0000
Epoch [16/650], Train Loss: 0.0000, Train L1 Loss: 0.0354
Epoch [16/650], Validation Loss: 0.0000, Validation L1: 0.0333, Smoothed Validation Loss: 0.0000
Epoch [17/650], Train Loss: 0.0000, Train L1 Loss: 0.0354
Epoch [17/650], Validation Loss: 0.0000, Validation L1: 0.0335, Smoothed Validation Loss: 0.0000
Epoch [18/650], Train Loss: 0.0000, Train L1 Loss: 0.0352
Epoch [18/650], Validation Loss: 0.0000, Validation L1: 0.0370, Smoothed Validation Loss: 0.0000
Epoch [19/650], Train Loss: 0.0000, Train L1 Loss: 0.0348
Epoch [19/650], Validation Loss: 0.0000, Validation L1: 0.0376, Smoothed Validation Loss: 0.0000
Epoch 00019: reducing learning rate of group 0 to 1.2500e-04.
Epoch [20/650], Train Loss: 0.0000, Train L1 Loss: 0.0326
Epoch [20/650], Validation Loss: 0.0000, Validation L1: 0.0317, Smoothed Validation Loss: 0.0000
Epoch [21/650], Train Loss: 0.0000, Train L1 Loss: 0.0323
Epoch [21/650], Validation Loss: 0.0000, Validation L1: 0.0312, Smoothed Validation Loss: 0.0000
Epoch [22/650], Train Loss: 0.0000, Train L1 Loss: 0.0318
Epoch [22/650], Validation Loss: 0.0000, Validation L1: 0.0307, Smoothed Validation Loss: 0.0000
Epoch [23/650], Train Loss: 0.0000, Train L1 Loss: 0.0312
Epoch [23/650], Validation Loss: 0.0000, Validation L1: 0.0304, Smoothed Validation Loss: 0.0000
Epoch [24/650], Train Loss: 0.0000, Train L1 Loss: 0.0309
Epoch [24/650], Validation Loss: 0.0000, Validation L1: 0.0306, Smoothed Validation Loss: 0.0000
Epoch [25/650], Train Loss: 0.0000, Train L1 Loss: 0.0306
Epoch [25/650], Validation Loss: 0.0000, Validation L1: 0.0306, Smoothed Validation Loss: 0.0000
Epoch [26/650], Train Loss: 0.0000, Train L1 Loss: 0.0304
Epoch [26/650], Validation Loss: 0.0000, Validation L1: 0.0302, Smoothed Validation Loss: 0.0000
Epoch [27/650], Train Loss: 0.0000, Train L1 Loss: 0.0301
Epoch [27/650], Validation Loss: 0.0000, Validation L1: 0.0297, Smoothed Validation Loss: 0.0000
Epoch [28/650], Train Loss: 0.0000, Train L1 Loss: 0.0299
Epoch [28/650], Validation Loss: 0.0000, Validation L1: 0.0293, Smoothed Validation Loss: 0.0000
Epoch [29/650], Train Loss: 0.0000, Train L1 Loss: 0.0296
Epoch [29/650], Validation Loss: 0.0000, Validation L1: 0.0289, Smoothed Validation Loss: 0.0000
Epoch [30/650], Train Loss: 0.0000, Train L1 Loss: 0.0294
Epoch [30/650], Validation Loss: 0.0000, Validation L1: 0.0285, Smoothed Validation Loss: 0.0000
Epoch [31/650], Train Loss: 0.0000, Train L1 Loss: 0.0292
Epoch [31/650], Validation Loss: 0.0000, Validation L1: 0.0283, Smoothed Validation Loss: 0.0000
Epoch [32/650], Train Loss: 0.0000, Train L1 Loss: 0.0290
Epoch [32/650], Validation Loss: 0.0000, Validation L1: 0.0282, Smoothed Validation Loss: 0.0000
Epoch [33/650], Train Loss: 0.0000, Train L1 Loss: 0.0288
Epoch [33/650], Validation Loss: 0.0000, Validation L1: 0.0282, Smoothed Validation Loss: 0.0000
Epoch [34/650], Train Loss: 0.0000, Train L1 Loss: 0.0287
Epoch [34/650], Validation Loss: 0.0000, Validation L1: 0.0282, Smoothed Validation Loss: 0.0000
Epoch [35/650], Train Loss: 0.0000, Train L1 Loss: 0.0285
Epoch [35/650], Validation Loss: 0.0000, Validation L1: 0.0282, Smoothed Validation Loss: 0.0000
Epoch [36/650], Train Loss: 0.0000, Train L1 Loss: 0.0284
Epoch [36/650], Validation Loss: 0.0000, Validation L1: 0.0283, Smoothed Validation Loss: 0.0000
Epoch [37/650], Train Loss: 0.0000, Train L1 Loss: 0.0283
Epoch [37/650], Validation Loss: 0.0000, Validation L1: 0.0283, Smoothed Validation Loss: 0.0000
Epoch [38/650], Train Loss: 0.0000, Train L1 Loss: 0.0282
Epoch [38/650], Validation Loss: 0.0000, Validation L1: 0.0284, Smoothed Validation Loss: 0.0000
Epoch [39/650], Train Loss: 0.0000, Train L1 Loss: 0.0281
Epoch [39/650], Validation Loss: 0.0000, Validation L1: 0.0285, Smoothed Validation Loss: 0.0000
Epoch [40/650], Train Loss: 0.0000, Train L1 Loss: 0.0280
Epoch [40/650], Validation Loss: 0.0000, Validation L1: 0.0285, Smoothed Validation Loss: 0.0000
Epoch [41/650], Train Loss: 0.0000, Train L1 Loss: 0.0279
Epoch [41/650], Validation Loss: 0.0000, Validation L1: 0.0285, Smoothed Validation Loss: 0.0000
Epoch [42/650], Train Loss: 0.0000, Train L1 Loss: 0.0278
Epoch [42/650], Validation Loss: 0.0000, Validation L1: 0.0285, Smoothed Validation Loss: 0.0000
Epoch [43/650], Train Loss: 0.0000, Train L1 Loss: 0.0278
Epoch [43/650], Validation Loss: 0.0000, Validation L1: 0.0284, Smoothed Validation Loss: 0.0000
Epoch [44/650], Train Loss: 0.0000, Train L1 Loss: 0.0277
Epoch [44/650], Validation Loss: 0.0000, Validation L1: 0.0284, Smoothed Validation Loss: 0.0000
Epoch [45/650], Train Loss: 0.0000, Train L1 Loss: 0.0276
Epoch [45/650], Validation Loss: 0.0000, Validation L1: 0.0284, Smoothed Validation Loss: 0.0000
Epoch [46/650], Train Loss: 0.0000, Train L1 Loss: 0.0275
Epoch [46/650], Validation Loss: 0.0000, Validation L1: 0.0283, Smoothed Validation Loss: 0.0000
Epoch [47/650], Train Loss: 0.0000, Train L1 Loss: 0.0274
Epoch [47/650], Validation Loss: 0.0000, Validation L1: 0.0282, Smoothed Validation Loss: 0.0000
Epoch [48/650], Train Loss: 0.0000, Train L1 Loss: 0.0273
Epoch [48/650], Validation Loss: 0.0000, Validation L1: 0.0282, Smoothed Validation Loss: 0.0000
Epoch [49/650], Train Loss: 0.0000, Train L1 Loss: 0.0273
Epoch [49/650], Validation Loss: 0.0000, Validation L1: 0.0281, Smoothed Validation Loss: 0.0000
Epoch [50/650], Train Loss: 0.0000, Train L1 Loss: 0.0272
Epoch [50/650], Validation Loss: 0.0000, Validation L1: 0.0281, Smoothed Validation Loss: 0.0000
Epoch [51/650], Train Loss: 0.0000, Train L1 Loss: 0.0271
Epoch [51/650], Validation Loss: 0.0000, Validation L1: 0.0280, Smoothed Validation Loss: 0.0000
Epoch [52/650], Train Loss: 0.0000, Train L1 Loss: 0.0271
Epoch [52/650], Validation Loss: 0.0000, Validation L1: 0.0280, Smoothed Validation Loss: 0.0000
Epoch [53/650], Train Loss: 0.0000, Train L1 Loss: 0.0270
Epoch [53/650], Validation Loss: 0.0000, Validation L1: 0.0279, Smoothed Validation Loss: 0.0000
Epoch [54/650], Train Loss: 0.0000, Train L1 Loss: 0.0269
Epoch [54/650], Validation Loss: 0.0000, Validation L1: 0.0279, Smoothed Validation Loss: 0.0000
Epoch [55/650], Train Loss: 0.0000, Train L1 Loss: 0.0269
Epoch [55/650], Validation Loss: 0.0000, Validation L1: 0.0278, Smoothed Validation Loss: 0.0000
Epoch [56/650], Train Loss: 0.0000, Train L1 Loss: 0.0268
Epoch [56/650], Validation Loss: 0.0000, Validation L1: 0.0277, Smoothed Validation Loss: 0.0000
Epoch [57/650], Train Loss: 0.0000, Train L1 Loss: 0.0267
Epoch [57/650], Validation Loss: 0.0000, Validation L1: 0.0275, Smoothed Validation Loss: 0.0000
Epoch [58/650], Train Loss: 0.0000, Train L1 Loss: 0.0267
Epoch [58/650], Validation Loss: 0.0000, Validation L1: 0.0274, Smoothed Validation Loss: 0.0000
Epoch [59/650], Train Loss: 0.0000, Train L1 Loss: 0.0266
Epoch [59/650], Validation Loss: 0.0000, Validation L1: 0.0273, Smoothed Validation Loss: 0.0000
Epoch [60/650], Train Loss: 0.0000, Train L1 Loss: 0.0266
Epoch [60/650], Validation Loss: 0.0000, Validation L1: 0.0271, Smoothed Validation Loss: 0.0000
Epoch [61/650], Train Loss: 0.0000, Train L1 Loss: 0.0265
Epoch [61/650], Validation Loss: 0.0000, Validation L1: 0.0270, Smoothed Validation Loss: 0.0000
Epoch [62/650], Train Loss: 0.0000, Train L1 Loss: 0.0264
Epoch [62/650], Validation Loss: 0.0000, Validation L1: 0.0269, Smoothed Validation Loss: 0.0000
Epoch [63/650], Train Loss: 0.0000, Train L1 Loss: 0.0264
Epoch [63/650], Validation Loss: 0.0000, Validation L1: 0.0267, Smoothed Validation Loss: 0.0000
Epoch [64/650], Train Loss: 0.0000, Train L1 Loss: 0.0263
Epoch [64/650], Validation Loss: 0.0000, Validation L1: 0.0266, Smoothed Validation Loss: 0.0000
Epoch [65/650], Train Loss: 0.0000, Train L1 Loss: 0.0263
Epoch [65/650], Validation Loss: 0.0000, Validation L1: 0.0266, Smoothed Validation Loss: 0.0000
Epoch [66/650], Train Loss: 0.0000, Train L1 Loss: 0.0262
Epoch [66/650], Validation Loss: 0.0000, Validation L1: 0.0265, Smoothed Validation Loss: 0.0000
Epoch [67/650], Train Loss: 0.0000, Train L1 Loss: 0.0262
Epoch [67/650], Validation Loss: 0.0000, Validation L1: 0.0264, Smoothed Validation Loss: 0.0000
Epoch [68/650], Train Loss: 0.0000, Train L1 Loss: 0.0261
Epoch [68/650], Validation Loss: 0.0000, Validation L1: 0.0264, Smoothed Validation Loss: 0.0000
Epoch [69/650], Train Loss: 0.0000, Train L1 Loss: 0.0261
Epoch [69/650], Validation Loss: 0.0000, Validation L1: 0.0263, Smoothed Validation Loss: 0.0000
Epoch [70/650], Train Loss: 0.0000, Train L1 Loss: 0.0260
Epoch [70/650], Validation Loss: 0.0000, Validation L1: 0.0262, Smoothed Validation Loss: 0.0000
Epoch [71/650], Train Loss: 0.0000, Train L1 Loss: 0.0260
Epoch [71/650], Validation Loss: 0.0000, Validation L1: 0.0262, Smoothed Validation Loss: 0.0000
Epoch [72/650], Train Loss: 0.0000, Train L1 Loss: 0.0259
Epoch [72/650], Validation Loss: 0.0000, Validation L1: 0.0261, Smoothed Validation Loss: 0.0000
Epoch [73/650], Train Loss: 0.0000, Train L1 Loss: 0.0259
Epoch [73/650], Validation Loss: 0.0000, Validation L1: 0.0261, Smoothed Validation Loss: 0.0000
Epoch [74/650], Train Loss: 0.0000, Train L1 Loss: 0.0258
Epoch [74/650], Validation Loss: 0.0000, Validation L1: 0.0260, Smoothed Validation Loss: 0.0000
Epoch [75/650], Train Loss: 0.0000, Train L1 Loss: 0.0258
Epoch [75/650], Validation Loss: 0.0000, Validation L1: 0.0260, Smoothed Validation Loss: 0.0000
Epoch [76/650], Train Loss: 0.0000, Train L1 Loss: 0.0258
Epoch [76/650], Validation Loss: 0.0000, Validation L1: 0.0259, Smoothed Validation Loss: 0.0000
Epoch [77/650], Train Loss: 0.0000, Train L1 Loss: 0.0257
Epoch [77/650], Validation Loss: 0.0000, Validation L1: 0.0259, Smoothed Validation Loss: 0.0000
Epoch [78/650], Train Loss: 0.0000, Train L1 Loss: 0.0257
Epoch [78/650], Validation Loss: 0.0000, Validation L1: 0.0258, Smoothed Validation Loss: 0.0000
Epoch [79/650], Train Loss: 0.0000, Train L1 Loss: 0.0256
Epoch [79/650], Validation Loss: 0.0000, Validation L1: 0.0258, Smoothed Validation Loss: 0.0000
Epoch [80/650], Train Loss: 0.0000, Train L1 Loss: 0.0256
Epoch [80/650], Validation Loss: 0.0000, Validation L1: 0.0258, Smoothed Validation Loss: 0.0000
Epoch [81/650], Train Loss: 0.0000, Train L1 Loss: 0.0255
Epoch [81/650], Validation Loss: 0.0000, Validation L1: 0.0257, Smoothed Validation Loss: 0.0000
Epoch [82/650], Train Loss: 0.0000, Train L1 Loss: 0.0255
Epoch [82/650], Validation Loss: 0.0000, Validation L1: 0.0257, Smoothed Validation Loss: 0.0000
Epoch [83/650], Train Loss: 0.0000, Train L1 Loss: 0.0255
Epoch [83/650], Validation Loss: 0.0000, Validation L1: 0.0256, Smoothed Validation Loss: 0.0000
Epoch [84/650], Train Loss: 0.0000, Train L1 Loss: 0.0254
Epoch [84/650], Validation Loss: 0.0000, Validation L1: 0.0256, Smoothed Validation Loss: 0.0000
Epoch [85/650], Train Loss: 0.0000, Train L1 Loss: 0.0254
Epoch [85/650], Validation Loss: 0.0000, Validation L1: 0.0256, Smoothed Validation Loss: 0.0000
Epoch [86/650], Train Loss: 0.0000, Train L1 Loss: 0.0254
Epoch [86/650], Validation Loss: 0.0000, Validation L1: 0.0255, Smoothed Validation Loss: 0.0000
Epoch [87/650], Train Loss: 0.0000, Train L1 Loss: 0.0253
Epoch [87/650], Validation Loss: 0.0000, Validation L1: 0.0255, Smoothed Validation Loss: 0.0000
Epoch [88/650], Train Loss: 0.0000, Train L1 Loss: 0.0253
Epoch [88/650], Validation Loss: 0.0000, Validation L1: 0.0255, Smoothed Validation Loss: 0.0000
Epoch [89/650], Train Loss: 0.0000, Train L1 Loss: 0.0252
Epoch [89/650], Validation Loss: 0.0000, Validation L1: 0.0255, Smoothed Validation Loss: 0.0000
Epoch [90/650], Train Loss: 0.0000, Train L1 Loss: 0.0252
Epoch [90/650], Validation Loss: 0.0000, Validation L1: 0.0254, Smoothed Validation Loss: 0.0000
Epoch [91/650], Train Loss: 0.0000, Train L1 Loss: 0.0252
Epoch [91/650], Validation Loss: 0.0000, Validation L1: 0.0254, Smoothed Validation Loss: 0.0000
Epoch [92/650], Train Loss: 0.0000, Train L1 Loss: 0.0251
Epoch [92/650], Validation Loss: 0.0000, Validation L1: 0.0254, Smoothed Validation Loss: 0.0000
Epoch [93/650], Train Loss: 0.0000, Train L1 Loss: 0.0251
Epoch [93/650], Validation Loss: 0.0000, Validation L1: 0.0254, Smoothed Validation Loss: 0.0000
Epoch [94/650], Train Loss: 0.0000, Train L1 Loss: 0.0251
Epoch [94/650], Validation Loss: 0.0000, Validation L1: 0.0253, Smoothed Validation Loss: 0.0000
Epoch [95/650], Train Loss: 0.0000, Train L1 Loss: 0.0250
Epoch [95/650], Validation Loss: 0.0000, Validation L1: 0.0253, Smoothed Validation Loss: 0.0000
Epoch [96/650], Train Loss: 0.0000, Train L1 Loss: 0.0250
Epoch [96/650], Validation Loss: 0.0000, Validation L1: 0.0253, Smoothed Validation Loss: 0.0000
Epoch [97/650], Train Loss: 0.0000, Train L1 Loss: 0.0250
Epoch [97/650], Validation Loss: 0.0000, Validation L1: 0.0253, Smoothed Validation Loss: 0.0000
Epoch [98/650], Train Loss: 0.0000, Train L1 Loss: 0.0249
Epoch [98/650], Validation Loss: 0.0000, Validation L1: 0.0252, Smoothed Validation Loss: 0.0000
Epoch [99/650], Train Loss: 0.0000, Train L1 Loss: 0.0249
Epoch [99/650], Validation Loss: 0.0000, Validation L1: 0.0252, Smoothed Validation Loss: 0.0000
Epoch [100/650], Train Loss: 0.0000, Train L1 Loss: 0.0249
Epoch [100/650], Validation Loss: 0.0000, Validation L1: 0.0252, Smoothed Validation Loss: 0.0000
Epoch [101/650], Train Loss: 0.0000, Train L1 Loss: 0.0248
Epoch [101/650], Validation Loss: 0.0000, Validation L1: 0.0252, Smoothed Validation Loss: 0.0000
Epoch [102/650], Train Loss: 0.0000, Train L1 Loss: 0.0248
Epoch [102/650], Validation Loss: 0.0000, Validation L1: 0.0252, Smoothed Validation Loss: 0.0000
Epoch [103/650], Train Loss: 0.0000, Train L1 Loss: 0.0248
Epoch [103/650], Validation Loss: 0.0000, Validation L1: 0.0251, Smoothed Validation Loss: 0.0000
Epoch [104/650], Train Loss: 0.0000, Train L1 Loss: 0.0248
Epoch [104/650], Validation Loss: 0.0000, Validation L1: 0.0251, Smoothed Validation Loss: 0.0000
Epoch [105/650], Train Loss: 0.0000, Train L1 Loss: 0.0247
Epoch [105/650], Validation Loss: 0.0000, Validation L1: 0.0251, Smoothed Validation Loss: 0.0000
Epoch [106/650], Train Loss: 0.0000, Train L1 Loss: 0.0247
Epoch [106/650], Validation Loss: 0.0000, Validation L1: 0.0251, Smoothed Validation Loss: 0.0000
Epoch [107/650], Train Loss: 0.0000, Train L1 Loss: 0.0247
Epoch [107/650], Validation Loss: 0.0000, Validation L1: 0.0251, Smoothed Validation Loss: 0.0000
Epoch [108/650], Train Loss: 0.0000, Train L1 Loss: 0.0246
Epoch [108/650], Validation Loss: 0.0000, Validation L1: 0.0250, Smoothed Validation Loss: 0.0000
Epoch [109/650], Train Loss: 0.0000, Train L1 Loss: 0.0246
Epoch [109/650], Validation Loss: 0.0000, Validation L1: 0.0250, Smoothed Validation Loss: 0.0000
Epoch [110/650], Train Loss: 0.0000, Train L1 Loss: 0.0246
Epoch [110/650], Validation Loss: 0.0000, Validation L1: 0.0250, Smoothed Validation Loss: 0.0000
Epoch [111/650], Train Loss: 0.0000, Train L1 Loss: 0.0245
Epoch [111/650], Validation Loss: 0.0000, Validation L1: 0.0250, Smoothed Validation Loss: 0.0000
Epoch [112/650], Train Loss: 0.0000, Train L1 Loss: 0.0245
Epoch [112/650], Validation Loss: 0.0000, Validation L1: 0.0249, Smoothed Validation Loss: 0.0000
Epoch [113/650], Train Loss: 0.0000, Train L1 Loss: 0.0245
Epoch [113/650], Validation Loss: 0.0000, Validation L1: 0.0249, Smoothed Validation Loss: 0.0000
Epoch [114/650], Train Loss: 0.0000, Train L1 Loss: 0.0244
Epoch [114/650], Validation Loss: 0.0000, Validation L1: 0.0249, Smoothed Validation Loss: 0.0000
Epoch [115/650], Train Loss: 0.0000, Train L1 Loss: 0.0244
Epoch [115/650], Validation Loss: 0.0000, Validation L1: 0.0249, Smoothed Validation Loss: 0.0000
Epoch [116/650], Train Loss: 0.0000, Train L1 Loss: 0.0244
Epoch [116/650], Validation Loss: 0.0000, Validation L1: 0.0248, Smoothed Validation Loss: 0.0000
Epoch [117/650], Train Loss: 0.0000, Train L1 Loss: 0.0243
Epoch [117/650], Validation Loss: 0.0000, Validation L1: 0.0248, Smoothed Validation Loss: 0.0000
Epoch [118/650], Train Loss: 0.0000, Train L1 Loss: 0.0243
Epoch [118/650], Validation Loss: 0.0000, Validation L1: 0.0248, Smoothed Validation Loss: 0.0000
Epoch [119/650], Train Loss: 0.0000, Train L1 Loss: 0.0243
Epoch [119/650], Validation Loss: 0.0000, Validation L1: 0.0248, Smoothed Validation Loss: 0.0000
Epoch [120/650], Train Loss: 0.0000, Train L1 Loss: 0.0243
Epoch [120/650], Validation Loss: 0.0000, Validation L1: 0.0248, Smoothed Validation Loss: 0.0000
Epoch [121/650], Train Loss: 0.0000, Train L1 Loss: 0.0242
Epoch [121/650], Validation Loss: 0.0000, Validation L1: 0.0247, Smoothed Validation Loss: 0.0000
Epoch [122/650], Train Loss: 0.0000, Train L1 Loss: 0.0242
Epoch [122/650], Validation Loss: 0.0000, Validation L1: 0.0247, Smoothed Validation Loss: 0.0000
Epoch [123/650], Train Loss: 0.0000, Train L1 Loss: 0.0242
Epoch [123/650], Validation Loss: 0.0000, Validation L1: 0.0247, Smoothed Validation Loss: 0.0000
Epoch [124/650], Train Loss: 0.0000, Train L1 Loss: 0.0241
Epoch [124/650], Validation Loss: 0.0000, Validation L1: 0.0247, Smoothed Validation Loss: 0.0000
Epoch [125/650], Train Loss: 0.0000, Train L1 Loss: 0.0241
Epoch [125/650], Validation Loss: 0.0000, Validation L1: 0.0246, Smoothed Validation Loss: 0.0000
Epoch [126/650], Train Loss: 0.0000, Train L1 Loss: 0.0241
Epoch [126/650], Validation Loss: 0.0000, Validation L1: 0.0246, Smoothed Validation Loss: 0.0000
Epoch [127/650], Train Loss: 0.0000, Train L1 Loss: 0.0241
Epoch [127/650], Validation Loss: 0.0000, Validation L1: 0.0246, Smoothed Validation Loss: 0.0000
Epoch [128/650], Train Loss: 0.0000, Train L1 Loss: 0.0240
Epoch [128/650], Validation Loss: 0.0000, Validation L1: 0.0246, Smoothed Validation Loss: 0.0000
Epoch [129/650], Train Loss: 0.0000, Train L1 Loss: 0.0240
Epoch [129/650], Validation Loss: 0.0000, Validation L1: 0.0246, Smoothed Validation Loss: 0.0000
Epoch [130/650], Train Loss: 0.0000, Train L1 Loss: 0.0240
Epoch [130/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [131/650], Train Loss: 0.0000, Train L1 Loss: 0.0240
Epoch [131/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [132/650], Train Loss: 0.0000, Train L1 Loss: 0.0239
Epoch [132/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [133/650], Train Loss: 0.0000, Train L1 Loss: 0.0239
Epoch [133/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [134/650], Train Loss: 0.0000, Train L1 Loss: 0.0239
Epoch [134/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [135/650], Train Loss: 0.0000, Train L1 Loss: 0.0239
Epoch [135/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [136/650], Train Loss: 0.0000, Train L1 Loss: 0.0238
Epoch [136/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [137/650], Train Loss: 0.0000, Train L1 Loss: 0.0238
Epoch [137/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [138/650], Train Loss: 0.0000, Train L1 Loss: 0.0238
Epoch [138/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [139/650], Train Loss: 0.0000, Train L1 Loss: 0.0238
Epoch [139/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [140/650], Train Loss: 0.0000, Train L1 Loss: 0.0237
Epoch [140/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [141/650], Train Loss: 0.0000, Train L1 Loss: 0.0237
Epoch [141/650], Validation Loss: 0.0000, Validation L1: 0.0245, Smoothed Validation Loss: 0.0000
Epoch [142/650], Train Loss: 0.0000, Train L1 Loss: 0.0237
Epoch [142/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [143/650], Train Loss: 0.0000, Train L1 Loss: 0.0237
Epoch [143/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [144/650], Train Loss: 0.0000, Train L1 Loss: 0.0236
Epoch [144/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [145/650], Train Loss: 0.0000, Train L1 Loss: 0.0236
Epoch [145/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [146/650], Train Loss: 0.0000, Train L1 Loss: 0.0236
Epoch [146/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [147/650], Train Loss: 0.0000, Train L1 Loss: 0.0236
Epoch [147/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [148/650], Train Loss: 0.0000, Train L1 Loss: 0.0235
Epoch [148/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [149/650], Train Loss: 0.0000, Train L1 Loss: 0.0235
Epoch [149/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [150/650], Train Loss: 0.0000, Train L1 Loss: 0.0235
Epoch [150/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [151/650], Train Loss: 0.0000, Train L1 Loss: 0.0235
Epoch [151/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [152/650], Train Loss: 0.0000, Train L1 Loss: 0.0235
Epoch [152/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [153/650], Train Loss: 0.0000, Train L1 Loss: 0.0234
Epoch [153/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [154/650], Train Loss: 0.0000, Train L1 Loss: 0.0234
Epoch [154/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [155/650], Train Loss: 0.0000, Train L1 Loss: 0.0234
Epoch [155/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [156/650], Train Loss: 0.0000, Train L1 Loss: 0.0234
Epoch [156/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [157/650], Train Loss: 0.0000, Train L1 Loss: 0.0234
Epoch [157/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [158/650], Train Loss: 0.0000, Train L1 Loss: 0.0233
Epoch [158/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [159/650], Train Loss: 0.0000, Train L1 Loss: 0.0233
Epoch [159/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [160/650], Train Loss: 0.0000, Train L1 Loss: 0.0233
Epoch [160/650], Validation Loss: 0.0000, Validation L1: 0.0244, Smoothed Validation Loss: 0.0000
Epoch [161/650], Train Loss: 0.0000, Train L1 Loss: 0.0233
Epoch [161/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [162/650], Train Loss: 0.0000, Train L1 Loss: 0.0233
Epoch [162/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [163/650], Train Loss: 0.0000, Train L1 Loss: 0.0232
Epoch [163/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [164/650], Train Loss: 0.0000, Train L1 Loss: 0.0232
Epoch [164/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [165/650], Train Loss: 0.0000, Train L1 Loss: 0.0232
Epoch [165/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [166/650], Train Loss: 0.0000, Train L1 Loss: 0.0232
Epoch [166/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [167/650], Train Loss: 0.0000, Train L1 Loss: 0.0232
Epoch [167/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [168/650], Train Loss: 0.0000, Train L1 Loss: 0.0231
Epoch [168/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch [169/650], Train Loss: 0.0000, Train L1 Loss: 0.0231
Epoch [169/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [170/650], Train Loss: 0.0000, Train L1 Loss: 0.0231
Epoch [170/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [171/650], Train Loss: 0.0000, Train L1 Loss: 0.0231
Epoch [171/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [172/650], Train Loss: 0.0000, Train L1 Loss: 0.0231
Epoch [172/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [173/650], Train Loss: 0.0000, Train L1 Loss: 0.0230
Epoch [173/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [174/650], Train Loss: 0.0000, Train L1 Loss: 0.0230
Epoch [174/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [175/650], Train Loss: 0.0000, Train L1 Loss: 0.0230
Epoch [175/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [176/650], Train Loss: 0.0000, Train L1 Loss: 0.0230
Epoch [176/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [177/650], Train Loss: 0.0000, Train L1 Loss: 0.0230
Epoch [177/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [178/650], Train Loss: 0.0000, Train L1 Loss: 0.0230
Epoch [178/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [179/650], Train Loss: 0.0000, Train L1 Loss: 0.0229
Epoch [179/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [180/650], Train Loss: 0.0000, Train L1 Loss: 0.0229
Epoch [180/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [181/650], Train Loss: 0.0000, Train L1 Loss: 0.0229
Epoch [181/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [182/650], Train Loss: 0.0000, Train L1 Loss: 0.0229
Epoch [182/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [183/650], Train Loss: 0.0000, Train L1 Loss: 0.0229
Epoch [183/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [184/650], Train Loss: 0.0000, Train L1 Loss: 0.0228
Epoch [184/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [185/650], Train Loss: 0.0000, Train L1 Loss: 0.0228
Epoch [185/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [186/650], Train Loss: 0.0000, Train L1 Loss: 0.0228
Epoch [186/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [187/650], Train Loss: 0.0000, Train L1 Loss: 0.0228
Epoch [187/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [188/650], Train Loss: 0.0000, Train L1 Loss: 0.0228
Epoch [188/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [189/650], Train Loss: 0.0000, Train L1 Loss: 0.0228
Epoch [189/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [190/650], Train Loss: 0.0000, Train L1 Loss: 0.0227
Epoch [190/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [191/650], Train Loss: 0.0000, Train L1 Loss: 0.0227
Epoch [191/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [192/650], Train Loss: 0.0000, Train L1 Loss: 0.0227
Epoch [192/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [193/650], Train Loss: 0.0000, Train L1 Loss: 0.0227
Epoch [193/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [194/650], Train Loss: 0.0000, Train L1 Loss: 0.0227
Epoch [194/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [195/650], Train Loss: 0.0000, Train L1 Loss: 0.0227
Epoch [195/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [196/650], Train Loss: 0.0000, Train L1 Loss: 0.0226
Epoch [196/650], Validation Loss: 0.0000, Validation L1: 0.0241, Smoothed Validation Loss: 0.0000
Epoch [197/650], Train Loss: 0.0000, Train L1 Loss: 0.0226
Epoch [197/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [198/650], Train Loss: 0.0000, Train L1 Loss: 0.0226
Epoch [198/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [199/650], Train Loss: 0.0000, Train L1 Loss: 0.0226
Epoch [199/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [200/650], Train Loss: 0.0000, Train L1 Loss: 0.0226
Epoch [200/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [201/650], Train Loss: 0.0000, Train L1 Loss: 0.0226
Epoch [201/650], Validation Loss: 0.0000, Validation L1: 0.0242, Smoothed Validation Loss: 0.0000
Epoch [202/650], Train Loss: 0.0000, Train L1 Loss: 0.0226
Epoch [202/650], Validation Loss: 0.0000, Validation L1: 0.0243, Smoothed Validation Loss: 0.0000
Epoch 00202: reducing learning rate of group 0 to 6.2500e-05.
Epoch [203/650], Train Loss: 0.0000, Train L1 Loss: 0.0221
Epoch [203/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [204/650], Train Loss: 0.0000, Train L1 Loss: 0.0221
Epoch [204/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [205/650], Train Loss: 0.0000, Train L1 Loss: 0.0220
Epoch [205/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [206/650], Train Loss: 0.0000, Train L1 Loss: 0.0220
Epoch [206/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [207/650], Train Loss: 0.0000, Train L1 Loss: 0.0220
Epoch [207/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [208/650], Train Loss: 0.0000, Train L1 Loss: 0.0220
Epoch [208/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [209/650], Train Loss: 0.0000, Train L1 Loss: 0.0219
Epoch [209/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [210/650], Train Loss: 0.0000, Train L1 Loss: 0.0219
Epoch [210/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [211/650], Train Loss: 0.0000, Train L1 Loss: 0.0219
Epoch [211/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [212/650], Train Loss: 0.0000, Train L1 Loss: 0.0219
Epoch [212/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [213/650], Train Loss: 0.0000, Train L1 Loss: 0.0219
Epoch [213/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [214/650], Train Loss: 0.0000, Train L1 Loss: 0.0218
Epoch [214/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [215/650], Train Loss: 0.0000, Train L1 Loss: 0.0218
Epoch [215/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [216/650], Train Loss: 0.0000, Train L1 Loss: 0.0218
Epoch [216/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [217/650], Train Loss: 0.0000, Train L1 Loss: 0.0218
Epoch [217/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [218/650], Train Loss: 0.0000, Train L1 Loss: 0.0218
Epoch [218/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [219/650], Train Loss: 0.0000, Train L1 Loss: 0.0218
Epoch [219/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [220/650], Train Loss: 0.0000, Train L1 Loss: 0.0218
Epoch [220/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [221/650], Train Loss: 0.0000, Train L1 Loss: 0.0217
Epoch [221/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [222/650], Train Loss: 0.0000, Train L1 Loss: 0.0217
Epoch [222/650], Validation Loss: 0.0000, Validation L1: 0.0239, Smoothed Validation Loss: 0.0000
Epoch [223/650], Train Loss: 0.0000, Train L1 Loss: 0.0217
Epoch [223/650], Validation Loss: 0.0000, Validation L1: 0.0240, Smoothed Validation Loss: 0.0000
Epoch [224/650], Train Loss: 0.0000, Train L1 Loss: 0.0217
Epoch [224/650], Validation Loss: 0.0000, Validation L1: 0.0240, Smoothed Validation Loss: 0.0000
Epoch [225/650], Train Loss: 0.0000, Train L1 Loss: 0.0217
Epoch [225/650], Validation Loss: 0.0000, Validation L1: 0.0240, Smoothed Validation Loss: 0.0000
Epoch [226/650], Train Loss: 0.0000, Train L1 Loss: 0.0217
Epoch [226/650], Validation Loss: 0.0000, Validation L1: 0.0240, Smoothed Validation Loss: 0.0000
Epoch [227/650], Train Loss: 0.0000, Train L1 Loss: 0.0217
Epoch [227/650], Validation Loss: 0.0000, Validation L1: 0.0240, Smoothed Validation Loss: 0.0000
Epoch 00227: reducing learning rate of group 0 to 3.1250e-05.
Epoch [228/650], Train Loss: 0.0000, Train L1 Loss: 0.0212
Epoch [228/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [229/650], Train Loss: 0.0000, Train L1 Loss: 0.0212
Epoch [229/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [230/650], Train Loss: 0.0000, Train L1 Loss: 0.0212
Epoch [230/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [231/650], Train Loss: 0.0000, Train L1 Loss: 0.0212
Epoch [231/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [232/650], Train Loss: 0.0000, Train L1 Loss: 0.0212
Epoch [232/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [233/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [233/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [234/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [234/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [235/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [235/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [236/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [236/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [237/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [237/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [238/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [238/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [239/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [239/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [240/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [240/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [241/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [241/650], Validation Loss: 0.0000, Validation L1: 0.0238, Smoothed Validation Loss: 0.0000
Epoch [242/650], Train Loss: 0.0000, Train L1 Loss: 0.0211
Epoch [242/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [243/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [243/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [244/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [244/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [245/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [245/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [246/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [246/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [247/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [247/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [248/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [248/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [249/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [249/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [250/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [250/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [251/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [251/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [252/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [252/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [253/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [253/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [254/650], Train Loss: 0.0000, Train L1 Loss: 0.0210
Epoch [254/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [255/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [255/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [256/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [256/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [257/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [257/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [258/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [258/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [259/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [259/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [260/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [260/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [261/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [261/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [262/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [262/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [263/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [263/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [264/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [264/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [265/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [265/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [266/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [266/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [267/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [267/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [268/650], Train Loss: 0.0000, Train L1 Loss: 0.0209
Epoch [268/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [269/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [269/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [270/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [270/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [271/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [271/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [272/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [272/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [273/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [273/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [274/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [274/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [275/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [275/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [276/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [276/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [277/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [277/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [278/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [278/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [279/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [279/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [280/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [280/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [281/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [281/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [282/650], Train Loss: 0.0000, Train L1 Loss: 0.0208
Epoch [282/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [283/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [283/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [284/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [284/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [285/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [285/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [286/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [286/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [287/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [287/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [288/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [288/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [289/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [289/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch [290/650], Train Loss: 0.0000, Train L1 Loss: 0.0207
Epoch [290/650], Validation Loss: 0.0000, Validation L1: 0.0237, Smoothed Validation Loss: 0.0000
Epoch 00290: reducing learning rate of group 0 to 1.5625e-05.
Epoch [291/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [291/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [292/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [292/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [293/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [293/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [294/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [294/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [295/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [295/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [296/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [296/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [297/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [297/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [298/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [298/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [299/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [299/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [300/650], Train Loss: 0.0000, Train L1 Loss: 0.0205
Epoch [300/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [301/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [301/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [302/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [302/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [303/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [303/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [304/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [304/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [305/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [305/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [306/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [306/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [307/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [307/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [308/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [308/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [309/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [309/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [310/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [310/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [311/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [311/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [312/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [312/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [313/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [313/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [314/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [314/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [315/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [315/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [316/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [316/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [317/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [317/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [318/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [318/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [319/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [319/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [320/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [320/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [321/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [321/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [322/650], Train Loss: 0.0000, Train L1 Loss: 0.0204
Epoch [322/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [323/650], Train Loss: 0.0000, Train L1 Loss: 0.0203
Epoch [323/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch [324/650], Train Loss: 0.0000, Train L1 Loss: 0.0203
Epoch [324/650], Validation Loss: 0.0000, Validation L1: 0.0233, Smoothed Validation Loss: 0.0000
Epoch 00324: reducing learning rate of group 0 to 7.8125e-06.
Epoch [325/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [325/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [326/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [326/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [327/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [327/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [328/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [328/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [329/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [329/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [330/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [330/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [331/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [331/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [332/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [332/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [333/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [333/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [334/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [334/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [335/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [335/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [336/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [336/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [337/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [337/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [338/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [338/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [339/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [339/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [340/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [340/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [341/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [341/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [342/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [342/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [343/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [343/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [344/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [344/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [345/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [345/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [346/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [346/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [347/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [347/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [348/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [348/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [349/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [349/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [350/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [350/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [351/650], Train Loss: 0.0000, Train L1 Loss: 0.0202
Epoch [351/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [352/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [352/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [353/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [353/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [354/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [354/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch [355/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [355/650], Validation Loss: 0.0000, Validation L1: 0.0232, Smoothed Validation Loss: 0.0000
Epoch 00355: reducing learning rate of group 0 to 3.9063e-06.
Epoch [356/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [356/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [357/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [357/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [358/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [358/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [359/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [359/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [360/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [360/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [361/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [361/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [362/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [362/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [363/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [363/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [364/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [364/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [365/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [365/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [366/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [366/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [367/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [367/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [368/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [368/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [369/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [369/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [370/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [370/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [371/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [371/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [372/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [372/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [373/650], Train Loss: 0.0000, Train L1 Loss: 0.0201
Epoch [373/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [374/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [374/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [375/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [375/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [376/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [376/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [377/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [377/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [378/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [378/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [379/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [379/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [380/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [380/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [381/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [381/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [382/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [382/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [383/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [383/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [384/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [384/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [385/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [385/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [386/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [386/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [387/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [387/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [388/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [388/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [389/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [389/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [390/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [390/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [391/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [391/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [392/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [392/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [393/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [393/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch 00393: reducing learning rate of group 0 to 1.9531e-06.
Epoch [394/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [394/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [395/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [395/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [396/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [396/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [397/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [397/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [398/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [398/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [399/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [399/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [400/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [400/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [401/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [401/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [402/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [402/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [403/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [403/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [404/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [404/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [405/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [405/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [406/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [406/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [407/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [407/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [408/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [408/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [409/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [409/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [410/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [410/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [411/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [411/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [412/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [412/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [413/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [413/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [414/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [414/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [415/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [415/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [416/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [416/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [417/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [417/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [418/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [418/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [419/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [419/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [420/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [420/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [421/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [421/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch [422/650], Train Loss: 0.0000, Train L1 Loss: 0.0200
Epoch [422/650], Validation Loss: 0.0000, Validation L1: 0.0231, Smoothed Validation Loss: 0.0000
Epoch 00422: reducing learning rate of group 0 to 9.7656e-07.
Epoch [423/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [423/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [424/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [424/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [425/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [425/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [426/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [426/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [427/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [427/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [428/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [428/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [429/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [429/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [430/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [430/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [431/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [431/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [432/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [432/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [433/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [433/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [434/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [434/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [435/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [435/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [436/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [436/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [437/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [437/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [438/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [438/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [439/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [439/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [440/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [440/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [441/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [441/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [442/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [442/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [443/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [443/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [444/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [444/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [445/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [445/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [446/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [446/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [447/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [447/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch 00447: reducing learning rate of group 0 to 4.8828e-07.
Epoch [448/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [448/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [449/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [449/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [450/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [450/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [451/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [451/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [452/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [452/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [453/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [453/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [454/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [454/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [455/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [455/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [456/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [456/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [457/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [457/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [458/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [458/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [459/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [459/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [460/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [460/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [461/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [461/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [462/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [462/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [463/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [463/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [464/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [464/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [465/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [465/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch 00465: reducing learning rate of group 0 to 2.4414e-07.
Epoch [466/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [466/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [467/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [467/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [468/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [468/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [469/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [469/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [470/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [470/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [471/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [471/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [472/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [472/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch 00472: reducing learning rate of group 0 to 1.2207e-07.
Epoch [473/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [473/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [474/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [474/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [475/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [475/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [476/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [476/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [477/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [477/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [478/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [478/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch 00478: reducing learning rate of group 0 to 6.1035e-08.
Epoch [479/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [479/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [480/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [480/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [481/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [481/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [482/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [482/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [483/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [483/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [484/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [484/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch 00484: reducing learning rate of group 0 to 3.0518e-08.
Epoch [485/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [485/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [486/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [486/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [487/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [487/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [488/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [488/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [489/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [489/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [490/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [490/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [491/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [491/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [492/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [492/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch 00492: reducing learning rate of group 0 to 1.5259e-08.
Epoch [493/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [493/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [494/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [494/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [495/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [495/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [496/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [496/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [497/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [497/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [498/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [498/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [499/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [499/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [500/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [500/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [501/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [501/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [502/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [502/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [503/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [503/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [504/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [504/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [505/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [505/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [506/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [506/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [507/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [507/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [508/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [508/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [509/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [509/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [510/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [510/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [511/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [511/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [512/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [512/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [513/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [513/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [514/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [514/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [515/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [515/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [516/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [516/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [517/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [517/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [518/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [518/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [519/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [519/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [520/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [520/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [521/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [521/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [522/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [522/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [523/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [523/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [524/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [524/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [525/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [525/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [526/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [526/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [527/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [527/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [528/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [528/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [529/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [529/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [530/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [530/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [531/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [531/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [532/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [532/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [533/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [533/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [534/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [534/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [535/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [535/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [536/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [536/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [537/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [537/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [538/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [538/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [539/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [539/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [540/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [540/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [541/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [541/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [542/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [542/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [543/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [543/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [544/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [544/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [545/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [545/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [546/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [546/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [547/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [547/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [548/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [548/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [549/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [549/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [550/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [550/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [551/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [551/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [552/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [552/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [553/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [553/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [554/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [554/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [555/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [555/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [556/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [556/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [557/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [557/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [558/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [558/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [559/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [559/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [560/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [560/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [561/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [561/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [562/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [562/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [563/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [563/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [564/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [564/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [565/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [565/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [566/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [566/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [567/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [567/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [568/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [568/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [569/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [569/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [570/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [570/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [571/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [571/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [572/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [572/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [573/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [573/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [574/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [574/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [575/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [575/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [576/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [576/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [577/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [577/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [578/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [578/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [579/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [579/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [580/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [580/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [581/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [581/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [582/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [582/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [583/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [583/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [584/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [584/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [585/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [585/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [586/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [586/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [587/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [587/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [588/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [588/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [589/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [589/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [590/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [590/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [591/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [591/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [592/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [592/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [593/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [593/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [594/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [594/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [595/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [595/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [596/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [596/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [597/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [597/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [598/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [598/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [599/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [599/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [600/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [600/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [601/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [601/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [602/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [602/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [603/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [603/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [604/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [604/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [605/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [605/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [606/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [606/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [607/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [607/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [608/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [608/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [609/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [609/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [610/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [610/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [611/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [611/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [612/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [612/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [613/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [613/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [614/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [614/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [615/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [615/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [616/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [616/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [617/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [617/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [618/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [618/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [619/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [619/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [620/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [620/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [621/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [621/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [622/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [622/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [623/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [623/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [624/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [624/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [625/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [625/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [626/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [626/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [627/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [627/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [628/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [628/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [629/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [629/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [630/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [630/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [631/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [631/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [632/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [632/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [633/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [633/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [634/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [634/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [635/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [635/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [636/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [636/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [637/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [637/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [638/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [638/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [639/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [639/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [640/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [640/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [641/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [641/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [642/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [642/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [643/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [643/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [644/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [644/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [645/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [645/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [646/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [646/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [647/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [647/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [648/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [648/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [649/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [649/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
Epoch [650/650], Train Loss: 0.0000, Train L1 Loss: 0.0199
Epoch [650/650], Validation Loss: 0.0000, Validation L1: 0.0230, Smoothed Validation Loss: 0.0000
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19686785: <fixWorkingSetup_6> in cluster <dcc> Done

Job <fixWorkingSetup_6> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Mon Dec  4 14:17:58 2023
Job was executed on host(s) <4*n-62-18-13>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Mon Dec  4 18:09:05 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Mon Dec  4 18:09:05 2023
Terminated at Tue Dec  5 05:17:43 2023
Results reported at Tue Dec  5 05:17:43 2023

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

    CPU time :                                   40450.23 sec.
    Max Memory :                                 1959 MB
    Average Memory :                             1949.19 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63577.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   40122 sec.
    Turnaround time :                            53985 sec.

The output (if any) is above this job summary.

