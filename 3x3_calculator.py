import numpy as np

def calculate(list):
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []}

    if len(list) == 9:
        arr = np.array(list).reshape(3, 3)

        # Mean for axis0, axis1 and flattened
        arr_mean_axis0 = np.mean(arr, axis=0)
        calculations['mean'].append(arr_mean_axis0.tolist())

        arr_mean_axis1 = np.mean(arr, axis=1)
        calculations['mean'].append(arr_mean_axis1.tolist())

        arr_mean_flat = np.mean(arr)
        calculations['mean'].append(arr_mean_flat.tolist())

        # Variance for axis0, axis1 and flattened
        arr_var_axis0 = np.var(arr, axis=0)
        calculations['variance'].append(arr_var_axis0.tolist())

        arr_var_axis1 = np.var(arr, axis=1)
        calculations['variance'].append(arr_var_axis1.tolist())

        arr_var_flat = np.var(arr)
        calculations['variance'].append(arr_var_flat)

        # Std for axis0, axis1 and flattened
        arr_stdev_axis0 = np.std(arr, axis=0)
        calculations['standard deviation'].append(arr_stdev_axis0.tolist())

        arr_stdev_axis1 = np.std(arr, axis=1)
        calculations['standard deviation'].append(arr_stdev_axis1.tolist())

        arr_stdev_flat = np.std(arr)
        calculations['standard deviation'].append(arr_stdev_flat)

        # Max for axis0, axis1 and flattened
        arr_max_axis0 = np.max(arr, axis=0)
        calculations['max'].append(arr_max_axis0.tolist())

        arr_max_axis1 = np.max(arr, axis=1)
        calculations['max'].append(arr_max_axis1.tolist())

        arr_max_flat = np.max(arr)
        calculations['max'].append(arr_max_flat)

        # Min for axis0, axis1 and flattened
        arr_min_axis0 = np.min(arr, axis=0)
        calculations['min'].append(arr_min_axis0.tolist())

        arr_min_axis1 = np.min(arr, axis=1)
        calculations['min'].append(arr_min_axis1.tolist())

        arr_min_flat = np.min(arr)
        calculations['min'].append(arr_min_flat)

        # Sum for axis0, axis1 and flattened
        arr_min_axis0 = np.sum(arr, axis=0)
        calculations['sum'].append(arr_min_axis0.tolist())

        arr_min_axis1 = np.sum(arr, axis=1)
        calculations['sum'].append(arr_min_axis1.tolist())

        arr_min_flat = np.sum(arr)
        calculations['sum'].append(arr_min_flat)

        return calculations

    else:
        raise ValueError('List must contain nine numbers.')


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])