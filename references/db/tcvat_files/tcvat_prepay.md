# 增值税预缴税款表-tcvat_prepay

## 增值税预缴税款表-主表 t_tcvat_prepay

- **表名称：** 增值税预缴税款表-主表
- **表名：** t_tcvat_prepay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :预征项目和栏次.建筑服务 2 :预征项目和栏次.销售不动产 3 :预征项目和栏次.出租不动产 4 :表头 5 :合计行 |
| 3 | fadvanceamount | 预征税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预征税额 |
| 4 | ftotalamount | 合计 | numeric | 23 | 10 | √ | 0.0000000000 | 合计 |
| 5 | fadvancescale | 预征率 | varchar | 50 |  | √ | ' ' | 预征率 |
| 6 | fprojectnum | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 7 | fratepayernum | 纳税人识别号： | varchar | 50 |  | √ | ' ' | 纳税人识别号： |
| 8 | fydjzfwyj | 异地建筑服务预缴 | varchar | 50 |  | √ | ' ' | 异地建筑服务预缴,枚举: 0 :否 1 :是 |
| 9 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 10 | fstarttime | 税款所属开始时间 | timestamp | 0 |  |  | null | 税款所属开始时间 |
| 11 | fprojectname | 项目名称 | varchar | 200 |  | √ | ' ' | 项目名称 |
| 12 | fratepayername | 纳税人名称：（公章） | varchar | 50 |  | √ | ' ' | 纳税人名称：（公章） |
| 13 | fcrossclaim | 扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除金额 |
| 14 | fprojectaddress | 项目地址 | varchar | 100 |  | √ | ' ' | 项目地址 |
| 15 | fsfzzsybnsr | 是否增值税一般纳税人 | varchar | 50 |  | √ | ' ' | 是否增值税一般纳税人,枚举: 0 :否 1 :是 |
| 16 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 17 | fsfyj | 是否预缴 | varchar | 50 |  | √ | ' ' | 是否预缴,枚举: 0 :否 1 :是 |
| 18 | fsfsyybjsff | 是否适用一般计税方法 | bpchar | 1 |  | √ | ' ' | 是否适用一般计税方法 |
| 19 | fendtime | 税款所属时间结束时间 | timestamp | 0 |  |  | null | 税款所属时间结束时间 |
| 20 | fsale | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_prepay |  | fid |
| 2 | idx_tcvat_prepay |  | fewblxh,fsbbid |
| 3 | idx_tcvat_prepay2 |  | fsbbid |
