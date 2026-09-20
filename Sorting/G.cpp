#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int>& A){
  int k = A[0];

  for (int i = 1; i < A.size(); i++) {
    if (A[i] > k) {
        k = A[i];
    }
  }

  vector<int> counter(k+1, 0);

  for (int i=0; i<A.size();i++){
  	counter[A[i]] += 1;
  }


  int j = 0;
  for (int i=0; i<k+1;i++){
  	while (counter[i] > 0){
  		A[j] = i;
  		j++;
  		counter[i]--;
	  }
  }




}

int main(){
	int x;
    vector<int> A;

    while (cin>>x){
    	A.push_back(x);
	}

	CountSort(A);

	for (int i=0; i<A.size(); i++){
    	cout<<A[i]<<" ";
	}

	return 0;

}
