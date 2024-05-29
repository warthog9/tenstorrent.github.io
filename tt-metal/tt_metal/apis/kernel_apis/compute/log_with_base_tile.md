# log_with_base_tile

### void ckernel::log_with_base_tile_init()

Please refer to documentation for any_init. 

### void ckernel::log_with_base_tile(uint32_t idst, uint32_t base_scale)

Performs element-wise computation of logarithm with a specified base on each element of a tile in DST register at index tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| idst          | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
| base_scale    | The log base                                                               | uint32_t  | Postive integers                                      | True           |
