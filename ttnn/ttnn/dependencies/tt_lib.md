<a id="tt-lib"></a>

# TT-LIB

## Overview

The `tt_lib` Python module is a
unified Python interface to the Tensor library located within `tt_eager`. This library currently only supports 4 dimensional tensors with shape `[W, Z, Y, X]`, in ROW_MAJOR layout, and with BFLOAT16 data type.

Some OPs in this library might change layout of input tensors and pad them to better match expectations of execution kernels on TT Accelerator device.
These OPs will unpad the result tensor before it is returned to caller.

There is a limitation that tensor in ROW_MAJOR layout on TT Accelerator device must have the size of last dimension `X` be divisible by 2.
You can’t create these type of tensors on TT Accelerator device or send them to TT Accelerator device with ``tt_lib.tensor.Tensor.to()`.
However, you can supply these type of tensors to OPs from TT-LIB library as they can automatically pad the last dimension before moving the tensor
to TT Accelerator device. To use this functionality, you must call tt_lib.device.SetDefaultDevice(tt_device) to set your TT Accelerator device
as the default device that will be used to execute operations on tensors that are on host machine.

### Operation Infrastructure

TT-LIB has operation infrastructure which is used to launch, profile and cache operations generically.

To add a new operation that can plug in to the infrastructure, all that’s needed is a struct that implements methods needed by operation interface.
Below, is an example of how to declare a new on-device operation with all of the methods required by the interface.

#### New Device Operation

```cpp
struct <NewOperation> {
    void validate(const std::vector<Tensor> &input_tensors) const;
    std::vector<Shape> compute_output_shapes(const std::vector<Tensor> &input_tensors) const;
    std::vector<Tensor> create_output_tensors(const std::vector<Tensor> &input_tensors) const;
    operation::ProgramWithCallbacks create_program(const std::vector<Tensor>& input_tensors, std::vector<Tensor> &output_tensors) const;

    static constexpr auto attribute_names = std::forward_as_tuple();
    const auto attribute_values() const {
        return std::forward_as_tuple();
    }
};
```

#### New Device Operation with a member

```cpp
struct <NewOperation> {
    int some_member

    void validate(const std::vector<Tensor> &input_tensors) const;
    std::vector<Shape> compute_output_shapes(const std::vector<Tensor> &input_tensors) const;
    std::vector<Tensor> create_output_tensors(const std::vector<Tensor> &input_tensors) const;
    operation::ProgramWithCallbacks create_program(const std::vector<Tensor>& input_tensors, std::vector<Tensor> &output_tensors) const;

    static constexpr auto attribute_names = std::forward_as_tuple("some_member");
    const auto attribute_values() const {
        return std::forward_as_tuple(std::cref(some_member));
    }
};
```

#### New Device Operation with Optional Input Tensors

```cpp
struct <NewOperation> {
    void validate(const std::vector<Tensor> &input_tensors,
        const std::vector<std::optional<const Tensor>>& optional_input_tensors) const;
    std::vector<Shape> compute_output_shapes(const std::vector<Tensor> &input_tensors) const;
    std::vector<Tensor> create_output_tensors(const std::vector<Tensor> &input_tensors) const;
    operation::ProgramWithCallbacks create_program(
        const std::vector<Tensor>& input_tensors,
        const std::vector<std::optional<const Tensor>>& optional_input_tensors,
        std::vector<Tensor> &output_tensors) const;

    static constexpr auto attribute_names = std::forward_as_tuple();
    const auto attribute_values() const {
        return std::forward_as_tuple();
    }
};
```

#### New Device Operation with Optional Output Tensors

If an operation is expected to leverage optional output tensors, please use instead the validate_with_output_tensors
and create_output_tensors with the additional parameter for the output_tensors.

```cpp
struct <NewOperation> {
    void validate_with_output_tensors(const std::vector<Tensor> &input_tensors, const std::vector<std::optional<Tensor>>& output_tensors) const;
    std::vector<Shape> compute_output_shapes(const std::vector<Tensor> &input_tensors) const;
    std::vector<std::optional<Tensor>> create_output_tensors(const std::vector<Tensor> &input_tensors, const std::vector<std::optional<Tensor>>& output_tensors) const;
    operation::ProgramWithOptionalOutputTensors create_program(const std::vector<Tensor>& input_tensors, std::vector<std::optional<Tensor>> &output_tensors) const;

