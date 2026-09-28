# 产品配置清单-pdm_productconfigure

## 销售订单-子表 t_pdm_prodconfigsaleorder

- **表名称：** 销售订单-子表
- **表名：** t_pdm_prodconfigsaleorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsaleorderentryseq | 销售订单行号 | varchar | 8 |  | √ | ' ' | 销售订单行号 |
| 3 | fsaleorderno | 销售订单编码 | int8 | 64 |  | √ | 0 | 销售订单F7 sm_salorder_f7 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsaleorderentryid | 销售订单分录ID | int8 | 64 |  | √ | 0 | 销售订单分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_prodconfigsaleorder |  | fentryid |
| 2 | idx_pdm_saleorder_num |  | fsaleorderentryid |

---

## 特征值-子表 t_pdm_prodconffeatureval

- **表名称：** 特征值-子表
- **表名：** t_pdm_prodconffeatureval

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryvalue | 特征值 | varchar | 50 |  | √ | ' ' | 特征值 |
| 3 | ffeaturedefnoid | 特征编码 | int8 | 64 |  | √ | 0 | 特征定义 pdm_featuredefinition |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryvaluename | 特征值名称 | varchar | 50 |  | √ | ' ' | 特征值名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_prodal_fseq |  | fseq |
| 2 | idx_pdm_prodal_fid |  | fid |
| 3 | pk_pdm_prodconffeatureval |  | fentryid |

---

## 特征-子表 t_pdm_prodconffeaturedef

- **表名称：** 特征-子表
- **表名：** t_pdm_prodconffeaturedef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffeaturevalue | 特征值 | varchar | 50 |  | √ | ' ' | 特征值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ffeatureid | 特征编码 | int8 | 64 |  | √ | 0 | 特征定义 pdm_featuredefinition |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fitemselector | 特征选择 | varchar | 1000 |  | √ | ' ' | 特征选择 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_prodef_fseq |  | fseq |
| 2 | pk_pdm_prodconffeaturedef |  | fentryid |
| 3 | idx_pdm_prodef_fid |  | fid |

---

## 组件-子表 t_pdm_configuretreelist

- **表名称：** 组件-子表
- **表名：** t_pdm_configuretreelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fscraprate | 变动损耗率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率（%） |
| 6 | fbomid | BOMID | int8 | 64 |  | √ | 0 | BOMID |
| 7 | fbomentryid | BOMEntryId | int8 | 64 |  | √ | 0 | BOMEntryId |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 11 | fconfigcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 12 | fqtytype | 用量类型 | varchar | 5 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 13 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 14 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 15 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 17 | foptioncontrol | 选项控制(隐藏) | varchar | 30 |  | √ | ' ' | 选项控制(隐藏),枚举: A :单选 B :多选 C :可选 |
| 18 | fentryseq | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 19 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 20 | ftype | 组件类型 | varchar | 5 |  | √ | ' ' | 组件类型,枚举: A :库存 B :选项类 |
| 21 | fmaxqty | 最大数量(隐藏) | numeric | 23 | 10 | √ | 0.0000000000 | 最大数量(隐藏) |
| 22 | fcheckboxfield | fcheckboxfield | bpchar | 1 |  | √ | '0' |  |
| 23 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 24 | fsuperbomentryid | 超级BOM分录ID | int8 | 64 |  | √ | 0 | 超级BOM分录ID |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fmutuexcopt | 选项互斥(隐藏) | bpchar | 1 |  | √ | '0' | 选项互斥(隐藏) |
| 27 | fminqty | 最小数量(隐藏) | numeric | 23 | 10 | √ | 0.0000000000 | 最小数量(隐藏) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_confst_fseq |  | fseq |
| 2 | pk_pdm_configuretreelist |  | fentryid |
| 3 | idx_pdm_confst_fid |  | fid |

---

## 产品配置清单-主表 t_pdm_configurelist

- **表名称：** 产品配置清单-主表
- **表名：** t_pdm_configurelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcid | 来源内码 | varchar | 50 |  | √ | ' ' | 来源内码 |
| 3 | fsrcentryid | 来源分录内码 | varchar | 50 |  | √ | ' ' | 来源分录内码 |
| 4 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fissimula | 模拟选配 | bpchar | 1 |  | √ | '0' | 模拟选配 |
| 7 | fmeasurementunitid | fmeasurementunitid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fpconfigplanid | 产品配置方案 | int8 | 64 |  | √ | 0 | 产品配置方案 pdm_proconfigscheme |
| 10 | fsrcentryentity | 来源分录实体 | varchar | 50 |  | √ | ' ' | 来源分录实体 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fsrcentityid | 来源实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 19 | fmaterielnoid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fprodorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fmaterielversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 26 | fsuperbomid | 超级BOM | int8 | 64 |  | √ | 0 | 超级BOM pdm_superbom |
| 27 | fenable | 使用状态 | varchar | 5 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 清单编码 | varchar | 30 |  | √ | ' ' | 清单编码 |
| 29 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pdm_configurelist_createorg |  | fcreateorgid |
| 2 | idx_t_pdm_configurelist_master |  | fmasterid |
| 3 | idx_pdm_confst_fnumber |  | fnumber |
| 4 | idx_pdm_confst_fcreatetime |  | fcreatetime |
| 5 | pk_pdm_configurelist |  | fid |

---

## 产品配置清单-使用范围位图表 t_pdm_configurelist_m

- **表名称：** 产品配置清单-使用范围位图表
- **表名：** t_pdm_configurelist_m

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
| 1 | pk_t_pdm_configurelist_m |  | forgid |

---

## 产品配置清单-多语言表 t_pdm_configurelist_l

- **表名称：** 产品配置清单-多语言表
- **表名：** t_pdm_configurelist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_confstl_fname |  | fname |
| 2 | idx_pdm_confstl_fid |  | fid,flocaleid |
| 3 | pk_pdm_configurelist_l |  | fpkid |

---

## 产品配置清单-使用范围表 t_pdm_configurelist_u

- **表名称：** 产品配置清单-使用范围表
- **表名：** t_pdm_configurelist_u

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
| 1 | idx_t_pdm_configurelist_u_uo |  | fuseorgid |
| 2 | pk_t_pdm_configurelist_u |  | fdataid,fuseorgid |
