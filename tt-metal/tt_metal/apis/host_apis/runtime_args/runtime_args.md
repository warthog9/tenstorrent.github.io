# Runtime Arguments

### void tt::tt_metal::SetRuntimeArgs(const Program &program, KernelHandle kernel, const std::variant<CoreCoord, CoreRange, CoreRangeSet> &core_spec, const std::vector<uint32_t> &runtime_args)

Set runtime args for a kernel that are sent to the core during runtime. This API needs to be called to update the runtime args for the kernel. Maximum of 255 allowed runtime args per core (unique and common runtime args count toward same limit).

Return value: void

| Argument      | Description                                                       | Type                                                   | Valid Range                                                         | Required       |
|---------------|-------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------|----------------|
| program       | The program containing kernels, circular buffers, semaphores      | const Program &                                        |                                                                     | Yes            |
| kernel_id     | ID of the kernel that will receive the runtime args               | KernelHandle (uint64_t)                                |                                                                     | Yes            |
| core_spec     | Location of Tensix core(s) where the runtime args will be written | const std::variant<CoreCoord,CoreRange,CoreRangeSet> & | Any logical Tensix core coordinate(s) on which the kernel is placed | Yes            |
| runtime_args  | The runtime args to be written                                    | const std::vector<uint32_t> &                          |                                                                     | Yes            |

### void tt::tt_metal::SetRuntimeArgs(const Program &program, KernelHandle kernel, const std::vector<CoreCoord> &core_spec, const std::vector<std::vector<uint32_t>> &runtime_args)

Set multiple runtime arguments of a kernel at once during runtime, each mapping to a specific core. The runtime args for each core may be unique. Maximum of 255 allowed runtime args per core (unique and common runtime args count toward same limit).

Return value: void

| Argument      | Description                                                       | Type                                    | Valid Range                                                              | Required       |
|---------------|-------------------------------------------------------------------|-----------------------------------------|--------------------------------------------------------------------------|----------------|
| program       | The program containing kernels, circular buffers, semaphores      | const Program &                         |                                                                          | Yes            |
| kernel_id     | ID of the kernel that will receive the runtime args               | KernelHandle (uint64_t)                 |                                                                          | Yes            |
| core_spec     | Location of Tensix core(s) where the runtime args will be written | const std::vector<CoreCoord> &          | Any set of logical Tensix core coordinates on which the kernel is placed | Yes            |
| runtime_args  | The runtime args to be written                                    | const std::vector< vector<uint32_t> > & | Outer vector size must be equal to size of core_spec vector              | Yes            |

### void tt::tt_metal::SetRuntimeArgs(Device *device, const std::shared_ptr<Kernel> kernel, const std::variant<CoreCoord, CoreRange, CoreRangeSet> &core_spec, std::shared_ptr<RuntimeArgs> runtime_args)

Set runtime args for a kernel that are sent to the specified cores using the command queue. This API must be used when Asynchronous Command Queue Mode is enabled. Maximum of 255 allowed runtime args per core (unique and common runtime args count toward same limit).

Return value: void

| Argument      | Description                                                       | Type                                                   | Valid Range                                                              | Required       |
|---------------|-------------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------|----------------|
| device        | The device that runtime args are being written to.                | Device\*                                               |                                                                          | Yes            |
| kernel        | The kernel that will recieve these runtime args.                  | std::shared_ptr<Kernel>                                |                                                                          | Yes            |
| core_spec     | Location of Tensix core(s) where the runtime args will be written | const std::variant<CoreCoord,CoreRange,CoreRangeSet> & | Any set of logical Tensix core coordinates on which the kernel is placed | Yes            |
| runtime_args  | The runtime args to be written                                    | std::shared_ptr<RuntimeArgs>                           |                                                                          | Yes            |

### void tt::tt_metal::SetRuntimeArgs(Device *device, const std::shared_ptr<Kernel> kernel, const std::vector<CoreCoord> &core_spec, const std::vector<std::shared_ptr<RuntimeArgs>> runtime_args)

