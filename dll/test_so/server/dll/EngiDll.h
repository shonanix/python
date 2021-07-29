#pragma once

//#include "global.h"
#include <map>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <algorithm>

struct BoilerroomData {
	int pid;										// ��Դ�ı�ţ�Ψһ��־
	double currentLoad;								// ��Դ���ܣ���ǰ����
	std::vector<double> requireLoad;				// ��Դ���ܣ����󸺺����У�Ԥ��ֵ
	std::vector<double>		InputFlowsum;				// �����ɢ���¯����������n��ʱ������
	std::vector<double>		targetFlowsum;				// ��������������n��ʱ������
	std::vector<double>		InputLoadsum;				// �����ɢ���¯�ܸ��ɣ���n��ʱ������
	std::vector<double>		targetLoadsum;				// �����ܸ��ɣ���n��ʱ������

	std::vector<int> m_vDataValid;					// ��������Ԥ�����жϺ������״̬
};

struct BoilerData {
	int pid;										// ��¯�ı�ţ�Ψһ��־
	int user_id = 1;									// ĳ��ţ���ʱ��
	double currentLoad;								// ��¯��ǰ����
	std::vector<double> requireLoad;				// ��¯���󸺺����У�Ԥ��ֵ
	std::vector<double>		InputTemp;				// �����ɢ�㹩ˮ�¶ȣ���n��ʱ������
	std::vector<double>		InputTempin;				// �����ɢ���ˮ�¶ȣ���n��ʱ������
	std::vector<double>		InputFlow;				// �����ɢ����������n��ʱ������
	std::vector<double>		InputLoad;				// �����ɢ�㸺�ɣ���n��ʱ������


	double	m_dMaxTempUp;							// �����������
	double	m_dMaxTempDown;							// ���������
	double	m_dMaxFlowUp;							// ��������ɣ���Ҫָ����������
	double	m_dMaxFlowDown;							// ��󽵸��ɣ���Ҫָ����������

	std::vector<int> m_vDataValid;					// ��������Ԥ�����жϺ������״̬

													// ���ɵ�λͳһ��GJ/h������
													// ������
	int m_iForeCount;								// Ԥ���ڵ�ʱ����������һ�β��԰�������6Сʱ��12Сʱ��24Сʱ
	std::vector<double>		targetTemp;				// Ŀ���¶ȣ���n��ʱ������
	std::vector<double>		targetTempin;				// Ŀ���ˮ�¶ȣ���n��ʱ������
	std::vector<double>		targetFlow;				// Ŀ����������n��ʱ������
	std::vector<double>		targetLoad;				// Ŀ�긺�ɣ���n��ʱ�����У���λΪMW


};

struct TempCalcData {
	int pid;
	std::vector<int> pidlist;
	std::vector<std::vector<double>>	value;	// һ������
	int status;									// ����״̬��0Ϊ������-1Ϊ�쳣
};

std::string resultStr;

/*
* @param paramStr:�������json�ַ���
*/
extern "C" char* climateModel(const char *paramStr);
