def find_max(arr,i):
  """
  Find the max element in a array
  """
  max = arr[0]
  max_index = 0

  for index in range(arr.shape[0]):
    if arr[index] > max:
      max = arr[index]
      max_index = index
  
  return max_index + i

def LUGAUSS(B):
  A = B.copy()
  A = A.astype(np.float)
  if A.shape[0] != A.shape[1]:
    return "Invalid Matrix. A must be a square marix."
  L = np.eye(A.shape[0])
  P = np.eye(A.shape[0])

  for i in range(A.shape[0]):

    max_index = find_max(A[i:,i],i)
    print(max_index)

    if max_index != i:
      tmp = A[i,i:]
      A[i,i:] = A[max_index,i:]
      A[max_index,i:] = tmp


      tmp = P[i,:]
      P[i,:] = P[max_index,:]
      P[max_index,:] = tmp

      tmp = L[i,:i-1]
      L[i,:i-1] = L[max_index,:i-1]
      L[max_index,:i-1] = tmp
    
    multipliers = A[i+1:,i] / A[i,i]
    
    A[i+1:,i+1:] = A[i+1:,i+1:] -  np.outer(multipliers, A[i,i+1:])
    A[i+1:,i] = 0
    L[i+1:,i] = multipliers
    

  U = A

  return (L,U)