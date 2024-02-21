def plot_2d_surface_heatmap(x,y,z):
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt
  
  # Sample data
  # Replace these with your actual data
  data = {
      'X': x,
      'Y': y,
      'Z': z,
  }
  
  # Create a DataFrame
  
  df = pd.DataFrame(data)
  
  # Create a 2D density plot
  sns.set(style="white")
  sns.kdeplot(data=df, x="X", y="Y", fill=True, cmap="Reds", thresh=0, levels=100, weights="Z")
  
  # Set plot labels and title
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.title("2D Density Plot with Z Intensity")
  
  # Show the plot
  plt.show()
