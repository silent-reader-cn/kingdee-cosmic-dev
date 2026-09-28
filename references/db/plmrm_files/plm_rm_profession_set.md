# 参数配置-plm_rm_profession_set

## 参数配置-主表 t_plm_rm_profession_set

- **表名称：** 参数配置-主表
- **表名：** t_plm_rm_profession_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsoft | 软件行业 | bpchar | 1 |  | √ | '1' | 软件行业 |
| 3 | felec | 机电行业 | bpchar | 1 |  | √ | '1' | 机电行业 |
| 4 | ftextfield | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_profession_set_m0 |  | ftextfield |
| 2 | pk_plm_rm_profession_set |  | fid |