Set multiple runtime arguments of a kernel using the command queue. Each core can have distinct arguments. This API must be used when Asynchronous Command Queue Mode is enabled. Maximum of 255 allowed runtime args per core (unique and common runtime args count toward same limit).

Return value: void 

| Argument      | Description                                                       | Type                                            | Valid Range                                                              | Required       |
|---------------|-------------------------------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------|----------------|
| device        | The device that runtime args are being written to.                | Device\*                                        |                                                                          | Yes            |
| kernel        | The kernel that will recieve these runtime args.                  | std::shared_ptr<Kernel>                         |                                                                          | Yes            |
| core_spec     | Location of Tensix core(s) where the runtime args will be written | const std::vector< CoreCoord > &                | Any set of logical Tensix core coordinates on which the kernel is placed | Yes            |
| runtime_args  | The runtime args to be written                                    | const std::vector<std::shared_ptr<RuntimeArgs>> | Outer vector size must be equal to size of core_spec vector              | Yes            |

### RuntimeArgsData &tt::tt_metal::GetRuntimeArgs(const Program &program, KernelHandle kernel_id, const CoreCoord &logical_core)

Get the runtime args for a kernel.

Return value: uint32_t \*

| Argument      | Description                                                            | Type                    | Valid Range                        | Required       |
|---------------|------------------------------------------------------------------------|-------------------------|------------------------------------|----------------|
| program       | The program containing kernels, circular buffers, semaphores           | const Program &         |                                    | Yes            |
| kernel_id     | ID of the kernel that will receive the runtime args                    | KernelHandle (uint64_t) |                                    | Yes            |
| logical_core  | The location of the Tensix core where the runtime args will be written | const CoreCoord &       | Any logical Tensix core coordinate | Yes            |

### std::vector<std::vector<RuntimeArgsData>> &tt::tt_metal::GetRuntimeArgs(const Program &program, KernelHandle kernel_id)

Get the runtime args for a kernel.

Return value: std::vector< std::vector< RuntimeArgsData > > &

| Argument      | Description                                                  | Type                    | Valid Range      | Required       |
|---------------|--------------------------------------------------------------|-------------------------|------------------|----------------|
| program       | The program containing kernels, circular buffers, semaphores | const Program &         |                  | Yes            |
| kernel_id     | ID of the kernel that will receive the runtime args          | KernelHandle (uint64_t) |                  | Yes            |

### void tt::tt_metal::SetCommonRuntimeArgs(const Program &program, KernelHandle kernel_id, const std::vector<uint32_t> &runtime_args)

Set common (shared by all cores) runtime args for a kernel that are sent to all cores during runtime. This API needs to be called to update the common runtime args for the kernel. Maximum of 255 allowed runtime args per core (unique and common runtime args count toward same limit).

Return value: void

| Argument      | Description                                                  | Type                          | Valid Range      | Required       |
|---------------|--------------------------------------------------------------|-------------------------------|------------------|----------------|
| program       | The program containing kernels, circular buffers, semaphores | const Program &               |                  | Yes            |
| kernel_id     | ID of the kernel that will receive the runtime args          | KernelHandle (uint64_t)       |                  | Yes            |
| runtime_args  | The runtime args to be written                               | const std::vector<uint32_t> & |                  | Yes            |

### RuntimeArgsData &tt::tt_metal::GetCommonRuntimeArgs(const Program &program, KernelHandle kernel_id)

Get the common runtime args for a kernel. Note that you must call SetCommonRuntimeArgs after updating the returned value to propagate the update.

Return value: RuntimeArgsData &

| Argument      | Description                                                  | Type                    | Valid Range      | Required       |
|---------------|--------------------------------------------------------------|-------------------------|------------------|----------------|
| program       | The program containing kernels, circular buffers, semaphores | const Program &         |                  | Yes            |
| kernel_id     | ID of the kernel that will receive the runtime args          | KernelHandle (uint64_t) |                  | Yes            |
