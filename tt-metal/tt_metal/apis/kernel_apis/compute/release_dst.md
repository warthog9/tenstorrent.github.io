# release_dst

### void ckernel::release_dst(tt::DstMode mode)

Releases the exclusive lock on the internal DST register for the current Tensix core. This lock had to be previously acquired with acquire_dst. This call is blocking and is only available on the compute engine.

Return value: None

DOX-TODO(Describe meanings of dst_mode values).

| Argument      | Description                                                | Type      | Valid Range                                 | Required       |
|---------------|------------------------------------------------------------|-----------|---------------------------------------------|----------------|
| dst_mode      | Specifies how the destination register is going to be used | uint32_t  | DstMode::Full, DstMode::Half, DstMode::Tile | True           |
