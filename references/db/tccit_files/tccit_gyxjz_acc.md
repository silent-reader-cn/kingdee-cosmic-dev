# 公益性捐赠台账-tccit_gyxjz_acc

## 公益性捐赠台账-主表 t_tccit_gyxjz_acc

- **表名称：** 公益性捐赠台账-主表
- **表名：** t_tccit_gyxjz_acc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fkcxe | 扣除限额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除限额 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsyjzkkcje | 剩余结转可扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余结转可扣除金额 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsjzc | 实际支出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实际支出金额 |
| 12 | fyear | 发生年度 | timestamp | 0 |  |  | null | 发生年度 |
| 13 | fafterone | 后第一年结转扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 后第一年结转扣除金额 |
| 14 | fafterthree | 后第三年结转扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 后第三年结转扣除金额 |
| 15 | fbillno | 业务编号 | varchar | 30 |  | √ | ' ' | 业务编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fjzje | 结转金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结转金额 |
| 18 | faftertwo | 后第二年结转扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 后第二年结转扣除金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_gyxjz_acc |  | fid |
| 2 | idx_tccit_gyxjz_acc |  | fbillno |
