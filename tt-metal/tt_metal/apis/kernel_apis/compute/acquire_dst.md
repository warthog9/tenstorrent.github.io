# acquire_dst

### void ckernel::acquire_dst(tt::DstMode mode)

Acquires an exclusive lock on the internal DST register for the current Tensix core.

This register is an array of 16 tiles of 32x32 elements each. This is a blocking function, i.e. this function will wait until the lock is acquired.

This is only available on the compute engine.

DOX-TODO(Describe meanings of dst_mode values).

Return value: None

| Argument      | Description                                                | Type      | Valid Range      | Required       |
|---------------|------------------------------------------------------------|-----------|------------------|----------------|
| dst_mode      | Specifies how the destination register is going to be used | DstMode   | Full, Half, Tile | True           |
