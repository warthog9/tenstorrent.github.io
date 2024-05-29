# matmul_tiles

### void ckernel::mm_init(uint32_t in0_cb_id = 0, uint32_t in1_cb_id = 1, uint32_t out_cb_id = 16, const uint32_t transpose = 0)

Initialization for matmul_tiles operation. Must be called before matmul_tiles.

Return value: None

| Argument      | Description                                                | Type      | Valid Range                                      | Required       |
|---------------|------------------------------------------------------------|-----------|--------------------------------------------------|----------------|
| in0_cb_id     | The identifier of the first input circular buffer (CB)     | uint32_t  | 0 to 31                                          | False          |
| in1_cb_id     | The identifier of the second input circular buffer (CB)    | uint32_t  | 0 to 31                                          | False          |
| out_cb_id     | The identifier of the output circular buffer (CB)          | uint32_t  | 0 to 31                                          | False          |
| transpose     | The transpose flag for performing transpose operation on B | uint32_t  | Any positive value will indicate tranpose is set | False          |

### void ckernel::mm_init_short_with_dt(uint32_t in0_cb_id = 0, uint32_t in1_cb_id = 1, uint32_t c_in_old_srca = 2, const uint32_t transpose = 0)

A short version of matmul_tiles initialization. It is used to reconfigure srcA of the compute engine back to matmul mode.

Return value: None

| Argument      | Description                                                   | Type      | Valid Range                                      | Required       |
|---------------|---------------------------------------------------------------|-----------|--------------------------------------------------|----------------|
| in0_cb_id     | The identifier of the first input circular buffer (CB)        | uint32_t  | 0 to 31                                          | False          |
| in1_cb_id     | The identifier of the second input circular buffer (CB)       | uint32_t  | 0 to 31                                          | False          |
| c_in_old_srca | The identifier of the old input to src A circular buffer (CB) | uint32_t  | 0 to 31                                          | False          |
| transpose     | The transpose flag for performing transpose operation on B    | uint32_t  | Any positive value will indicate tranpose is set | False          |

### void ckernel::mm_init_short(uint32_t in0_cb_id = 0, uint32_t in1_cb_id = 1, const uint32_t transpose = 0)

A short version of matmul_tiles initialization. Configure the unpacker and math engine to matmul mode.

Return value: None

| Argument      | Description                                                | Type      | Valid Range                                      | Required       |
|---------------|------------------------------------------------------------|-----------|--------------------------------------------------|----------------|
| in0_cb_id     | The identifier of the first input circular buffer (CB)     | uint32_t  | 0 to 31                                          | False          |
| in1_cb_id     | The identifier of the second input circular buffer (CB)    | uint32_t  | 0 to 31                                          | False          |
| transpose     | The transpose flag for performing transpose operation on B | uint32_t  | Any positive value will indicate tranpose is set | False          |

### void ckernel::matmul_tiles(uint32_t in0_cb_id, uint32_t in1_cb_id, uint32_t in0_tile_index, uint32_t in1_tile_index, uint32_t idst, const uint32_t transpose)

Performs tile-sized matrix multiplication *C=A\*B* between the tiles in two specified input CBs and writes the result to DST. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument       | Description                                                             | Type      | Valid Range                                    | Required       |
|----------------|-------------------------------------------------------------------------|-----------|------------------------------------------------|----------------|
| in0_cb_id      | The identifier of the first input circular buffer (CB)                  | uint32_t  | 0 to 31                                        | True           |
| in1_cb_id      | The identifier of the second input circular buffer (CB)                 | uint32_t  | 0 to 31                                        | True           |
| in0_tile_index | The index of the tile A from the first input CB                         | uint32_t  | Must be less than the size of the CB           | True           |
| in1_tile_index | The index of the tile B from the second input CB                        | uint32_t  | Must be less than the size of the CB           | True           |
| dst_tile_index | The index of the tile in DST REG to which the result C will be written. | uint32_t  | Must be less than the acquired size of DST REG | True           |
