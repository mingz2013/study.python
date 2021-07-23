# -*- coding: utf-8 -*-
"""
@FileName: test_dataclass
@Time: 2021/2/17 12:51
@Author: zhaojm

Module Description

"""

# from dataclasses import dataclass
import dataclasses


# dataclasses.Field
# dataclasses.field(
#
# )
# dataclasses.dataclass(
#
# )
#
# dataclasses.is_dataclass(
#
# )
# dataclasses.

@dataclasses.dataclass
class A:
    a: str = dataclasses.field(init=True, default=1)


print(A())
