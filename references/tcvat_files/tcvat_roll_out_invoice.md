# 进项税额转出台账发票明细-tcvat_roll_out_invoice

## 进项税额转出台账发票明细-主表 t_tcvat_roll_out_invoice

- **表名称：** 进项税额转出台账发票明细-主表
- **表名：** t_tcvat_roll_out_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属月份 | varchar | 100 |  | √ | ' ' | 所属月份 |
| 3 | ftaxaccountid | ftaxaccountid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fexportamount | 出口税额 | numeric | 23 | 2 | √ | 0.00 | 出口税额 |
| 8 | ftaxruleid | ftaxruleid | int8 | 64 |  | √ | 0 |  |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 4 :增值税专用发票 15 :通行费发票 |
| 12 | frolloutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 13 | fjzjtamount | 即征即退税额 | numeric | 23 | 2 | √ | 0.00 | 即征即退税额 |
| 14 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 15 | frolloutdate | 转出日期 | timestamp | 0 |  |  | null | 转出日期 |
| 16 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 17 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 18 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 19 | fmaingoodsname | 主要商品名称 | varchar | 100 |  | √ | ' ' | 主要商品名称 |
| 20 | fcombofield | 转出类型 | varchar | 30 |  | √ | ' ' | 转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税方法征税项目用 5 :免抵退税办法不得抵扣的进项税额 6 :按比例转出 8 :红字专用发票信息表注明的进项税额 7 :其它 |
| 21 | fsalertaxno | 销方税号 | varchar | 100 |  | √ | ' ' | 销方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_roll_out_invoice |  | forgid,ftaxperiod |
| 2 | t_tcvat_roll_out_invoice_pkey |  | fid |
