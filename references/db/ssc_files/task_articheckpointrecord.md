# 人工检查项记录-task_articheckpointrecord

## 人工检查项记录-主表 t_tk_articheckpointrecord

- **表名称：** 人工检查项记录-主表
- **表名：** t_tk_articheckpointrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | farticheckpoint | 人工检查项 | int8 | 64 |  | √ | 0 | 人工检查项 task_checkpoint |
| 4 | fiscontented | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格 |
| 5 | ftaskid | 任务id | varchar | 50 |  | √ | ' ' | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_chpointrecord_taskid |  | ftaskid |
| 2 | pk_t_tk_articheckpointrecord |  | fid |
