# 分支机构年报会计利润台账-tccit_branch_pr_summary

## 分支机构年报会计利润台账-主表 t_tccit_branch_pr_summary

- **表名称：** 分支机构年报会计利润台账-主表
- **表名：** t_tccit_branch_pr_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: income :营业收入 jcost :营业成本 profit :利润总额 |
| 3 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbqfse | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |
| 6 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_branch_pr_summary |  | fid |
| 2 | idx_tccit_branch_pr_summary |  | forgid,ftype |
