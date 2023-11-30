#!/bin/sh
mkdir -p outputs/WorkingSetup/Markdown
bsub -o "outputs/WorkingSetup/Markdown/WorkingSetup_0.md" -J "WorkingSetup_0" -env MYARGS="-name WorkingSetup-0 -time 84600 -epochs 1000 -batch_size 32 -isServer True -num_atoms 10 -num_embeddings 128 -cutoff_dist 5.0 -hidden_out_dim 128 -ID 0" < submit_gpu_a80.sh
