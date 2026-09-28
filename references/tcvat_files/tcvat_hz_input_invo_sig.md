# 总机构进项标识单据-tcvat_hz_input_invo_sig

## 总机构进项标识单据-主表 t_tcvat_hz_input_invo_sig

- **表名称：** 总机构进项标识单据-主表
- **表名：** t_tcvat_hz_input_invo_sig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | frefundabletaxamount | 即征即退税额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退税额 |
| 4 | feffectivetaxamount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 5 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fsignstatus | 标记状态 | varchar | 30 |  | √ | ' ' | 标记状态,枚举: 1 :未标记 2 :已取消标记 |
| 9 | fsignedtaxamount | 已标识税额 | numeric | 23 | 10 | √ | 0.0000000000 | 已标识税额 |
| 10 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 11 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 12 | fremark | 备注 | varchar | 125 |  | √ | ' ' | 备注 |
| 13 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsignrate | 标识比列 | numeric | 23 | 10 | √ | 0.0000000000 | 标识比列 |
| 16 | fundistinguishtaxamount | 无法划分税额 | numeric | 23 | 10 | √ | 0.0000000000 | 无法划分税额 |
| 17 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 18 | fcurrentsigntaxamount | 本次标识税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次标识税额 |
| 19 | frollouttype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税项目用 5 :开具红字专用发票信息表 6 :其他 |
| 20 | finvoicepkid | 发票主键id | varchar | 50 |  | √ | ' ' | 发票主键id |
| 21 | fconsumertype | 用途标识 | varchar | 30 |  | √ | ' ' | 用途标识,枚举: 4 :即征即退标识 5 :无法划分标识 |
| 22 | fsigncoid | 标记关联id | varchar | 50 |  | √ | ' ' | 标记关联id |
| 23 | ftype | 标识数据类型 | varchar | 30 |  | √ | ' ' | 标识数据类型,枚举: 1 :进项转出标识 2 :进项标识 |
| 24 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 4 :增值税专用发票 15 :通行费发票 2 :增值税电子专用发票 |
| 25 | frollouttaxamount | 转出税额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出税额 |
| 26 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 27 | frolloutid | 进项转出登记表id | varchar | 50 |  | √ | ' ' | 进项转出登记表id |
| 28 | fsigntype | 标记类型 | varchar | 30 |  | √ | ' ' | 标记类型,枚举: 1 :进项标记 2 :取消标记 3 :转出标记 |
| 29 | favaliabletaxamount | 可标识税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可标识税额 |
| 30 | fsignrule | 标识规则 | varchar | 30 |  | √ | ' ' | 标识规则,枚举: 1 :全部标识 2 :按比例标识 3 :录入税额标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_hz_input_invo_sig |  | fid |
| 2 | idx_tcvat_hz_input_invo_sig |  | forgid,fstartdate,fenddate |
