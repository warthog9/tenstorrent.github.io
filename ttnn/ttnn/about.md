# What is ttnn?

[ttnn]() is a library that provides a user-friendly interface to operations that run on TensTorrent’s hardware using `tt-metal` programming model.

[ttnn]() is designed to be intuitive to an user that is familiar with [PyTorch](https://pytorch.org/).

[ttnn]()’s primary dependency is [tt_lib](dependencies/tt_lib.md) which provides the implementation for all of the operations used by [ttnn]().

We trust that this library will be valuable to helping you on your journey to take full advantage of our devices!

## Key features of [ttnn]()

Key features of [ttnn]():
: * Support for N-D tensors.
  * Intuitive way of converting between [ttnn.ROW_MAJOR_LAYOUT](tensor.md#ttnn-row-major-layout) and [ttnn.TILE_LAYOUT](tensor.md#ttnn-tile-layout) using [ttnn.to_layout](ttnn/to_layout.md#ttnn-to-layout)
  * Stable APIs.
  * The computation graph of [ttnn]() operations can be traced and then visualized or used in any other way. The graph is networkx compatible. Refer to [ttnn Tracer](tutorials/ttnn-tracer.md#ttnn-tracer) for examples
  * Infrastructure for converting parameters and some sub-modules from a torch.nn.Module object. This infrastructure supports caching of the converted parameters which could significantly speed up repeated runs.
  * Ability to compare the result of each operation to the equivalent [PyTorch](https://pytorch.org/) operation. Very useful for debugging.
