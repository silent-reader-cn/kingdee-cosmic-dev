# BOM模板测试-mpdm_bomtest

## 安装位置-多语言表 t_mpdm_bomtestsetentry_l

- **表名称：** 安装位置-多语言表
- **表名：** t_mpdm_bomtestsetentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fsetuplocation | 安装位置 | varchar | 50 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_bomtestsetentry_l |  | fdetailid,flocaleid |
| 2 | t_mpdm_bomtestsetentry_l_pkey |  | fpkid |

---

## BOM模板测试-使用范围位图表 t_mpdm_bomtest_m

- **表名称：** BOM模板测试-使用范围位图表
- **表名：** t_mpdm_bomtest_m

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
| 1 | pk_t_mpdm_bomtest_m |  | forgid |

---

## BOM模板测试-多语言表 t_mpdm_bomtest_l

- **表名称：** BOM模板测试-多语言表
- **表名：** t_mpdm_bomtest_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_bomtest_l_pkey |  | fpkid |
| 2 | idx_mpdm_bomtest_l_fid |  | fid,flocaleid |

---

## BOM模板测试-使用范围表 t_mpdm_bomtest_u

- **表名称：** BOM模板测试-使用范围表
- **表名：** t_mpdm_bomtest_u

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
| 1 | idx_t_mpdm_bomtest_u_uo |  | fuseorgid |
| 2 | t_mpdm_bomtest_u_pkey |  | fdataid,fuseorgid |

---

## 阶梯用量-子表 t_mpdm_bomtestqtyentry

- **表名称：** 阶梯用量-子表
- **表名：** t_mpdm_bomtestqtyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbatchstartqty | 批量开始 | numeric | 23 | 10 | √ | 0.0000000000 | 批量开始 |
| 2 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 3 | fbatchendqty | 批量截止 | numeric | 23 | 10 | √ | 0.0000000000 | 批量截止 |
| 4 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 5 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 6 | fisstepfix | 是否阶梯固定 | bpchar | 1 |  | √ | '0' | 是否阶梯固定 |
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
| 1 | t_mpdm_bomtestqtyentry_pkey |  | fdetailid |
| 2 | idx_mpdm_bomtestqtyentry |  | fentryid,fseq |

---

## 安装位置-子表 t_mpdm_bomtestsetentry

- **表名称：** 安装位置-子表
- **表名：** t_mpdm_bomtestsetentry

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
| 1 | idx_mpdm_bomtestsetentry |  | fentryid,fseq |
| 2 | t_mpdm_bomtestsetentry_pkey |  | fdetailid |

---

## 联副产品-子表 t_mpdm_bomtestcopentry

- **表名称：** 联副产品-子表
- **表名：** t_mpdm_bomtestcopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | ftype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
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
| 1 | t_mpdm_bomtestcopentry_pkey |  | fentryid |
| 2 | idx_mpdm_bomtestcopentry |  | fid,fseq |

---

## BOM模板测试-主表 t_mpdm_bomtest

- **表名称：** BOM模板测试-主表
- **表名：** t_mpdm_bomtest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | BOM分组 | int8 | 64 |  | √ | 0 | [BOM分组 mpdm_bomgroup](../mpdm_files/mpdm_bomgroup.md) |
| 3 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fyieldrate | 成品率 | numeric | 23 | 10 | √ | 0.0000000000 | 成品率 |
| 7 | fiscoproduct | 联副产品 | bpchar | 1 |  | √ | '0' | 联副产品 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | freplacenoid | 替代号 | int8 | 64 |  | √ | 0 | [BOM替代号 mpdm_replaceno](../mpdm_files/mpdm_replaceno.md) |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 22 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | ftypeid | BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | BOM编码 | varchar | 30 |  | √ | ' ' | BOM编码 |
| 28 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_bomtest_pkey |  | fid |
| 2 | idx_t_mpdm_bomtest_createorg |  | fcreateorgid |
| 3 | idx_mpdm_bomtest |  | fnumber |
| 4 | idx_t_mpdm_bomtest_master |  | fmasterid |

---

## 组件信息-子表 t_mpdm_bomtestentry

- **表名称：** 组件信息-子表
- **表名：** t_mpdm_bomtestentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 5 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 6 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 11 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率 |
| 12 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 13 | ftype | 组件类型 | varchar | 30 |  | √ | ' ' | 组件类型,枚举: A :库存 |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 15 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 16 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_bomtestentry |  | fid,fseq |
| 2 | t_mpdm_bomtestentry_pkey |  | fentryid |
