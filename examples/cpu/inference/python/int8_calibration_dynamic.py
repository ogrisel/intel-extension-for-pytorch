import os
import torch
#################### code changes ####################
import intel_extension_for_pytorch as ipex
from intel_extension_for_pytorch.quantization import prepare, convert
######################################################

##### Example Model #####
from transformers import BertModel

model = BertModel.from_pretrained("bert-base-uncased")
model.eval()

vocab_size = model.config.vocab_size
batch_size = 1
seq_length = 512
data = torch.randint(vocab_size, size=[batch_size, seq_length])
#########################

qconfig = ipex.quantization.default_dynamic_qconfig
# Alternatively, define your own qconfig:
# from torch.ao.quantization import PerChannelMinMaxObserver, PlaceholderObserver, QConfig
# qconfig = QConfig(
#        activation = PlaceholderObserver.with_args(dtype=torch.float, compute_dtype=torch.quint8),
#        weight = PerChannelMinMaxObserver.with_args(dtype=torch.qint8, qscheme=torch.per_channel_symmetric))
prepared_model = prepare(model, qconfig, example_inputs=data)

converted_model = convert(prepared_model)
with torch.no_grad():
  traced_model = torch.jit.trace(converted_model, (data,), check_trace=False, strict=False)
  traced_model = torch.jit.freeze(traced_model)

traced_model.save("quantized_model.pt")