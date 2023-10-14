# Execute Training

```bash
export PYTORCH_ENABLE_MPS_FALLBACK='1' && python training_run.py
```

## Euler Setup

### Environment
0. Create environment and activate it
    ```bash
    module load gcc/6.3.0 python/3.8.5
    python -m venv --system-site-packages iplanner_venv
    source iplanner_venv/bin/activate
    ```
1. Load modules
    ```bash
    module load gcc/8.2.0 cuda/11.8.0 python/3.8.5 cudnn/8.0.5 cmake/3.19.8 eth_proxy
    ```
2. Activate Environment
    ```bash
    module load gcc/6.3.0 python/3.8.5
    source iplanner_venv/bin/activate
    ```

### Running on Interactive Mode
```bash
srun -n 4 --mem-per-cpu=4000 --gpus=gtx_1080_ti:1 --pty bash
export EXPERIMENT_DIRECTORY="/cluster/home/passutte/semester_project/iPlanner/iPlanner/iplanner"
export DATA_DIRECTORY= "/cluster/scratch/passutte/iPlanner_data"
python training_run.py --data-root data/public --wandb

```
### Submit Job on Euler
Data Generation
```bash
sbatch -n 4 --time=24:00:00 --mem-per-cpu=4000 --gpus=1 --gres=gpumem:11G --output="training_log" \
--export=EXPERIMENT_DIRECTORY="/cluster/home/passutte/semester_project/iPlanner/iPlanner/iplanner" \
--export=DATA_DIRECTORY="/cluster/scratch/passutte/iPlanner_data" \
--wrap="python data_generation.py"
```

Training
```bash
sbatch -n 4 --time=24:00:00 --mem-per-cpu=4000 --gpus=1 --gres=gpumem:11G --output="training_log" 
--export=EXPERIMENT_DIRECTORY="/cluster/home/passutte/semester_project/iPlanner/iPlanner/iplanner"
--export=DATA_DIRECTORY="/cluster/scratch/passutte/iPlanner_data"
--wrap="python training_run.py"
```

Info of Job:
```bash
squeue
scancel job_id
myjobs -j job_id
vim  training_log
srun --interactive --jobid job_id --pty bash
```

