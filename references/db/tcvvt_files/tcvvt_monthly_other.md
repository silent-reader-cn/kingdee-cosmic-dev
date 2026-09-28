# 千户集团月度报送附表-tcvvt_monthly_other

## 千户集团月度报送附表-主表 t_tcvvt_monthly_other

- **表名称：** 千户集团月度报送附表-主表
- **表名：** t_tcvvt_monthly_other

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fbq | 本期_职工人数(个) | int8 | 64 |  | √ | 0 | 本期_职工人数(个) |
| 5 | fsq | 上期_职工人数(个) | int8 | 64 |  | √ | 0 | 上期_职工人数(个) |
| 6 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 7 | fbqexceptdec | 本期异常说明 | varchar | 2000 |  | √ | ' ' | 本期异常说明 |
| 8 | fcreatename | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 9 | freportdate | 报表期 | varchar | 50 |  | √ | ' ' | 报表期 |
| 10 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 11 | fsntq | 上年同期_职工人数(个) | int8 | 64 |  | √ | 0 | 上年同期_职工人数(个) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvvt_monthly_other |  | fid |
| 2 | idx_tcvvt_monthlyo_sbbid |  | fewblxh,fsbbid |
