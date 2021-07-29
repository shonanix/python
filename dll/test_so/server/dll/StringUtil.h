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
	 * 拆分字符串
	*/
	static std::vector<std::string> splitString(const std::string &str, const std::string& delim = ".");

	/*
	* 时间转字符串
	*/
	static std::string dateTimeToString(const time_t &time);

	/*
	* 字符串转时间
	*/
	static time_t stringToDateTime(const std::string &str);
};

