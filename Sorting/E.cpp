#include <iostream>
#include <vector>

using namespace std;

vector<int> Merge(vector<int>& left,vector<int>& right){
	vector<int> res;
	int i, j =0;
	while (i<left.size() && j<right.size()){
		if (left[i]<=right[j]){
			res.push_back(left[i]);
			i+=1;
		}
		else{
			res.push_back(right[j]);
			j+=1;

		}

	}

    while (i<left.size()){
    	res.push_back(left[i]);
    	i++;
	}

	while (j<right.size()){
    	res.push_back(right[j]);
    	j++;
	}


	return res;
}

vector<int> MergeSort(vector<int>& A){
	int n = A.size();
	if (n<=1){
	    return A;
	}

	int ind = n / 2;
	vector<int> left(A.begin(), A.begin()+ind);
	vector<int> right(A.begin()+ind, A.end());
	left = MergeSort(left);
	right = MergeSort(right);

	return Merge(left, right);

}



int main(){
	int n;
	int x;
    vector<int> A;
    cin>>n;
    while (n!=0){
    	cin>>x;
    	A.push_back(x);
    	n--;
	}

	A = MergeSort(A);

	for (int i=0; i<A.size(); i++){
    	cout<<A[i]<<" ";
	}

	return 0;

}
