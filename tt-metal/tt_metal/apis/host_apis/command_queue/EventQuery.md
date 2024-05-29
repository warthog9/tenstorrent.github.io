# EventQuery

### bool tt::tt_metal::EventQuery(std::shared_ptr<Event> event)

Host will query an event for completion status on device. Return value: bool. True if event is completed, false otherwise. 

| Argument      | Description                                           | Type                   | Valid Range      | Required       |
|---------------|-------------------------------------------------------|------------------------|------------------|----------------|
| event         | The event object that host will query for completion. | std::shared_ptr<Event> |                  | Yes            |
