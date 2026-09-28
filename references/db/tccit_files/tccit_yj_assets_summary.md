# 预缴资产总额底稿-tccit_yj_assets_summary

## 预缴资产总额底稿-主表 t_tccit_yj_assets_summary

- **表名称：** 预缴资产总额底稿-主表
- **表名：** t_tccit_yj_assets_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbjamount | 本季数 | numeric | 23 | 10 | √ | 0 | 本季数 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 021 :期初资产 022 :期末资产 |
| 4 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 5 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 6 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 8 | fbqamount | 本期数 | numeric | 23 | 10 | √ | 0 | 本期数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_yj_assets_summary |  | fid |
| 2 | idx_t_tccit_yj_assets_sum_1 |  | forgid,fskssqq,fskssqz |
