#include <iostream>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& A){
	int n = A.size();
	for (int i=0; i<n-1; i++){
		int m_ind = i;
		for (int j=i+1; j<n; j++){
			if(A[j]>A[m_ind]){
				m_ind = j;
			}

		}
		if (i != m_ind){
			swap(A[i], A[m_ind]);
		}

	}

}

int main(){
	int x;
    vector<int> A;

    while (cin>>x){
    	A.push_back(x);
	}

	SelectionSort(A);

	for (int i=0; i<A.size(); i++){
    	cout<<A[i]<<" ";
	}

	return 0;

}
