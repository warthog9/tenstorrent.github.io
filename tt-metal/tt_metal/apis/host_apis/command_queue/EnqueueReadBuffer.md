# EnqueueReadBuffer

---
```cpp
void tt::tt_metal::EnqueueReadBuffer(CommandQueue &cq, std::variant<std::reference_wrapper<Buffer>, std::shared_ptr<Buffer>> buffer, std::vector<uint32_t> &dst, bool blocking)void tt::tt_metal::EnqueueReadBuffer(CommandQueue &cq, std::variant<std::reference_wrapper<Buffer>, std::shared_ptr<Buffer>> buffer, std::vector<uint32_t> &dst, bool blocking)
```

Reads a buffer from the device

Return value: void

| Argument      | Description                                                           | Type                                | Valid Range                            | Required       |
|---------------|-----------------------------------------------------------------------|-------------------------------------|----------------------------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue &                      |                                        | Yes            |
| buffer        | The device buffer we are reading from                                 | Buffer & or std::shared_ptr<Buffer> |                                        | Yes            |
| dst           | The vector where the results that are read will be stored             | vector<uint32_t> &                  |                                        | Yes            |
| blocking      | Whether or not this is a blocking operation                           | bool                                | Only blocking mode supported currently | Yes            |

---
```cpp
void tt::tt_metal::EnqueueReadBuffer(CommandQueue &cq, std::variant<std::reference_wrapper<Buffer>, std::shared_ptr<Buffer>> buffer, void *dst, bool blocking)void tt::tt_metal::EnqueueReadBuffer(CommandQueue &cq, std::variant<std::reference_wrapper<Buffer>, std::shared_ptr<Buffer>> buffer, void \*dst, bool blocking)
```

Reads a buffer from the device

Return value: void

| Argument      | Description                                                           | Type                                | Valid Range                            | Required       |
|---------------|-----------------------------------------------------------------------|-------------------------------------|----------------------------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue &                      |                                        | Yes            |
| buffer        | The device buffer we are reading from                                 | Buffer & or std::shared_ptr<Buffer> |                                        | Yes            |
| dst           | The memory where the result will be stored                            | void\*                              |                                        | Yes            |
| blocking      | Whether or not this is a blocking operation                           | bool                                | Only blocking mode supported currently | Yes            |
