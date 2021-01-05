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
python finetune_trainer.py \
    --learning_rate=3e-5 \
    --do_train \
    --freeze_encoder \
    --val_check_interval=0.1 \
    --eval_batch_size=2 \
    --max_source_length=265 \
    --max_target_length=30 \
    --val_max_target_length=50 \
    --test_max_target_length=50 \
    --model_name_or_path=sshleifer/distilbart-xsum-12-6 \
    "$@"
