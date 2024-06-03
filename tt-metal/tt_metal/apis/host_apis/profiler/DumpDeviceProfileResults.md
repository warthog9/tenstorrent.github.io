<a id="dumpdeviceprofileresults"></a>

# DumpDeviceProfileResults

---
```cpp
void tt::tt_metal::DumpDeviceProfileResults(Device *device, const Program &program)void tt::tt_metal::DumpDeviceProfileResults(Device \*device, const Program &program)
```

Read device side profiler data and dump results into device side CSV log

This function only works in PROFILER builds. Please refer to the “Device Program Profiler” section for more information.

Return value: void

| Argument      | Description                                    | Type            | Valid Range      | Required       |
|---------------|------------------------------------------------|-----------------|------------------|----------------|
| device        | The device holding the program being profiled. | Device \*       |                  | True           |
| program       | The program being profiled.                    | const Program & |                  | True           |
