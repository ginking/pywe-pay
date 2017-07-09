# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from pywe_pay.base import BaseWeChatPayAPI


class WeChatCoupon(BaseWeChatPayAPI):

    def send(self, openid, stock_id, op_user_id=None, device_info=None, out_trade_no=None):
        """
        发放代金券

        :param openid: 用户在公众号下的 openid
        :param stock_id: 代金券批次 ID
        :param op_user_id: 可选，操作员账号，默认为商户号
        :param device_info: 可选，微信支付分配的终端设备号
        :param out_trade_no: 可选，商户订单号，需保持唯一性，默认自动生成
        :return: 返回的结果信息
        """
        data = {
            'appid': self.appid,
            'coupon_stock_id': stock_id,
            'openid': openid,
            'openid_count': 1,
            'partner_trade_no': out_trade_no or self.out_trade_no(),
            'op_user_id': op_user_id,
            'device_info': device_info,
            'version': '1.0',
            'type': 'XML',
        }
        return self._post('mmpaymkttransfers/send_coupon', data=data)

    def query_stock(self, stock_id, op_user_id=None, device_info=None):
        """
        查询代金券批次

        :param stock_id: 代金券批次 ID
        :param op_user_id: 可选，操作员账号，默认为商户号
        :param device_info: 可选，微信支付分配的终端设备号
        :return: 返回的结果信息
        """
        data = {
            'appid': self.appid,
            'coupon_stock_id': stock_id,
            'op_user_id': op_user_id,
            'device_info': device_info,
            'version': '1.0',
            'type': 'XML',
        }
        return self._post('mmpaymkttransfers/query_coupon_stock', data=data)

    def query_coupon(self, coupon_id, openid, op_user_id=None, device_info=None):
        """
        查询代金券信息

        :param coupon_id: 代金券 ID
        :param openid: 用户在公众号下的 openid
        :param op_user_id: 可选，操作员账号，默认为商户号
        :param device_info: 可选，微信支付分配的终端设备号
        :return: 返回的结果信息
        """
        data = {
            'coupon_id': coupon_id,
            'openid': openid,
            'appid': self.appid,
            'op_user_id': op_user_id,
            'device_info': device_info,
            'version': '1.0',
            'type': 'XML',
        }
        return self._post('promotion/query_coupon', data=data)
