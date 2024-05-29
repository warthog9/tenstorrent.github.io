# cb_pop_front

### void ckernel::cb_pop_front(uint32_t cbid, uint32_t ntiles)

Pops a specified number of tiles from the front of the specified CB. This also frees this number of tiles in the circular buffer. This call is used by the consumer to free up the space in the CB.

We use the convention that the producer pushes tiles into the “back” of the CB queue and the consumer consumes tiles from the “front” of the CB queue.

Note that the act of reading of the tile data from the CB does not free up the space in the CB. Waiting on available tiles and popping them is separated in order to allow the consumer to: 1) read the tile data from the CB via multiple reads of sub-tiles 2) access the tiles (or their sub-tiles) that are visible to the consumer by random access of the valid section of the CB

Important note: This operation updates the read pointer of the CB, the CB pointer can only be updated from one thread at a time. Example: if compute kernel has cb_pop_front(input_id, 1) and writer kernel also has cb_pop_front(input_id, 1), these calls will produce non-deterministic behavior because cb pointers are not synchronized across threads. Per circular buffer index, only have one thread pop tiles to update the read pointer

Return value: None

| Argument      | Description                          | Type      | Valid Range                                                                                       | Required       |
|---------------|--------------------------------------|-----------|---------------------------------------------------------------------------------------------------|----------------|
| cb_id         | The index of the cirular buffer (CB) | uint32_t  | 0 to 31                                                                                           | True           |
| ntiles        | The number of tiles to be popped     | uint32_t  | It must be less or equal than the size of the CB (the total number of tiles that fit into the CB) | True           |
