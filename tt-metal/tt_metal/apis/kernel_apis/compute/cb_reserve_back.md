# cb_reserve_back

```cpp
void ckernel::cb_reserve_back(uint32_t cbid, uint32_t ntiles)
```

A blocking call that waits for the specified number of tiles to be free in the specified circular buffer. This call is used by the producer to wait for the consumer to consume (ie. free up) the specified number of tiles.

CB total size must be an even multiple of the argument passed to this call.

Return value: None

| Argument      | Description                          | Type      | Valid Range                                                                                       | Required       |
|---------------|--------------------------------------|-----------|---------------------------------------------------------------------------------------------------|----------------|
| cb_id         | The index of the cirular buffer (CB) | uint32_t  | 0 to 31                                                                                           | True           |
| ntiles        | The number of free tiles to wait for | uint32_t  | It must be less or equal than the size of the CB (the total number of tiles that fit into the CB) | True           |
