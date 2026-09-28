# 开票设备-bdm_tax_equipment

## 终端单据体-子表 t_bdm_terminal

- **表名称：** 终端单据体-子表
- **表名：** t_bdm_terminal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 开票终端名称 | varchar | 50 |  | √ | ' ' | 开票终端名称 |
| 3 | fsurpluscount | 剩余份数 | int8 | 64 |  | √ | 0 | 剩余份数 |
| 4 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 004 :纸质增值税专用发票 005 :机动车销售统一发票 006 :二手车销售统一发票 007 :增值税普通发票（纸票） 025 :增值税普通发票（卷票） 026 :增值税电子普通发票 028 :增值税电子专用发票 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | finvoicecount | 发票份数 | int8 | 64 |  | √ | 0 | 发票份数 |
| 7 | fterminalcode | 开票终端代码 | varchar | 50 |  | √ | ' ' | 开票终端代码 |
| 8 | foncebuylimit | 每次购票限额 | int8 | 64 |  | √ | 0 | 每次购票限额 |
| 9 | fmaxcount | 最高持票量 | int8 | 64 |  | √ | 0 | 最高持票量 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmonthbuylimit | 每月购票限额 | int8 | 64 |  | √ | 0 | 每月购票限额 |
| 12 | fdevno | 虚拟设备号 | varchar | 50 |  | √ | ' ' | 虚拟设备号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_terminal_fk |  | fid |
| 2 | pk_bdm_terminal |  | fentryid |

---

## 开票设备-主表 t_bdm_tax_equipment

- **表名称：** 开票设备-主表
- **表名：** t_bdm_tax_equipment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_device_is_authorize | f_device_is_authorize | varchar | 50 |  | √ | ' ' |  |
| 3 | ftotalinvoicecount | 发票份数 | int8 | 64 |  | √ | 0 | 发票份数 |
| 4 | fpaperticketquota | fpaperticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | felectpticketquota | 电子普票限额 | numeric | 23 | 10 | √ | 0.0000000000 | 电子普票限额 |
| 6 | fdrawer | 设备开票人 | varchar | 50 |  | √ | ' ' | 设备开票人 |
| 7 | fpayee | 设备收款人 | varchar | 50 |  | √ | ' ' | 设备收款人 |
| 8 | fdefaultequipment | 默认开票设备 | varchar | 10 |  | √ | ' ' | 默认开票设备,枚举: 0 :否 1 :是 |
| 9 | felectzticketquota | 电子专票限额 | numeric | 23 | 10 | √ | 0.0000000000 | 电子专票限额 |
| 10 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 11 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |
| 12 | fdisen | 启用/禁用 | varchar | 30 |  | √ | ' ' | 启用/禁用,枚举: 1 :启用 0 :禁用 |
| 13 | ffjh | 分机号 | varchar | 10 |  |  | ' ' | 分机号 |
| 14 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 15 | ftotalsurplus | 剩余发票 | int8 | 64 |  | √ | 0 | 剩余发票 |
| 16 | fticketquota | 卷票限额 | numeric | 23 | 10 | √ | 0.0000000000 | 卷票限额 |
| 17 | ftaxno | ftaxno | varchar | 50 |  | √ | ' ' |  |
| 18 | fauthstatus | 激活状态 | varchar | 2 |  | √ | ' ' | 激活状态,枚举: 0 :未激活 1 :已激活 2 :激活中 3 :激活失败 |
| 19 | freviewer | 设备复核人 | varchar | 50 |  | √ | ' ' | 设备复核人 |
| 20 | fpaperzticketquota | 纸质专票限额 | numeric | 23 | 10 | √ | 0.0000000000 | 纸质专票限额 |
| 21 | fequipmentpwd | 设备密码 | varchar | 50 |  | √ | ' ' | 设备密码 |
| 22 | fmotorticketquota | 机动车发票限额 | numeric | 23 | 10 | √ | 0.0000000000 | 机动车发票限额 |
| 23 | fequipmentname | 设备名称 | varchar | 50 |  | √ | ' ' | 设备名称 |
| 24 | fdefaultterminal | 默认开票终端 | varchar | 50 |  | √ | ' ' | 默认开票终端,枚举: 0 :否 1 :是 |
| 25 | fequipmentno | 设备编号 | varchar | 50 |  | √ | ' ' | 设备编号 |
| 26 | finvoicetypes | 允许发票种类 | varchar | 199 |  | √ | ' ' | 允许发票种类 |
| 27 | fconntype | 连接类型 | varchar | 30 |  | √ | ' ' | 连接类型,枚举: 0 :本地连接 1 :长连接 |
| 28 | fcabinet | 托管机柜 | varchar | 50 |  | √ | ' ' | 托管机柜,枚举: |
| 29 | fpaperpticketquota | 纸质普票限额 | numeric | 23 | 10 | √ | 0.0000000000 | 纸质普票限额 |
| 30 | fequipmenttype | 设备类型 | varchar | 30 |  | √ | ' ' | 设备类型,枚举: 0 :税务Ukey 1 :税控盘 2 :金税盘 3 :虚拟Ukey 4 :金税盘-托管 5 :区块链 6 :税控盘-托管 7 :税务ukey-托管 8 :百望服务器 9 :联云托管金税盘 10 :联云托管税务ukey 11 :联云托管税控盘 |
| 31 | fpermission | 授权id | int8 | 64 |  | √ | 0 | 授权id |
| 32 | fissuetype | 开票方式 | varchar | 30 |  | √ | ' ' | 开票方式,枚举: 0 :本地Ukey 1 :盘托管 2 :虚拟Ukey |
| 33 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 34 | fcombofield | fcombofield | varchar | 30 |  | √ | ' ' |  |
| 35 | fterminalno | 终端编号 | varchar | 50 |  | √ | ' ' | 终端编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_tax_equipment_dx |  | ftaxno |
| 2 | pk_bdm_tax_equipment |  | fid |
