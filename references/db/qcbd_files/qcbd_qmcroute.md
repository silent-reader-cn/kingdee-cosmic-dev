# 质量工艺路线-qcbd_qmcroute

## 工序活动-子表 t_qcbd_ractentry

- **表名称：** 工序活动-子表
- **表名：** t_qcbd_ractentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factscheduling | 排程 | bpchar | 1 |  | √ | '0' | 排程 |
| 2 | fstandardformula1id | 标准公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 3 | fprocessno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | foperationnumber | 工序名称 | varchar | 50 |  | √ | ' ' | 工序名称 |
| 6 | factivityid | 活动编码 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 7 | fprocessstage | 工序阶段 | varchar | 5 |  | √ | ' ' | 工序阶段,枚举: A :排队阶段 B :准备阶段 C :加工阶段 D :拆卸阶段 E :等待阶段 F :转移阶段 |
| 8 | fminformulaid | 最小值公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 9 | fbiztype | 业务类型 | varchar | 5 |  | √ | ' ' | 业务类型,枚举: A :生产 B :成本 C :工资 |
| 10 | fstandardformulaid | 标准公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 11 | factresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 12 | fminformula1id | 最小值公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_ractentry |  | fdetailid |
| 2 | idx_qcbd_ractry_fentryid |  | fentryid |
| 3 | idx_qcbd_ractry_fseq |  | fseq |

---

## 子单据体-子表 t_qcbd_rsubentry

- **表名称：** 子单据体-子表
- **表名：** t_qcbd_rsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_rsubentry |  | fdetailid |
| 2 | idx_qcbd_rsubry_fentryid |  | fentryid |
| 3 | idx_qcbd_rsubry_fseq |  | fseq |

---

## 工序序列-子表 t_qcbd_proeqentry

- **表名称：** 工序序列-子表
- **表名：** t_qcbd_proeqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 3 | fprocessseqtype | 序列类型 | varchar | 5 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | frelation | 并行关系 | varchar | 5 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :开始-结束 C :结束-开始 D :结束-结束 |
| 6 | freference | 参照序列 | varchar | 50 |  | √ | ' ' | 参照序列 |
| 7 | foutput | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 8 | fprocessseqremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | finput | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 11 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_proery_fid |  | fid |
| 2 | idx_qcbd_proery_fseq |  | fseq |
| 3 | pk_qcbd_proeqentry |  | fentryid |

---

## 质量工艺路线-多语言表 t_qcbd_qroute_l

- **表名称：** 质量工艺路线-多语言表
- **表名：** t_qcbd_qroute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工艺路线名称 | varchar | 50 |  | √ | ' ' | 工艺路线名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_qroutel_fid |  | fid,flocaleid |
| 2 | idx_qcbd_qroutel_fname |  | fname |
| 3 | pk_qcbd_qroute_l |  | fpkid |

---

## 质量工艺路线-使用范围位图表 t_qcbd_qroute_m

- **表名称：** 质量工艺路线-使用范围位图表
- **表名：** t_qcbd_qroute_m

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
| 1 | pk_t_qcbd_qroute_m |  | forgid |

---

## 质量工艺路线-使用范围表 t_qcbd_qroute_u

- **表名称：** 质量工艺路线-使用范围表
- **表名：** t_qcbd_qroute_u

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
| 1 | idx_t_qcbd_qroute_u_uo |  | fuseorgid |
| 2 | pk_t_qcbd_qroute_u |  | fdataid,fuseorgid |

---

## 质量工艺路线-主表 t_qcbd_qroute

- **表名称：** 质量工艺路线-主表
- **表名：** t_qcbd_qroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 工艺路线分组 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_processgroup |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fbomversionstr | BOM | varchar | 50 |  | √ | ' ' | BOM |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmaterialgroupid | 物料控制组 | int8 | 64 |  | √ | 0 | 物料控制组 bd_materialcontrolgroup |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsyntime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | froutereplace | 替代号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_routereplace |
| 13 | fcancelerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | forigin | 来源 | varchar | 5 |  | √ | ' ' | 来源,枚举: A :制造 B :质量 |
| 15 | fcanceltime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fbomversionid | fbomversionid | int8 | 64 |  | √ | 0 |  |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fmanurouteid | 制造源单ID | varchar | 50 |  | √ | ' ' | 制造源单ID |
| 28 | fversionid | 版本 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_processversion |
| 29 | fprocesstype | 工艺类型 | varchar | 5 |  | √ | ' ' | 工艺类型,枚举: A :物料 B :物料组 C :通用 |
| 30 | fqauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | fbomtypestr | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 33 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 工艺路线编码 | varchar | 30 |  | √ | ' ' | 工艺路线编码 |
| 35 | fismainprocess | 主工艺路线 | bpchar | 1 |  | √ | '0' | 主工艺路线 |
| 36 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 37 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_qroute_fcreatetime |  | fcreatetime |
| 2 | idx_qcbd_qroute_fnumber |  | fnumber |
| 3 | idx_t_qcbd_qroute_master |  | fmasterid |
| 4 | idx_t_qcbd_qroute_createorg |  | fcreateorgid |
| 5 | pk_qcbd_qroute |  | fid |

