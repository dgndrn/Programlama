
#include"lib.h"


int main()
{
	int secim, veri;
	cout << "1 Heksadesimal\n2 Oktal\n3 Binary\n";
	cin >> secim;

	cout << "Sayi giriniz:";
	cin >> veri;
	switch (secim) {

	case 1:
		cout << ToHex(veri);

		break;
	case 2:
		cout << ToOctal(veri);
		break;
	case 3:
		cout << ToBinary(veri);
		break;

	}



}

