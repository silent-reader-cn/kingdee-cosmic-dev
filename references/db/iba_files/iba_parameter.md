# 参数设置数据-iba_parameter

## 参数设置数据-主表 t_iba_parameter

- **表名称：** 参数设置数据-主表
- **表名：** t_iba_parameter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffound_date | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fcredit_no | fcredit_no | varchar | 50 |  | √ | ' ' |  |
| 5 | fstock_code | 股票代码 | varchar | 50 |  | √ | ' ' | 股票代码 |
| 6 | fcompany | 公司 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 7 | fcycle | 报告期类型 | varchar | 50 |  | √ | ' ' | 报告期类型,枚举: 5 :季报 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | freport_type | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: 1 :个别报表 2 :合并报表 |
| 10 | findustry | 所属行业 | int8 | 64 |  | √ | 0 | [证监会行业 csrc_industry_info](../ipobase_files/csrc_industry_info.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iba_parameter |  | fcompany |
| 2 | pk_t_iba_parameter |  | fid |
