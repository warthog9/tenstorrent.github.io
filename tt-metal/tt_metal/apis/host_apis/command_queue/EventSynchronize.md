# EventSynchronize

---
```cpp
void tt::tt_metal::EventSynchronize(std::shared_ptr<Event> event)void tt::tt_metal::EventSynchronize(std::shared_ptr<Event> event)
```

Blocking function for host to synchronize (wait) on an event completion on device. Return value: void 

| Argument      | Description                                             | Type                   | Valid Range      | Required       |
|---------------|---------------------------------------------------------|------------------------|------------------|----------------|
| event         | The event object that host will wait on for completion. | std::shared_ptr<Event> |                  | Yes            |