---

## 工序信息-存值-子表 t_qcbd_rproentry

- **表名称：** 工序信息-存值-子表
- **表名：** t_qcbd_rproentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 3 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 4 | ffirstcheck | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 5 | foverlapqty | 重叠批量 | numeric | 23 | 10 | √ | 0.0000000000 | 重叠批量 |
| 6 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 7 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 10 | foperationqty | 工序数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工序数量 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | fmachiningtype | 加工类型 | varchar | 5 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 13 | fchecktype | 检验方式 | varchar | 5 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 14 | foverlapunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | ffloorratio | 汇报下限比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 汇报下限比例(%) |
| 16 | fbasebatchqty | 基本批量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本批量 |
| 17 | fentrymaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 18 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 19 | fminoverlaptime | 重叠最小时间 | numeric | 23 | 10 | √ | 0.0000000000 | 重叠最小时间 |
| 20 | fminworktime | 最小加工时间 | numeric | 23 | 10 | √ | 0.0000000000 | 最小加工时间 |
| 21 | foperationid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 22 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fparentid | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 24 | fsettlementcoefficient | 结算系数 | numeric | 23 | 10 | √ | 0.0000000000 | 结算系数 |
| 25 | fissplit | 是否拆分排程 | bpchar | 1 |  | √ | '0' | 是否拆分排程 |
| 26 | fpurchasepersonid | 采购员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fsplitqty | 建议拆分数 | numeric | 23 | 10 | √ | 0.0000000000 | 建议拆分数 |
| 28 | foperationunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | fheadqty | 表头数量 | numeric | 23 | 10 | √ | 0.0000000000 | 表头数量 |
| 32 | foprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | 工序控制策略(废弃) mpdm_proctrlstrategy |
| 33 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 34 | foverlaptimeunit | 重叠时间单位 | varchar | 5 |  | √ | ' ' | 重叠时间单位,枚举: A :分钟 B :秒 |
| 35 | ftimeunit | 加工时间单位 | varchar | 5 |  | √ | ' ' | 加工时间单位,枚举: A :分钟 B :秒 |
| 36 | fisprocessoverlap | 是否工序重叠 | bpchar | 1 |  | √ | '0' | 是否工序重叠 |
| 37 | fproductionorgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fheadunitid | 表头单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 39 | fupperratio | 汇报上限比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 汇报上限比例(%) |
| 40 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fsettlementunitid | 结算单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_rprory_fid |  | fid |
| 2 | pk_qcbd_rproentry |  | fentryid |
| 3 | idx_qcbd_rprory_fseq |  | fseq |

---

## 序列关系-子表 t_qcbd_proseqrel

- **表名称：** 序列关系-子表
- **表名：** t_qcbd_proseqrel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseqrelationparname | 并行序列名称 | varchar | 50 |  | √ | ' ' | 并行序列名称 |
| 3 | ftransferprocessno | 转入工序号 | varchar | 50 |  | √ | ' ' | 转入工序号 |
| 4 | fseqrelationseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 5 | ftransferprocessname | 转入工序名称 | varchar | 50 |  | √ | ' ' | 转入工序名称 |
| 6 | fparallelration | 并行关系 | varchar | 5 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :结束-开始 C :结束-结束 D :开始-结束 |
| 7 | fseqrelationname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 8 | fturnoutprocessno | 转出工序号 | varchar | 50 |  | √ | ' ' | 转出工序号 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fturnoutprocessname | 转出工序名称 | varchar | 50 |  | √ | ' ' | 转出工序名称 |
| 11 | fseqrelationparseq | 并行序列号 | varchar | 50 |  | √ | ' ' | 并行序列号 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_prosel_fseq |  | fseq |
| 2 | pk_qcbd_proseqrel |  | fentryid |
| 3 | idx_qcbd_prosel_fid |  | fid |
