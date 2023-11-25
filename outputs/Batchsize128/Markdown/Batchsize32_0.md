wandb: Currently logged in as: chessproject65. Use `wandb login --relogin` to force relogin
wandb: Tracking run with wandb version 0.16.0
wandb: Run data is saved locally in /zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/wandb/run-20231125_122346-5kqf3gmc
wandb: Run `wandb offline` to turn off syncing.
wandb: Syncing run Batchsize128-0
wandb: ⭐️ View project at https://wandb.ai/chessproject65/deeplearning_painn
wandb: 🚀 View run at https://wandb.ai/chessproject65/deeplearning_painn/runs/5kqf3gmc

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
| <c>name</c>       | <d>str</d>        | <j>"Batchsize128-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>84600</f>      |
| <c>epochs</c>     | <d>int</d>        | <f>1000</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>32</f>         |
| <c>num_atoms</c>  | <d>int</d>        | <f>10</f>         |
| <c>num_embeddings</c>| <d>int</d>        | <f>128</f>        |
| <c>cutoff_dist</c>| <d>float</d>      | <f>5.0</f>        |
| <c>hidden_out_dim</c>| <d>int</d>        | <f>128</f>        |

# Output

```
Traceback (most recent call last):
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 76, in <module>
    Defaults.start()
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/main.py", line 62, in run
    training_loop(model=model, train_loader=train_loader, val_loader=val_loader, epochs=epochs, optimizer=optimizer, criterion=criterion, param=param, isServer=isServer, name=name, batch_size=batch_size, num_atoms=num_atoms, num_embeddings=num_embeddings, cutoff_dist=cutoff_dist, device=device)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/train.py", line 74, in training_loop
    output = model(batch)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 153, in forward
    embeddings, equivariant_repr = self.message(embeddings, equivariant_repr, data.pos, data.batch)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/project-env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 21, in forward
    neighbours = self.get_neighbours_as_edge_index(pos, batch, self.cutoff_dist)
  File "/zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023/PaiNN.py", line 52, in get_neighbours_as_edge_index
    neighbours = neighbours * torch.block_diag(*[torch.ones((u,u)) for u in unique[1]])
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!
wandb: 🚀 View run Batchsize128-0 at: https://wandb.ai/chessproject65/deeplearning_painn/runs/5kqf3gmc
wandb: ️⚡ View job at https://wandb.ai/chessproject65/deeplearning_painn/jobs/QXJ0aWZhY3RDb2xsZWN0aW9uOjExODQwNjM4Mg==/version_details/v1
wandb: Synced 5 W&B file(s), 0 media file(s), 2 artifact file(s) and 0 other file(s)
wandb: Find logs at: ./wandb/run-20231125_122346-5kqf3gmc/logs

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 19543409: <Batchsize128_0> in cluster <dcc> Exited

Job <Batchsize128_0> was submitted from host <gbarlogin2> by user <s230208> in cluster <dcc> at Sat Nov 25 12:23:03 2023
Job was executed on host(s) <4*n-62-18-9>, in queue <gpua100>, as user <s230208> in cluster <dcc> at Sat Nov 25 12:23:05 2023
</zhome/59/9/198225> was used as the home directory.
</zhome/59/9/198225/Desktop/Deep_learning_2023/Deep_learning_2023> was used as the working directory.
Started at Sat Nov 25 12:23:05 2023
Terminated at Sat Nov 25 12:24:12 2023
Results reported at Sat Nov 25 12:24:12 2023

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

    CPU time :                                   11.29 sec.
    Max Memory :                                 107 MB
    Average Memory :                             107.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65429.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   168 sec.
    Turnaround time :                            69 sec.

The output (if any) is above this job summary.

