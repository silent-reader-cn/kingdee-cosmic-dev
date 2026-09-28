# 政府补助递延收益中间表-tccit_govdefer_middle

## 政府补助递延收益中间表-主表 t_tccit_govdefer_midd

- **表名称：** 政府补助递延收益中间表-主表
- **表名：** t_tccit_govdefer_midd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 补助项目名称 | varchar | 50 |  | √ | ' ' | 补助项目名称 |
| 3 | fljjzsyamount | 累计结转损益金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计结转损益金额 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :禁用 1 :可用 |
| 5 | faccountingmethod | 核算方法 | varchar | 50 |  | √ | ' ' | 核算方法,枚举: 1 :总额法 2 :净额法 |
| 6 | fdnjzsy | 本年账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本年账载金额 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fsywjzamount | 剩余未结转金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余未结转金额 |
| 10 | fgovdepartment | 发放补助政府主管部门 | varchar | 50 |  | √ | ' ' | 发放补助政府主管部门 |
| 11 | frelateassetcode | 关联资产编码 | varchar | 50 |  | √ | ' ' | 关联资产编码 |
| 12 | fsyjzsyje | 剩余结转损益金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余结转损益金额 |
| 13 | fljsdbzamount | 累计收到补助金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计收到补助金额 |
| 14 | fljjzsy | 累计账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计账载金额 |
| 15 | fyear | 年份 | timestamp | 0 |  |  | null | 年份 |
| 16 | fhtzje | 合同总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合同总金额 |
| 17 | fdnsdbz | 本年收到补助 | numeric | 23 | 10 | √ | 0.0000000000 | 本年收到补助 |
| 18 | fbillno | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 19 | fsubsidytype | 补助类型 | varchar | 50 |  | √ | ' ' | 补助类型,枚举: 1 :资产相关 2 :收益相关 3 :其他 |
| 20 | fljsdbz | 累计收到补助 | numeric | 23 | 10 | √ | 0.0000000000 | 累计收到补助 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_govdefer_midd |  | fid |
| 2 | idx_tccit_govdefer_midd |  | fbillno |
