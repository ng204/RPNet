ann_file = '/root/autodl-tmp/mmaction2/tools/data/skeleton/my_train.pkl'
auto_scale_lr = dict(base_batch_size=48, enable=False)
backbone_cfg = dict(
    channel_ratio=4,
    pose_pathway=dict(
        base_channels=32,
        conv1_kernel=(
            1,
            7,
            7,
        ),
        conv1_stride_s=1,
        conv1_stride_t=1,
        dilations=(
            1,
            1,
            1,
        ),
        fusion_kernel=7,
        in_channels=16,
        inflate=(
            0,
            1,
            1,
        ),
        lateral=True,
        lateral_activate=(
            0,
            1,
            1,
        ),
        lateral_infl=16,
        lateral_inv=True,
        num_stages=3,
        out_indices=(2, ),
        pool1_stride_s=1,
        pool1_stride_t=1,
        spatial_strides=(
            2,
            2,
            2,
        ),
        stage_blocks=(
            4,
            6,
            3,
        ),
        temporal_strides=(
            1,
            1,
            1,
        ),
        with_pool2=False),
    rgb_pathway=dict(
        base_channels=64,
        conv1_kernel=(
            1,
            7,
            7,
        ),
        fusion_kernel=7,
        inflate=(
            0,
            0,
            1,
            1,
        ),
        lateral=True,
        lateral_activate=[
            0,
            0,
            1,
            1,
        ],
        lateral_infl=1,
        num_stages=4,
        with_pool2=False),
    speed_ratio=4,
    type='RGBPoseConv3D')
data_preprocessor = dict(
    preprocessors=dict(
        heatmap_imgs=dict(type='ActionDataPreprocessor'),
        imgs=dict(
            format_shape='NCTHW',
            mean=[
                123.675,
                116.28,
                103.53,
            ],
            std=[
                58.395,
                57.12,
                57.375,
            ],
            type='ActionDataPreprocessor')),
    type='MultiModalDataPreprocessor')