    static constexpr auto attribute_names = std::forward_as_tuple();
    const auto attribute_values() const {
        return std::forward_as_tuple();
    }
};
```

#### New Host Operation

And below, is an example of how to declare a new on-host operation with all of the methods required by the interface.

```default
struct <NewOperation> {
    void validate(const std::vector<Tensor> &input_tensors) const;
    std::vector<Shape> compute_output_shapes(const std::vector<Tensor> &input_tensors) const;
    std::vector<Tensor> compute_output_tensors(const std::vector<Tensor> &input_tensors) const;

    static constexpr auto attribute_names = std::forward_as_tuple();
    const auto attribute_values() const {
        return std::forward_as_tuple();
    }
};
```

### Profiler

Profiler is supported out of the box for any op.

And there are 2 special methods that can be optionally implemented to set the preferred_name and parallelization_strategy.

```default
// Implement `get_parallelization_strategy` to set the parallelization strategy on the profiler
struct <NewOperation> {
    <ParallelizationStrategyEnum> get_parallelization_strategy(const std::vector<Tensor> &input_tensors) const;
};
```

### Fast Dispatch

Fast dispatch allows programs/kernels to be enqueued to run, so host code does not have to wait for ops/programs to finish running.
The enqueued programs run asynchronously to the host code.
To wait for kernels to complete, either read a tensor from device to host with:

or to perform only a wait, use:

### Program Caching

Program caching provides an ability for an operation to cache the program and simply reload it the next time the same operation is used.

It can be enabled by running:

```default
tt::tt_metal::program_cache::enable()
```

And it can be disabled by running:

```default
tt::tt_metal::program_cache::disable_and_clear()
```

Number of entries can be queried using:

```default
tt::tt_metal::program_cache::num_entries()
```

In order for an op to be cachable, it needs to implement the following:

```default
struct <NewOperation> {
   // Mandatory methods

