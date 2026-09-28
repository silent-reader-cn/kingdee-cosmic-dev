# 序列号轨迹关联表-bd_snmovetrack_rel

## 序列号轨迹关联表-主表 t_bd_snmovetrack_rel

- **表名称：** 序列号轨迹关联表-主表
- **表名：** t_bd_snmovetrack_rel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftrackid | 轨迹id | int8 | 64 |  | √ | 0 | 轨迹id |
| 3 | fsnmainfileid | 序列号id | int8 | 64 |  | √ | 0 | 序列号id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_snmovetrackrel_smf |  | fsnmainfileid |
| 2 | pk_t_bd_snmovetrack_rel |  | fid |
| 3 | idx_bd_snmovetrackrel_track |  | ftrackid |
