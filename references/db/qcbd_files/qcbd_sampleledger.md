# 样品台账-qcbd_sampleledger

## 样品台账-关联追踪表 t_qcbd_sample_ledger_tc

- **表名称：** 样品台账-关联追踪表
- **表名：** t_qcbd_sample_ledger_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_sample_ledger_tc_tbill |  | ftbillid |
| 2 | idx_qcbd_sample_ledger_tc_tid |  | ftid |
| 3 | pk_qcbd_sample_ledger_tc |  | fid |

---

## 样品台账-反写记录表 t_qcbd_sample_ledger_wb

- **表名称：** 样品台账-反写记录表
- **表名：** t_qcbd_sample_ledger_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_sample_ledger_wb_fk |  | fid |
| 2 | pk_qcbd_sample_ledger_wb |  | fentryid |

---

## 关联子实体-子表 t_qcbd_sample_ledger_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcbd_sample_ledger_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_sample_ledger_lk_fk |  | fid |
| 2 | pk_qcbd_sample_ledger_lk |  | fpkid |

---

## 样品台账-主表 t_qcbd_sample_ledger

- **表名称：** 样品台账-主表
- **表名：** t_qcbd_sample_ledger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 3 | fsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | forgid | 样品责任组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsamplesrc | 样品来源 | varchar | 20 |  | √ | ' ' | 样品来源,枚举: QY :取样出库单 JY :检验单 XZ :临时新增 |
| 8 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | frecorddate | 记录生成日期 | timestamp | 0 |  |  | null | 记录生成日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsampleno | 样品编号 | varchar | 150 |  | √ | ' ' | 样品编号 |
| 13 | fsrcbillsubentryseq | 来源单据子分录序号 | int4 | 32 |  | √ | 0 | 来源单据子分录序号 |
| 14 | fsrcbillype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 15 | fsamplebaseqty | 样品基本数量 | numeric | 23 | 10 | √ | 0 | 样品基本数量 |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 17 | fbillno | 唯一性编码 | varchar | 80 |  | √ | ' ' | 唯一性编码 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsampleunit | 样品计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fsamplename | 样品名称 | varchar | 150 |  | √ | ' ' | 样品名称 |
| 25 | fsampleuserid | 样品责任人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fserialnumber | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 28 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 29 | fsamplebaseunit | 样品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fsrcbillsubentryid | 来源单据子分录ID | int8 | 64 |  | √ | 0 | 来源单据子分录ID |
| 31 | fsampletype | 样品类型 | varchar | 20 |  | √ | ' ' | 样品类型,枚举: CGLY :采购留样 CPLY :产品留样 CKLY :库存留样 LSLY :临时留样 |
| 32 | fsampleqty | 样品数量 | numeric | 23 | 10 | √ | 0 | 样品数量 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_sample_ledger |  | fid |
| 2 | idx_qcbd_sledger_fstatus |  | fbillstatus |
| 3 | idx_qcbd_sledger_fbillno |  | fbillno |

---

## 样品台账-多语言表 t_qcbd_sample_ledger_l

- **表名称：** 样品台账-多语言表
- **表名：** t_qcbd_sample_ledger_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 3 | fsampleno | 样品编号 | varchar | 150 |  | √ | ' ' | 样品编号 |
| 4 | fsamplename | 样品名称 | varchar | 150 |  | √ | ' ' | 样品名称 |
| 5 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_sample_ledger_l |  | fpkid |
| 2 | idx_qcbd_sledger_flocaleid |  | fid,flocaleid |

---

## 样品台账-分表 t_qcbd_sample_ledger_s

- **表名称：** 样品台账-分表
- **表名：** t_qcbd_sample_ledger_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flossqty | 留样期损耗数量 | numeric | 23 | 10 | √ | 0 | 留样期损耗数量 |
| 3 | frsbegindate | 留样开始日期 | timestamp | 0 |  |  | null | 留样开始日期 |
| 4 | fretentionperiod | 留存期限 | int4 | 32 |  | √ | 0 | 留存期限 |
| 5 | fsamplestorageloc | 留样位置 | varchar | 50 |  | √ | ' ' | 留样位置 |
| 6 | fsamplestate | 样品状态 | varchar | 20 |  | √ | ' ' | 样品状态,枚举: CSH :初始化 CDZ :存档中 JYZ :检验中 DXH :待销毁 YXH :已销毁 |
| 7 | fsampleplanid | 取样方案 | int8 | 64 |  | √ | 0 | [取样方案 bd_samplingplan](../basedata_files/bd_samplingplan.md) |
| 8 | fdestroydate | 销毁日期 | timestamp | 0 |  |  | null | 销毁日期 |
| 9 | flossbaseqty | 留样期损耗基本数量 | numeric | 23 | 10 | √ | 0 | 留样期损耗基本数量 |
| 10 | fobscount | 预计观察次数 | int4 | 32 |  | √ | 0 | 预计观察次数 |
| 11 | fsampleform | 样品形态 | varchar | 50 |  | √ | ' ' | 样品形态 |
| 12 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 13 | frsenddate | 留样截止日期 | timestamp | 0 |  |  | null | 留样截止日期 |
| 14 | fperiodunit | 留存期限单位 | varchar | 20 |  | √ | ' ' | 留存期限单位,枚举: DAY :天 MONTH :月 YEAR :年 |
| 15 | finitqualitystate | 初始质量状态 | varchar | 20 |  | √ | ' ' | 初始质量状态,枚举: A :合格品 B :不合格品 C :待检品 D :报废品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_sledger_fstate |  | fsamplestate |
| 2 | pk_qcbd_sample_ledger_s |  | fid |
