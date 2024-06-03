# noc_semaphore_set_multicast

---
```cpp
inline void noc_semaphore_set_multicast(std::uint32_t src_local_l1_addr, std::uint64_t dst_noc_addr_multicast, std::uint32_t num_dests, bool linked = false, bool multicast_path_reserve = true)inline void noc_semaphore_set_multicast(std::uint32_t src_local_l1_addr, std::uint64_t dst_noc_addr_multicast, std::uint32_t num_dests, bool linked = false, bool multicast_path_reserve = true)
```

Initiates an asynchronous write from a source address in L1 memory on the Tensix core executing this function call to a rectangular destination grid. The destinations are specified using a uint64_t encoding referencing an on-chip grid of nodes located at NOC coordinate range (x_start,y_start,x_end,y_end) and a local address created using *get_noc_multicast_addr* function. The size of data that is sent is 4 Bytes. This is usually used to set a semaphore value at the destination nodes, as a way of a synchronization mechanism. The same as *noc_async_write_multicast* with preset size of 4 Bytes.

Return value: None

| Argument               | Description                                                              | Type      | Valid Range                                                   | Required       |
|------------------------|--------------------------------------------------------------------------|-----------|---------------------------------------------------------------|----------------|
| src_local_l1_addr      | Source address in local L1 memory                                        | uint32_t  | 0..1MB                                                        | True           |
| dst_noc_addr_multicast | Encoding of the destinations nodes (x_start,y_start,x_end,y_end)+address | uint64_t  | DOX-TODO(insert a reference to what constitutes valid coords) | True           |
| num_dests              | Number of destinations that the multicast source is targetting           | uint32_t  | 0..119                                                        | True           |
