# Circular Buffer APIs

Circular buffers are used for communication between threads of the Tensix core. They act as limited capacity double-ended queues with producers pushing tiles to the back of the queue and consumers popping tiles off the front of the queue.

* [cb_wait_front](cb_wait_front.md)
* [cb_reserve_back](cb_reserve_back.md)
* [cb_push_back](cb_push_back.md)
* [cb_pop_front](cb_pop_front.md)
