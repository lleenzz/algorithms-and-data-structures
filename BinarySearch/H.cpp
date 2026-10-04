#include <iostream>

using namespace std;

bool good(long long m, long long w,long long h, long long n){
	
	return ((m / w) * (m/h) >= n);

}

int main(){
	long long w, h, n;
	
    cin>>w>>h>>n;
    
    long long l = -1;
    long long r = n*max(w,h);
    
    while (r - l > 1){
    	long long m = (r+l)/2;
    	if (good(m,w,h,n)){
    		
    		r = m;
    		
		}
		else{
			l = m;
			
		}
    	
	}
    cout<<r;
    
	return 0;
	
	
}
