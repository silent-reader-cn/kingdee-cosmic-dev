# 税源采集调整明细-tcret_sycj_adjust_detail

## 税源采集调整明细-主表 t_tcret_sycj_tzmx

- **表名称：** 税源采集调整明细-主表
- **表名：** t_tcret_sycj_tzmx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 3 | ftaxitem | 税目名称 | varchar | 50 |  | √ | ' ' | 税目名称 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 总额 | numeric | 23 | 10 | √ | 0.0000000000 | 总额 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 8 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整额 |
| 9 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: 1 :应税合同凭证 2 :产权转移书据 3 :资金账簿 |
| 10 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 11 | fruleid | 规则id | varchar | 50 |  | √ | ' ' | 规则id |
| 12 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |
| 13 | ffetchtype | 取数类型 | varchar | 50 |  | √ | 'amount' | 取数类型,枚举: amount :金额 taxamount :税额 count :份数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_sycj_tzmx |  | fid |
| 2 | idx_tcret_sycj_tzmx |  | forgid,fskssqq,fskssqz |
