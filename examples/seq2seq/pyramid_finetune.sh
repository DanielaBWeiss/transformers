# Copyright 2020 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# the proper usage is documented in the README, you need to specify data_dir, output_dir and model_name_or_path
# run ./finetune.sh --help to see all the possible options

#The max and min numbers apply to the training data that has only up to 4 input sentences

#PARAMS
#calculating generative metrics (BLEU, ROUGE) is optional and is controlled using the --predict_with_generate
#For multi-gpu training use torch.distributed.launch, e.g. with 2 gpus:
    #python -m torch.distributed.launch --nproc_per_node=2  finetune_trainer.py ...
#--data_dir $XSUM_DIR
#--output_dir
#--gpus=1
#--eval_beams=6
#--config_name=fusion_config.json when we want to make our own configuration to the beam search

#command to run: "./pyramid_finetune.sh  --n_train 10 --n_val 5 --data_dir training_data/tiny --output_dir output_models/tiny"
#data_dir is the training data, #output_dir saves the model. The rest of the options are here.

python finetune_trainer.py \
    --learning_rate=3e-5 \
    --overwrite_output_dir \
    --do_train \
    --do_eval --do_predict\
    --task 'summarization' \
    --num_train_epochs=3 \
    --freeze_encoder \
    --evaluation_strategy steps \
    --predict_with_generate \
    --eval_steps=100 \
    --per_device_train_batch_size=2 \
    --per_device_eval_batch_size=2 \
    --max_source_length=265 \
    --max_target_length=30 \
    --val_max_target_length=30 \
    --test_max_target_length=50 \
    --model_name_or_path=sshleifer/distilbart-xsum-12-6 \
    "$@"
