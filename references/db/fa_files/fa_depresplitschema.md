# 分摊方案-fa_depresplitschema

## 分摊方案-主表 t_fa_depresplitschema

- **表名称：** 分摊方案-主表
- **表名：** t_fa_depresplitschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftext | 记录文本 | varchar | 500 |  | √ | ' ' | 记录文本 |
| 3 | fuseorg | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdepreaccount | 科目影响因素 | varchar | 30 |  | √ | ' ' | 科目影响因素,枚举: |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdepreadimension | 核算维度取值 | varchar | 500 |  | √ | ' ' | 核算维度取值 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | faccumulatteddimension | 核算维度取值 | varchar | 500 |  | √ | ' ' | 核算维度取值 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fisreference | 是否被引用 | bpchar | 1 |  | √ | '0' | 是否被引用 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | faccumulattedccount | 科目影响因素 | varchar | 30 |  | √ | ' ' | 科目影响因素,枚举: |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fbasedatafield | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fa_depresplitschema_master |  | fmasterid |
| 2 | idx_t_fa_depresplitschema_createorg |  | fcreateorgid |
| 3 | pk_t_fa_depresplitschema |  | fid |
| 4 | idx_fa_depresplitscheme |  | fbasedatafield |

---

## 核算维度-多选基础资料表 t_fa_depresplitschema_ast

- **表名称：** 核算维度-多选基础资料表
- **表名：** t_fa_depresplitschema_ast

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depresplitschema_ast |  | fid |
| 2 | pk_t_fa_depresplitschema_ast |  | fpkid |

---

## 分摊方案-使用范围表 t_fa_depresplitschema_u

- **表名称：** 分摊方案-使用范围表
- **表名：** t_fa_depresplitschema_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_depresplitschema_u |  | fdataid,fuseorgid |
| 2 | idx_t_fa_depresplitschema_u_uo |  | fuseorgid |

---

## 分摊方案-使用范围位图表 t_fa_depresplitschema_m

- **表名称：** 分摊方案-使用范围位图表
- **表名：** t_fa_depresplitschema_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_depresplitschema_m |  | forgid |

---

## 分摊方案-多语言表 t_fa_depresplitschema_l

- **表名称：** 分摊方案-多语言表
- **表名：** t_fa_depresplitschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depresplitscheme_l |  | fid,flocaleid |
| 2 | pk_t_fa_depresplitschema_l |  | fpkid |
