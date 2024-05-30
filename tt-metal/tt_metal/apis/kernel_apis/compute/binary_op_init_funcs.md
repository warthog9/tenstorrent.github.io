# binary_init_funcs

```cpp
void ckernel::binary_op_init_common(uint32_t icb0, uint32_t icb1, uint32_t ocb = 16)
```

Init function for all binary ops Followed by the specific init required with an opcode (binrary_op_specific_init) 

| Argument      | Description                                                  | Type      | Valid Range                | Required       |
|---------------|--------------------------------------------------------------|-----------|----------------------------|----------------|
| icb0          | The identifier of the circular buffer (CB) containing A      | uint32_t  | 0 to 31                    | True           |
| icb1          | The identifier of the circular buffer (CB) containing B      | uint32_t  | 0 to 31                    | True           |
| ocb           | The identifier of the circular buffer (CB) containing output | uint32_t  | 0 to 31, defaults to CB 16 | True           |

```cpp
template<bool full_init = false> void ckernel::binary_op_specific_init(int op_code)
```

Init function with a specified op 

| Argument      | Description                 | Type      | Valid Range      | Required       |
|---------------|-----------------------------|-----------|------------------|----------------|
| op_code       | op code corresponding to op | uint32_t  | 0 to 31          | True           |
