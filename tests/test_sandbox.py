import pytest
import os
import argparse
import torch
import torch.nn as nn


def test_argparse():
    # https://docs.python.org/ja/3/library/argparse.html
    # https://note.nkmk.me/python-argparse-bool/
    # > add_argument()の引数typeにboolを指定してはいけない
    parser = argparse.ArgumentParser()
    parser.add_argument('--use_gpu', type=bool, default=True)
    args = parser.parse_args(['--use_gpu', '1'])
    assert args.use_gpu == True
    args = parser.parse_args(['--use_gpu', '0'])
    assert args.use_gpu == True
    args = parser.parse_args(['--use_gpu', ''])
    assert args.use_gpu == False

    # > 引数typeではなく引数actionを使う
    parser = argparse.ArgumentParser()
    parser.add_argument('--use_cpu', action='store_true')
    args = parser.parse_args([])
    assert args.use_cpu == False
    args = parser.parse_args(['--use_cpu'])
    assert args.use_cpu == True


@pytest.mark.skipif('SKIP_SLOW_TESTS' in os.environ, reason='SLOW')
def test_linear():
    model = nn.Linear(4, 3)
    model.to('cuda')
    input_ = torch.tensor([
        [1., 1., 1., 1.],
        [2., 2. ,2., 2.],
    ]).to('cuda')
    output_ = model(input_)
    assert tuple(output_.size()) == (2, 3)
