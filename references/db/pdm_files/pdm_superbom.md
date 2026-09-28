# 超级BOM-pdm_superbom

## 组件信息-分表 t_pdm_superbomentry_o

- **表名称：** 组件信息-分表
- **表名：** t_pdm_superbomentry_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaxqty | 最大数量(隐藏) | numeric | 23 | 10 | √ | 0.0000000000 | 最大数量(隐藏) |
| 3 | fqtyopt | 数量可选(隐藏) | bpchar | 1 |  | √ | '0' | 数量可选(隐藏) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fopt | 可选(隐藏) | bpchar | 1 |  | √ | '0' | 可选(隐藏) |
| 6 | fmutuexcopt | 选项互斥(隐藏) | bpchar | 1 |  | √ | '0' | 选项互斥(隐藏) |
| 7 | fminqty | 最小数量(隐藏) | numeric | 23 | 10 | √ | 0.0000000000 | 最小数量(隐藏) |
| 8 | fpreferopt | 首选(隐藏) | bpchar | 1 |  | √ | '0' | 首选(隐藏) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_superbomentry_o |  | fentryid |
| 2 | idx_pdm_superyo_fid |  | fid |

---

## 安装位置-多语言表 t_pdm_superbomsetupentry_l

- **表名称：** 安装位置-多语言表
- **表名：** t_pdm_superbomsetupentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |
| 4 | fsetuplocation | 安装位置 | varchar | 50 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_superbomsetupentry_l |  | fpkid |
| 2 | idx_pdm_superyl_fdetailid |  | fdetailid,flocaleid |

---

## 特征规则-子表 t_pdm_superbomchrulentry

- **表名称：** 特征规则-子表
- **表名：** t_pdm_superbomchrulentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchararuleid | 特征规则编码 | int8 | 64 |  | √ | 0 | [配置规则 pdm_chararule](../pdm_files/pdm_chararule.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_superbomchrulentry |  | fdetailid |
| 2 | idx_pdm_superychrul_fentryid |  | fentryid |
| 3 | idx_pdm_superychrul_fseq |  | fseq |

---

## 联副产品-子表 t_pdm_superbomcopentry

- **表名称：** 联副产品-子表
- **表名：** t_pdm_superbomcopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | ftype | 产品类型 | varchar | 5 |  | √ | '10720' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 9 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | foperationid | 产出工序 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_superycopy_fid |  | fid |
| 2 | idx_pdm_superycopy_fseq |  | fseq |
| 3 | pk_pdm_superbomcopentry |  | fentryid |

---

## 阶梯用量-子表 t_pdm_superbomqtyentry

- **表名称：** 阶梯用量-子表
- **表名：** t_pdm_superbomqtyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbatchstartqty | 批量(从) | numeric | 23 | 10 | √ | 0.0000000000 | 批量(从) |
| 2 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 3 | fbatchendqty | 批量(至) | numeric | 23 | 10 | √ | 0.0000000000 | 批量(至) |
| 4 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 5 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 6 | fisstepfix | 阶梯固定 | bpchar | 1 |  | √ | '0' | 阶梯固定 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_superbomqtyentry |  | fdetailid |
| 2 | idx_pdm_superyqty_fseq |  | fseq |
| 3 | idx_pdm_superyqty_fentryid |  | fentryid |

---

## 超级BOM-使用范围表 t_pdm_superbom_u

- **表名称：** 超级BOM-使用范围表
- **表名：** t_pdm_superbom_u

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
| 1 | idx_t_pdm_superbom_u_uo |  | fuseorgid |
| 2 | pk_t_pdm_superbom_u |  | fdataid,fuseorgid |

---

## 超级BOM-使用范围位图表 t_pdm_superbom_m

- **表名称：** 超级BOM-使用范围位图表
- **表名：** t_pdm_superbom_m

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
| 1 | pk_t_pdm_superbom_m |  | forgid |

---

## 超级BOM-多语言表 t_pdm_superbom_l

- **表名称：** 超级BOM-多语言表
- **表名：** t_pdm_superbom_l

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
| 1 | pk_pdm_superbom_l |  | fpkid |
| 2 | idx_pdm_supeoml_fid |  | fid,flocaleid |

---

## 超级BOM-主表 t_pdm_superbom

- **表名称：** 超级BOM-主表
- **表名：** t_pdm_superbom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | BOM分组 | int8 | 64 |  | √ | 0 | [超级BOM分组 pdm_superbomgrp](../pdm_files/pdm_superbomgrp.md) |
| 3 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fyieldrate | 成品率(封存) | numeric | 23 | 10 | √ | 0.0000000000 | 成品率(封存) |
| 7 | fiscoproduct | 联副产品 | bpchar | 1 |  | √ | '0' | 联副产品 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | freplacenoid | 替代号(封存) | int8 | 64 |  | √ | 0 | [BOM替代号 mpdm_replaceno](../mpdm_files/mpdm_replaceno.md) |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 23 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 24 | foptioncontrol | 选项控制 | varchar | 5 |  | √ | ' ' | 选项控制,枚举: A :单选 B :多选 C :可选 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | ftypeid | BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 28 | fenable | 使用状态 | varchar | 5 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | BOM编码 | varchar | 30 |  | √ | ' ' | BOM编码 |
| 30 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_superbom |  | fid |
| 2 | idx_t_pdm_superbom_master |  | fmasterid |
| 3 | idx_pdm_superbom_fnumber |  | fnumber |
| 4 | idx_t_pdm_superbom_createorg |  | fcreateorgid |

---

## 组件信息-子表 t_pdm_superbomentry

- **表名称：** 组件信息-子表
- **表名：** t_pdm_superbomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 4 | fqtytype | 用量类型 | varchar | 5 |  | √ | 'A' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 5 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 6 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 8 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 11 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率 |
| 12 | fentryseq | 序号(隐藏) | int8 | 64 |  | √ | 0 | 序号(隐藏) |
| 13 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 14 | ftype | 组件类型 | varchar | 5 |  | √ | 'A' | 组件类型,枚举: A :库存 B :选项类 |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 16 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 17 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_supery_fid |  | fid |
| 2 | idx_pdm_supery_fseq |  | fseq |
| 3 | pk_pdm_superbomentry |  | fentryid |

---

## 安装位置-子表 t_pdm_superbomsetupentry

- **表名称：** 安装位置-子表
- **表名：** t_pdm_superbomsetupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 组件数量 | numeric | 23 | 10 | √ | 0.0000000000 | 组件数量 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_superbomsetupentry |  | fdetailid |
| 2 | idx_pdm_superysetup_fseq |  | fseq |
| 3 | idx_pdm_superysetup_fentryid |  | fentryid |
