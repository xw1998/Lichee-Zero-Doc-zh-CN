# coding: utf-8

#----------------  Conver timestamp  2018-02-17 14:15:55  ---------------#

writer.header_list = ['分区序号', '分区大小', '分区作用', '地址空间及分区名']

writer.value_matrix = [
	['mtd0', '1MB', 'spl+uboot', '0x0000000-0x0100000:"uboot"'],
	['mtd1', '64KB', 'dtb文件', '0x0100000-0x0110000:"dtb"'],
	['mtd2', '4MB', 'linux内核', '0x0110000-0x0510000:"kernel"'],
	['mtd3', '剩余', '根文件系统', '0x0510000-0x2000000:"rootfs"'],
]
