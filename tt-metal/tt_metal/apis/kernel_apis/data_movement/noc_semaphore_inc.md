# noc_semaphore_inc

---
```cpp
inline void noc_semaphore_inc(uint64_t addr, uint32_t incr)inline void noc_semaphore_inc(uint64_t addr, uint32_t incr)
```

The Tensix core executing this function call initiates an atomic increment (with 32-bit wrap) of a remote Tensix core L1 memory address. This L1 memory address is used as a semaphore of size 4 Bytes, as a synchronization mechanism.

Return value: None

| Argument      | Description                                        | Type      | Valid Range                                                   | Required       |
|---------------|----------------------------------------------------|-----------|---------------------------------------------------------------|----------------|
| addr          | Encoding of the destination location (x,y)+address | uint64_t  | DOX-TODO(insert a reference to what constitutes valid coords) | True           |
| incr          | The value to increment by                          | uint32_t  | Any uint32_t value                                            | True           |
