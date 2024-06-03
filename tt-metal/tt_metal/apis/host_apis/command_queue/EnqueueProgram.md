# EnqueueProgram

---
```cpp
void tt::tt_metal::EnqueueProgram(CommandQueue &cq, std::variant<std::reference_wrapper<Program>, std::shared_ptr<Program>> program, bool blocking)void tt::tt_metal::EnqueueProgram(CommandQueue &cq, std::variant<std::reference_wrapper<Program>, std::shared_ptr<Program>> program, bool blocking)
```

Writes a program to the device and launches it

Return value: void

| Argument      | Description                                                           | Type           | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------------|----------------|------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue & |                  | Yes            |
| program       | The program that will be executed on the device that cq is bound to   | Program &      |                  | Yes            |
| blocking      | Whether or not this is a blocking operation                           | bool           |                  | Yes            |
