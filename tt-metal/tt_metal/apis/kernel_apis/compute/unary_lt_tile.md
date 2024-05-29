# unary_lt_tile

### void ckernel::unary_lt_tile_init()

Please refer to documentation for any_init. 

### void ckernel::unary_lt_tile(uint32_t idst, uint32_t param0)

Performs element-wise computation of: result = 1 if x < value , where x is each element of a tile in DST register at index tile_index. The value is provided as const param0 The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| idst          | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
| param0        | The value to be compared with the input tensor                             | uint32_t  |                                                       | True           |
