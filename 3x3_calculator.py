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
        calculations['mean'].append(arr_mean_axis0)

        arr_mean_axis1 = np.mean(arr, axis=1)
        calculations['mean'].append(arr_mean_axis1)

        arr_mean_flat = np.mean(arr)
        calculations['mean'].append(arr_mean_flat)

        # calculations['mean'] = np.array(calculations['mean']).tolist()

        # Variance for axis0, axis1 and flattened
        arr_var_axis0 = np.var(arr, axis=0)
        calculations['variance'].append(arr_var_axis0)

        arr_var_axis1 = np.var(arr, axis=1)
        calculations['variance'].append(arr_var_axis1)

        arr_var_flat = np.var(arr)
        calculations['variance'].append(arr_var_flat)

        # calculations['variance'] = np.array(calculations['variance']).tolist()

        # Std for axis0, axis1 and flattened
        arr_stdev_axis0 = np.std(arr, axis=0)
        calculations['standard deviation'].append(arr_stdev_axis0)

        arr_stdev_axis1 = np.std(arr, axis=1)
        calculations['standard deviation'].append(arr_stdev_axis1)

        arr_stdev_flat = np.std(arr)
        calculations['standard deviation'].append(arr_stdev_flat)

        # calculations['standard deviation'] = np.array(calculations['standard deviation']).tolist()

        # Max for axis0, axis1 and flattened
        arr_max_axis0 = np.max(arr, axis=0)
        calculations['max'].append(arr_max_axis0)

        arr_max_axis1 = np.max(arr, axis=1)
        calculations['max'].append(arr_max_axis1)

        arr_max_flat = np.max(arr)
        calculations['max'].append(arr_max_flat)

        # calculations['max'] = np.array(calculations['max']).tolist()

        # Min for axis0, axis1 and flattened
        arr_min_axis0 = np.min(arr, axis=0)
        calculations['min'].append(arr_min_axis0)

        arr_min_axis1 = np.min(arr, axis=1)
        calculations['min'].append(arr_min_axis1)

        arr_min_flat = np.min(arr)
        calculations['min'].append(arr_min_flat)

        # calculations['min'] = np.array(calculations['min']).tolist()

        # Sum for axis0, axis1 and flattened
        arr_min_axis0 = np.sum(arr, axis=0)
        calculations['sum'].append(arr_min_axis0)

        arr_min_axis1 = np.sum(arr, axis=1)
        calculations['sum'].append(arr_min_axis1)

        arr_min_flat = np.sum(arr)
        calculations['sum'].append(arr_min_flat)

        # calculations['sum'] = np.array(calculations['sum']).tolist()

        # calculations = np.array(calculations['sum']).tolist()

        #return calculations
        print(calculations)

    else:
        print("List must contain nine numbers.")


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
# https://forum.freecodecamp.org/t/data-analysis-with-python-projects-mean-variance-standard-deviation-calculator/409025
