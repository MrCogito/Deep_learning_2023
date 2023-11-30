
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
| <c>name</c>       | <d>str</d>        | <j>"NamingFix-0"</j> |
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
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231128_153355-sjijhmo2
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run NamingFix-0
wandb: ⭐️ View project at https://wandb.ai/chessproject65/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/chessproject65/deeplearning_painn/runs/sjijhmo2
/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py:135: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
  warnings.warn(
Traceback (most recent call last):
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 91, in <module>
    Defaults.start()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 77, in run
    training_loop(model=model, train_loader=train_loader, val_loader=val_loader, epochs=epochs, optimizer=optimizer, criterion=criterion, param=param, device=device, save_path=save_path)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/train.py", line 78, in training_loop
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
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 161, in forward
    embeddings, equivariant_repr = self.messagelayer(embeddings, equivariant_repr, data.pos, data.batch)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/tmp/s230208_pyg/tmpwkra3z0q.py", line 244, in forward
    neighbours = self.get_neighbours_as_edge_index(pos, batch, self.cutoff_dist)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 117, in get_neighbours_as_edge_index
    unique = torch.unique(batch, return_counts=True)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 490, in catch_errors
    return callback(frame, cache_entry, hooks, frame_state)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 641, in _convert_frame
    result = inner_convert(frame, cache_size, hooks, frame_state)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 133, in _fn
    return fn(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 389, in _convert_frame_assert
    return _compile(
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 569, in _compile
    guarded_code = compile_inner(code, one_graph, hooks, transform)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 189, in time_wrapper
    r = func(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 491, in compile_inner
    out_code = transform_code_object(code, transform)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/bytecode_transformation.py", line 1028, in transform_code_object
    transformations(instructions, code_options)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 458, in transform
    tracer.run()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 2069, in run
    super().run()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 719, in run
    and self.step()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 683, in step
    getattr(self, inst.opname)(inst)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 439, in wrapper
    self.output.compile_subgraph(self, reason=reason)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 857, in compile_subgraph
    self.compile_and_call_fx_graph(tx, pass2.graph_output_vars(), root)
  File "/appl/python/3.10.12/lib/python3.10/contextlib.py", line 79, in inner
    return func(*args, **kwds)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 957, in compile_and_call_fx_graph
    compiled_fn = self.call_user_compiler(gm)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 189, in time_wrapper
    r = func(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 1024, in call_user_compiler
    raise BackendCompilerFailed(self.compiler_fn, e).with_traceback(
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 1009, in call_user_compiler
    compiled_fn = compiler_fn(gm, self.example_inputs())
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/repro/after_dynamo.py", line 117, in debug_wrapper
    compiled_gm = compiler_fn(gm, example_inputs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/__init__.py", line 1568, in __call__
    return compile_fx(model_, inputs_, config_patches=self.config)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py", line 1150, in compile_fx
    return aot_autograd(
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/backends/common.py", line 55, in compiler_fn
    cg = aot_module_simplified(gm, example_inputs, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_functorch/aot_autograd.py", line 3891, in aot_module_simplified
    compiled_fn = create_aot_dispatcher_function(
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 189, in time_wrapper
    r = func(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_functorch/aot_autograd.py", line 3429, in create_aot_dispatcher_function
    compiled_fn = compiler_fn(flat_fn, fake_flat_args, aot_config, fw_metadata=fw_metadata)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_functorch/aot_autograd.py", line 2212, in aot_wrapper_dedupe
    return compiler_fn(flat_fn, leaf_flat_args, aot_config, fw_metadata=fw_metadata)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_functorch/aot_autograd.py", line 2392, in aot_wrapper_synthetic_base
    return compiler_fn(flat_fn, flat_args, aot_config, fw_metadata=fw_metadata)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_functorch/aot_autograd.py", line 1573, in aot_dispatch_base
    compiled_fw = compiler(fw_module, flat_args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 189, in time_wrapper
    r = func(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py", line 1092, in fw_compiler_base
    return inner_compile(
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/repro/after_aot.py", line 80, in debug_wrapper
    inner_compiled_fn = compiler_fn(gm, example_inputs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/debug.py", line 228, in inner
    return fn(*args, **kwargs)
  File "/appl/python/3.10.12/lib/python3.10/contextlib.py", line 79, in inner
    return func(*args, **kwds)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py", line 54, in newFunction
    return old_func(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py", line 341, in compile_fx_inner
    compiled_graph: CompiledFxGraph = fx_codegen_and_compile(
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/compile_fx.py", line 565, in fx_codegen_and_compile
    compiled_fn = graph.compile_to_fn()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/graph.py", line 970, in compile_to_fn
    return self.compile_to_module().call
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 189, in time_wrapper
    r = func(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/graph.py", line 941, in compile_to_module
    mod = PyCodeCache.load_by_key_path(key, path, linemap=linemap)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/codecache.py", line 1139, in load_by_key_path
    exec(code, mod.__dict__, mod.__dict__)
  File "/tmp/torchinductor_s230208/tn/ctnia7up7wd6yksk3ikaefmodgyx62kz4p6ro5ccb2qtigdsp64d.py", line 130, in <module>
    async_compile.wait(globals())
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/codecache.py", line 1418, in wait
    scope[key] = result.result()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/_inductor/codecache.py", line 1277, in result
    self.future.result()
  File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 458, in result
    return self.__get_result()
  File "/appl/python/3.10.12/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
    raise self._exception
torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
FileNotFoundError: [Errno 2] No such file or directory: 'ldconfig'

Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

wandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: | 0.005 MB of 0.005 MB uploadedwandb: / 0.005 MB of 0.005 MB uploadedwandb: - 0.005 MB of 0.005 MB uploadedwandb: \ 0.005 MB of 0.005 MB uploadedwandb: 🚀 View run NamingFix-0 at: https://wandb.ai/chessproject65/deeplearning_painn/runs/sjijhmo2
wandb: ️⚡ View job at https://wandb.ai/chessproject65/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjExODQwNjM4Mg==/version_details/v4
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231128_153355-sjijhmo2/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19588143: <NamingFix_0> in cluster <dcc> Exited

Job <NamingFix_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Tue Nov 28 12:34:59 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Tue Nov 28 15:32:45 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Tue Nov 28 15:32:45 2023
Terminated at Tue Nov 28 15:34:32 2023
Results reported at Tue Nov 28 15:34:32 2023

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   21.03 sec.
    Max Memory :                                 73 MB
    Average Memory :                             73.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65463.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   108 sec.
    Turnaround time :                            10773 sec.

The output (if any) is above this job summary.

