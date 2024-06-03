# noc_async_write_multicast

---
```cpp
template<uint32_t max_page_size = NOC_MAX_BURST_SIZE + 1> inline void noc_async_write_multicast(std::uint32_t src_local_l1_addr, std::uint64_t dst_noc_addr_multicast, std::uint32_t size, std::uint32_t num_dests, bool linked = false, bool multicast_path_reserve = true)template<uint32_t max_page_size = NOC_MAX_BURST_SIZE + 1>inline void noc_async_write_multicast(std::uint32_t src_local_l1_addr, std::uint64_t dst_noc_addr_multicast, std::uint32_t size, std::uint32_t num_dests, bool linked = false, bool multicast_path_reserve = true)
```

Initiates an asynchronous write from a source address in L1 memory on the Tensix core executing this function call to a rectangular destination grid. The destinations are specified using a uint64_t encoding referencing an on-chip grid of nodes located at NOC coordinate range (x_start,y_start,x_end,y_end) and a local address created using *get_noc_multicast_addr* function. Also, *see noc_async_write_barrier*.

The destination nodes can only be a set of Tensix cores + L1 memory address. The destination nodes must form a rectangular grid. The destination L1 memory address must be the same on all destination nodes.

With this API, the multicast sender cannot be part of the multicast destinations. If the multicast sender has to be in the multicast destinations (i.e. must perform a local L1 write), the other API variant *noc_async_write_multicast_loopback_src* can be used.

Note: there is no restriction on the number of destinations, i.e. the multicast destinations can span the full chip. However, as mentioned previosuly, the multicast source cannot be part of the destinations. So, the maximum number of destinations is 119.

Return value: None

| Argument               | Description                                                              | Type      | Valid Range                                                   | Required       |
|------------------------|--------------------------------------------------------------------------|-----------|---------------------------------------------------------------|----------------|
| src_local_l1_addr      | Source address in local L1 memory                                        | uint32_t  | 0..1MB                                                        | True           |
| dst_noc_addr_multicast | Encoding of the destinations nodes (x_start,y_start,x_end,y_end)+address | uint64_t  | DOX-TODO(insert a reference to what constitutes valid coords) | True           |
| size                   | Size of data transfer in bytes                                           | uint32_t  | 0..1MB                                                        | True           |
| num_dests              | Number of destinations that the multicast source is targetting           | uint32_t  | 0..119                                                        | True           |
