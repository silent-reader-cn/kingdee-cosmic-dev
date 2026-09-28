# 促销匹配服务入参-ocdpm_pparamdetail

## 促销匹配服务入参-主表 t_ocdpm_pparamdetail

- **表名称：** 促销匹配服务入参-主表
- **表名：** t_ocdpm_pparamdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam | 参数标识 | varchar | 80 |  | √ | ' ' | 参数标识 |
| 3 | fparamname | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fparamtype | 参数类型 | bpchar | 1 |  | √ | 'A' | 参数类型,枚举: A :表头 B :分录 |
| 6 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 7 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_pparamdetail_fid |  | fid |
| 2 | pk_ocdpm_pparamdetail |  | fentryid |

---

## 促销匹配服务入参-多语言表 t_ocdpm_pparamdetail_l

- **表名称：** 促销匹配服务入参-多语言表
- **表名：** t_ocdpm_pparamdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparamname | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_pparamdetail_l |  | fpkid |
| 2 | idx_ocdpm_pparamdetaill_flid |  | fentryid,flocaleid |
