
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
| <c>name</c>       | <d>str</d>        | <j>"dynamoFix-0"</j> |
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
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231128_181800-f966upm8
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run dynamoFix-0
wandb: ⭐️ View project at https://wandb.ai/chessproject65/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/chessproject65/deeplearning_painn/runs/f966upm8
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in get_neighbours_as_edge_index> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 118 
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:14,200] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <listcomp> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 124 
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING]   File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1397, in run_node
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING]     return node.target(*args, **kwargs)
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.TorchRuntimeError: Failed running call_function <built-in method ones of type object at 0x7fdc61ef3a40>(*((FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(), dtype=torch.int64)),), **{}):
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] ones(): argument 'size' (position 1) must be tuple of ints, but found element of type FakeTensor at pos 0
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] from user code:
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING]    File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 124, in <listcomp>
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING]     neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]]).to(self.device)
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:18,332] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT propagate /tmp/s230208_pyg/tmpcu5m3psq.py line 218 
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,221] torch._dynamo.convert_frame: [WARNING] 
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:110: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  torch.has_cuda,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:111: UserWarning: 'has_cudnn' is deprecated, please use 'torch.backends.cudnn.is_available()'
  torch.has_cudnn,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:117: UserWarning: 'has_mps' is deprecated, please use 'torch.backends.mps.is_built()'
  torch.has_mps,
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/overrides.py:118: UserWarning: 'has_mkldnn' is deprecated, please use 'torch.backends.mkldnn.is_available()'
  torch.has_mkldnn,
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _collect /tmp/s230208_pyg/tmpcu5m3psq.py line 117 
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,768] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT _lift /tmp/s230208_pyg/tmpcu5m3psq.py line 90 
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:28,970] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT message /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 51 
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:29,570] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT scatter /zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch_geometric/utils/scatter.py line 15 
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:32,876] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT <resume in aggregate> /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 85 
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:34,347] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] WON'T CONVERT update /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py line 92 
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] due to: 
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] Traceback (most recent call last):
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING]   File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING]     raise self._exception
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] 
[2023-11-28 18:18:35,497] torch._dynamo.convert_frame: [WARNING] 
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
wandb: ERROR Error while calling W&B API: An internal error occurred. Please contact support. (<Response [500]>)
Process ForkProcess-3:
Process ForkProcess-4:

