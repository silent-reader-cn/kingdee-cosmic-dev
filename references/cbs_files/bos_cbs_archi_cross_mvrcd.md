# 归档调度数据迁移记录-bos_cbs_archi_cross_mvrcd

## 归档调度数据迁移记录-主表 t_cbs_archi_cross_mvrcd

- **表名称：** 归档调度数据迁移记录-主表
- **表名：** t_cbs_archi_cross_mvrcd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 3 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_cross_mvrcd |  | fid |
| 2 | idx_cbs_archi_cross_mvrcd_bid |  | fbillid |
| 3 | idx_cbs_archi_cross_mvrcd_tid |  | ftaskid |
