# acos_tile

---
```cpp
void ckernel::acos_tile_init()void ckernel::acos_tile_init()
```

Please refer to documentation for any_init. 

---
```cpp
void ckernel::acos_tile(uint32_t idst)void ckernel::acos_tile(uint32_t idst)
```

Performs element-wise computation of arccossine on each element of a tile in DST register at index tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| idst          | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
