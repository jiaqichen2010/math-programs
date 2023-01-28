#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, d, amount = 0; cin >> n >> d;
	int potatomass[n];
	for (int i = 0; i < n; i++) {
		cin >> potatomass[i];
	}
	sort(potatomass, potatomass + n);
	reverse(potatomass, potatomass + n);
	for(int j = 0; j < d; j++) {
		amount += potatomass[j];
	}
	cout << amount;
	return 0;
}
