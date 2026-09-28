# 关账表-cal_closeaccounttable

## 关账表-主表 t_cal_closeaccount

- **表名称：** 关账表-主表
- **表名：** t_cal_closeaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fownerid | 货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | '0' | 是否叶子节点 |
| 4 | fclosedate | 关账日期 | timestamp | 0 |  |  | null | 关账日期 |
| 5 | fpreviousid | 上一次关账记录 | int8 | 64 |  | √ | 0 | 上一次关账记录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_ca_cco |  | fownerid |
| 2 | idx_cal_ca_lastid |  | fpreviousid |
| 3 | t_cal_closeaccount_pkey |  | fid |
