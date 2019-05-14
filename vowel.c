#include<stdio.h>
int main()
{
	char c;
	int isLowercaseVowel,isUppercaseVowel;
	printf("Enter an alphabet:");
	scanf("%c",&c);
	if(isLowercaseVowel||isUppercaseVowel)
	printf("%c is a vowel",c);
	else
	printf("%c is a consonent",c);
	return 0;
}
	
