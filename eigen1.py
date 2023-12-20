import numpy as np
num=np.array([[5,4],[1,2]])
eigeen_values=np.linalg.eigvals(num)
print(eigeen_values)
eig_values,eig_vectors=np.linalg.eig(num)
print(f"eigenL_values:{eig_values}  eig_vectors {eig_vectors}")