# ReleaseTrace

### void tt::tt_metal::ReleaseTrace(Device *device, const uint32_t tid)

Release a previously instantiated trace, deallocating the associated trace buffers on device This operation is not thread-safe, user must ensure that the trace being released is no longer needed by device threads If this releases the last trace on a device, then buffer allocations are re-enabled

Return value: void

| Argument      | Description                                          | Type      | Valid Range      | Required       |
|---------------|------------------------------------------------------|-----------|------------------|----------------|
| device        | The device holding the trace.                        | Device \* |                  | Yes            |
| trace_id      | A unique id representing an existing captured trace. | uint32_t  |                  | Yes            |
