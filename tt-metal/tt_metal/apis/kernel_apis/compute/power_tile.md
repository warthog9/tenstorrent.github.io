# power_tile

```cpp
void ckernel::power_tile_init()
```

Please refer to documentation for any_init. 

```cpp
void ckernel::power_tile(uint32_t idst, uint32_t param0)
```

Performs element-wise computation of power operation (x ^(const param0)) value on each element of a tile in DST register at index tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| idst          | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
| param0        | The value of the exponent in the power operation                           | uint32_t  |                                                       | True           |
