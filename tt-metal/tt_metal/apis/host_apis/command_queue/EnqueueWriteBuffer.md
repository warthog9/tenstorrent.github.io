# EnqueueWriteBuffer

### void tt::tt_metal::EnqueueWriteBuffer(CommandQueue &cq, std::variant<std::reference_wrapper<Buffer>, std::shared_ptr<Buffer>> buffer, std::vector<uint32_t> &src, bool blocking)

Writes a buffer to the device

Return value: void

| Argument      | Description                                                           | Type                                | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------------|-------------------------------------|------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue &                      |                  | Yes            |
| buffer        | The device buffer we are writing to                                   | Buffer & or std::shared_ptr<Buffer> |                  | Yes            |
| src           | The vector we are writing to the device                               | vector<uint32_t> &                  |                  | Yes            |
| blocking      | Whether or not this is a blocking operation                           | bool                                |                  | Yes            |

### void tt::tt_metal::EnqueueWriteBuffer(CommandQueue &cq, std::variant<std::reference_wrapper<Buffer>, std::shared_ptr<Buffer>> buffer, HostDataType src, bool blocking)

Writes a buffer to the device

Return value: void

| Argument      | Description                                                           | Type                                | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------------|-------------------------------------|------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue &                      |                  | Yes            |
| buffer        | The device buffer we are writing to                                   | Buffer & or std::shared_ptr<Buffer> |                  | Yes            |
| src           | The memory we are writing to the device                               | HostDataType                        |                  | Yes            |
| blocking      | Whether or not this is a blocking operation                           | bool                                |                  | Yes            |
