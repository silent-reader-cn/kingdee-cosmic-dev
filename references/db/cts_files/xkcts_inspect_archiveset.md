# 业务巡检执行情况归档设置-xkcts_inspect_archiveset

## 业务巡检执行情况归档设置-主表 t_xkinsp_archiveset

- **表名称：** 业务巡检执行情况归档设置-主表
- **表名：** t_xkinsp_archiveset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 4 | fcleardays | 清理天数 | int8 | 64 |  | √ | 0 | 清理天数 |
| 5 | farchivedays | 归档天数 | int8 | 64 |  | √ | 0 | 归档天数 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_archiveset |  | fid |
