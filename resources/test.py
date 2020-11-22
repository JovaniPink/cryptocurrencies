# Create an elbow curve to find the best value for K.
inertia = []
k = list(range(1, 11))

for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(df_crypto_scaled_pca)
    inertia.append(km.inertia_)

elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)
df_elbow.hvplot.line(
    x="k",
    y="inertia",
    xticks=k,
    title="Elbow Visualization",
    xlabel="Number of Clusters",
    ylabel="Inertia",
)