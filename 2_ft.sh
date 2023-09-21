nohup python run_mindformer.py --config \
    ./nsc_config/collection_2.yaml --run_mode\
    finetune --load_checkpoint\
    ./checkpoint_download/gpt2/gpt2.ckpt --device_target\
    GPU --train_dataset_dir\
    ./data/nsc_collection_2.mindrecord > ft_2.log 2>&1 &
