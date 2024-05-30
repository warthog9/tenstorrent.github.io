# CircularBuffers

```cpp
CBHandle tt::tt_metal::CreateCircularBuffer(Program &program, const std::variant<CoreCoord, CoreRange, CoreRangeSet> &core_spec, const CircularBufferConfig &config)
```

Creates a Circular Buffer (CB) in L1 memory of all cores within core ranges (inclusive) and adds it to the program. There can be a total of NUM_CIRCULAR_BUFFERS (32) circular buffers per core. Circular buffers hold data and have an associated config which indicates usage of the address space. If the config is specified for multiple buffer indices, the circular buffer address space is shared and each buffer index can potentially have a unique view of the shared space.

Circular buffers can be dynamically allocated or program-local allocated. If the config is created with an L1 buffer or sets a globally allocated address it is dynamic and shares the same address space as the L1 buffer. Otherwise, the circular buffer address space is managed by the program. Address space for program-local circular buffers does not persist across programs.

Return value: Circular Buffer ID (uintptr_t)

| Argument      | Description                                                                                                                                       | Type                                                     | Valid Range      | Required       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------------|----------------|
| program       | The program to which buffer will be added to                                                                                                      | Program &                                                |                  | Yes            |
| core_spec     | Either a single logical core, a range of logical cores or a set of logical core ranges that indicate where the circular buffer will be configured | const std::variant<CoreCoord, CoreRange, CoreRangeSet> & |                  | Yes            |
| config        | Config for circular buffer                                                                                                                        | const CircularBufferConfig &                             |                  | Yes            |

```cpp
const CircularBufferConfig &tt::tt_metal::GetCircularBufferConfig(Program &program, CBHandle cb_handle)
```

Gets a reference to the config owned by circular buffer at the given circular buffer ID.

Return value: const CircularBufferConfig &

| Argument      | Description                                                    | Type                 | Valid Range      | Required       |
|---------------|----------------------------------------------------------------|----------------------|------------------|----------------|
| program       | The program containing the circular buffer                     | Program &            |                  | Yes            |
| cb_handle     | ID of the circular buffer, returned by `CreateCircularBuffers` | CBHandle (uintptr_t) |                  | Yes            |

```cpp
void tt::tt_metal::UpdateCircularBufferTotalSize(Program &program, CBHandle cb_handle, uint32_t total_size)
```

Update the total size of the circular buffer at the given circular buffer handle. Updating a program-local circular buffer requires all circular buffers in the program to be reallocated.

Return value: void

| Argument      | Description                                | Type      | Valid Range      | Required       |
|---------------|--------------------------------------------|-----------|------------------|----------------|
| program       | The program containing the circular buffer | Program & |                  | Yes            |

| cb_handle | ID of the circular buffer, returned by `CreateCircularBuffers` | CBHandle (uintptr_t) | | Yes | | | total_size | New size of the circular buffer in bytes | uint32_t | | Yes | 

```cpp
void tt::tt_metal::UpdateCircularBufferPageSize(Program &program, CBHandle cb_handle, uint8_t buffer_index, uint32_t page_size)
```

Update the page size at specified `buffer_index` of the circular buffer at the given circular buffer handle.

Return value: void

| Argument      | Description                                                                                                                | Type                 | Valid Range                   | Required       |
|---------------|----------------------------------------------------------------------------------------------------------------------------|----------------------|-------------------------------|----------------|
| program       | The program containing the circular buffer                                                                                 | Program &            |                               | Yes            |
| cb_handle     | ID of the circular buffer, returned by `CreateCircularBuffers`                                                             | CBHandle (uintptr_t) |                               | Yes            |
| buffer_index  | Circular buffer index to update page size. `cb_handle` must be a circular buffer that had previously programmed this index | uint8_t              | 0 to NUM_CIRCULAR_BUFFERS - 1 | Yes            |
| page_size     | Updated page size in bytes                                                                                                 | uint32_t             |                               | Yes            |

```cpp
void tt::tt_metal::UpdateDynamicCircularBufferAddress(Program &program, CBHandle cb_handle, const Buffer &buffer)
```

Update the address of a dynamic circular buffer. Dynamic circular buffers share the same address space as L1 buffers.

Return value: void

| Argument      | Description                                | Type      | Valid Range      | Required       |
|---------------|--------------------------------------------|-----------|------------------|----------------|
| program       | The program containing the circular buffer | Program & |                  | Yes            |

| cb_handle | ID of the circular buffer, returned by `CreateCircularBuffers` | CBHandle (uintptr_t) | | Yes | | | buffer | Dynamically allocated L1 buffer that shares address space of circular buffer `cb_handle` | const Buffer & | L1 buffer | Yes |
