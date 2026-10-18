#include <iostream>

using namespace std;

bool good(long long m, long long x,long long y, long long N){
	if (m < min(x, y)) {
        return false;
    }
	m = m - min(x,y);
	return (m/x+m/y >= N-1);

}

int main(){
	long long N, x, y;
	
    cin>>N>>x>>y;
    
    long long l = -1;
    long long r = N*min(x,y);
    
    while (r - l > 1){
    	long long m = (r+l)/2 ;
    	if (good(m,x,y,N)){
    		
    		r = m;
    		
		}
		else{
			l = m;
			
		}
    	
	}
    cout<<r;
    
	return 0;
	
	
}
