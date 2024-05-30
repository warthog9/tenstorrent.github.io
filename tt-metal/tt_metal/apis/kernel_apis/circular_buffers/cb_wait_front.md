# cb_wait_front

```cpp
void cb_wait_front(int32_t operand, int32_t num_pages)
```

A blocking call that waits for the specified number of tiles to be available in the specified circular buffer (CB). This call is used by the consumer of the CB to wait for the producer to fill the CB with at least the specfied number of tiles. Important note: in case multiple calls of cb_wait_front(n) are issued without a paired [cb_pop_front()](cb_pop_front.md#dataflow__api_8h_1aa3daf8e5e7299140cf2607be1a8656b0) call, n is expected to be incremented by the user to be equal to a cumulative total of tiles. Example: 4 calls of cb_wait_front(8) followed by a cb_pop_front(32) would produce incorrect behavior. Instead 4 calls of [cb_wait_front()](#dataflow__api_8h_1af6d8057bd05a650c3501c5208f7d9f8a) waiting on 8, 16, 24, 32 tiles should be issued.

Important note: number of tiles used in all cb_\* calls must evenly divide the cb size and must be the same number in all cb_wait_front calls in the same kernel. Example 1: cb_wait_front(32), cb_wait_front(40), cb_pop_front(32+8) tiles on a CB of size 64 would produce incorrect behavior. Example 2: cb_wait_front(3) on a cb of size 32 would also produce incorrect behavior. These limitations are due to performance optimizations in the CB implementation.

Important note: CB total size must be an even multiple of the argument passed to this call.

Return value: None

| Argument      | Description                          | Type      | Valid Range                                                                                       | Required       |
|---------------|--------------------------------------|-----------|---------------------------------------------------------------------------------------------------|----------------|
| cb_id         | The index of the cirular buffer (CB) | uint32_t  | 0 to 31                                                                                           | True           |
| num_tiles     | The number of tiles to wait for      | uint32_t  | It must be less or equal than the size of the CB (the total number of tiles that fit into the CB) |                |
