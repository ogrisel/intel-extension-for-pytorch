// Autogenerated file by gen-gpu-ops.py. Do not edit directly!

#include <ATen/Tensor.h>

namespace at {

class AtenIpexTypeDefault {
 public:
  static at::Tensor as_strided(const at::Tensor & self, at::IntArrayRef size, at::IntArrayRef stride, c10::optional<int64_t> storage_offset);
  static at::Tensor bitwise_not(const at::Tensor & self);
  static at::Tensor & bitwise_not_(at::Tensor & self);
  static at::Tensor & bitwise_not_out(at::Tensor & out, const at::Tensor & self);
  static at::Tensor logical_not(const at::Tensor & self);
  static at::Tensor & logical_not_(at::Tensor & self);
  static at::Tensor & logical_not_out(at::Tensor & out, const at::Tensor & self);
  static at::Tensor convolution_overrideable(const at::Tensor & input, const at::Tensor & weight, const at::Tensor & bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups);
  static at::Tensor & copy_(at::Tensor & self, const at::Tensor & src, bool non_blocking);
  static at::Tensor empty(at::IntArrayRef size, const at::TensorOptions & options, c10::optional<at::MemoryFormat> memory_format);
  static at::Tensor & resize_(at::Tensor & self, at::IntArrayRef size, c10::optional<at::MemoryFormat> memory_format);
  static at::Tensor & fill_(at::Tensor & self, at::Scalar value);
  static at::Tensor & fill_(at::Tensor & self, const at::Tensor & value);
  static std::tuple<at::Tensor,at::Tensor,at::Tensor> native_batch_norm(const at::Tensor & input, const at::Tensor & weight, const at::Tensor & bias, const at::Tensor & running_mean, const at::Tensor & running_var, bool training, double momentum, double eps);
  static at::Tensor neg(const at::Tensor & self);
  static at::Tensor & neg_(at::Tensor & self);
  static at::Tensor & neg_out(at::Tensor & out, const at::Tensor & self);
  static at::Tensor threshold(const at::Tensor & self, at::Scalar threshold, at::Scalar value);
  static at::Tensor & threshold_(at::Tensor & self, at::Scalar threshold, at::Scalar value);
  static at::Tensor & threshold_out(at::Tensor & out, const at::Tensor & self, at::Scalar threshold, at::Scalar value);
  static at::Tensor & resize_as_(at::Tensor & self, const at::Tensor & the_template, c10::optional<at::MemoryFormat> memory_format);
  static at::Tensor addmm(const at::Tensor & self, const at::Tensor & mat1, const at::Tensor & mat2, at::Scalar beta, at::Scalar alpha);

};

void RegisterAtenTypeFunctions();

}  // namespace at

