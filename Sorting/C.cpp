 #include <iostream>
#include <vector>

using namespace std;

void BubbleSort(vector<int>& A){
	int n = A.size();
	for (int i=0; i<n-1; i++){
		for(int j=0; j<n-i-1; j++){
			if (A[j+1]>A[j]){
				swap(A[j+1],A[j]);
			}
		}
	}
}


int main(){
    int x;
    vector<int> A;

    while (cin>>x){
    	A.push_back(x);
	}

    BubbleSort(A);

    for (int i=0; i<A.size(); i++){
    	cout<<A[i]<<" ";
	}

	return 0;
}
