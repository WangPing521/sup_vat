#!/usr/bin/env bash
cd ../../
save_dir=sup_vat_baseline
declare -a StringArray=(
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Trainer.save_dir=${save_dir}/epsilon1"
)
# just using 0 and 1 gpus for those jobs
gpuqueue "${StringArray[@]}" --available_gpus 1