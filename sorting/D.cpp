#include <iostream>
#include <vector>

using namespace std;

int BubbleSort(vector<int>& A){
	int n = A.size();
	int count = 0;
	for (int i=0; i<n-1; i++){
		for(int j=0; j<n-i-1; j++){
			if (A[j+1]<A[j]){
				swap(A[j+1],A[j]);
				count += 1;
			}
		}
	}
	return count;
}


int main(){
    int x;
    vector<int> A;
    int n;

    cin>>n;

    for (int i=0; i<n; i++){
    	cin>>x;
    	A.push_back(x);
	}

    int c = BubbleSort(A);

	cout<<c;

	return 0;
}

