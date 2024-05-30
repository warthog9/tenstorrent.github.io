# CreateSemaphore

```cpp
uint32_t tt::tt_metal::CreateSemaphore(Program &program, const std::variant<CoreRange, CoreRangeSet> &core_spec, uint32_t initial_value, CoreType core_type = CoreType::WORKER)
```

Initializes semaphore on all cores within core range (inclusive). Each core can have up to four 32B semaphores.

Return value: Semaphore address (uint32_t)

| Argument      | Description                                          | Type                                         | Valid Range      | Required       |
|---------------|------------------------------------------------------|----------------------------------------------|------------------|----------------|
| program       | The program to which semaphore will be added to      | Program &                                    |                  | Yes            |
| core_spec     | Range of the Tensix co-ordinates using the semaphore | const std::variant<CoreRange,CoreRangeSet> & |                  | Yes            |
| initial_value | Initial value of the semaphore                       | uint32_t                                     |                  | Yes            |
| core_type     | Tensix or Ethernet core to create semaphore on.      | CoreType                                     |                  | Yes            |
