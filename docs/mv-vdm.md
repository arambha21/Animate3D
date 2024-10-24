# Training
Please download MV-Video dataset from [Huggingface](https://huggingface.co/datasets/yanqinJiang/MV-Video) and prepare the dataset according to its instructions. Then use the following command to genereate training json file:
```bash
python tools/generate_training_info.py \
    --uid_info_dict_path /path/to/your/uid/info/dict/file/ \
    --data_root /path/to/your/videos/folder/
```
Training json file will be found at `data/vdm/meta/training_info.json`.

Use the following command to train:
```bash
bash train.sh ${machine_num} ${gpu_per_machine} ${config_name} 
```
For example:
```bash
bash train.sh 1 2 train 
```
You can find the outputs in `outputs/vdm/train` folder. 
# Inference
Use the following command to inference:
```bash
bash inference.sh ${gpu_id} ${config_file} ${prompt} ${ip_image_root} ${ip_image_name} ${save_name}
```
For example:
```bash
bash inference.sh 1 inference "A lion is attacking." "data/vdm/examples/images" "051a2a7ea842426f825e128fef3bf92b" "vdm/inference"
```
You can find the outputs in `outputs/vdm/inference` folder. 