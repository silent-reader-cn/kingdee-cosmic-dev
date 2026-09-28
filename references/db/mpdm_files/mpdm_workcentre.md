# 工作中心定义(废弃)-mpdm_workcentre

## 资源-子表 t_mpdm_workcentreentryb

- **表名称：** 资源-子表
- **表名：** t_mpdm_workcentreentryb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresouceqty | 资源数量 | int4 | 32 |  | √ | 0 | 资源数量 |
| 3 | fresourcenumber | 资源编码 | varchar | 30 |  | √ | ' ' | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fprocessactive | 工序活动 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_workcentreentryb_pkey |  | fentryid |
| 2 | idx_mpdm_workcentreb_fk |  | fid,fseq |

---

## 生产能力-子表 t_mpdm_workcentreentrya

- **表名称：** 生产能力-子表
- **表名：** t_mpdm_workcentreentrya

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworkcent | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 3 | fmaterialgroup | 物料控制组 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fcapacitynumber | fcapacitynumber | varchar | 50 |  | √ | ' ' |  |
| 7 | fproducttype | 产品维度 | varchar | 30 |  | √ | ' ' | 产品维度,枚举: A :物料 C :物料控制组 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcapagroupnum | 能力项组编码 | int8 | 64 |  | √ | 0 | [能力项组 mpdm_capacitygroup](../mpdm_files/mpdm_capacitygroup.md) |
| 11 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fcapacityqty | fcapacityqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fefficiencyqty | fefficiencyqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fcapagroupseq | 能力项组编码序号 | int4 | 32 |  | √ | 0 | 能力项组编码序号 |
| 15 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 16 | fcapacityname | fcapacityname | varchar | 50 |  | √ | ' ' |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | faddefficiencyqty | faddefficiencyqty | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_workcentrea_fk |  | fid,fseq |
| 2 | t_mpdm_workcentreentrya_pkey |  | fentryid |

---

## 工作中心定义(废弃)-主表 t_mpdm_workcentre