    // Return type of `create_program` needs to implement override_runtime_args_callback
    // i.e.:
    operation::ProgramWithCallbacks create_program(const std::vector<Tensor> &input_tensors) const {

        Program program{};

        // ...

        auto override_runtime_args_callback = [unary_reader_kernel_id, unary_writer_kernel_id](
            const Program &program,
            const std::vector<Buffer*>& input_buffers,
            const std::vector<Buffer*>& output_buffers
        ) {

            auto src_dram_buffer = input_buffers.at(0);
            auto dst_dram_buffer = output_buffers.at(0);

            CoreCoord core = {0, 0};

            {
                auto &runtime_args = GetRuntimeArgs(program, unary_reader_kernel_id, core);
                runtime_args[0] = src_dram_buffer->address();
            }

            {
                auto &runtime_args = GetRuntimeArgs(program, unary_writer_kernel_id, core);
                runtime_args[0] = dst_dram_buffer->address();
            }
        };

        return {std::move(program), override_runtime_args_callback};
    }
};
```

### Logs

To see logs related to operation infrastructure, use the following environment variables:

```default
export TT_METAL_LOGGER_TYPES=Op
export TT_METAL_LOGGER_LEVEL=Debug
```

The logs will print currently running op and information related to program caching. i.e.:

```default
Op | DEBUG    | Operation Type: silu (fallback operation)
Op | DEBUG    | Operation Attributes: ()
Op | DEBUG    | Input Tensors: {tt::tt_metal::Tensor(storage=tt::tt_metal::DeviceStorage(memory_config=tt::tt_metal::MemoryConfig(memory_layout=tt::tt_metal::TensorMemoryLayout::INTERLEAVED, buffer_type=tt::tt_metal::BufferType::DRAM)), shape={1, 1, 1, 1280}, dtype=tt::tt_metal::DataType::BFLOAT16, layout=tt::tt_metal::Layout::ROW_MAJOR)}
Op | DEBUG    | Operation Type: tt::tt_metal::LayoutConversionOnHost
Op | DEBUG    | Operation Attributes: (target_layout=tt::tt_metal::Layout::TILE)
Op | DEBUG    | Input Tensors: {tt::tt_metal::Tensor(storage=tt::tt_metal::OwnedStorage(), shape={1, 1, 320, 1280}, dtype=tt::tt_metal::DataType::BFLOAT16, layout=tt::tt_metal::Layout::ROW_MAJOR)}
...
Op | DEBUG    | Program Cache: MISS - Compiling new program "tt::tt_metal::EltwiseUnary(op_type=tt::tt_metal::UnaryOpType::Enum::GELU, param=1)_tt::tt_metal::Tensor(storage=tt::tt_metal::DeviceStorage(memory_config=tt::tt_metal::MemoryConfig(memory_layout=tt::tt_metal::TensorMemoryLayout::INTERLEAVED, buffer_type=tt::tt_metal::BufferType::DRAM)), shape={1, 1, 32, 32}, dtype=tt::tt_metal::DataType::BFLOAT16, layout=tt::tt_metal::Layout::TILE)"
Op | DEBUG    | Operation Name: tt::tt_metal::EltwiseUnary
Op | DEBUG    | Operation Attributes: (op_type=tt::tt_metal::UnaryOpType::Enum::GELU, param=0)
Op | DEBUG    | Input Tensors: {tt::tt_metal::Tensor(storage=tt::tt_metal::DeviceStorage(memory_config=tt::tt_metal::MemoryConfig(memory_layout=tt::tt_metal::TensorMemoryLayout::INTERLEAVED, buffer_type=tt::tt_metal::BufferType::DRAM)), shape={1, 1, 32, 32}, dtype=tt::tt_metal::DataType::BFLOAT16, layout=tt::tt_metal::Layout::TILE)}
```

If OPERATION_HISTORY_CSV=<csv_file_path> environment variable is set, then the history of all executed operations will be dumped into <csv_file_path>

## TT-LIB API through `tt_lib`

### Primary Operations

autofunction:: tt_lib.operations.primary.matmul

### Enums

### Tensor elementwise operations

### Tensor relational operations

### Tensor ternary operations

### Tensor matrix math operations

Tensor manipulation operations
-=============================

These operations change the tensor shape in some way, giving it new dimensions
but in general retaining the data.

### Tensor creation operations

### Broadcast and Reduce

## Fallback Operations

These operations are currently not supported on TT accelerator device and will execute on host machine using Pytorch.

## Experimental Operations

Operations in this section are experimental, don’t have full support, and may behave in unexpected ways.

### Fused Operations from `tt_lib` Mini-Graph Library

We have a variety of common operations that require fusion of multiple
base operations together.

### Complex Operations

> We use the following Tensor representation for complex tensors on device; we support complex tensor **x** as  N,H,W,C rank-4 tensor with last dim of size divisible by 64 to represent real and imaginary components
> : * with indices [:,:,:,0:N/2] being real, and
>   * with indices [:,:,:,N/2:N] being imaginary.

The following functions are available,

Complex arithmetic can be carried out for multiply, divide, add and subtract as follows:

and then unary operations for,

### Complex Operations (Type 2)

Type 2 Complex representation allows for more flexible storage than earlier one while providing same set of
operations; specifically this storage allows for compute without the cost of split-concat implicit in
the Type 1 contiguous representations.

### Other Operations

### Backward Operations

### Loss Functions
