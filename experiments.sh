#!/bin/sh
mkdir -p outputs/LossFix/Markdown
bsub -o "outputs/LossFix/Markdown/LossFix_0.md" -J "LossFix_0" -env MYARGS="-name LossFix-0 -time 84600 -epochs 1000 -batch_size 32 -isServer True -num_atoms 10 -num_embeddings 128 -cutoff_dist 5.0 -hidden_out_dim 128 -ID 0" < submit_gpu_a80.sh