Process ForkProcess-2:
Epoch [1/1000], Train Loss: 5396073623079684061681189650432.0000, Train L1 Loss: 98952196952614.6094
Epoch [1/1000], Validation Loss: 27356305369322391008657369202688.0000, Validation L1: 310916769360191.3125, Smoothed Validation Loss: 27356305369322391008657369202688.0000
Epoch [2/1000], Train Loss: 31940022260972882852298342006784.0000, Train L1 Loss: 189592370729324.0625
Epoch [2/1000], Validation Loss: 27356305431436996336071879950336.0000, Validation L1: 310916775886872.3125, Smoothed Validation Loss: 27356305375533850190318932066304.0000
Epoch [3/1000], Train Loss: 31939982713711475781379161063424.0000, Train L1 Loss: 189592338475984.6562
Epoch [3/1000], Validation Loss: 27356317849430290660699643314176.0000, Validation L1: 310916858317743.3125, Smoothed Validation Loss: 27356306622923495588436891402240.0000
Epoch [4/1000], Train Loss: 31940015122955115948536573722624.0000, Train L1 Loss: 189592372522205.7500
Epoch [4/1000], Validation Loss: 27356332743458596894871914545152.0000, Validation L1: 310916903186973.8750, Smoothed Validation Loss: 27356309234977007070160281927680.0000
Epoch [5/1000], Train Loss: 31939987613451059039108243390464.0000, Train L1 Loss: 189592343260459.9375
Epoch [5/1000], Validation Loss: 27356281404465857806177866350592.0000, Validation L1: 310916687998803.0625, Smoothed Validation Loss: 27356306451925893494841928581120.0000
Epoch [6/1000], Train Loss: 31939990577982934165041056841728.0000, Train L1 Loss: 189592329702253.0000
Epoch [6/1000], Validation Loss: 27356266201913941988563514032128.0000, Validation L1: 310916596200192.6250, Smoothed Validation Loss: 27356302426924699244934012600320.0000
Epoch [7/1000], Train Loss: 31939949571121488131570609946624.0000, Train L1 Loss: 189592253211165.6562
Epoch [7/1000], Validation Loss: 27356281514076415595759649423360.0000, Validation L1: 310916690860843.5625, Smoothed Validation Loss: 27356300335639868628216762597376.0000
Epoch 00007: reducing learning rate of group 0 to 5.0000e-04.
Epoch [8/1000], Train Loss: 31939984791389729462709634727936.0000, Train L1 Loss: 189592320704917.3438
Epoch [8/1000], Validation Loss: 27356305614647225711989530558464.0000, Validation L1: 310916794517619.4375, Smoothed Validation Loss: 27356300863540607489113778552832.0000
Epoch [9/1000], Train Loss: 31939983106724717555317729132544.0000, Train L1 Loss: 189592333207347.4688
Epoch [9/1000], Validation Loss: 27356317628609320853508609540096.0000, Validation L1: 310916847438007.2500, Smoothed Validation Loss: 27356302540047474772313597018112.0000
Epoch [10/1000], Train Loss: 31939988849301653529571555803136.0000, Train L1 Loss: 189592343543922.9375
Epoch [10/1000], Validation Loss: 27356299474852271178901926969344.0000, Validation L1: 310916765074895.5625, Smoothed Validation Loss: 27356302233527953512252504539136.0000
Epoch [11/1000], Train Loss: 31939976539819331620305677320192.0000, Train L1 Loss: 189592315141526.5000
Epoch [11/1000], Validation Loss: 27356287582356063529250253176832.0000, Validation L1: 310916712800251.7500, Smoothed Validation Loss: 27356300768410766315392130351104.0000
Epoch [12/1000], Train Loss: 31939974141143438640038969081856.0000, Train L1 Loss: 189592312173139.5625
Epoch [12/1000], Validation Loss: 27356287328793613682701424918528.0000, Validation L1: 310916696293474.6250, Smoothed Validation Loss: 27356299424449051502483022544896.0000
Epoch [13/1000], Train Loss: 31940003645616322419006432608256.0000, Train L1 Loss: 189592360690520.3438
Epoch [13/1000], Validation Loss: 27356372111810072722865181949952.0000, Validation L1: 310917091870883.1250, Smoothed Validation Loss: 27356306693185153174161275748352.0000
Epoch 00013: reducing learning rate of group 0 to 2.5000e-04.
Epoch [14/1000], Train Loss: 31939984577362101923434941382656.0000, Train L1 Loss: 189592332872317.0312
Epoch [14/1000], Validation Loss: 27356347853964394290016254164992.0000, Validation L1: 310916986440013.7500, Smoothed Validation Loss: 27356310809263075033946959904768.0000
Epoch [15/1000], Train Loss: 31940000284136685244278718332928.0000, Train L1 Loss: 189592347484558.7500
Epoch [15/1000], Validation Loss: 27356296507914505578033383997440.0000, Validation L1: 310916744170676.8125, Smoothed Validation Loss: 27356309379128219439435490525184.0000
Epoch [16/1000], Train Loss: 31939988245003359295836614819840.0000, Train L1 Loss: 189592334462566.1875
Epoch [16/1000], Validation Loss: 27356259896681642051823246245888.0000, Validation L1: 310916552612300.3125, Smoothed Validation Loss: 27356304430883562151034228834304.0000
Epoch [17/1000], Train Loss: 31940001397413380633751917166592.0000, Train L1 Loss: 189592369642567.0625
Epoch [17/1000], Validation Loss: 27356305379876545210202734985216.0000, Validation L1: 310916760346415.0000, Smoothed Validation Loss: 27356304525782864059830781345792.0000
Epoch [18/1000], Train Loss: 31939959232946614323375140503552.0000, Train L1 Loss: 189592294721416.2812
Epoch [18/1000], Validation Loss: 27356266226292602311464114454528.0000, Validation L1: 310916592851898.1875, Smoothed Validation Loss: 27356300695833839686433965604864.0000
Epoch [19/1000], Train Loss: 31940002641907396119055369764864.0000, Train L1 Loss: 189592324625621.3750
Epoch [19/1000], Validation Loss: 27356241915060704456610787885056.0000, Validation L1: 310916484407260.6250, Smoothed Validation Loss: 27356294817756529766331349729280.0000
Epoch 00019: reducing learning rate of group 0 to 1.2500e-04.
Epoch [20/1000], Train Loss: 31940042511365561918495198806016.0000, Train L1 Loss: 189592413070085.4688
Epoch [20/1000], Validation Loss: 27356314641752422331156514471936.0000, Validation L1: 310916823453593.5000, Smoothed Validation Loss: 27356296800156120824253717151744.0000
Epoch [21/1000], Train Loss: 31940005375557723741013080539136.0000, Train L1 Loss: 189592372498326.5625
Epoch [21/1000], Validation Loss: 27356281258296451839488744751104.0000, Validation L1: 310916669570535.8125, Smoothed Validation Loss: 27356295245970153925777219911680.0000
Epoch [22/1000], Train Loss: 31940011000826707068570430341120.0000, Train L1 Loss: 189592360526269.7812
Epoch [22/1000], Validation Loss: 27356305525862145765299984531456.0000, Validation L1: 310916785351030.8125, Smoothed Validation Loss: 27356296273959354911169347321856.0000
Epoch [23/1000], Train Loss: 31939979762232275369063199277056.0000, Train L1 Loss: 189592312233240.7812
Epoch [23/1000], Validation Loss: 27356296417480653304163872014336.0000, Validation L1: 310916737701826.5000, Smoothed Validation Loss: 27356296288311484750468799791104.0000
Epoch [24/1000], Train Loss: 31939998564611718047212446416896.0000, Train L1 Loss: 189592354768137.9688
Epoch [24/1000], Validation Loss: 27356290444463887380987068284928.0000, Validation L1: 310916720273931.1875, Smoothed Validation Loss: 27356295703926725463880589377536.0000
Epoch [25/1000], Train Loss: 31939974257070105755823523233792.0000, Train L1 Loss: 189592305869158.1562
Epoch [25/1000], Validation Loss: 27356278278269834109196682919936.0000, Validation L1: 310916661926276.8125, Smoothed Validation Loss: 27356293961361036328412198731776.0000
Epoch 00025: reducing learning rate of group 0 to 6.2500e-05.
Epoch [26/1000], Train Loss: 31939948968431397799572281491456.0000, Train L1 Loss: 189592284138447.0000
Epoch [26/1000], Validation Loss: 27356363010403665292607946227712.0000, Validation L1: 310917046847090.1250, Smoothed Validation Loss: 27356300866265298774471810744320.0000
Epoch [27/1000], Train Loss: 31939969548491820987337683238912.0000, Train L1 Loss: 189592294248913.3438
Epoch [27/1000], Validation Loss: 27356314640560999553335277125632.0000, Validation L1: 310916828029314.3750, Smoothed Validation Loss: 27356302243694870203438045593600.0000
Epoch [28/1000], Train Loss: 31939952119191256325332658028544.0000, Train L1 Loss: 189592243819375.3125
Epoch [28/1000], Validation Loss: 27356269306347644544567222468608.0000, Validation L1: 310916617372049.4375, Smoothed Validation Loss: 27356298949960148538270888755200.0000
Epoch [29/1000], Train Loss: 31940010531197633958654171414528.0000, Train L1 Loss: 189592360557445.5938
Epoch [29/1000], Validation Loss: 27356308537944111124520691040256.0000, Validation L1: 310916799568686.0625, Smoothed Validation Loss: 27356299908758544346535906246656.0000
Epoch [30/1000], Train Loss: 31939982638887424075148958892032.0000, Train L1 Loss: 189592337630708.6250
Epoch [30/1000], Validation Loss: 27356353997172298217915158626304.0000, Validation L1: 310917011524246.5625, Smoothed Validation Loss: 27356305317599918382593943273472.0000
Epoch [31/1000], Train Loss: 31939959709227751780897127399424.0000, Train L1 Loss: 189592274702735.6875
Epoch [31/1000], Validation Loss: 27356326755855540973370156777472.0000, Validation L1: 310916890650706.6250, Smoothed Validation Loss: 27356307461425480641671564623872.0000
Epoch 00031: reducing learning rate of group 0 to 3.1250e-05.
Epoch [32/1000], Train Loss: 31940014521676273595771063894016.0000, Train L1 Loss: 189592358653497.5000
Epoch [32/1000], Validation Loss: 27356260310244218953902202028032.0000, Validation L1: 310916583590024.1875, Smoothed Validation Loss: 27356302746307352221094814679040.0000
Epoch [33/1000], Train Loss: 31939967681561975337805741555712.0000, Train L1 Loss: 189592281650302.1562
Epoch [33/1000], Validation Loss: 27356314488300394025834267017216.0000, Validation L1: 310916812527357.5625, Smoothed Validation Loss: 27356303920506658203008610861056.0000
Epoch [34/1000], Train Loss: 31939976930996235149783553015808.0000, Train L1 Loss: 189592280266862.1562
Epoch [34/1000], Validation Loss: 27356281002692060914690878865408.0000, Validation L1: 310916657174093.6250, Smoothed Validation Loss: 27356301628725202077056539557888.0000
Epoch [35/1000], Train Loss: 31939976667124293655045888540672.0000, Train L1 Loss: 189592316676387.4062
Epoch [35/1000], Validation Loss: 27356275212948209970645095677952.0000, Validation L1: 310916630105133.6875, Smoothed Validation Loss: 27356298987147501064975544221696.0000
Epoch [36/1000], Train Loss: 31939999808600708877501826334720.0000, Train L1 Loss: 189592353547866.7500
Epoch [36/1000], Validation Loss: 27356281419278489714575206776832.0000, Validation L1: 310916683826443.5000, Smoothed Validation Loss: 27356297230360601731375361425408.0000
Epoch [37/1000], Train Loss: 31939988125269754379039506694144.0000, Train L1 Loss: 189592330940143.6250
Epoch [37/1000], Validation Loss: 27356278302243093904440273403904.0000, Validation L1: 310916651693717.8750, Smoothed Validation Loss: 27356295337548848246522076200960.0000
Epoch 00037: reducing learning rate of group 0 to 1.5625e-05.
Epoch [38/1000], Train Loss: 31939991219687676543752600551424.0000, Train L1 Loss: 189592350888599.9688
Epoch [38/1000], Validation Loss: 27356266076962263881511717568512.0000, Validation L1: 310916585244819.1250, Smoothed Validation Loss: 27356292411490188909301114863616.0000
Epoch [39/1000], Train Loss: 31939966239284406341586883969024.0000, Train L1 Loss: 189592283208054.8438
Epoch [39/1000], Validation Loss: 27356357078647847831084959006720.0000, Validation L1: 310917037881459.0625, Smoothed Validation Loss: 27356298878205953000039648329728.0000
Epoch [40/1000], Train Loss: 31939948709492829941045452079104.0000, Train L1 Loss: 189592236790969.4062
Epoch [40/1000], Validation Loss: 27356323958052242803853029801984.0000, Validation L1: 310916886985802.0000, Smoothed Validation Loss: 27356301386190581530061023739904.0000
Epoch [41/1000], Train Loss: 31939981019901269823064004100096.0000, Train L1 Loss: 189592311068028.3750
Epoch [41/1000], Validation Loss: 27356299586486291777461646524416.0000, Validation L1: 310916765960986.3750, Smoothed Validation Loss: 27356301206220156157680787914752.0000
Epoch [42/1000], Train Loss: 31940035975496399549134494760960.0000, Train L1 Loss: 189592398760715.8438
Epoch [42/1000], Validation Loss: 27356290091646848541199756689408.0000, Validation L1: 310916699301431.5625, Smoothed Validation Loss: 27356300094762824945672722055168.0000
Epoch [43/1000], Train Loss: 31940012522662372087722907009024.0000, Train L1 Loss: 189592372242235.4375
Epoch [43/1000], Validation Loss: 27356323643207002481065021407232.0000, Validation L1: 310916861479326.0625, Smoothed Validation Loss: 27356302449607240897772101042176.0000
Epoch 00043: reducing learning rate of group 0 to 7.8125e-06.
Epoch [44/1000], Train Loss: 31939989961768056770488627625984.0000, Train L1 Loss: 189592313019353.5312
Epoch [44/1000], Validation Loss: 27356296533333213688080044654592.0000, Validation L1: 310916756635556.0625, Smoothed Validation Loss: 27356301857979842230042560036864.0000
Epoch [45/1000], Train Loss: 31939987904371498298643167838208.0000, Train L1 Loss: 189592339173093.9062
Epoch [45/1000], Validation Loss: 27356290188963020700823567990784.0000, Validation L1: 310916696374287.0000, Smoothed Validation Loss: 27356300691078160077120660832256.0000
Epoch [46/1000], Train Loss: 31940015124228630340365520470016.0000, Train L1 Loss: 189592366039690.0312
Epoch [46/1000], Validation Loss: 27356323844350155745605896372224.0000, Validation L1: 310916878069372.7500, Smoothed Validation Loss: 27356303006405358292889296175104.0000
Epoch [47/1000], Train Loss: 31939996123810505232410329743360.0000, Train L1 Loss: 189592332172095.1562
Epoch [47/1000], Validation Loss: 27356281465491303592509841604608.0000, Validation L1: 310916684845232.4375, Smoothed Validation Loss: 27356300852313953273211313455104.0000
Epoch [48/1000], Train Loss: 31940029207343633543405332594688.0000, Train L1 Loss: 189592404197715.2500
Epoch [48/1000], Validation Loss: 27356241939573558537608146976768.0000, Validation L1: 310916482475250.3125, Smoothed Validation Loss: 27356294961039911998211145859072.0000
Epoch [49/1000], Train Loss: 31939999321705451789396035502080.0000, Train L1 Loss: 189592352004224.0938
Epoch [49/1000], Validation Loss: 27356314773676604906500704436224.0000, Validation L1: 310916828448861.2500, Smoothed Validation Loss: 27356296942303582640119989927936.0000
Epoch 00049: reducing learning rate of group 0 to 3.9063e-06.
Epoch [50/1000], Train Loss: 31940039531851174602621002448896.0000, Train L1 Loss: 189592412099328.1250
Epoch [50/1000], Validation Loss: 27356266335650845931922465488896.0000, Validation L1: 310916607626333.0000, Smoothed Validation Loss: 27356293881638311221100051169280.0000
Epoch [51/1000], Train Loss: 31940031196952411244436922564608.0000, Train L1 Loss: 189592385809182.5938
Epoch [51/1000], Validation Loss: 27356347889508905730250190618624.0000, Validation L1: 310916992564193.1875, Smoothed Validation Loss: 27356299282425371122375027851264.0000
Epoch [52/1000], Train Loss: 31939976645164602260398901559296.0000, Train L1 Loss: 189592311261581.2812
Epoch [52/1000], Validation Loss: 27356242011360441201934842462208.0000, Validation L1: 310916487764298.0000, Smoothed Validation Loss: 27356293555318876328891158364160.0000
Epoch [53/1000], Train Loss: 31939980528479192547908994990080.0000, Train L1 Loss: 189592317027289.8750
Epoch [53/1000], Validation Loss: 27356326754370560061038028390400.0000, Validation L1: 310916890285900.8750, Smoothed Validation Loss: 27356296875224042450306031681536.0000
Epoch [54/1000], Train Loss: 31940000482286174239316485603328.0000, Train L1 Loss: 189592360115884.9375
Epoch [54/1000], Validation Loss: 27356290319618323088355375448064.0000, Validation L1: 310916711790798.5625, Smoothed Validation Loss: 27356296219663471414830891532288.0000
Epoch [55/1000], Train Loss: 31939992238355254962819237412864.0000, Train L1 Loss: 189592332112571.6562
Epoch [55/1000], Validation Loss: 27356278485615754608118295691264.0000, Validation L1: 310916667125532.3750, Smoothed Validation Loss: 27356294446258699283799669211136.0000
Epoch 00055: reducing learning rate of group 0 to 1.9531e-06.
Epoch [56/1000], Train Loss: 31939946553019876402417677369344.0000, Train L1 Loss: 189592267469192.2500
Epoch [56/1000], Validation Loss: 27356323750051305264327769980928.0000, Validation L1: 310916873955404.8125, Smoothed Validation Loss: 27356297376637958981132553814016.0000
Epoch [57/1000], Train Loss: 31939983192783741625962149707776.0000, Train L1 Loss: 189592292926785.9688
Epoch [57/1000], Validation Loss: 27356305412357969392677647548416.0000, Validation L1: 310916775491058.0000, Smoothed Validation Loss: 27356298180209962274086876872704.0000
Epoch [58/1000], Train Loss: 31940008397293290009491266338816.0000, Train L1 Loss: 189592358968721.8750
Epoch [58/1000], Validation Loss: 27356290446610469596578059386880.0000, Validation L1: 310916720474554.1875, Smoothed Validation Loss: 27356297406850014807775846072320.0000
Epoch [59/1000], Train Loss: 31940002237492319110908879044608.0000, Train L1 Loss: 189592333333599.2500
Epoch [59/1000], Validation Loss: 27356278395433585999424383877120.0000, Validation L1: 310916667574389.9375, Smoothed Validation Loss: 27356295505708371926940699852800.0000
Epoch [60/1000], Train Loss: 31940027182807720357057890615296.0000, Train L1 Loss: 189592392575194.8438
Epoch [60/1000], Validation Loss: 27356308478761596852503878565888.0000, Validation L1: 310916797199275.6875, Smoothed Validation Loss: 27356296803013695320216943198208.0000
Epoch [61/1000], Train Loss: 31940029971364250289656052056064.0000, Train L1 Loss: 189592386846576.0625
Epoch [61/1000], Validation Loss: 27356257152637938735017296396288.0000, Validation L1: 310916550117076.6875, Smoothed Validation Loss: 27356292837976119661696978518016.0000
Epoch 00061: reducing learning rate of group 0 to 9.7656e-07.
Epoch [62/1000], Train Loss: 31939990215239966250128799432704.0000, Train L1 Loss: 189592359758806.9062
Epoch [62/1000], Validation Loss: 27356269292503610815227709358080.0000, Validation L1: 310916620919528.8750, Smoothed Validation Loss: 27356290483428869227410014339072.0000
Epoch [63/1000], Train Loss: 31939990294074568000124603072512.0000, Train L1 Loss: 189592357275051.7500
Epoch [63/1000], Validation Loss: 27356317563451822409064204206080.0000, Validation L1: 310916835513838.2500, Smoothed Validation Loss: 27356293191431160942695731429376.0000
Epoch [64/1000], Train Loss: 31939977862564331883493618352128.0000, Train L1 Loss: 189592326598310.8750
Epoch [64/1000], Validation Loss: 27356308593083771032644773478400.0000, Validation L1: 310916802950770.1250, Smoothed Validation Loss: 27356294731596422402050598371328.0000
Epoch [65/1000], Train Loss: 31940032640599939218504866070528.0000, Train L1 Loss: 189592372676243.1875
Epoch [65/1000], Validation Loss: 27356290404762287772312149164032.0000, Validation L1: 310916713877934.3750, Smoothed Validation Loss: 27356294298913011641236529872896.0000
Epoch [66/1000], Train Loss: 31940017053184927858205822812160.0000, Train L1 Loss: 189592385602935.3750
Epoch [66/1000], Validation Loss: 27356314587587449468786464260096.0000, Validation L1: 310916820485911.6875, Smoothed Validation Loss: 27356296327780455423991523311616.0000
Epoch [67/1000], Train Loss: 31939995080518482540779347640320.0000, Train L1 Loss: 189592358941334.0000
Epoch [67/1000], Validation Loss: 27356305227412485065935635349504.0000, Validation L1: 310916755379648.8125, Smoothed Validation Loss: 27356297217743659288905859989504.0000
Epoch 00067: reducing learning rate of group 0 to 4.8828e-07.
Epoch [68/1000], Train Loss: 31939971905585208492556321554432.0000, Train L1 Loss: 189592318337645.8750
Epoch [68/1000], Validation Loss: 27356299757647131343150280343552.0000, Validation L1: 310916782173255.7500, Smoothed Validation Loss: 27356297471734009646850041184256.0000
Epoch [69/1000], Train Loss: 31939987794032154506561408991232.0000, Train L1 Loss: 189592302233045.0000
Epoch [69/1000], Validation Loss: 27356308487772655692125527080960.0000, Validation L1: 310916795904769.3750, Smoothed Validation Loss: 27356298573337874701737552510976.0000
Epoch [70/1000], Train Loss: 31940017196536643207231711477760.0000, Train L1 Loss: 189592379130044.6250
Epoch [70/1000], Validation Loss: 27356278270231323105506065645568.0000, Validation L1: 310916657215961.6875, Smoothed Validation Loss: 27356296543027220893194292035584.0000
Epoch [71/1000], Train Loss: 31939995149196089029568707428352.0000, Train L1 Loss: 189592318495774.8750
Epoch [71/1000], Validation Loss: 27356287364155810402820148953088.0000, Validation L1: 310916697067816.5000, Smoothed Validation Loss: 27356295625140078042717026779136.0000
Epoch [72/1000], Train Loss: 31939981351148642506733495779328.0000, Train L1 Loss: 189592318752668.1250
Epoch [72/1000], Validation Loss: 27356317406618671647497283174400.0000, Validation L1: 310916823524391.6875, Smoothed Validation Loss: 27356297803287937853555015155712.0000
Epoch [73/1000], Train Loss: 31939989278487186013801370615808.0000, Train L1 Loss: 189592336471326.5312
Epoch [73/1000], Validation Loss: 27356323653854818044060811395072.0000, Validation L1: 310916865793729.9375, Smoothed Validation Loss: 27356300388344625872605594779648.0000
Epoch 00073: reducing learning rate of group 0 to 2.4414e-07.
Epoch [74/1000], Train Loss: 31940015014795018980143124185088.0000, Train L1 Loss: 189592385791191.3125
Epoch [74/1000], Validation Loss: 27356248038319386913915677966336.0000, Validation L1: 310916511739810.7500, Smoothed Validation Loss: 27356295153342102877456528572416.0000
Epoch [75/1000], Train Loss: 31939983377789421065323595956224.0000, Train L1 Loss: 189592342484827.0938
Epoch [75/1000], Validation Loss: 27356299574428894567095164993536.0000, Validation L1: 310916773428996.9375, Smoothed Validation Loss: 27356295595450786550020019585024.0000
Epoch [76/1000], Train Loss: 31939997390798771373731137716224.0000, Train L1 Loss: 189592336621654.1250
Epoch [76/1000], Validation Loss: 27356305432977947984572968861696.0000, Validation L1: 310916772260959.1250, Smoothed Validation Loss: 27356296579203506296355016409088.0000
Epoch [77/1000], Train Loss: 31939994289405615559351463837696.0000, Train L1 Loss: 189592338759805.1875
Epoch [77/1000], Validation Loss: 27356317670614880966752981745664.0000, Validation L1: 310916848385602.0000, Smoothed Validation Loss: 27356298688344641061235036520448.0000
Epoch [78/1000], Train Loss: 31939993839562071584373183873024.0000, Train L1 Loss: 189592333156286.6875
Epoch [78/1000], Validation Loss: 27356299301228322905011821477888.0000, Validation L1: 310916746559145.6250, Smoothed Validation Loss: 27356298749633006993812901330944.0000
Epoch [79/1000], Train Loss: 31940010823932078112097657946112.0000, Train L1 Loss: 189592381607523.4688
Epoch [79/1000], Validation Loss: 27356287458238456576787099942912.0000, Validation L1: 310916697300217.5000, Smoothed Validation Loss: 27356297620493552852830246666240.0000
Epoch 00079: reducing learning rate of group 0 to 1.2207e-07.
Epoch [80/1000], Train Loss: 31940050366664129469377411022848.0000, Train L1 Loss: 189592425339128.1875
Epoch [80/1000], Validation Loss: 27356269058468674377365176975360.0000, Validation L1: 310916600435622.4375, Smoothed Validation Loss: 27356294764291065005283739697152.0000
Epoch [81/1000], Train Loss: 31939974859547981969780526546944.0000, Train L1 Loss: 189592306191448.8750
Epoch [81/1000], Validation Loss: 27356332725238176716836239835136.0000, Validation L1: 310916901818574.3125, Smoothed Validation Loss: 27356298560385774374999138762752.0000
Epoch [82/1000], Train Loss: 31940006403254118693032087781376.0000, Train L1 Loss: 189592378490639.0625
Epoch [82/1000], Validation Loss: 27356287229665138989828197580800.0000, Validation L1: 310916686829672.3125, Smoothed Validation Loss: 27356297427313709485402156433408.0000
Epoch [83/1000], Train Loss: 31940009209845777204197019615232.0000, Train L1 Loss: 189592362799417.7500
Epoch [83/1000], Validation Loss: 27356299578186423376595837255680.0000, Validation L1: 310916769017177.6250, Smoothed Validation Loss: 27356297642400979973801599041536.0000
Epoch [84/1000], Train Loss: 31940031374011511659301265473536.0000, Train L1 Loss: 189592388429658.0625
Epoch [84/1000], Validation Loss: 27356326724519773989303142580224.0000, Validation L1: 310916884381837.6250, Smoothed Validation Loss: 27356300550612860276071678869504.0000
Epoch [85/1000], Train Loss: 31939988975644606151508782743552.0000, Train L1 Loss: 189592342575676.0625
Epoch [85/1000], Validation Loss: 27356326591202920783189037285376.0000, Validation L1: 310916873854944.4375, Smoothed Validation Loss: 27356303154671865426063489236992.0000
Epoch 00085: reducing learning rate of group 0 to 6.1035e-08.
Epoch [86/1000], Train Loss: 31939986642352846259734645309440.0000, Train L1 Loss: 189592315178785.0625
Epoch [86/1000], Validation Loss: 27356256915324215135242830217216.0000, Validation L1: 310916535044565.7500, Smoothed Validation Loss: 27356298530737100847341386072064.0000
Epoch [87/1000], Train Loss: 31939967563551582746429406314496.0000, Train L1 Loss: 189592313409691.2812
Epoch [87/1000], Validation Loss: 27356260067353174525197330415616.0000, Validation L1: 310916563078337.8750, Smoothed Validation Loss: 27356294684398711818006682402816.0000
Epoch [88/1000], Train Loss: 31939969639147070218888728805376.0000, Train L1 Loss: 189592279034549.2812
Epoch [88/1000], Validation Loss: 27356269284174959909143375249408.0000, Validation L1: 310916623218364.8125, Smoothed Validation Loss: 27356292144376340230000053583872.0000
Epoch [89/1000], Train Loss: 31940015556132076192514174877696.0000, Train L1 Loss: 189592394314896.9688
Epoch [89/1000], Validation Loss: 27356290359753024865995260428288.0000, Validation L1: 310916719158519.0625, Smoothed Validation Loss: 27356291965914008243239611531264.0000
Epoch [90/1000], Train Loss: 31939945647594441418854079922176.0000, Train L1 Loss: 189592261310604.9375
Epoch [90/1000], Validation Loss: 27356314509368723975032830689280.0000, Validation L1: 310916815045182.2500, Smoothed Validation Loss: 27356294220259481617858784395264.0000
Epoch [91/1000], Train Loss: 31940001678196271175271383564288.0000, Train L1 Loss: 189592328133396.7500
Epoch [91/1000], Validation Loss: 27356260043422077429665182515200.0000, Validation L1: 310916571771302.4375, Smoothed Validation Loss: 27356290802575740748679461470208.0000
Epoch 00091: reducing learning rate of group 0 to 3.0518e-08.
Epoch [92/1000], Train Loss: 31939976874465012496397888389120.0000, Train L1 Loss: 189592294008243.3750
Epoch [92/1000], Validation Loss: 27356281091477046285788250112000.0000, Validation L1: 310916659071092.7500, Smoothed Validation Loss: 27356289831465868149870601175040.0000
Epoch [93/1000], Train Loss: 31939998227419810028196013801472.0000, Train L1 Loss: 189592364513523.5312
Epoch [93/1000], Validation Loss: 27356278319291803560223711428608.0000, Validation L1: 310916652766520.1250, Smoothed Validation Loss: 27356288680248462591625837674496.0000
Epoch [94/1000], Train Loss: 31940011505060935312043315036160.0000, Train L1 Loss: 189592367622911.5938
Epoch [94/1000], Validation Loss: 27356290336556460366087613054976.0000, Validation L1: 310916711026161.6875, Smoothed Validation Loss: 27356288845879264620871828897792.0000
Epoch [95/1000], Train Loss: 31940009417868151877948562997248.0000, Train L1 Loss: 189592356552413.9688
Epoch [95/1000], Validation Loss: 27356326639452037232639241879552.0000, Validation L1: 310916882552732.8125, Smoothed Validation Loss: 27356292625236544133848383881216.0000
Epoch [96/1000], Train Loss: 31939987645168190839620991188992.0000, Train L1 Loss: 189592319563114.4688
Epoch [96/1000], Validation Loss: 27356314781279194487859621920768.0000, Validation L1: 310916840423804.6875, Smoothed Validation Loss: 27356294840840810520329395896320.0000
Epoch [97/1000], Train Loss: 31940007892367241309259862900736.0000, Train L1 Loss: 189592351829949.4062
Epoch [97/1000], Validation Loss: 27356281378537216117523299172352.0000, Validation L1: 310916676915717.6875, Smoothed Validation Loss: 27356293494610452431128674435072.0000
Epoch 00097: reducing learning rate of group 0 to 1.5259e-08.
Epoch [98/1000], Train Loss: 31939972936087575696008143699968.0000, Train L1 Loss: 189592297006652.3125
Epoch [98/1000], Validation Loss: 27356335931861693826816779747328.0000, Validation L1: 310916943111587.1250, Smoothed Validation Loss: 27356297738335578372137335914496.0000
Epoch [99/1000], Train Loss: 31939952497089260324711607304192.0000, Train L1 Loss: 189592249525687.5312
Epoch [99/1000], Validation Loss: 27356335608251417304851118292992.0000, Validation L1: 310916912701388.0000, Smoothed Validation Loss: 27356301525327161815048751415296.0000
Epoch [100/1000], Train Loss: 31939999058248219762745155780608.0000, Train L1 Loss: 189592348244443.1250
Epoch [100/1000], Validation Loss: 27356241848222890473196313640960.0000, Validation L1: 310916476887552.8125, Smoothed Validation Loss: 27356295557616735131223470374912.0000
Epoch [101/1000], Train Loss: 31939980395479793575928608587776.0000, Train L1 Loss: 189592312810037.1562
Epoch [101/1000], Validation Loss: 27356257299306771382383669149696.0000, Validation L1: 310916566953379.8125, Smoothed Validation Loss: 27356291731785734703099825618944.0000
Epoch [102/1000], Train Loss: 31939994486306981457259399217152.0000, Train L1 Loss: 189592340243084.7188
Epoch [102/1000], Validation Loss: 27356305424373050780945355898880.0000, Validation L1: 310916773921836.1250, Smoothed Validation Loss: 27356293101044465860524415909888.0000
Epoch [103/1000], Train Loss: 31939985756592009753914874265600.0000, Train L1 Loss: 189592313604998.7188
Epoch [103/1000], Validation Loss: 27356287593833469165205452750848.0000, Validation L1: 310916710922163.0000, Smoothed Validation Loss: 27356292550323366190992519593984.0000
Epoch [104/1000], Train Loss: 31939945630480857410438369902592.0000, Train L1 Loss: 189592257686586.1562
Epoch [104/1000], Validation Loss: 27356332734430852218630858342400.0000, Validation L1: 310916895482699.1250, Smoothed Validation Loss: 27356296568734114343396390731776.0000
Epoch [105/1000], Train Loss: 31939963739060903107007122243584.0000, Train L1 Loss: 189592291362283.8438
Epoch [105/1000], Validation Loss: 27356332762216661300022706438144.0000, Validation L1: 310916903822061.5625, Smoothed Validation Loss: 27356300188082372191578761461760.0000
Epoch [106/1000], Train Loss: 31940014897564694880223632556032.0000, Train L1 Loss: 189592383578440.0000
Epoch [106/1000], Validation Loss: 27356305639463397227890292555776.0000, Validation L1: 310916788784162.1875, Smoothed Validation Loss: 27356300733220471993050138148864.0000
Epoch [107/1000], Train Loss: 31939994632593494525059035824128.0000, Train L1 Loss: 189592348745274.9688
Epoch [107/1000], Validation Loss: 27356332698015840006422478716928.0000, Validation L1: 310916898861803.7500, Smoothed Validation Loss: 27356303929700009244747334942720.0000
Epoch [108/1000], Train Loss: 31940008232851357217077793390592.0000, Train L1 Loss: 189592345434072.4062
Epoch [108/1000], Validation Loss: 27356344977722113079769684770816.0000, Validation L1: 310916980595840.2500, Smoothed Validation Loss: 27356308034502219177889607188480.0000
Epoch [109/1000], Train Loss: 31939979966567386394700304875520.0000, Train L1 Loss: 189592305963469.8438
Epoch [109/1000], Validation Loss: 27356281342703740214398389583872.0000, Validation L1: 310916685010407.6875, Smoothed Validation Loss: 27356305365322374884420187324416.0000
Epoch [110/1000], Train Loss: 31940001766481370498529511866368.0000, Train L1 Loss: 189592368645795.7500
Epoch [110/1000], Validation Loss: 27356241968718504446944509689856.0000, Validation L1: 310916491615781.1250, Smoothed Validation Loss: 27356299025661987840672619560960.0000
Epoch [111/1000], Train Loss: 31940029586859560212516759928832.0000, Train L1 Loss: 189592406595486.2500
Epoch [111/1000], Validation Loss: 27356281028786633228016284598272.0000, Validation L1: 310916656719136.5000, Smoothed Validation Loss: 27356297225974455982286687961088.0000
Epoch [112/1000], Train Loss: 31940004024103473810839108059136.0000, Train L1 Loss: 189592357302402.6250
Epoch [112/1000], Validation Loss: 27356299618889330808422175604736.0000, Validation L1: 310916769466529.6875, Smoothed Validation Loss: 27356297465265944365620162199552.0000
Epoch [113/1000], Train Loss: 31939951364642335595790296154112.0000, Train L1 Loss: 189592278291131.0000
Epoch [113/1000], Validation Loss: 27356296453698245723106838577152.0000, Validation L1: 310916737739544.8125, Smoothed Validation Loss: 27356297364109174501368829837312.0000
Epoch [114/1000], Train Loss: 31939995530500214966723863904256.0000, Train L1 Loss: 189592352426321.0938
Epoch [114/1000], Validation Loss: 27356278113436524998365831757824.0000, Validation L1: 310916644581061.5625, Smoothed Validation Loss: 27356295439041906398548790870016.0000
Epoch [115/1000], Train Loss: 31940005685628324300056554373120.0000, Train L1 Loss: 189592360627559.4375
Epoch [115/1000], Validation Loss: 27356323796636409205458986860544.0000, Validation L1: 310916867392811.0625, Smoothed Validation Loss: 27356298274801357579959735943168.0000
Epoch [116/1000], Train Loss: 31940005083658273980081848188928.0000, Train L1 Loss: 189592358538115.1562
Epoch [116/1000], Validation Loss: 27356305606693085143718072156160.0000, Validation L1: 310916789933634.9375, Smoothed Validation Loss: 27356299007990529435615644090368.0000
Epoch [117/1000], Train Loss: 31939982510361927994596187439104.0000, Train L1 Loss: 189592333882822.7812
Epoch [117/1000], Validation Loss: 27356308654374366247038186684416.0000, Validation L1: 310916811477305.2500, Smoothed Validation Loss: 27356299972628914017477823823872.0000
Epoch [118/1000], Train Loss: 31939962657172833450427385118720.0000, Train L1 Loss: 189592286174369.1562
Epoch [118/1000], Validation Loss: 27356326496429976369137618780160.0000, Validation L1: 310916870555588.9375, Smoothed Validation Loss: 27356302625009021153363728793600.0000
Epoch [119/1000], Train Loss: 31940002601664454827971262283776.0000, Train L1 Loss: 189592382621619.2188
Epoch [119/1000], Validation Loss: 27356296584625511484936295546880.0000, Validation L1: 310916750706354.1250, Smoothed Validation Loss: 27356302020970670186520985468928.0000
Epoch [120/1000], Train Loss: 31939988009956950410463687999488.0000, Train L1 Loss: 189592305058320.6250
Epoch [120/1000], Validation Loss: 27356305664997654193576398028800.0000, Validation L1: 310916788487163.7500, Smoothed Validation Loss: 27356302385373367686506601250816.0000
Epoch [121/1000], Train Loss: 31939984928547603711816233910272.0000, Train L1 Loss: 189592312191894.6875
Epoch [121/1000], Validation Loss: 27356281338985892621214478761984.0000, Validation L1: 310916684404996.1875, Smoothed Validation Loss: 27356300280734621080697314476032.0000
Epoch [122/1000], Train Loss: 31940011385564336829236206632960.0000, Train L1 Loss: 189592403237363.8750
Epoch [122/1000], Validation Loss: 27356287418476864517475978444800.0000, Validation L1: 310916692380606.8125, Smoothed Validation Loss: 27356298994508846325095106347008.0000
Epoch [123/1000], Train Loss: 31940006159783497021081652297728.0000, Train L1 Loss: 189592360017444.6562
Epoch [123/1000], Validation Loss: 27356344880988418481551463940096.0000, Validation L1: 310916971354220.5625, Smoothed Validation Loss: 27356303583156799937861040209920.0000
Epoch [124/1000], Train Loss: 31939992928094773973915541700608.0000, Train L1 Loss: 189592351442147.4062
Epoch [124/1000], Validation Loss: 27356326812337088922865924833280.0000, Validation L1: 310916897440669.6250, Smoothed Validation Loss: 27356305906074828836361528672256.0000
Epoch [125/1000], Train Loss: 31940008456117124096385410400256.0000, Train L1 Loss: 189592361206335.1250
Epoch [125/1000], Validation Loss: 27356296456864915772295383875584.0000, Validation L1: 310916735300146.7500, Smoothed Validation Loss: 27356304961153838430674839666688.0000
Epoch [126/1000], Train Loss: 31939999655052884504505781059584.0000, Train L1 Loss: 189592353739530.3125
Epoch [126/1000], Validation Loss: 27356290519950954520759127506944.0000, Validation L1: 310916727793232.1875, Smoothed Validation Loss: 27356303517033549589323305713664.0000
Epoch [127/1000], Train Loss: 31939994313378731239406978465792.0000, Train L1 Loss: 189592355342938.5625
Epoch [127/1000], Validation Loss: 27356305449786341060640289849344.0000, Validation L1: 310916774305645.1250, Smoothed Validation Loss: 27356303710308828736455004127232.0000
Epoch [128/1000], Train Loss: 31939986030955487400978945146880.0000, Train L1 Loss: 189592320095102.8438
Epoch [128/1000], Validation Loss: 27356290594276160510664009318400.0000, Validation L1: 310916733762438.8750, Smoothed Validation Loss: 27356302398705562814595830120448.0000
Epoch [129/1000], Train Loss: 31939961827361377044135147470848.0000, Train L1 Loss: 189592280666140.8125
Epoch [129/1000], Validation Loss: 27356326846677441405532420177920.0000, Validation L1: 310916893034648.1875, Smoothed Validation Loss: 27356304843502752024769377337344.0000
Epoch [130/1000], Train Loss: 31939965778574324984109938507776.0000, Train L1 Loss: 189592271072226.8438
Epoch [130/1000], Validation Loss: 27356317601466301539732097597440.0000, Validation L1: 310916841239480.2500, Smoothed Validation Loss: 27356306119299104274105872941056.0000
Epoch [131/1000], Train Loss: 31939961513419054403439395078144.0000, Train L1 Loss: 189592253821034.5938
Epoch [131/1000], Validation Loss: 27356278407642196070879457181696.0000, Validation L1: 310916667801692.3750, Smoothed Validation Loss: 27356303348133417957382858735616.0000
Epoch [132/1000], Train Loss: 31940007886760538996360492351488.0000, Train L1 Loss: 189592341594418.3750
Epoch [132/1000], Validation Loss: 27356305653148530451577292455936.0000, Validation L1: 310916790424973.1875, Smoothed Validation Loss: 27356303578634933710401929478144.0000
Epoch [133/1000], Train Loss: 31939991941710907210082625257472.0000, Train L1 Loss: 189592358949254.6875
Epoch [133/1000], Validation Loss: 27356269262566301587451781578752.0000, Validation L1: 310916626337766.0625, Smoothed Validation Loss: 27356300147028071398826840162304.0000
Epoch [134/1000], Train Loss: 31939974838829748344814863122432.0000, Train L1 Loss: 189592301004798.1250
Epoch [134/1000], Validation Loss: 27356299186096806835836174729216.0000, Validation L1: 310916741106490.6250, Smoothed Validation Loss: 27356300050934946293607661830144.0000
Epoch [135/1000], Train Loss: 31939961408895334910970724089856.0000, Train L1 Loss: 189592303758316.7812
Epoch [135/1000], Validation Loss: 27356275159940126284153605849088.0000, Validation L1: 310916620230792.1250, Smoothed Validation Loss: 27356297561835464743022218969088.0000
Epoch [136/1000], Train Loss: 31939998015897692587614485348352.0000, Train L1 Loss: 189592334607245.5312
Epoch [136/1000], Validation Loss: 27356299499158455072999253999616.0000, Validation L1: 310916765285302.4375, Smoothed Validation Loss: 27356297755567764676739847946240.0000
Epoch [137/1000], Train Loss: 31939992619376671936965838372864.0000, Train L1 Loss: 189592342082538.5625
Epoch [137/1000], Validation Loss: 27356338700518199611150322106368.0000, Validation L1: 310916943942507.2500, Smoothed Validation Loss: 27356301850062811322700634521600.0000
Epoch [138/1000], Train Loss: 31940027739033160023558653476864.0000, Train L1 Loss: 189592395830742.7812
Epoch [138/1000], Validation Loss: 27356317701643696111017305047040.0000, Validation L1: 310916855880795.1250, Smoothed Validation Loss: 27356303435220897549732487888896.0000
Epoch [139/1000], Train Loss: 31939977915893675345803955142656.0000, Train L1 Loss: 189592310368726.1562
Epoch [139/1000], Validation Loss: 27356290135413770972308357251072.0000, Validation L1: 310916698772356.9375, Smoothed Validation Loss: 27356302105240184441630112088064.0000
Epoch [140/1000], Train Loss: 31940004320208844270970901364736.0000, Train L1 Loss: 189592348278666.8438
Epoch [140/1000], Validation Loss: 27356323645206456600429445775360.0000, Validation L1: 310916861634520.0000, Smoothed Validation Loss: 27356304259236811207150082719744.0000
Epoch [141/1000], Train Loss: 31939997058132998994620563062784.0000, Train L1 Loss: 189592337492206.5938
Epoch [141/1000], Validation Loss: 27356266180574729528977869766656.0000, Validation L1: 310916589263423.9375, Smoothed Validation Loss: 27356300451370602138612935950336.0000
Epoch [142/1000], Train Loss: 31940004471830929443303322550272.0000, Train L1 Loss: 189592357402617.5000
Epoch [142/1000], Validation Loss: 27356353947931345015329894957056.0000, Validation L1: 310917015774849.6875, Smoothed Validation Loss: 27356305801026674174484818165760.0000
Epoch [143/1000], Train Loss: 31940011324742548321653552578560.0000, Train L1 Loss: 189592344519865.9375
Epoch [143/1000], Validation Loss: 27356314710682599694248066416640.0000, Validation L1: 310916829206941.0000, Smoothed Validation Loss: 27356306691992266726461142990848.0000
Epoch [144/1000], Train Loss: 31939988720285981161976152195072.0000, Train L1 Loss: 189592304931652.1250
Epoch [144/1000], Validation Loss: 27356287452966461788193904656384.0000, Validation L1: 310916708550851.5625, Smoothed Validation Loss: 27356304768089688034074270105600.0000
Epoch [145/1000], Train Loss: 31939977631120667592028267216896.0000, Train L1 Loss: 189592299403324.5000
Epoch [145/1000], Validation Loss: 27356305342946420279814972768256.0000, Validation L1: 310916769293355.4375, Smoothed Validation Loss: 27356304825575363060088191320064.0000
Epoch [146/1000], Train Loss: 31940016580911314025499844411392.0000, Train L1 Loss: 189592382713402.6250
Epoch [146/1000], Validation Loss: 27356260251480210684458047635456.0000, Validation L1: 310916578839080.8125, Smoothed Validation Loss: 27356300368165846921805251477504.0000
Epoch [147/1000], Train Loss: 31939978043992707563242504847360.0000, Train L1 Loss: 189592329402786.6875
Epoch [147/1000], Validation Loss: 27356314577049864010270194532352.0000, Validation L1: 310916818405171.0625, Smoothed Validation Loss: 27356301789054249531371671257088.0000
Epoch [148/1000], Train Loss: 31940029242182602058816152403968.0000, Train L1 Loss: 189592406470269.6875
Epoch [148/1000], Validation Loss: 27356305708651279568859239022592.0000, Validation L1: 310916793070719.5000, Smoothed Validation Loss: 27356302181013950733680577085440.0000
Epoch [149/1000], Train Loss: 31939957198435236969601304625152.0000, Train L1 Loss: 189592273731494.5312
Epoch [149/1000], Validation Loss: 27356290705351387978258479841280.0000, Validation L1: 310916740347081.5625, Smoothed Validation Loss: 27356301033447694458138367361024.0000
Epoch [150/1000], Train Loss: 31939982861170843285736386461696.0000, Train L1 Loss: 189592301135261.0000
Epoch [150/1000], Validation Loss: 27356257274639371776573464117248.0000, Validation L1: 310916557314676.0625, Smoothed Validation Loss: 27356296657566860388542026088448.0000
Epoch [151/1000], Train Loss: 31939989659449186998064072622080.0000, Train L1 Loss: 189592313997193.2188
Epoch [151/1000], Validation Loss: 27356332783183844905190156140544.0000, Validation L1: 310916898728522.8125, Smoothed Validation Loss: 27356300270128558389846876356608.0000
Epoch [152/1000], Train Loss: 31939989501524426737217326546944.0000, Train L1 Loss: 189592304614729.8125
Epoch [152/1000], Validation Loss: 27356275355762037898175989153792.0000, Validation L1: 310916641582844.0625, Smoothed Validation Loss: 27356297778691906791039750373376.0000
Epoch [153/1000], Train Loss: 31939986816279476960980694466560.0000, Train L1 Loss: 189592333246851.5000
Epoch [153/1000], Validation Loss: 27356317680799447264878187773952.0000, Validation L1: 310916847268036.5000, Smoothed Validation Loss: 27356299768902662639863445061632.0000
Epoch [154/1000], Train Loss: 31939961172883057027914156474368.0000, Train L1 Loss: 189592304018434.9062
Epoch [154/1000], Validation Loss: 27356278038312542564152009293824.0000, Validation L1: 310916641178979.8125, Smoothed Validation Loss: 27356297595843649731572376010752.0000
Epoch [155/1000], Train Loss: 31939959906846018681888407814144.0000, Train L1 Loss: 189592273707044.7812
Epoch [155/1000], Validation Loss: 27356296583953898679705788219392.0000, Validation L1: 310916746212333.0000, Smoothed Validation Loss: 27356297494654674626385717231616.0000
Epoch [156/1000], Train Loss: 31940001682477474045843069730816.0000, Train L1 Loss: 189592365567682.1562
Epoch [156/1000], Validation Loss: 27356278129828060389324112265216.0000, Validation L1: 310916645197258.8750, Smoothed Validation Loss: 27356295558172015454479370420224.0000
Epoch [157/1000], Train Loss: 31939996308725139901704854044672.0000, Train L1 Loss: 189592354575788.2188
Epoch [157/1000], Validation Loss: 27356317674538457494514804195328.0000, Validation L1: 310916844658184.5000, Smoothed Validation Loss: 27356297769808660108842876534784.0000
Epoch [158/1000], Train Loss: 31939992035972823670816686211072.0000, Train L1 Loss: 189592332379769.1875
Epoch [158/1000], Validation Loss: 27356290269515349391894007250944.0000, Validation L1: 310916711517662.8750, Smoothed Validation Loss: 27356297019779326785348175921152.0000
Epoch [159/1000], Train Loss: 31939945745007760726039900192768.0000, Train L1 Loss: 189592228609997.5312
Epoch [159/1000], Validation Loss: 27356308661366839676078340964352.0000, Validation L1: 310916809766454.2500, Smoothed Validation Loss: 27356298183938078074421192425472.0000
Epoch [160/1000], Train Loss: 31939985368920667641985546321920.0000, Train L1 Loss: 189592318384676.0312
Epoch [160/1000], Validation Loss: 27356278215592215777966076985344.0000, Validation L1: 310916651145566.5625, Smoothed Validation Loss: 27356296187103490944055755407360.0000
Epoch [161/1000], Train Loss: 31939993287717553491393344700416.0000, Train L1 Loss: 189592376888874.0312
Epoch [161/1000], Validation Loss: 27356317644259171932634125172736.0000, Validation L1: 310916844904829.0000, Smoothed Validation Loss: 27356298332819060844353443332096.0000
Epoch [162/1000], Train Loss: 31939976124904841664084509196288.0000, Train L1 Loss: 189592333081867.4375
Epoch [162/1000], Validation Loss: 27356260149087544996065194278912.0000, Validation L1: 310916574962162.9375, Smoothed Validation Loss: 27356294514445908809164655689728.0000
Epoch [163/1000], Train Loss: 31940000217457614140529799331840.0000, Train L1 Loss: 189592351237311.4375
Epoch [163/1000], Validation Loss: 27356287454412959441710152155136.0000, Validation L1: 310916701682657.8125, Smoothed Validation Loss: 27356293808442612521339317125120.0000
Epoch [164/1000], Train Loss: 31939969901673011885794918400000.0000, Train L1 Loss: 189592299069229.7188
Epoch [164/1000], Validation Loss: 27356317865450004362822588301312.0000, Validation L1: 310916860584934.3750, Smoothed Validation Loss: 27356296214143350804767718768640.0000
Epoch [165/1000], Train Loss: 31939979225475050214955144970240.0000, Train L1 Loss: 189592301396004.2812
Epoch [165/1000], Validation Loss: 27356305480027692802859627184128.0000, Validation L1: 310916779162864.9375, Smoothed Validation Loss: 27356297140731785905296835084288.0000
Epoch [166/1000], Train Loss: 31939976847366916588904397144064.0000, Train L1 Loss: 189592294805350.5000
Epoch [166/1000], Validation Loss: 27356281181336716628765788078080.0000, Validation L1: 310916665393159.6250, Smoothed Validation Loss: 27356295544792280328723618594816.0000
Epoch [167/1000], Train Loss: 31939987767384909454164350730240.0000, Train L1 Loss: 189592336536930.6250
Epoch [167/1000], Validation Loss: 27356317692930847624321621295104.0000, Validation L1: 310916848489209.5000, Smoothed Validation Loss: 27356297759606137959003344338944.0000
Epoch [168/1000], Train Loss: 31940002228736132484999009009664.0000, Train L1 Loss: 189592362499221.7188
Epoch [168/1000], Validation Loss: 27356266046135854015300306468864.0000, Validation L1: 310916584827812.1875, Smoothed Validation Loss: 27356294588259109564633040551936.0000
Epoch [169/1000], Train Loss: 31940032545687085978429555736576.0000, Train L1 Loss: 189592389186899.0938
Epoch [169/1000], Validation Loss: 27356250826923128081407564316672.0000, Validation L1: 310916515150124.5000, Smoothed Validation Loss: 27356290212125515469550157561856.0000
Epoch [170/1000], Train Loss: 31940006559118482124356831936512.0000, Train L1 Loss: 189592400577170.8438
Epoch [170/1000], Validation Loss: 27356299344386520796086516318208.0000, Validation L1: 310916755617874.1250, Smoothed Validation Loss: 27356291125351617353283681648640.0000
Epoch [171/1000], Train Loss: 31940006821030898414026338861056.0000, Train L1 Loss: 189592357731253.1250
Epoch [171/1000], Validation Loss: 27356308647931629210112639369216.0000, Validation L1: 310916811793530.4375, Smoothed Validation Loss: 27356292877609620340406428368896.0000
Epoch [172/1000], Train Loss: 31940008430068137218488248827904.0000, Train L1 Loss: 189592380363077.1562
Epoch [172/1000], Validation Loss: 27356305317361578883114241884160.0000, Validation L1: 310916765434103.1250, Smoothed Validation Loss: 27356294121584816645037172457472.0000
Epoch [173/1000], Train Loss: 31940003282519191429397759393792.0000, Train L1 Loss: 189592343781972.7188
Epoch [173/1000], Validation Loss: 27356317567447208832884449214464.0000, Validation L1: 310916837432118.5625, Smoothed Validation Loss: 27356296466171054963101974659072.0000
Epoch [174/1000], Train Loss: 31940009233306572397842121359360.0000, Train L1 Loss: 189592384160198.7812
Epoch [174/1000], Validation Loss: 27356275128721254732014620246016.0000, Validation L1: 310916621488325.1875, Smoothed Validation Loss: 27356294332426075390353201954816.0000
Epoch [175/1000], Train Loss: 31939985137298543711686011912192.0000, Train L1 Loss: 189592340557117.0312
Epoch [175/1000], Validation Loss: 27356326700058220411661160808448.0000, Validation L1: 310916887484590.0000, Smoothed Validation Loss: 27356297569189288991764072366080.0000
Epoch [176/1000], Train Loss: 31939968816563566955352966561792.0000, Train L1 Loss: 189592289043791.5000
Epoch [176/1000], Validation Loss: 27356278200147872957036731826176.0000, Validation L1: 310916648224572.6875, Smoothed Validation Loss: 27356295632285146937931375575040.0000
Epoch [177/1000], Train Loss: 31939975157108280821931004919808.0000, Train L1 Loss: 189592312726187.8438
Epoch [177/1000], Validation Loss: 27356296260900577820057408634880.0000, Validation L1: 310916725864318.6250, Smoothed Validation Loss: 27356295695146692277943792566272.0000
Epoch [178/1000], Train Loss: 31939974172177270794288183115776.0000, Train L1 Loss: 189592305149360.9062
Epoch [178/1000], Validation Loss: 27356296540540121509777817731072.0000, Validation L1: 310916748728954.8125, Smoothed Validation Loss: 27356295779686035201127195082752.0000
Epoch [179/1000], Train Loss: 31939964421308927332352484442112.0000, Train L1 Loss: 189592266006330.1250
Epoch [179/1000], Validation Loss: 27356305667566755119008034324480.0000, Validation L1: 310916792171696.3125, Smoothed Validation Loss: 27356296768474103590035577110528.0000
Epoch [180/1000], Train Loss: 31939997727092377900273369088000.0000, Train L1 Loss: 189592330258871.1250
Epoch [180/1000], Validation Loss: 27356317611275731499696223420416.0000, Validation L1: 310916844804968.7500, Smoothed Validation Loss: 27356298852754265029921753530368.0000
Epoch [181/1000], Train Loss: 31940017857481862072379092500480.0000, Train L1 Loss: 189592379921839.1875
Epoch [181/1000], Validation Loss: 27356326956298019704285102604288.0000, Validation L1: 310916899112736.2500, Smoothed Validation Loss: 27356301663108640497358088437760.0000
Epoch [182/1000], Train Loss: 31939991341937010226797377224704.0000, Train L1 Loss: 189592327156146.8750
Epoch [182/1000], Validation Loss: 27356317750738138210524951740416.0000, Validation L1: 310916852684679.4375, Smoothed Validation Loss: 27356303271871592070114625716224.0000
Epoch [183/1000], Train Loss: 31939978263113361345518317338624.0000, Train L1 Loss: 189592299285968.6562
Epoch [183/1000], Validation Loss: 27356287338878330673488199680000.0000, Validation L1: 310916690711151.6250, Smoothed Validation Loss: 27356301678572263228292206690304.0000
Epoch [184/1000], Train Loss: 31940033157679437901955308978176.0000, Train L1 Loss: 189592377725680.0625
Epoch [184/1000], Validation Loss: 27356268977300960322411951030272.0000, Validation L1: 310916598491677.1250, Smoothed Validation Loss: 27356298408445131586624292913152.0000
Epoch [185/1000], Train Loss: 31939998711217874098564703977472.0000, Train L1 Loss: 189592353940036.5938
Epoch [185/1000], Validation Loss: 27356239088227977708199351418880.0000, Validation L1: 310916479858571.5625, Smoothed Validation Loss: 27356292476423417099501724237824.0000
Epoch [186/1000], Train Loss: 31940040795337910048059759263744.0000, Train L1 Loss: 189592424122125.0938
Epoch [186/1000], Validation Loss: 27356314702811798237081099042816.0000, Validation L1: 310916836926624.0000, Smoothed Validation Loss: 27356294699062256564339549929472.0000
Epoch [187/1000], Train Loss: 31940021446984395894807741857792.0000, Train L1 Loss: 189592403676723.6875
Epoch [187/1000], Validation Loss: 27356275171364799272071924285440.0000, Validation L1: 310916624222596.9375, Smoothed Validation Loss: 27356292746292509484032899153920.0000
Epoch [188/1000], Train Loss: 31939957520956308914488156880896.0000, Train L1 Loss: 189592271851598.1250
Epoch [188/1000], Validation Loss: 27356260170685786491818679992320.0000, Validation L1: 310916570971013.7500, Smoothed Validation Loss: 27356289488731834933011663552512.0000
Epoch [189/1000], Train Loss: 31939990761747939461056341999616.0000, Train L1 Loss: 189592325162071.9375
Epoch [189/1000], Validation Loss: 27356314562296792206944828915712.0000, Validation L1: 310916820670052.2500, Smoothed Validation Loss: 27356291996088328408605166403584.0000
Epoch [190/1000], Train Loss: 31939992772316663482654197284864.0000, Train L1 Loss: 189592332068602.1250
Epoch [190/1000], Validation Loss: 27356299639481044809056119685120.0000, Validation L1: 310916769800440.0625, Smoothed Validation Loss: 27356292760427597346490485309440.0000
Epoch [191/1000], Train Loss: 31939991901959187041154699886592.0000, Train L1 Loss: 189592331306060.6562
Epoch [191/1000], Validation Loss: 27356290364692370275311988768768.0000, Validation L1: 310916714739175.5625, Smoothed Validation Loss: 27356292520854075540092561129472.0000
Epoch [192/1000], Train Loss: 31940022614202478439550555258880.0000, Train L1 Loss: 189592402757982.5000
Epoch [192/1000], Validation Loss: 27356266151173447736050833162240.0000, Validation L1: 310916589894267.5000, Smoothed Validation Loss: 27356289883886011408608500121600.0000
Epoch [193/1000], Train Loss: 31940002122577268557822795186176.0000, Train L1 Loss: 189592366462777.7812
Epoch [193/1000], Validation Loss: 27356317551443780147014075940864.0000, Validation L1: 310916837749532.8125, Smoothed Validation Loss: 27356292650641786481009206755328.0000
Epoch [194/1000], Train Loss: 31940009916710053654384540123136.0000, Train L1 Loss: 189592366236601.0000
Epoch [194/1000], Validation Loss: 27356299358932940426910359355392.0000, Validation L1: 310916746827236.2500, Smoothed Validation Loss: 27356293321470902325959284752384.0000
Epoch [195/1000], Train Loss: 31939976968256140666485147172864.0000, Train L1 Loss: 189592313978127.6875
Epoch [195/1000], Validation Loss: 27356296259971336598143172083712.0000, Validation L1: 310916722838471.5625, Smoothed Validation Loss: 27356293615320946653897598959616.0000
Epoch [196/1000], Train Loss: 31939971855523415711087629172736.0000, Train L1 Loss: 189592301806116.6250
Epoch [196/1000], Validation Loss: 27356275256879563327748620419072.0000, Validation L1: 310916638698617.3750, Smoothed Validation Loss: 27356291779476810122722552053760.0000
Epoch [197/1000], Train Loss: 31939988815686803925276683141120.0000, Train L1 Loss: 189592342591002.8750
Epoch [197/1000], Validation Loss: 27356281353772790961341024174080.0000, Validation L1: 310916676221174.3125, Smoothed Validation Loss: 27356290736906408206584399265792.0000
Epoch [198/1000], Train Loss: 31939999766666963163915504058368.0000, Train L1 Loss: 189592353664118.6562
Epoch [198/1000], Validation Loss: 27356305508900432143518462377984.0000, Validation L1: 310916779048356.0000, Smoothed Validation Loss: 27356292214105807447758066417664.0000
Epoch [199/1000], Train Loss: 31940001917729008383443840532480.0000, Train L1 Loss: 189592362937233.3750
Epoch [199/1000], Validation Loss: 27356278425999030281628184215552.0000, Validation L1: 310916669776307.8125, Smoothed Validation Loss: 27356290835295130631865003671552.0000
Epoch [200/1000], Train Loss: 31939985925880144508151798956032.0000, Train L1 Loss: 189592316469962.8750
Epoch [200/1000], Validation Loss: 27356299488575545387833127600128.0000, Validation L1: 310916763060236.1875, Smoothed Validation Loss: 27356291700623171657101853327360.0000
Epoch [201/1000], Train Loss: 31940003254338547265074712543232.0000, Train L1 Loss: 189592317489170.9375
Epoch [201/1000], Validation Loss: 27356275358946109856324694048768.0000, Validation L1: 310916641312263.0000, Smoothed Validation Loss: 27356290066455468629543876558848.0000
Epoch [202/1000], Train Loss: 31939984409294577776204242223104.0000, Train L1 Loss: 189592314524756.3438
Epoch [202/1000], Validation Loss: 27356296565479344878297223790592.0000, Validation L1: 310916744445292.3750, Smoothed Validation Loss: 27356290716357856704779174019072.0000
Epoch [203/1000], Train Loss: 31939996082507380560246188539904.0000, Train L1 Loss: 189592355662276.3125
Epoch [203/1000], Validation Loss: 27356323666491860051667267354624.0000, Validation L1: 310916863551237.1250, Smoothed Validation Loss: 27356294011371258390547871563776.0000
Epoch [204/1000], Train Loss: 31939979301743505400874867359744.0000, Train L1 Loss: 189592311813894.8750
Epoch [204/1000], Validation Loss: 27356305490277399165995120066560.0000, Validation L1: 310916776902072.1250, Smoothed Validation Loss: 27356295159261872918452559151104.0000
Epoch [205/1000], Train Loss: 31940015269734246254376877293568.0000, Train L1 Loss: 189592372520334.6250
Epoch [205/1000], Validation Loss: 27356305692867477926016842727424.0000, Validation L1: 310916795797954.3750, Smoothed Validation Loss: 27356296212622431167409173823488.0000
Epoch [206/1000], Train Loss: 31939960487480189206001723899904.0000, Train L1 Loss: 189592259162490.9375
Epoch [206/1000], Validation Loss: 27356305462347344292138222354432.0000, Validation L1: 310916775030834.2500, Smoothed Validation Loss: 27356297137594920678442227728384.0000
Epoch [207/1000], Train Loss: 31940030022150564164777600352256.0000, Train L1 Loss: 189592401888181.5625
Epoch [207/1000], Validation Loss: 27356269491737818802115424813056.0000, Validation L1: 310916628382473.3125, Smoothed Validation Loss: 27356294373009209590089621962752.0000
Epoch [208/1000], Train Loss: 31939995840058837312928605011968.0000, Train L1 Loss: 189592346582129.0312
Epoch [208/1000], Validation Loss: 27356308506952432662783664848896.0000, Validation L1: 310916800233163.3125, Smoothed Validation Loss: 27356295786403527844119361617920.0000
Epoch [209/1000], Train Loss: 31940005761888686517445891981312.0000, Train L1 Loss: 189592377188287.8438
Epoch [209/1000], Validation Loss: 27356299125557533636478099259392.0000, Validation L1: 310916732757531.5625, Smoothed Validation Loss: 27356296120318927522635309907968.0000
Epoch [210/1000], Train Loss: 31940012244872465772162815361024.0000, Train L1 Loss: 189592368605736.9688
Epoch [210/1000], Validation Loss: 27356305449185646438741985722368.0000, Validation L1: 310916775440227.0625, Smoothed Validation Loss: 27356297053205601666045791174656.0000
Epoch [211/1000], Train Loss: 31939994516888553129728813301760.0000, Train L1 Loss: 189592338162452.5938
Epoch [211/1000], Validation Loss: 27356299506410115164194207694848.0000, Validation L1: 310916761376401.5000, Smoothed Validation Loss: 27356297298526054366940521037824.0000
Epoch [212/1000], Train Loss: 31939965540750028294580479197184.0000, Train L1 Loss: 189592297411399.5312
Epoch [212/1000], Validation Loss: 27356281251901119692240899276800.0000, Validation L1: 310916671352582.3125, Smoothed Validation Loss: 27356295693863558197310782439424.0000
Epoch [213/1000], Train Loss: 31939999848831319312806193397760.0000, Train L1 Loss: 189592345314198.6562
Epoch [213/1000], Validation Loss: 27356335815309287571606114140160.0000, Validation L1: 310916926716000.1875, Smoothed Validation Loss: 27356299706008128432580539187200.0000
Epoch [214/1000], Train Loss: 31940018201825405234866580094976.0000, Train L1 Loss: 189592427434819.6875
Epoch [214/1000], Validation Loss: 27356278400303022031725440008192.0000, Validation L1: 310916662313529.0625, Smoothed Validation Loss: 27356297575437619143574917480448.0000
Epoch [215/1000], Train Loss: 31939994565102622566878820696064.0000, Train L1 Loss: 189592351999620.6562
Epoch [215/1000], Validation Loss: 27356260173979710252078206025728.0000, Validation L1: 310916579410760.8750, Smoothed Validation Loss: 27356293835291826002625432649728.0000
Epoch [216/1000], Train Loss: 31940010263573243714795508596736.0000, Train L1 Loss: 189592364110848.2500
Epoch [216/1000], Validation Loss: 27356348042057993835482045218816.0000, Validation L1: 310916995213176.0625, Smoothed Validation Loss: 27356299255968443686631019380736.0000
Epoch [217/1000], Train Loss: 31940009748065415732904448753664.0000, Train L1 Loss: 189592397416126.0000
Epoch [217/1000], Validation Loss: 27356348149893845141503701155840.0000, Validation L1: 310917008549427.6875, Smoothed Validation Loss: 27356304145360984282478250295296.0000
Epoch [218/1000], Train Loss: 31940016784028084258342919208960.0000, Train L1 Loss: 189592375999761.0938
Epoch [218/1000], Validation Loss: 27356308612230257394857388539904.0000, Validation L1: 310916804941068.5625, Smoothed Validation Loss: 27356304592047914746235903279104.0000
Epoch [219/1000], Train Loss: 31940021937263851397703700316160.0000, Train L1 Loss: 189592411786229.7500
Epoch [219/1000], Validation Loss: 27356317772750800943989070495744.0000, Validation L1: 310916854033518.9375, Smoothed Validation Loss: 27356305910118201114211406315520.0000
Epoch [220/1000], Train Loss: 31940012332505538444969870622720.0000, Train L1 Loss: 189592367281645.2500
Epoch [220/1000], Validation Loss: 27356256984064218996869408227328.0000, Validation L1: 310916535952922.9375, Smoothed Validation Loss: 27356301017512806054996945666048.0000
Epoch [221/1000], Train Loss: 31939974376555661412344319180800.0000, Train L1 Loss: 189592309721643.6250
Epoch [221/1000], Validation Loss: 27356281231540985288045973471232.0000, Validation L1: 310916667780453.8125, Smoothed Validation Loss: 27356299038915626680461624868864.0000
Epoch [222/1000], Train Loss: 31939988691857323766173812129792.0000, Train L1 Loss: 189592346272123.5938
Epoch [222/1000], Validation Loss: 27356333009457714594406230654976.0000, Validation L1: 310916920045563.0000, Smoothed Validation Loss: 27356302435969836822935973658624.0000
Epoch [223/1000], Train Loss: 31939997912264249173084041379840.0000, Train L1 Loss: 189592342056827.0312
Epoch [223/1000], Validation Loss: 27356290458168732860243068846080.0000, Validation L1: 310916720545405.8750, Smoothed Validation Loss: 27356301238189728228106534125568.0000
Epoch [224/1000], Train Loss: 31939996476685149615031337353216.0000, Train L1 Loss: 189592329728766.1875
Epoch [224/1000], Validation Loss: 27356314731326370802974786060288.0000, Validation L1: 310916837227423.3750, Smoothed Validation Loss: 27356302587503394737393173004288.0000
Epoch [225/1000], Train Loss: 31939993796656025732835335733248.0000, Train L1 Loss: 189592377217258.2500
Epoch [225/1000], Validation Loss: 27356275246161914948930823520256.0000, Validation L1: 310916637840617.8125, Smoothed Validation Loss: 27356299853369245407467049844736.0000
Epoch [226/1000], Train Loss: 31940014368501261703528375648256.0000, Train L1 Loss: 189592387768788.2188
Epoch [226/1000], Validation Loss: 27356269037049401427203767402496.0000, Validation L1: 310916602224108.8750, Smoothed Validation Loss: 27356296771737263261240535285760.0000
Epoch [227/1000], Train Loss: 31940001347721738705656805851136.0000, Train L1 Loss: 189592363752407.1562
Epoch [227/1000], Validation Loss: 27356338913520753832039962116096.0000, Validation L1: 310916956504597.1875, Smoothed Validation Loss: 27356300985915609616160701546496.0000
Epoch [228/1000], Train Loss: 31940014590304444071450777747456.0000, Train L1 Loss: 189592358347063.9375
Epoch [228/1000], Validation Loss: 27356265953514909647191605772288.0000, Validation L1: 310916567359606.7500, Smoothed Validation Loss: 27356297482675540970343680180224.0000
Epoch [229/1000], Train Loss: 31939979978354770289407788318720.0000, Train L1 Loss: 189592305099887.1562
Epoch [229/1000], Validation Loss: 27356314670533229692621835730944.0000, Validation L1: 310916825555052.9375, Smoothed Validation Loss: 27356299201461309842571495735296.0000
Epoch [230/1000], Train Loss: 31940023056609521083827714260992.0000, Train L1 Loss: 189592419341721.2812
Epoch [230/1000], Validation Loss: 27356347871352283544535846354944.0000, Validation L1: 310916983299734.4375, Smoothed Validation Loss: 27356304068450410365287669956608.0000
Epoch [231/1000], Train Loss: 31939958553443412473722156613632.0000, Train L1 Loss: 189592289232638.0312
Epoch [231/1000], Validation Loss: 27356278044839195172934351060992.0000, Validation L1: 310916630673116.9375, Smoothed Validation Loss: 27356301466089289296412300804096.0000
Epoch [232/1000], Train Loss: 31940028528676930288540144631808.0000, Train L1 Loss: 189592411624942.5000
Epoch [232/1000], Validation Loss: 27356335819021037290894565310464.0000, Validation L1: 310916926967045.0000, Smoothed Validation Loss: 27356304901382464996580452728832.0000
Epoch [233/1000], Train Loss: 31940032364568882212216930041856.0000, Train L1 Loss: 189592431773693.4688
Epoch [233/1000], Validation Loss: 27356238912166951531953975721984.0000, Validation L1: 310916466989430.6875, Smoothed Validation Loss: 27356298302460912749397879554048.0000
Epoch [234/1000], Train Loss: 31940032609909182276669481680896.0000, Train L1 Loss: 189592398103051.9375
Epoch [234/1000], Validation Loss: 27356314701108784555989082832896.0000, Validation L1: 310916829125068.7500, Smoothed Validation Loss: 27356299942325696327177297985536.0000
Epoch [235/1000], Train Loss: 31939948207883939071551179063296.0000, Train L1 Loss: 189592238666083.7500
Epoch [235/1000], Validation Loss: 27356305634598820579587169189888.0000, Validation L1: 310916790431265.8750, Smoothed Validation Loss: 27356300511553010103498173317120.0000
Epoch [236/1000], Train Loss: 31940016626543276141494369517568.0000, Train L1 Loss: 189592365242537.5000
Epoch [236/1000], Validation Loss: 27356314706646541262193038458880.0000, Validation L1: 310916833068243.5000, Smoothed Validation Loss: 27356301931062360967567846146048.0000
Epoch [237/1000], Train Loss: 31939986789941908426160886251520.0000, Train L1 Loss: 189592326692805.9688
Epoch [237/1000], Validation Loss: 27356305538667275621798789513216.0000, Validation L1: 310916787085020.3750, Smoothed Validation Loss: 27356302291822853333710865956864.0000
Epoch [238/1000], Train Loss: 31939974738452276856484094017536.0000, Train L1 Loss: 189592292525699.7812
Epoch [238/1000], Validation Loss: 27356229835943511289248692043776.0000, Validation L1: 310916423760834.1875, Smoothed Validation Loss: 27356295046234920480344536776704.0000
Epoch [239/1000], Train Loss: 31939988725435433004708596285440.0000, Train L1 Loss: 189592328762279.4688
Epoch [239/1000], Validation Loss: 27356308356268996731987057180672.0000, Validation L1: 310916787879303.4375, Smoothed Validation Loss: 27356296377238329006228714291200.0000
Epoch [240/1000], Train Loss: 31939943787484324627455242403840.0000, Train L1 Loss: 189592247647011.3438
Epoch [240/1000], Validation Loss: 27356296469073201584577286504448.0000, Validation L1: 310916744296924.8125, Smoothed Validation Loss: 27356296386421817164783496986624.0000
Epoch [241/1000], Train Loss: 31940031490438812420463206072320.0000, Train L1 Loss: 189592390424248.0938
Epoch [241/1000], Validation Loss: 27356275458626500683532175671296.0000, Validation L1: 310916648183856.0625, Smoothed Validation Loss: 27356294293642286867738253066240.0000
Epoch [242/1000], Train Loss: 31939993479783535073782772269056.0000, Train L1 Loss: 189592335186464.4688
Epoch [242/1000], Validation Loss: 27356266218757301012137739550720.0000, Validation L1: 310916593343778.3125, Smoothed Validation Loss: 27356291486153786030378388029440.0000
Epoch [243/1000], Train Loss: 31940021173647540804400539762688.0000, Train L1 Loss: 189592411823392.6562
Epoch [243/1000], Validation Loss: 27356326572414312965365418688512.0000, Validation L1: 310916874515925.5625, Smoothed Validation Loss: 27356294994779840074956979306496.0000
Epoch [244/1000], Train Loss: 31939992149967365481666004910080.0000, Train L1 Loss: 189592334577914.4375
Epoch [244/1000], Validation Loss: 27356299204186870322657610432512.0000, Validation L1: 310916737486278.5625, Smoothed Validation Loss: 27356295415720542649367079682048.0000
Epoch [245/1000], Train Loss: 31940009814026761674838213918720.0000, Train L1 Loss: 189592358820888.5000
Epoch [245/1000], Validation Loss: 27356314614636672313123730882560.0000, Validation L1: 310916817148385.5000, Smoothed Validation Loss: 27356297335612156966822633013248.0000
Epoch [246/1000], Train Loss: 31939979999503854283524732354560.0000, Train L1 Loss: 189592316422462.7812
Epoch [246/1000], Validation Loss: 27356335747096110290789709381632.0000, Validation L1: 310916923842692.5000, Smoothed Validation Loss: 27356301176760552749579303387136.0000
Epoch [247/1000], Train Loss: 31939969130413128954523768848384.0000, Train L1 Loss: 189592324041154.7500
Epoch [247/1000], Validation Loss: 27356287423331925059766467952640.0000, Validation L1: 310916701548710.1875, Smoothed Validation Loss: 27356299801417692682757796265984.0000
Epoch [248/1000], Train Loss: 31939969931121549949611953618944.0000, Train L1 Loss: 189592303302872.0312
Epoch [248/1000], Validation Loss: 27356260351163073987860955660288.0000, Validation L1: 310916585473408.2500, Smoothed Validation Loss: 27356295856392231263628074942464.0000
Epoch [249/1000], Train Loss: 31940018043125260226175455723520.0000, Train L1 Loss: 189592381791912.1562
Epoch [249/1000], Validation Loss: 27356278270481966439167743229952.0000, Validation L1: 310916656480903.0000, Smoothed Validation Loss: 27356294097801207933701780930560.0000
Epoch [250/1000], Train Loss: 31939970839031494746806287335424.0000, Train L1 Loss: 189592283158035.5000
Epoch [250/1000], Validation Loss: 27356305550710725184119304617984.0000, Validation L1: 310916787758645.9375, Smoothed Validation Loss: 27356295243092160109103496036352.0000
Epoch [251/1000], Train Loss: 31939970564180723116461101416448.0000, Train L1 Loss: 189592298518859.4375
Epoch [251/1000], Validation Loss: 27356269268877222766883821846528.0000, Validation L1: 310916623495275.0625, Smoothed Validation Loss: 27356292645670668176321379565568.0000
Epoch [252/1000], Train Loss: 31940011936757427250515413041152.0000, Train L1 Loss: 189592346724861.8438
Epoch [252/1000], Validation Loss: 27356296368322593356319989694464.0000, Validation L1: 310916731424266.8750, Smoothed Validation Loss: 27356293017935862495761091526656.0000
Epoch [253/1000], Train Loss: 31940024396973616399205194006528.0000, Train L1 Loss: 189592371245664.1875
Epoch [253/1000], Validation Loss: 27356287268680907929249000718336.0000, Validation L1: 310916692211446.1875, Smoothed Validation Loss: 27356292443010364787310068760576.0000
Epoch [254/1000], Train Loss: 31940003953650282636562283888640.0000, Train L1 Loss: 189592369866343.4062
Epoch [254/1000], Validation Loss: 27356299440584205973854355456000.0000, Validation L1: 310916758571948.9375, Smoothed Validation Loss: 27356293142767749356324460167168.0000
Epoch [255/1000], Train Loss: 31940037339623076269187173187584.0000, Train L1 Loss: 189592447909805.5000
Epoch [255/1000], Validation Loss: 27356308694250381262081910374400.0000, Validation L1: 310916819413747.3750, Smoothed Validation Loss: 27356294697916009394380466028544.0000
Epoch [256/1000], Train Loss: 31939992548438659255603325566976.0000, Train L1 Loss: 189592331491768.0312
Epoch [256/1000], Validation Loss: 27356305598479618301703365853184.0000, Validation L1: 310916787236554.0000, Smoothed Validation Loss: 27356295787972370285112756011008.0000
Epoch [257/1000], Train Loss: 31939993809494599320166994018304.0000, Train L1 Loss: 189592373980513.4375
Epoch [257/1000], Validation Loss: 27356242057117675445164305285120.0000, Validation L1: 310916495507439.3125, Smoothed Validation Loss: 27356290414886902152197799149568.0000
Epoch [258/1000], Train Loss: 31939972481813174234840655986688.0000, Train L1 Loss: 189592284841684.0625
Epoch [258/1000], Validation Loss: 27356308786956281533561328107520.0000, Validation L1: 310916820364853.4375, Smoothed Validation Loss: 27356292252093841441414040256512.0000
Epoch [259/1000], Train Loss: 31940028320106841338906683637760.0000, Train L1 Loss: 189592374058258.0625
Epoch [259/1000], Validation Loss: 27356338887299900585163087675392.0000, Validation L1: 310916951505024.3750, Smoothed Validation Loss: 27356296915614449607588758683648.0000
Epoch [260/1000], Train Loss: 31940030874387402181585443749888.0000, Train L1 Loss: 189592390197684.6562
Epoch [260/1000], Validation Loss: 27356326625729578175240595308544.0000, Validation L1: 310916875728246.4375, Smoothed Validation Loss: 27356299886625964265793793294336.0000
Epoch [261/1000], Train Loss: 31939992399634967262476007112704.0000, Train L1 Loss: 189592327493789.7188
Epoch [261/1000], Validation Loss: 27356275300100699023615817940992.0000, Validation L1: 310916633360362.8750, Smoothed Validation Loss: 27356297427973437291216033021952.0000
Epoch [262/1000], Train Loss: 31940046330754500849637401821184.0000, Train L1 Loss: 189592403924667.0000
Epoch [262/1000], Validation Loss: 27356335528534101020691442696192.0000, Validation L1: 310916908184733.3750, Smoothed Validation Loss: 27356301238029503664163573989376.0000
Epoch [263/1000], Train Loss: 31940017297389983046588956672000.0000, Train L1 Loss: 189592378407353.5938
Epoch [263/1000], Validation Loss: 27356305470090567779061038317568.0000, Validation L1: 310916775819623.1875, Smoothed Validation Loss: 27356301661235611426733208633344.0000
Epoch [264/1000], Train Loss: 31939995899686009990554216038400.0000, Train L1 Loss: 189592330612917.5312
Epoch [264/1000], Validation Loss: 27356372288273774748993008435200.0000, Validation L1: 310917102224641.7500, Smoothed Validation Loss: 27356308723939425056799412191232.0000
Epoch [265/1000], Train Loss: 31939996391184986229346576367616.0000, Train L1 Loss: 189592357568951.6875
Epoch [265/1000], Validation Loss: 27356281363357590379091164397568.0000, Validation L1: 310916681416111.3125, Smoothed Validation Loss: 27356305987881238886868810989568.0000
Epoch [266/1000], Train Loss: 31939980465820975723873101152256.0000, Train L1 Loss: 189592313274427.4375
Epoch [266/1000], Validation Loss: 27356336044361090100974994849792.0000, Validation L1: 310916943478331.4375, Smoothed Validation Loss: 27356308993529222206839578427392.0000
Epoch [267/1000], Train Loss: 31939947540272077706804271775744.0000, Train L1 Loss: 189592251581876.3125
Epoch [267/1000], Validation Loss: 27356281039347493289406805049344.0000, Validation L1: 310916656228551.9375, Smoothed Validation Loss: 27356306198111048414376375615488.0000
Epoch [268/1000], Train Loss: 31939998091467670996526435401728.0000, Train L1 Loss: 189592340243297.3125
Epoch [268/1000], Validation Loss: 27356305385340596004905145073664.0000, Validation L1: 310916768099966.3750, Smoothed Validation Loss: 27356306116834004974869103509504.0000
Epoch [269/1000], Train Loss: 31939964777011926856554338320384.0000, Train L1 Loss: 189592275104191.0000
Epoch [269/1000], Validation Loss: 27356332596833890516654517911552.0000, Validation L1: 310916884077481.6875, Smoothed Validation Loss: 27356308764833996681567384109056.0000
Epoch [270/1000], Train Loss: 31939967878703311038258486444032.0000, Train L1 Loss: 189592286674288.1562
Epoch [270/1000], Validation Loss: 27356344698838313939918691237888.0000, Validation L1: 310916953752687.5625, Smoothed Validation Loss: 27356312358234432010282216718336.0000
Epoch [271/1000], Train Loss: 31940039868589957448729179979776.0000, Train L1 Loss: 189592417244802.9375
Epoch [271/1000], Validation Loss: 27356332923913384407175847215104.0000, Validation L1: 310916919738504.0625, Smoothed Validation Loss: 27356314414802328150691505242112.0000
Epoch [272/1000], Train Loss: 31939982105192520566863275491328.0000, Train L1 Loss: 189592331464547.6875
Epoch [272/1000], Validation Loss: 27356278291506210651613977116672.0000, Validation L1: 310916658649360.1250, Smoothed Validation Loss: 27356310802472718652583566114816.0000
Epoch [273/1000], Train Loss: 31939985578698567968484245897216.0000, Train L1 Loss: 189592308593366.8750
Epoch [273/1000], Validation Loss: 27356305366836061740777175252992.0000, Validation L1: 310916766807083.4375, Smoothed Validation Loss: 27356310258909054762842777976832.0000
Epoch [274/1000], Train Loss: 31939969677030994499958778888192.0000, Train L1 Loss: 189592315274088.5938
Epoch [274/1000], Validation Loss: 27356299505720037600491481333760.0000, Validation L1: 310916764995090.3750, Smoothed Validation Loss: 27356309183590151695527760101376.0000
Epoch [275/1000], Train Loss: 31939981601678742162980103782400.0000, Train L1 Loss: 189592316885428.1250
Epoch [275/1000], Validation Loss: 27356296521544411159489939505152.0000, Validation L1: 310916745562845.3750, Smoothed Validation Loss: 27356307917385579443363828989952.0000
Epoch [276/1000], Train Loss: 31939952856975243715211824201728.0000, Train L1 Loss: 189592276058280.9375
Epoch [276/1000], Validation Loss: 27356281380247593184006066143232.0000, Validation L1: 310916682483431.5625, Smoothed Validation Loss: 27356305263671780817428052705280.0000
Epoch [277/1000], Train Loss: 31940000119743783141008427974656.0000, Train L1 Loss: 189592323971864.6250
Epoch [277/1000], Validation Loss: 27356308667217285808010257498112.0000, Validation L1: 310916813339458.3750, Smoothed Validation Loss: 27356305604026332667566161395712.0000
Epoch [278/1000], Train Loss: 31940028742887237339499867406336.0000, Train L1 Loss: 189592374099847.6250
Epoch [278/1000], Validation Loss: 27356287424763421222923944329216.0000, Validation L1: 310916704858537.6875, Smoothed Validation Loss: 27356303786100041973461902426112.0000
Epoch [279/1000], Train Loss: 31939978642372465742279314767872.0000, Train L1 Loss: 189592303655918.4688
Epoch [279/1000], Validation Loss: 27356323698498262559845649481728.0000, Validation L1: 310916865379880.4375, Smoothed Validation Loss: 27356305777339865833540128079872.0000
Epoch [280/1000], Train Loss: 31940062449352632105248036487168.0000, Train L1 Loss: 189592447311842.0938
Epoch [280/1000], Validation Loss: 27356317620385770451928220696576.0000, Validation L1: 310916839617551.5625, Smoothed Validation Loss: 27356306961644456745738900078592.0000
Epoch [281/1000], Train Loss: 31940008846913788709324395118592.0000, Train L1 Loss: 189592357001668.7188
Epoch [281/1000], Validation Loss: 27356332622346768894909495640064.0000, Validation L1: 310916900573246.7500, Smoothed Validation Loss: 27356309527714684808136220475392.0000
Epoch [282/1000], Train Loss: 31939996854291054646178663628800.0000, Train L1 Loss: 189592344241484.5000
Epoch [282/1000], Validation Loss: 27356299574400873170213665767424.0000, Validation L1: 310916763108653.1250, Smoothed Validation Loss: 27356308532383300491824225845248.0000
Epoch [283/1000], Train Loss: 31939986777621100177189131780096.0000, Train L1 Loss: 189592326611370.5938
Epoch [283/1000], Validation Loss: 27356281202071064133198183137280.0000, Validation L1: 310916670057564.2500, Smoothed Validation Loss: 27356305799352078207041509785600.0000
Epoch [284/1000], Train Loss: 31939973593826249640866241052672.0000, Train L1 Loss: 189592297801365.6250
Epoch [284/1000], Validation Loss: 27356257265151814081977507643392.0000, Validation L1: 310916561420344.6875, Smoothed Validation Loss: 27356300945932053145614997782528.0000
Epoch [285/1000], Train Loss: 31939965738880120286023161741312.0000, Train L1 Loss: 189592275386596.0625
Epoch [285/1000], Validation Loss: 27356287640913347568598847062016.0000, Validation L1: 310916716517975.3125, Smoothed Validation Loss: 27356299615430183488633308184576.0000
Epoch [286/1000], Train Loss: 31939964609969142761336267079680.0000, Train L1 Loss: 189592308446638.5312
Epoch [286/1000], Validation Loss: 27356308564262408756534980902912.0000, Validation L1: 310916798183824.8750, Smoothed Validation Loss: 27356300510313407816863326404608.0000
Epoch [287/1000], Train Loss: 31940016416073195070266961559552.0000, Train L1 Loss: 189592369878444.5312
Epoch [287/1000], Validation Loss: 27356326799388767116214874931200.0000, Validation L1: 310916887869261.8125, Smoothed Validation Loss: 27356303139220942846078555783168.0000
Epoch [288/1000], Train Loss: 31939996900147305030815494176768.0000, Train L1 Loss: 189592323237829.0312
Epoch [288/1000], Validation Loss: 27356269258672345234439174881280.0000, Validation L1: 310916620442954.8750, Smoothed Validation Loss: 27356299751166082184194692218880.0000
Epoch [289/1000], Train Loss: 31939999036472054556513143881728.0000, Train L1 Loss: 189592343469361.2188
Epoch [289/1000], Validation Loss: 27356314809121136435007015878656.0000, Validation L1: 310916833006964.2500, Smoothed Validation Loss: 27356301256961591662515589218304.0000
Epoch [290/1000], Train Loss: 31939988160006450650512369909760.0000, Train L1 Loss: 189592307582213.5000
Epoch [290/1000], Validation Loss: 27356287236920064190752994885632.0000, Validation L1: 310916690142246.2500, Smoothed Validation Loss: 27356299854957439816059255259136.0000
Epoch [291/1000], Train Loss: 31939963913699282693362804588544.0000, Train L1 Loss: 189592291235504.3125
Epoch [291/1000], Validation Loss: 27356281429045883075617456390144.0000, Validation L1: 310916684822540.3125, Smoothed Validation Loss: 27356298012366285042735000846336.0000
Epoch [292/1000], Train Loss: 31939978532018768978185126150144.0000, Train L1 Loss: 189592301223209.2812
Epoch [292/1000], Validation Loss: 27356372082029822028494172848128.0000, Validation L1: 310917090203445.9375, Smoothed Validation Loss: 27356305419332640092390806257664.0000
Epoch [293/1000], Train Loss: 31940008281005348635198678368256.0000, Train L1 Loss: 189592341634211.9688
Epoch [293/1000], Validation Loss: 27356278404071436041525466759168.0000, Validation L1: 310916663865625.0625, Smoothed Validation Loss: 27356302717806520137664235044864.0000
Epoch [294/1000], Train Loss: 31939990200036525476867129475072.0000, Train L1 Loss: 189592348479645.3125
Epoch [294/1000], Validation Loss: 27356296956061840810956604571648.0000, Validation L1: 310916771877944.1875, Smoothed Validation Loss: 27356302141632052655353434734592.0000
Epoch [295/1000], Train Loss: 31940039373178452012060937027584.0000, Train L1 Loss: 189592425978160.7812
Epoch [295/1000], Validation Loss: 27356287362739775097183435489280.0000, Validation L1: 310916695214994.1250, Smoothed Validation Loss: 27356300663742823548456546598912.0000
Epoch [296/1000], Train Loss: 31940003483770246437410804072448.0000, Train L1 Loss: 189592335612406.8125
Epoch [296/1000], Validation Loss: 27356299357271828236751398240256.0000, Validation L1: 310916750578348.3750, Smoothed Validation Loss: 27356300533095722215846180814848.0000
Epoch [297/1000], Train Loss: 31939973195739608311102634459136.0000, Train L1 Loss: 189592296393729.1875
Epoch [297/1000], Validation Loss: 27356287434894083937109152890880.0000, Validation L1: 310916706843195.6250, Smoothed Validation Loss: 27356299223275557487252552548352.0000
Epoch [298/1000], Train Loss: 31939979188919854457145603915776.0000, Train L1 Loss: 189592305869240.5000
Epoch [298/1000], Validation Loss: 27356308887594799670693000642560.0000, Validation L1: 310916829531056.0625, Smoothed Validation Loss: 27356300189707482606316522831872.0000
Epoch [299/1000], Train Loss: 31940000487571499682806697558016.0000, Train L1 Loss: 189592363836507.4688
Epoch [299/1000], Validation Loss: 27356317487678880275745548009472.0000, Validation L1: 310916833940352.6250, Smoothed Validation Loss: 27356301919504620121459611664384.0000
Epoch [300/1000], Train Loss: 31940022416084001231546861223936.0000, Train L1 Loss: 189592418226455.6562
Epoch [300/1000], Validation Loss: 27356296127725349311425223327744.0000, Validation L1: 310916713746957.3750, Smoothed Validation Loss: 27356301340326693040456172830720.0000
Epoch [301/1000], Train Loss: 31940003004692941064844787843072.0000, Train L1 Loss: 189592349804036.8438
Epoch [301/1000], Validation Loss: 27356287331203962721268251230208.0000, Validation L1: 310916691021959.5000, Smoothed Validation Loss: 27356299939414420909257306144768.0000
Epoch [302/1000], Train Loss: 31939977749172556350371194208256.0000, Train L1 Loss: 189592306691963.1250
Epoch [302/1000], Validation Loss: 27356299402355814868085618245632.0000, Validation L1: 310916753673912.5000, Smoothed Validation Loss: 27356299885708563007299913777152.0000
Epoch [303/1000], Train Loss: 31940004996007957024301591298048.0000, Train L1 Loss: 189592358036687.3750
Epoch [303/1000], Validation Loss: 27356299590217123248371266486272.0000, Validation L1: 310916766804486.0000, Smoothed Validation Loss: 27356299856159419031407049048064.0000
Epoch [304/1000], Train Loss: 31939958972307586324745013952512.0000, Train L1 Loss: 189592258388319.6250
Epoch [304/1000], Validation Loss: 27356281421950777114669155876864.0000, Validation L1: 310916683998020.8125, Smoothed Validation Loss: 27356298012738552587933446045696.0000
Epoch [305/1000], Train Loss: 31939997052833221499926119186432.0000, Train L1 Loss: 189592323208246.5625
Epoch [305/1000], Validation Loss: 27356299616521270570356358250496.0000, Validation L1: 310916769635268.3750, Smoothed Validation Loss: 27356298173116824386175737266176.0000
Epoch [306/1000], Train Loss: 31939994677265140581710467956736.0000, Train L1 Loss: 189592349326791.9062
Epoch [306/1000], Validation Loss: 27356305847627617275505497079808.0000, Validation L1: 310916803486786.1250, Smoothed Validation Loss: 27356298940567905026188601458688.0000
Epoch [307/1000], Train Loss: 31940029704512839871440751689728.0000, Train L1 Loss: 189592381675123.1250
Epoch [307/1000], Validation Loss: 27356281372054194381930922770432.0000, Validation L1: 310916680971279.9375, Smoothed Validation Loss: 27356297183716536663922610012160.0000
Epoch [308/1000], Train Loss: 31940015429059522416544418103296.0000, Train L1 Loss: 189592360376484.2188
Epoch [308/1000], Validation Loss: 27356268932198819680979800555520.0000, Validation L1: 310916591128951.3125, Smoothed Validation Loss: 27356294358564764965628329066496.0000
Epoch [309/1000], Train Loss: 31940001330064538697020085370880.0000, Train L1 Loss: 189592368101455.8438
Epoch [309/1000], Validation Loss: 27356275457684964634635217666048.0000, Validation L1: 310916650275896.8125, Smoothed Validation Loss: 27356292468476788535408719822848.0000
Epoch [310/1000], Train Loss: 31940026054680400692730853851136.0000, Train L1 Loss: 189592398319054.7812
Epoch [310/1000], Validation Loss: 27356299402317430688461539508224.0000, Validation L1: 310916747897948.0000, Smoothed Validation Loss: 27356293161860850048554225369088.0000
Epoch [311/1000], Train Loss: 31939983385685546263195267629056.0000, Train L1 Loss: 189592330324162.6875
Epoch [311/1000], Validation Loss: 27356314607732762170755817406464.0000, Validation L1: 310916824616936.6250, Smoothed Validation Loss: 27356295306448038558614608150528.0000
Epoch [312/1000], Train Loss: 31940014875931960314924116213760.0000, Train L1 Loss: 189592365100898.3750
Epoch [312/1000], Validation Loss: 27356269198272206241969083514880.0000, Validation L1: 310916609190800.8125, Smoothed Validation Loss: 27356292695630454426230130212864.0000
Epoch [313/1000], Train Loss: 31939971498241557740321108918272.0000, Train L1 Loss: 189592280177954.1562
Epoch [313/1000], Validation Loss: 27356323636730092130166986768384.0000, Validation L1: 310916864878236.4375, Smoothed Validation Loss: 27356295789740420448423629553664.0000
Epoch [314/1000], Train Loss: 31939980889449845390663258996736.0000, Train L1 Loss: 189592327469490.4688
Epoch [314/1000], Validation Loss: 27356317418160303117738413391872.0000, Validation L1: 310916828172292.7500, Smoothed Validation Loss: 27356297952582409616075033411584.0000
Epoch [315/1000], Train Loss: 31940020498376902949343640682496.0000, Train L1 Loss: 189592395995816.4688
Epoch [315/1000], Validation Loss: 27356335846484001329398732029952.0000, Validation L1: 310916929912934.8750, Smoothed Validation Loss: 27356301741972569688127328747520.0000
Epoch [316/1000], Train Loss: 31939972577066035735983556657152.0000, Train L1 Loss: 189592299153049.5312
Epoch [316/1000], Validation Loss: 27356344846657924378469282611200.0000, Validation L1: 310916961389770.0625, Smoothed Validation Loss: 27356306052441105157161524133888.0000
Epoch [317/1000], Train Loss: 31939998209211364921569517240320.0000, Train L1 Loss: 189592344171737.9688
Epoch [317/1000], Validation Loss: 27356366333624597632475092484096.0000, Validation L1: 310917100831264.8125, Smoothed Validation Loss: 27356312080559453053612992757760.0000
Epoch [318/1000], Train Loss: 31940007753758451375402565763072.0000, Train L1 Loss: 189592380239849.9375
Epoch [318/1000], Validation Loss: 27356305502773316375678294163456.0000, Validation L1: 310916774373987.9375, Smoothed Validation Loss: 27356311422780841187259373846528.0000
Epoch [319/1000], Train Loss: 31939991535014860573464407834624.0000, Train L1 Loss: 189592324058084.4062
Epoch [319/1000], Validation Loss: 27356290306393858566952476213248.0000, Validation L1: 310916717125701.1875, Smoothed Validation Loss: 27356309311142145177028497768448.0000
Epoch [320/1000], Train Loss: 31939994317539642963931598684160.0000, Train L1 Loss: 189592322926720.9062
Epoch [320/1000], Validation Loss: 27356269203716819500679762542592.0000, Validation L1: 310916610005145.3750, Smoothed Validation Loss: 27356305300399613059753586982912.0000
Epoch [321/1000], Train Loss: 31939978168047462279306075439104.0000, Train L1 Loss: 189592337277519.1562
Epoch [321/1000], Validation Loss: 27356317626325671583258597392384.0000, Validation L1: 310916845897925.7500, Smoothed Validation Loss: 27356306532992218011384162549760.0000
Epoch [322/1000], Train Loss: 31940009394696460758782882873344.0000, Train L1 Loss: 189592372825758.1562
Epoch [322/1000], Validation Loss: 27356290344307529123561308422144.0000, Validation L1: 310916715070247.7500, Smoothed Validation Loss: 27356304914123747321162026188800.0000
Epoch [323/1000], Train Loss: 31939943099499759311953418256384.0000, Train L1 Loss: 189592241292912.7500
Epoch [323/1000], Validation Loss: 27356296476451921732059244003328.0000, Validation L1: 310916747378712.5000, Smoothed Validation Loss: 27356304070356563411171859759104.0000
Epoch [324/1000], Train Loss: 31940041634321325397860711137280.0000, Train L1 Loss: 189592412019443.3125
Epoch [324/1000], Validation Loss: 27356265987293298464755183255552.0000, Validation L1: 310916576576515.3750, Smoothed Validation Loss: 27356300262050235565450303897600.0000
Epoch [325/1000], Train Loss: 31940021987853195839522572599296.0000, Train L1 Loss: 189592417877382.8438
Epoch [325/1000], Validation Loss: 27356290406106292505508698914816.0000, Validation L1: 310916715559618.6250, Smoothed Validation Loss: 27356299276455845312695808032768.0000
Epoch [326/1000], Train Loss: 31939928318915880194147159638016.0000, Train L1 Loss: 189592201450684.1562
Epoch [326/1000], Validation Loss: 27356323995938936798693912739840.0000, Validation L1: 310916880953121.0000, Smoothed Validation Loss: 27356301748404151308775879344128.0000
Epoch [327/1000], Train Loss: 31940019227669820940919037231104.0000, Train L1 Loss: 189592395690697.5000
Epoch [327/1000], Validation Loss: 27356296407925217355984187424768.0000, Validation L1: 310916738434195.0625, Smoothed Validation Loss: 27356301214356260165296523837440.0000
Epoch [328/1000], Train Loss: 31940005995587942653482737074176.0000, Train L1 Loss: 189592353458313.7188
Epoch [328/1000], Validation Loss: 27356269152336854633477117575168.0000, Validation L1: 310916607436784.3750, Smoothed Validation Loss: 27356298008154320512834508685312.0000
Epoch [329/1000], Train Loss: 31939988815320237937206488989696.0000, Train L1 Loss: 189592338908920.9375
Epoch [329/1000], Validation Loss: 27356281580221702057274107756544.0000, Validation L1: 310916694853585.6875, Smoothed Validation Loss: 27356296365361057766558543118336.0000
Epoch [330/1000], Train Loss: 31939997522635638159499868504064.0000, Train L1 Loss: 189592329791852.5312
Epoch [330/1000], Validation Loss: 27356290299868286822080703365120.0000, Validation L1: 310916713746234.7500, Smoothed Validation Loss: 27356295758811783374270535565312.0000
Epoch [331/1000], Train Loss: 31939997066892779493033074753536.0000, Train L1 Loss: 189592333368506.2812
Epoch [331/1000], Validation Loss: 27356327026271946813416413331456.0000, Validation L1: 310916906991603.1875, Smoothed Validation Loss: 27356298885557800168545086078976.0000
Epoch [332/1000], Train Loss: 31939990549367116175924453703680.0000, Train L1 Loss: 189592308612864.5938
Epoch [332/1000], Validation Loss: 27356281264288013762144688406528.0000, Validation L1: 310916674875002.8750, Smoothed Validation Loss: 27356297123430825130784748208128.0000
Epoch [333/1000], Train Loss: 31940006144391999438179872538624.0000, Train L1 Loss: 189592377030960.4688
Epoch [333/1000], Validation Loss: 27356305419096597428721063821312.0000, Validation L1: 310916769387677.6875, Smoothed Validation Loss: 27356297952997402810938342506496.0000
Epoch [334/1000], Train Loss: 31939948687828682768345026527232.0000, Train L1 Loss: 189592250062235.1562
Epoch [334/1000], Validation Loss: 27356317724686449172851367870464.0000, Validation L1: 310916848645538.0000, Smoothed Validation Loss: 27356299930166306096049756831744.0000
Epoch [335/1000], Train Loss: 31940007151423713068402278924288.0000, Train L1 Loss: 189592348491157.4062
Epoch [335/1000], Validation Loss: 27356260120254180626948459331584.0000, Validation L1: 310916569580701.3750, Smoothed Validation Loss: 27356295949175093549139627081728.0000
Epoch [336/1000], Train Loss: 31940001860419644779241846865920.0000, Train L1 Loss: 189592340243600.7188
Epoch [336/1000], Validation Loss: 27356290417759748354497438547968.0000, Validation L1: 310916716970612.7500, Smoothed Validation Loss: 27356295396033556777875594543104.0000
Epoch [337/1000], Train Loss: 31940005269916949411369941204992.0000, Train L1 Loss: 189592354071698.0625
Epoch [337/1000], Validation Loss: 27356314522434080825200357670912.0000, Validation L1: 310916817350857.8750, Smoothed Validation Loss: 27356297308673610083327996329984.0000
Epoch [338/1000], Train Loss: 31939993027447865698203872526336.0000, Train L1 Loss: 189592346113122.9375
Epoch [338/1000], Validation Loss: 27356299480605998005236434731008.0000, Validation L1: 310916766323946.2500, Smoothed Validation Loss: 27356297525866849325878802907136.0000
Epoch [339/1000], Train Loss: 31939983115004346779458135392256.0000, Train L1 Loss: 189592315659105.9062
Epoch [339/1000], Validation Loss: 27356296561266709312052253425664.0000, Validation L1: 310916748883778.2500, Smoothed Validation Loss: 27356297429406838477015887118336.0000
Epoch [340/1000], Train Loss: 31939983262160176172530216730624.0000, Train L1 Loss: 189592293522735.2812
Epoch [340/1000], Validation Loss: 27356278122441778698067799703552.0000, Validation L1: 310916643134411.7500, Smoothed Validation Loss: 27356295498710332048761115639808.0000
Epoch [341/1000], Train Loss: 31939959307301670171610233962496.0000, Train L1 Loss: 189592291531338.5938
Epoch [341/1000], Validation Loss: 27356299436624870865051211268096.0000, Validation L1: 310916758892816.0000, Smoothed Validation Loss: 27356295892501786831110050676736.0000
Epoch [342/1000], Train Loss: 31939969752132657094419353174016.0000, Train L1 Loss: 189592273931216.8750
Epoch [342/1000], Validation Loss: 27356299629210923628809756344320.0000, Validation L1: 310916774111275.5000, Smoothed Validation Loss: 27356296266172703213039797665792.0000
Epoch [343/1000], Train Loss: 31940024600356562880824747229184.0000, Train L1 Loss: 189592377909761.7500
Epoch [343/1000], Validation Loss: 27356308560980428542487241424896.0000, Validation L1: 310916807082444.0625, Smoothed Validation Loss: 27356297495653473944544691093504.0000
Epoch [344/1000], Train Loss: 31940006922490431770426907557888.0000, Train L1 Loss: 189592339203955.7500
Epoch [344/1000], Validation Loss: 27356326641488074091776796786688.0000, Validation L1: 310916883347442.9375, Smoothed Validation Loss: 27356300410236934409627864399872.0000
Epoch [345/1000], Train Loss: 31939989648731700748832861061120.0000, Train L1 Loss: 189592328125850.7500
Epoch [345/1000], Validation Loss: 27356314721412777087229208035328.0000, Validation L1: 310916833198220.6250, Smoothed Validation Loss: 27356301841354520478827849711616.0000
Epoch [346/1000], Train Loss: 31940002622689243975972408000512.0000, Train L1 Loss: 189592338222297.9688
Epoch [346/1000], Validation Loss: 27356238759513307857773087686656.0000, Validation L1: 310916457143641.0000, Smoothed Validation Loss: 27356295533170399216722373509120.0000
Epoch [347/1000], Train Loss: 31939978107784043564323697590272.0000, Train L1 Loss: 189592298227744.2812
Epoch [347/1000], Validation Loss: 27356326751541768070293327183872.0000, Validation L1: 310916889526225.1250, Smoothed Validation Loss: 27356298655007537453159357087744.0000
Epoch [348/1000], Train Loss: 31940017983550185189039266594816.0000, Train L1 Loss: 189592383065817.2500
Epoch [348/1000], Validation Loss: 27356332870567292057851319549952.0000, Validation L1: 310916917454455.7500, Smoothed Validation Loss: 27356302076563513814348478808064.0000
Epoch [349/1000], Train Loss: 31940000966842257177366413443072.0000, Train L1 Loss: 189592335499639.3438
Epoch [349/1000], Validation Loss: 27356299084216948022613490270208.0000, Validation L1: 310916732868769.2500, Smoothed Validation Loss: 27356301777328857685534942691328.0000
Epoch [350/1000], Train Loss: 31940027671759109365838563508224.0000, Train L1 Loss: 189592382360443.5938
Epoch [350/1000], Validation Loss: 27356296366686498662091071684608.0000, Validation L1: 310916726423827.5000, Smoothed Validation Loss: 27356301236264619531390741905408.0000
Epoch [351/1000], Train Loss: 31939995733971612145024973668352.0000, Train L1 Loss: 189592358206873.6562
Epoch [351/1000], Validation Loss: 27356287538699749504989871996928.0000, Validation L1: 310916707555068.6875, Smoothed Validation Loss: 27356299866508132528750654914560.0000
Epoch [352/1000], Train Loss: 31939995334742542697786293354496.0000, Train L1 Loss: 189592320545118.8750
Epoch [352/1000], Validation Loss: 27356317531644321378428640034816.0000, Validation L1: 310916834916848.7500, Smoothed Validation Loss: 27356301633021753215158304374784.0000
Epoch [353/1000], Train Loss: 31939956478350828460852415299584.0000, Train L1 Loss: 189592274034076.0938
Epoch [353/1000], Validation Loss: 27356269165983419029955316547584.0000, Validation L1: 310916613598936.6250, Smoothed Validation Loss: 27356298386317919796638005592064.0000
Epoch [354/1000], Train Loss: 31940014934424982491189760491520.0000, Train L1 Loss: 189592367926018.2812
Epoch [354/1000], Validation Loss: 27356281499686869850756002873344.0000, Validation L1: 310916694533028.0625, Smoothed Validation Loss: 27356296697654814802049805320192.0000
Epoch [355/1000], Train Loss: 31939984757942112023377910693888.0000, Train L1 Loss: 189592338869125.7188
Epoch [355/1000], Validation Loss: 27356375131869241584049111171072.0000, Validation L1: 310917109062358.1250, Smoothed Validation Loss: 27356304541076259732049549590528.0000
Epoch [356/1000], Train Loss: 31939988821421611129576607449088.0000, Train L1 Loss: 189592326087233.6562
Epoch [356/1000], Validation Loss: 27356287453032178313956494934016.0000, Validation L1: 310916698186406.3750, Smoothed Validation Loss: 27356302832271850239160355913728.0000
Epoch [357/1000], Train Loss: 31939939802984970100410081607680.0000, Train L1 Loss: 189592242354091.4688
Epoch [357/1000], Validation Loss: 27356257034587085804588664619008.0000, Validation L1: 310916541876216.0000, Smoothed Validation Loss: 27356298252503373795703186784256.0000
Epoch [358/1000], Train Loss: 31939963204052128450631625080832.0000, Train L1 Loss: 189592286265475.0312
Epoch [358/1000], Validation Loss: 27356275378204443115283055378432.0000, Validation L1: 310916640316429.3750, Smoothed Validation Loss: 27356295965073484780900838277120.0000
Epoch [359/1000], Train Loss: 31939997282508272678127175467008.0000, Train L1 Loss: 189592332359222.9688
Epoch [359/1000], Validation Loss: 27356287484205468934266863747072.0000, Validation L1: 310916711666470.3125, Smoothed Validation Loss: 27356295116986682295517515350016.0000
Epoch [360/1000], Train Loss: 31940012496792673510991364882432.0000, Train L1 Loss: 189592375770916.2188
Epoch [360/1000], Validation Loss: 27356326827049457192759115907072.0000, Validation L1: 310916893648963.0000, Smoothed Validation Loss: 27356298287992959334881712668672.0000
Epoch [361/1000], Train Loss: 31940012695737921538587734573056.0000, Train L1 Loss: 189592384945220.0938
Epoch [361/1000], Validation Loss: 27356266287060122443536954032128.0000, Validation L1: 310916602055157.1875, Smoothed Validation Loss: 27356295087899675195387274067968.0000
Epoch [362/1000], Train Loss: 31940009280783555698378909155328.0000, Train L1 Loss: 189592350189081.1562
Epoch [362/1000], Validation Loss: 27356290491264875873855917260800.0000, Validation L1: 310916724655239.3750, Smoothed Validation Loss: 27356294628236194362514212913152.0000
Epoch [363/1000], Train Loss: 31940038727296166115400893857792.0000, Train L1 Loss: 189592405481802.5312
Epoch [363/1000], Validation Loss: 27356327126438127421629468246016.0000, Validation L1: 310916918095977.2500, Smoothed Validation Loss: 27356297878056388118785701183488.0000
Epoch [364/1000], Train Loss: 31939979305401792888986803372032.0000, Train L1 Loss: 189592312027130.7188
Epoch [364/1000], Validation Loss: 27356260053266248157154844344320.0000, Validation L1: 310916569041478.8125, Smoothed Validation Loss: 27356294095577375473702503710720.0000
Epoch [365/1000], Train Loss: 31940008064774551151015083638784.0000, Train L1 Loss: 189592374330691.1250
Epoch [365/1000], Validation Loss: 27356287531503141415639895244800.0000, Validation L1: 310916711325379.5625, Smoothed Validation Loss: 27356293439169952067896242864128.0000
Epoch [366/1000], Train Loss: 31940000583086659833446910656512.0000, Train L1 Loss: 189592364774924.6250
Epoch [366/1000], Validation Loss: 27356290501231796712789189328896.0000, Validation L1: 310916724194745.8125, Smoothed Validation Loss: 27356293145376135181305649299456.0000
Epoch [367/1000], Train Loss: 31939980803211393407264770490368.0000, Train L1 Loss: 189592315406543.1875
Epoch [367/1000], Validation Loss: 27356296598769246258678433054720.0000, Validation L1: 310916747546485.3125, Smoothed Validation Loss: 27356293490715446739402890412032.0000
Epoch [368/1000], Train Loss: 31939985336150405097409226997760.0000, Train L1 Loss: 189592314445383.7188
Epoch [368/1000], Validation Loss: 27356278479120879398306680143872.0000, Validation L1: 310916668941169.2500, Smoothed Validation Loss: 27356291989555987753493455699968.0000
Epoch [369/1000], Train Loss: 31939975214868598864020861091840.0000, Train L1 Loss: 189592312782820.8438
Epoch [369/1000], Validation Loss: 27356281140167326347536413753344.0000, Validation L1: 310916658884043.7500, Smoothed Validation Loss: 27356290904617121162537788768256.0000
Epoch [370/1000], Train Loss: 31939980425367455121412404019200.0000, Train L1 Loss: 189592305651189.6562
Epoch [370/1000], Validation Loss: 27356281349071690475911822442496.0000, Validation L1: 310916679035751.9375, Smoothed Validation Loss: 27356289949062582597474819506176.0000
Epoch [371/1000], Train Loss: 31940021348605680467899154694144.0000, Train L1 Loss: 189592359543161.6562
Epoch [371/1000], Validation Loss: 27356338985356500552323627483136.0000, Validation L1: 310916965843621.8750, Smoothed Validation Loss: 27356294852691978896559327674368.0000
Epoch [372/1000], Train Loss: 31939974066708173682440407089152.0000, Train L1 Loss: 189592299149035.3125
Epoch [372/1000], Validation Loss: 27356266206327883954552318197760.0000, Validation L1: 310916597963792.2500, Smoothed Validation Loss: 27356291988055568501638701252608.0000
Epoch [373/1000], Train Loss: 31939993819239659330657113341952.0000, Train L1 Loss: 189592347438135.5000
Epoch [373/1000], Validation Loss: 27356281270599268207949154091008.0000, Validation L1: 310916670252430.8750, Smoothed Validation Loss: 27356290916309938472269746536448.0000
Epoch [374/1000], Train Loss: 31940039106669216086333992206336.0000, Train L1 Loss: 189592418958131.3750
Epoch [374/1000], Validation Loss: 27356281402171444932818438717440.0000, Validation L1: 310916683673462.8125, Smoothed Validation Loss: 27356289964896090469404503965696.0000
Epoch [375/1000], Train Loss: 31939973779568672943269226741760.0000, Train L1 Loss: 189592291587887.1250
Epoch [375/1000], Validation Loss: 27356280990164330277239959584768.0000, Validation L1: 310916650453409.8125, Smoothed Validation Loss: 27356289067422913549468124053504.0000
Epoch [376/1000], Train Loss: 31939964949099219915987866353664.0000, Train L1 Loss: 189592266200435.6250
Epoch [376/1000], Validation Loss: 27356281207500635369153444708352.0000, Validation L1: 310916663532242.4375, Smoothed Validation Loss: 27356288281430688883956395278336.0000
Epoch [377/1000], Train Loss: 31940033101193107129655273455616.0000, Train L1 Loss: 189592414704306.1875
Epoch [377/1000], Validation Loss: 27356323719135323305127587086336.0000, Validation L1: 310916866872545.1250, Smoothed Validation Loss: 27356291825201154577873328144384.0000
Epoch [378/1000], Train Loss: 31939986221536731265416122335232.0000, Train L1 Loss: 189592350695010.4688
Epoch [378/1000], Validation Loss: 27356278302976964470919550468096.0000, Validation L1: 310916653704838.6250, Smoothed Validation Loss: 27356290472978739170057652273152.0000
Epoch [379/1000], Train Loss: 31940029547070586267471225815040.0000, Train L1 Loss: 189592385965551.8438
Epoch [379/1000], Validation Loss: 27356278184408544360514619179008.0000, Validation L1: 310916644254413.4375, Smoothed Validation Loss: 27356289244121721490543199911936.0000
Epoch [380/1000], Train Loss: 31940000372685700009300385071104.0000, Train L1 Loss: 189592361519011.5312
Epoch [380/1000], Validation Loss: 27356281332978959913030319603712.0000, Validation L1: 310916680677859.6875, Smoothed Validation Loss: 27356288453007444882431949144064.0000
Epoch [381/1000], Train Loss: 31940031590577385962960479846400.0000, Train L1 Loss: 189592383669718.8750
Epoch [381/1000], Validation Loss: 27356333029395591497538898755584.0000, Validation L1: 310916920074588.6250, Smoothed Validation Loss: 27356292910646261795742457790464.0000
Epoch [382/1000], Train Loss: 31940002793056648366510162575360.0000, Train L1 Loss: 189592343629893.4688
Epoch [382/1000], Validation Loss: 27356305463758493192179238830080.0000, Validation L1: 310916772436387.0000, Smoothed Validation Loss: 27356294165957486736825986842624.0000
Epoch [383/1000], Train Loss: 31939940768454597576294915899392.0000, Train L1 Loss: 189592232570813.7500
Epoch [383/1000], Validation Loss: 27356314848583504831476014252032.0000, Validation L1: 310916840533728.3750, Smoothed Validation Loss: 27356296234220087195211101372416.0000
Epoch [384/1000], Train Loss: 31940008617594769599665113399296.0000, Train L1 Loss: 189592352060310.0312
Epoch [384/1000], Validation Loss: 27356323594052140088956572139520.0000, Validation L1: 310916853717903.1250, Smoothed Validation Loss: 27356298970203292934945611186176.0000
Epoch [385/1000], Train Loss: 31939971588902949881763887841280.0000, Train L1 Loss: 189592322386003.4062
Epoch [385/1000], Validation Loss: 27356345255291996035534590836736.0000, Validation L1: 310917004329098.3125, Smoothed Validation Loss: 27356303598712160993204695465984.0000
Epoch [386/1000], Train Loss: 31939975908200098865915325579264.0000, Train L1 Loss: 189592284497805.6875
Epoch [386/1000], Validation Loss: 27356299506855093325376549552128.0000, Validation L1: 310916761648773.4375, Smoothed Validation Loss: 27356303189526456928581657296896.0000
Epoch [387/1000], Train Loss: 31939993289817464904045895352320.0000, Train L1 Loss: 189592343921348.9375
Epoch [387/1000], Validation Loss: 27356290380614504484308697219072.0000, Validation L1: 310916717236060.0625, Smoothed Validation Loss: 27356301908635263485594212237312.0000
Epoch [388/1000], Train Loss: 31939947806217544023977723166720.0000, Train L1 Loss: 189592247964378.8125
Epoch [388/1000], Validation Loss: 27356239013390906095446421143552.0000, Validation L1: 310916473986552.5000, Smoothed Validation Loss: 27356295619110825494779619442688.0000
Epoch [389/1000], Train Loss: 31940001665748961316366419230720.0000, Train L1 Loss: 189592363769795.1875
Epoch [389/1000], Validation Loss: 27356296528203262431734114811904.0000, Validation L1: 310916744891310.0000, Smoothed Validation Loss: 27356295710020068738115106242560.0000
Epoch [390/1000], Train Loss: 31939954661464941338264778833920.0000, Train L1 Loss: 189592257263445.4375
Epoch [390/1000], Validation Loss: 27356260161333877217999122857984.0000, Validation L1: 310916575175172.4375, Smoothed Validation Loss: 27356292155151450036463470641152.0000
Epoch [391/1000], Train Loss: 31939982104410862304737970094080.0000, Train L1 Loss: 189592327224522.0938
Epoch [391/1000], Validation Loss: 27356290191390951792335648718848.0000, Validation L1: 310916708171455.1875, Smoothed Validation Loss: 27356291958775397509890912026624.0000
Epoch [392/1000], Train Loss: 31940004192924472693727028051968.0000, Train L1 Loss: 189592358457727.0938
Epoch [392/1000], Validation Loss: 27356323974534777928881958551552.0000, Validation L1: 310916884877822.3125, Smoothed Validation Loss: 27356295160351338704309755838464.0000
Epoch [393/1000], Train Loss: 31939925890418969935682484568064.0000, Train L1 Loss: 189592221407933.7500
Epoch [393/1000], Validation Loss: 27356281258546757403178369548288.0000, Validation L1: 310916674736640.1250, Smoothed Validation Loss: 27356293770170878772756766261248.0000
Epoch [394/1000], Train Loss: 31939966126416890337487031894016.0000, Train L1 Loss: 189592303373157.8438
Epoch [394/1000], Validation Loss: 27356314501727421451277036421120.0000, Validation L1: 310916816668735.6875, Smoothed Validation Loss: 27356295843326532139888867803136.0000
Epoch [395/1000], Train Loss: 31939971035191806836829289709568.0000, Train L1 Loss: 189592307684346.5938
Epoch [395/1000], Validation Loss: 27356338733818648421858833072128.0000, Validation L1: 310916943867031.9375, Smoothed Validation Loss: 27356300132375745119165752541184.0000
Epoch [396/1000], Train Loss: 31939999034194124857789892263936.0000, Train L1 Loss: 189592380546149.7188
Epoch [396/1000], Validation Loss: 27356332897423364521369920339968.0000, Validation L1: 310916911032504.3750, Smoothed Validation Loss: 27356303408880509761545945743360.0000
Epoch [397/1000], Train Loss: 31940015623653559117361627267072.0000, Train L1 Loss: 189592365168375.4062
Epoch [397/1000], Validation Loss: 27356239124980530208879522349056.0000, Validation L1: 310916480831636.9375, Smoothed Validation Loss: 27356296980490509104119526981632.0000
Epoch [398/1000], Train Loss: 31939968603182998596140356599808.0000, Train L1 Loss: 189592289145592.7500
Epoch [398/1000], Validation Loss: 27356287414465774041755092516864.0000, Validation L1: 310916705000466.5625, Smoothed Validation Loss: 27356296023888036948962971746304.0000
Epoch [399/1000], Train Loss: 31939992934781290858670653964288.0000, Train L1 Loss: 189592339879021.0938
Epoch [399/1000], Validation Loss: 27356323706392370145084259172352.0000, Validation L1: 310916866406717.0000, Smoothed Validation Loss: 27356298792138471169295025963008.0000
Epoch [400/1000], Train Loss: 31940025726969880436820880130048.0000, Train L1 Loss: 189592383189865.6875
Epoch [400/1000], Validation Loss: 27356238861361636970004551303168.0000, Validation L1: 310916455861771.0625, Smoothed Validation Loss: 27356292799060785497566164811776.0000
Epoch [401/1000], Train Loss: 31939990732812406430793079980032.0000, Train L1 Loss: 189592324456945.9062
Epoch [401/1000], Validation Loss: 27356314741361165391892158873600.0000, Validation L1: 310916833918730.8750, Smoothed Validation Loss: 27356294993290823937358726955008.0000
Epoch [402/1000], Train Loss: 31939954086092641510782329159680.0000, Train L1 Loss: 189592254484375.4062
Epoch [402/1000], Validation Loss: 27356335477042073083960937676800.0000, Validation L1: 310916906300207.7500, Smoothed Validation Loss: 27356299041665947951299022553088.0000
Epoch [403/1000], Train Loss: 31940033012193588286708481261568.0000, Train L1 Loss: 189592374971349.0312
Epoch [403/1000], Validation Loss: 27356278225225681093289582788608.0000, Validation L1: 310916647168439.7500, Smoothed Validation Loss: 27356296960021919013698264891392.0000
Epoch [404/1000], Train Loss: 31940014644510174510448530948096.0000, Train L1 Loss: 189592397832607.8125
Epoch [404/1000], Validation Loss: 27356281586740856172676877647872.0000, Validation L1: 310916695359578.8750, Smoothed Validation Loss: 27356295422693812729596126167040.0000
Epoch [405/1000], Train Loss: 31939956506357088744004049174528.0000, Train L1 Loss: 189592278817060.8750
Epoch [405/1000], Validation Loss: 27356299206120864621438204641280.0000, Validation L1: 310916736781926.7500, Smoothed Validation Loss: 27356295801036515666980520329216.0000
Epoch [406/1000], Train Loss: 31939967319431686123400221163520.0000, Train L1 Loss: 189592288941105.6250
Epoch [406/1000], Validation Loss: 27356278518016420242075200520192.0000, Validation L1: 310916666945665.3125, Smoothed Validation Loss: 27356294072734510177729652981760.0000
Epoch [407/1000], Train Loss: 31940016214566168970233059999744.0000, Train L1 Loss: 189592358459742.3750
Epoch [407/1000], Validation Loss: 27356323818044211487369483780096.0000, Validation L1: 310916873090632.5625, Smoothed Validation Loss: 27356297047265479858333673324544.0000
Epoch [408/1000], Train Loss: 31939999222861154233009886461952.0000, Train L1 Loss: 189592341780923.2812
Epoch [408/1000], Validation Loss: 27356314667844702312271588622336.0000, Validation L1: 310916823559059.0625, Smoothed Validation Loss: 27356298809323405706607166750720.0000
Epoch [409/1000], Train Loss: 31939984638420302389856782254080.0000, Train L1 Loss: 189592305653038.9688
Epoch [409/1000], Validation Loss: 27356308373257114958383852552192.0000, Validation L1: 310916785063597.9375, Smoothed Validation Loss: 27356299765716775731064909856768.0000
Epoch [410/1000], Train Loss: 31939975008051792774520125784064.0000, Train L1 Loss: 189592305017921.7500
Epoch [410/1000], Validation Loss: 27356326824569018633191522566144.0000, Validation L1: 310916890558195.6250, Smoothed Validation Loss: 27356302471601997319117794705408.0000
Epoch [411/1000], Train Loss: 31939951715327784703146133028864.0000, Train L1 Loss: 189592266842976.3750
Epoch [411/1000], Validation Loss: 27356268982805575038958087176192.0000, Validation L1: 310916597936635.0000, Smoothed Validation Loss: 27356299122722355541461786689536.0000
Epoch [412/1000], Train Loss: 31939991991341980226789230772224.0000, Train L1 Loss: 189592321825574.3438
Epoch [412/1000], Validation Loss: 27356299513153057648680644902912.0000, Validation L1: 310916765358842.3750, Smoothed Validation Loss: 27356299161765429805423337144320.0000
Epoch [413/1000], Train Loss: 31939992599412512026407836057600.0000, Train L1 Loss: 189592337608616.2188
Epoch [413/1000], Validation Loss: 27356266208388992352815444656128.0000, Validation L1: 310916599772136.1875, Smoothed Validation Loss: 27356295866427786960882473369600.0000
Epoch [414/1000], Train Loss: 31940032466320892839217820860416.0000, Train L1 Loss: 189592406289818.4062
Epoch [414/1000], Validation Loss: 27356250939070252792712859222016.0000, Validation L1: 310916527828003.3125, Smoothed Validation Loss: 27356291373692035345505362903040.0000
Epoch [415/1000], Train Loss: 31939952671702496314347680169984.0000, Train L1 Loss: 189592241890554.6875
Epoch [415/1000], Validation Loss: 27356269079969638121167459975168.0000, Validation L1: 310916608251020.1250, Smoothed Validation Loss: 27356289144319796523791498084352.0000
Epoch [416/1000], Train Loss: 31940033171789728944864593182720.0000, Train L1 Loss: 189592402581296.1875
Epoch [416/1000], Validation Loss: 27356275107084340826260904083456.0000, Validation L1: 310916623008531.3125, Smoothed Validation Loss: 27356287740596251404398401421312.0000
Epoch [417/1000], Train Loss: 31939959899063343662229826306048.0000, Train L1 Loss: 189592268656859.3438
Epoch [417/1000], Validation Loss: 27356290267192676430872829755392.0000, Validation L1: 310916706808574.5000, Smoothed Validation Loss: 27356287993255896158845657939968.0000
Epoch [418/1000], Train Loss: 31939987755727990337062163185664.0000, Train L1 Loss: 189592326563821.5000
Epoch [418/1000], Validation Loss: 27356305663314087055675367620608.0000, Validation L1: 310916787352556.4375, Smoothed Validation Loss: 27356289760261715248528628908032.0000
Epoch [419/1000], Train Loss: 31939981416344155835632535470080.0000, Train L1 Loss: 189592318155234.9688
Epoch [419/1000], Validation Loss: 27356314590241033419627943690240.0000, Validation L1: 310916815341532.9375, Smoothed Validation Loss: 27356292243259647966358485860352.0000
Epoch [420/1000], Train Loss: 31939995029297463215225489588224.0000, Train L1 Loss: 189592323779332.2188
Epoch [420/1000], Validation Loss: 27356323697240064910349389791232.0000, Validation L1: 310916861367363.0625, Smoothed Validation Loss: 27356295388657687408957762568192.0000
Epoch [421/1000], Train Loss: 31940035498171152057602559442944.0000, Train L1 Loss: 189592397048358.5938
Epoch [421/1000], Validation Loss: 27356323676696688044516013244416.0000, Validation L1: 310916856909703.8750, Smoothed Validation Loss: 27356298217461585671073736687616.0000
Epoch [422/1000], Train Loss: 31939978227531055697211487682560.0000, Train L1 Loss: 189592291660576.7812
Epoch [422/1000], Validation Loss: 27356308601273247199444477149184.0000, Validation L1: 310916809764749.1875, Smoothed Validation Loss: 27356299255842752724630736207872.0000
Epoch [423/1000], Train Loss: 31939967845361235456194189983744.0000, Train L1 Loss: 189592292446023.2812
Epoch [423/1000], Validation Loss: 27356338725248302834572406554624.0000, Validation L1: 310916940500444.3750, Smoothed Validation Loss: 27356303202783306834904977768448.0000
Epoch [424/1000], Train Loss: 31939980786529803682305693188096.0000, Train L1 Loss: 189592311014994.0000
Epoch [424/1000], Validation Loss: 27356363106573405634687951437824.0000, Validation L1: 310917062048204.6250, Smoothed Validation Loss: 27356309193162314012723498713088.0000
Epoch [425/1000], Train Loss: 31939992220914561002668726157312.0000, Train L1 Loss: 189592325388254.0938
Epoch [425/1000], Validation Loss: 27356290334957520368784501637120.0000, Validation L1: 310916706605986.0000, Smoothed Validation Loss: 27356307307341831495809859846144.0000
Epoch [426/1000], Train Loss: 31940015509171061294085970067456.0000, Train L1 Loss: 189592373240484.5625
Epoch [426/1000], Validation Loss: 27356338886127694666951840235520.0000, Validation L1: 310916943557172.6875, Smoothed Validation Loss: 27356310465220417362564095148032.0000
Epoch [427/1000], Train Loss: 31940003213845309417500235005952.0000, Train L1 Loss: 189592341242368.1562
Epoch [427/1000], Validation Loss: 27356275315278496300599240294400.0000, Validation L1: 310916643770483.1875, Smoothed Validation Loss: 27356306950226223905287721451520.0000
Epoch [428/1000], Train Loss: 31939960661932813322126882766848.0000, Train L1 Loss: 189592273964285.7500
Epoch [428/1000], Validation Loss: 27356296092930529583161516490752.0000, Validation L1: 310916710902571.1250, Smoothed Validation Loss: 27356305864496655824154989166592.0000
Epoch [429/1000], Train Loss: 31939967281231325421712237920256.0000, Train L1 Loss: 189592274760554.6250
Epoch [429/1000], Validation Loss: 27356323718458427777534174167040.0000, Validation L1: 310916867640057.3125, Smoothed Validation Loss: 27356307649892829416613205770240.0000
Epoch [430/1000], Train Loss: 31939976602429985928676911349760.0000, Train L1 Loss: 189592327233340.7188
Epoch [430/1000], Validation Loss: 27356305396151860709177092472832.0000, Validation L1: 310916771205793.5000, Smoothed Validation Loss: 27356307424518733896949482651648.0000
Epoch [431/1000], Train Loss: 31940012343084786703638944808960.0000, Train L1 Loss: 189592370486111.6562
Epoch [431/1000], Validation Loss: 27356308593262064038292744044544.0000, Validation L1: 310916802974984.1875, Smoothed Validation Loss: 27356307541393066460723846053888.0000
Epoch [432/1000], Train Loss: 31939979755743205299171264299008.0000, Train L1 Loss: 189592314363761.2500
Epoch [432/1000], Validation Loss: 27356326745994247560097232322560.0000, Validation L1: 310916887779752.6250, Smoothed Validation Loss: 27356309461853183669941259206656.0000
Epoch [433/1000], Train Loss: 31939980550597099901065134866432.0000, Train L1 Loss: 189592313722460.3125
Epoch [433/1000], Validation Loss: 27356260034905140030359742709760.0000, Validation L1: 310916558797680.0000, Smoothed Validation Loss: 27356304519158379756343070294016.0000
Epoch [434/1000], Train Loss: 31939930584525130956397212598272.0000, Train L1 Loss: 189592217004088.1562
Epoch [434/1000], Validation Loss: 27356305548505744792160200294400.0000, Validation L1: 310916783957309.1250, Smoothed Validation Loss: 27356304622093116710284746031104.0000
Epoch [435/1000], Train Loss: 31940012694537293403128151932928.0000, Train L1 Loss: 189592365570247.9688
Epoch [435/1000], Validation Loss: 27356299552578609118195889471488.0000, Validation L1: 310916767068419.1250, Smoothed Validation Loss: 27356304115141668653235636797440.0000
Epoch [436/1000], Train Loss: 31939945945180104544105908928512.0000, Train L1 Loss: 189592256935370.3125
Epoch [436/1000], Validation Loss: 27356296503654005754948720001024.0000, Validation L1: 310916744123945.0625, Smoothed Validation Loss: 27356303353992902813766907854848.0000
Epoch [437/1000], Train Loss: 31940007031085243196451921592320.0000, Train L1 Loss: 189592332285108.7188
Epoch [437/1000], Validation Loss: 27356278382164243107734737649664.0000, Validation L1: 310916665984716.0000, Smoothed Validation Loss: 27356300856810036392803728097280.0000
Epoch [438/1000], Train Loss: 31939958869755871511911944159232.0000, Train L1 Loss: 189592285962421.4375
Epoch [438/1000], Validation Loss: 27356281250563811811690249453568.0000, Validation L1: 310916668832320.0625, Smoothed Validation Loss: 27356298896185412583612492021760.0000
Epoch [439/1000], Train Loss: 31940017679713705924982283960320.0000, Train L1 Loss: 189592380872795.8750
Epoch [439/1000], Validation Loss: 27356278346520292187728460644352.0000, Validation L1: 310916659950933.8750, Smoothed Validation Loss: 27356296841218901895103977095168.0000
Epoch [440/1000], Train Loss: 31939985186562424739974218776576.0000, Train L1 Loss: 189592315461148.5938
Epoch [440/1000], Validation Loss: 27356333027389044208761365856256.0000, Validation L1: 310916929170373.1875, Smoothed Validation Loss: 27356300459835914775389827760128.0000
Epoch [441/1000], Train Loss: 31939972298056473576538242023424.0000, Train L1 Loss: 189592288680454.3438
Epoch [441/1000], Validation Loss: 27356296431700242206429810786304.0000, Validation L1: 310916734997641.5000, Smoothed Validation Loss: 27356300057022344816334049640448.0000
Epoch [442/1000], Train Loss: 31939987795324394865640962260992.0000, Train L1 Loss: 189592322874377.9062
Epoch [442/1000], Validation Loss: 27356251255937122959430464307200.0000, Validation L1: 310916544379915.8750, Smoothed Validation Loss: 27356295176913821729923765633024.0000
Epoch [443/1000], Train Loss: 31939987698307536440851821494272.0000, Train L1 Loss: 189592327329809.8438
Epoch [443/1000], Validation Loss: 27356332645045199247232947191808.0000, Validation L1: 310916900227659.8750, Smoothed Validation Loss: 27356298923726959932014646525952.0000
Epoch [444/1000], Train Loss: 31939998431204090287009061404672.0000, Train L1 Loss: 189592373910215.2812
Epoch [444/1000], Validation Loss: 27356308638119969968332965150720.0000, Validation L1: 310916804634175.0625, Smoothed Validation Loss: 27356299895166261836366403862528.0000
Epoch [445/1000], Train Loss: 31940018590660418943713288388608.0000, Train L1 Loss: 189592378982902.4375
Epoch [445/1000], Validation Loss: 27356326560176821309500018393088.0000, Validation L1: 310916874904745.6250, Smoothed Validation Loss: 27356302561667315531879951630336.0000
Epoch [446/1000], Train Loss: 31939973010713347421444105043968.0000, Train L1 Loss: 189592310955067.2188
Epoch [446/1000], Validation Loss: 27356287488516688296354974269440.0000, Validation L1: 310916702390812.3750, Smoothed Validation Loss: 27356301054352251006887602946048.0000
Epoch [447/1000], Train Loss: 31939955971868191614213692588032.0000, Train L1 Loss: 189592273097288.2188
Epoch [447/1000], Validation Loss: 27356332872927903342133466103808.0000, Validation L1: 310916912176101.3125, Smoothed Validation Loss: 27356304236209816240412189261824.0000
Epoch [448/1000], Train Loss: 31939985988788396679899675361280.0000, Train L1 Loss: 189592317205186.9688
Epoch [448/1000], Validation Loss: 27356281379894700124404568817664.0000, Validation L1: 310916686079084.3750, Smoothed Validation Loss: 27356301950578304628811427217408.0000
Epoch [449/1000], Train Loss: 31939959929254903606968955437056.0000, Train L1 Loss: 189592267947003.3750
Epoch [449/1000], Validation Loss: 27356275122401979375273807708160.0000, Validation L1: 310916626578312.8125, Smoothed Validation Loss: 27356299267760673454537553477632.0000
Epoch [450/1000], Train Loss: 31939988631411099438716838477824.0000, Train L1 Loss: 189592334769458.6562
Epoch [450/1000], Validation Loss: 27356269228849211264416343916544.0000, Validation L1: 310916618932273.7500, Smoothed Validation Loss: 27356296263869526334805507047424.0000
Epoch [451/1000], Train Loss: 31940010713450303478200679792640.0000, Train L1 Loss: 189592372074057.1875
Epoch [451/1000], Validation Loss: 27356347873630731157216245579776.0000, Validation L1: 310916987205044.5625, Smoothed Validation Loss: 27356301424845643664526841741312.0000
Epoch [452/1000], Train Loss: 31939995040369319704735975997440.0000, Train L1 Loss: 189592324182171.5938
Epoch [452/1000], Validation Loss: 27356314347144962617887030247424.0000, Validation L1: 310916799200740.8750, Smoothed Validation Loss: 27356302717075576910942748803072.0000
Epoch [453/1000], Train Loss: 31940029761998024005095289520128.0000, Train L1 Loss: 189592370590073.5625
Epoch [453/1000], Validation Loss: 27356332827290527899386841661440.0000, Validation L1: 310916911394488.6250, Smoothed Validation Loss: 27356305728097070658707269877760.0000
Epoch [454/1000], Train Loss: 31940014862900916390317525041152.0000, Train L1 Loss: 189592381241744.6562
Epoch [454/1000], Validation Loss: 27356296509335418282066539708416.0000, Validation L1: 310916747274648.6250, Smoothed Validation Loss: 27356304806220904970683234123776.0000
Epoch [455/1000], Train Loss: 31939964626250551630606456848384.0000, Train L1 Loss: 189592298447546.6875
Epoch [455/1000], Validation Loss: 27356323772167262558845258432512.0000, Validation L1: 310916873922499.0000, Smoothed Validation Loss: 27356306702815542530939287502848.0000
Epoch [456/1000], Train Loss: 31939983083228915881769076523008.0000, Train L1 Loss: 189592335820101.8750
Epoch [456/1000], Validation Loss: 27356296439026950281815266426880.0000, Validation L1: 310916747209944.2500, Smoothed Validation Loss: 27356305676436684657106773606400.0000
Epoch [457/1000], Train Loss: 31939998276391384922669738622976.0000, Train L1 Loss: 189592350947834.8750
Epoch [457/1000], Validation Loss: 27356317618461364316754298273792.0000, Validation L1: 310916838391310.2500, Smoothed Validation Loss: 27356306870639156225951227969536.0000
Epoch [458/1000], Train Loss: 31940012281052989062572895371264.0000, Train L1 Loss: 189592366975929.1562
Epoch [458/1000], Validation Loss: 27356259877933156803079871397888.0000, Validation L1: 310916550927267.4375, Smoothed Validation Loss: 27356302171368555382944166838272.0000
Epoch [459/1000], Train Loss: 31939990414141412267749363679232.0000, Train L1 Loss: 189592308199324.1250
Epoch [459/1000], Validation Loss: 27356305643641089364626495242240.0000, Validation L1: 310916779577944.1875, Smoothed Validation Loss: 27356302518595807430032511467520.0000
Epoch [460/1000], Train Loss: 31940005243193512460477028892672.0000, Train L1 Loss: 189592350349809.3125
Epoch [460/1000], Validation Loss: 27356365987146114059433366519808.0000, Validation L1: 310917069098647.5000, Smoothed Validation Loss: 27356308865450838993692522446848.0000
Epoch [461/1000], Train Loss: 31939997071869711944839837253632.0000, Train L1 Loss: 189592330262961.7188
Epoch [461/1000], Validation Loss: 27356314535077454893882896547840.0000, Validation L1: 310916818861777.5000, Smoothed Validation Loss: 27356309432413499682991634382848.0000
Epoch [462/1000], Train Loss: 31939984213281600947990665625600.0000, Train L1 Loss: 189592306633098.9062
Epoch [462/1000], Validation Loss: 27356281403101658932252187295744.0000, Validation L1: 310916680521406.8750, Smoothed Validation Loss: 27356306629482317409357540622336.0000
Epoch [463/1000], Train Loss: 31939964975617121587086843969536.0000, Train L1 Loss: 189592304174691.1562
Epoch [463/1000], Validation Loss: 27356344928701471467355758395392.0000, Validation L1: 310916966506970.5000, Smoothed Validation Loss: 27356310459404234616597213347840.0000
Epoch [464/1000], Train Loss: 31939974177391988802820480434176.0000, Train L1 Loss: 189592295541139.3750
Epoch [464/1000], Validation Loss: 27356281140605994965640809545728.0000, Validation L1: 310916664396206.6875, Smoothed Validation Loss: 27356307527524411552221498441728.0000
Epoch [465/1000], Train Loss: 31940040031810973389361766203392.0000, Train L1 Loss: 189592414973651.9062
Epoch [465/1000], Validation Loss: 27356278364011259830519308746752.0000, Validation L1: 310916658604226.8125, Smoothed Validation Loss: 27356304611173094578611428524032.0000
Epoch [466/1000], Train Loss: 31940060850868115357649988485120.0000, Train L1 Loss: 189592461793461.5938
Epoch [466/1000], Validation Loss: 27356269190532297404372012236800.0000, Validation L1: 310916608124519.4375, Smoothed Validation Loss: 27356301069109015761907412369408.0000
Epoch [467/1000], Train Loss: 31939999749305613622000006201344.0000, Train L1 Loss: 189592350239714.0938
Epoch [467/1000], Validation Loss: 27356338611474135664289208336384.0000, Validation L1: 310916934306031.0625, Smoothed Validation Loss: 27356304823345527301785629229056.0000
Epoch [468/1000], Train Loss: 31939992671626921403360812728320.0000, Train L1 Loss: 189592333781502.1562
Epoch [468/1000], Validation Loss: 27356338853752294226904483889152.0000, Validation L1: 310916952009021.6875, Smoothed Validation Loss: 27356308226386205795737365643264.0000
Epoch [469/1000], Train Loss: 31940013282687940180125434249216.0000, Train L1 Loss: 189592379827987.6250
Epoch [469/1000], Validation Loss: 27356281344175165291852132777984.0000, Validation L1: 310916674908186.2500, Smoothed Validation Loss: 27356305538165101745348842356736.0000
Epoch [470/1000], Train Loss: 31939986635308725550167806181376.0000, Train L1 Loss: 189592317252886.5312
Epoch [470/1000], Validation Loss: 27356338796944753218381502480384.0000, Validation L1: 310916940773137.1875, Smoothed Validation Loss: 27356308864043067793372033843200.0000
Epoch [471/1000], Train Loss: 31939961631477198661664739688448.0000, Train L1 Loss: 189592274281595.7500
Epoch [471/1000], Validation Loss: 27356287611612505054561427259392.0000, Validation L1: 310916714420749.1250, Smoothed Validation Loss: 27356306738800015122370675081216.0000
Epoch [472/1000], Train Loss: 31939976085247237720169372450816.0000, Train L1 Loss: 189592321560002.9375
Epoch [472/1000], Validation Loss: 27356269301926649941561956106240.0000, Validation L1: 310916623038321.3750, Smoothed Validation Loss: 27356302995112676802849952235520.0000
Epoch [473/1000], Train Loss: 31940016912759012035898195836928.0000, Train L1 Loss: 189592367863409.7500
Epoch [473/1000], Validation Loss: 27356278030253265462579586662400.0000, Validation L1: 310916632207286.6875, Smoothed Validation Loss: 27356300498626737920622729363456.0000
Epoch [474/1000], Train Loss: 31939980447453855291575459905536.0000, Train L1 Loss: 189592315633718.6562
Epoch [474/1000], Validation Loss: 27356290294905919011468857049088.0000, Validation L1: 310916709878485.8125, Smoothed Validation Loss: 27356299478254655128987416657920.0000
Epoch [475/1000], Train Loss: 31940001098654610870363366621184.0000, Train L1 Loss: 189592352276737.9062
Epoch [475/1000], Validation Loss: 27356299437570554729204977500160.0000, Validation L1: 310916759905793.0625, Smoothed Validation Loss: 27356299474186247340808986427392.0000
Epoch [476/1000], Train Loss: 31939995655227420157548632735744.0000, Train L1 Loss: 189592355446955.7188
Epoch [476/1000], Validation Loss: 27356308599758749695154562531328.0000, Validation L1: 310916804200457.8125, Smoothed Validation Loss: 27356300386743497125883581300736.0000
Epoch [477/1000], Train Loss: 31940027193081939812965161107456.0000, Train L1 Loss: 189592405393325.0625
Epoch [477/1000], Validation Loss: 27356317828200349038872889393152.0000, Validation L1: 310916857335324.4375, Smoothed Validation Loss: 27356302130889184118622363058176.0000
Epoch [478/1000], Train Loss: 31939965005666791121966038253568.0000, Train L1 Loss: 189592258183767.0000
Epoch [478/1000], Validation Loss: 27356308690159977893323402641408.0000, Validation L1: 310916809841619.3125, Smoothed Validation Loss: 27356302786816262595372541542400.0000
Epoch [479/1000], Train Loss: 31939972006138392423948577931264.0000, Train L1 Loss: 189592285533060.6562
Epoch [479/1000], Validation Loss: 27356278045054886069888006225920.0000, Validation L1: 310916633814503.5000, Smoothed Validation Loss: 27356300312640124942824088010752.0000
Epoch [480/1000], Train Loss: 31940017678243050963064821121024.0000, Train L1 Loss: 189592381861848.6250
Epoch [480/1000], Validation Loss: 27356257269169506834752118718464.0000, Validation L1: 310916565363041.1875, Smoothed Validation Loss: 27356296008293062231296965607424.0000
Epoch [481/1000], Train Loss: 31939972617942628991039065554944.0000, Train L1 Loss: 189592319237242.7188
Epoch [481/1000], Validation Loss: 27356335619943698686227418972160.0000, Validation L1: 310916914787933.9375, Smoothed Validation Loss: 27356299969458127678229861892096.0000
Epoch [482/1000], Train Loss: 31939978701473865681407557238784.0000, Train L1 Loss: 189592295835294.5625
Epoch [482/1000], Validation Loss: 27356296298695947821654472654848.0000, Validation L1: 310916725628452.5000, Smoothed Validation Loss: 27356299602381913295452024864768.0000
Epoch [483/1000], Train Loss: 31939946156943799572299218157568.0000, Train L1 Loss: 189592273517226.3438
Epoch [483/1000], Validation Loss: 27356299598182315650128292085760.0000, Validation L1: 310916771423665.5625, Smoothed Validation Loss: 27356299601961952630199726112768.0000
Epoch [484/1000], Train Loss: 31939963414597550240025314066432.0000, Train L1 Loss: 189592297615601.3125
Epoch [484/1000], Validation Loss: 27356362959917007425892748623872.0000, Validation L1: 310917050068821.6875, Smoothed Validation Loss: 27356305937757458560128991100928.0000
Epoch [485/1000], Train Loss: 31939945929682745348363158290432.0000, Train L1 Loss: 189592258941686.8125
Epoch [485/1000], Validation Loss: 27356326754818015202015424020480.0000, Validation L1: 310916892837525.6875, Smoothed Validation Loss: 27356308019463515575397522604032.0000
Epoch [486/1000], Train Loss: 31940009594192899841173500198912.0000, Train L1 Loss: 189592358215835.8750
Epoch [486/1000], Validation Loss: 27356305613933855531014043992064.0000, Validation L1: 310916788351423.3750, Smoothed Validation Loss: 27356307778910550922039062953984.0000
Epoch [487/1000], Train Loss: 31940012434676532456103920795648.0000, Train L1 Loss: 189592378865906.1250
Epoch [487/1000], Validation Loss: 27356323574549558607807399329792.0000, Validation L1: 310916859489047.2500, Smoothed Validation Loss: 27356309358474454843135635750912.0000
Epoch [488/1000], Train Loss: 31940018489133700888071606632448.0000, Train L1 Loss: 189592421267049.3125
Epoch [488/1000], Validation Loss: 27356314590703625158952931557376.0000, Validation L1: 310916821461912.3125, Smoothed Validation Loss: 27356309881697367821477700698112.0000
Epoch [489/1000], Train Loss: 31939962274954130011744710426624.0000, Train L1 Loss: 189592259298672.5625
Epoch [489/1000], Validation Loss: 27356260078842046325803815272448.0000, Validation L1: 310916566846287.1250, Smoothed Validation Loss: 27356304901411837473350163103744.0000
Epoch [490/1000], Train Loss: 31939962980978318498241420722176.0000, Train L1 Loss: 189592289637317.4688
Epoch [490/1000], Validation Loss: 27356266112872850417456464789504.0000, Validation L1: 310916589275882.6875, Smoothed Validation Loss: 27356301022557936515960979587072.0000
Epoch [491/1000], Train Loss: 31939988164254457488230708150272.0000, Train L1 Loss: 189592336635197.0312
Epoch [491/1000], Validation Loss: 27356296605343236203144066105344.0000, Validation L1: 310916749157755.3750, Smoothed Validation Loss: 27356300580836463332159549079552.0000
Epoch [492/1000], Train Loss: 31940002335560984221471144411136.0000, Train L1 Loss: 189592362738184.5000
Epoch [492/1000], Validation Loss: 27356299120361212832423610417152.0000, Validation L1: 310916735408393.0625, Smoothed Validation Loss: 27356300434788938282185955213312.0000
Epoch [493/1000], Train Loss: 31939990704680153444466129108992.0000, Train L1 Loss: 189592353848721.4375
Epoch [493/1000], Validation Loss: 27356290589353757643145448783872.0000, Validation L1: 310916731610238.8750, Smoothed Validation Loss: 27356299450245422470081718255616.0000
Epoch [494/1000], Train Loss: 31940031147410468967955606536192.0000, Train L1 Loss: 189592395501927.5000
Epoch [494/1000], Validation Loss: 27356305413822972337062760415232.0000, Validation L1: 310916770498940.2500, Smoothed Validation Loss: 27356300046603181510019487105024.0000
Epoch [495/1000], Train Loss: 31939983885260300792594736087040.0000, Train L1 Loss: 189592340675911.6250
Epoch [495/1000], Validation Loss: 27356290489704049840199242350592.0000, Validation L1: 310916723763798.1250, Smoothed Validation Loss: 27356299090913269243757388103680.0000
Epoch [496/1000], Train Loss: 31940007034643127434471259766784.0000, Train L1 Loss: 189592328138826.9062
Epoch [496/1000], Validation Loss: 27356275081889421085297910743040.0000, Validation L1: 310916615902967.9375, Smoothed Validation Loss: 27356296690010882176111626682368.0000
Epoch [497/1000], Train Loss: 31939989167404437534829191364608.0000, Train L1 Loss: 189592341201774.5625
Epoch [497/1000], Validation Loss: 27356281212778944204424213430272.0000, Validation L1: 310916664127637.8750, Smoothed Validation Loss: 27356295142287688829302848094208.0000
Epoch [498/1000], Train Loss: 31939984303525027518816070926336.0000, Train L1 Loss: 189592312886266.1250
Epoch [498/1000], Validation Loss: 27356338791482283187148299436032.0000, Validation L1: 310916946760425.0000, Smoothed Validation Loss: 27356299507207148715447355965440.0000
Epoch [499/1000], Train Loss: 31939988446231193744170937221120.0000, Train L1 Loss: 189592297478956.1562
Epoch [499/1000], Validation Loss: 27356323450192977148317085466624.0000, Validation L1: 310916847181380.1875, Smoothed Validation Loss: 27356301901505732009094291652608.0000
Epoch [500/1000], Train Loss: 31939952829320840663747392438272.0000, Train L1 Loss: 189592276367786.5000
Epoch [500/1000], Validation Loss: 27356287356469769120366056177664.0000, Validation L1: 310916700417802.6250, Smoothed Validation Loss: 27356300447002137521661319053312.0000
Epoch [501/1000], Train Loss: 31940038917664425746260465549312.0000, Train L1 Loss: 189592406545249.6562
Epoch [501/1000], Validation Loss: 27356326961512170259264351240192.0000, Validation L1: 310916905377989.6250, Smoothed Validation Loss: 27356303098453138543621808586752.0000
Epoch [502/1000], Train Loss: 31940004027717283749031133052928.0000, Train L1 Loss: 189592377094746.3750
Epoch [502/1000], Validation Loss: 27356290331010889914530169618432.0000, Validation L1: 310916715567188.4375, Smoothed Validation Loss: 27356301821708913680712644689920.0000
Epoch [503/1000], Train Loss: 31939956708412873955033418301440.0000, Train L1 Loss: 189592273365332.5938
Epoch [503/1000], Validation Loss: 27356296224043370671236402118656.0000, Validation L1: 310916726148752.0000, Smoothed Validation Loss: 27356301261942356677605244010496.0000
Epoch [504/1000], Train Loss: 31940033032995498792750688501760.0000, Train L1 Loss: 189592403294046.6875
Epoch [504/1000], Validation Loss: 27356305453074977594937282920448.0000, Validation L1: 310916781481900.4375, Smoothed Validation Loss: 27356301681055620120418336112640.0000
Epoch [505/1000], Train Loss: 31940002552414827692503683039232.0000, Train L1 Loss: 189592336892316.1250
Epoch [505/1000], Validation Loss: 27356305681718254098507758567424.0000, Validation L1: 310916795726403.2500, Smoothed Validation Loss: 27356302081121886220387054780416.0000
Epoch [506/1000], Train Loss: 31940010915231139428379452768256.0000, Train L1 Loss: 189592371657278.5000
Epoch [506/1000], Validation Loss: 27356269197085647351745406304256.0000, Validation L1: 310916613589162.0000, Smoothed Validation Loss: 27356298792718264585322703618048.0000
Epoch [507/1000], Train Loss: 31939989148213464615497410543616.0000, Train L1 Loss: 189592315558183.9062
Epoch [507/1000], Validation Loss: 27356278342267588095598774976512.0000, Validation L1: 310916656896571.0625, Smoothed Validation Loss: 27356296747673197386710273490944.0000
Epoch [508/1000], Train Loss: 31939973510626678067229660020736.0000, Train L1 Loss: 189592299993692.5625
Epoch [508/1000], Validation Loss: 27356275151152153252073754853376.0000, Validation L1: 310916630928415.6250, Smoothed Validation Loss: 27356294588021094324326509838336.0000
Epoch [509/1000], Train Loss: 31939950958349361125821738123264.0000, Train L1 Loss: 189592274898435.7188
Epoch [509/1000], Validation Loss: 27356290194777109272963722510336.0000, Validation L1: 310916701112630.3750, Smoothed Validation Loss: 27356294148696698070990044790784.0000
Epoch [510/1000], Train Loss: 31939994922113471926468693983232.0000, Train L1 Loss: 189592354623451.0312
Epoch [510/1000], Validation Loss: 27356256934145609158353706024960.0000, Validation L1: 310916539102496.8750, Smoothed Validation Loss: 27356290427241590981166261862400.0000
Epoch [511/1000], Train Loss: 31939980979136874745525176369152.0000, Train L1 Loss: 189592314299759.9375
Epoch [511/1000], Validation Loss: 27356257117845843684528148709376.0000, Validation L1: 310916551980208.9375, Smoothed Validation Loss: 27356287096302020304742115180544.0000
Epoch [512/1000], Train Loss: 31939998423952506757007773007872.0000, Train L1 Loss: 189592352475847.4688
Epoch [512/1000], Validation Loss: 27356278410209166793687347232768.0000, Validation L1: 310916664888189.1875, Smoothed Validation Loss: 27356286227692737655796414808064.0000
Epoch [513/1000], Train Loss: 31940014884868245889932532383744.0000, Train L1 Loss: 189592364068337.4062
Epoch [513/1000], Validation Loss: 27356278339667642016319278153728.0000, Validation L1: 310916654881523.6250, Smoothed Validation Loss: 27356285438890226290408850194432.0000
Epoch [514/1000], Train Loss: 31939985075725874541831502430208.0000, Train L1 Loss: 189592311400720.0312
Epoch [514/1000], Validation Loss: 27356299665599161941233418371072.0000, Validation L1: 310916773966510.3750, Smoothed Validation Loss: 27356286861561117603691493326848.0000
Epoch [515/1000], Train Loss: 31940028122471564342122824859648.0000, Train L1 Loss: 189592400777371.4688
Epoch [515/1000], Validation Loss: 27356314558543694939477489221632.0000, Validation L1: 310916825642605.6875, Smoothed Validation Loss: 27356289631259378039429869338624.0000
Epoch [516/1000], Train Loss: 31940002475379571619629350518784.0000, Train L1 Loss: 189592341767169.9688
Epoch [516/1000], Validation Loss: 27356275302599575320057866092544.0000, Validation L1: 310916633022207.3750, Smoothed Validation Loss: 27356288198393395515692855328768.0000
Epoch [517/1000], Train Loss: 31939994530610593352362114416640.0000, Train L1 Loss: 189592353615313.8750
Epoch [517/1000], Validation Loss: 27356335601835791937682341363712.0000, Validation L1: 310916910856966.3750, Smoothed Validation Loss: 27356292938737635608251766669312.0000
Epoch [518/1000], Train Loss: 31939979092438955913210943766528.0000, Train L1 Loss: 189592300629631.0625
Epoch [518/1000], Validation Loss: 27356323745537441933406496620544.0000, Validation L1: 310916865171398.9375, Smoothed Validation Loss: 27356296019417615340047314190336.0000
Epoch [519/1000], Train Loss: 31939978820777471409382957776896.0000, Train L1 Loss: 189592301705154.1562
Epoch [519/1000], Validation Loss: 27356268901849359029705434464256.0000, Validation L1: 310916589256073.3750, Smoothed Validation Loss: 27356293307660789709013126217728.0000
Epoch [520/1000], Train Loss: 31939990505280595797259505893376.0000, Train L1 Loss: 189592316367611.5938
Epoch [520/1000], Validation Loss: 27356317331863867289137529749504.0000, Validation L1: 310916822550014.6875, Smoothed Validation Loss: 27356295710081097016665603833856.0000
Epoch [521/1000], Train Loss: 31939991866139568714083209314304.0000, Train L1 Loss: 189592328355650.0000
Epoch [521/1000], Validation Loss: 27356275390006851018347446796288.0000, Validation L1: 310916649325608.0000, Smoothed Validation Loss: 27356293678073676019713490026496.0000
Epoch [522/1000], Train Loss: 31939984298911621125331027492864.0000, Train L1 Loss: 189592309830471.5938
Epoch [522/1000], Validation Loss: 27356308700529781747721984540672.0000, Validation L1: 310916814964847.2500, Smoothed Validation Loss: 27356295180319286142154376740864.0000
Epoch [523/1000], Train Loss: 31939967511296748615613768794112.0000, Train L1 Loss: 189592286934768.5938
Epoch [523/1000], Validation Loss: 27356296593551326190811075313664.0000, Validation L1: 310916753104848.7500, Smoothed Validation Loss: 27356295321642490147020046598144.0000
Epoch [524/1000], Train Loss: 31940047451501145804244202291200.0000, Train L1 Loss: 189592410487666.6875
Epoch [524/1000], Validation Loss: 27356296641411831532015107178496.0000, Validation L1: 310916753987564.1250, Smoothed Validation Loss: 27356295453619423384799627182080.0000
Epoch [525/1000], Train Loss: 31939982706691210639038503452672.0000, Train L1 Loss: 189592303945780.8438
Epoch [525/1000], Validation Loss: 27356278366047044488077730906112.0000, Validation L1: 310916660357110.3750, Smoothed Validation Loss: 27356293744862189098007139450880.0000
Epoch [526/1000], Train Loss: 31940007682170555757011608272896.0000, Train L1 Loss: 189592376170628.0000
Epoch [526/1000], Validation Loss: 27356250945823909340712810840064.0000, Validation L1: 310916528772868.6250, Smoothed Validation Loss: 27356289464958359320837855641600.0000
Epoch [527/1000], Train Loss: 31939971459392471526708915208192.0000, Train L1 Loss: 189592276031489.7188
Epoch [527/1000], Validation Loss: 27356278448395651904923401977856.0000, Validation L1: 310916665971438.3125, Smoothed Validation Loss: 27356288363302090380686261223424.0000
Epoch [528/1000], Train Loss: 31939978902538196945270193782784.0000, Train L1 Loss: 189592299713375.5625
Epoch [528/1000], Validation Loss: 27356290511677923070072819023872.0000, Validation L1: 310916724868939.8750, Smoothed Validation Loss: 27356288578139676802144656162816.0000
Epoch [529/1000], Train Loss: 31939988353059914005197189283840.0000, Train L1 Loss: 189592329672018.5625
Epoch [529/1000], Validation Loss: 27356332794035673531305829597184.0000, Validation L1: 310916906197289.8125, Smoothed Validation Loss: 27356292999729277375780698980352.0000
Epoch [530/1000], Train Loss: 31939975470438987611632079732736.0000, Train L1 Loss: 189592303403476.4688
Epoch [530/1000], Validation Loss: 27356317557721798027568547364864.0000, Validation L1: 310916837440339.6250, Smoothed Validation Loss: 27356295455528526288439744659456.0000
Epoch [531/1000], Train Loss: 31940014755019101346498925821952.0000, Train L1 Loss: 189592364579497.8750
Epoch [531/1000], Validation Loss: 27356308677549534145116196831232.0000, Validation L1: 310916810574506.5000, Smoothed Validation Loss: 27356296777730626623747427139584.0000
Epoch [532/1000], Train Loss: 31940002447510819743900219998208.0000, Train L1 Loss: 189592334389941.3750
Epoch [532/1000], Validation Loss: 27356281259008678106158879211520.0000, Validation L1: 310916676370346.0000, Smoothed Validation Loss: 27356295225858433573428423294976.0000
Epoch [533/1000], Train Loss: 31939946923773320413340170715136.0000, Train L1 Loss: 189592270718537.3750
Epoch [533/1000], Validation Loss: 27356296294981450906593325481984.0000, Validation L1: 310916728008256.9375, Smoothed Validation Loss: 27356295332770736207464838987776.0000
Epoch [534/1000], Train Loss: 31939978052998898011666965856256.0000, Train L1 Loss: 189592293405795.4688
Epoch [534/1000], Validation Loss: 27356275319570197061902327087104.0000, Validation L1: 310916640674201.7500, Smoothed Validation Loss: 27356293331450685445428326957056.0000
Epoch [535/1000], Train Loss: 31940000946141871317724019294208.0000, Train L1 Loss: 189592326954044.8125
Epoch [535/1000], Validation Loss: 27356393570105191438766051426304.0000, Validation L1: 310917214384782.5625, Smoothed Validation Loss: 27356303355316136945482024878080.0000
Epoch [536/1000], Train Loss: 31940005285919977276873478504448.0000, Train L1 Loss: 189592355791889.5000
Epoch [536/1000], Validation Loss: 27356317638116752933260152012800.0000, Validation L1: 310916843117847.5625, Smoothed Validation Loss: 27356304783596198544259837591552.0000
Epoch [537/1000], Train Loss: 31939969905432972639094370729984.0000, Train L1 Loss: 189592274984874.8750
Epoch [537/1000], Validation Loss: 27356299530962488331921742888960.0000, Validation L1: 310916764582095.5625, Smoothed Validation Loss: 27356304258332826171946139910144.0000
Epoch [538/1000], Train Loss: 31939960940345594487750078234624.0000, Train L1 Loss: 189592276564649.4062
Epoch [538/1000], Validation Loss: 27356323707523453695097986613248.0000, Validation L1: 310916869276512.7500, Smoothed Validation Loss: 27356306203251889374621287317504.0000
Epoch [539/1000], Train Loss: 31939986334635777326359091609600.0000, Train L1 Loss: 189592326928215.0312
Epoch [539/1000], Validation Loss: 27356308696410996694111787941888.0000, Validation L1: 310916812223426.3750, Smoothed Validation Loss: 27356306452567800556930300116992.0000
Epoch [540/1000], Train Loss: 31939977608871786554508938575872.0000, Train L1 Loss: 189592321903621.7500
Epoch [540/1000], Validation Loss: 27356278132696425509994518020096.0000, Validation L1: 310916642555829.5000, Smoothed Validation Loss: 27356303620580663502596684644352.0000
Epoch [541/1000], Train Loss: 31940016792121579709884102868992.0000, Train L1 Loss: 189592370866304.4375
Epoch [541/1000], Validation Loss: 27356281456216374347120928358400.0000, Validation L1: 310916689911977.9375, Smoothed Validation Loss: 27356301404144230984169407119360.0000
Epoch [542/1000], Train Loss: 31940025992776843051054179287040.0000, Train L1 Loss: 189592385185627.8438
Epoch [542/1000], Validation Loss: 27356299263095322542950418743296.0000, Validation L1: 310916737355490.8125, Smoothed Validation Loss: 27356301190039344193287172915200.0000
Epoch [543/1000], Train Loss: 31939980535001332549864711520256.0000, Train L1 Loss: 189592307193686.6250
Epoch [543/1000], Validation Loss: 27356335772744601061024067485696.0000, Validation L1: 310916922646130.5625, Smoothed Validation Loss: 27356304648309867177901085949952.0000
Epoch [544/1000], Train Loss: 31940006648031031954899472482304.0000, Train L1 Loss: 189592366935373.3125
Epoch [544/1000], Validation Loss: 27356269314885262473361547591680.0000, Validation L1: 310916620677482.4375, Smoothed Validation Loss: 27356301114967405356367243902976.0000
Epoch [545/1000], Train Loss: 31939977137168981456574033690624.0000, Train L1 Loss: 189592318485017.1562
Epoch [545/1000], Validation Loss: 27356324090596395407500669616128.0000, Validation L1: 310916891964405.8125, Smoothed Validation Loss: 27356303412530303460760661000192.0000
Epoch [546/1000], Train Loss: 31939989221926311660469098643456.0000, Train L1 Loss: 189592336962658.6562
Epoch [546/1000], Validation Loss: 27356326684593260111637713518592.0000, Validation L1: 310916883639126.8750, Smoothed Validation Loss: 27356305739736596874048552566784.0000
Epoch [547/1000], Train Loss: 31940007670627874948057300729856.0000, Train L1 Loss: 189592384236278.7500
Epoch [547/1000], Validation Loss: 27356287525648421367661604110336.0000, Validation L1: 310916706525754.0625, Smoothed Validation Loss: 27356303918327780674489745932288.0000
Epoch [548/1000], Train Loss: 31940005230924369506430468751360.0000, Train L1 Loss: 189592361241595.3750
Epoch [548/1000], Validation Loss: 27356296444659138465005926612992.0000, Validation L1: 310916735823823.6875, Smoothed Validation Loss: 27356303170960916903901326737408.0000
Epoch [549/1000], Train Loss: 31939992052330721676158136483840.0000, Train L1 Loss: 189592336392620.6875
Epoch [549/1000], Validation Loss: 27356314672565695197254885834752.0000, Validation L1: 310916829722087.1250, Smoothed Validation Loss: 27356304321121395183596645384192.0000
Epoch [550/1000], Train Loss: 31939947170649744267493270093824.0000, Train L1 Loss: 189592261827303.7500
Epoch [550/1000], Validation Loss: 27356317841537056773788743499776.0000, Validation L1: 310916857966883.0000, Smoothed Validation Loss: 27356305673162959541176004247552.0000
Epoch [551/1000], Train Loss: 31939994513101242015892339949568.0000, Train L1 Loss: 189592352065973.5312
Epoch [551/1000], Validation Loss: 27356281143133604227705481461760.0000, Validation L1: 310916671577647.1875, Smoothed Validation Loss: 27356303220160022658749063757824.0000
Epoch [552/1000], Train Loss: 31939977705723209750586251542528.0000, Train L1 Loss: 189592301916177.9375
Epoch [552/1000], Validation Loss: 27356269208691099332306003820544.0000, Validation L1: 310916609486961.8125, Smoothed Validation Loss: 27356299819013130326104757764096.0000
Epoch [553/1000], Train Loss: 31939982124734517551951194882048.0000, Train L1 Loss: 189592330157925.7812
Epoch [553/1000], Validation Loss: 27356326714283299201872864215040.0000, Validation L1: 310916892462106.9375, Smoothed Validation Loss: 27356302508540147664041531146240.0000
Epoch [554/1000], Train Loss: 31940018981778996354417088790528.0000, Train L1 Loss: 189592394429583.4375
Epoch [554/1000], Validation Loss: 27356363430693539174067854114816.0000, Validation L1: 310917075441161.8750, Smoothed Validation Loss: 27356308600755486364684200706048.0000
Epoch [555/1000], Train Loss: 31939973489657458835030638854144.0000, Train L1 Loss: 189592297562777.5312
Epoch [555/1000], Validation Loss: 27356296396774282160616702476288.0000, Validation L1: 310916736511687.0000, Smoothed Validation Loss: 27356307380357363692477637197824.0000
Epoch [556/1000], Train Loss: 31940003721310807343216667394048.0000, Train L1 Loss: 189592334629952.6875
Epoch [556/1000], Validation Loss: 27356278270116283156624513695744.0000, Validation L1: 310916656193861.0000, Smoothed Validation Loss: 27356304469333255638892324847616.0000
Epoch [557/1000], Train Loss: 31940005299345536528837725126656.0000, Train L1 Loss: 189592356023208.6562
Epoch [557/1000], Validation Loss: 27356308630697736041251353919488.0000, Validation L1: 310916808887283.1875, Smoothed Validation Loss: 27356304885469702778408302280704.0000
Epoch [558/1000], Train Loss: 31939966882215677057215018041344.0000, Train L1 Loss: 189592276988504.0625
Epoch [558/1000], Validation Loss: 27356335856414551097741359972352.0000, Validation L1: 310916932892501.5000, Smoothed Validation Loss: 27356307982564190762861347209216.0000
Epoch [559/1000], Train Loss: 31939979825664170076684697993216.0000, Train L1 Loss: 189592318701979.5000
Epoch [559/1000], Validation Loss: 27356296496982220144574736629760.0000, Validation L1: 310916752265258.4375, Smoothed Validation Loss: 27356306834005994151392648888320.0000
Epoch [560/1000], Train Loss: 31940006501519095711351433068544.0000, Train L1 Loss: 189592367137336.4375
Epoch [560/1000], Validation Loss: 27356269185235181537057344323584.0000, Validation L1: 310916613925823.4375, Smoothed Validation Loss: 27356303069128913340319081168896.0000
Epoch [561/1000], Train Loss: 31939978326845704695080583954432.0000, Train L1 Loss: 189592329223204.0938
Epoch [561/1000], Validation Loss: 27356275278984716486760047050752.0000, Validation L1: 310916638431953.2500, Smoothed Validation Loss: 27356300290114493204603215020032.0000
Epoch [562/1000], Train Loss: 31940005400949977706848566902784.0000, Train L1 Loss: 189592385374715.0625
Epoch [562/1000], Validation Loss: 27356296396562941740903087210496.0000, Validation L1: 310916734361753.4375, Smoothed Validation Loss: 27356299900759336256793351290880.0000
Epoch [563/1000], Train Loss: 31940033022811531473375922749440.0000, Train L1 Loss: 189592400166055.3750
Epoch [563/1000], Validation Loss: 27356314716124596361575243186176.0000, Validation L1: 310916827942495.0625, Smoothed Validation Loss: 27356301382295859565111764058112.0000
Epoch [564/1000], Train Loss: 31940002098984657506684186394624.0000, Train L1 Loss: 189592366239578.4062
Epoch [564/1000], Validation Loss: 27356259979324208423546644332544.0000, Validation L1: 310916558740566.3125, Smoothed Validation Loss: 27356297241998695802035140296704.0000
Epoch [565/1000], Train Loss: 31939971932704102023129009750016.0000, Train L1 Loss: 189592320092537.0625
Epoch [565/1000], Validation Loss: 27356326718059833201801039970304.0000, Validation L1: 310916889474316.0000, Smoothed Validation Loss: 27356300189604809542011730264064.0000
Epoch [566/1000], Train Loss: 31939992216524988014263623745536.0000, Train L1 Loss: 189592356887953.5625
Epoch [566/1000], Validation Loss: 27356278327859600110121046245376.0000, Validation L1: 310916653114016.7500, Smoothed Validation Loss: 27356298003430287698102736388096.0000
Epoch [567/1000], Train Loss: 31940020167091803611595666358272.0000, Train L1 Loss: 189592389476610.0000
Epoch [567/1000], Validation Loss: 27356314761960805727870275026944.0000, Validation L1: 310916835977086.6875, Smoothed Validation Loss: 27356299679283340401799415726080.0000
Epoch [568/1000], Train Loss: 31939970894539427507259337342976.0000, Train L1 Loss: 189592269167494.2188
Epoch [568/1000], Validation Loss: 27356290318321376467665220009984.0000, Validation L1: 310916711141532.4375, Smoothed Validation Loss: 27356298743187144458745958891520.0000
Epoch [569/1000], Train Loss: 31940016305943836114410979459072.0000, Train L1 Loss: 189592403632399.0625
Epoch [569/1000], Validation Loss: 27356317661913115838740256784384.0000, Validation L1: 310916840527299.8750, Smoothed Validation Loss: 27356300635059739795305537732608.0000
Epoch [570/1000], Train Loss: 31940030612913334754446789312512.0000, Train L1 Loss: 189592388536454.3750
Epoch [570/1000], Validation Loss: 27356314537481760101749791653888.0000, Validation L1: 310916821178062.4375, Smoothed Validation Loss: 27356302025301944077749776809984.0000
Epoch [571/1000], Train Loss: 31939976213157749257206193192960.0000, Train L1 Loss: 189592320947195.0000
Epoch [571/1000], Validation Loss: 27356257000216487146824749023232.0000, Validation L1: 310916547663653.8125, Smoothed Validation Loss: 27356297522793399285377199505408.0000
Epoch [572/1000], Train Loss: 31939999528704153764246637772800.0000, Train L1 Loss: 189592352291345.0312
Epoch [572/1000], Validation Loss: 27356314877013058443604201046016.0000, Validation L1: 310916843076284.6875, Smoothed Validation Loss: 27356299258215366101919825133568.0000
Epoch [573/1000], Train Loss: 31939997139638996431984096444416.0000, Train L1 Loss: 189592343237282.5312
Epoch [573/1000], Validation Loss: 27356308667650590638958455029760.0000, Validation L1: 310916814953097.0625, Smoothed Validation Loss: 27356300199158885403103948963840.0000
Epoch [574/1000], Train Loss: 31939976244124185043031807754240.0000, Train L1 Loss: 189592317147201.4375
Epoch [574/1000], Validation Loss: 27356290379276012157056048955392.0000, Validation L1: 310916719134282.6250, Smoothed Validation Loss: 27356299217170599429579047174144.0000
Epoch [575/1000], Train Loss: 31939961211090123589447294386176.0000, Train L1 Loss: 189592288251401.2812
Epoch [575/1000], Validation Loss: 27356290348347203946117114888192.0000, Validation L1: 310916715323048.8750, Smoothed Validation Loss: 27356298330288258530152965734400.0000
Epoch [576/1000], Train Loss: 31940002373968722175200656883712.0000, Train L1 Loss: 189592352255184.7500
Epoch [576/1000], Validation Loss: 27356281055802988802273001340928.0000, Validation L1: 310916652881245.1875, Smoothed Validation Loss: 27356296602839730206285081083904.0000
Epoch [577/1000], Train Loss: 31939959391872524781386347839488.0000, Train L1 Loss: 189592278482456.5000
Epoch [577/1000], Validation Loss: 27356344937877839434899668336640.0000, Validation L1: 310916975849430.3750, Smoothed Validation Loss: 27356301436343540678786577072128.0000
Epoch [578/1000], Train Loss: 31939956145126605224348271771648.0000, Train L1 Loss: 189592261807912.5000
Epoch [578/1000], Validation Loss: 27356335981522184356289369341952.0000, Validation L1: 310916942538047.2500, Smoothed Validation Loss: 27356304890861403245097005350912.0000
Epoch [579/1000], Train Loss: 31940018459635240422385169465344.0000, Train L1 Loss: 189592382469585.3125
Epoch [579/1000], Validation Loss: 27356326710308291566366470701056.0000, Validation L1: 310916892415644.3125, Smoothed Validation Loss: 27356307072806090275784100937728.0000
Epoch [580/1000], Train Loss: 31939987955224046613484454019072.0000, Train L1 Loss: 189592305759982.5312
Epoch [580/1000], Validation Loss: 27356268942911140301438418157568.0000, Validation L1: 310916590483269.6875, Smoothed Validation Loss: 27356303259816595278349532659712.0000
Epoch [581/1000], Train Loss: 31939960771212617747875321872384.0000, Train L1 Loss: 189592281127588.2500
Epoch [581/1000], Validation Loss: 27356314633443258500659812499456.0000, Validation L1: 310916818745373.9375, Smoothed Validation Loss: 27356304397179262050940523380736.0000
Epoch [582/1000], Train Loss: 31939979278080552627156358791168.0000, Train L1 Loss: 189592335738046.7812
Epoch [582/1000], Validation Loss: 27356296497066297846018116419584.0000, Validation L1: 310916747088038.0625, Smoothed Validation Loss: 27356303607167966531168208158720.0000
Epoch [583/1000], Train Loss: 31939963308290459338313455108096.0000, Train L1 Loss: 189592291372176.5938
Epoch [583/1000], Validation Loss: 27356332870558131736209247961088.0000, Validation L1: 310916912822617.6250, Smoothed Validation Loss: 27356306533506983952392237613056.0000
Epoch [584/1000], Train Loss: 31940012704312203271948482904064.0000, Train L1 Loss: 189592379144933.4375
Epoch [584/1000], Validation Loss: 27356296401800740697525658320896.0000, Validation L1: 310916736447523.4375, Smoothed Validation Loss: 27356305520336359626905579683840.0000
Epoch [585/1000], Train Loss: 31939935988995549884909696843776.0000, Train L1 Loss: 189592212374240.3125
Epoch [585/1000], Validation Loss: 27356314544308410992510164271104.0000, Validation L1: 310916818642746.6250, Smoothed Validation Loss: 27356306422733565213826000879616.0000
Epoch [586/1000], Train Loss: 31940019261597666215716531994624.0000, Train L1 Loss: 189592417245917.3438
Epoch [586/1000], Validation Loss: 27356269271865162961260541640704.0000, Validation L1: 310916616586900.6875, Smoothed Validation Loss: 27356302707646723637489566744576.0000
Epoch [587/1000], Train Loss: 31940011761453059854863809118208.0000, Train L1 Loss: 189592387960356.2500
Epoch [587/1000], Validation Loss: 27356266294935927399889930027008.0000, Validation L1: 310916597070973.6250, Smoothed Validation Loss: 27356299066375645364809491283968.0000
Epoch [588/1000], Train Loss: 31940009205663491395840899022848.0000, Train L1 Loss: 189592353553532.0938
Epoch [588/1000], Validation Loss: 27356296464741400772192092815360.0000, Validation L1: 310916738094415.8750, Smoothed Validation Loss: 27356298806212220004827825963008.0000
Epoch [589/1000], Train Loss: 31939991119723090565659531149312.0000, Train L1 Loss: 189592345427098.1250
Epoch [589/1000], Validation Loss: 27356287168606177415069331095552.0000, Validation L1: 310916679966638.5000, Smoothed Validation Loss: 27356297642451613944412125528064.0000
Epoch [590/1000], Train Loss: 31939989866632721205221587419136.0000, Train L1 Loss: 189592315459120.2500
Epoch [590/1000], Validation Loss: 27356281343784131247006434721792.0000, Validation L1: 310916678736706.0625, Smoothed Validation Loss: 27356296012584866575391481921536.0000
Epoch [591/1000], Train Loss: 31940016913310432774273439367168.0000, Train L1 Loss: 189592374685108.0938
Epoch [591/1000], Validation Loss: 27356278438554084258018360295424.0000, Validation L1: 310916665151045.8750, Smoothed Validation Loss: 27356294255181789244374095233024.0000
Epoch [592/1000], Train Loss: 31939979765121293997624726126592.0000, Train L1 Loss: 189592323968637.2188
Epoch [592/1000], Validation Loss: 27356290380981782041120015908864.0000, Validation L1: 310916713937487.1250, Smoothed Validation Loss: 27356293867761788524048687300608.0000
Epoch [593/1000], Train Loss: 31940035284574095664302249738240.0000, Train L1 Loss: 189592423598430.2500
Epoch [593/1000], Validation Loss: 27356266322194229856927871926272.0000, Validation L1: 310916600974078.3125, Smoothed Validation Loss: 27356291113205035359496382185472.0000
Epoch [594/1000], Train Loss: 31939992058225555286017416626176.0000, Train L1 Loss: 189592335502532.9375
Epoch [594/1000], Validation Loss: 27356290406807250765911152394240.0000, Validation L1: 310916714336793.5000, Smoothed Validation Loss: 27356291042565255549057970995200.0000
Epoch [595/1000], Train Loss: 31939992260037907426388528332800.0000, Train L1 Loss: 189592320930064.1875
Epoch [595/1000], Validation Loss: 27356287266209827849707083268096.0000, Validation L1: 310916693577041.4375, Smoothed Validation Loss: 27356290664929712328762919485440.0000
Epoch [596/1000], Train Loss: 31940000069764253110333285072896.0000, Train L1 Loss: 189592363080350.3750
Epoch [596/1000], Validation Loss: 27356278399072602584730801537024.0000, Validation L1: 310916670454525.2500, Smoothed Validation Loss: 27356289438343999552919856742400.0000
Epoch [597/1000], Train Loss: 31940015511927719129599078039552.0000, Train L1 Loss: 189592389125415.0000
Epoch [597/1000], Validation Loss: 27356266176445401548639998836736.0000, Validation L1: 310916600380304.7500, Smoothed Validation Loss: 27356287112154141553931721900032.0000
Epoch [598/1000], Train Loss: 31940016757554939360340749582336.0000, Train L1 Loss: 189592412664900.8750
Epoch [598/1000], Validation Loss: 27356305463923685226511188623360.0000, Validation L1: 310916770448125.0625, Smoothed Validation Loss: 27356288947331096821909594046464.0000
Epoch [599/1000], Train Loss: 31939978286681441289486639038464.0000, Train L1 Loss: 189592301347859.7500
Epoch [599/1000], Validation Loss: 27356308436486505308760636915712.0000, Validation L1: 310916798520555.6875, Smoothed Validation Loss: 27356290896246640823114437492736.0000
Epoch [600/1000], Train Loss: 31939982094352658004957525442560.0000, Train L1 Loss: 189592313072433.0625
Epoch [600/1000], Validation Loss: 27356335821751997586933897232384.0000, Validation L1: 310916921265990.1250, Smoothed Validation Loss: 27356295388797177400216308940800.0000
Epoch [601/1000], Train Loss: 31940013125277346881536322961408.0000, Train L1 Loss: 189592370273799.1562
Epoch [601/1000], Validation Loss: 27356274940041052327884567347200.0000, Validation L1: 310916606477124.1250, Smoothed Validation Loss: 27356293343921567144782948466688.0000
Epoch [602/1000], Train Loss: 31939954805753018100215776804864.0000, Train L1 Loss: 189592252856542.4375
Epoch [602/1000], Validation Loss: 27356308377068056459465138896896.0000, Validation L1: 310916788227462.6875, Smoothed Validation Loss: 27356294847236214725171279298560.0000
Epoch [603/1000], Train Loss: 31940004289993509823798883385344.0000, Train L1 Loss: 189592393407979.0625
Epoch [603/1000], Validation Loss: 27356338951939201345683361628160.0000, Validation L1: 310916948647618.3125, Smoothed Validation Loss: 27356299257706513387222487531520.0000
Epoch [604/1000], Train Loss: 31940024658970961570647653744640.0000, Train L1 Loss: 189592376159079.1250
Epoch [604/1000], Validation Loss: 27356287408097823780241659658240.0000, Validation L1: 310916701426054.1250, Smoothed Validation Loss: 27356298072745644426524404744192.0000
Epoch [605/1000], Train Loss: 31940006962459234448593345576960.0000, Train L1 Loss: 189592367419686.5625
Epoch [605/1000], Validation Loss: 27356323504584841359914061266944.0000, Validation L1: 310916851684418.1875, Smoothed Validation Loss: 27356300615929565470943258607616.0000
Epoch [606/1000], Train Loss: 31939975234490597792889389973504.0000, Train L1 Loss: 189592280355046.6562
Epoch [606/1000], Validation Loss: 27356305384808910040097039056896.0000, Validation L1: 310916768603102.5000, Smoothed Validation Loss: 27356301092817499927858636652544.0000
Epoch [607/1000], Train Loss: 31940006611660934141774858813440.0000, Train L1 Loss: 189592364865803.5312
Epoch [607/1000], Validation Loss: 27356323620231172909693684154368.0000, Validation L1: 310916854696863.5625, Smoothed Validation Loss: 27356303345558867676402104139776.0000
Epoch [608/1000], Train Loss: 31940017157406937700838062161920.0000, Train L1 Loss: 189592397409629.9688
Epoch [608/1000], Validation Loss: 27356278264778779007851587174400.0000, Validation L1: 310916653739128.2500, Smoothed Validation Loss: 27356300837480857008107201495040.0000
Epoch [609/1000], Train Loss: 31939998097168088714071758602240.0000, Train L1 Loss: 189592341681930.1875
Epoch [609/1000], Validation Loss: 27356220734924165728965813600256.0000, Validation L1: 310916379403735.1875, Smoothed Validation Loss: 27356292827225185178033286283264.0000
Epoch [610/1000], Train Loss: 31939974828996877148790273867776.0000, Train L1 Loss: 189592303303303.5312
Epoch [610/1000], Validation Loss: 27356287457410568864486836404224.0000, Validation L1: 310916697926750.3125, Smoothed Validation Loss: 27356292290243725798478454980608.0000
Epoch [611/1000], Train Loss: 31939977865826437712385771831296.0000, Train L1 Loss: 189592305902896.5000
Epoch [611/1000], Validation Loss: 27356299542991976735397409456128.0000, Validation L1: 310916763124869.0625, Smoothed Validation Loss: 27356293015518550892170350428160.0000
Epoch [612/1000], Train Loss: 31940007710423514220551343177728.0000, Train L1 Loss: 189592360073041.3750
Epoch [612/1000], Validation Loss: 27356257251689311802269940842496.0000, Validation L1: 310916552091720.2500, Smoothed Validation Loss: 27356289439135624281020533047296.0000
Epoch [613/1000], Train Loss: 31939947008688250034647390486528.0000, Train L1 Loss: 189592263954787.0625
Epoch [613/1000], Validation Loss: 27356260164700543119439937142784.0000, Validation L1: 310916578484779.0625, Smoothed Validation Loss: 27356286511692117065582398930944.0000
Epoch [614/1000], Train Loss: 31939944150981235652385967177728.0000, Train L1 Loss: 189592253509489.6562
Epoch [614/1000], Validation Loss: 27356278387042803432880846405632.0000, Validation L1: 310916660667286.9375, Smoothed Validation Loss: 27356285699227184351232355467264.0000
Epoch [615/1000], Train Loss: 31939974427279681497420078776320.0000, Train L1 Loss: 189592308533546.7500
Epoch [615/1000], Validation Loss: 27356353910298424355891712098304.0000, Validation L1: 310917009695571.6875, Smoothed Validation Loss: 27356292520334310603498104815616.0000
Epoch [616/1000], Train Loss: 31940039175410066624690515869696.0000, Train L1 Loss: 189592424565567.6250
Epoch [616/1000], Validation Loss: 27356290472345325896866501492736.0000, Validation L1: 310916717603833.8750, Smoothed Validation Loss: 27356292315535409881035130798080.0000
Epoch [617/1000], Train Loss: 31940008768732587207666012520448.0000, Train L1 Loss: 189592345269637.7812
Epoch [617/1000], Validation Loss: 27356305677046827831023301033984.0000, Validation L1: 310916789554572.5625, Smoothed Validation Loss: 27356293651686549874594096873472.0000
Epoch [618/1000], Train Loss: 31939979348722678813000630009856.0000, Train L1 Loss: 189592295808464.6562
Epoch [618/1000], Validation Loss: 27356290315021075610333337354240.0000, Validation L1: 310916711792272.6875, Smoothed Validation Loss: 27356293318020001097088132710400.0000
Epoch [619/1000], Train Loss: 31939974423681237841156641914880.0000, Train L1 Loss: 189592296420404.8750
Epoch [619/1000], Validation Loss: 27356248294119180019345894932480.0000, Validation L1: 310916532634915.1875, Smoothed Validation Loss: 27356288815629918989313908932608.0000
Epoch [620/1000], Train Loss: 31940039857034391841240965447680.0000, Train L1 Loss: 189592415699490.2812
Epoch [620/1000], Validation Loss: 27356290414053511041152888864768.0000, Validation L1: 310916721683798.8125, Smoothed Validation Loss: 27356288975472275942697993240576.0000
Epoch [621/1000], Train Loss: 31939944733450519441861330862080.0000, Train L1 Loss: 189592248471139.7188
Epoch [621/1000], Validation Loss: 27356269040007694425233507221504.0000, Validation L1: 310916607990324.1250, Smoothed Validation Loss: 27356286981925816439871656427520.0000
Epoch [622/1000], Train Loss: 31939971949799937345413252644864.0000, Train L1 Loss: 189592310089891.6250
Epoch [622/1000], Validation Loss: 27356275215797835613266012798976.0000, Validation L1: 310916632568286.5625, Smoothed Validation Loss: 27356285805313022410450756698112.0000
Aborted!
Process ForkProcess-1:
Traceback (most recent call last):
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/process.py", line 240, in _process_worker
    call_item = call_queue.get(block=True)
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/queues.py", line 102, in get
    with self._rlock:
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/synchronize.py", line 95, in __enter__
    return self._semlock.__enter__()
