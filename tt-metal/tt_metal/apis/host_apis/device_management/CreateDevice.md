# CreateDevice

### Device *tt::tt_metal::CreateDevice(chip_id_t device_id, const uint8_t num_hw_cqs = 1, const size_t l1_small_size = DEFAULT_L1_SMALL_SIZE, const std::vector<uint32_t> &l1_bank_remap = {})

Instantiates a device object.

Return value: Device \*

| Argument      | Description                | Type            | Valid Range                       | Required       |
|---------------|----------------------------|-----------------|-----------------------------------|----------------|
| device_id     | ID of the device to target | chip_id_t (int) | 0 to (GetNumAvailableDevices - 1) | Yes            |