- **表名称：** 工作中心定义(废弃)-主表
- **表名：** t_mpdm_workcentre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 工作中心类别 | int8 | 64 |  | √ | 0 | [工作中心类别(废弃) mpdm_workcentgroup](../mpdm_files/mpdm_workcentgroup.md) |
| 3 | fremake | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 4 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcalendar | 生产日历 | int8 | 64 |  | √ | 0 | [生产日历 mpdm_calendar](../mpdm_files/mpdm_calendar.md) |
| 7 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 8 | flocation | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fprocessstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | [工序控制策略(废弃) mpdm_proctrlstrategy](../mpdm_files/mpdm_proctrlstrategy.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fbackflushflag | 倒冲 | varchar | 20 |  | √ | ' ' | 倒冲,枚举: 0 :否 1 :是 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fabilitytype | 能力类别 | int8 | 64 |  | √ | 0 | [基础资料模板 mpdm_abilitytype](../mpdm_files/mpdm_abilitytype.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fparentcenter | 上级工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 23 | factivestandard | 活动量标准值 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_activestandard](../mpdm_files/mpdm_activestandard.md) |
| 24 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fworkmode | 工作模式 | varchar | 20 |  | √ | ' ' | 工作模式,枚举: A :自然日历 B :工作日历 |
| 28 | fnumber | 工作中心编码 | varchar | 60 |  | √ | ' ' | 工作中心编码 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fparentorg | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_workcentre_forg |  | fnumber,fcreateorgid |
| 2 | t_mpdm_workcentre_pkey |  | fid |
| 3 | idx_t_mpdm_workcentre_createorg |  | fcreateorgid |
| 4 | idx_t_mpdm_workcentre_master |  | fmasterid |

---

## 计算能力项子单据体-子表 t_mpdm_workcentredetailb

- **表名称：** 计算能力项子单据体-子表
- **表名：** t_mpdm_workcentredetailb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprecision | 精度 | int4 | 32 |  | √ | 0 | 精度 |
| 2 | fcompleteresult | 计算结果 | varchar | 50 |  | √ | ' ' | 计算结果 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcapacitytype | 能力项类别 | varchar | 50 |  | √ | ' ' | 能力项类别,枚举: A :固定值 B :计算值 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fworkstype | 工时种类 | varchar | 50 |  | √ | ' ' | 工时种类,枚举: A :机器工时 B :人工工时 |
| 7 | fcapacityname | 能力项名称 | varchar | 50 |  | √ | ' ' | 能力项名称 |
| 8 | fcapacitynumber | 能力项编码 | varchar | 50 |  | √ | ' ' | 能力项编码 |
| 9 | fcapacitycalen | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fworkunits | 工时单位 | varchar | 50 |  | √ | ' ' | 工时单位,枚举: A :秒 B :分 C :时 D :天 |
| 12 | fcapacitycal | 计算表达式 | varchar | 255 |  | √ | ' ' | 计算表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_workcentredetailb |  | fdetailid |
| 2 | idx_mpdm_workcentredetailb |  | fentryid,fseq |

---

## 固定能力项子单据体-子表 t_mpdm_workcentredetaila

- **表名称：** 固定能力项子单据体-子表
- **表名：** t_mpdm_workcentredetaila

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 2 | fcapacitytype | 能力项类别 | varchar | 50 |  | √ | ' ' | 能力项类别,枚举: A :固定值 B :计算值 |
| 3 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcapacitynumber | 能力项编码 | varchar | 50 |  | √ | ' ' | 能力项编码 |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fcapacityqty | 能力数值 | numeric | 23 | 10 | √ | 0.0000000000 | 能力数值 |
| 9 | fefficiencyqty | 效率 | numeric | 23 | 10 | √ | 0.0000000000 | 效率 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fcapacityname | 能力项名称 | varchar | 50 |  | √ | ' ' | 能力项名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | faddefficiencyqty | 额外效率 | numeric | 23 | 10 | √ | 0.0000000000 | 额外效率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_workcentredetaila |  | fentryid,fseq |
| 2 | pk_t_mpdm_workcentredetaila |  | fdetailid |

---

## 工作中心定义(废弃)-使用范围位图表 t_mpdm_workcentre_m

- **表名称：** 工作中心定义(废弃)-使用范围位图表
- **表名：** t_mpdm_workcentre_m

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
| 1 | pk_t_mpdm_workcentre_m |  | forgid |

---

## 工作中心定义(废弃)-多语言表 t_mpdm_workcentre_l

- **表名称：** 工作中心定义(废弃)-多语言表
- **表名：** t_mpdm_workcentre_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工作中心名称 | varchar | 100 |  | √ | ' ' | 工作中心名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_workcentre_l_pkey |  | fpkid |
| 2 | idx_mpdm_workcentre_l |  | fid,flocaleid |

---

## 工作中心定义(废弃)-使用范围表 t_mpdm_workcentre_u

- **表名称：** 工作中心定义(废弃)-使用范围表
- **表名：** t_mpdm_workcentre_u

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
| 1 | idx_t_mpdm_workcentre_u_uo |  | fuseorgid |
| 2 | t_mpdm_workcentre_u_pkey |  | fdataid,fuseorgid |

---

## 工序活动-子表 t_mpdm_workcentreprocess

- **表名称：** 工序活动-子表
- **表名：** t_mpdm_workcentreprocess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factiveformula | 活动量公式-标准公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 3 | fprocessqty | 基本数量 | int4 | 32 |  | √ | 0 | 基本数量 |
| 4 | fprocessunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | freportformula | 活动量汇报公式-标准公式 | int8 | 64 |  | √ | 0 | [工序活动公式(废弃) mpdm_processformula](../mpdm_files/mpdm_processformula.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fprocessnumber | 工序活动编码 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |
| 8 | fprocessroutecontrol | 工艺路线录入控制 | bpchar | 1 |  | √ | ' ' | 工艺路线录入控制,枚举: 1 :必录 2 :可选 3 :不检查 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_workcentreprocess |  | fid,fseq |
| 2 | pk_t_mpdm_workcentreprocess |  | fentryid |
