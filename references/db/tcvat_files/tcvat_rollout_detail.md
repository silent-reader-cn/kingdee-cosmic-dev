# 进项转出登记明细模板-tcvat_rollout_detail

## 进项转出登记明细模板-主表 t_tcvat_roll_out_detail

- **表名称：** 进项转出登记明细模板-主表
- **表名：** t_tcvat_roll_out_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票税额 |
| 3 | ftaxperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 4 | fgroupid | 组id | varchar | 100 |  | √ | ' ' | 组id |
| 5 | fregisterule | 登记规则 | varchar | 100 |  | √ | ' ' | 登记规则 |
| 6 | fcreatetime | 登记时间 | timestamp | 0 |  |  | null | 登记时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fexportamount | 出口税额 | numeric | 23 | 10 | √ | 0.0000000000 | 出口税额 |
| 9 | fcreaterfield | 登记人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | frolloutype | 进项转出类型 | varchar | 30 |  | √ | ' ' | 进项转出类型,枚举: 1 :免税项目用 2 :集体福利、个人消费 3 :非正常损失 4 :简易计税方法征税项目用 5 :免抵退税办法不得抵扣的进项税额 6 :按比例转出 8 :红字专用发票信息表注明的进项税额 7 :其它 |
| 11 | frolloutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 12 | fjzjtamount | 即征即退税额 | numeric | 23 | 10 | √ | 0.0000000000 | 即征即退税额 |
| 13 | finvoiceid | 发票id | varchar | 100 |  | √ | ' ' | 发票id |
| 14 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 15 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 16 | fregistertype | 登记类型 | varchar | 30 |  | √ | ' ' | 登记类型,枚举: 1 :转出登记 2 :撤销登记 |
| 17 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 18 | fmaingoodsname | 主要商品名称 | varchar | 400 |  | √ | ' ' | 主要商品名称 |
| 19 | fsalertaxno | 销方税号 | varchar | 200 |  | √ | ' ' | 销方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_roll_out_detail_pkey |  | fid |
| 2 | idx_t_tcvat_roll_out_detail |  | finvoicecode,finvoiceno |
