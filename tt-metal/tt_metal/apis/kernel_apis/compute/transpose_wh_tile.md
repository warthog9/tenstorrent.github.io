# transpose_wh_tile

### void ckernel::transpose_wh_init(uint32_t icb, uint32_t ocb = 16)

Paired Init function for transpose_wh. For general information on init functions refer to any_init.

| Argument      | Description                                                 | Type      | Valid Range      | Required       |
|---------------|-------------------------------------------------------------|-----------|------------------|----------------|
| icb           | The identifier of the circular buffer (CB) containing input | uint32_t  | 0 to 31          | True           |

### void ckernel::transpose_wh_tile(uint32_t icb, uint32_t itile, uint32_t idst)

Performs a 32x32 transpose operation *B[w,h] = A[h,w]* on a tile in the CB at a given index and writes the result to the DST register at index dst_tile_index. The DST register buffer must be in acquired state via *acquire_dst* call.

This call is blocking and is only available on the compute engine.

Return value: None

| Argument       | Description                                             | Type      | Valid Range                                    | Required       |
|----------------|---------------------------------------------------------|-----------|------------------------------------------------|----------------|
| in_cb_id       | The identifier of the circular buffer (CB) containing A | uint32_t  | 0 to 31                                        | True           |
| in_tile_index  | The index of tile A within the first CB                 | uint32_t  | Must be less than the size of the CB           | True           |
| dst_tile_index | The index of the tile in DST REG for the result B       | uint32_t  | Must be less than the acquired size of DST REG | True           |
