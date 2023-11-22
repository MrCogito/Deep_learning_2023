#!/bin/sh
mkdir -p outputs/Test1/Markdown
bsub -o "outputs/Test1/Markdown/Test1_0.md" -J "Test1_0" -env MYARGS="-name Test1-0 -time 84600 -ID 0" < submit_gpu_a80.sh
