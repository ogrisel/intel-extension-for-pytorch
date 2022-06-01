import torch
import intel_extension_for_pytorch

from torch.overrides import (
    handle_torch_function,
    has_torch_function,
    get_overridable_functions,
    get_testing_overrides,
    is_tensor_method_or_property,
    TorchFunctionMode
)
import functools
from functools import partial

# The dispatch table for tensor factory's __torch_function__ implementation.
HANDLED_FUNCTIONS_SUB = {}

DEFAULT_XPU_DEVICE = "xpu"
DEFAULT_DTYPE = torch.float

def implements_sub(torch_function):
    "Register a torch function override for SubTensor"
    HANDLED_FUNCTIONS_SUB[torch_function] = partial(torch_function, device=DEFAULT_XPU_DEVICE, dtype=DEFAULT_DTYPE)

implements_sub(torch.empty)

def set_default_tensor_type(tensor_type):
    class XPUDefaultTensorTypeMode(TorchFunctionMode):

        def __init__(self, tensor_type):
            if tensor_type is torch.xpu.FloatTensor:
                self.dtype = torch.float
            if tensor_type is torch.xpu.DoubleTensor:
                self.dtype = torch.float64

        def __torch_function__(self, func, types, args=(), kwargs=None):
            if kwargs is None:
                kwargs = {}

            print("johnlu function:", func)
            if func in HANDLED_FUNCTIONS_SUB:
                return partial(func, device="xpu", dtype=self.dtype)(*args, **kwargs)

            return func(*args, **kwargs)



    if tensor_type in [torch.xpu.FloatTensor, torch.xpu.DoubleTensor]:
        mode_info = torch.overrides._TorchFunctionModeInfo()

        old = mode_info.get_mode()
        if old is None:
            inner = mode_info.base_mode_class(inner=None)
        else:
            inner = old

        mode = partial(XPUDefaultTensorTypeMode, tensor_type)(inner=inner)
        mode_info.set_mode(mode)