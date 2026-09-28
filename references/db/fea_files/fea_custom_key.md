# 自定义档案项-fea_custom_key

## 自定义档案项-多语言表 t_fea_exportlog_l

- **表名称：** 自定义档案项-多语言表
- **表名：** t_fea_exportlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanname | fplanname | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | bpchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_exportlog_l |  | fpkid |
| 2 | idx_fea_exportlog_l |  | fid,flocaleid |

---

## 自定义档案项-主表 t_fea_exportlog

- **表名称：** 自定义档案项-主表
- **表名：** t_fea_exportlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuser | fuser | int8 | 64 |  | √ | 0 |  |
| 3 | ffiletype | ffiletype | varchar | 100 |  | √ | ' ' |  |
| 4 | fplanname | fplanname | varchar | 100 |  | √ | ' ' |  |
| 5 | fdatetime | fdatetime | timestamp | 0 |  |  | null |  |
| 6 | fplan | fplan | int8 | 64 |  | √ | 0 |  |
| 7 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 8 | fplannumber | fplannumber | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_exportlog |  | fid |
| 2 | idx_fea_exportlog |  | fplan,fuser |
