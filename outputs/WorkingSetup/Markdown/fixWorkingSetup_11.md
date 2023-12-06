
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
| <c>name</c>       | <d>str</d>        | <j>"11fixWorkingSetup-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>650</f>        |
| <c>batch_size</c> | <d>int</d>        | <f>80</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |
| <c>param</c>      | <d>int</d>        | <f>11</f>         |
| <c>path</c>       | <d>str</d>        | <j>"/zhome/59/9/198225/Desktop/Deep_learning_2023/models/"</j> |

# Output

```
wandb: Currently logged in as: mrcogito (deeplearning_painn). Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231205_101858-3vxiy46f
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 11fixWorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/3vxiy46f
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:10,186] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7f9d92f20a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:13,037] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpes8b54uz.py line 218 
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:18,524] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpes8b54uz.py line 117 
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:18,990] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpes8b54uz.py line 90 
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:19,118] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:19,677] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:22,253] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:23,731] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] 
[2023-12-05 10:19:24,718] torch._dynamo.convert_frame: [WARNING] 
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.117 MB uploadedwandb: | 0.117 MB of 0.117 MB uploadedwandb: / 0.117 MB of 0.117 MB uploadedwandb: - 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▄▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▆▅▄▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▅▅▄▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▄▄▂▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▃▃▁▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.0205
wandb:     train l1 loss 0.73393
wandb:        train_loss 0.01209
wandb:       val l1 loss 0.95673
wandb:          val loss 0.0205
wandb: 
wandb: 🚀 View run 11fixWorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/3vxiy46f
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231205_101858-3vxiy46f/logs
Epoch [1/650], Train Loss: 0.0748, Train L1 Loss: 1.6675
Epoch [1/650], Validation Loss: 0.0377, Validation L1: 1.3636, Smoothed Validation Loss: 0.0377
Epoch [2/650], Train Loss: 0.0372, Train L1 Loss: 1.3594
Epoch [2/650], Validation Loss: 0.0331, Validation L1: 1.2757, Smoothed Validation Loss: 0.0373
Epoch [3/650], Train Loss: 0.0332, Train L1 Loss: 1.2810
Epoch [3/650], Validation Loss: 0.0316, Validation L1: 1.2434, Smoothed Validation Loss: 0.0367
Epoch [4/650], Train Loss: 0.0311, Train L1 Loss: 1.2350
Epoch [4/650], Validation Loss: 0.0294, Validation L1: 1.2028, Smoothed Validation Loss: 0.0360
Epoch [5/650], Train Loss: 0.0294, Train L1 Loss: 1.1994
Epoch [5/650], Validation Loss: 0.0276, Validation L1: 1.1594, Smoothed Validation Loss: 0.0351
Epoch [6/650], Train Loss: 0.0280, Train L1 Loss: 1.1679
Epoch [6/650], Validation Loss: 0.0275, Validation L1: 1.1619, Smoothed Validation Loss: 0.0344
Epoch [7/650], Train Loss: 0.0269, Train L1 Loss: 1.1445
Epoch [7/650], Validation Loss: 0.0273, Validation L1: 1.1612, Smoothed Validation Loss: 0.0337
Epoch [8/650], Train Loss: 0.0262, Train L1 Loss: 1.1281
Epoch [8/650], Validation Loss: 0.0271, Validation L1: 1.1552, Smoothed Validation Loss: 0.0330
Epoch [9/650], Train Loss: 0.0255, Train L1 Loss: 1.1121
Epoch [9/650], Validation Loss: 0.0268, Validation L1: 1.1456, Smoothed Validation Loss: 0.0324
Epoch [10/650], Train Loss: 0.0249, Train L1 Loss: 1.0984
Epoch [10/650], Validation Loss: 0.0268, Validation L1: 1.1455, Smoothed Validation Loss: 0.0318
Epoch [11/650], Train Loss: 0.0245, Train L1 Loss: 1.0865
Epoch [11/650], Validation Loss: 0.0254, Validation L1: 1.1116, Smoothed Validation Loss: 0.0312
Epoch [12/650], Train Loss: 0.0240, Train L1 Loss: 1.0763
Epoch [12/650], Validation Loss: 0.0253, Validation L1: 1.1127, Smoothed Validation Loss: 0.0306
Epoch [13/650], Train Loss: 0.0236, Train L1 Loss: 1.0665
Epoch [13/650], Validation Loss: 0.0244, Validation L1: 1.0854, Smoothed Validation Loss: 0.0300
Epoch [14/650], Train Loss: 0.0233, Train L1 Loss: 1.0587
Epoch [14/650], Validation Loss: 0.0242, Validation L1: 1.0795, Smoothed Validation Loss: 0.0294
Epoch [15/650], Train Loss: 0.0230, Train L1 Loss: 1.0505
Epoch [15/650], Validation Loss: 0.0248, Validation L1: 1.0935, Smoothed Validation Loss: 0.0289
Epoch [16/650], Train Loss: 0.0226, Train L1 Loss: 1.0421
Epoch [16/650], Validation Loss: 0.0227, Validation L1: 1.0443, Smoothed Validation Loss: 0.0283
Epoch [17/650], Train Loss: 0.0223, Train L1 Loss: 1.0347
Epoch [17/650], Validation Loss: 0.0232, Validation L1: 1.0570, Smoothed Validation Loss: 0.0278
Epoch [18/650], Train Loss: 0.0221, Train L1 Loss: 1.0291
Epoch [18/650], Validation Loss: 0.0232, Validation L1: 1.0575, Smoothed Validation Loss: 0.0273
Epoch [19/650], Train Loss: 0.0218, Train L1 Loss: 1.0229
Epoch [19/650], Validation Loss: 0.0224, Validation L1: 1.0304, Smoothed Validation Loss: 0.0268
Epoch [20/650], Train Loss: 0.0216, Train L1 Loss: 1.0172
Epoch [20/650], Validation Loss: 0.0221, Validation L1: 1.0314, Smoothed Validation Loss: 0.0264
Epoch [21/650], Train Loss: 0.0215, Train L1 Loss: 1.0124
Epoch [21/650], Validation Loss: 0.0224, Validation L1: 1.0385, Smoothed Validation Loss: 0.0260
Epoch [22/650], Train Loss: 0.0213, Train L1 Loss: 1.0084
Epoch [22/650], Validation Loss: 0.0236, Validation L1: 1.0737, Smoothed Validation Loss: 0.0257
Epoch [23/650], Train Loss: 0.0211, Train L1 Loss: 1.0043
Epoch [23/650], Validation Loss: 0.0224, Validation L1: 1.0366, Smoothed Validation Loss: 0.0254
Epoch [24/650], Train Loss: 0.0209, Train L1 Loss: 0.9995
Epoch [24/650], Validation Loss: 0.0224, Validation L1: 1.0364, Smoothed Validation Loss: 0.0251
Epoch [25/650], Train Loss: 0.0208, Train L1 Loss: 0.9969
Epoch [25/650], Validation Loss: 0.0233, Validation L1: 1.0621, Smoothed Validation Loss: 0.0249
Epoch [26/650], Train Loss: 0.0207, Train L1 Loss: 0.9935
Epoch [26/650], Validation Loss: 0.0218, Validation L1: 1.0199, Smoothed Validation Loss: 0.0246
Epoch [27/650], Train Loss: 0.0204, Train L1 Loss: 0.9869
Epoch [27/650], Validation Loss: 0.0225, Validation L1: 1.0370, Smoothed Validation Loss: 0.0244
Epoch [28/650], Train Loss: 0.0203, Train L1 Loss: 0.9846
Epoch [28/650], Validation Loss: 0.0225, Validation L1: 1.0384, Smoothed Validation Loss: 0.0242
Epoch [29/650], Train Loss: 0.0203, Train L1 Loss: 0.9838
Epoch [29/650], Validation Loss: 0.0223, Validation L1: 1.0293, Smoothed Validation Loss: 0.0240
Epoch [30/650], Train Loss: 0.0202, Train L1 Loss: 0.9803
Epoch [30/650], Validation Loss: 0.0226, Validation L1: 1.0421, Smoothed Validation Loss: 0.0239
Epoch [31/650], Train Loss: 0.0202, Train L1 Loss: 0.9790
Epoch [31/650], Validation Loss: 0.0228, Validation L1: 1.0459, Smoothed Validation Loss: 0.0238
Epoch [32/650], Train Loss: 0.0201, Train L1 Loss: 0.9762
Epoch [32/650], Validation Loss: 0.0226, Validation L1: 1.0403, Smoothed Validation Loss: 0.0237
Epoch [33/650], Train Loss: 0.0198, Train L1 Loss: 0.9702
Epoch [33/650], Validation Loss: 0.0222, Validation L1: 1.0325, Smoothed Validation Loss: 0.0235
Epoch [34/650], Train Loss: 0.0198, Train L1 Loss: 0.9702
Epoch [34/650], Validation Loss: 0.0218, Validation L1: 1.0166, Smoothed Validation Loss: 0.0233
Epoch [35/650], Train Loss: 0.0197, Train L1 Loss: 0.9664
Epoch [35/650], Validation Loss: 0.0218, Validation L1: 1.0156, Smoothed Validation Loss: 0.0232
Epoch [36/650], Train Loss: 0.0197, Train L1 Loss: 0.9667
Epoch [36/650], Validation Loss: 0.0222, Validation L1: 1.0231, Smoothed Validation Loss: 0.0231
Epoch [37/650], Train Loss: 0.0196, Train L1 Loss: 0.9645
Epoch [37/650], Validation Loss: 0.0218, Validation L1: 1.0202, Smoothed Validation Loss: 0.0230
Epoch [38/650], Train Loss: 0.0194, Train L1 Loss: 0.9599
Epoch [38/650], Validation Loss: 0.0220, Validation L1: 1.0198, Smoothed Validation Loss: 0.0229
Epoch [39/650], Train Loss: 0.0195, Train L1 Loss: 0.9621
Epoch [39/650], Validation Loss: 0.0221, Validation L1: 1.0245, Smoothed Validation Loss: 0.0228
Epoch [40/650], Train Loss: 0.0195, Train L1 Loss: 0.9607
Epoch [40/650], Validation Loss: 0.0225, Validation L1: 1.0346, Smoothed Validation Loss: 0.0227
Epoch [41/650], Train Loss: 0.0192, Train L1 Loss: 0.9534
Epoch [41/650], Validation Loss: 0.0218, Validation L1: 1.0163, Smoothed Validation Loss: 0.0227
Epoch [42/650], Train Loss: 0.0192, Train L1 Loss: 0.9550
Epoch [42/650], Validation Loss: 0.0219, Validation L1: 1.0198, Smoothed Validation Loss: 0.0226
Epoch [43/650], Train Loss: 0.0192, Train L1 Loss: 0.9532
Epoch [43/650], Validation Loss: 0.0218, Validation L1: 1.0170, Smoothed Validation Loss: 0.0225
Epoch [44/650], Train Loss: 0.0193, Train L1 Loss: 0.9558
Epoch [44/650], Validation Loss: 0.0217, Validation L1: 1.0176, Smoothed Validation Loss: 0.0224
Epoch [45/650], Train Loss: 0.0189, Train L1 Loss: 0.9473
Epoch [45/650], Validation Loss: 0.0221, Validation L1: 1.0241, Smoothed Validation Loss: 0.0224
Epoch [46/650], Train Loss: 0.0189, Train L1 Loss: 0.9466
Epoch [46/650], Validation Loss: 0.0216, Validation L1: 1.0127, Smoothed Validation Loss: 0.0223
Epoch [47/650], Train Loss: 0.0188, Train L1 Loss: 0.9458
Epoch [47/650], Validation Loss: 0.0220, Validation L1: 1.0216, Smoothed Validation Loss: 0.0223
Epoch [48/650], Train Loss: 0.0188, Train L1 Loss: 0.9435
Epoch [48/650], Validation Loss: 0.0216, Validation L1: 1.0081, Smoothed Validation Loss: 0.0222
Epoch [49/650], Train Loss: 0.0187, Train L1 Loss: 0.9405
Epoch [49/650], Validation Loss: 0.0220, Validation L1: 1.0214, Smoothed Validation Loss: 0.0222
Epoch [50/650], Train Loss: 0.0186, Train L1 Loss: 0.9381
Epoch [50/650], Validation Loss: 0.0223, Validation L1: 1.0237, Smoothed Validation Loss: 0.0222
Epoch [51/650], Train Loss: 0.0187, Train L1 Loss: 0.9416
Epoch [51/650], Validation Loss: 0.0228, Validation L1: 1.0363, Smoothed Validation Loss: 0.0223
Epoch [52/650], Train Loss: 0.0187, Train L1 Loss: 0.9394
Epoch [52/650], Validation Loss: 0.0222, Validation L1: 1.0211, Smoothed Validation Loss: 0.0223
Epoch [53/650], Train Loss: 0.0185, Train L1 Loss: 0.9347
Epoch [53/650], Validation Loss: 0.0220, Validation L1: 1.0208, Smoothed Validation Loss: 0.0222
Epoch [54/650], Train Loss: 0.0185, Train L1 Loss: 0.9349
Epoch [54/650], Validation Loss: 0.0226, Validation L1: 1.0342, Smoothed Validation Loss: 0.0223
Epoch [55/650], Train Loss: 0.0184, Train L1 Loss: 0.9327
Epoch [55/650], Validation Loss: 0.0226, Validation L1: 1.0346, Smoothed Validation Loss: 0.0223
Epoch 00055: reducing learning rate of group 0 to 5.0000e-04.
Epoch [56/650], Train Loss: 0.0172, Train L1 Loss: 0.8969
Epoch [56/650], Validation Loss: 0.0207, Validation L1: 0.9793, Smoothed Validation Loss: 0.0221
Epoch [57/650], Train Loss: 0.0168, Train L1 Loss: 0.8845
Epoch [57/650], Validation Loss: 0.0210, Validation L1: 0.9856, Smoothed Validation Loss: 0.0220
Epoch [58/650], Train Loss: 0.0166, Train L1 Loss: 0.8789
Epoch [58/650], Validation Loss: 0.0210, Validation L1: 0.9856, Smoothed Validation Loss: 0.0219
Epoch [59/650], Train Loss: 0.0164, Train L1 Loss: 0.8752
Epoch [59/650], Validation Loss: 0.0214, Validation L1: 0.9975, Smoothed Validation Loss: 0.0219
Epoch [60/650], Train Loss: 0.0164, Train L1 Loss: 0.8741
Epoch [60/650], Validation Loss: 0.0214, Validation L1: 0.9974, Smoothed Validation Loss: 0.0218
Epoch [61/650], Train Loss: 0.0162, Train L1 Loss: 0.8682
Epoch [61/650], Validation Loss: 0.0216, Validation L1: 1.0025, Smoothed Validation Loss: 0.0218
Epoch [62/650], Train Loss: 0.0160, Train L1 Loss: 0.8645
Epoch [62/650], Validation Loss: 0.0217, Validation L1: 1.0044, Smoothed Validation Loss: 0.0218
Epoch [63/650], Train Loss: 0.0160, Train L1 Loss: 0.8630
Epoch [63/650], Validation Loss: 0.0216, Validation L1: 1.0022, Smoothed Validation Loss: 0.0218
Epoch [64/650], Train Loss: 0.0160, Train L1 Loss: 0.8639
Epoch [64/650], Validation Loss: 0.0216, Validation L1: 1.0010, Smoothed Validation Loss: 0.0218
Epoch [65/650], Train Loss: 0.0159, Train L1 Loss: 0.8622
Epoch [65/650], Validation Loss: 0.0216, Validation L1: 1.0029, Smoothed Validation Loss: 0.0217
Epoch [66/650], Train Loss: 0.0160, Train L1 Loss: 0.8652
Epoch [66/650], Validation Loss: 0.0212, Validation L1: 0.9947, Smoothed Validation Loss: 0.0217
Epoch [67/650], Train Loss: 0.0159, Train L1 Loss: 0.8614
Epoch [67/650], Validation Loss: 0.0212, Validation L1: 0.9968, Smoothed Validation Loss: 0.0216
Epoch [68/650], Train Loss: 0.0158, Train L1 Loss: 0.8589
Epoch [68/650], Validation Loss: 0.0215, Validation L1: 1.0033, Smoothed Validation Loss: 0.0216
Epoch [69/650], Train Loss: 0.0158, Train L1 Loss: 0.8584
Epoch [69/650], Validation Loss: 0.0218, Validation L1: 1.0114, Smoothed Validation Loss: 0.0216
Epoch [70/650], Train Loss: 0.0157, Train L1 Loss: 0.8576
Epoch [70/650], Validation Loss: 0.0221, Validation L1: 1.0179, Smoothed Validation Loss: 0.0217
Epoch [71/650], Train Loss: 0.0157, Train L1 Loss: 0.8579
Epoch [71/650], Validation Loss: 0.0224, Validation L1: 1.0241, Smoothed Validation Loss: 0.0218
Epoch [72/650], Train Loss: 0.0156, Train L1 Loss: 0.8559
Epoch [72/650], Validation Loss: 0.0219, Validation L1: 1.0156, Smoothed Validation Loss: 0.0218
Epoch [73/650], Train Loss: 0.0156, Train L1 Loss: 0.8548
Epoch [73/650], Validation Loss: 0.0219, Validation L1: 1.0142, Smoothed Validation Loss: 0.0218
Epoch [74/650], Train Loss: 0.0156, Train L1 Loss: 0.8543
Epoch [74/650], Validation Loss: 0.0218, Validation L1: 1.0100, Smoothed Validation Loss: 0.0218
Epoch 00074: reducing learning rate of group 0 to 2.5000e-04.
Epoch [75/650], Train Loss: 0.0155, Train L1 Loss: 0.8474
Epoch [75/650], Validation Loss: 0.0209, Validation L1: 0.9823, Smoothed Validation Loss: 0.0217
Epoch [76/650], Train Loss: 0.0150, Train L1 Loss: 0.8332
Epoch [76/650], Validation Loss: 0.0211, Validation L1: 0.9848, Smoothed Validation Loss: 0.0216
Epoch [77/650], Train Loss: 0.0148, Train L1 Loss: 0.8268
Epoch [77/650], Validation Loss: 0.0213, Validation L1: 0.9883, Smoothed Validation Loss: 0.0216
Epoch [78/650], Train Loss: 0.0146, Train L1 Loss: 0.8228
Epoch [78/650], Validation Loss: 0.0214, Validation L1: 0.9911, Smoothed Validation Loss: 0.0216
Epoch [79/650], Train Loss: 0.0145, Train L1 Loss: 0.8185
Epoch [79/650], Validation Loss: 0.0217, Validation L1: 0.9969, Smoothed Validation Loss: 0.0216
Epoch [80/650], Train Loss: 0.0144, Train L1 Loss: 0.8149
Epoch [80/650], Validation Loss: 0.0218, Validation L1: 0.9984, Smoothed Validation Loss: 0.0216
Epoch [81/650], Train Loss: 0.0142, Train L1 Loss: 0.8113
Epoch [81/650], Validation Loss: 0.0220, Validation L1: 1.0032, Smoothed Validation Loss: 0.0217
Epoch [82/650], Train Loss: 0.0141, Train L1 Loss: 0.8086
Epoch [82/650], Validation Loss: 0.0221, Validation L1: 1.0054, Smoothed Validation Loss: 0.0217
Epoch [83/650], Train Loss: 0.0140, Train L1 Loss: 0.8057
Epoch [83/650], Validation Loss: 0.0223, Validation L1: 1.0093, Smoothed Validation Loss: 0.0218
Epoch [84/650], Train Loss: 0.0139, Train L1 Loss: 0.8035
Epoch [84/650], Validation Loss: 0.0224, Validation L1: 1.0119, Smoothed Validation Loss: 0.0218
Epoch 00084: reducing learning rate of group 0 to 1.2500e-04.
Epoch [85/650], Train Loss: 0.0142, Train L1 Loss: 0.8090
Epoch [85/650], Validation Loss: 0.0211, Validation L1: 0.9801, Smoothed Validation Loss: 0.0218
Epoch [86/650], Train Loss: 0.0140, Train L1 Loss: 0.8011
Epoch [86/650], Validation Loss: 0.0211, Validation L1: 0.9792, Smoothed Validation Loss: 0.0217
Epoch [87/650], Train Loss: 0.0138, Train L1 Loss: 0.7967
Epoch [87/650], Validation Loss: 0.0212, Validation L1: 0.9799, Smoothed Validation Loss: 0.0216
Epoch [88/650], Train Loss: 0.0137, Train L1 Loss: 0.7933
Epoch [88/650], Validation Loss: 0.0213, Validation L1: 0.9811, Smoothed Validation Loss: 0.0216
Epoch [89/650], Train Loss: 0.0136, Train L1 Loss: 0.7904
Epoch [89/650], Validation Loss: 0.0214, Validation L1: 0.9827, Smoothed Validation Loss: 0.0216
Epoch [90/650], Train Loss: 0.0135, Train L1 Loss: 0.7878
Epoch [90/650], Validation Loss: 0.0215, Validation L1: 0.9844, Smoothed Validation Loss: 0.0216
Epoch [91/650], Train Loss: 0.0134, Train L1 Loss: 0.7854
Epoch [91/650], Validation Loss: 0.0216, Validation L1: 0.9865, Smoothed Validation Loss: 0.0216
Epoch [92/650], Train Loss: 0.0134, Train L1 Loss: 0.7831
Epoch [92/650], Validation Loss: 0.0217, Validation L1: 0.9891, Smoothed Validation Loss: 0.0216
Epoch [93/650], Train Loss: 0.0133, Train L1 Loss: 0.7811
Epoch [93/650], Validation Loss: 0.0218, Validation L1: 0.9920, Smoothed Validation Loss: 0.0216
Epoch [94/650], Train Loss: 0.0132, Train L1 Loss: 0.7793
Epoch [94/650], Validation Loss: 0.0220, Validation L1: 0.9946, Smoothed Validation Loss: 0.0216
Epoch [95/650], Train Loss: 0.0132, Train L1 Loss: 0.7770
Epoch [95/650], Validation Loss: 0.0221, Validation L1: 0.9973, Smoothed Validation Loss: 0.0217
Epoch [96/650], Train Loss: 0.0131, Train L1 Loss: 0.7750
Epoch [96/650], Validation Loss: 0.0222, Validation L1: 1.0001, Smoothed Validation Loss: 0.0217
Epoch 00096: reducing learning rate of group 0 to 6.2500e-05.
Epoch [97/650], Train Loss: 0.0134, Train L1 Loss: 0.7826
Epoch [97/650], Validation Loss: 0.0215, Validation L1: 0.9856, Smoothed Validation Loss: 0.0217
Epoch [98/650], Train Loss: 0.0133, Train L1 Loss: 0.7786
Epoch [98/650], Validation Loss: 0.0214, Validation L1: 0.9835, Smoothed Validation Loss: 0.0217
Epoch [99/650], Train Loss: 0.0132, Train L1 Loss: 0.7759
Epoch [99/650], Validation Loss: 0.0214, Validation L1: 0.9825, Smoothed Validation Loss: 0.0217
Epoch [100/650], Train Loss: 0.0131, Train L1 Loss: 0.7737
Epoch [100/650], Validation Loss: 0.0214, Validation L1: 0.9823, Smoothed Validation Loss: 0.0216
Epoch [101/650], Train Loss: 0.0131, Train L1 Loss: 0.7717
Epoch [101/650], Validation Loss: 0.0214, Validation L1: 0.9823, Smoothed Validation Loss: 0.0216
Epoch [102/650], Train Loss: 0.0130, Train L1 Loss: 0.7699
Epoch [102/650], Validation Loss: 0.0214, Validation L1: 0.9823, Smoothed Validation Loss: 0.0216
Epoch 00102: reducing learning rate of group 0 to 3.1250e-05.
Epoch [103/650], Train Loss: 0.0133, Train L1 Loss: 0.7767
Epoch [103/650], Validation Loss: 0.0205, Validation L1: 0.9621, Smoothed Validation Loss: 0.0215
Epoch [104/650], Train Loss: 0.0132, Train L1 Loss: 0.7734
Epoch [104/650], Validation Loss: 0.0205, Validation L1: 0.9614, Smoothed Validation Loss: 0.0214
Epoch [105/650], Train Loss: 0.0131, Train L1 Loss: 0.7716
Epoch [105/650], Validation Loss: 0.0205, Validation L1: 0.9611, Smoothed Validation Loss: 0.0213
Epoch [106/650], Train Loss: 0.0131, Train L1 Loss: 0.7701
Epoch [106/650], Validation Loss: 0.0205, Validation L1: 0.9609, Smoothed Validation Loss: 0.0212
Epoch [107/650], Train Loss: 0.0131, Train L1 Loss: 0.7688
Epoch [107/650], Validation Loss: 0.0205, Validation L1: 0.9609, Smoothed Validation Loss: 0.0211
Epoch [108/650], Train Loss: 0.0130, Train L1 Loss: 0.7675
Epoch [108/650], Validation Loss: 0.0205, Validation L1: 0.9609, Smoothed Validation Loss: 0.0211
Epoch [109/650], Train Loss: 0.0130, Train L1 Loss: 0.7664
Epoch [109/650], Validation Loss: 0.0205, Validation L1: 0.9610, Smoothed Validation Loss: 0.0210
Epoch [110/650], Train Loss: 0.0129, Train L1 Loss: 0.7653
Epoch [110/650], Validation Loss: 0.0205, Validation L1: 0.9610, Smoothed Validation Loss: 0.0210
Epoch [111/650], Train Loss: 0.0129, Train L1 Loss: 0.7642
Epoch [111/650], Validation Loss: 0.0205, Validation L1: 0.9612, Smoothed Validation Loss: 0.0209
Epoch [112/650], Train Loss: 0.0129, Train L1 Loss: 0.7632
Epoch [112/650], Validation Loss: 0.0205, Validation L1: 0.9613, Smoothed Validation Loss: 0.0209
Epoch [113/650], Train Loss: 0.0129, Train L1 Loss: 0.7623
Epoch [113/650], Validation Loss: 0.0205, Validation L1: 0.9615, Smoothed Validation Loss: 0.0209
Epoch [114/650], Train Loss: 0.0128, Train L1 Loss: 0.7613
Epoch [114/650], Validation Loss: 0.0205, Validation L1: 0.9617, Smoothed Validation Loss: 0.0208
Epoch [115/650], Train Loss: 0.0128, Train L1 Loss: 0.7604
Epoch [115/650], Validation Loss: 0.0206, Validation L1: 0.9619, Smoothed Validation Loss: 0.0208
Epoch [116/650], Train Loss: 0.0128, Train L1 Loss: 0.7595
Epoch [116/650], Validation Loss: 0.0206, Validation L1: 0.9621, Smoothed Validation Loss: 0.0208
Epoch [117/650], Train Loss: 0.0127, Train L1 Loss: 0.7587
Epoch [117/650], Validation Loss: 0.0206, Validation L1: 0.9623, Smoothed Validation Loss: 0.0208
Epoch [118/650], Train Loss: 0.0127, Train L1 Loss: 0.7578
Epoch [118/650], Validation Loss: 0.0206, Validation L1: 0.9626, Smoothed Validation Loss: 0.0207
Epoch [119/650], Train Loss: 0.0127, Train L1 Loss: 0.7570
Epoch [119/650], Validation Loss: 0.0206, Validation L1: 0.9628, Smoothed Validation Loss: 0.0207
Epoch [120/650], Train Loss: 0.0127, Train L1 Loss: 0.7561
Epoch [120/650], Validation Loss: 0.0206, Validation L1: 0.9631, Smoothed Validation Loss: 0.0207
Epoch [121/650], Train Loss: 0.0126, Train L1 Loss: 0.7553
Epoch [121/650], Validation Loss: 0.0206, Validation L1: 0.9633, Smoothed Validation Loss: 0.0207
Epoch [122/650], Train Loss: 0.0126, Train L1 Loss: 0.7545
Epoch [122/650], Validation Loss: 0.0207, Validation L1: 0.9636, Smoothed Validation Loss: 0.0207
Epoch [123/650], Train Loss: 0.0126, Train L1 Loss: 0.7537
Epoch [123/650], Validation Loss: 0.0207, Validation L1: 0.9639, Smoothed Validation Loss: 0.0207
Epoch [124/650], Train Loss: 0.0126, Train L1 Loss: 0.7529
Epoch [124/650], Validation Loss: 0.0207, Validation L1: 0.9641, Smoothed Validation Loss: 0.0207
Epoch [125/650], Train Loss: 0.0125, Train L1 Loss: 0.7521
Epoch [125/650], Validation Loss: 0.0207, Validation L1: 0.9644, Smoothed Validation Loss: 0.0207
Epoch [126/650], Train Loss: 0.0125, Train L1 Loss: 0.7514
Epoch [126/650], Validation Loss: 0.0207, Validation L1: 0.9646, Smoothed Validation Loss: 0.0207
Epoch [127/650], Train Loss: 0.0125, Train L1 Loss: 0.7506
Epoch [127/650], Validation Loss: 0.0207, Validation L1: 0.9649, Smoothed Validation Loss: 0.0207
Epoch [128/650], Train Loss: 0.0125, Train L1 Loss: 0.7499
Epoch [128/650], Validation Loss: 0.0207, Validation L1: 0.9652, Smoothed Validation Loss: 0.0207
Epoch [129/650], Train Loss: 0.0124, Train L1 Loss: 0.7491
Epoch [129/650], Validation Loss: 0.0208, Validation L1: 0.9654, Smoothed Validation Loss: 0.0207
Epoch [130/650], Train Loss: 0.0124, Train L1 Loss: 0.7484
Epoch [130/650], Validation Loss: 0.0208, Validation L1: 0.9657, Smoothed Validation Loss: 0.0207
Epoch [131/650], Train Loss: 0.0124, Train L1 Loss: 0.7477
Epoch [131/650], Validation Loss: 0.0208, Validation L1: 0.9661, Smoothed Validation Loss: 0.0207
Epoch 00131: reducing learning rate of group 0 to 1.5625e-05.
Epoch [132/650], Train Loss: 0.0125, Train L1 Loss: 0.7514
Epoch [132/650], Validation Loss: 0.0206, Validation L1: 0.9595, Smoothed Validation Loss: 0.0207
Epoch [133/650], Train Loss: 0.0125, Train L1 Loss: 0.7502
Epoch [133/650], Validation Loss: 0.0205, Validation L1: 0.9593, Smoothed Validation Loss: 0.0207
Epoch [134/650], Train Loss: 0.0125, Train L1 Loss: 0.7494
Epoch [134/650], Validation Loss: 0.0205, Validation L1: 0.9592, Smoothed Validation Loss: 0.0207
Epoch [135/650], Train Loss: 0.0125, Train L1 Loss: 0.7487
Epoch [135/650], Validation Loss: 0.0205, Validation L1: 0.9592, Smoothed Validation Loss: 0.0207
Epoch [136/650], Train Loss: 0.0125, Train L1 Loss: 0.7481
Epoch [136/650], Validation Loss: 0.0205, Validation L1: 0.9592, Smoothed Validation Loss: 0.0206
Epoch [137/650], Train Loss: 0.0124, Train L1 Loss: 0.7476
Epoch [137/650], Validation Loss: 0.0205, Validation L1: 0.9592, Smoothed Validation Loss: 0.0206
Epoch [138/650], Train Loss: 0.0124, Train L1 Loss: 0.7471
Epoch [138/650], Validation Loss: 0.0205, Validation L1: 0.9593, Smoothed Validation Loss: 0.0206
Epoch [139/650], Train Loss: 0.0124, Train L1 Loss: 0.7466
Epoch [139/650], Validation Loss: 0.0205, Validation L1: 0.9593, Smoothed Validation Loss: 0.0206
Epoch [140/650], Train Loss: 0.0124, Train L1 Loss: 0.7461
Epoch [140/650], Validation Loss: 0.0205, Validation L1: 0.9594, Smoothed Validation Loss: 0.0206
Epoch [141/650], Train Loss: 0.0124, Train L1 Loss: 0.7456
Epoch [141/650], Validation Loss: 0.0206, Validation L1: 0.9595, Smoothed Validation Loss: 0.0206
Epoch [142/650], Train Loss: 0.0124, Train L1 Loss: 0.7451
Epoch [142/650], Validation Loss: 0.0206, Validation L1: 0.9596, Smoothed Validation Loss: 0.0206
Epoch [143/650], Train Loss: 0.0124, Train L1 Loss: 0.7447
Epoch [143/650], Validation Loss: 0.0206, Validation L1: 0.9597, Smoothed Validation Loss: 0.0206
Epoch [144/650], Train Loss: 0.0123, Train L1 Loss: 0.7442
Epoch [144/650], Validation Loss: 0.0206, Validation L1: 0.9599, Smoothed Validation Loss: 0.0206
Epoch [145/650], Train Loss: 0.0123, Train L1 Loss: 0.7438
Epoch [145/650], Validation Loss: 0.0206, Validation L1: 0.9600, Smoothed Validation Loss: 0.0206
Epoch [146/650], Train Loss: 0.0123, Train L1 Loss: 0.7434
Epoch [146/650], Validation Loss: 0.0206, Validation L1: 0.9601, Smoothed Validation Loss: 0.0206
Epoch [147/650], Train Loss: 0.0123, Train L1 Loss: 0.7429
Epoch [147/650], Validation Loss: 0.0206, Validation L1: 0.9603, Smoothed Validation Loss: 0.0206
Epoch [148/650], Train Loss: 0.0123, Train L1 Loss: 0.7425
Epoch [148/650], Validation Loss: 0.0206, Validation L1: 0.9604, Smoothed Validation Loss: 0.0206
Epoch [149/650], Train Loss: 0.0123, Train L1 Loss: 0.7421
Epoch [149/650], Validation Loss: 0.0206, Validation L1: 0.9606, Smoothed Validation Loss: 0.0206
Epoch [150/650], Train Loss: 0.0123, Train L1 Loss: 0.7417
Epoch [150/650], Validation Loss: 0.0206, Validation L1: 0.9607, Smoothed Validation Loss: 0.0206
Epoch [151/650], Train Loss: 0.0123, Train L1 Loss: 0.7413
Epoch [151/650], Validation Loss: 0.0206, Validation L1: 0.9609, Smoothed Validation Loss: 0.0206
Epoch [152/650], Train Loss: 0.0122, Train L1 Loss: 0.7409
Epoch [152/650], Validation Loss: 0.0206, Validation L1: 0.9610, Smoothed Validation Loss: 0.0206
Epoch 00152: reducing learning rate of group 0 to 7.8125e-06.
Epoch [153/650], Train Loss: 0.0123, Train L1 Loss: 0.7436
Epoch [153/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0206
Epoch [154/650], Train Loss: 0.0123, Train L1 Loss: 0.7427
Epoch [154/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0206
Epoch [155/650], Train Loss: 0.0123, Train L1 Loss: 0.7423
Epoch [155/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0206
Epoch [156/650], Train Loss: 0.0123, Train L1 Loss: 0.7420
Epoch [156/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0206
Epoch [157/650], Train Loss: 0.0123, Train L1 Loss: 0.7417
Epoch [157/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0206
Epoch [158/650], Train Loss: 0.0123, Train L1 Loss: 0.7414
Epoch [158/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0206
Epoch [159/650], Train Loss: 0.0123, Train L1 Loss: 0.7411
Epoch [159/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0206
Epoch [160/650], Train Loss: 0.0123, Train L1 Loss: 0.7408
Epoch [160/650], Validation Loss: 0.0205, Validation L1: 0.9578, Smoothed Validation Loss: 0.0206
Epoch [161/650], Train Loss: 0.0123, Train L1 Loss: 0.7405
Epoch [161/650], Validation Loss: 0.0205, Validation L1: 0.9578, Smoothed Validation Loss: 0.0206
Epoch [162/650], Train Loss: 0.0123, Train L1 Loss: 0.7403
Epoch [162/650], Validation Loss: 0.0205, Validation L1: 0.9579, Smoothed Validation Loss: 0.0206
Epoch [163/650], Train Loss: 0.0122, Train L1 Loss: 0.7400
Epoch [163/650], Validation Loss: 0.0205, Validation L1: 0.9579, Smoothed Validation Loss: 0.0205
Epoch [164/650], Train Loss: 0.0122, Train L1 Loss: 0.7398
Epoch [164/650], Validation Loss: 0.0205, Validation L1: 0.9580, Smoothed Validation Loss: 0.0205
Epoch [165/650], Train Loss: 0.0122, Train L1 Loss: 0.7395
Epoch [165/650], Validation Loss: 0.0205, Validation L1: 0.9581, Smoothed Validation Loss: 0.0205
Epoch [166/650], Train Loss: 0.0122, Train L1 Loss: 0.7393
Epoch [166/650], Validation Loss: 0.0205, Validation L1: 0.9581, Smoothed Validation Loss: 0.0205
Epoch [167/650], Train Loss: 0.0122, Train L1 Loss: 0.7391
Epoch [167/650], Validation Loss: 0.0205, Validation L1: 0.9582, Smoothed Validation Loss: 0.0205
Epoch [168/650], Train Loss: 0.0122, Train L1 Loss: 0.7388
Epoch [168/650], Validation Loss: 0.0206, Validation L1: 0.9583, Smoothed Validation Loss: 0.0205
Epoch [169/650], Train Loss: 0.0122, Train L1 Loss: 0.7386
Epoch [169/650], Validation Loss: 0.0206, Validation L1: 0.9584, Smoothed Validation Loss: 0.0205
Epoch [170/650], Train Loss: 0.0122, Train L1 Loss: 0.7384
Epoch [170/650], Validation Loss: 0.0206, Validation L1: 0.9585, Smoothed Validation Loss: 0.0205
Epoch 00170: reducing learning rate of group 0 to 3.9063e-06.
Epoch [171/650], Train Loss: 0.0123, Train L1 Loss: 0.7397
Epoch [171/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0205
Epoch [172/650], Train Loss: 0.0122, Train L1 Loss: 0.7391
Epoch [172/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0205
Epoch [173/650], Train Loss: 0.0122, Train L1 Loss: 0.7389
Epoch [173/650], Validation Loss: 0.0205, Validation L1: 0.9575, Smoothed Validation Loss: 0.0205
Epoch [174/650], Train Loss: 0.0122, Train L1 Loss: 0.7387
Epoch [174/650], Validation Loss: 0.0205, Validation L1: 0.9575, Smoothed Validation Loss: 0.0205
Epoch [175/650], Train Loss: 0.0122, Train L1 Loss: 0.7385
Epoch [175/650], Validation Loss: 0.0205, Validation L1: 0.9575, Smoothed Validation Loss: 0.0205
Epoch [176/650], Train Loss: 0.0122, Train L1 Loss: 0.7384
Epoch [176/650], Validation Loss: 0.0205, Validation L1: 0.9575, Smoothed Validation Loss: 0.0205
Epoch [177/650], Train Loss: 0.0122, Train L1 Loss: 0.7382
Epoch [177/650], Validation Loss: 0.0205, Validation L1: 0.9575, Smoothed Validation Loss: 0.0205
Epoch [178/650], Train Loss: 0.0122, Train L1 Loss: 0.7381
Epoch [178/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0205
Epoch [179/650], Train Loss: 0.0122, Train L1 Loss: 0.7379
Epoch [179/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0205
Epoch [180/650], Train Loss: 0.0122, Train L1 Loss: 0.7378
Epoch [180/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0205
Epoch [181/650], Train Loss: 0.0122, Train L1 Loss: 0.7377
Epoch [181/650], Validation Loss: 0.0205, Validation L1: 0.9576, Smoothed Validation Loss: 0.0205
Epoch [182/650], Train Loss: 0.0122, Train L1 Loss: 0.7375
Epoch [182/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0205
Epoch [183/650], Train Loss: 0.0122, Train L1 Loss: 0.7374
Epoch [183/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0205
Epoch [184/650], Train Loss: 0.0122, Train L1 Loss: 0.7373
Epoch [184/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0205
Epoch [185/650], Train Loss: 0.0122, Train L1 Loss: 0.7371
Epoch [185/650], Validation Loss: 0.0205, Validation L1: 0.9577, Smoothed Validation Loss: 0.0205
Epoch 00185: reducing learning rate of group 0 to 1.9531e-06.
Epoch [186/650], Train Loss: 0.0122, Train L1 Loss: 0.7375
Epoch [186/650], Validation Loss: 0.0205, Validation L1: 0.9573, Smoothed Validation Loss: 0.0205
Epoch [187/650], Train Loss: 0.0122, Train L1 Loss: 0.7371
Epoch [187/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [188/650], Train Loss: 0.0122, Train L1 Loss: 0.7370
Epoch [188/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [189/650], Train Loss: 0.0122, Train L1 Loss: 0.7369
Epoch [189/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [190/650], Train Loss: 0.0122, Train L1 Loss: 0.7368
Epoch [190/650], Validation Loss: 0.0205, Validation L1: 0.9571, Smoothed Validation Loss: 0.0205
Epoch [191/650], Train Loss: 0.0122, Train L1 Loss: 0.7367
Epoch [191/650], Validation Loss: 0.0205, Validation L1: 0.9571, Smoothed Validation Loss: 0.0205
Epoch [192/650], Train Loss: 0.0122, Train L1 Loss: 0.7367
Epoch [192/650], Validation Loss: 0.0205, Validation L1: 0.9571, Smoothed Validation Loss: 0.0205
Epoch [193/650], Train Loss: 0.0122, Train L1 Loss: 0.7366
Epoch [193/650], Validation Loss: 0.0205, Validation L1: 0.9571, Smoothed Validation Loss: 0.0205
Epoch [194/650], Train Loss: 0.0122, Train L1 Loss: 0.7365
Epoch [194/650], Validation Loss: 0.0205, Validation L1: 0.9571, Smoothed Validation Loss: 0.0205
Epoch [195/650], Train Loss: 0.0122, Train L1 Loss: 0.7364
Epoch [195/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [196/650], Train Loss: 0.0122, Train L1 Loss: 0.7364
Epoch [196/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [197/650], Train Loss: 0.0122, Train L1 Loss: 0.7363
Epoch [197/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [198/650], Train Loss: 0.0122, Train L1 Loss: 0.7362
Epoch [198/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [199/650], Train Loss: 0.0122, Train L1 Loss: 0.7361
Epoch [199/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [200/650], Train Loss: 0.0122, Train L1 Loss: 0.7361
Epoch [200/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [201/650], Train Loss: 0.0122, Train L1 Loss: 0.7360
Epoch [201/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [202/650], Train Loss: 0.0121, Train L1 Loss: 0.7359
Epoch [202/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch [203/650], Train Loss: 0.0121, Train L1 Loss: 0.7359
Epoch [203/650], Validation Loss: 0.0205, Validation L1: 0.9572, Smoothed Validation Loss: 0.0205
Epoch 00203: reducing learning rate of group 0 to 9.7656e-07.
Epoch [204/650], Train Loss: 0.0121, Train L1 Loss: 0.7359
Epoch [204/650], Validation Loss: 0.0205, Validation L1: 0.9569, Smoothed Validation Loss: 0.0205
Epoch [205/650], Train Loss: 0.0121, Train L1 Loss: 0.7357
Epoch [205/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [206/650], Train Loss: 0.0121, Train L1 Loss: 0.7356
Epoch [206/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [207/650], Train Loss: 0.0121, Train L1 Loss: 0.7355
Epoch [207/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [208/650], Train Loss: 0.0121, Train L1 Loss: 0.7355
Epoch [208/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [209/650], Train Loss: 0.0121, Train L1 Loss: 0.7354
Epoch [209/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [210/650], Train Loss: 0.0121, Train L1 Loss: 0.7354
Epoch [210/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [211/650], Train Loss: 0.0121, Train L1 Loss: 0.7354
Epoch [211/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [212/650], Train Loss: 0.0121, Train L1 Loss: 0.7353
Epoch [212/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [213/650], Train Loss: 0.0121, Train L1 Loss: 0.7353
Epoch [213/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [214/650], Train Loss: 0.0121, Train L1 Loss: 0.7352
Epoch [214/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [215/650], Train Loss: 0.0121, Train L1 Loss: 0.7352
Epoch [215/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [216/650], Train Loss: 0.0121, Train L1 Loss: 0.7352
Epoch [216/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [217/650], Train Loss: 0.0121, Train L1 Loss: 0.7351
Epoch [217/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [218/650], Train Loss: 0.0121, Train L1 Loss: 0.7351
Epoch [218/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [219/650], Train Loss: 0.0121, Train L1 Loss: 0.7351
Epoch [219/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [220/650], Train Loss: 0.0121, Train L1 Loss: 0.7350
Epoch [220/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [221/650], Train Loss: 0.0121, Train L1 Loss: 0.7350
Epoch [221/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [222/650], Train Loss: 0.0121, Train L1 Loss: 0.7350
Epoch [222/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch [223/650], Train Loss: 0.0121, Train L1 Loss: 0.7349
Epoch [223/650], Validation Loss: 0.0205, Validation L1: 0.9568, Smoothed Validation Loss: 0.0205
Epoch 00223: reducing learning rate of group 0 to 4.8828e-07.
Epoch [224/650], Train Loss: 0.0121, Train L1 Loss: 0.7348
Epoch [224/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [225/650], Train Loss: 0.0121, Train L1 Loss: 0.7347
Epoch [225/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [226/650], Train Loss: 0.0121, Train L1 Loss: 0.7347
Epoch [226/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [227/650], Train Loss: 0.0121, Train L1 Loss: 0.7347
Epoch [227/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [228/650], Train Loss: 0.0121, Train L1 Loss: 0.7346
Epoch [228/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [229/650], Train Loss: 0.0121, Train L1 Loss: 0.7346
Epoch [229/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [230/650], Train Loss: 0.0121, Train L1 Loss: 0.7346
Epoch [230/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [231/650], Train Loss: 0.0121, Train L1 Loss: 0.7346
Epoch [231/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [232/650], Train Loss: 0.0121, Train L1 Loss: 0.7346
Epoch [232/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [233/650], Train Loss: 0.0121, Train L1 Loss: 0.7345
Epoch [233/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [234/650], Train Loss: 0.0121, Train L1 Loss: 0.7345
Epoch [234/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [235/650], Train Loss: 0.0121, Train L1 Loss: 0.7345
Epoch [235/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [236/650], Train Loss: 0.0121, Train L1 Loss: 0.7345
Epoch [236/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch 00236: reducing learning rate of group 0 to 2.4414e-07.
Epoch [237/650], Train Loss: 0.0121, Train L1 Loss: 0.7344
Epoch [237/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [238/650], Train Loss: 0.0121, Train L1 Loss: 0.7344
Epoch [238/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [239/650], Train Loss: 0.0121, Train L1 Loss: 0.7343
Epoch [239/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [240/650], Train Loss: 0.0121, Train L1 Loss: 0.7343
Epoch [240/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [241/650], Train Loss: 0.0121, Train L1 Loss: 0.7343
Epoch [241/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [242/650], Train Loss: 0.0121, Train L1 Loss: 0.7343
Epoch [242/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [243/650], Train Loss: 0.0121, Train L1 Loss: 0.7343
Epoch [243/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [244/650], Train Loss: 0.0121, Train L1 Loss: 0.7343
Epoch [244/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch 00244: reducing learning rate of group 0 to 1.2207e-07.
Epoch [245/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [245/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [246/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [246/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [247/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [247/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [248/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [248/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [249/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [249/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [250/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [250/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [251/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [251/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [252/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [252/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [253/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [253/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [254/650], Train Loss: 0.0121, Train L1 Loss: 0.7342
Epoch [254/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [255/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [255/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [256/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [256/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch 00256: reducing learning rate of group 0 to 6.1035e-08.
Epoch [257/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [257/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [258/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [258/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [259/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [259/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [260/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [260/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [261/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [261/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [262/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [262/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch 00262: reducing learning rate of group 0 to 3.0518e-08.
Epoch [263/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [263/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [264/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [264/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [265/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [265/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [266/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [266/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [267/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [267/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [268/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [268/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch 00268: reducing learning rate of group 0 to 1.5259e-08.
Epoch [269/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [269/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [270/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [270/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [271/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [271/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [272/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [272/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [273/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [273/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [274/650], Train Loss: 0.0121, Train L1 Loss: 0.7341
Epoch [274/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [275/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [275/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [276/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [276/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [277/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [277/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [278/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [278/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [279/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [279/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [280/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [280/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [281/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [281/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [282/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [282/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [283/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [283/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [284/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [284/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [285/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [285/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [286/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [286/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [287/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [287/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [288/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [288/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [289/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [289/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [290/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [290/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [291/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [291/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [292/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [292/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [293/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [293/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [294/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [294/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [295/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [295/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [296/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [296/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [297/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [297/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [298/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [298/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [299/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [299/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [300/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [300/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [301/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [301/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [302/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [302/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [303/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [303/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [304/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [304/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [305/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [305/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [306/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [306/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [307/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [307/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [308/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [308/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [309/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [309/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [310/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [310/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [311/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [311/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [312/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [312/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [313/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [313/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [314/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [314/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [315/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [315/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [316/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [316/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [317/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [317/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [318/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [318/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [319/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [319/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [320/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [320/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [321/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [321/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [322/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [322/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [323/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [323/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [324/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [324/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [325/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [325/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [326/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [326/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [327/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [327/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [328/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [328/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [329/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [329/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [330/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [330/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [331/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [331/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [332/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [332/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [333/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [333/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [334/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [334/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [335/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [335/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [336/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [336/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [337/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [337/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [338/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [338/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [339/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [339/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [340/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [340/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [341/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [341/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [342/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [342/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [343/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [343/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [344/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [344/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [345/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [345/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [346/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [346/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [347/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [347/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [348/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [348/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [349/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [349/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [350/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [350/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [351/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [351/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [352/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [352/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [353/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [353/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [354/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [354/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [355/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [355/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [356/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [356/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [357/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [357/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [358/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [358/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [359/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [359/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [360/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [360/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [361/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [361/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [362/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [362/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [363/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [363/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [364/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [364/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [365/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [365/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [366/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [366/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [367/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [367/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [368/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [368/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [369/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [369/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [370/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [370/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [371/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [371/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [372/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [372/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [373/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [373/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [374/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [374/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [375/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [375/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [376/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [376/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [377/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [377/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [378/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [378/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [379/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [379/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [380/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [380/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [381/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [381/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [382/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [382/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [383/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [383/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [384/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [384/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [385/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [385/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [386/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [386/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [387/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [387/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [388/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [388/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [389/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [389/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [390/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [390/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [391/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [391/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [392/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [392/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [393/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [393/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [394/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [394/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [395/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [395/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [396/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [396/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [397/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [397/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [398/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [398/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [399/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [399/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [400/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [400/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [401/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [401/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [402/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [402/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [403/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [403/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [404/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [404/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [405/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [405/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [406/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [406/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [407/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [407/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [408/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [408/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [409/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [409/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [410/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [410/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [411/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [411/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [412/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [412/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [413/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [413/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [414/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [414/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [415/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [415/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [416/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [416/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [417/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [417/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [418/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [418/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [419/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [419/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [420/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [420/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [421/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [421/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [422/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [422/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [423/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [423/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [424/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [424/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [425/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [425/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [426/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [426/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [427/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [427/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [428/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [428/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [429/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [429/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [430/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [430/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [431/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [431/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [432/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [432/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [433/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [433/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [434/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [434/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [435/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [435/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [436/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [436/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [437/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [437/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [438/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [438/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [439/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [439/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [440/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [440/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [441/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [441/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [442/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [442/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [443/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [443/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [444/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [444/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [445/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [445/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [446/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [446/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [447/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [447/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [448/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [448/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [449/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [449/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [450/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [450/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [451/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [451/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [452/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [452/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [453/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [453/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [454/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [454/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [455/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [455/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [456/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [456/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [457/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [457/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [458/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [458/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [459/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [459/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [460/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [460/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [461/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [461/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [462/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [462/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [463/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [463/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [464/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [464/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [465/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [465/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [466/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [466/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [467/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [467/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [468/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [468/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [469/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [469/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [470/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [470/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [471/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [471/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [472/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [472/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [473/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [473/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [474/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [474/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [475/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [475/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [476/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [476/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [477/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [477/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [478/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [478/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [479/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [479/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [480/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [480/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [481/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [481/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [482/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [482/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [483/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [483/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [484/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [484/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [485/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [485/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [486/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [486/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [487/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [487/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [488/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [488/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [489/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [489/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [490/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [490/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [491/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [491/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [492/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [492/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [493/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [493/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [494/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [494/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [495/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [495/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [496/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [496/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [497/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [497/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [498/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [498/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [499/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [499/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [500/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [500/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [501/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [501/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [502/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [502/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [503/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [503/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [504/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [504/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [505/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [505/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [506/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [506/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [507/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [507/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [508/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [508/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [509/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [509/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [510/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [510/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [511/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [511/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [512/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [512/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [513/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [513/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [514/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [514/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [515/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [515/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [516/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [516/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [517/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [517/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [518/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [518/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [519/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [519/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [520/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [520/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [521/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [521/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [522/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [522/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [523/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [523/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [524/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [524/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [525/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [525/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [526/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [526/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [527/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [527/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [528/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [528/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [529/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [529/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [530/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [530/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [531/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [531/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [532/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [532/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [533/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [533/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [534/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [534/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [535/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [535/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [536/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [536/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [537/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [537/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [538/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [538/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [539/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [539/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [540/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [540/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [541/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [541/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [542/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [542/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [543/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [543/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [544/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [544/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [545/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [545/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [546/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [546/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [547/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [547/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [548/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [548/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [549/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [549/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [550/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [550/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [551/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [551/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [552/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [552/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [553/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [553/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [554/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [554/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [555/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [555/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [556/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [556/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [557/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [557/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [558/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [558/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [559/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [559/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [560/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [560/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [561/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [561/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [562/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [562/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [563/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [563/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [564/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [564/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [565/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [565/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [566/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [566/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [567/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [567/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [568/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [568/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [569/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [569/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [570/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [570/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [571/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [571/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [572/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [572/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [573/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [573/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [574/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [574/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [575/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [575/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [576/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [576/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [577/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [577/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [578/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [578/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [579/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [579/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [580/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [580/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [581/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [581/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [582/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [582/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [583/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [583/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [584/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [584/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [585/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [585/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [586/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [586/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [587/650], Train Loss: 0.0121, Train L1 Loss: 0.7340
Epoch [587/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [588/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [588/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [589/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [589/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [590/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [590/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [591/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [591/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [592/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [592/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [593/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [593/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [594/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [594/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [595/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [595/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [596/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [596/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [597/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [597/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [598/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [598/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [599/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [599/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [600/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [600/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [601/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [601/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [602/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [602/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [603/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [603/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [604/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [604/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [605/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [605/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [606/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [606/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [607/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [607/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [608/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [608/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [609/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [609/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [610/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [610/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [611/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [611/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [612/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [612/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [613/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [613/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [614/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [614/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [615/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [615/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [616/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [616/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [617/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [617/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [618/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [618/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [619/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [619/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [620/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [620/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [621/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [621/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [622/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [622/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [623/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [623/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [624/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [624/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [625/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [625/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [626/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [626/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [627/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [627/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [628/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [628/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [629/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [629/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [630/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [630/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [631/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [631/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [632/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [632/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [633/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [633/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [634/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [634/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [635/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [635/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [636/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [636/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [637/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [637/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [638/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [638/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [639/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [639/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [640/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [640/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [641/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [641/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [642/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [642/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [643/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [643/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [644/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [644/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [645/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [645/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [646/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [646/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [647/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [647/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [648/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [648/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [649/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [649/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
Epoch [650/650], Train Loss: 0.0121, Train L1 Loss: 0.7339
Epoch [650/650], Validation Loss: 0.0205, Validation L1: 0.9567, Smoothed Validation Loss: 0.0205
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19686786: <fixWorkingSetup_11> in cluster <dcc> Done

Job <fixWorkingSetup_11> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Mon Dec  4 14:17:58 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Tue Dec  5 10:17:28 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Tue Dec  5 10:17:28 2023
Terminated at Tue Dec  5 20:20:17 2023
Results reported at Tue Dec  5 20:20:17 2023

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

    CPU time :                                   36482.21 sec.
    Max Memory :                                 1940 MB
    Average Memory :                             1931.15 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63596.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   36172 sec.
    Turnaround time :                            108139 sec.

The output (if any) is above this job summary.

