#pragma once

#include <string>
#include <list>
#include <vector>

#include <json/json.h>

/*
 * json工具类
 * @author	wq
 * @since	2021/02/22
 * @note	通过 . 路径读取、设置json
			如 :
			{
				"a" : {
					"b" : 1
				}
			}

			setValue("a.b", 1);
*/
class JsonUtil {
public:
	JsonUtil(const std::string &jsonStr = "{}");
	~JsonUtil();

	//
	Json::Value &getRootValue() const { return *m_rootValue; }

	//
	bool setValue(const std::string &path, int value);
	bool setValue(const std::string &path, double value);
	bool setValue(const std::string &path, const std::string &value);

	//
	bool setValue(const std::string &path, const std::list<int> &value);
	bool setValue(const std::string &path, const std::list<double> &value);
	bool setValue(const std::string &path, const std::list<std::string> &value);
	bool setValue(const std::string &path, const std::list<Json::Value> &value);

	//
	bool setValue(const std::string &path, const std::vector<int> &value);
	bool setValue(const std::string &path, const std::vector<double> &value);
	bool setValue(const std::string &path, const std::vector<std::string> &value);
	bool setValue(const std::string &path, const std::vector<Json::Value> &value);

	//
	bool getValue(const std::string &path, int &value);
	bool getValue(const std::string &path, double &value);
	bool getValue(const std::string &path, std::string &value);

	//
	bool getValue(const std::string &path, std::list<int> &value);
	bool getValue(const std::string &path, std::list<double> &value);
	bool getValue(const std::string &path, std::list<std::string> &value);
	bool getValue(const std::string &path, std::list<Json::Value> &value);

	//
	bool getValue(const std::string &path, std::vector<int> &value);
	bool getValue(const std::string &path, std::vector<double> &value);
	bool getValue(const std::string &path, std::vector<std::string> &value);
	bool getValue(const std::string &path, std::vector<Json::Value> &value);

private:
	//
	Json::Value *m_rootValue = 0;
};