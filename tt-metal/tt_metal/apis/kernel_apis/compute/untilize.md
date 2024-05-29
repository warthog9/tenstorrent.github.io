# untilize

### void ckernel::untilize_init(uint32_t icb, uint32_t ocb = 16)

Init function for untilize operations, to be used at the beginning of the kernel. 

### void ckernel::untilize_init_short(uint32_t icb)

Short init function to initialize untilize op, after a full init is already performed. 

### template<int N = 1> void ckernel::untilize_block(uint32_t icb, uint32_t block, uint32_t ocb)

Perform the untilize operation on a block of tiles. This simply loops over the provided block size. 

### void ckernel::untilize_uninit(uint32_t icb)

Uninitialize untilize operation, to allow initializing another operation.
