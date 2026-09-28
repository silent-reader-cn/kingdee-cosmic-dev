# 流程实例（历史）-isc_sf_proc_inst_es

## 流程实例（历史）-主表 t_iscb_es_bak

- **表名称：** 流程实例（历史）-主表
- **表名：** t_iscb_es_bak

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcolumn3 | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: Created :新建 Waiting :等待中 Running :执行中 Failed :已失败 Complete :已结束 Terminated :已撤销 Retried :已重做 Reverted :已还原 |
| 3 | fcolumn2 | 修改时间 | varchar | 30 |  | √ | ' ' | 修改时间 |
| 4 | fcolumn1 | 发起时间 | varchar | 30 |  | √ | ' ' | 发起时间 |
| 5 | fcolumn5 | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 6 | fcolumn4 | 运行时上下文 | varchar | 30 |  | √ | ' ' | 运行时上下文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_es_bak |  | fid |
| 2 | idx_isc_es_bak |  | fcolumn1 |
