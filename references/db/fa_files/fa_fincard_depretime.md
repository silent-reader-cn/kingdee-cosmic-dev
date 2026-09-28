# 财务卡片实际计提时点-fa_fincard_depretime

## 财务卡片实际计提时点-主表 t_fa_fincard_depretime

- **表名称：** 财务卡片实际计提时点-主表
- **表名：** t_fa_fincard_depretime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmasterid | 实物卡片masterid | int8 | 64 |  | √ | 0 | 实物卡片masterid |
| 3 | fdepretime | 计提时点 | varchar | 30 |  | √ | ' ' | 计提时点,枚举: CLEAR :次月 NEW :当月 NEXT_DAY :次日 NEW_AND_CLEAR :当日 NEXT_YEAR :次年 THIS_YEAR :当年 FIRST_YEAR_CONVEN :首年常规 |
| 4 | fchangebilltype | fchangebilltype | varchar | 25 |  | √ | ' ' |  |
| 5 | fchangebillid | fchangebillid | int8 | 64 |  | √ | 0 |  |
| 6 | ffincardid | ffincardid | int8 | 64 |  | √ | 0 |  |
| 7 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | [启用期间设置 fa_assetbook](../fa_files/fa_assetbook.md) |
| 8 | fdepreuseid | fdepreuseid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_fincard_depretime_pkey |  | fid |
| 2 | idx_fa_fincard_depretime |  | ffincardid |
