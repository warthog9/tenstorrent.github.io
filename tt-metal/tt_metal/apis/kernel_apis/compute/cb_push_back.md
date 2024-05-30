# cb_push_back

```cpp
void ckernel::cb_push_back(uint32_t cbid, uint32_t ntiles)
```

Pushes a given number of tiles in the back of the specified CB’s queue. Decreases the available space in the circular buffer by this number of tiles. This call is used by the producer to make the tiles visible to the consumer of the CB.

We use the convention that the producer pushes tiles into the “back” of the CB queue and the consumer consumes tiles from the “front” of the CB queue.

Note that the act of writing the tile data into the CB does not make the tiles visible to the consumer. Writing of the tiles and pushing is separated to allow the producer to: 1) write the tile data to the CB via multiple writes of sub-tiles 2) modify tiles (or sub-tiles) by random access of the valid section of the CB

Important note: This operation updates the write pointer of the CB, the CB pointer can only be updated from one thread at a time. Example: if compute kernel has cb_push_back(output_id, 1) and reader kernel also has cb_push_back(output_id, 1), these calls will produce non-deterministic behavior because cb pointers are not synchronized across threads. Per circular buffer index, only have one thread push tiles to update the write pointer

Return value: None

| Argument      | Description                          | Type      | Valid Range                                                                                       | Required       |
|---------------|--------------------------------------|-----------|---------------------------------------------------------------------------------------------------|----------------|
| cb_id         | The index of the cirular buffer (CB) | uint32_t  | 0 to 31                                                                                           | True           |
| ntiles        | The number of tiles to be pushed     | uint32_t  | It must be less or equal than the size of the CB (the total number of tiles that fit into the CB) | True           |
