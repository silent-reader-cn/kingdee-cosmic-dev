# 检验标准-qcbd_inspectionstd

## 单据体-子表 t_qcbd_inspectionstdentry

- **表名称：** 单据体-子表
- **表名：** t_qcbd_inspectionstdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckmethod | 检验方法 | int8 | 64 |  | √ | 0 | [检验方法 qcbd_inspectionmethod](../qcbd_files/qcbd_inspectionmethod.md) |
| 3 | fcheckbasis | 检验依据 | int8 | 64 |  | √ | 0 | [检验依据 qcbd_inspectioncrit](../qcbd_files/qcbd_inspectioncrit.md) |
| 4 | funitld | 检验项目单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fdetectiontype | 检测值类型 | int8 | 64 |  | √ | 0 | [检测值类型 qcbd_detectiontype](../qcbd_files/qcbd_detectiontype.md) |
| 6 | fdownvalue | 下限值 | numeric | 23 | 10 |  | null | 下限值 |
| 7 | fcheckcontent | 检验内容 | varchar | 255 |  | √ | ' ' | 检验内容 |
| 8 | fmatchflagint | 比较符 | int8 | 64 |  | √ | 0 | [比较符 qcbd_matchflag](../qcbd_files/qcbd_matchflag.md) |
| 9 | fnormtype | 指标类型 | varchar | 50 |  | √ | ' ' | 指标类型,枚举: A :定量 B :定性 |
| 10 | fspecvalue | 标准值 | varchar | 50 |  | √ | ' ' | 标准值 |
| 11 | fisjoininspect | 联合检验项 | bpchar | 1 |  | √ | '0' | 联合检验项 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | ftopvalue | 上限值 | numeric | 23 | 10 |  | null | 上限值 |
| 14 | fkeyitem | 关键项目 | varchar | 1 |  | √ | '0' | 关键项目 |
| 15 | fmatchflag | fmatchflag | varchar | 50 |  | √ | ' ' |  |
| 16 | fcheckinstruct | 检验仪器 | int8 | 64 |  | √ | 0 | [检验仪器 qcbd_inspectioninstru](../qcbd_files/qcbd_inspectioninstru.md) |
| 17 | fkeyquality | 特性分类 | varchar | 50 |  | √ | ' ' | 特性分类,枚举: A :关键特性 C :重要特性 B :一般特性 |
| 18 | fcheckfreq | 检验频率 | int8 | 64 |  | √ | 0 | [检验频率 qcbd_inspectionfreq](../qcbd_files/qcbd_inspectionfreq.md) |
| 19 | fprojsampid | 项目抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 20 | fcheckitems | 检验项目 | int8 | 64 |  | √ | 0 | [检验项目 qcbd_inspectionitems](../qcbd_files/qcbd_inspectionitems.md) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fcheckstatus | fcheckstatus | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_ispstdent_fnumber |  | fid |
| 2 | t_qcbd_inspectionstdentry_pkey |  | fentryid |

---

## 检验标准-主表 t_qcbd_inspectionstd

- **表名称：** 检验标准-主表
- **表名：** t_qcbd_inspectionstd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckbasis | fcheckbasis | int8 | 64 |  | √ | 0 |  |
| 3 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [检验标准分类 qcbd_inspectionstdgrp](../qcbd_files/qcbd_inspectionstdgrp.md) |
| 4 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 5 | fisrepair | 是否已修复 | bpchar | 1 |  | √ | '0' | 是否已修复 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fradiogroupfield | fradiogroupfield | varchar | 30 |  | √ | ' ' |  |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcheckinstruct | fcheckinstruct | int8 | 64 |  | √ | 0 |  |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcheckmethod | fcheckmethod | int8 | 64 |  | √ | 0 |  |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 21 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fsrcstdid | 来源标准ID | int8 | 64 |  | √ | 0 | 来源标准ID |
| 25 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 2 :分配/局部共享 7 :私有 |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fradiogroupfield1 | fradiogroupfield1 | varchar | 30 |  | √ | ' ' |  |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_qcbd_inspectionstd_createorg |  | fcreateorgid |
| 2 | uidx_qcbd_inspectionstd_billno |  | fnumber,forgid |
| 3 | idx_t_qcbd_inspectionstd_master |  | fmasterid |
| 4 | t_qcbd_inspectionstd_pkey |  | fid |

---

## 检验标准-使用范围表 t_qcbd_inspectionstd_u

- **表名称：** 检验标准-使用范围表
- **表名：** t_qcbd_inspectionstd_u

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
| 1 | idx_t_qcbd_inspectionstd_u_uo |  | fuseorgid |
| 2 | t_qcbd_inspectionstd_u_pkey |  | fdataid,fuseorgid |

---

## 检验标准-使用范围位图表 t_qcbd_inspectionstd_m

- **表名称：** 检验标准-使用范围位图表
- **表名：** t_qcbd_inspectionstd_m

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
| 1 | pk_t_qcbd_inspectionstd_m |  | forgid |

---

## 检验标准-多语言表 t_qcbd_inspectionstd_l

- **表名称：** 检验标准-多语言表
- **表名：** t_qcbd_inspectionstd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_qcbd_inspectionstd_l_pkey |  | fpkid |
| 2 | idx_qcbd_ispstd_fid |  | fid,flocaleid |
