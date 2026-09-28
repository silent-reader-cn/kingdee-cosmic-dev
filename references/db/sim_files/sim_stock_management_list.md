# 库存管理-sim_stock_management_list

## 库存管理-主表 t_bdm_tax_equipment

- **表名称：** 库存管理-主表
- **表名：** t_bdm_tax_equipment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_device_is_authorize | f_device_is_authorize | varchar | 50 |  | √ | ' ' |  |
| 3 | ftotalinvoicecount | 发票份数 | int8 | 64 |  | √ | 0 | 发票份数 |
| 4 | fpaperticketquota | fpaperticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | felectpticketquota | felectpticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fdrawer | fdrawer | varchar | 50 |  | √ | ' ' |  |
| 7 | fpayee | fpayee | varchar | 50 |  | √ | ' ' |  |
| 8 | fdefaultequipment | fdefaultequipment | varchar | 10 |  | √ | ' ' |  |
| 9 | felectzticketquota | felectzticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |
| 12 | fdisen | fdisen | varchar | 30 |  | √ | ' ' |  |
| 13 | ffjh | ffjh | varchar | 10 |  |  | ' ' |  |
| 14 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 15 | ftotalsurplus | 剩余发票 | int8 | 64 |  | √ | 0 | 剩余发票 |
| 16 | fticketquota | fticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | ftaxno | ftaxno | varchar | 50 |  | √ | ' ' |  |
| 18 | fauthstatus | 设备状态 | varchar | 2 |  | √ | ' ' | 设备状态,枚举: 0 :未发行 1 :已发行 2 :已注销 3 :发行失败 |
| 19 | freviewer | freviewer | varchar | 50 |  | √ | ' ' |  |
| 20 | fpaperzticketquota | fpaperzticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 21 | fequipmentpwd | fequipmentpwd | varchar | 50 |  | √ | ' ' |  |
| 22 | fmotorticketquota | fmotorticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fequipmentname | 设备名称 | varchar | 50 |  | √ | ' ' | 设备名称 |
| 24 | fdefaultterminal | fdefaultterminal | varchar | 50 |  | √ | ' ' |  |
| 25 | fequipmentno | 虚拟设备号 | varchar | 50 |  | √ | ' ' | 虚拟设备号 |
| 26 | finvoicetypes | finvoicetypes | varchar | 199 |  | √ | ' ' |  |
| 27 | fconntype | fconntype | varchar | 30 |  | √ | ' ' |  |
| 28 | fcabinet | fcabinet | varchar | 50 |  | √ | ' ' |  |
| 29 | fpaperpticketquota | fpaperpticketquota | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | fequipmenttype | 设备类型 | varchar | 30 |  | √ | ' ' | 设备类型,枚举: 0 :税务Ukey 1 :税控盘 2 :金税盘 3 :虚拟Ukey 4 :金税盘-托管 5 :区块链 6 :税控盘-托管 7 :税务ukey-托管 |
| 31 | fpermission | fpermission | int8 | 64 |  | √ | 0 |  |
| 32 | fissuetype | fissuetype | varchar | 30 |  | √ | ' ' |  |
| 33 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 34 | fcombofield | fcombofield | varchar | 30 |  | √ | ' ' |  |
| 35 | fterminalno | fterminalno | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_tax_equipment_dx |  | ftaxno |
| 2 | pk_bdm_tax_equipment |  | fid |
