# get_compile_time_arg_val

---
```cpp
get_compile_time_arg_val(arg_idx)get_compile_time_arg_val(arg_idx)
```

Returns the value of a constexpr argument from kernel_compile_time_args array provided during kernel creation using CreateKernel calls.

Return value: constexpr uint32_t

| Argument      | Description               | Type      | Valid Range      | Required       |
|---------------|---------------------------|-----------|------------------|----------------|
| arg_idx       | The index of the argument | uint32_t  | 0 to 31          | True           |
