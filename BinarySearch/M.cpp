#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool good(int m, int N, int K, const vector<int>& A) {
    if (m == 0) {
        return false;
    }
    int c = 0;

    for (int i = 0; i < N; i++) {
        c += A[i] / m;
    }
    return c >= K;
}

int main() {
    int N, K;

    cin >> N >> K;
    vector<int> A;
    int x;
    for (int i = 0; i < N; i++) {
        cin >> x;
        A.push_back(x);
    }

    int l = 0;
    int r = (int)*max_element(A.begin(), A.end()) + 1;

    while (r - l > 1) {
        int m = (r + l) / 2;
        if (good(m, N, K, A)) {
            l = m;
        } else {
            r = m;
        }
    }
    cout << l;

    return 0;
}
