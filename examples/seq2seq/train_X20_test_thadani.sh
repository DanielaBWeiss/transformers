for i in {1..20}
do

    CUDA_VISIBLE_DEVICES=$1,$2,$3  python finetune_trainer.py --model_name_or_path=facebook/bart-base --learning_rate=3e-5 --do_train --do_eval --do_predict --num_train_epochs=4 --evaluation_strategy steps --eval_steps=5000 --per_device_train_batch_size=10 --per_device_eval_batch_size=10 --max_source_length=265 --eval_beams=6 --max_target_length=30 --val_max_target_length=30 --test_max_target_length=30 --data_dir training_data/$4/$5$i --output_dir ../../../output_models/$5$i --predict_with_generate --min_target_length=4 &> val_$i.log 

done


for i in {1..20}
do

    CUDA_VISIBLE_DEVICES=$1,$2,$3  python finetune_trainer.py --model_name_or_path=../../../output_models/$5$i --learning_rate=3e-5 --do_eval --do_predict --num_train_epochs=4  --eval_steps=5000 --per_device_train_batch_size=10 --per_device_eval_batch_size=10 --max_source_length=265 --eval_beams=6 --max_target_length=30 --val_max_target_length=30 --test_max_target_length=30 --data_dir training_data/training/thadani-baseline/thadani_\#$i --output_dir ../../../output_models/$5$i --predict_with_generate --min_target_length=4 &> val_thadani_$i.log

done

