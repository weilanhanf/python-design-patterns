#!/user/bin/env python
# -*- coding: utf-8 -*-


class ACpnStaff:
    """
    A公司
    """
    name=""
    id=""
    phone=""
    def __init__(self,id):
        self.id=id
    def getName(self):
        print("A protocol getName method...id:%s"%self.id)
        return self.name
    def setName(self,name):
        print("A protocol setName method...id:%s"%self.id)
        self.name=name
    def getPhone(self):
        print("A protocol getPhone method...id:%s"%self.id)
        return self.phone
    def setPhone(self,phone):
        print("A protocol setPhone method...id:%s"%self.id)
        self.phone=phone

class BCpnStaff:
    """
    公司
    """
    name=""
    id=""
    telephone=""
    def __init__(self,id):
        self.id=id
    def get_name(self):
        print("B protocol get_name method...id:%s"%self.id)
        return self.name
    def set_name(self,name):
        print("B protocol set_name method...id:%s"%self.id)
        self.name=name
    def get_telephone(self):
        print("B protocol get_telephone method...id:%s"%self.id)
        return self.telephone
    def set_telephone(self,telephone):
        print("B protocol get_name method...id:%s"%self.id)
        self.telephone=telephone

class CpnStaffAdapter:
    """
    C公司
    """
    b_cpn=""
    def __init__(self,id):
        self.b_cpn=BCpnStaff(id)
    def getName(self):
        return self.b_cpn.get_name()
    def getPhone(self):
        return self.b_cpn.get_telephone()
    def setName(self,name):
        self.b_cpn.set_name(name)
    def setPhone(self,phone):
        self.b_cpn.set_telephone(phone)

#业务场景
if __name__=="__main__":
    acpn_staff=ACpnStaff("123")
    acpn_staff.setName("X-A")
    acpn_staff.setPhone("10012345678")
    print("A Staff Name:%s"%acpn_staff.getName())
    print("A Staff Phone:%s"%acpn_staff.getPhone())
    bcpn_staff=CpnStaffAdapter("456")
    bcpn_staff.setName("Y-B")
    bcpn_staff.setPhone("99987654321")
    print("B Staff Name:%s"%bcpn_staff.getName())
    print("B Staff Phone:%s"%bcpn_staff.getPhone())