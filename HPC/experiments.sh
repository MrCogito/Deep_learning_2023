#!/bin/sh
mkdir -p outputs/Batchsize128/Markdown
bsub -o "outputs/Batchsize128/Markdown/Batchsize128_0.md" -J "Batchsize128_0" -env MYARGS="-name Batchsize128-0 -time 84600 -epochs 1000 -batch_size 128 -isServer True -num_atoms 10 -num_embeddings 128 -cutoff_dist 5.0 -hidden_out_dim 128 -ID 0" < submit_gpu_a80.sh
