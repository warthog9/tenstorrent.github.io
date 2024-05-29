# noc_async_read

### inline void noc_async_read(std::uint64_t src_noc_addr, std::uint32_t dst_local_l1_addr, std::uint32_t size)

Initiates an asynchronous read from a specified source node located at NOC coordinates (x,y) at a local address (encoded as a uint64_t using *get_noc_addr* function). The destination is in L1 memory on the Tensix core executing this function call. Also, see *noc_async_read_barrier*.

The source node can be either a DRAM bank, a Tensix core or a PCIe controller.

Return value: None

| Argument          | Description                                        | Data type      | Valid range                           | required       |
|-------------------|----------------------------------------------------|----------------|---------------------------------------|----------------|
| src_noc_addr      | Encoding of the source DRAM location (x,y)+address | uint64_t       | DOX-TODO(ref to explain valid coords) | Yes            |
| dst_local_l1_addr | Address in local L1 memory                         | uint32_t       | 0..1MB                                | Yes            |
| size              | Size of data transfer in bytes                     | uint32_t       | 0..1MB                                | Yes            |
