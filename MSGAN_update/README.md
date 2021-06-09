### Prerequisites and Installation

Refer to [p2pHD](https://github.com/NVIDIA/pix2pixHD).


### Training
an example:
```
python3 train.py --dataroot  dataroot_of_the_data --name model_name --resize_or_crop none --loadSize 512 --fineSize 512 --label_nc 0 --no_instance --save_epoch_freq 300 --netG global --n_downsample_global 3 --n_blocks_global 9
```


## Acknowledgments
This code borrows heavily from [p2pHD](https://github.com/NVIDIA/pix2pixHD).
