# move_copy_tile

### void ckernel::copy_tile_to_dst_init_short_with_dt(uint32_t old_cbid, uint32_t new_cbid, uint32_t transpose = 0)

Return value: None

| Argument      | Description                                                       | Type      | Valid Range                                      | Required       |
|---------------|-------------------------------------------------------------------|-----------|--------------------------------------------------|----------------|
| old_cbid      | The identifier of the previous input circular buffer (CB) to SrcA | uint32_t  | 0 to 31                                          | True           |
| new_cbid      | The identifier of the new input circular buffer (CB) to SrcA      | uint32_t  | 0 to 31                                          | True           |
| transpose     | Flag to perform transpose on SrcA                                 | uint32_t  | Any positive value will indicate tranpose is set | False          |

### void ckernel::copy_tile_to_dst_init_short(uint32_t cbid = 0, uint32_t transpose = 0)

Perform the init short for copy tile. This does not reconfigure the unpacker data types. Return value: None

| Argument      | Description                                      | Type      | Valid Range                                      | Required       |
|---------------|--------------------------------------------------|-----------|--------------------------------------------------|----------------|
| cbid          | The identifier of the input circular buffer (CB) | uint32_t  | 0 to 31                                          | False          |
| transpose     | Flag to perform transpose on SrcA                | uint32_t  | Any positive value will indicate tranpose is set | False          |

### void ckernel::copy_tile_init()

Perform a init for the copy tile operation. This calls the short init function and initializes packer dst offset registers.
