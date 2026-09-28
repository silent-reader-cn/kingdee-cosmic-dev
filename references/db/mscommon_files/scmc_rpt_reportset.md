# 报表取数分片设置-scmc_rpt_reportset

## 报表取数分片设置-主表 t_scmc_rpt_reportset

- **表名称：** 报表取数分片设置-主表
- **表名：** t_scmc_rpt_reportset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmindaydiff | 最小时间间隔（天） | int4 | 32 |  | √ | 0 | 最小时间间隔（天） |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | freportid | 报表标识 | varchar | 50 |  | √ | ' ' | 报表标识 |
| 8 | ftimefield | 时间过滤字段 | varchar | 50 |  | √ | ' ' | 时间过滤字段 |
| 9 | fsplitcount | 数据块最大分片数 | int4 | 32 |  | √ | 0 | 数据块最大分片数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scmc_rpt_reportset |  | fid |
| 2 | idx_scmc_rpt_reportset |  | freportid |
