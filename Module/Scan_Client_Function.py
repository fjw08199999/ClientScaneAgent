import wmi


class ScanClientFunction:

    info = wmi.WMI()

    def printCPU(self):

        self.info = wmi.WMI()
        tmpdict = {}
        tmpdict["CpuCores"] = 0

        for cpu in self.Win32_Processor():
            tmpdict["cpuid"] = cpu.ProcessorId.strip()
            tmpdict["CpuType"] = cpu.Name
            tmpdict['systemName'] = cpu.SystemName
            try:
                tmpdict["CpuCores"] = cpu.NumberOfCores
            except:
                tmpdict["CpuCores"] += 1
            tmpdict["CpuClock"] = cpu.MaxClockSpeed
            tmpdict['DataWidth'] = cpu.DataWidth
        print(tmpdict)
        return tmpdict


    def printBIOS(self):
        bioss = []
        for bios_id in self.Win32_BIOS():
            tmpmsg = {}
            tmpmsg['BiosCharacteristics'] = bios_id.BiosCharacteristics  # BIOS特征码
            tmpmsg['version'] = bios_id.Version  # BIOS版本
            tmpmsg['Manufacturer'] = bios_id.Manufacturer.strip()  # BIOS固件生产厂家
            tmpmsg['ReleaseDate'] = bios_id.ReleaseDate  # BIOS释放日期
            tmpmsg['SMBIOSBIOSVersion'] = bios_id.SMBIOSBIOSVersion  # 系统管理规范版本
            bioss.append(tmpmsg)
        print(bioss)
        return bioss


    def printDisk(self):
        disks = []
        for disk in self.Win32_DiskDrive():
            # print disk.__dict__
            tmpmsg = {}
            tmpmsg['SerialNumber'] = disk.SerialNumber.strip()
            tmpmsg['DeviceID'] = disk.DeviceID
            tmpmsg['Caption'] = disk.Caption
            tmpmsg['Size'] = disk.Size
            tmpmsg['UUID'] = disk.qualifiers['UUID'][1:-1]
            disks.append(tmpmsg)
        for d in disks:
            print(d)
        return disks


    def printPhysicalMemory(self):
        memorys = []
        for mem in self.Win32_PhysicalMemory():
            tmpmsg = {}
            tmpmsg['UUID'] = mem.qualifiers['UUID'][1:-1]
            tmpmsg['BankLabel'] = mem.BankLabel
            tmpmsg['SerialNumber'] = mem.SerialNumber.strip()
            # tmpmsg['ConfiguredClockSpeed'] = mem.ConfiguredClockSpeed
            tmpmsg['Capacity'] = mem.Capacity
            # tmpmsg['ConfiguredVoltage'] = mem.ConfiguredVoltage
            memorys.append(tmpmsg)
        for m in memorys:
            print(m)
        return memorys


    def printMacAddress(self):
        macs = []
        for n in self.Win32_NetworkAdapter():
            mactmp = n.MACAddress
            if mactmp and len(mactmp.strip()) > 5:
                tmpmsg = {}

                tmpmsg['MACAddress'] = n.MACAddress
                tmpmsg['Name'] = n.Name
                tmpmsg['DeviceID'] = n.DeviceID
                tmpmsg['AdapterType'] = n.AdapterType
                tmpmsg['Speed'] = n.Speed
                macs.append(tmpmsg)
        print(macs)
        return macs


    def printBattery(self):
        isBatterys = False
        for battery in self.Win32_Battery():
            isBatterys = True

        print(battery)
        return isBatterys
