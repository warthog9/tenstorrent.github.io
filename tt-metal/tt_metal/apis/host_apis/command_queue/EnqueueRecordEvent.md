# EnqueueRecordEvent

---
```cpp
void tt::tt_metal::EnqueueRecordEvent(CommandQueue &cq, std::shared_ptr<Event> event)void tt::tt_metal::EnqueueRecordEvent(CommandQueue &cq, std::shared_ptr<Event> event)
```

Enqueues a command to record an Event on the device for a given CQ, and updates the Event object for the user. Return value: void 

| Argument      | Description                                                           | Type                   | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------------|------------------------|------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue &         |                  | Yes            |
| event         | An event that will be populated by this function, and inserted in CQ  | std::shared_ptr<Event> |                  | Yes            |
