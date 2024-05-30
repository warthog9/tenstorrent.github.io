# EndTraceCapture

```cpp
void tt::tt_metal::EndTraceCapture(Device *device, const uint8_t cq_id, const uint32_t tid)
```

Completes capture on a trace, if captured commands do not conform to the rules of the trace, the trace will be invalidated. This trace can be enqueued for execution via ReplayTrace on the same device command queue. After ending a trace capture, buffer allocations on device are disabled until either a new trace begins capture, or all traces on the device are released

Return value: void

| Argument      | Description                                                     | Type      | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------|-----------|------------------|----------------|
| device        | The device holding being traced.                                | Device \* |                  | Yes            |
| cq_id         | The command queue id associated with the trace.                 | uint8_t   |                  | Yes            |
| tid           | A unique id from BeginTraceCapture for the trace being captured | uint32_t  |                  | Yes            |
