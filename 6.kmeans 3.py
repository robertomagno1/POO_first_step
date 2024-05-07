"""This file contains an implementation of k-means algorithm
and a number of supporting functions for running the tests.
At the end of this file you can find some commented code lines to run
the elbow method. You can uncomment the code lines to run it."""

import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


#support function
def plot_error_graph_vs_number_of_clusters(data_set, max_number_of_clusters):
    total_errors = np.ndarray(max_number_of_clusters, float)
    print("Creating graph...")
    for i in range(max_number_of_clusters):
        print("Running kmeans with",  i + 1,  "cluster(s)")
        _, _, errors = kmeans(data_set, i + 1, False)
        total_errors[i]=sum(errors)
    print("Completed.")
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.title("Error vs. Number of clusters ")
    plt.plot(range(1, max_number_of_clusters + 1), total_errors, linewidth=3, marker='o')
    ax.set_xlabel(r'Number of clusters', fontsize=14)
    ax.set_ylabel(r'Error', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()


#support function
def plot_data(data_set):
    plt.title("Data set")
    plt.scatter(data_set[:,0], data_set[:,1], alpha=0.5)
    plt.show()


#support function
def plot_data_without_colors(data_set, centroids, iteration):
    plt.title("Data and centroids - Iteration " +str(iteration))
    plt.scatter(data_set[:,0], data_set[:,1], alpha=0.5)
    plt.scatter(centroids[:,0], centroids[:,1], s=150, c=list(range(len(centroids))), edgecolors='black')
    plt.show()


#support function
def plot_data_with_colors(data_set, assigned_centroids, centroids, iteration):
    plt.title("Clusters and centroids - Iteration " +str(iteration))
    plt.scatter(data_set[:,0], data_set[:,1], c=assigned_centroids, alpha=0.5)
    plt.scatter(centroids[:,0], centroids[:,1], s=150, c=list(range(len(centroids))), edgecolors='black')
    plt.show()


#support function
def plot_data_clusters(data_set, assigned_centroids, iteration):
    plt.title("Final clusters - Total iterations " +str(iteration))
    plt.scatter(data_set[:,0], data_set[:,1], c=assigned_centroids, alpha=0.5)
    plt.show()


def calculate_new_centroid_positions(data_set, assigned_centroids, number_of_clusters):
    sum_of_positions = np.zeros([number_of_clusters, 2],float)
    points_per_centroids = np.zeros(number_of_clusters,int)

    #sum all point positions depending on the assigned centroids
    for i in range(len(data_set)):
        sum_of_positions[assigned_centroids[i]]+= data_set[i]  # sum the positions
        points_per_centroids[assigned_centroids[i]] += 1 # count the assigned points for each centroid

    #calculate the average position for each coordinate
    centroid_positions = np.zeros([number_of_clusters, 2], float)
    for i in range(number_of_clusters):
        centroid_positions[i]=sum_of_positions[i]/points_per_centroids[i]

    return centroid_positions


def centroid_assignation(data_set, centroids):
    n = len(data_set)
    assigned_centroids = np.empty(n, dtype=int)
    assignment_errors = np.empty(n, dtype=float)

    for i in range(len(data_set)):
        nearest_centroid = 0
        nearest_centroid_error = np.sqrt(np.sum((centroids[0, :] - data_set[i, :]) ** 2))
        for j in range(1, len(centroids)):
            # error estimation
            error = np.sqrt(np.sum((centroids[j, :] - data_set[i, :]) ** 2))
            if error < nearest_centroid_error:
                nearest_centroid = j
                nearest_centroid_error = error

        assigned_centroids[i]=nearest_centroid
        assignment_errors[i]=nearest_centroid_error

    return assigned_centroids, assignment_errors


def kmeans(data_set, number_of_clusters, max_error=1e-4, plot=False):
    # inizialization
    previous_error = 0
    stop = False
    current_iteration = 0
    centroids = np.empty([number_of_clusters, 2])

    # select random data points as centroids
    i=0
    random_indexes = random.sample(range(0, len(data_set)), number_of_clusters)
    for index in random_indexes:
        centroids[i] = data_set[index]
        i+=1

    if plot:
        plot_data_without_colors(data_set, centroids, current_iteration)

    while True:

        current_iteration += 1

        # assign centroids and calculate the errors
        assigned_centroids, assignment_errors = centroid_assignation(data_set, centroids)

        if plot:
            plot_data_with_colors(data_set, assigned_centroids, centroids,  current_iteration)

        # error check
        total_error = sum(assignment_errors)
        print("Iteration ", current_iteration, ": current error = {0:.6f}".format(total_error),
              "previous error = {0:.6f}".format(previous_error),
              "difference = {0:.6f}".format(abs(previous_error - total_error)))
        if abs(previous_error - total_error) <= max_error:
            break

        previous_error = total_error
        # update centroid position
        centroids = calculate_new_centroid_positions(data_set, assigned_centroids, number_of_clusters)


        if plot:
            plot_data_without_colors(data_set, centroids, current_iteration)

    if plot:
        plot_data_clusters(data_set, assigned_centroids, current_iteration)

    return centroids, assigned_centroids, assignment_errors


# settings
number_of_samples = 1000
number_of_clusters = 5

# create a test dataset
data, true_labels = make_blobs(n_samples=number_of_samples, centers=number_of_clusters, random_state=40, cluster_std=1.3)
# plot dataset
plot_data(data)

# run kmeans
centroids, assignment, errors = kmeans(data, number_of_clusters, plot=True)

# you can uncomment the underlying lines of code to execute the elbow method
max_centroids = 10
plot_error_graph_vs_number_of_clusters(data, min(max_centroids, number_of_samples))