KeyboardInterrupt
Traceback (most recent call last):
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/process.py", line 240, in _process_worker
    call_item = call_queue.get(block=True)
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/queues.py", line 102, in get
    with self._rlock:
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/synchronize.py", line 95, in __enter__
    return self._semlock.__enter__()
KeyboardInterrupt
Traceback (most recent call last):
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/process.py", line 240, in _process_worker
    call_item = call_queue.get(block=True)
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/queues.py", line 102, in get
    with self._rlock:
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/synchronize.py", line 95, in __enter__
    return self._semlock.__enter__()
KeyboardInterrupt
Traceback (most recent call last):
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/appl/python/3.10.12/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/process.py", line 240, in _process_worker
    call_item = call_queue.get(block=True)
Traceback (most recent call last):
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 94, in <module>
    Defaults.start()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 80, in run
    training_loop(model=model, train_loader=train_loader, val_loader=val_loader, epochs=epochs, optimizer=optimizer, criterion=criterion, param=param, device=device, save_path=save_path)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/train.py", line 80, in training_loop
    output = model(batch)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 328, in _fn
    return fn(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 162, in forward
    self.linear_out1 = nn.Linear(num_embeddings, hidden_out_dim)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/tmp/s230208_pyg/tmpcu5m3psq.py", line 244, in forward
    neighbours = self.get_neighbours_as_edge_index(pos, batch, self.cutoff_dist)
  File "/tmp/s230208_pyg/tmpcu5m3psq.py", line 246, in <resume in forward>
    return self.propagate(neighbours, s=embeddings, v=equivar_repr, r=pos, neighbours=neighbours, size=None)
  File "/tmp/s230208_pyg/tmpcu5m3psq.py", line 227, in propagate
    return self.update(out, s=kwargs.s, v=kwargs.v)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 95, in update
    s_i, v_i = agg_message
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
KeyboardInterrupt
Terminated

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19590330: <dynamoFix_0> in cluster <dcc> Exited

Job <dynamoFix_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Tue Nov 28 16:00:31 2023
Job was executed on host(s) <4*n-62-18-12>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Tue Nov 28 18:17:01 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Tue Nov 28 18:17:01 2023
Terminated at Wed Nov 29 09:26:42 2023
Results reported at Wed Nov 29 09:26:42 2023

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

TERM_OWNER: job killed by owner.
Exited with exit code 143.

Resource usage summary:

    CPU time :                                   55162.00 sec.
    Max Memory :                                 1946 MB
    Average Memory :                             1930.84 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               63590.00 MB
    Max Swap :                                   -
    Max Processes :                              10
    Max Threads :                                49
    Run time :                                   54582 sec.
    Turnaround time :                            62771 sec.

The output (if any) is above this job summary.

