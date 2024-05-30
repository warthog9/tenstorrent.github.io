# APIs

## Device

* [ttnn.open_device](ttnn/open_device.md)
* [ttnn.close_device](ttnn/close_device.md)
* [ttnn.manage_device](ttnn/manage_device.md)
* [ttnn.synchronize_device](ttnn/synchronize_device.md)

## Memory Config

* [ttnn.create_sharded_memory_config](ttnn/create_sharded_memory_config.md)

## Operations

### Core

* [ttnn.as_tensor](ttnn/as_tensor.md)
* [ttnn.from_torch](ttnn/from_torch.md)
* [ttnn.to_torch](ttnn/to_torch.md)
* [ttnn.to_device](ttnn/to_device.md)
* [ttnn.from_device](ttnn/from_device.md)
* [ttnn.to_layout](ttnn/to_layout.md)
* [ttnn.dump_tensor](ttnn/dump_tensor.md)
* [ttnn.load_tensor](ttnn/load_tensor.md)
* [ttnn.deallocate](ttnn/deallocate.md)
* [ttnn.reallocate](ttnn/reallocate.md)
* [ttnn.to_memory_config](ttnn/to_memory_config.md)

### Tensor Creation

* [ttnn.arange](ttnn/arange.md)
* [ttnn.empty](ttnn/empty.md)
* [ttnn.zeros](ttnn/zeros.md)
* [ttnn.zeros_like](ttnn/zeros_like.md)
* [ttnn.ones](ttnn/ones.md)
* [ttnn.ones_like](ttnn/ones_like.md)
* [ttnn.full](ttnn/full.md)
* [ttnn.full_like](ttnn/full_like.md)

### Matrix Multiplication

* [ttnn.matmul](ttnn/matmul.md)
* [ttnn.linear](ttnn/linear.md)

### Pointwise Unary

* [ttnn.abs](ttnn/abs.md)
* [ttnn.acos](ttnn/acos.md)
* [ttnn.acosh](ttnn/acosh.md)
* [ttnn.asin](ttnn/asin.md)
* [ttnn.asinh](ttnn/asinh.md)
* [ttnn.atan](ttnn/atan.md)
* [ttnn.atan2](ttnn/atan2.md)
* [ttnn.atanh](ttnn/atanh.md)
* [ttnn.cbrt](ttnn/cbrt.md)
* [ttnn.celu](ttnn/celu.md)
* [ttnn.clip](ttnn/clip.md)
* [ttnn.clone](ttnn/clone.md)
* [ttnn.cos](ttnn/cos.md)
* [ttnn.cosh](ttnn/cosh.md)
* [ttnn.deg2rad](ttnn/deg2rad.md)
* [ttnn.digamma](ttnn/digamma.md)
* [ttnn.elu](ttnn/elu.md)
* [ttnn.erf](ttnn/erf.md)
* [ttnn.erfc](ttnn/erfc.md)
* [ttnn.erfinv](ttnn/erfinv.md)
* [ttnn.exp](ttnn/exp.md)
* [ttnn.exp2](ttnn/exp2.md)
* [ttnn.expm1](ttnn/expm1.md)
* [ttnn.geglu](ttnn/geglu.md)
* [ttnn.gelu](ttnn/gelu.md)
* [ttnn.glu](ttnn/glu.md)
* [ttnn.hardshrink](ttnn/hardshrink.md)
* [ttnn.hardsigmoid](ttnn/hardsigmoid.md)
* [ttnn.hardswish](ttnn/hardswish.md)
* [ttnn.hardtanh](ttnn/hardtanh.md)
* [ttnn.heaviside](ttnn/heaviside.md)
* [ttnn.hypot](ttnn/hypot.md)
* [ttnn.i0](ttnn/i0.md)
* [ttnn.isfinite](ttnn/isfinite.md)
* [ttnn.isinf](ttnn/isinf.md)
* [ttnn.isnan](ttnn/isnan.md)
* [ttnn.isneginf](ttnn/isneginf.md)
* [ttnn.isposinf](ttnn/isposinf.md)
* [ttnn.leaky_relu](ttnn/leaky_relu.md)
* [ttnn.lerp](ttnn/lerp.md)
* [ttnn.lgamma](ttnn/lgamma.md)
* [ttnn.log](ttnn/log.md)
* [ttnn.log10](ttnn/log10.md)
* [ttnn.log1p](ttnn/log1p.md)
* [ttnn.log2](ttnn/log2.md)
* [ttnn.log_sigmoid](ttnn/log_sigmoid.md)
* [ttnn.logical_not](ttnn/logical_not.md)
* [ttnn.logit](ttnn/logit.md)
* [ttnn.mish](ttnn/mish.md)
* [ttnn.multigammaln](ttnn/multigammaln.md)
* [ttnn.neg](ttnn/neg.md)
* [ttnn.prelu](ttnn/prelu.md)
* [ttnn.reglu](ttnn/reglu.md)
* [ttnn.relu](ttnn/relu.md)
* [ttnn.relu6](ttnn/relu6.md)
* [ttnn.rsqrt](ttnn/rsqrt.md)
* [ttnn.sigmoid](ttnn/sigmoid.md)
* [ttnn.sigmoid_accurate](ttnn/sigmoid_accurate.md)
* [ttnn.sign](ttnn/sign.md)
* [ttnn.silu](ttnn/silu.md)
* [ttnn.sin](ttnn/sin.md)
* [ttnn.sinh](ttnn/sinh.md)
* [ttnn.softmax](ttnn/softmax.md)
* [ttnn.softplus](ttnn/softplus.md)
* [ttnn.softshrink](ttnn/softshrink.md)
* [ttnn.softsign](ttnn/softsign.md)
* [ttnn.swish](ttnn/swish.md)
* [ttnn.tan](ttnn/tan.md)
* [ttnn.tanh](ttnn/tanh.md)
* [ttnn.signbit](ttnn/signbit.md)
* [ttnn.polygamma](ttnn/polygamma.md)
* [ttnn.rad2deg](ttnn/rad2deg.md)
* [ttnn.reciprocal](ttnn/reciprocal.md)
* [ttnn.sqrt](ttnn/sqrt.md)
* [ttnn.square](ttnn/square.md)
* [ttnn.swiglu](ttnn/swiglu.md)
* [ttnn.tril](ttnn/tril.md)
* [ttnn.triu](ttnn/triu.md)
* [ttnn.tanhshrink](ttnn/tanhshrink.md)
* [ttnn.threshold](ttnn/threshold.md)

