#!/usr/bin/env python
# coding: utf-8

import numpy as np


def conv(_img: np.ndarray, _filter: np.ndarray, _stride: int = 1, _padding: int = 0) -> np.ndarray:
    """
    卷积\n
    :param _img: 图像
    :param _filter: 卷积核
    :param _stride: 步长
    :param _padding: 填充大小
    :return: 卷积后的图像
    """
    result = np.zeros((int((_img.shape[0] - _filter.shape[0] + 2 * _padding) / _stride + 1), int((_img.shape[1] - _filter.shape[1] + 2 * _padding) / _stride + 1)), dtype=float)
    _img = np.pad(_img, _padding)
    for i in range(0, _img.shape[0] - _filter.shape[0] + 1, _stride):
        for j in range(0, _img.shape[1] - _filter.shape[1] + 1, _stride):
            result[i, j] = np.sum(_img[i:i + _filter.shape[0], j:j + _filter.shape[1]] * _filter)
    return np.clip(result, 0, 255)


def max_pooling(_img: np.ndarray, _filter_shape: (int, ), _stride: (int, ) = None) -> np.ndarray:
    """
    最大池化\n
    :param _img: 图像
    :param _filter_shape: 池化大小
    :param _stride: 步长
    :return: 池化后的图像
    """
    if _stride is None:
        _stride = _filter_shape
    result = np.zeros((int((_img.shape[0] - _filter_shape[0]) / _stride[0] + 1), int((_img.shape[1] - _filter_shape[1]) / _stride[1] + 1)), dtype=float)
    for i, ii in enumerate(range(0, _img.shape[0], _stride[0])):
        for j, jj in enumerate(range(0, _img.shape[1], _stride[1])):
            result[i, j] = np.max(_img[ii:ii + _filter_shape[0], jj:jj + _filter_shape[1]])
    return result
