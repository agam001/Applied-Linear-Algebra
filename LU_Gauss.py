def LUGAUSS(A):
  A = A.astype(np.float)
  if A.shape[0] != A.shape[1]:
    return "Invalid Matrix. A must be a square marix."

  multipliers = dict()
  for i in range(A.shape[0]):
  
    if A[i,i] == 0:
      return "Pivot is zero"
    else:
      multipliers[(i+1,i)] = A[i+1:,i] / A[i,i]
      A[i+1:,i] =  multipliers[(i+1,i)]
      A[i+1:,i+1:] = A[i+1:,i+1:] -  A[i+1:,i].reshape(-1,1) * A[i,i+1:].reshape(1,-1)

    
  L = np.eye(A.shape[0])
  for x in range(L.shape[1]):
    L[x+1:,x] = multipliers[(x+1,x)]

  U = A.copy()
  for x in range(U.shape[1]):
    U[x+1:,x] = 0 

  return (L,U)