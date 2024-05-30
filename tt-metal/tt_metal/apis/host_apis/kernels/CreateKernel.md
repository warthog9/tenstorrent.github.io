# CreateKernel

```cpp
KernelHandle tt::tt_metal::CreateKernel(Program &program, const std::string &file_name, const std::variant<CoreCoord, CoreRange, CoreRangeSet> &core_spec, const std::variant<DataMovementConfig, ComputeConfig, EthernetConfig> &config)
```

Creates a data movement kernel with no compile time arguments and adds it to the program.

Return value: Kernel ID (uintptr_t)

| Argument      | Description                                                                                                                          | Type                                                                  | Valid Range      | Required       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------|----------------|
| program       | The program to which this kernel will be added to                                                                                    | Program &                                                             |                  | Yes            |
| file_name     | Path to kernel src. Assumed to be absolute path, but will fall back to relative path from TT_METAL_HOME if file doesn’t exist.       | const std::string &                                                   |                  | Yes            |
| core_spec     | Either a single logical core, a range of logical cores or a set of logical core ranges that indicate which cores kernel is placed on | const std::variant<CoreCoord, CoreRange, CoreRangeSet> &              |                  | Yes            |
| config        | Config for data movement or compute kernel                                                                                           | const std::variant<DataMovementConfig,ComputeConfig,EthernetConfig> & |                  | No             |
