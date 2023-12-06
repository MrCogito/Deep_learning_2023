
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
| <c>name</c>       | <d>str</d>        | <j>"6WorkingSetup-0"</j> |
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
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231202_230757-tuz7594g
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run 6WorkingSetup-0
wandb: ⭐️ View project at https://wandb.ai/deeplearning_painn/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/tuz7594g
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 120 
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:11,903] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 126 
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7f4154d07a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 126, in <listcomp>
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:16,522] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpolqaoktb.py line 218 
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:25,844] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpolqaoktb.py line 117 
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:26,341] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpolqaoktb.py line 90 
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:26,514] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 53 
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:27,041] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:29,967] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 87 
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:31,049] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 94 
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] 
[2023-12-02 23:08:32,038] torch._dynamo.convert_frame: [WARNING] 
wandb: Network error (ReadTimeout), entering retry loop.
wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.005 MB uploadedwandb: / 0.117 MB of 0.117 MB uploadedwandb: - 0.117 MB of 0.117 MB uploadedwandb: \ 0.117 MB of 0.117 MB uploadedwandb:                                                                                
wandb: 
wandb: Run history:
wandb: smoothed val loss █▃▃▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:     train l1 loss █▇▇▅▄▄▃▃▃▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:        train_loss █▆▇▄▄▃▃▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:       val l1 loss █▅▆▄▄▄▄▄▃▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          val loss █▅▆▃▃▂▃▂▂▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb: smoothed val loss 0.02229
wandb:     train l1 loss 0.78153
wandb:        train_loss 0.01375
wandb:       val l1 loss 0.94143
wandb:          val loss 0.02229
wandb: 
wandb: 🚀 View run 6WorkingSetup-0 at: https://wandb.ai/deeplearning_painn/deeplearning_painn/runs/tuz7594g
wandb: ️⚡ View job at https://wandb.ai/deeplearning_painn/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjEyMDA0MzI5Ng==/version_details/v0
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231202_230757-tuz7594g/logs
Epoch [1/650], Train Loss: 0.1668, Train L1 Loss: 2.0352
Epoch [1/650], Validation Loss: 0.1021, Validation L1: 2.2521, Smoothed Validation Loss: 0.1021
Epoch [2/650], Train Loss: 0.0594, Train L1 Loss: 1.5541
Epoch [2/650], Validation Loss: 0.0733, Validation L1: 1.7803, Smoothed Validation Loss: 0.0992
Epoch [3/650], Train Loss: 0.0554, Train L1 Loss: 1.5002
Epoch [3/650], Validation Loss: 0.0820, Validation L1: 1.9531, Smoothed Validation Loss: 0.0975
Epoch [4/650], Train Loss: 0.0523, Train L1 Loss: 1.4545
Epoch [4/650], Validation Loss: 0.0912, Validation L1: 2.1246, Smoothed Validation Loss: 0.0968
Epoch [5/650], Train Loss: 0.0497, Train L1 Loss: 1.4153
Epoch [5/650], Validation Loss: 0.0537, Validation L1: 1.4967, Smoothed Validation Loss: 0.0925
Epoch [6/650], Train Loss: 0.0475, Train L1 Loss: 1.3817
Epoch [6/650], Validation Loss: 0.0394, Validation L1: 1.2580, Smoothed Validation Loss: 0.0872
Epoch [7/650], Train Loss: 0.0456, Train L1 Loss: 1.3507
Epoch [7/650], Validation Loss: 0.0380, Validation L1: 1.2330, Smoothed Validation Loss: 0.0823
Epoch [8/650], Train Loss: 0.0430, Train L1 Loss: 1.3122
Epoch [8/650], Validation Loss: 0.0404, Validation L1: 1.2883, Smoothed Validation Loss: 0.0781
Epoch [9/650], Train Loss: 0.0416, Train L1 Loss: 1.2937
Epoch [9/650], Validation Loss: 0.0412, Validation L1: 1.3173, Smoothed Validation Loss: 0.0744
Epoch [10/650], Train Loss: 0.0405, Train L1 Loss: 1.2759
Epoch [10/650], Validation Loss: 0.0336, Validation L1: 1.1684, Smoothed Validation Loss: 0.0703
Epoch [11/650], Train Loss: 0.0388, Train L1 Loss: 1.2517
Epoch [11/650], Validation Loss: 0.0324, Validation L1: 1.1533, Smoothed Validation Loss: 0.0665
Epoch [12/650], Train Loss: 0.0378, Train L1 Loss: 1.2356
Epoch [12/650], Validation Loss: 0.0327, Validation L1: 1.1633, Smoothed Validation Loss: 0.0632
Epoch [13/650], Train Loss: 0.0371, Train L1 Loss: 1.2249
Epoch [13/650], Validation Loss: 0.0336, Validation L1: 1.1632, Smoothed Validation Loss: 0.0602
Epoch [14/650], Train Loss: 0.0388, Train L1 Loss: 1.2506
Epoch [14/650], Validation Loss: 0.0330, Validation L1: 1.1635, Smoothed Validation Loss: 0.0575
Epoch [15/650], Train Loss: 0.0353, Train L1 Loss: 1.1967
Epoch [15/650], Validation Loss: 0.0298, Validation L1: 1.1050, Smoothed Validation Loss: 0.0547
Epoch [16/650], Train Loss: 0.0374, Train L1 Loss: 1.2273
Epoch [16/650], Validation Loss: 0.0333, Validation L1: 1.1589, Smoothed Validation Loss: 0.0526
Epoch [17/650], Train Loss: 0.0354, Train L1 Loss: 1.1942
Epoch [17/650], Validation Loss: 0.0291, Validation L1: 1.0856, Smoothed Validation Loss: 0.0502
Epoch [18/650], Train Loss: 0.0344, Train L1 Loss: 1.1756
Epoch [18/650], Validation Loss: 0.0320, Validation L1: 1.1314, Smoothed Validation Loss: 0.0484
Epoch [19/650], Train Loss: 0.0387, Train L1 Loss: 1.2207
Epoch [19/650], Validation Loss: 0.0427, Validation L1: 1.3405, Smoothed Validation Loss: 0.0478
Epoch [20/650], Train Loss: 0.0420, Train L1 Loss: 1.2867
Epoch [20/650], Validation Loss: 0.0336, Validation L1: 1.1844, Smoothed Validation Loss: 0.0464
Epoch [21/650], Train Loss: 0.0379, Train L1 Loss: 1.2254
Epoch [21/650], Validation Loss: 0.0307, Validation L1: 1.1162, Smoothed Validation Loss: 0.0448
Epoch [22/650], Train Loss: 0.0363, Train L1 Loss: 1.1993
Epoch [22/650], Validation Loss: 0.0315, Validation L1: 1.1273, Smoothed Validation Loss: 0.0435
Epoch [23/650], Train Loss: 0.0352, Train L1 Loss: 1.1841
Epoch [23/650], Validation Loss: 0.0317, Validation L1: 1.1260, Smoothed Validation Loss: 0.0423
Epoch [24/650], Train Loss: 0.0367, Train L1 Loss: 1.2058
Epoch [24/650], Validation Loss: 0.0316, Validation L1: 1.1321, Smoothed Validation Loss: 0.0413
Epoch [25/650], Train Loss: 0.0416, Train L1 Loss: 1.2634
Epoch [25/650], Validation Loss: 0.0408, Validation L1: 1.2996, Smoothed Validation Loss: 0.0412
Epoch [26/650], Train Loss: 0.0387, Train L1 Loss: 1.2422
Epoch [26/650], Validation Loss: 0.0348, Validation L1: 1.2192, Smoothed Validation Loss: 0.0406
Epoch [27/650], Train Loss: 0.0355, Train L1 Loss: 1.1894
Epoch [27/650], Validation Loss: 0.0315, Validation L1: 1.1512, Smoothed Validation Loss: 0.0397
Epoch [28/650], Train Loss: 0.0363, Train L1 Loss: 1.2056
Epoch [28/650], Validation Loss: 0.0331, Validation L1: 1.1630, Smoothed Validation Loss: 0.0390
Epoch [29/650], Train Loss: 0.0354, Train L1 Loss: 1.1884
Epoch [29/650], Validation Loss: 0.0307, Validation L1: 1.1386, Smoothed Validation Loss: 0.0382
Epoch [30/650], Train Loss: 0.0359, Train L1 Loss: 1.1956
Epoch [30/650], Validation Loss: 0.0355, Validation L1: 1.2347, Smoothed Validation Loss: 0.0379
Epoch [31/650], Train Loss: 0.0339, Train L1 Loss: 1.1615
Epoch [31/650], Validation Loss: 0.0295, Validation L1: 1.1210, Smoothed Validation Loss: 0.0371
Epoch [32/650], Train Loss: 0.0338, Train L1 Loss: 1.1722
Epoch [32/650], Validation Loss: 0.0309, Validation L1: 1.1257, Smoothed Validation Loss: 0.0364
Epoch [33/650], Train Loss: 0.0342, Train L1 Loss: 1.1772
Epoch [33/650], Validation Loss: 0.0340, Validation L1: 1.1928, Smoothed Validation Loss: 0.0362
Epoch [34/650], Train Loss: 0.0421, Train L1 Loss: 1.2737
Epoch [34/650], Validation Loss: 0.0359, Validation L1: 1.2577, Smoothed Validation Loss: 0.0362
Epoch [35/650], Train Loss: 0.0363, Train L1 Loss: 1.1995
Epoch [35/650], Validation Loss: 0.0312, Validation L1: 1.1589, Smoothed Validation Loss: 0.0357
Epoch [36/650], Train Loss: 0.0354, Train L1 Loss: 1.1851
Epoch [36/650], Validation Loss: 0.0323, Validation L1: 1.2070, Smoothed Validation Loss: 0.0353
Epoch [37/650], Train Loss: 0.0352, Train L1 Loss: 1.1917
Epoch [37/650], Validation Loss: 0.0327, Validation L1: 1.1701, Smoothed Validation Loss: 0.0351
Epoch [38/650], Train Loss: 0.0347, Train L1 Loss: 1.1671
Epoch [38/650], Validation Loss: 0.0302, Validation L1: 1.1528, Smoothed Validation Loss: 0.0346
Epoch [39/650], Train Loss: 0.0344, Train L1 Loss: 1.1790
Epoch [39/650], Validation Loss: 0.0338, Validation L1: 1.1552, Smoothed Validation Loss: 0.0345
Epoch [40/650], Train Loss: 0.0370, Train L1 Loss: 1.2093
Epoch [40/650], Validation Loss: 0.0346, Validation L1: 1.2112, Smoothed Validation Loss: 0.0345
Epoch [41/650], Train Loss: 0.0346, Train L1 Loss: 1.1812
Epoch [41/650], Validation Loss: 0.0317, Validation L1: 1.1708, Smoothed Validation Loss: 0.0342
Epoch [42/650], Train Loss: 0.0327, Train L1 Loss: 1.1512
Epoch [42/650], Validation Loss: 0.0325, Validation L1: 1.2282, Smoothed Validation Loss: 0.0341
Epoch [43/650], Train Loss: 0.0342, Train L1 Loss: 1.1560
Epoch [43/650], Validation Loss: 0.0308, Validation L1: 1.1728, Smoothed Validation Loss: 0.0337
Epoch [44/650], Train Loss: 0.0323, Train L1 Loss: 1.1293
Epoch [44/650], Validation Loss: 0.0295, Validation L1: 1.1314, Smoothed Validation Loss: 0.0333
Epoch [45/650], Train Loss: 0.0317, Train L1 Loss: 1.1268
Epoch [45/650], Validation Loss: 0.0300, Validation L1: 1.1430, Smoothed Validation Loss: 0.0330
Epoch [46/650], Train Loss: 0.0339, Train L1 Loss: 1.1668
Epoch [46/650], Validation Loss: 0.0344, Validation L1: 1.1993, Smoothed Validation Loss: 0.0331
Epoch [47/650], Train Loss: 0.0356, Train L1 Loss: 1.1838
Epoch [47/650], Validation Loss: 0.0375, Validation L1: 1.3079, Smoothed Validation Loss: 0.0336
Epoch [48/650], Train Loss: 0.0350, Train L1 Loss: 1.1733
Epoch [48/650], Validation Loss: 0.0364, Validation L1: 1.2406, Smoothed Validation Loss: 0.0338
Epoch [49/650], Train Loss: 0.0339, Train L1 Loss: 1.1702
Epoch [49/650], Validation Loss: 0.0324, Validation L1: 1.2175, Smoothed Validation Loss: 0.0337
Epoch [50/650], Train Loss: 0.0352, Train L1 Loss: 1.1676
Epoch [50/650], Validation Loss: 0.0315, Validation L1: 1.1772, Smoothed Validation Loss: 0.0335
Epoch [51/650], Train Loss: 0.0315, Train L1 Loss: 1.1190
Epoch [51/650], Validation Loss: 0.0307, Validation L1: 1.1806, Smoothed Validation Loss: 0.0332
Epoch 00051: reducing learning rate of group 0 to 5.0000e-04.
Epoch [52/650], Train Loss: 0.0284, Train L1 Loss: 1.0679
Epoch [52/650], Validation Loss: 0.0296, Validation L1: 1.1570, Smoothed Validation Loss: 0.0328
Epoch [53/650], Train Loss: 0.0273, Train L1 Loss: 1.0568
Epoch [53/650], Validation Loss: 0.0300, Validation L1: 1.1725, Smoothed Validation Loss: 0.0326
Epoch [54/650], Train Loss: 0.0273, Train L1 Loss: 1.0619
Epoch [54/650], Validation Loss: 0.0299, Validation L1: 1.1636, Smoothed Validation Loss: 0.0323
Epoch [55/650], Train Loss: 0.0268, Train L1 Loss: 1.0569
Epoch [55/650], Validation Loss: 0.0291, Validation L1: 1.1558, Smoothed Validation Loss: 0.0320
Epoch [56/650], Train Loss: 0.0270, Train L1 Loss: 1.0588
Epoch [56/650], Validation Loss: 0.0278, Validation L1: 1.1136, Smoothed Validation Loss: 0.0316
Epoch [57/650], Train Loss: 0.0259, Train L1 Loss: 1.0446
Epoch [57/650], Validation Loss: 0.0290, Validation L1: 1.1462, Smoothed Validation Loss: 0.0313
Epoch [58/650], Train Loss: 0.0276, Train L1 Loss: 1.0631
Epoch [58/650], Validation Loss: 0.0281, Validation L1: 1.1197, Smoothed Validation Loss: 0.0310
Epoch [59/650], Train Loss: 0.0269, Train L1 Loss: 1.0483
Epoch [59/650], Validation Loss: 0.0296, Validation L1: 1.1669, Smoothed Validation Loss: 0.0308
Epoch [60/650], Train Loss: 0.0265, Train L1 Loss: 1.0485
Epoch [60/650], Validation Loss: 0.0287, Validation L1: 1.1419, Smoothed Validation Loss: 0.0306
Epoch [61/650], Train Loss: 0.0259, Train L1 Loss: 1.0422
Epoch [61/650], Validation Loss: 0.0289, Validation L1: 1.1506, Smoothed Validation Loss: 0.0305
Epoch [62/650], Train Loss: 0.0250, Train L1 Loss: 1.0293
Epoch [62/650], Validation Loss: 0.0296, Validation L1: 1.1761, Smoothed Validation Loss: 0.0304
Epoch [63/650], Train Loss: 0.0257, Train L1 Loss: 1.0402
Epoch [63/650], Validation Loss: 0.0289, Validation L1: 1.1599, Smoothed Validation Loss: 0.0302
Epoch [64/650], Train Loss: 0.0253, Train L1 Loss: 1.0250
Epoch [64/650], Validation Loss: 0.0303, Validation L1: 1.1818, Smoothed Validation Loss: 0.0302
Epoch [65/650], Train Loss: 0.0257, Train L1 Loss: 1.0205
Epoch [65/650], Validation Loss: 0.0288, Validation L1: 1.1560, Smoothed Validation Loss: 0.0301
Epoch [66/650], Train Loss: 0.0254, Train L1 Loss: 1.0260
Epoch [66/650], Validation Loss: 0.0271, Validation L1: 1.1106, Smoothed Validation Loss: 0.0298
Epoch [67/650], Train Loss: 0.0246, Train L1 Loss: 1.0176
Epoch [67/650], Validation Loss: 0.0283, Validation L1: 1.1474, Smoothed Validation Loss: 0.0296
Epoch [68/650], Train Loss: 0.0244, Train L1 Loss: 1.0138
Epoch [68/650], Validation Loss: 0.0283, Validation L1: 1.1497, Smoothed Validation Loss: 0.0295
Epoch [69/650], Train Loss: 0.0240, Train L1 Loss: 1.0101
Epoch [69/650], Validation Loss: 0.0292, Validation L1: 1.1679, Smoothed Validation Loss: 0.0295
Epoch [70/650], Train Loss: 0.0252, Train L1 Loss: 1.0202
Epoch [70/650], Validation Loss: 0.0284, Validation L1: 1.1479, Smoothed Validation Loss: 0.0294
Epoch [71/650], Train Loss: 0.0244, Train L1 Loss: 1.0171
Epoch [71/650], Validation Loss: 0.0268, Validation L1: 1.0907, Smoothed Validation Loss: 0.0291
Epoch [72/650], Train Loss: 0.0253, Train L1 Loss: 1.0255
Epoch [72/650], Validation Loss: 0.0271, Validation L1: 1.0957, Smoothed Validation Loss: 0.0289
Epoch [73/650], Train Loss: 0.0249, Train L1 Loss: 1.0203
Epoch [73/650], Validation Loss: 0.0277, Validation L1: 1.1318, Smoothed Validation Loss: 0.0288
Epoch [74/650], Train Loss: 0.0239, Train L1 Loss: 1.0078
Epoch [74/650], Validation Loss: 0.0280, Validation L1: 1.1366, Smoothed Validation Loss: 0.0287
Epoch [75/650], Train Loss: 0.0236, Train L1 Loss: 1.0041
Epoch [75/650], Validation Loss: 0.0278, Validation L1: 1.1283, Smoothed Validation Loss: 0.0286
Epoch [76/650], Train Loss: 0.0240, Train L1 Loss: 1.0087
Epoch [76/650], Validation Loss: 0.0276, Validation L1: 1.1079, Smoothed Validation Loss: 0.0285
Epoch [77/650], Train Loss: 0.0234, Train L1 Loss: 1.0013
Epoch [77/650], Validation Loss: 0.0276, Validation L1: 1.1181, Smoothed Validation Loss: 0.0284
Epoch [78/650], Train Loss: 0.0232, Train L1 Loss: 0.9970
Epoch [78/650], Validation Loss: 0.0283, Validation L1: 1.1297, Smoothed Validation Loss: 0.0284
Epoch [79/650], Train Loss: 0.0231, Train L1 Loss: 0.9939
Epoch [79/650], Validation Loss: 0.0281, Validation L1: 1.1473, Smoothed Validation Loss: 0.0284
Epoch [80/650], Train Loss: 0.0229, Train L1 Loss: 0.9910
Epoch [80/650], Validation Loss: 0.0288, Validation L1: 1.1537, Smoothed Validation Loss: 0.0284
Epoch [81/650], Train Loss: 0.0224, Train L1 Loss: 0.9838
Epoch [81/650], Validation Loss: 0.0277, Validation L1: 1.1295, Smoothed Validation Loss: 0.0283
Epoch [82/650], Train Loss: 0.0225, Train L1 Loss: 0.9848
Epoch [82/650], Validation Loss: 0.0279, Validation L1: 1.1418, Smoothed Validation Loss: 0.0283
Epoch [83/650], Train Loss: 0.0225, Train L1 Loss: 0.9847
Epoch [83/650], Validation Loss: 0.0283, Validation L1: 1.1531, Smoothed Validation Loss: 0.0283
Epoch [84/650], Train Loss: 0.0220, Train L1 Loss: 0.9783
Epoch [84/650], Validation Loss: 0.0279, Validation L1: 1.1359, Smoothed Validation Loss: 0.0283
Epoch [85/650], Train Loss: 0.0217, Train L1 Loss: 0.9715
Epoch [85/650], Validation Loss: 0.0273, Validation L1: 1.1175, Smoothed Validation Loss: 0.0282
Epoch [86/650], Train Loss: 0.0215, Train L1 Loss: 0.9671
Epoch [86/650], Validation Loss: 0.0272, Validation L1: 1.1169, Smoothed Validation Loss: 0.0281
Epoch [87/650], Train Loss: 0.0221, Train L1 Loss: 0.9798
Epoch [87/650], Validation Loss: 0.0279, Validation L1: 1.1358, Smoothed Validation Loss: 0.0281
Epoch [88/650], Train Loss: 0.0231, Train L1 Loss: 0.9957
Epoch [88/650], Validation Loss: 0.0255, Validation L1: 1.0665, Smoothed Validation Loss: 0.0278
Epoch [89/650], Train Loss: 0.0222, Train L1 Loss: 0.9785
Epoch [89/650], Validation Loss: 0.0257, Validation L1: 1.0754, Smoothed Validation Loss: 0.0276
Epoch [90/650], Train Loss: 0.0224, Train L1 Loss: 0.9772
Epoch [90/650], Validation Loss: 0.0254, Validation L1: 1.0560, Smoothed Validation Loss: 0.0274
Epoch [91/650], Train Loss: 0.0216, Train L1 Loss: 0.9699
Epoch [91/650], Validation Loss: 0.0264, Validation L1: 1.0909, Smoothed Validation Loss: 0.0273
Epoch [92/650], Train Loss: 0.0211, Train L1 Loss: 0.9600
Epoch [92/650], Validation Loss: 0.0266, Validation L1: 1.0994, Smoothed Validation Loss: 0.0272
Epoch [93/650], Train Loss: 0.0212, Train L1 Loss: 0.9623
Epoch [93/650], Validation Loss: 0.0269, Validation L1: 1.1015, Smoothed Validation Loss: 0.0272
Epoch [94/650], Train Loss: 0.0212, Train L1 Loss: 0.9620
Epoch [94/650], Validation Loss: 0.0268, Validation L1: 1.0954, Smoothed Validation Loss: 0.0271
Epoch [95/650], Train Loss: 0.0221, Train L1 Loss: 0.9765
Epoch [95/650], Validation Loss: 0.0268, Validation L1: 1.0944, Smoothed Validation Loss: 0.0271
Epoch [96/650], Train Loss: 0.0225, Train L1 Loss: 0.9823
Epoch [96/650], Validation Loss: 0.0251, Validation L1: 1.0429, Smoothed Validation Loss: 0.0269
Epoch [97/650], Train Loss: 0.0217, Train L1 Loss: 0.9681
Epoch [97/650], Validation Loss: 0.0260, Validation L1: 1.0693, Smoothed Validation Loss: 0.0268
Epoch [98/650], Train Loss: 0.0210, Train L1 Loss: 0.9561
Epoch [98/650], Validation Loss: 0.0270, Validation L1: 1.1038, Smoothed Validation Loss: 0.0268
Epoch [99/650], Train Loss: 0.0210, Train L1 Loss: 0.9519
Epoch [99/650], Validation Loss: 0.0274, Validation L1: 1.1279, Smoothed Validation Loss: 0.0269
Epoch [100/650], Train Loss: 0.0213, Train L1 Loss: 0.9588
Epoch [100/650], Validation Loss: 0.0280, Validation L1: 1.1127, Smoothed Validation Loss: 0.0270
Epoch [101/650], Train Loss: 0.0215, Train L1 Loss: 0.9649
Epoch [101/650], Validation Loss: 0.0264, Validation L1: 1.0813, Smoothed Validation Loss: 0.0269
Epoch [102/650], Train Loss: 0.0218, Train L1 Loss: 0.9681
Epoch [102/650], Validation Loss: 0.0251, Validation L1: 1.0449, Smoothed Validation Loss: 0.0268
Epoch [103/650], Train Loss: 0.0204, Train L1 Loss: 0.9465
Epoch [103/650], Validation Loss: 0.0265, Validation L1: 1.0796, Smoothed Validation Loss: 0.0267
Epoch [104/650], Train Loss: 0.0209, Train L1 Loss: 0.9513
Epoch [104/650], Validation Loss: 0.0264, Validation L1: 1.0856, Smoothed Validation Loss: 0.0267
Epoch [105/650], Train Loss: 0.0216, Train L1 Loss: 0.9671
Epoch [105/650], Validation Loss: 0.0263, Validation L1: 1.0790, Smoothed Validation Loss: 0.0266
Epoch [106/650], Train Loss: 0.0205, Train L1 Loss: 0.9447
Epoch [106/650], Validation Loss: 0.0265, Validation L1: 1.1042, Smoothed Validation Loss: 0.0266
Epoch [107/650], Train Loss: 0.0215, Train L1 Loss: 0.9610
Epoch [107/650], Validation Loss: 0.0286, Validation L1: 1.1490, Smoothed Validation Loss: 0.0268
Epoch [108/650], Train Loss: 0.0207, Train L1 Loss: 0.9539
Epoch [108/650], Validation Loss: 0.0252, Validation L1: 1.0542, Smoothed Validation Loss: 0.0267
Epoch [109/650], Train Loss: 0.0231, Train L1 Loss: 0.9838
Epoch [109/650], Validation Loss: 0.0243, Validation L1: 1.0114, Smoothed Validation Loss: 0.0264
Epoch [110/650], Train Loss: 0.0207, Train L1 Loss: 0.9481
Epoch [110/650], Validation Loss: 0.0249, Validation L1: 1.0542, Smoothed Validation Loss: 0.0263
Epoch [111/650], Train Loss: 0.0211, Train L1 Loss: 0.9543
Epoch [111/650], Validation Loss: 0.0252, Validation L1: 1.0448, Smoothed Validation Loss: 0.0262
Epoch [112/650], Train Loss: 0.0203, Train L1 Loss: 0.9429
Epoch [112/650], Validation Loss: 0.0260, Validation L1: 1.0724, Smoothed Validation Loss: 0.0262
Epoch [113/650], Train Loss: 0.0202, Train L1 Loss: 0.9402
Epoch [113/650], Validation Loss: 0.0265, Validation L1: 1.0760, Smoothed Validation Loss: 0.0262
Epoch [114/650], Train Loss: 0.0205, Train L1 Loss: 0.9437
Epoch [114/650], Validation Loss: 0.0255, Validation L1: 1.0682, Smoothed Validation Loss: 0.0261
Epoch [115/650], Train Loss: 0.0204, Train L1 Loss: 0.9449
Epoch [115/650], Validation Loss: 0.0275, Validation L1: 1.1009, Smoothed Validation Loss: 0.0263
Epoch [116/650], Train Loss: 0.0205, Train L1 Loss: 0.9462
Epoch [116/650], Validation Loss: 0.0263, Validation L1: 1.0901, Smoothed Validation Loss: 0.0263
Epoch [117/650], Train Loss: 0.0195, Train L1 Loss: 0.9288
Epoch [117/650], Validation Loss: 0.0257, Validation L1: 1.0795, Smoothed Validation Loss: 0.0262
Epoch [118/650], Train Loss: 0.0199, Train L1 Loss: 0.9364
Epoch [118/650], Validation Loss: 0.0261, Validation L1: 1.0875, Smoothed Validation Loss: 0.0262
Epoch [119/650], Train Loss: 0.0200, Train L1 Loss: 0.9306
Epoch [119/650], Validation Loss: 0.0260, Validation L1: 1.0817, Smoothed Validation Loss: 0.0262
Epoch [120/650], Train Loss: 0.0195, Train L1 Loss: 0.9250
Epoch [120/650], Validation Loss: 0.0255, Validation L1: 1.0744, Smoothed Validation Loss: 0.0261
Epoch [121/650], Train Loss: 0.0191, Train L1 Loss: 0.9204
Epoch [121/650], Validation Loss: 0.0254, Validation L1: 1.0626, Smoothed Validation Loss: 0.0260
Epoch [122/650], Train Loss: 0.0194, Train L1 Loss: 0.9269
Epoch [122/650], Validation Loss: 0.0252, Validation L1: 1.0476, Smoothed Validation Loss: 0.0260
Epoch [123/650], Train Loss: 0.0190, Train L1 Loss: 0.9183
Epoch [123/650], Validation Loss: 0.0259, Validation L1: 1.0729, Smoothed Validation Loss: 0.0260
Epoch [124/650], Train Loss: 0.0193, Train L1 Loss: 0.9232
Epoch [124/650], Validation Loss: 0.0259, Validation L1: 1.0767, Smoothed Validation Loss: 0.0260
Epoch [125/650], Train Loss: 0.0192, Train L1 Loss: 0.9217
Epoch [125/650], Validation Loss: 0.0250, Validation L1: 1.0519, Smoothed Validation Loss: 0.0259
Epoch [126/650], Train Loss: 0.0197, Train L1 Loss: 0.9317
Epoch [126/650], Validation Loss: 0.0261, Validation L1: 1.0821, Smoothed Validation Loss: 0.0259
Epoch [127/650], Train Loss: 0.0191, Train L1 Loss: 0.9203
Epoch [127/650], Validation Loss: 0.0242, Validation L1: 1.0338, Smoothed Validation Loss: 0.0257
Epoch [128/650], Train Loss: 0.0187, Train L1 Loss: 0.9115
Epoch [128/650], Validation Loss: 0.0249, Validation L1: 1.0440, Smoothed Validation Loss: 0.0256
Epoch [129/650], Train Loss: 0.0187, Train L1 Loss: 0.9130
Epoch [129/650], Validation Loss: 0.0244, Validation L1: 1.0319, Smoothed Validation Loss: 0.0255
Epoch [130/650], Train Loss: 0.0190, Train L1 Loss: 0.9180
Epoch [130/650], Validation Loss: 0.0247, Validation L1: 1.0385, Smoothed Validation Loss: 0.0254
Epoch [131/650], Train Loss: 0.0190, Train L1 Loss: 0.9185
Epoch [131/650], Validation Loss: 0.0235, Validation L1: 1.0000, Smoothed Validation Loss: 0.0252
Epoch [132/650], Train Loss: 0.0186, Train L1 Loss: 0.9104
Epoch [132/650], Validation Loss: 0.0245, Validation L1: 1.0311, Smoothed Validation Loss: 0.0252
Epoch [133/650], Train Loss: 0.0186, Train L1 Loss: 0.9095
Epoch [133/650], Validation Loss: 0.0258, Validation L1: 1.0556, Smoothed Validation Loss: 0.0252
Epoch [134/650], Train Loss: 0.0184, Train L1 Loss: 0.9063
Epoch [134/650], Validation Loss: 0.0282, Validation L1: 1.0788, Smoothed Validation Loss: 0.0255
Epoch [135/650], Train Loss: 0.0183, Train L1 Loss: 0.9042
Epoch [135/650], Validation Loss: 0.0253, Validation L1: 1.0569, Smoothed Validation Loss: 0.0255
Epoch [136/650], Train Loss: 0.0189, Train L1 Loss: 0.9150
Epoch [136/650], Validation Loss: 0.0245, Validation L1: 1.0293, Smoothed Validation Loss: 0.0254
Epoch [137/650], Train Loss: 0.0183, Train L1 Loss: 0.9041
Epoch [137/650], Validation Loss: 0.0253, Validation L1: 1.0505, Smoothed Validation Loss: 0.0254
Epoch [138/650], Train Loss: 0.0186, Train L1 Loss: 0.9107
Epoch [138/650], Validation Loss: 0.0246, Validation L1: 1.0320, Smoothed Validation Loss: 0.0253
Epoch 00138: reducing learning rate of group 0 to 2.5000e-04.
Epoch [139/650], Train Loss: 0.0173, Train L1 Loss: 0.8803
Epoch [139/650], Validation Loss: 0.0230, Validation L1: 0.9750, Smoothed Validation Loss: 0.0251
Epoch [140/650], Train Loss: 0.0170, Train L1 Loss: 0.8710
Epoch [140/650], Validation Loss: 0.0229, Validation L1: 0.9778, Smoothed Validation Loss: 0.0249
Epoch [141/650], Train Loss: 0.0168, Train L1 Loss: 0.8683
Epoch [141/650], Validation Loss: 0.0231, Validation L1: 0.9801, Smoothed Validation Loss: 0.0247
Epoch [142/650], Train Loss: 0.0167, Train L1 Loss: 0.8653
Epoch [142/650], Validation Loss: 0.0231, Validation L1: 0.9818, Smoothed Validation Loss: 0.0245
Epoch [143/650], Train Loss: 0.0166, Train L1 Loss: 0.8637
Epoch [143/650], Validation Loss: 0.0233, Validation L1: 0.9856, Smoothed Validation Loss: 0.0244
Epoch [144/650], Train Loss: 0.0166, Train L1 Loss: 0.8611
Epoch [144/650], Validation Loss: 0.0234, Validation L1: 0.9881, Smoothed Validation Loss: 0.0243
Epoch [145/650], Train Loss: 0.0165, Train L1 Loss: 0.8600
Epoch [145/650], Validation Loss: 0.0235, Validation L1: 0.9899, Smoothed Validation Loss: 0.0242
Epoch [146/650], Train Loss: 0.0164, Train L1 Loss: 0.8582
Epoch [146/650], Validation Loss: 0.0236, Validation L1: 0.9920, Smoothed Validation Loss: 0.0242
Epoch [147/650], Train Loss: 0.0164, Train L1 Loss: 0.8576
Epoch [147/650], Validation Loss: 0.0237, Validation L1: 0.9926, Smoothed Validation Loss: 0.0241
Epoch [148/650], Train Loss: 0.0164, Train L1 Loss: 0.8565
Epoch [148/650], Validation Loss: 0.0237, Validation L1: 0.9917, Smoothed Validation Loss: 0.0241
Epoch [149/650], Train Loss: 0.0163, Train L1 Loss: 0.8557
Epoch [149/650], Validation Loss: 0.0237, Validation L1: 0.9910, Smoothed Validation Loss: 0.0240
Epoch [150/650], Train Loss: 0.0162, Train L1 Loss: 0.8531
Epoch [150/650], Validation Loss: 0.0238, Validation L1: 0.9931, Smoothed Validation Loss: 0.0240
Epoch [151/650], Train Loss: 0.0162, Train L1 Loss: 0.8520
Epoch [151/650], Validation Loss: 0.0238, Validation L1: 0.9947, Smoothed Validation Loss: 0.0240
Epoch [152/650], Train Loss: 0.0161, Train L1 Loss: 0.8505
Epoch [152/650], Validation Loss: 0.0238, Validation L1: 0.9942, Smoothed Validation Loss: 0.0240
Epoch [153/650], Train Loss: 0.0161, Train L1 Loss: 0.8498
Epoch [153/650], Validation Loss: 0.0239, Validation L1: 0.9969, Smoothed Validation Loss: 0.0240
Epoch [154/650], Train Loss: 0.0160, Train L1 Loss: 0.8481
Epoch [154/650], Validation Loss: 0.0241, Validation L1: 0.9979, Smoothed Validation Loss: 0.0240
Epoch [155/650], Train Loss: 0.0160, Train L1 Loss: 0.8470
Epoch [155/650], Validation Loss: 0.0241, Validation L1: 0.9985, Smoothed Validation Loss: 0.0240
Epoch [156/650], Train Loss: 0.0160, Train L1 Loss: 0.8474
Epoch [156/650], Validation Loss: 0.0243, Validation L1: 1.0010, Smoothed Validation Loss: 0.0240
Epoch [157/650], Train Loss: 0.0159, Train L1 Loss: 0.8466
Epoch [157/650], Validation Loss: 0.0242, Validation L1: 1.0002, Smoothed Validation Loss: 0.0240
Epoch [158/650], Train Loss: 0.0159, Train L1 Loss: 0.8461
Epoch [158/650], Validation Loss: 0.0244, Validation L1: 1.0024, Smoothed Validation Loss: 0.0241
Epoch [159/650], Train Loss: 0.0159, Train L1 Loss: 0.8453
Epoch [159/650], Validation Loss: 0.0243, Validation L1: 1.0026, Smoothed Validation Loss: 0.0241
Epoch 00159: reducing learning rate of group 0 to 1.2500e-04.
Epoch [160/650], Train Loss: 0.0159, Train L1 Loss: 0.8443
Epoch [160/650], Validation Loss: 0.0229, Validation L1: 0.9599, Smoothed Validation Loss: 0.0240
Epoch [161/650], Train Loss: 0.0158, Train L1 Loss: 0.8407
Epoch [161/650], Validation Loss: 0.0229, Validation L1: 0.9590, Smoothed Validation Loss: 0.0239
Epoch [162/650], Train Loss: 0.0156, Train L1 Loss: 0.8352
Epoch [162/650], Validation Loss: 0.0230, Validation L1: 0.9619, Smoothed Validation Loss: 0.0238
Epoch [163/650], Train Loss: 0.0155, Train L1 Loss: 0.8323
Epoch [163/650], Validation Loss: 0.0231, Validation L1: 0.9644, Smoothed Validation Loss: 0.0237
Epoch [164/650], Train Loss: 0.0154, Train L1 Loss: 0.8304
Epoch [164/650], Validation Loss: 0.0231, Validation L1: 0.9650, Smoothed Validation Loss: 0.0237
Epoch [165/650], Train Loss: 0.0153, Train L1 Loss: 0.8287
Epoch [165/650], Validation Loss: 0.0231, Validation L1: 0.9664, Smoothed Validation Loss: 0.0236
Epoch [166/650], Train Loss: 0.0153, Train L1 Loss: 0.8272
Epoch [166/650], Validation Loss: 0.0231, Validation L1: 0.9666, Smoothed Validation Loss: 0.0236
Epoch [167/650], Train Loss: 0.0152, Train L1 Loss: 0.8257
Epoch [167/650], Validation Loss: 0.0231, Validation L1: 0.9672, Smoothed Validation Loss: 0.0235
Epoch [168/650], Train Loss: 0.0152, Train L1 Loss: 0.8249
Epoch [168/650], Validation Loss: 0.0232, Validation L1: 0.9674, Smoothed Validation Loss: 0.0235
Epoch [169/650], Train Loss: 0.0152, Train L1 Loss: 0.8234
Epoch [169/650], Validation Loss: 0.0231, Validation L1: 0.9677, Smoothed Validation Loss: 0.0234
Epoch [170/650], Train Loss: 0.0151, Train L1 Loss: 0.8221
Epoch [170/650], Validation Loss: 0.0232, Validation L1: 0.9689, Smoothed Validation Loss: 0.0234
Epoch [171/650], Train Loss: 0.0151, Train L1 Loss: 0.8208
Epoch [171/650], Validation Loss: 0.0232, Validation L1: 0.9692, Smoothed Validation Loss: 0.0234
Epoch [172/650], Train Loss: 0.0150, Train L1 Loss: 0.8200
Epoch [172/650], Validation Loss: 0.0233, Validation L1: 0.9694, Smoothed Validation Loss: 0.0234
Epoch [173/650], Train Loss: 0.0150, Train L1 Loss: 0.8189
Epoch [173/650], Validation Loss: 0.0233, Validation L1: 0.9699, Smoothed Validation Loss: 0.0234
Epoch [174/650], Train Loss: 0.0150, Train L1 Loss: 0.8177
Epoch [174/650], Validation Loss: 0.0234, Validation L1: 0.9710, Smoothed Validation Loss: 0.0234
Epoch [175/650], Train Loss: 0.0149, Train L1 Loss: 0.8168
Epoch [175/650], Validation Loss: 0.0234, Validation L1: 0.9715, Smoothed Validation Loss: 0.0234
Epoch [176/650], Train Loss: 0.0149, Train L1 Loss: 0.8158
Epoch [176/650], Validation Loss: 0.0234, Validation L1: 0.9717, Smoothed Validation Loss: 0.0234
Epoch [177/650], Train Loss: 0.0149, Train L1 Loss: 0.8152
Epoch [177/650], Validation Loss: 0.0235, Validation L1: 0.9728, Smoothed Validation Loss: 0.0234
Epoch [178/650], Train Loss: 0.0148, Train L1 Loss: 0.8138
Epoch [178/650], Validation Loss: 0.0236, Validation L1: 0.9743, Smoothed Validation Loss: 0.0234
Epoch [179/650], Train Loss: 0.0148, Train L1 Loss: 0.8131
Epoch [179/650], Validation Loss: 0.0237, Validation L1: 0.9743, Smoothed Validation Loss: 0.0234
Epoch 00179: reducing learning rate of group 0 to 6.2500e-05.
Epoch [180/650], Train Loss: 0.0149, Train L1 Loss: 0.8170
Epoch [180/650], Validation Loss: 0.0237, Validation L1: 0.9820, Smoothed Validation Loss: 0.0235
Epoch [181/650], Train Loss: 0.0148, Train L1 Loss: 0.8142
Epoch [181/650], Validation Loss: 0.0236, Validation L1: 0.9806, Smoothed Validation Loss: 0.0235
Epoch [182/650], Train Loss: 0.0148, Train L1 Loss: 0.8118
Epoch [182/650], Validation Loss: 0.0236, Validation L1: 0.9803, Smoothed Validation Loss: 0.0235
Epoch [183/650], Train Loss: 0.0147, Train L1 Loss: 0.8102
Epoch [183/650], Validation Loss: 0.0236, Validation L1: 0.9803, Smoothed Validation Loss: 0.0235
Epoch [184/650], Train Loss: 0.0147, Train L1 Loss: 0.8088
Epoch [184/650], Validation Loss: 0.0236, Validation L1: 0.9803, Smoothed Validation Loss: 0.0235
Epoch [185/650], Train Loss: 0.0146, Train L1 Loss: 0.8077
Epoch [185/650], Validation Loss: 0.0236, Validation L1: 0.9804, Smoothed Validation Loss: 0.0235
Epoch 00185: reducing learning rate of group 0 to 3.1250e-05.
Epoch [186/650], Train Loss: 0.0147, Train L1 Loss: 0.8110
Epoch [186/650], Validation Loss: 0.0227, Validation L1: 0.9517, Smoothed Validation Loss: 0.0234
Epoch [187/650], Train Loss: 0.0147, Train L1 Loss: 0.8089
Epoch [187/650], Validation Loss: 0.0226, Validation L1: 0.9512, Smoothed Validation Loss: 0.0233
Epoch [188/650], Train Loss: 0.0146, Train L1 Loss: 0.8076
Epoch [188/650], Validation Loss: 0.0226, Validation L1: 0.9509, Smoothed Validation Loss: 0.0233
Epoch [189/650], Train Loss: 0.0146, Train L1 Loss: 0.8066
Epoch [189/650], Validation Loss: 0.0226, Validation L1: 0.9507, Smoothed Validation Loss: 0.0232
Epoch [190/650], Train Loss: 0.0146, Train L1 Loss: 0.8057
Epoch [190/650], Validation Loss: 0.0226, Validation L1: 0.9505, Smoothed Validation Loss: 0.0231
Epoch [191/650], Train Loss: 0.0146, Train L1 Loss: 0.8048
Epoch [191/650], Validation Loss: 0.0226, Validation L1: 0.9504, Smoothed Validation Loss: 0.0231
Epoch [192/650], Train Loss: 0.0145, Train L1 Loss: 0.8041
Epoch [192/650], Validation Loss: 0.0226, Validation L1: 0.9503, Smoothed Validation Loss: 0.0230
Epoch [193/650], Train Loss: 0.0145, Train L1 Loss: 0.8034
Epoch [193/650], Validation Loss: 0.0226, Validation L1: 0.9502, Smoothed Validation Loss: 0.0230
Epoch [194/650], Train Loss: 0.0145, Train L1 Loss: 0.8027
Epoch [194/650], Validation Loss: 0.0226, Validation L1: 0.9502, Smoothed Validation Loss: 0.0229
Epoch [195/650], Train Loss: 0.0145, Train L1 Loss: 0.8021
Epoch [195/650], Validation Loss: 0.0226, Validation L1: 0.9502, Smoothed Validation Loss: 0.0229
Epoch [196/650], Train Loss: 0.0144, Train L1 Loss: 0.8015
Epoch [196/650], Validation Loss: 0.0226, Validation L1: 0.9502, Smoothed Validation Loss: 0.0229
Epoch [197/650], Train Loss: 0.0144, Train L1 Loss: 0.8009
Epoch [197/650], Validation Loss: 0.0226, Validation L1: 0.9502, Smoothed Validation Loss: 0.0228
Epoch [198/650], Train Loss: 0.0144, Train L1 Loss: 0.8004
Epoch [198/650], Validation Loss: 0.0226, Validation L1: 0.9502, Smoothed Validation Loss: 0.0228
Epoch [199/650], Train Loss: 0.0144, Train L1 Loss: 0.7998
Epoch [199/650], Validation Loss: 0.0226, Validation L1: 0.9503, Smoothed Validation Loss: 0.0228
Epoch [200/650], Train Loss: 0.0144, Train L1 Loss: 0.7993
Epoch [200/650], Validation Loss: 0.0226, Validation L1: 0.9503, Smoothed Validation Loss: 0.0228
Epoch [201/650], Train Loss: 0.0144, Train L1 Loss: 0.7988
Epoch [201/650], Validation Loss: 0.0226, Validation L1: 0.9504, Smoothed Validation Loss: 0.0227
Epoch [202/650], Train Loss: 0.0143, Train L1 Loss: 0.7983
Epoch [202/650], Validation Loss: 0.0226, Validation L1: 0.9504, Smoothed Validation Loss: 0.0227
Epoch [203/650], Train Loss: 0.0143, Train L1 Loss: 0.7979
Epoch [203/650], Validation Loss: 0.0226, Validation L1: 0.9505, Smoothed Validation Loss: 0.0227
Epoch [204/650], Train Loss: 0.0143, Train L1 Loss: 0.7974
Epoch [204/650], Validation Loss: 0.0226, Validation L1: 0.9505, Smoothed Validation Loss: 0.0227
Epoch [205/650], Train Loss: 0.0143, Train L1 Loss: 0.7969
Epoch [205/650], Validation Loss: 0.0226, Validation L1: 0.9505, Smoothed Validation Loss: 0.0227
Epoch [206/650], Train Loss: 0.0143, Train L1 Loss: 0.7965
Epoch [206/650], Validation Loss: 0.0226, Validation L1: 0.9506, Smoothed Validation Loss: 0.0227
Epoch [207/650], Train Loss: 0.0143, Train L1 Loss: 0.7961
Epoch [207/650], Validation Loss: 0.0226, Validation L1: 0.9506, Smoothed Validation Loss: 0.0227
Epoch [208/650], Train Loss: 0.0143, Train L1 Loss: 0.7956
Epoch [208/650], Validation Loss: 0.0226, Validation L1: 0.9507, Smoothed Validation Loss: 0.0227
Epoch [209/650], Train Loss: 0.0142, Train L1 Loss: 0.7952
Epoch [209/650], Validation Loss: 0.0226, Validation L1: 0.9507, Smoothed Validation Loss: 0.0227
Epoch [210/650], Train Loss: 0.0142, Train L1 Loss: 0.7948
Epoch [210/650], Validation Loss: 0.0226, Validation L1: 0.9508, Smoothed Validation Loss: 0.0227
Epoch [211/650], Train Loss: 0.0142, Train L1 Loss: 0.7944
Epoch [211/650], Validation Loss: 0.0226, Validation L1: 0.9508, Smoothed Validation Loss: 0.0227
Epoch [212/650], Train Loss: 0.0142, Train L1 Loss: 0.7940
Epoch [212/650], Validation Loss: 0.0226, Validation L1: 0.9509, Smoothed Validation Loss: 0.0227
Epoch [213/650], Train Loss: 0.0142, Train L1 Loss: 0.7936
Epoch [213/650], Validation Loss: 0.0226, Validation L1: 0.9510, Smoothed Validation Loss: 0.0226
Epoch [214/650], Train Loss: 0.0142, Train L1 Loss: 0.7932
Epoch [214/650], Validation Loss: 0.0226, Validation L1: 0.9511, Smoothed Validation Loss: 0.0226
Epoch [215/650], Train Loss: 0.0142, Train L1 Loss: 0.7928
Epoch [215/650], Validation Loss: 0.0226, Validation L1: 0.9511, Smoothed Validation Loss: 0.0226
Epoch [216/650], Train Loss: 0.0141, Train L1 Loss: 0.7925
Epoch [216/650], Validation Loss: 0.0226, Validation L1: 0.9512, Smoothed Validation Loss: 0.0226
Epoch [217/650], Train Loss: 0.0141, Train L1 Loss: 0.7921
Epoch [217/650], Validation Loss: 0.0226, Validation L1: 0.9513, Smoothed Validation Loss: 0.0226
Epoch [218/650], Train Loss: 0.0141, Train L1 Loss: 0.7917
Epoch [218/650], Validation Loss: 0.0226, Validation L1: 0.9513, Smoothed Validation Loss: 0.0226
Epoch [219/650], Train Loss: 0.0141, Train L1 Loss: 0.7914
Epoch [219/650], Validation Loss: 0.0226, Validation L1: 0.9514, Smoothed Validation Loss: 0.0226
Epoch [220/650], Train Loss: 0.0141, Train L1 Loss: 0.7910
Epoch [220/650], Validation Loss: 0.0227, Validation L1: 0.9515, Smoothed Validation Loss: 0.0226
Epoch [221/650], Train Loss: 0.0141, Train L1 Loss: 0.7907
Epoch [221/650], Validation Loss: 0.0227, Validation L1: 0.9516, Smoothed Validation Loss: 0.0226
Epoch 00221: reducing learning rate of group 0 to 1.5625e-05.
Epoch [222/650], Train Loss: 0.0141, Train L1 Loss: 0.7930
Epoch [222/650], Validation Loss: 0.0223, Validation L1: 0.9439, Smoothed Validation Loss: 0.0226
Epoch [223/650], Train Loss: 0.0141, Train L1 Loss: 0.7922
Epoch [223/650], Validation Loss: 0.0223, Validation L1: 0.9438, Smoothed Validation Loss: 0.0226
Epoch [224/650], Train Loss: 0.0141, Train L1 Loss: 0.7917
Epoch [224/650], Validation Loss: 0.0223, Validation L1: 0.9437, Smoothed Validation Loss: 0.0226
Epoch [225/650], Train Loss: 0.0141, Train L1 Loss: 0.7913
Epoch [225/650], Validation Loss: 0.0223, Validation L1: 0.9437, Smoothed Validation Loss: 0.0225
Epoch [226/650], Train Loss: 0.0141, Train L1 Loss: 0.7909
Epoch [226/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0225
Epoch [227/650], Train Loss: 0.0141, Train L1 Loss: 0.7906
Epoch [227/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0225
Epoch [228/650], Train Loss: 0.0141, Train L1 Loss: 0.7903
Epoch [228/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0225
Epoch [229/650], Train Loss: 0.0141, Train L1 Loss: 0.7900
Epoch [229/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0225
Epoch [230/650], Train Loss: 0.0140, Train L1 Loss: 0.7897
Epoch [230/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0224
Epoch [231/650], Train Loss: 0.0140, Train L1 Loss: 0.7895
Epoch [231/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0224
Epoch [232/650], Train Loss: 0.0140, Train L1 Loss: 0.7892
Epoch [232/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0224
Epoch [233/650], Train Loss: 0.0140, Train L1 Loss: 0.7890
Epoch [233/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0224
Epoch [234/650], Train Loss: 0.0140, Train L1 Loss: 0.7887
Epoch [234/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0224
Epoch [235/650], Train Loss: 0.0140, Train L1 Loss: 0.7885
Epoch [235/650], Validation Loss: 0.0223, Validation L1: 0.9436, Smoothed Validation Loss: 0.0224
Epoch [236/650], Train Loss: 0.0140, Train L1 Loss: 0.7882
Epoch [236/650], Validation Loss: 0.0223, Validation L1: 0.9437, Smoothed Validation Loss: 0.0224
Epoch [237/650], Train Loss: 0.0140, Train L1 Loss: 0.7880
Epoch [237/650], Validation Loss: 0.0223, Validation L1: 0.9437, Smoothed Validation Loss: 0.0224
Epoch [238/650], Train Loss: 0.0140, Train L1 Loss: 0.7878
Epoch [238/650], Validation Loss: 0.0223, Validation L1: 0.9437, Smoothed Validation Loss: 0.0224
Epoch [239/650], Train Loss: 0.0140, Train L1 Loss: 0.7875
Epoch [239/650], Validation Loss: 0.0223, Validation L1: 0.9437, Smoothed Validation Loss: 0.0224
Epoch [240/650], Train Loss: 0.0140, Train L1 Loss: 0.7873
Epoch [240/650], Validation Loss: 0.0223, Validation L1: 0.9437, Smoothed Validation Loss: 0.0224
Epoch [241/650], Train Loss: 0.0140, Train L1 Loss: 0.7871
Epoch [241/650], Validation Loss: 0.0223, Validation L1: 0.9438, Smoothed Validation Loss: 0.0224
Epoch [242/650], Train Loss: 0.0140, Train L1 Loss: 0.7869
Epoch [242/650], Validation Loss: 0.0223, Validation L1: 0.9438, Smoothed Validation Loss: 0.0224
Epoch [243/650], Train Loss: 0.0139, Train L1 Loss: 0.7867
Epoch [243/650], Validation Loss: 0.0223, Validation L1: 0.9438, Smoothed Validation Loss: 0.0224
Epoch [244/650], Train Loss: 0.0139, Train L1 Loss: 0.7865
Epoch [244/650], Validation Loss: 0.0223, Validation L1: 0.9438, Smoothed Validation Loss: 0.0224
Epoch [245/650], Train Loss: 0.0139, Train L1 Loss: 0.7863
Epoch [245/650], Validation Loss: 0.0223, Validation L1: 0.9438, Smoothed Validation Loss: 0.0223
Epoch [246/650], Train Loss: 0.0139, Train L1 Loss: 0.7861
Epoch [246/650], Validation Loss: 0.0223, Validation L1: 0.9439, Smoothed Validation Loss: 0.0223
Epoch [247/650], Train Loss: 0.0139, Train L1 Loss: 0.7858
Epoch [247/650], Validation Loss: 0.0223, Validation L1: 0.9439, Smoothed Validation Loss: 0.0223
Epoch [248/650], Train Loss: 0.0139, Train L1 Loss: 0.7856
Epoch [248/650], Validation Loss: 0.0223, Validation L1: 0.9439, Smoothed Validation Loss: 0.0223
Epoch [249/650], Train Loss: 0.0139, Train L1 Loss: 0.7854
Epoch [249/650], Validation Loss: 0.0224, Validation L1: 0.9440, Smoothed Validation Loss: 0.0223
Epoch [250/650], Train Loss: 0.0139, Train L1 Loss: 0.7852
Epoch [250/650], Validation Loss: 0.0224, Validation L1: 0.9440, Smoothed Validation Loss: 0.0223
Epoch 00250: reducing learning rate of group 0 to 7.8125e-06.
Epoch [251/650], Train Loss: 0.0139, Train L1 Loss: 0.7869
Epoch [251/650], Validation Loss: 0.0222, Validation L1: 0.9428, Smoothed Validation Loss: 0.0223
Epoch [252/650], Train Loss: 0.0139, Train L1 Loss: 0.7865
Epoch [252/650], Validation Loss: 0.0222, Validation L1: 0.9426, Smoothed Validation Loss: 0.0223
Epoch [253/650], Train Loss: 0.0139, Train L1 Loss: 0.7863
Epoch [253/650], Validation Loss: 0.0222, Validation L1: 0.9425, Smoothed Validation Loss: 0.0223
Epoch [254/650], Train Loss: 0.0139, Train L1 Loss: 0.7861
Epoch [254/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [255/650], Train Loss: 0.0139, Train L1 Loss: 0.7859
Epoch [255/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [256/650], Train Loss: 0.0139, Train L1 Loss: 0.7857
Epoch [256/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [257/650], Train Loss: 0.0139, Train L1 Loss: 0.7855
Epoch [257/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [258/650], Train Loss: 0.0139, Train L1 Loss: 0.7854
Epoch [258/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [259/650], Train Loss: 0.0139, Train L1 Loss: 0.7852
Epoch [259/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [260/650], Train Loss: 0.0139, Train L1 Loss: 0.7851
Epoch [260/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [261/650], Train Loss: 0.0139, Train L1 Loss: 0.7849
Epoch [261/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [262/650], Train Loss: 0.0139, Train L1 Loss: 0.7848
Epoch [262/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0223
Epoch [263/650], Train Loss: 0.0139, Train L1 Loss: 0.7846
Epoch [263/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0222
Epoch [264/650], Train Loss: 0.0139, Train L1 Loss: 0.7845
Epoch [264/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0222
Epoch [265/650], Train Loss: 0.0139, Train L1 Loss: 0.7844
Epoch [265/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0222
Epoch [266/650], Train Loss: 0.0139, Train L1 Loss: 0.7843
Epoch [266/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0222
Epoch [267/650], Train Loss: 0.0139, Train L1 Loss: 0.7841
Epoch [267/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0222
Epoch [268/650], Train Loss: 0.0139, Train L1 Loss: 0.7840
Epoch [268/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0222
Epoch [269/650], Train Loss: 0.0138, Train L1 Loss: 0.7839
Epoch [269/650], Validation Loss: 0.0222, Validation L1: 0.9424, Smoothed Validation Loss: 0.0222
Epoch [270/650], Train Loss: 0.0138, Train L1 Loss: 0.7838
Epoch [270/650], Validation Loss: 0.0222, Validation L1: 0.9425, Smoothed Validation Loss: 0.0222
Epoch [271/650], Train Loss: 0.0138, Train L1 Loss: 0.7836
Epoch [271/650], Validation Loss: 0.0222, Validation L1: 0.9425, Smoothed Validation Loss: 0.0222
Epoch [272/650], Train Loss: 0.0138, Train L1 Loss: 0.7835
Epoch [272/650], Validation Loss: 0.0222, Validation L1: 0.9425, Smoothed Validation Loss: 0.0222
Epoch [273/650], Train Loss: 0.0138, Train L1 Loss: 0.7834
Epoch [273/650], Validation Loss: 0.0222, Validation L1: 0.9425, Smoothed Validation Loss: 0.0222
Epoch [274/650], Train Loss: 0.0138, Train L1 Loss: 0.7833
Epoch [274/650], Validation Loss: 0.0222, Validation L1: 0.9425, Smoothed Validation Loss: 0.0222
Epoch [275/650], Train Loss: 0.0138, Train L1 Loss: 0.7831
Epoch [275/650], Validation Loss: 0.0222, Validation L1: 0.9425, Smoothed Validation Loss: 0.0222
Epoch 00275: reducing learning rate of group 0 to 3.9063e-06.
Epoch [276/650], Train Loss: 0.0138, Train L1 Loss: 0.7842
Epoch [276/650], Validation Loss: 0.0222, Validation L1: 0.9414, Smoothed Validation Loss: 0.0222
Epoch [277/650], Train Loss: 0.0138, Train L1 Loss: 0.7839
Epoch [277/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [278/650], Train Loss: 0.0138, Train L1 Loss: 0.7838
Epoch [278/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [279/650], Train Loss: 0.0138, Train L1 Loss: 0.7837
Epoch [279/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [280/650], Train Loss: 0.0138, Train L1 Loss: 0.7836
Epoch [280/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [281/650], Train Loss: 0.0138, Train L1 Loss: 0.7835
Epoch [281/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [282/650], Train Loss: 0.0138, Train L1 Loss: 0.7834
Epoch [282/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [283/650], Train Loss: 0.0138, Train L1 Loss: 0.7833
Epoch [283/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [284/650], Train Loss: 0.0138, Train L1 Loss: 0.7832
Epoch [284/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [285/650], Train Loss: 0.0138, Train L1 Loss: 0.7831
Epoch [285/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [286/650], Train Loss: 0.0138, Train L1 Loss: 0.7831
Epoch [286/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [287/650], Train Loss: 0.0138, Train L1 Loss: 0.7830
Epoch [287/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [288/650], Train Loss: 0.0138, Train L1 Loss: 0.7829
Epoch [288/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [289/650], Train Loss: 0.0138, Train L1 Loss: 0.7828
Epoch [289/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [290/650], Train Loss: 0.0138, Train L1 Loss: 0.7828
Epoch [290/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [291/650], Train Loss: 0.0138, Train L1 Loss: 0.7827
Epoch [291/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [292/650], Train Loss: 0.0138, Train L1 Loss: 0.7826
Epoch [292/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [293/650], Train Loss: 0.0138, Train L1 Loss: 0.7825
Epoch [293/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [294/650], Train Loss: 0.0138, Train L1 Loss: 0.7825
Epoch [294/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [295/650], Train Loss: 0.0138, Train L1 Loss: 0.7824
Epoch [295/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [296/650], Train Loss: 0.0138, Train L1 Loss: 0.7823
Epoch [296/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [297/650], Train Loss: 0.0138, Train L1 Loss: 0.7823
Epoch [297/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [298/650], Train Loss: 0.0138, Train L1 Loss: 0.7822
Epoch [298/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [299/650], Train Loss: 0.0138, Train L1 Loss: 0.7821
Epoch [299/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [300/650], Train Loss: 0.0138, Train L1 Loss: 0.7821
Epoch [300/650], Validation Loss: 0.0222, Validation L1: 0.9413, Smoothed Validation Loss: 0.0222
Epoch [301/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [301/650], Validation Loss: 0.0222, Validation L1: 0.9414, Smoothed Validation Loss: 0.0222
Epoch [302/650], Train Loss: 0.0138, Train L1 Loss: 0.7819
Epoch [302/650], Validation Loss: 0.0222, Validation L1: 0.9414, Smoothed Validation Loss: 0.0222
Epoch 00302: reducing learning rate of group 0 to 1.9531e-06.
Epoch [303/650], Train Loss: 0.0138, Train L1 Loss: 0.7824
Epoch [303/650], Validation Loss: 0.0222, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [304/650], Train Loss: 0.0138, Train L1 Loss: 0.7823
Epoch [304/650], Validation Loss: 0.0222, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [305/650], Train Loss: 0.0138, Train L1 Loss: 0.7822
Epoch [305/650], Validation Loss: 0.0222, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [306/650], Train Loss: 0.0138, Train L1 Loss: 0.7821
Epoch [306/650], Validation Loss: 0.0222, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [307/650], Train Loss: 0.0138, Train L1 Loss: 0.7821
Epoch [307/650], Validation Loss: 0.0222, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [308/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [308/650], Validation Loss: 0.0222, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch 00308: reducing learning rate of group 0 to 9.7656e-07.
Epoch [309/650], Train Loss: 0.0138, Train L1 Loss: 0.7822
Epoch [309/650], Validation Loss: 0.0222, Validation L1: 0.9404, Smoothed Validation Loss: 0.0222
Epoch [310/650], Train Loss: 0.0138, Train L1 Loss: 0.7821
Epoch [310/650], Validation Loss: 0.0222, Validation L1: 0.9405, Smoothed Validation Loss: 0.0222
Epoch [311/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [311/650], Validation Loss: 0.0222, Validation L1: 0.9405, Smoothed Validation Loss: 0.0222
Epoch [312/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [312/650], Validation Loss: 0.0222, Validation L1: 0.9405, Smoothed Validation Loss: 0.0222
Epoch [313/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [313/650], Validation Loss: 0.0222, Validation L1: 0.9405, Smoothed Validation Loss: 0.0222
Epoch [314/650], Train Loss: 0.0138, Train L1 Loss: 0.7820
Epoch [314/650], Validation Loss: 0.0222, Validation L1: 0.9405, Smoothed Validation Loss: 0.0222
Epoch 00314: reducing learning rate of group 0 to 4.8828e-07.
Epoch [315/650], Train Loss: 0.0138, Train L1 Loss: 0.7819
Epoch [315/650], Validation Loss: 0.0223, Validation L1: 0.9405, Smoothed Validation Loss: 0.0222
Epoch [316/650], Train Loss: 0.0138, Train L1 Loss: 0.7819
Epoch [316/650], Validation Loss: 0.0223, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [317/650], Train Loss: 0.0138, Train L1 Loss: 0.7819
Epoch [317/650], Validation Loss: 0.0223, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [318/650], Train Loss: 0.0138, Train L1 Loss: 0.7818
Epoch [318/650], Validation Loss: 0.0223, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [319/650], Train Loss: 0.0138, Train L1 Loss: 0.7818
Epoch [319/650], Validation Loss: 0.0223, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch [320/650], Train Loss: 0.0138, Train L1 Loss: 0.7818
Epoch [320/650], Validation Loss: 0.0223, Validation L1: 0.9406, Smoothed Validation Loss: 0.0222
Epoch 00320: reducing learning rate of group 0 to 2.4414e-07.
Epoch [321/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [321/650], Validation Loss: 0.0223, Validation L1: 0.9409, Smoothed Validation Loss: 0.0222
Epoch [322/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [322/650], Validation Loss: 0.0223, Validation L1: 0.9409, Smoothed Validation Loss: 0.0222
Epoch [323/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [323/650], Validation Loss: 0.0223, Validation L1: 0.9409, Smoothed Validation Loss: 0.0223
Epoch [324/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [324/650], Validation Loss: 0.0223, Validation L1: 0.9409, Smoothed Validation Loss: 0.0223
Epoch [325/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [325/650], Validation Loss: 0.0223, Validation L1: 0.9409, Smoothed Validation Loss: 0.0223
Epoch [326/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [326/650], Validation Loss: 0.0223, Validation L1: 0.9409, Smoothed Validation Loss: 0.0223
Epoch 00326: reducing learning rate of group 0 to 1.2207e-07.
Epoch [327/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [327/650], Validation Loss: 0.0223, Validation L1: 0.9411, Smoothed Validation Loss: 0.0223
Epoch [328/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [328/650], Validation Loss: 0.0223, Validation L1: 0.9411, Smoothed Validation Loss: 0.0223
Epoch [329/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [329/650], Validation Loss: 0.0223, Validation L1: 0.9411, Smoothed Validation Loss: 0.0223
Epoch [330/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [330/650], Validation Loss: 0.0223, Validation L1: 0.9411, Smoothed Validation Loss: 0.0223
Epoch [331/650], Train Loss: 0.0138, Train L1 Loss: 0.7817
Epoch [331/650], Validation Loss: 0.0223, Validation L1: 0.9411, Smoothed Validation Loss: 0.0223
Epoch [332/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [332/650], Validation Loss: 0.0223, Validation L1: 0.9412, Smoothed Validation Loss: 0.0223
Epoch 00332: reducing learning rate of group 0 to 6.1035e-08.
Epoch [333/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [333/650], Validation Loss: 0.0223, Validation L1: 0.9412, Smoothed Validation Loss: 0.0223
Epoch [334/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [334/650], Validation Loss: 0.0223, Validation L1: 0.9412, Smoothed Validation Loss: 0.0223
Epoch [335/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [335/650], Validation Loss: 0.0223, Validation L1: 0.9412, Smoothed Validation Loss: 0.0223
Epoch [336/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [336/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [337/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [337/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [338/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [338/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch 00338: reducing learning rate of group 0 to 3.0518e-08.
Epoch [339/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [339/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [340/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [340/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [341/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [341/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [342/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [342/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [343/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [343/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [344/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [344/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch 00344: reducing learning rate of group 0 to 1.5259e-08.
Epoch [345/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [345/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [346/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [346/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [347/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [347/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [348/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [348/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [349/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [349/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [350/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [350/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [351/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [351/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [352/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [352/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [353/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [353/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [354/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [354/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [355/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [355/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [356/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [356/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [357/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [357/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [358/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [358/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [359/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [359/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [360/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [360/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [361/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [361/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [362/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [362/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [363/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [363/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [364/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [364/650], Validation Loss: 0.0223, Validation L1: 0.9413, Smoothed Validation Loss: 0.0223
Epoch [365/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [365/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [366/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [366/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [367/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [367/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [368/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [368/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [369/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [369/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [370/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [370/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [371/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [371/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [372/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [372/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [373/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [373/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [374/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [374/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [375/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [375/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [376/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [376/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [377/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [377/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [378/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [378/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [379/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [379/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [380/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [380/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [381/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [381/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [382/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [382/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [383/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [383/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [384/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [384/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [385/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [385/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [386/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [386/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [387/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [387/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [388/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [388/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [389/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [389/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [390/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [390/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [391/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [391/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [392/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [392/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [393/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [393/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [394/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [394/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [395/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [395/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [396/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [396/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [397/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [397/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [398/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [398/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [399/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [399/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [400/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [400/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [401/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [401/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [402/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [402/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [403/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [403/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [404/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [404/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [405/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [405/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [406/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [406/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [407/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [407/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [408/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [408/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [409/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [409/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [410/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [410/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [411/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [411/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [412/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [412/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [413/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [413/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [414/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [414/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [415/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [415/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [416/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [416/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [417/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [417/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [418/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [418/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [419/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [419/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [420/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [420/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [421/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [421/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [422/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [422/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [423/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [423/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [424/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [424/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [425/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [425/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [426/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [426/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [427/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [427/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [428/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [428/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [429/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [429/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [430/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [430/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [431/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [431/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [432/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [432/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [433/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [433/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [434/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [434/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [435/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [435/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [436/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [436/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [437/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [437/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [438/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [438/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [439/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [439/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [440/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [440/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [441/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [441/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [442/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [442/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [443/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [443/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [444/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [444/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [445/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [445/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [446/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [446/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [447/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [447/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [448/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [448/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [449/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [449/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [450/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [450/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [451/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [451/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [452/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [452/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [453/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [453/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [454/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [454/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [455/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [455/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [456/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [456/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [457/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [457/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [458/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [458/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [459/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [459/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [460/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [460/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [461/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [461/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [462/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [462/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [463/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [463/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [464/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [464/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [465/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [465/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [466/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [466/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [467/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [467/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [468/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [468/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [469/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [469/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [470/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [470/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [471/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [471/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [472/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [472/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [473/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [473/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [474/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [474/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [475/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [475/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [476/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [476/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [477/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [477/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [478/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [478/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [479/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [479/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [480/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [480/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [481/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [481/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [482/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [482/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [483/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [483/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [484/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [484/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [485/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [485/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [486/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [486/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [487/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [487/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [488/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [488/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [489/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [489/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [490/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [490/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [491/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [491/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [492/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [492/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [493/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [493/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [494/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [494/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [495/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [495/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [496/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [496/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [497/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [497/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [498/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [498/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [499/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [499/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [500/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [500/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [501/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [501/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [502/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [502/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [503/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [503/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [504/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [504/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [505/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [505/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [506/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [506/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [507/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [507/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [508/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [508/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [509/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [509/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [510/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [510/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [511/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [511/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [512/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [512/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [513/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [513/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [514/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [514/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [515/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [515/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [516/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [516/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [517/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [517/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [518/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [518/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [519/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [519/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [520/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [520/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [521/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [521/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [522/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [522/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [523/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [523/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [524/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [524/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [525/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [525/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [526/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [526/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [527/650], Train Loss: 0.0138, Train L1 Loss: 0.7816
Epoch [527/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [528/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [528/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [529/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [529/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [530/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [530/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [531/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [531/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [532/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [532/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [533/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [533/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [534/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [534/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [535/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [535/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [536/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [536/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [537/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [537/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [538/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [538/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [539/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [539/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [540/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [540/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [541/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [541/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [542/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [542/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [543/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [543/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [544/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [544/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [545/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [545/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [546/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [546/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [547/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [547/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [548/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [548/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [549/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [549/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [550/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [550/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [551/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [551/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [552/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [552/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [553/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [553/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [554/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [554/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [555/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [555/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [556/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [556/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [557/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [557/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [558/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [558/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [559/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [559/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [560/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [560/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [561/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [561/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [562/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [562/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [563/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [563/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [564/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [564/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [565/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [565/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [566/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [566/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [567/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [567/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [568/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [568/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [569/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [569/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [570/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [570/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [571/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [571/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [572/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [572/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [573/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [573/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [574/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [574/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [575/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [575/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [576/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [576/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [577/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [577/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [578/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [578/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [579/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [579/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [580/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [580/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [581/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [581/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [582/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [582/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [583/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [583/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [584/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [584/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [585/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [585/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [586/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [586/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [587/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [587/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [588/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [588/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [589/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [589/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [590/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [590/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [591/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [591/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [592/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [592/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [593/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [593/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [594/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [594/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [595/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [595/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [596/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [596/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [597/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [597/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [598/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [598/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [599/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [599/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [600/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [600/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [601/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [601/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [602/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [602/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [603/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [603/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [604/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [604/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [605/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [605/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [606/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [606/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [607/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [607/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [608/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [608/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [609/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [609/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [610/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [610/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [611/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [611/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [612/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [612/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [613/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [613/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [614/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [614/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [615/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [615/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [616/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [616/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [617/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [617/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [618/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [618/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [619/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [619/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [620/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [620/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [621/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [621/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [622/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [622/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [623/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [623/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [624/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [624/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [625/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [625/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [626/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [626/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [627/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [627/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [628/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [628/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [629/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [629/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [630/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [630/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [631/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [631/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [632/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [632/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [633/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [633/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [634/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [634/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [635/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [635/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [636/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [636/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [637/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [637/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [638/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [638/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [639/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [639/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [640/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [640/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [641/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [641/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [642/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [642/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [643/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [643/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [644/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [644/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [645/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [645/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [646/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [646/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [647/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [647/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [648/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [648/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [649/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [649/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
Epoch [650/650], Train Loss: 0.0138, Train L1 Loss: 0.7815
Epoch [650/650], Validation Loss: 0.0223, Validation L1: 0.9414, Smoothed Validation Loss: 0.0223
cuda
```

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19673444: <WorkingSetup_6> in cluster <dcc> Done

Job <WorkingSetup_6> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Sat Dec  2 18:17:08 2023
Job was executed on host(s) <4*n-62-18-13>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Sat Dec  2 23:05:56 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Sat Dec  2 23:05:56 2023
Terminated at Sun Dec  3 09:12:30 2023
Results reported at Sun Dec  3 09:12:30 2023

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

    CPU time :                                   36688.20 sec.
    Max Memory :                                 1937 MB
    Average Memory :                             1921.67 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63599.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   36393 sec.
    Turnaround time :                            53722 sec.

The output (if any) is above this job summary.

