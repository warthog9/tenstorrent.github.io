# cb_reserve_back

### void cb_reserve_back(int32_t operand, int32_t num_pages)

A blocking call that waits for the specified number of tiles to be free in the specified circular buffer. This call is used by the producer to wait for the consumer to consume (ie. free up) the specified number of tiles.

CB total size must be an even multiple of the argument passed to this call.

Return value: None

| Argument      | Description                          | Type      | Valid Range                                                                                       | Required       |
|---------------|--------------------------------------|-----------|---------------------------------------------------------------------------------------------------|----------------|
| cb_id         | The index of the cirular buffer (CB) | uint32_t  | 0 to 31                                                                                           | True           |
| num_tiles     | The number of free tiles to wait for | uint32_t  | It must be less or equal than the size of the CB (the total number of tiles that fit into the CB) | True           |