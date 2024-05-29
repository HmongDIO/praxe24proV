//============================================================================
// Name        : zajac_test4.cpp
// Author      : Zajac
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

double pole(double pole[6]);
bool basketbal(double vyska);
void hodnoceni(int znamka);
double median(double pole1[]);

int main() {


}

double pole(double pole[6]){
	int max=0;
	int min=100000;
	double prumer;
	for(int i=0;i<6;i++){
		if(pole[i]<min){
			min=pole[i];
		}
		else if(pole[i]>max){
			max=pole[i];
		}
	}
	prumer = (max+min)/2;
	return prumer;
}

bool basketbal(double vyska){
	bool vysledek;
	if(vyska>190){
		vysledek=true;
	}
	else{
		vysledek=false;
	}
	return vysledek;
}

void hodnoceni(int znamka){
	switch(znamka){
	case 1:
		cout<<"vyborny"<<endl;
		break;
	case 2:
		cout<<"chvalitebny"<<endl;
		break;
	case 3:
		cout<<"dobry"<<endl;
		break;
	case 4:
		cout<<"dostatecny"<<endl;
		break;
	case 5:
		cout<<"nedostatecny"<<endl;
		break;
	defalut:
		cout<<"spatna hodnota"<<endl;
	}
}

double median(double pole1){
	float arr.size();
	float m;
	float m2;
	if(pocet % 2==1){
		m=pocet/2;
		return m;
	}
	else{
		m=pocet/2-1;
		m2=pocet/2+1;
		double pole[]={m,m2};
		return pole[1];
	}
}








