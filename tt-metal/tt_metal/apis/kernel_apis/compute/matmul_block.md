# matmul_block

### void ckernel::mm_block_init(uint32_t in0_cb_id = 0, uint32_t in1_cb_id = 1, uint32_t out_cb_id = 16, const uint32_t transpose = 0, uint32_t ct_dim = 1, uint32_t rt_dim = 1, uint32_t kt_dim = 1)

Initialization for matmul_block operation. Must be called before matmul_block.

Return value: None

| Argument      | Description                                             | Type      | Valid Range                                         | Required       |
|---------------|---------------------------------------------------------|-----------|-----------------------------------------------------|----------------|
| in0_cb_id     | The identifier of the first input circular buffer (CB)  | uint32_t  | 0 to 31                                             | False          |
| in1_cb_id     | The identifier of the second input circular buffer (CB) | uint32_t  | 0 to 31                                             | False          |
| out_cb_id     | The identifier of the output circular buffer (CB)       | uint32_t  | 0 to 31                                             | False          |
| ct_dim        | the number of columns of the output matrix in tiles     | uint32_t  | 1 to 8 in half-sync mode, 1 to 16 in full-sync mode | False          |
| rt_dim        | the number of rows of the output matrix in tiles        | uint32_t  | 1 to 8 in half-sync mode, 1 to 16 in full-sync mode | False          |
| kt_dim        | the inner dim of the input matrices in tiles            | uint32_t  | 1 to 2^32-1                                         | False          |

### void ckernel::mm_block_init_short(uint32_t in0_cb_id = 0, uint32_t in1_cb_id = 1, const uint32_t transpose = 0, uint32_t ct_dim = 1, uint32_t rt_dim = 1, uint32_t kt_dim = 1)

A short version of matmul_block initialization. Configure the unpacker and math engine to matmul mode.

Return value: None

| Argument      | Description                                                | Type      | Valid Range                                      | Required       |
|---------------|------------------------------------------------------------|-----------|--------------------------------------------------|----------------|
| in0_cb_id     | The identifier of the first input circular buffer (CB)     | uint32_t  | 0 to 31                                          | False          |
| in1_cb_id     | The identifier of the second input circular buffer (CB)    | uint32_t  | 0 to 31                                          | False          |
| transpose     | The transpose flag for performing transpose operation on B | uint32_t  | Any positive value will indicate tranpose is set | False          |
| ct_dim        | The coloumn dimension for the output block.                | uint32_t  | Must be equal to block B column dimension        | False          |
| rt_dim        | The row dimension for the output block.                    | uint32_t  | Must be equal to block A row dimension           | False          |
| kt_dim        | The inner dimension.                                       | uint32_t  | Must be equal to block A column dimension        | False          |

### void ckernel::mm_block_init_short_with_dt(uint32_t in0_cb_id = 0, uint32_t in1_cb_id = 1, uint32_t old_in1_cb_id = 2, const uint32_t transpose = 0, uint32_t ct_dim = 1, uint32_t rt_dim = 1, uint32_t kt_dim = 1)

A short version of matmul_block initialization. It is used to reconfigure srcA of the compute engine back to matmul mode.

Return value: None

| Argument      | Description                                              | Type      | Valid Range                               | Required       |
|---------------|----------------------------------------------------------|-----------|-------------------------------------------|----------------|
| in0_cb_id     | The identifier of the first input circular buffer (CB)   | uint32_t  | 0 to 31                                   | False          |
| in1_cb_id     | The identifier of the second input circular buffer (CB)  | uint32_t  | 0 to 31                                   | False          |
| old_in1_cb_id | The identifier of the old in1_cb_id circular buffer (CB) | uint32_t  | 0 to 31                                   | False          |
| ct_dim        | The coloumn dimension for the output block.              | uint32_t  | Must be equal to block B column dimension | False          |
| rt_dim        | The row dimension for the output block.                  | uint32_t  | Must be equal to block A row dimension    | False          |
| kt_dim        | The inner dimension.                                     | uint32_t  | Must be equal to block A column dimension | False          |

### void ckernel::matmul_block(uint32_t in0_cb_id, uint32_t in1_cb_id, uint32_t in0_tile_index, uint32_t in1_tile_index, uint32_t idst, const uint32_t transpose, uint32_t ct_dim, uint32_t rt_dim, uint32_t kt_dim)

Performs block-sized matrix multiplication *C=A\*B* between the blocks in two different input CBs and writes the result to DST. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument       | Description                                                             | Type      | Valid Range                                    | Required       |
|----------------|-------------------------------------------------------------------------|-----------|------------------------------------------------|----------------|
| in0_cb_id      | The identifier of the first input circular buffer (CB)                  | uint32_t  | 0 to 31                                        | True           |
| in1_cb_id      | The identifier of the second input circular buffer (CB)                 | uint32_t  | 0 to 31                                        | True           |
| in0_tile_index | The index of the tile in block A from the first input CB                | uint32_t  | Must be less than the size of the CB           | True           |
| in1_tile_index | The index of the tile in block B from the second input CB               | uint32_t  | Must be less than the size of the CB           | True           |
| idst           | The index of the tile in DST REG to which the result C will be written. | uint32_t  | Must be less than the acquired size of DST REG | True           |
| transpose      | The transpose flag for performing transpose operation on tiles in B.    | bool      | Must be true or false                          | True           |
| ct_dim         | The coloumn dimension for the output block.                             | uint32_t  | Must be equal to block B column dimension      | True           |
| rt_dim         | The row dimension for the output block.                                 | uint32_t  | Must be equal to block A row dimension         | True           |
| kt_dim         | The inner dimension.                                                    | uint32_t  | Must be equal to block A column dimension      | True           |