### Pointwise Binary

* [ttnn.add](ttnn/add.md)
* [ttnn.multiply](ttnn/multiply.md)
* [ttnn.subtract](ttnn/subtract.md)
* [ttnn.pow](ttnn/pow.md)
* [ttnn.ldexp](ttnn/ldexp.md)
* [ttnn.logical_and](ttnn/logical_and.md)
* [ttnn.logical_or](ttnn/logical_or.md)
* [ttnn.logical_xor](ttnn/logical_xor.md)
* [ttnn.logaddexp](ttnn/logaddexp.md)
* [ttnn.logaddexp2](ttnn/logaddexp2.md)
* [ttnn.xlogy](ttnn/xlogy.md)
* [ttnn.squared_difference](ttnn/squared_difference.md)
* [ttnn.gtz](ttnn/gtz.md)
* [ttnn.ltz](ttnn/ltz.md)
* [ttnn.gez](ttnn/gez.md)
* [ttnn.lez](ttnn/lez.md)
* [ttnn.nez](ttnn/nez.md)
* [ttnn.eqz](ttnn/eqz.md)
* [ttnn.gt](ttnn/gt.md)
* [ttnn.ge](ttnn/ge.md)
* [ttnn.lt](ttnn/lt.md)
* [ttnn.le](ttnn/le.md)
* [ttnn.eq](ttnn/eq.md)
* [ttnn.ne](ttnn/ne.md)
* [ttnn.isclose](ttnn/isclose.md)
* [ttnn.polyval](ttnn/polyval.md)
* [ttnn.nextafter](ttnn/nextafter.md)
* [ttnn.maximum](ttnn/maximum.md)
* [ttnn.minimum](ttnn/minimum.md)

### Pointwise Ternary

* [ttnn.addcdiv](ttnn/addcdiv.md)
* [ttnn.addcmul](ttnn/addcmul.md)
* [ttnn.mac](ttnn/mac.md)
* [ttnn.where](ttnn/where.md)

### Losses

* [ttnn.l1_loss](ttnn/l1_loss.md)
* [ttnn.mse_loss](ttnn/mse_loss.md)

### Reduction

* [ttnn.max](ttnn/max.md)
* [ttnn.mean](ttnn/mean.md)
* [ttnn.min](ttnn/min.md)
* [ttnn.std](ttnn/std.md)
* [ttnn.sum](ttnn/sum.md)
* [ttnn.var](ttnn/var.md)

### Data Movement

* [ttnn.concat](ttnn/concat.md)
* [ttnn.pad](ttnn/pad.md)
* [ttnn.permute](ttnn/permute.md)
* [ttnn.reshape](ttnn/reshape.md)
* [ttnn.split](ttnn/split.md)
* [ttnn.repeat](ttnn/repeat.md)
* [ttnn.repeat_interleave](ttnn/repeat_interleave.md)

### Normalization

* [ttnn.group_norm](ttnn/group_norm.md)
* [ttnn.layer_norm](ttnn/layer_norm.md)
* [ttnn.rms_norm](ttnn/rms_norm.md)

### Transformer

* [ttnn.transformer.split_query_key_value_and_split_heads](ttnn/transformer/split_query_key_value_and_split_heads.md)
* [ttnn.transformer.concatenate_heads](ttnn/transformer/concatenate_heads.md)
* [ttnn.transformer.attention_softmax](ttnn/transformer/attention_softmax.md)
* [ttnn.transformer.attention_softmax_](ttnn/transformer/attention_softmax_.md)
* [ttnn.transformer.rotary_embedding](ttnn/transformer/rotary_embedding.md)

### Embedding

* [ttnn.embedding](ttnn/embedding.md)

### Pooling

* [ttnn.global_avg_pool2d](ttnn/global_avg_pool2d.md)
* [ttnn.MaxPool2d](ttnn/MaxPool2d.md)

### Vision

* [ttnn.upsample](ttnn/upsample.md)

### KV Cache

* [ttnn.kv_cache.fill_cache_for_user_](ttnn/kv_cache/fill_cache_for_user_.md)
* [ttnn.kv_cache.update_cache_for_token_](ttnn/kv_cache/update_cache_for_token_.md)

## Model Conversion

* [ttnn.model_preprocessing.preprocess_model](ttnn/model_preprocessing/preprocess_model.md)
* [ttnn.model_preprocessing.preprocess_model_parameters](ttnn/model_preprocessing/preprocess_model_parameters.md)

## Reports

* [ttnn.set_printoptions](ttnn/set_printoptions.md)

## Operation Hooks

* [ttnn.register_pre_operation_hook](ttnn/register_pre_operation_hook.md)
* [ttnn.register_post_operation_hook](ttnn/register_post_operation_hook.md)
