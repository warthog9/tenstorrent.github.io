# ReplayTrace

---
```cpp
void tt::tt_metal::ReplayTrace(Device *device, const uint8_t cq_id, const uint32_t tid, const bool blocking)void tt::tt_metal::ReplayTrace(Device \*device, const uint8_t cq_id, const uint32_t tid, const bool blocking)
```

Replay a trace of previously generated commands and data.

Return value: void

| Argument      | Description                                          | Type      | Valid Range      | Required       |
|---------------|------------------------------------------------------|-----------|------------------|----------------|
| device        | The device holding the trace.                        | Device \* |                  | Yes            |
| cq_id         | The command queue id associated with the trace.      | uint8_t   |                  | Yes            |
| trace_id      | A unique id representing an existing captured trace. | uint32_t  |                  | Yes            |
| blocking      | Whether or not this is a blocking operation          | bool      |                  | Yes            |
