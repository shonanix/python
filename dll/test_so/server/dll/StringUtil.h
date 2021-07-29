#pragma once

#include <iostream>  
#include <time.h>
#include <stdlib.h> 
#include <string>
#include <vector>

class StringUtil
{
public:
	StringUtil();
	~StringUtil();

	/*
	 * ����ַ���
	*/
	static std::vector<std::string> splitString(const std::string &str, const std::string& delim = ".");

	/*
	* ʱ��ת�ַ���
	*/
	static std::string dateTimeToString(const time_t &time);

	/*
	* �ַ���תʱ��
	*/
	static time_t stringToDateTime(const std::string &str);
};

