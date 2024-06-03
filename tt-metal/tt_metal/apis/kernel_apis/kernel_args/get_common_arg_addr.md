# get_common_arg_addr

---
```cpp
static uint32_t get_common_arg_addr(int arg_idx)static uint32_t get_common_arg_addr(int arg_idx)
```

Returns the address in L1 for a given runtime argument index for common (all cores) runtime arguments set via SetCommonRuntimeArgs() API.

Return value: Associated L1 address of given common runtime argument index

| Argument      | Description                   | Type      | Valid Range      | Required       |
|---------------|-------------------------------|-----------|------------------|----------------|
| arg_idx       | Common Runtime argument index | uint32_t  | 0 to 255         | True           |
