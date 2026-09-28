# 工卡实施经验-mpdm_cardimpexperience

## 工卡实施经验-主表 t_mpdm_cardimpexp

- **表名称：** 工卡实施经验-主表
- **表名：** t_mpdm_cardimpexp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcardnum | 工卡编码 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 20 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 23 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cardimpexp_createorg |  | fcreateorgid |
| 2 | idx_t_cardimpexp_master |  | fmasterid |
| 3 | pk_mpdm_cardimpexp |  | fid |
| 4 | idx_t_mpdm_cardimpexp_createorg |  | fcreateorgid |
| 5 | idx_t_mpdm_cardimpexp_master |  | fmasterid |

---

## 实施经验-子表 t_mpdm_cardimpexp_entry

- **表名称：** 实施经验-子表
- **表名：** t_mpdm_cardimpexp_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprogroup | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 3 | fdescribe | 经验描述 | varchar | 255 |  | √ | ' ' | 经验描述 |
| 4 | fbasematerialtype | 工作区域 | int8 | 64 |  | √ | 0 | 工作区域 mpdm_area |
| 5 | fprofessiona | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffunctionlocation | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmrtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 10 | fenginemodel | 发动机型号 | int8 | 64 |  | √ | 0 | 发动机型号 mpdm_enginetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_cardimpexp_entry |  | fentryid |
| 2 | idx_mpdm_cardimpexp_entry_fk |  | fid |

---

## 工卡实施经验-多语言表 t_mpdm_cardimpexp_l

- **表名称：** 工卡实施经验-多语言表
- **表名：** t_mpdm_cardimpexp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cardimpexp_l_0 |  | fid,flocaleid |
| 2 | pk_mpdm_cardimpexp_l |  | fpkid |

---

## 工卡实施经验-使用范围位图表 t_mpdm_cardimpexp_m

- **表名称：** 工卡实施经验-使用范围位图表
- **表名：** t_mpdm_cardimpexp_m

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
| 1 | pk_t_mpdm_cardimpexp_m |  | forgid |

---

## 工卡实施经验-使用范围表 t_mpdm_cardimpexp_u

- **表名称：** 工卡实施经验-使用范围表
- **表名：** t_mpdm_cardimpexp_u

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
| 1 | pk_t_mpdm_cardimpexp_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_cardimpexp_u_uo |  | fuseorgid |
