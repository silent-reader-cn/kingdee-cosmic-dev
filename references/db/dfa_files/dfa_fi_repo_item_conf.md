# 标准报表项目配置-dfa_fi_repo_item_conf

## 标准报表项目配置-主表 t_dfa_fi_repo_item_conf

- **表名称：** 标准报表项目配置-主表
- **表名：** t_dfa_fi_repo_item_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdefault_data_type | 默认项目数据类型 | varchar | 50 |  | √ | ' ' | 默认项目数据类型,枚举: qms :期末数 ncs :年初数 pre_qms :上期期末数 pre_year_qms :上年同期期末数 cur_fss :本期发生数 cur_year_ljs :本年累计数 pre_fss :上期发生数 pre_year_fss :上年同期发生数 |
| 3 | fipo_fin_report_item | IPO财务报表项目 | int8 | 64 |  | √ | 0 | [财务报表项目 ipo_fin_report_item](../ipobase_files/ipo_fin_report_item.md) |
| 4 | fclean_item_name | 清洗后-项目名称 | varchar | 255 |  | √ | ' ' | 清洗后-项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_fi_repo_item_conf |  | fid |
| 2 | idx_dfa_fi_repo_item_conf |  | fipo_fin_report_item |
