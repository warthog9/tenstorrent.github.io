# reduce_tile

```cpp
template<PoolType reduce_type = REDUCE_OP, ReduceDim reduce_dim = REDUCE_DIM> void ckernel::reduce_tile(uint32_t icb0, uint32_t icb1, uint32_t itile0, uint32_t itile1, uint32_t idst)
```

Performs a reduction operation *B = reduce(A)* using reduce_func for dimension reduction on a tile in the CB at a given index and writes the result to the DST register at index *dst_tile_index*. Reduction can be either of type *Reduce::R*, *Reduce::C* or *Reduce::RC*, identifying the dimension(s) to be reduced in size to 1. The DST register buffer must be in acquired state via *acquire_dst* call.

The templates takes reduce_type which can be ReduceFunc::Sum, ReduceFunc::Max and reduce_dim which can be Reduce::R, Reduce::C, Reduce::RC. They can also be specified by defines REDUCE_OP and REDUCE_DIM.

This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                  | Type      | Valid Range                                    | Required       |
|---------------|--------------------------------------------------------------|-----------|------------------------------------------------|----------------|
| icb0          | The identifier of the circular buffer (CB) containing A      | uint32_t  | 0 to 31                                        | True           |
| icb1          | CB for Scaling factor applied to each element of the result. | uint32_t  | 0 to 31                                        | True           |
| itile0        | The index of the tile within the first CB                    | uint32_t  | Must be less than the size of the CB           | True           |
| itile1        | The index of the tile within the scaling factor CB           | uint32_t  | Must be less than the size of the CB           | True           |
| idst          | The index of the tile in DST REG for the result              | uint32_t  | Must be less than the acquired size of DST REG | True           |
