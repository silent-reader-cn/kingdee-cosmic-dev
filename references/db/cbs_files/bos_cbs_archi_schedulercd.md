# 调度记录-bos_cbs_archi_schedulercd

## 调度记录-主表 t_cbs_archi_schedulercd

- **表名称：** 调度记录-主表
- **表名：** t_cbs_archi_schedulercd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscheduleid | 调度id | int8 | 64 |  | √ | 0 | 调度id |
| 3 | ftaskcount | 生成归档任务数 | int8 | 64 |  | √ | 0 | 生成归档任务数 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fbatchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 6 | fdesc | 调度描述 | varchar | 1000 |  | √ | ' ' | 调度描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_schedulercd |  | fid |
| 2 | idx_cbs_archi_schedulercd |  | fscheduleid |
