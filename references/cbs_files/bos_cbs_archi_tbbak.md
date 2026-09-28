# 中间表详情-bos_cbs_archi_tbbak

## 中间表详情-主表 t_cbs_archi_tbbak

- **表名称：** 中间表详情-主表
- **表名：** t_cbs_archi_tbbak

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftable_name | 备份表名 | varchar | 50 |  | √ | ' ' | 备份表名 |
| 3 | fcleanstatus | 清理状态 | bpchar | 1 |  | √ | ' ' | 清理状态,枚举: 0 :未清理 1 :清理中 2 :已清理 |
| 4 | fmap_name | 备份映射表名 | varchar | 50 |  | √ | ' ' | 备份映射表名 |
| 5 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_tbbak |  | fid |
| 2 | idx_cbs_archi_tbbak |  | ftaskid,fcleanstatus |
