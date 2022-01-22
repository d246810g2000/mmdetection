_base_ = ['faster_rcnn_r50_fpn_1x_coco.py']

dataset_type = 'CocoDataset'
classes = ('car',)
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        # 將類別名字添加至 `classes` 字段中
        classes=classes,
        ann_file='datasets/car/annotations/instances_train2017.json',
        img_prefix='datasets/car/train2017'),
    val=dict(
        type=dataset_type,
        # 將類別名字添加至 `classes` 字段中
        classes=classes,
        ann_file='datasets/car/annotations/instances_val2017.json',
        img_prefix='datasets/car/val2017'),
    test=dict(
        type=dataset_type,
        # 將類別名字添加至 `classes` 字段中
        classes=classes,
        ann_file='datasets/car/annotations/instances_val2017.json',
        img_prefix='datasets/car/val2017'))

# 2. 模型設置

# 將所有的 `num_classes` 默認值修改為3（原來為80）
model = dict(
    roi_head=dict(
        bbox_head=dict(
                type='Shared2FCBBoxHead',
                # 將 `num_classes` 默認值修改為 1（原來為 80）
                num_classes=1)))