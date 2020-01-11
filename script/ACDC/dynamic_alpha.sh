#!/usr/bin/env bash
cd ../../
save_dir=check_dynamic_alpha
declare -a StringArray=(
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Loss.jsd_alpha=1.0 Trainer.save_dir=${save_dir}/reduce2"
)
# just using 0 and 1 gpus for those jobs
gpuqueue "${StringArray[@]}" --available_gpus 1 6