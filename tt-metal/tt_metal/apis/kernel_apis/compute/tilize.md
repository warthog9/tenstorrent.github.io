# tilize

### void ckernel::tilize_init(uint32_t icb, uint32_t block, uint32_t ocb = 16)

Initialize the tilize operation. To be called once at beginning of a kernel. 

### void ckernel::tilize_init_short(uint32_t icb, uint32_t block)

Re-initialize for the tilize operation. This can be called after a full init. 

### void ckernel::tilize_init_short_with_dt(uint32_t old_icb, uint32_t new_icb, uint32_t block)

Re-initialize for the tilize operation. This also reconfigure the unpacker with CB data type. 

### void ckernel::tilize_block(uint32_t icb, uint32_t block, uint32_t ocb)

Perform tilize operation on a block. This simply loops over the provided blocks. 

### void ckernel::tilize_uninit(uint32_t icb)

Uninitialize tilize operation before re-initializing for another operation. 

### void ckernel::tilize_uninit_with_dt(uint32_t old_icb = 0, uint32_t new_icb = 1)

Uninitialize the tilize operation along with re-configuring unpacker with the CB data types.
