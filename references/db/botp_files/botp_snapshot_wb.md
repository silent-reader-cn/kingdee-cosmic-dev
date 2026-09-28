# 反写快照_反写条目-botp_snapshot_wb

## 反写快照_反写条目-主表 t_botp_writebacksnap

- **表名称：** 反写快照_反写条目-主表
- **表名：** t_botp_writebacksnap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主表内码 | int8 | 64 |  | √ | 0 | 主表内码 |
| 2 | foperate | 反写操作 | bpchar | 1 |  |  | null | 反写操作,枚举: 0 :提交 1 :审核 |
| 3 | fruleverid | 反写规则版本 | int8 | 64 |  |  | null | 反写规则版本 |
| 4 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 5 | fstableid | 源单表格编码 | int8 | 64 |  |  | null | 源单表格编码 |
| 6 | fsid | 源单行内码 | int8 | 64 |  |  | null | 源单行内码 |
| 7 | fwritevalue | 反写量 | numeric | 23 | 10 |  | null | 反写量 |
| 8 | fseq | 序号 | int8 | 64 |  |  | null | 序号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fruleitemid | 反写条目 | int8 | 64 |  |  | null | 反写条目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_botp_writebacksnap_pkey |  | fentryid |
| 2 | idx_botp_writebacksnap_fid |  | fid |
