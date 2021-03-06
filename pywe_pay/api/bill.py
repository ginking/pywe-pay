# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from datetime import date, datetime

from pywe_pay.base import BaseWeChatPayAPI


class WeChatBill(BaseWeChatPayAPI):

    def download_bill(self, bill_date, bill_type='ALL', device_info=None):
        """
        下载对账单

        :param bill_date: 下载对账单的日期
        :param bill_type: 账单类型，ALL，返回当日所有订单信息，默认值
                          SUCCESS，返回当日成功支付的订单,
                          REFUND，返回当日退款订单,
                          REVOKED，已撤销的订单
        :param device_info: 微信支付分配的终端设备号，填写此字段，只下载该设备号的对账单
        :return: 返回的结果数据
        """
        if isinstance(bill_date, (datetime, date)):
            bill_date = bill_date.strftime('%Y%m%d')

        data = {
            'appid': self.appid,
            'bill_date': bill_date,
            'bill_type': bill_type,
            'device_info': device_info,
        }
        return self._post('/pay/downloadbill', data=data)
