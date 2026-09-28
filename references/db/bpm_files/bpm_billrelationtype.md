# 单据关系类型-bpm_billrelationtype

## 单据关系类型-主表 t_bpm_billrelationtype

- **表名称：** 单据关系类型-主表
- **表名：** t_bpm_billrelationtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodelformid | 模型参数表单 | varchar | 100 |  | √ | ' ' | 模型参数表单 |
| 3 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | fpreinsert | 是否为内置数据 | bpchar | 1 |  | √ | '0' | 是否为内置数据 |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 6 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 7 | fparseclass | 解析类 | varchar | 200 |  | √ | ' ' | 解析类 |
| 8 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 9 | fformid | 转换参数表单 | varchar | 100 |  | √ | ' ' | 转换参数表单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bpm_billrelationtype |  | fnumber |
| 2 | pk_t_bpm_billrelationtype |  | fid |

---

## 单据关系类型-多语言表 t_bpm_billrelationtype_l

- **表名称：** 单据关系类型-多语言表
- **表名：** t_bpm_billrelationtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bpm_billrelationtype_l |  | fpkid |
| 2 | idx_bpm_billrelationtype_l |  | fid,flocaleid |
