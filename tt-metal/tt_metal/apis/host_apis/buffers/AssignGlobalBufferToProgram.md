# AssignGlobalBufferToProgram

```cpp
void tt::tt_metal::AssignGlobalBufferToProgram(std::shared_ptr<Buffer> buffer, std::variant<std::reference_wrapper<Program>, std::shared_ptr<Program>> program)
```

Gives the specified program ownership of the buffer: the buffer will remain on device at least until the program is enqueued. This is required for asynchronous Command Queues.

Return value: void

| Argument      | Description                                  | Type                           | Valid Range      | Required       |
|---------------|----------------------------------------------|--------------------------------|------------------|----------------|
| buffer        | The buffer that will be owned by the program | std::shared_ptr<Buffer> buffer |                  | Yes            |
| program       | The program getting ownership of the buffer  | std::shared_ptr<Buffer> buffer |                  | Yes            |
