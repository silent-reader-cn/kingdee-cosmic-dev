# 金融机构背景图扩展-cas_finorgimgext

## 金融机构背景图扩展-主表 t_cas_finorgimgext

- **表名称：** 金融机构背景图扩展-主表
- **表名：** t_cas_finorgimgext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffinorgnumber | 金融机构编码 | varchar | 50 |  | √ | ' ' | 金融机构编码 |
| 3 | fbackgroundimg | 背景图片 | varchar | 80 |  | √ | ' ' | 背景图片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_foie_number |  | ffinorgnumber |
| 2 | t_cas_finorgimgext_pkey |  | fid |
