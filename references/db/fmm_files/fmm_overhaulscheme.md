# 标准检修方案-fmm_overhaulscheme

## 工卡清单-子表 t_fmm_overhaulschemeentry

- **表名称：** 工卡清单-子表
- **表名：** t_fmm_overhaulschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryapplyrule | 适用规则（不可见） | varchar | 50 |  | √ | ' ' | 适用规则（不可见）,枚举: bd_customer :客户 |
| 3 | fentrymandatory | 必选（封存） | bpchar | 1 |  | √ | '1' | 必选（封存） |
| 4 | fentryproductncr | 产生NRC（封存） | bpchar | 1 |  | √ | '0' | 产生NRC（封存） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fworkcardid | 工卡编码 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 7 | fentrybaseapplyrule | 适用规则 | varchar | 50 |  | √ | ' ' | 适用规则,枚举: must :必选 demand :按需确认 C :按产品型号确认 bd_customer :按客户确认 E :按检别确认 |
| 8 | fentryremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fentryapplyobject | 适用对象 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_overhaulschemeentry |  | fentryid |
| 2 | idx_fmm_overhaulschemeentry |  | fid |

---

## 标准检修方案-使用范围表 t_fmm_overhaulscheme_u

- **表名称：** 标准检修方案-使用范围表
- **表名：** t_fmm_overhaulscheme_u

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
| 1 | idx_t_fmm_overhaulscheme_u_uo |  | fuseorgid |
| 2 | pk_t_fmm_overhaulscheme_u |  | fdataid,fuseorgid |

---

## 精细型号（封存）-多选基础资料表 t_fmm_overhaulentryfm

- **表名称：** 精细型号（封存）-多选基础资料表
- **表名：** t_fmm_overhaulentryfm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_overhaulentryfm |  | fentryid |
| 2 | pk_fmm_overhaulentryfm |  | fpkid |

---

## 客户（封存）-多选基础资料表 t_fmm_overhaulentrycust

- **表名称：** 客户（封存）-多选基础资料表
- **表名：** t_fmm_overhaulentrycust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_overhaulentrycust |  | fentryid |
| 2 | pk_fmm_overhaulentrycust |  | fpkid |

---

## 标准检修方案-使用范围位图表 t_fmm_overhaulscheme_m

- **表名称：** 标准检修方案-使用范围位图表
- **表名：** t_fmm_overhaulscheme_m

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
| 1 | pk_t_fmm_overhaulscheme_m |  | forgid |

---

## 标准检修方案-多语言表 t_fmm_overhaulscheme_l

- **表名称：** 标准检修方案-多语言表
- **表名：** t_fmm_overhaulscheme_l

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
| 1 | pk_fmm_overhaulscheme_l |  | fpkid |
| 2 | idx_fmm_overhaulscheme_l |  | fid,flocaleid |

---

## 检别（封存）-多选基础资料表 t_fmm_overhaulentrycheck

- **表名称：** 检别（封存）-多选基础资料表
- **表名：** t_fmm_overhaulentrycheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_overhaulentrycheck |  | fpkid |
| 2 | idx_fmm_overhaulentrycheck |  | fentryid |

---

## 适用规则-多选基础资料表 t_fmm_overhaulentryrule

- **表名称：** 适用规则-多选基础资料表
- **表名：** t_fmm_overhaulentryrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 适用规则 mpdm_applicablerule |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fmm_overhaulentryrule |  | fpkid |
| 2 | idx_fmm_overhaulentryrule |  | fentryid |

---

## 客户-多选基础资料表 t_fmm_overhaulcustomer

- **表名称：** 客户-多选基础资料表
- **表名：** t_fmm_overhaulcustomer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_overhaulcustomer |  | fid |
| 2 | pk_fmm_overhaulcustomer |  | fpkid |

---

## 标准检修方案-主表 t_fmm_overhaulscheme

- **表名称：** 标准检修方案-主表
- **表名：** t_fmm_overhaulscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmaterielid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fmrtypeid | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fproductmodel | 产品型号 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
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
| 1 | idx_fmm_overhaulscheme |  | fmaterielid,fproductmodel |
| 2 | pk_fmm_overhaulscheme |  | fid |
| 3 | idx_t_fmm_overhaulscheme_createorg |  | fcreateorgid |
| 4 | idx_t_fmm_overhaulscheme_master |  | fmasterid |