data_root = '/root/autodl-tmp/mmaction2/videos/'
dataset_type = 'PoseDataset'
default_hooks = dict(
    checkpoint=dict(interval=1, save_best='auto', type='CheckpointHook'),
    logger=dict(ignore_last=False, interval=20, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    runtime_info=dict(type='RuntimeInfoHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    sync_buffers=dict(type='SyncBuffersHook'),
    timer=dict(type='IterTimerHook'))
default_scope = 'mmaction'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
head_cfg = dict(
    average_clips='prob',
    in_channels=[
        2048,
        512,
    ],
    loss_components=[
        'rgb',
        'pose',
    ],
    loss_weights=[
        1.0,
        1.0,
    ],
    num_classes=60,
    type='RGBPoseHead')
launcher = 'none'
left_kp = [
    3,
    4,
    5,
    10,
    11,
    12,
]
load_from = 'https://download.openmmlab.com/mmaction/v1.0/skeleton/posec3d/rgbpose_conv3d/rgbpose_conv3d_init_20230228-09b7684b.pth'
log_level = 'INFO'
log_processor = dict(by_epoch=True, type='LogProcessor', window_size=20)
model = dict(
    backbone=dict(
        channel_ratio=4,
        pose_pathway=dict(
            base_channels=32,
            conv1_kernel=(
                1,
                7,
                7,
            ),
            conv1_stride_s=1,
            conv1_stride_t=1,
            dilations=(
                1,
                1,
                1,
            ),
            fusion_kernel=7,
            in_channels=16,
            inflate=(
                0,
                1,
                1,
            ),
            lateral=True,
            lateral_activate=(
                0,
                1,
                1,
            ),
            lateral_infl=16,
            lateral_inv=True,
            num_stages=3,
            out_indices=(2, ),
            pool1_stride_s=1,
            pool1_stride_t=1,
            spatial_strides=(
                2,
                2,
                2,
            ),
            stage_blocks=(
                4,
                6,
                3,
            ),
            temporal_strides=(
                1,
                1,
                1,
            ),
            with_pool2=False),
        rgb_pathway=dict(
            base_channels=64,
            conv1_kernel=(
                1,
                7,
                7,
            ),
            fusion_kernel=7,
            inflate=(
                0,
                0,
                1,
                1,
            ),
            lateral=True,
            lateral_activate=[
                0,
                0,
                1,
                1,
            ],
            lateral_infl=1,
            num_stages=4,
            with_pool2=False),
        speed_ratio=4,
        type='RGBPoseConv3D'),
    cls_head=dict(
        average_clips='prob',
        in_channels=[
            2048,
            512,
        ],
        loss_components=[
            'rgb',
            'pose',
        ],
        loss_weights=[
            1.0,
            1.0,
        ],
        num_classes=60,
        type='RGBPoseHead'),
    data_preprocessor=dict(
        preprocessors=dict(
            heatmap_imgs=dict(type='ActionDataPreprocessor'),
            imgs=dict(
                format_shape='NCTHW',
                mean=[
                    123.675,
                    116.28,
                    103.53,
                ],
                std=[
                    58.395,
                    57.12,
                    57.375,
                ],
                type='ActionDataPreprocessor')),
        type='MultiModalDataPreprocessor'),
    type='MMRecognizer3D')
optim_wrapper = dict(
    clip_grad=dict(max_norm=40, norm_type=2),
    optimizer=dict(lr=0.0075, momentum=0.9, type='SGD', weight_decay=0.0001))
param_scheduler = [
    dict(
        begin=0,
        by_epoch=True,
        end=20,
        gamma=0.1,
        milestones=[
            12,
            16,
        ],
        type='MultiStepLR'),
]
randomness = dict(deterministic=False, diff_rank_seed=False, seed=None)
resume = False
right_kp = [
    6,
    7,
    8,
    13,
    14,
    15,
]
test_cfg = dict(type='TestLoop')
test_dataloader = dict(
    batch_size=2,
    dataset=dict(
        ann_file='/root/autodl-tmp/mmaction2/tools/data/skeleton/my_train.pkl',
        data_prefix=dict(video='/root/autodl-tmp/mmaction2/videos/'),
        pipeline=[
            dict(
                clip_len=dict(Pose=32, RGB=8),
                num_clips=10,
                test_mode=True,
                type='MMUniformSampleFrames'),
            dict(type='MMDecode'),
            dict(allow_imgpad=True, hw_ratio=1.0, type='MMCompact'),
            dict(keep_ratio=False, scale=(
                256,
                256,
            ), type='Resize'),
            dict(
                scaling=0.25,
                sigma=0.7,
                type='GeneratePoseTarget',
                use_score=True,
                with_kp=True,
                with_limb=False),
            dict(input_format='NCTHW', type='FormatShape'),
            dict(
                collect_keys=(
                    'imgs',
                    'heatmap_imgs',
                ),
                type='PackActionInputs'),
        ],
        split='xsub_val',
        test_mode=True,
        type='PoseDataset'),
    num_workers=16,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
test_evaluator = [
    dict(type='AccMetric'),
]
test_pipeline = [
    dict(
        clip_len=dict(Pose=32, RGB=8),
        num_clips=10,
        test_mode=True,
        type='MMUniformSampleFrames'),
    dict(type='MMDecode'),
    dict(allow_imgpad=True, hw_ratio=1.0, type='MMCompact'),
    dict(keep_ratio=False, scale=(
        256,
        256,
    ), type='Resize'),
    dict(
        scaling=0.25,
        sigma=0.7,
        type='GeneratePoseTarget',
        use_score=True,
        with_kp=True,
        with_limb=False),
    dict(input_format='NCTHW', type='FormatShape'),
    dict(collect_keys=(
        'imgs',
        'heatmap_imgs',
    ), type='PackActionInputs'),
]
train_cfg = dict(
    max_epochs=20, type='EpochBasedTrainLoop', val_begin=1, val_interval=1)
train_dataloader = dict(
    batch_size=12,
    dataset=dict(
        ann_file='/root/autodl-tmp/mmaction2/tools/data/skeleton/my_train.pkl',
        data_prefix=dict(video='/root/autodl-tmp/mmaction2/videos/'),
        pipeline=[
            dict(
                clip_len=dict(Pose=32, RGB=8),
                num_clips=1,
                type='MMUniformSampleFrames'),
            dict(type='MMDecode'),
            dict(allow_imgpad=True, hw_ratio=1.0, type='MMCompact'),
            dict(keep_ratio=False, scale=(
                256,
                256,
            ), type='Resize'),
            dict(area_range=(
                0.56,
                1.0,
            ), type='RandomResizedCrop'),
            dict(keep_ratio=False, scale=(
                224,
                224,
            ), type='Resize'),
            dict(
                flip_ratio=0.5,
                left_kp=[
                    3,
                    4,
                    5,
                    10,
                    11,
                    12,
                ],
                right_kp=[
                    6,
                    7,
                    8,
                    13,
                    14,
                    15,
                ],
                type='Flip'),
            dict(
                scaling=0.25,
                sigma=0.7,
                type='GeneratePoseTarget',
                use_score=True,
                with_kp=True,
                with_limb=False),
            dict(input_format='NCTHW', type='FormatShape'),
            dict(
                collect_keys=(
                    'imgs',
                    'heatmap_imgs',
                ),
                type='PackActionInputs'),
        ],
        split='xsub_train',
        type='PoseDataset'),
    num_workers=16,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(
        clip_len=dict(Pose=32, RGB=8),
        num_clips=1,
        type='MMUniformSampleFrames'),
    dict(type='MMDecode'),
    dict(allow_imgpad=True, hw_ratio=1.0, type='MMCompact'),
    dict(keep_ratio=False, scale=(
        256,
        256,
    ), type='Resize'),
    dict(area_range=(
        0.56,
        1.0,
    ), type='RandomResizedCrop'),
    dict(keep_ratio=False, scale=(
        224,
        224,
    ), type='Resize'),
    dict(
        flip_ratio=0.5,
        left_kp=[
            3,
            4,
            5,
            10,
            11,
            12,
        ],
        right_kp=[
            6,
            7,
            8,
            13,
            14,
            15,
        ],
        type='Flip'),
    dict(
        scaling=0.25,
        sigma=0.7,
        type='GeneratePoseTarget',
        use_score=True,
        with_kp=True,
        with_limb=False),
    dict(input_format='NCTHW', type='FormatShape'),
    dict(collect_keys=(
        'imgs',
        'heatmap_imgs',
    ), type='PackActionInputs'),
]
val_cfg = dict(type='ValLoop')
val_dataloader = dict(
    batch_size=2,
    dataset=dict(
        ann_file='/root/autodl-tmp/mmaction2/tools/data/skeleton/my_train.pkl',
        data_prefix=dict(video='/root/autodl-tmp/mmaction2/videos/'),
        pipeline=[
            dict(
                clip_len=dict(Pose=32, RGB=8),
                num_clips=1,
                test_mode=True,
                type='MMUniformSampleFrames'),
            dict(type='MMDecode'),
            dict(allow_imgpad=True, hw_ratio=1.0, type='MMCompact'),
            dict(keep_ratio=False, scale=(
                256,
                256,
            ), type='Resize'),
            dict(
                scaling=0.25,
                sigma=0.7,
                type='GeneratePoseTarget',
                use_score=True,
                with_kp=True,
                with_limb=False),
            dict(input_format='NCTHW', type='FormatShape'),
            dict(
                collect_keys=(
                    'imgs',
                    'heatmap_imgs',
                ),
                type='PackActionInputs'),
        ],
        split='xsub_val',
        test_mode=True,
        type='PoseDataset'),
    num_workers=16,
    persistent_workers=True,
    sampler=dict(shuffle=False, type='DefaultSampler'))
val_evaluator = [
    dict(type='AccMetric'),
]
val_pipeline = [
    dict(
        clip_len=dict(Pose=32, RGB=8),
        num_clips=1,
        test_mode=True,
        type='MMUniformSampleFrames'),
    dict(type='MMDecode'),
    dict(allow_imgpad=True, hw_ratio=1.0, type='MMCompact'),
    dict(keep_ratio=False, scale=(
        256,
        256,
    ), type='Resize'),
    dict(
        scaling=0.25,
        sigma=0.7,
        type='GeneratePoseTarget',
        use_score=True,
        with_kp=True,
        with_limb=False),
    dict(input_format='NCTHW', type='FormatShape'),
    dict(collect_keys=(
        'imgs',
        'heatmap_imgs',
    ), type='PackActionInputs'),
]
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    type='ActionVisualizer', vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = './work_dirs/rgbpose_conv3d-ep20'
