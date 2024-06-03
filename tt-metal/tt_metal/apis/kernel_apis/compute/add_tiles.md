# add_tiles

---
```cpp
void ckernel::add_tiles_init_nof()void ckernel::add_tiles_init_nof()
```

Please refer to documentation for any_init. nof means low fidelity with resepect to accuracy this is set during createprogram 

---
```cpp
void ckernel::add_tiles_init(uint32_t icb0 = 0, uint32_t icb1 = 1)void ckernel::add_tiles_init(uint32_t icb0 = 0, uint32_t icb1 = 1)
```

Please refer to documentation for any_init. 

---
```cpp
void ckernel::add_tiles(uint32_t icb0, uint32_t icb1, uint32_t itile0, uint32_t itile1, uint32_t idst)void ckernel::add_tiles(uint32_t icb0, uint32_t icb1, uint32_t itile0, uint32_t itile1, uint32_t idst)
```

Performs element-wise addition C=A+B of tiles in two CBs at given indices and writes the result to the DST register at index dst_tile_index. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument       | Description                                             | Type      | Valid Range                                    | Required       |
|----------------|---------------------------------------------------------|-----------|------------------------------------------------|----------------|
| in0_cb_id      | The identifier of the circular buffer (CB) containing A | uint32_t  | 0 to 31                                        | True           |
| in1_cb_id      | The identifier of the circular buffer (CB) containing B | uint32_t  | 0 to 31                                        | True           |
| in0_tile_index | The index of tile A within the first CB                 | uint32_t  | Must be less than the size of the CB           | True           |
| in1_tile_index | The index of tile B within the second CB                | uint32_t  | Must be less than the size of the CB           | True           |
| dst_tile_index | The index of the tile in DST REG for the result C       | uint32_t  | Must be less than the acquired size of DST REG | True           |
