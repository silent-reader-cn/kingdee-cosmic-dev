# 规则取数汇总结果表-tcvvt_fetch_summary

## 规则取数汇总结果表-主表 t_tcvvt_fetch_summary

- **表名称：** 规则取数汇总结果表-主表
- **表名：** t_tcvvt_fetch_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fserialno | 规则取数明细流水号 | varchar | 50 |  | √ | ' ' | 规则取数明细流水号 |
| 4 | faccessprojectid | 取数项目id | varchar | 75 |  | √ | ' ' | 取数项目id |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftaxlimit | 申报期限 | varchar | 50 |  | √ | ' ' | 申报期限,枚举: month :月 season :季度 halfyear :半年 year :年 single :次 |
| 8 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 9 | ftemplatetype | 模板类型 | varchar | 100 |  | √ | ' ' | 模板类型 |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 13 | ffetchamount | 取数金额 | numeric | 23 | 10 | √ | 0 | 取数金额 |
| 14 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: system :自动取数 useradd :手工新增 |
| 15 | freportingamount | 填报金额 | numeric | 23 | 10 | √ | 0 | 填报金额 |
| 16 | fformulakey | 行列维 | varchar | 50 |  | √ | ' ' | 行列维 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_fetchsum_no |  | fserialno |
| 2 | pk_tcvvt_fetch_summary |  | fid |
| 3 | idx_tcvvt_fetchsum_org |  | faccessprojectid,forgid |
