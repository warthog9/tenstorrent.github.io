# BeginTraceCapture

---
```cpp
uint32_t tt::tt_metal::BeginTraceCapture(Device *device, const uint8_t cq_id, const uint32_t trace_buff_size)uint32_t tt::tt_metal::BeginTraceCapture(Device \*device, const uint8_t cq_id, const uint32_t trace_buff_size)
```

Begins capture on a trace, when the trace is in capture mode all programs pushed into the trace queue will have their execution delayed until the trace is instantiated and enqueued. The capture must be later ended via EndTraceCapture, and finally scheduled to be executed via ReplayTrace. Beginning a trace capture enabled buffer allocations until capture has ended.

Return value: Trace ID

| Argument        | Description                                     | Type      | Valid Range      | Required       |
|-----------------|-------------------------------------------------|-----------|------------------|----------------|
| device          | The device holding being traced.                | Device \* |                  | Yes            |
| cq_id           | The command queue id associated with the trace. | uint8_t   |                  | Yes            |
| trace_buff_size | The size of the trace buffer to pre-allocate.   | uint32_t  |                  | Yes            |
