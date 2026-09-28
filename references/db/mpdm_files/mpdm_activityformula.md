# 活动公式-mpdm_activityformula

## 活动公式-主表 t_mpdm_activityformula

- **表名称：** 活动公式-主表
- **表名：** t_mpdm_activityformula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fformula | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fexpression | 公式 | varchar | 255 |  | √ | ' ' | 公式 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fpurpose | 用途 | bpchar | 1 |  | √ | ' ' | 用途,枚举: 1 :准备活动汇报量 2 :加工活动汇报量 3 :其他活动一汇报量 4 :其他活动二汇报量 6 :准备活动计划量 5 :加工活动计划量 7 :其他活动一计划量 8 :其他活动二计划量 |
| 22 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 24 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 26 | factivitytype | 活动类型 | varchar | 10 |  | √ | ' ' | 活动类型,枚举: 0 :机器 1 :人工 |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fftranexpr | 公式译文 | varchar | 255 |  | √ | ' ' | 公式译文 |
| 29 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_formula_number |  | fnumber |
| 2 | idx_t_mpdm_activityformula_createorg |  | fcreateorgid |
| 3 | pk_mpdm_activityformula |  | fid |
| 4 | idx_t_mpdm_activityformula_master |  | fmasterid |

---

## 活动公式-多语言表 t_mpdm_activityformula_l

- **表名称：** 活动公式-多语言表
- **表名：** t_mpdm_activityformula_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fformula | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fftranexpr | 公式译文 | varchar | 255 |  | √ | ' ' | 公式译文 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_activityformula_l |  | fpkid |
| 2 | idx_mpdm_activityformula_lid |  | fid,flocaleid |

---

## 活动公式-使用范围表 t_mpdm_activityformula_u

- **表名称：** 活动公式-使用范围表
- **表名：** t_mpdm_activityformula_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_activityformula_u |  | fdataid,fuseorgid |
| 2 | idx_mpdm_actformula_use |  | fuseorgid |
