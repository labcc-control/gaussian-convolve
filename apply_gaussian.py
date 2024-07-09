import os
import numpy as np
import matplotlib.pyplot as plt
import argparse


def apply_gaussian(E, F, hw, ei=100.0, ef=600.0, n_points=5001):
    hw2 = hw**2 / 2.7725887
    X = np.linspace(ei, ef, n_points)
    Y = np.zeros(n_points)

    for j in range(len(E)):
        AR = X - E[j]
        ARG = AR**2 / hw2
        EX = np.exp(-ARG)
        Y += F[j] * EX

    return X, Y


def read_data(filename):

    E = []
    F = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Ensure it's not an empty line
                parts = line.split()
                E.append(float(parts[6]))
                F.append(float(line.split('f=')[-1].split()[0]))
    return np.array(E), np.array(F)


def process_files(folder_path, hw, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    data_files = [f for f in os.listdir(folder_path) if f.endswith('.log')]
    aggregate_X = None
    aggregate_Y = None

    for filename in data_files:
        file_path = os.path.join(folder_path, filename)
        E, F = read_data(file_path)
        X, Y = apply_gaussian(E, F, hw)

        if aggregate_X is None:
            aggregate_X = X
            aggregate_Y = Y
        else:
            aggregate_Y += Y

        output_file = os.path.join(output_folder, filename.replace('.log', '.dat'))

        with open(output_file, 'w') as outfile:
            for i in range(len(X)):
                outfile.write(f"    {X[i]:10.5f}  {Y[i]:10.5f}\n")

        plt.figure()
        plt.plot(X, Y, label=f'Gaussian for {filename}')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Intensity')
        plt.title(f'Gaussian Spectrum for {filename}')
        plt.legend()
        plt.savefig(os.path.join(output_folder, filename.replace('.log', '.png')))
        plt.close()

    # Plot aggregate
    plt.figure()
    plt.plot(aggregate_X, aggregate_Y, label='Aggregate Gaussian Spectrum')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.title('Aggregate Gaussian Spectrum')
    plt.legend()
    plt.savefig(os.path.join(output_folder, 'aggregate_spectrum.png'))
    plt.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process Gaussian spectra from a folder of data files.")
    parser.add_argument('--hw', type=float, default=10.0, help='Full Width at Half Maximum (FWHM) for the Gaussian.')
    parser.add_argument('-i', '--input-folder', dest='input_folder', type=str, default='gaussian_data', help='Path to the folder containing the .log files.')
    parser.add_argument('-o', '--output-folder', dest='output_folder', type=str, default='output', help='Folder to save the output .dat and plots.')

    args = parser.parse_args()

    process_files(args.input_folder, args.hw, args.output_folder)