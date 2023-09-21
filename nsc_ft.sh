nohup python run_mindformer.py --config \
    ./nsc_config/nsc.yaml --run_mode\
    finetune --load_checkpoint\
    ./checkpoint_download/gpt2/gpt2.ckpt --device_target\
    GPU --train_dataset_dir\
    ./data/nsc_train.mindrecord > fine_tune_nsc.log 2>&1 &
