class DataParallelRouter:
    # TODO(data-parallel): first implement request-level offline sharding here.
    # Each replica should own an independent LLMEngine, Scheduler, BlockManager,
    # and KV cache; the router only assigns requests and merges outputs.
    pass
