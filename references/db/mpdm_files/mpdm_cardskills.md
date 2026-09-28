# 工卡技能信息-mpdm_cardskills

## 技能信息-子表 t_mpdm_cardskills_entry

- **表名称：** 技能信息-子表
- **表名：** t_mpdm_cardskills_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fskills | 技能 | int8 | 64 |  | √ | 0 | 技能 mpdm_skills |
| 3 | fprofessiona | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmrtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 7 | fenginemodel | 发动机型号 | int8 | 64 |  | √ | 0 | 发动机型号 mpdm_enginetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_cardskills_entry_fk |  | fid |
| 2 | pk_mpdm_cardskills_entry |  | fentryid |

---

## 工卡技能信息-使用范围表 t_mpdm_cardskills_u

- **表名称：** 工卡技能信息-使用范围表
- **表名：** t_mpdm_cardskills_u

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
| 1 | idx_t_mpdm_cardskills_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_cardskills_u |  | fdataid,fuseorgid |

---

## 工卡技能信息-使用范围位图表 t_mpdm_cardskills_m

- **表名称：** 工卡技能信息-使用范围位图表
- **表名：** t_mpdm_cardskills_m

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
| 1 | pk_t_mpdm_cardskills_m |  | forgid |

---

## 工卡技能信息-多语言表 t_mpdm_cardskills_l

- **表名称：** 工卡技能信息-多语言表
- **表名：** t_mpdm_cardskills_l

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
| 1 | idx_mpdm_cardskills_l_0 |  | fid,flocaleid |
| 2 | pk_t_mpdm_cardskills_l |  | fpkid |

---

## 工卡技能信息-主表 t_mpdm_cardskills

- **表名称：** 工卡技能信息-主表
- **表名：** t_mpdm_cardskills

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 4 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 12 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 13 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fenabletime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fcard | 工卡编码 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 26 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_cardskills_createorg |  | fcreateorgid |
| 2 | idx_t_mpdm_cardskills_fcard |  | fcard |
| 3 | pk_mpdm_cardskills |  | fid |
| 4 | idx_t_mpdm_cardskills_master |  | fmasterid |
