# isinf_tile

---
```cpp
void ckernel::isinf_tile_init()void ckernel::isinf_tile_init()
```

Please refer to documentation for any_init. 

---
```cpp
void ckernel::isinf_tile(uint32_t idst)void ckernel::isinf_tile(uint32_t idst)
```

Will store in the output of the compute core True if the input tile is infinity. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |

# isposinf_tile

---
```cpp
void ckernel::isposinf_tile_init()void ckernel::isposinf_tile_init()
```

Please refer to documentation for any_init. 

---
```cpp
void ckernel::isposinf_tile(uint32_t idst)void ckernel::isposinf_tile(uint32_t idst)
```

Will store in the output of the compute core True if the input tile is positive infinity. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |

# isneginf_tile

---
```cpp
void ckernel::isneginf_tile_init()void ckernel::isneginf_tile_init()
```

Please refer to documentation for any_init. 

---
```cpp
void ckernel::isneginf_tile(uint32_t idst)void ckernel::isneginf_tile(uint32_t idst)
```

Will store in the output of the compute core True if the input tile is negative infinity. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |

# isfinite_tile

---
```cpp
void ckernel::isfinite_tile_init()void ckernel::isfinite_tile_init()
```

Please refer to documentation for any_init. 

---
```cpp
void ckernel::isfinite_tile(uint32_t idst)void ckernel::isfinite_tile(uint32_t idst)
```

Will store in the output of the compute core True if the input tile is finite The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| tile_index    | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
