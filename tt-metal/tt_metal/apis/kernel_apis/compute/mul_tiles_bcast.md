# mul_tiles_bcast

### void ckernel::mul_bcast_cols_init_short(uint32_t icb0 = 0, uint32_t icb1 = 1)

Performs a first-call or switch-from-another-op tile hw reconfiguration step needed for mul_bcast_cols to be executed correctly. 

### void ckernel::mul_bcast_rows_init_short(uint32_t icb0 = 0, uint32_t icb1 = 1)

Performs a switch-from-another-op tile hw reconfiguration step needed for mul_bcast_rows to be executed correctly. 

### template<BroadcastType tBcastDim> void ckernel::mul_tiles_bcast(uint32_t icb0, uint32_t icb1, uint32_t itile0, uint32_t itile1, uint32_t idst)

Please refer to documentation for *add_tiles_bcast*. 

### void ckernel::mul_tiles_bcast_scalar_init_short(uint32_t icb0 = 0, uint32_t icb1 = 1)

Performs a first-call or switch-from-another-op tile hw reconfiguration step needed for mul_bcast_cols to be executed correctly. 

### void ckernel::mul_tiles_bcast_scalar(uint32_t icb0, uint32_t icb1, uint32_t itile0, uint32_t itile1, uint32_t idst)

Performs a broadcast-multiply of a tile from icb0[itile0] with a scalar encoded as a tile from icb1[itile1].
