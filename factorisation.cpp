#include <bits/stdc++.h>
using namespace std;

int main() {
	long long n; cin >> n;
	long long factor = 2;
	while (factor <= n) {
		if (n % factor == 0) {
			cout << factor << " ";
			n /= factor;
			factor = 1;
		}
		factor += 1;
	}
	return 0;
}
