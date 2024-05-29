# sign_tile

### void ckernel::sign_tile_init()

Please refer to documentation for any_init. 

### void ckernel::sign_tile(uint32_t idst)

Will store in the output of the compute core the signum of the tile. The DST register buffer must be in acquired state via *acquire_dst* call. This call is blocking and is only available on the compute engine.

Return value: None

| Argument      | Description                                                                | Type      | Valid Range                                           | Required       |
|---------------|----------------------------------------------------------------------------|-----------|-------------------------------------------------------|----------------|
| idst          | The index of the tile in DST register buffer to perform the computation on | uint32_t  | Must be less than the size of the DST register buffer | True           |
