# 促销匹配服务入参配置-ocdpm_pmt_inparams

## 入参配置明细-子表 t_ocdpm_pparamdetail

- **表名称：** 入参配置明细-子表
- **表名：** t_ocdpm_pparamdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam | 参数标识 | varchar | 80 |  | √ | ' ' | 参数标识 |
| 3 | fparamname | fparamname | varchar | 255 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparamtype | 参数类型 | bpchar | 1 |  | √ | 'A' | 参数类型,枚举: A :表头 B :分录 |
| 6 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :启用 0 :禁用 |
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

## 促销匹配服务入参配置-主表 t_ocdpm_inparams

- **表名称：** 促销匹配服务入参配置-主表
- **表名：** t_ocdpm_inparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_inparams |  | fid |
| 2 | idx_ocdpm_inparams_number |  | fnumber |

---

## 入参配置明细-多语言表 t_ocdpm_pparamdetail_l

- **表名称：** 入参配置明细-多语言表
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

---

## 促销匹配服务入参配置-多语言表 t_ocdpm_inparams_l

- **表名称：** 促销匹配服务入参配置-多语言表
- **表名：** t_ocdpm_inparams_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_inparams_l |  | fpkid |
| 2 | idx_ocdpm_inparamsl_flid |  | fid,flocaleid |
