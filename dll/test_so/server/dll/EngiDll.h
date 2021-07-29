#pragma once

//#include "global.h"
#include <map>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <algorithm>

struct BoilerroomData {
	int pid;										// 热源的编号，唯一标志
	double currentLoad;								// 热源（总）当前负荷
	std::vector<double> requireLoad;				// 热源（总）需求负荷序列，预测值
	std::vector<double>		InputFlowsum;				// 输入的散点锅炉总流量，分n个时间序列
	std::vector<double>		targetFlowsum;				// 计算总流量，分n个时间序列
	std::vector<double>		InputLoadsum;				// 输入的散点锅炉总负荷，分n个时间序列
	std::vector<double>		targetLoadsum;				// 计算总负荷，分n个时间序列

	std::vector<int> m_vDataValid;					// 经过数据预处理判断后的数据状态
};

struct BoilerData {
	int pid;										// 锅炉的编号，唯一标志
	int user_id = 1;									// 某编号，临时用
	double currentLoad;								// 锅炉当前负荷
	std::vector<double> requireLoad;				// 锅炉需求负荷序列，预测值
	std::vector<double>		InputTemp;				// 输入的散点供水温度，分n个时间序列
	std::vector<double>		InputTempin;				// 输入的散点回水温度，分n个时间序列
	std::vector<double>		InputFlow;				// 输入的散点流量，分n个时间序列
	std::vector<double>		InputLoad;				// 输入的散点负荷，分n个时间序列


	double	m_dMaxTempUp;							// 最大升温速率
	double	m_dMaxTempDown;							// 最大降温速率
	double	m_dMaxFlowUp;							// 最大升负荷（主要指流量）速率
	double	m_dMaxFlowDown;							// 最大降负荷（主要指流量）速率

	std::vector<int> m_vDataValid;					// 经过数据预处理判断后的数据状态

													// 负荷单位统一成GJ/h！！！
													// 输出结果
	int m_iForeCount;								// 预调节的时段数量，出一次策略包含将来6小时、12小时、24小时
	std::vector<double>		targetTemp;				// 目标温度，分n个时间序列
	std::vector<double>		targetTempin;				// 目标回水温度，分n个时间序列
	std::vector<double>		targetFlow;				// 目标流量，分n个时间序列
	std::vector<double>		targetLoad;				// 目标负荷，分n个时间序列，单位为MW


};

struct TempCalcData {
	int pid;
	std::vector<int> pidlist;
	std::vector<std::vector<double>>	value;	// 一组数据
	int status;									// 数据状态，0为正常，-1为异常
};

std::string resultStr;

/*
* @param paramStr:输入参数json字符串
*/
extern "C" char* climateModel(const char *paramStr);
