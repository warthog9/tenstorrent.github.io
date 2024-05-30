<a id="tt-tt-metal-finish"></a>

# Finish

```cpp
void tt::tt_metal::Finish(CommandQueue &cq)
```

Blocks until all previously dispatched commands on the device have completed

Return value: void

| Argument      | Description                                                           | Type           | Valid Range      | Required       |
|---------------|-----------------------------------------------------------------------|----------------|------------------|----------------|
| cq            | The command queue object which dispatches the command to the hardware | CommandQueue & |                  | Yes            |
