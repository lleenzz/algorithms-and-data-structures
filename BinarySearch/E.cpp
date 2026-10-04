#include <iostream>
#include <vector>

using namespace std;

bool good(int m, int N, int K,vector<int> A){
	int c = 1;
	int l_k = A[0];
	for (int i = 1; i<N; i++){
		if (l_k+m <= A[i]){
			c++;
			l_k = A[i];
		}
	}
    return c>=K;
}

int main(){
	int N, K;
	
    cin>>N>>K;
    vector<int> A;
    int x;
    for (int i = 0; i<N; i++){
    	cin>>x;
    	A.push_back(x);
	}
    
    int l = -1;
    int r = A[N-1]+1;
    
    while (r - l > 1){
    	int m = (r+l)/2 ;
    	if (good(m,N, K, A)){
    		l = m;
    		
		}
		else{
			r = m;
			
		}
    	
	}
    cout<<l;
    
	return 0;
	
	
}
