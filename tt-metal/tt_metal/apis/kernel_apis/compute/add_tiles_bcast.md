# add_tiles_bcast

### void ckernel::add_bcast_cols_init_short(uint32_t icb0 = 0, uint32_t icb1 = 1)

Performs a first-call or switch-from-another-op tile hw reconfiguration step needed for add_bcast_cols to be executed correctly. Required to be called before add_tiles_bcast if using column as broadcast type 

### void ckernel::add_bcast_rows_init_short(uint32_t icb0 = 0, uint32_t icb1 = 1)

Performs a first-call or switch-from-another-op tile hw reconfiguration step needed for add_bcast_rows to be executed correctly. Required to be called before add_tiles_bcast if using column as broadcast type 

### template<BroadcastType tBcastDim> void ckernel::add_tiles_bcast(uint32_t icb0, uint32_t icb1, uint32_t itile0, uint32_t itile1, uint32_t idst)

This documentation applies to either one of the 3 broadcast operation variants - *add_tiles_bcast*, *sub_tiles_bcast* and *mul_tiles_bcast*.

The description below describes *add_tiles_bcast*, the other 2 operations use the same definition with the corresponding substitution of the math operator.

Performs a broadcast-operation *C=A+B* of tiles in two CBs at given indices and writes the result to the DST register at index dst_tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Broadcasting semantics are defined as follows:

For *dim==BroadcastType::COL*, the input in *B* is expected to be a single tile with a filled 0-column and zeros elsewhere. The result is *C[h, w] = A[h,w] + B[w]*

For *dim==Dim::C*, the input in *B* is expected to be a single tile with a filled 0-row, and zeros elsewhere. The result is *C[h, w] = A[h,w] + B[h]*

For *dim==Dim::RC*, the input in *B* is expected to be a single tile with a filled single value at location [0,0], and zeros elsewhere. The result is *C[h, w] = A[h,w] + B[0,0]*

Return value: None

DOX-TODO(AP): verify that the bcast tile is actually required to be filled with zeros.

| Argument       | Description                                              | Type          | Valid Range                                    | Required       |
|----------------|----------------------------------------------------------|---------------|------------------------------------------------|----------------|
| tBcastDim      | Broadcast dimension                                      | BroadcastType | One of Dim::R, Dim::C, Dim::RC.                | True           |
| in0_cb_id      | The identifier of the circular buffer (CB) containing A  | uint32_t      | 0 to 31                                        | True           |
| in1_cb_id      | The indentifier of the circular buffer (CB) containing B | uint32_t      | 0 to 31                                        | True           |
| in0_tile_index | The index of tile A within the first CB                  | uint32_t      | Must be less than the size of the CB           | True           |
| in1_tile_index | The index of tile B within the second CB                 | uint32_t      | Must be less than the size of the CB           | True           |
| dst_tile_index | The index of the tile in DST REG for the result C        | uint32_t      | Must be less than the acquired size of DST REG | True           |
