#!/usr/bin/env bash
cd ../../
save_dir=check_different_alpha_run5
declare -a StringArray=(
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Loss.jsd_alpha=0.0 Trainer.save_dir=${save_dir}/check_alpha/0.0"
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Loss.jsd_alpha=0.2 Trainer.save_dir=${save_dir}/check_alpha/0.2"
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Loss.jsd_alpha=0.4 Trainer.save_dir=${save_dir}/check_alpha/0.4"
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Loss.jsd_alpha=0.6 Trainer.save_dir=${save_dir}/check_alpha/0.6"
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Loss.jsd_alpha=0.8 Trainer.save_dir=${save_dir}/check_alpha/0.8"
"python train_ACDC_cotraining.py  config=config/ACDC_config_cotraing.yaml Loss.jsd_alpha=1.0 Trainer.save_dir=${save_dir}/check_alpha/1.0"
)
# just using 0 and 1 gpus for those jobs
gpuqueue "${StringArray[@]}" --available_gpus 3 4