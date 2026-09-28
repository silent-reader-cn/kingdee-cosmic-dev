# 可发量操作-sm_expectqtyoperate

## 可发量操作-多语言表 t_sm_expectqtyoperateset_l

- **表名称：** 可发量操作-多语言表
- **表名：** t_sm_expectqtyoperateset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperationname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyoperateset_l |  | fentryid,flocaleid |
| 2 | pk_sm_expectqtyoperateset_l |  | fpkid |

---

## 可发量操作-主表 t_sm_expectqtyoperateset

- **表名称：** 可发量操作-主表
- **表名：** t_sm_expectqtyoperateset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据 | int8 | 64 |  | √ | 0 | [可发量单据配置 sm_expectqtybillsetting](../sm_files/sm_expectqtybillsetting.md) |
| 2 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 3 | foperationname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 5 | foperation | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyoperateset |  | fid |
| 2 | pk_sm_expectqtyoperateset |  | fentryid |
