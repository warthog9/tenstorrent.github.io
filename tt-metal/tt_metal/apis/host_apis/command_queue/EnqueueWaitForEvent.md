# EnqueueWaitForEvent

---
```cpp
void tt::tt_metal::EnqueueWaitForEvent(CommandQueue &cq, std::shared_ptr<Event> event)void tt::tt_metal::EnqueueWaitForEvent(CommandQueue &cq, std::shared_ptr<Event> event)
```

Enqueues a command on the device for a given CQ (non-blocking). The command on device will block and wait for completion of the specified event (which may be in another CQ). Return value: void 

| Argument      | Description                                                           | Type                   | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------------|------------------------|------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue &         |                  | Yes            |
|               | and waits for the event to complete.                                  |                        |                  |                |
| event         | The event object that this CQ will wait on for completion.            | std::shared_ptr<Event> |                  | Yes            |
