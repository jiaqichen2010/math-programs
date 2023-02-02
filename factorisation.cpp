#include <bits/stdc++.h>
using namespace std;

int main() {
	long long n; cin >> n;
	long long factor = 2;
	while (n % 2 == 0) {
		n /= factor;
	}
	factor += 1;
	while (factor <= n) {
		if (factor > floor(sqrt(n))) {
			cout << n;
			break;
		}
		if (n % factor == 0) {
			cout << factor << " ";
			n /= factor;
			factor -= 2;
		}
		factor += 2;
			
	}
	return 0;
}
