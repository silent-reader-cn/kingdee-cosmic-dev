# 标品开发商标识-tlmgt_standardisv

## 标品开发商标识-主表 t_tlmgt_standardisv

- **表名称：** 标品开发商标识-主表
- **表名：** t_tlmgt_standardisv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisv | 开发商标识 | varchar | 64 |  | √ | ' ' | 开发商标识 |
| 3 | fdescription | 备注 | varchar | 64 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_stdisv |  | fisv |
| 2 | pk_t_tlmgt_standardisv |  | fid |
