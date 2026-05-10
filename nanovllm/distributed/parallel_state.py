from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ParallelState:
    # TODO(distributed): this is the learning entry point for the future
    # DP/PP/TP topology. It should eventually own process groups, local device
    # assignment, and helpers such as is_first_pipeline_stage().
    data_parallel_rank: int = 0
    data_parallel_size: int = 1
    pipeline_parallel_rank: int = 0
    pipeline_parallel_size: int = 1
    tensor_parallel_rank: int = 0
    tensor_parallel_size: int = 1


_PARALLEL_STATE = ParallelState()


def get_parallel_state() -> ParallelState:
    return _PARALLEL_STATE
