_base_ = './fcos_r50_caffe_fpn_gn-head_4x4_1x_coco.py'
model = dict(
    #pretrained='open-mmlab://detectron/resnet101_caffe',
    pretrained='../checkpoint/resnet101_caffe-3ad79236.pth',
    backbone=dict(depth=101))
