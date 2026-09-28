# 核销日志-occba_verifylog

## 核销日志-主表 t_occba_verifylog

- **表名称：** 核销日志-主表
- **表名：** t_occba_verifylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffailed | 失败数量 | numeric | 23 | 10 | √ | 0 | 失败数量 |
| 3 | flog_tag | 失败摘要_详情 | text | 0 |  |  | null | 失败摘要_详情 |
| 4 | fcreatetime | 核销时间 | timestamp | 0 |  |  | null | 核销时间 |
| 5 | fcreaterorid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fverifyplanid | 关联核销方案 | int8 | 64 |  | √ | 0 | [资金池使用核销方案 occba_verifyplan](../occba_files/occba_verifyplan.md) |
| 7 | fbillno | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 8 | flog | 失败摘要 | text | 0 |  |  | null | 失败摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_verifylog |  | fid |
| 2 | idx_occba_verifylog_no |  | fbillno |
