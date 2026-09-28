# 许可授权-bdm_invoice_permission

## 许可授权-主表 t_bdm_invoice_permission

- **表名称：** 许可授权-主表
- **表名：** t_bdm_invoice_permission

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fequipment | 设备(弃用，误删) | int8 | 64 |  | √ | 0 | [开票设备 bdm_tax_equipment](../bdm_files/bdm_tax_equipment.md) |
| 3 | fresulturl | 授权文件地址 | varchar | 100 |  | √ | ' ' | 授权文件地址 |
| 4 | fequipmentno | fequipmentno | varchar | 100 |  | √ | ' ' |  |
| 5 | forgid | 机构信息 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fregistercode | 注册码 | varchar | 500 |  | √ | ' ' | 注册码 |
| 7 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |
| 8 | fequipmenttype | 设备类型 | varchar | 60 |  | √ | ' ' | 设备类型,枚举: 0 :税务Ukey 1 :税控盘 2 :金税盘 3 :虚拟UKey 4 :金税盘-托管 5 :区块链 6 :税控盘-托管 7 :税务ukey-托管 8 :百旺服务器 9 :联云托管-金税盘(航信) 10 :联云托管-UKey 11 :联云托管-税控盘(百旺) |
| 9 | fvalidendtime | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 10 | fdevcount | 设备数量 | int8 | 64 |  | √ | 0 | 设备数量 |
| 11 | fauthstate | 授权状态 | varchar | 4 |  | √ | ' ' | 授权状态,枚举: 0 :未授权 1 :已授权 3 :授权失败 |
| 12 | fuserfield | 授权人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fauthdate | 授权日期 | timestamp | 0 |  |  | null | 授权日期 |
| 14 | fservergroup | 服务分组 | varchar | 8 |  | √ | ' ' | 服务分组,枚举: 0 :发票开票服务 1 :发票收票服务 2 :发票预警服务 3 :电子档案服务 |
| 15 | fissuetype | fissuetype | varchar | 60 |  | √ | ' ' |  |
| 16 | fvalidstarttime | 有效期始 | timestamp | 0 |  |  | null | 有效期始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_invoice_permission |  | fepinfo,fservergroup |
| 2 | pk_bdm_invoice_permission |  | fid |
