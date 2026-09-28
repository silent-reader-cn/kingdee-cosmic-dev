# 参数设置数据-iba_parameter

## 参数设置数据-主表 t_iba_parameter

- **表名称：** 参数设置数据-主表
- **表名：** t_iba_parameter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fcompany | 公司 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 4 | fcycle | 报告期类型 | varchar | 50 |  | √ | ' ' | 报告期类型,枚举: 5 :季报 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | freport_type | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: 1 :个别报表 2 :合并报表 |
| 7 | findustry | 所属行业 | int8 | 64 |  | √ | 0 | 证监会行业 csrc_industry_info |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iba_parameter |  | fcompany |
| 2 | pk_t_iba_parameter |  | fid |
