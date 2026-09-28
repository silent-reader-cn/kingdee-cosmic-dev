# 财务报表分析历史记录-dfa_rpt_analysis_history

## 财务报表分析历史记录-主表 t_dfa_rptanalysis_history

- **表名称：** 财务报表分析历史记录-主表
- **表名：** t_dfa_rptanalysis_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchat_context | fchat_context | int8 | 64 |  | √ | 0 |  |
| 3 | freport_url | 报告链接 | varchar | 255 |  | √ | ' ' | 报告链接 |
| 4 | freport_type | 报告类型 | varchar | 50 |  | √ | ' ' | 报告类型 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | freportdate | 报告期 | varchar | 50 |  | √ | ' ' | 报告期 |
| 7 | fcompany1_name | 公司1名称 | varchar | 255 |  | √ | ' ' | 公司1名称 |
| 8 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 10 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :财务报表分析 1 :财务报表对比 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fuid | uid | varchar | 50 |  | √ | ' ' | uid |
| 13 | fcompany2_name | 公司2名称 | varchar | 255 |  | √ | ' ' | 公司2名称 |
| 14 | fstockcode1 | 股票代码1 | varchar | 50 |  | √ | ' ' | 股票代码1 |
| 15 | fstockcode2 | 股票代码2 | varchar | 50 |  | √ | ' ' | 股票代码2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dfa_rptanalysis_history |  | fid |
| 2 | idx_fuserid |  | fuserid |
