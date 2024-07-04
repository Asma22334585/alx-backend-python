#!/usr/bin/env python3
'''Variable Annotations'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns their sum as a float.'''
    return float(sum(mxd_lst))
