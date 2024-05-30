# EnqueueTrace

```cpp
void tt::tt_metal::EnqueueTrace(CommandQueue &cq, uint32_t trace_id, bool blocking)
```

Enqueues a trace of previously generated commands and data.

Return value: void

| Argument      | Description                                                           | Type           | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------------|----------------|------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue & |                  | Yes            |
| trace_id      | A unique id representing an existing on-device trace, which has been  | uint32_t       |                  | Yes            |
|               | instantiated via InstantiateTrace where the trace_id is returned      |                |                  |                |
| blocking      | Whether or not this is a blocking operation                           | bool           |                  | Yes            |
