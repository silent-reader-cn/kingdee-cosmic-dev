# 自定义参数-kf_cusparamtype

## 单据体-多语言表 t_kf_param_l

- **表名称：** 单据体-多语言表
- **表名：** t_kf_param_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kf_param_l_fid |  | fentryid,flocaleid |
| 2 | pk_t_kf_param_l |  | fpkid |

---

## 单据体-子表 t_kf_param

- **表名称：** 单据体-子表
- **表名：** t_kf_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 5 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 6 | fvaluetype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: String :字符串 Boolean :布尔值 Decimal :小数 Long :整数 DateTime :日期 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kf_param |  | fentryid |
| 2 | idx_kf_param_id |  | fid,fnumber |

---

## 自定义参数-主表 t_kf_cusparamtype

- **表名称：** 自定义参数-主表
- **表名：** t_kf_cusparamtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用列表 bos_devp_bizapplist |
| 6 | freserved | 系统内置 | bpchar | 1 |  | √ | '0' | 系统内置 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 12 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kf_cusparamtype |  | fid |
| 2 | idx_kf_cpt_number |  | fnumber |

---

## 自定义参数-多语言表 t_kf_cusparamtype_l

- **表名称：** 自定义参数-多语言表
- **表名：** t_kf_cusparamtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kf_cusparamtype_l_fid |  | fid,flocaleid |
| 2 | pk_t_kf_cusparamtype_l |  | fpkid |
