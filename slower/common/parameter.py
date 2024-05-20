from flwr.common import ndarray_to_bytes, bytes_to_ndarray


def ndarray_dict_to_bytes(ndarray_dict):
    return {
        key: [ndarray_to_bytes(v) for v in val] if isinstance(val, list) else ndarray_to_bytes(val)
        for key, val in ndarray_dict.items()
    }


def bytes_to_ndarray_dict(bytes_dict):
    return {
        key: [bytes_to_ndarray(v) for v in val] if isinstance(val, list) else bytes_to_ndarray(val)
        for key, val in bytes_dict.items()
    }
