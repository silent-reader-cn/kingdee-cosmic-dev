# 清理集成日志设置-ccas_clearsetting

## 清理集成日志设置-主表 t_ccas_clearsetting

- **表名称：** 清理集成日志设置-主表
- **表名：** t_ccas_clearsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenclear | 开启自动清理 | bpchar | 1 |  | √ | '1' | 开启自动清理 |
| 3 | ffate | 自动清理周期(天数) | int4 | 32 |  | √ | 7 | 自动清理周期(天数) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_clearsetting |  | fopenclear |
| 2 | pk_t_ccas_clearsetting |  | fid |
