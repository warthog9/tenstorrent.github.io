# noc_async_write

---
```cpp
template<uint32_t max_page_size = NOC_MAX_BURST_SIZE + 1> inline void noc_async_write(std::uint32_t src_local_l1_addr, std::uint64_t dst_noc_addr, std::uint32_t size)template<uint32_t max_page_size = NOC_MAX_BURST_SIZE + 1>inline void noc_async_write(std::uint32_t src_local_l1_addr, std::uint64_t dst_noc_addr, std::uint32_t size)
```

Initiates an asynchronous write from a source address in L1 memory on the Tensix core executing this function call. The destination is specified using a uint64_t encoding referencing an on-chip node located at NOC coordinates (x,y) and a local address created using get_noc_addr function. Also, see *noc_async_write_barrier*.

The destination node can be either a DRAM bank, Tensix core+L1 memory address or a PCIe controller.

Return value: None

| Argument          | Description                                             | Type      | Valid Range                                                   | Required       |
|-------------------|---------------------------------------------------------|-----------|---------------------------------------------------------------|----------------|
| src_local_l1_addr | Source address in local L1 memory                       | uint32_t  | 0..1MB                                                        | True           |
| dst_noc_addr      | Encoding of the destination DRAM location (x,y)+address | uint64_t  | DOX-TODO(insert a reference to what constitutes valid coords) | True           |
| size              | Size of data transfer in bytes                          | uint32_t  | 0..1MB                                                        | True           |
