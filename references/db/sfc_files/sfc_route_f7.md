# 工艺路线F7(废弃)-sfc_route_f7

## 工序活动-子表 t_pdm_routeactive

- **表名称：** 工序活动-子表
- **表名：** t_pdm_routeactive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factscheduling | 排程 | bpchar | 1 |  | √ | '0' | 排程 |
| 2 | fstandardformula1id | 标准公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 3 | fprocessno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | factivityid | 活动编码 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 6 | foperationnumber | 工序名称 | varchar | 50 |  | √ | ' ' | 工序名称 |
| 7 | fprocessstage | 工序阶段 | bpchar | 1 |  | √ | ' ' | 工序阶段,枚举: A :排队阶段 B :准备阶段 C :加工阶段 D :拆卸阶段 E :等待阶段 F :转移阶段 |
| 8 | fminformulaid | 最小值公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 9 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: A :生产 B :成本 C :工资 |
| 10 | fstandardformulaid | 标准公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 11 | factresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 12 | fminformula1id | 最小值公式 | int8 | 64 |  | √ | 0 | 工序活动公式(废弃) mpdm_processformula |
| 13 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_routeactive_pkey |  | fdetailid |
| 2 | idx_pdm_routeactive |  | fentryid,fseq |

---

## 工艺路线F7(废弃)-主表 t_pdm_route

- **表名称：** 工艺路线F7(废弃)-主表
- **表名：** t_pdm_route

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 工艺路线分组 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_processgroup |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmaterialgroupid | 物料控制组 | int8 | 64 |  | √ | 0 | 物料控制组 bd_materialcontrolgroup |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcancelerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | froutereplace | 替代号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_routereplace |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcanceltime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fbomversionid | BOM | int8 | 64 |  | √ | 0 | 制造BOMf7(废弃) sfc_mftbomf7 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fversionid | 版本 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_processversion |
| 24 | fprocesstype | 工艺类型 | bpchar | 1 |  | √ | ' ' | 工艺类型,枚举: A :物料 B :物料组 C :通用 |
| 25 | fctrlstrategy | 控制策略 | varchar | 100 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 工艺路线编码 | varchar | 100 |  | √ | ' ' | 工艺路线编码 |
| 28 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 29 | fismainprocess | 主工艺路线 | bpchar | 1 |  | √ | '1' | 主工艺路线 |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_route |  | fnumber,fcreateorgid |
| 2 | idx_t_pdm_route_createorg |  | fcreateorgid |
| 3 | t_pdm_route_pkey |  | fid |
| 4 | idx_t_pdm_route_master |  | fmasterid |

---

## 工艺路线F7(废弃)-使用范围位图表 t_pdm_route_m

- **表名称：** 工艺路线F7(废弃)-使用范围位图表
- **表名：** t_pdm_route_m

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
| 1 | pk_t_pdm_route_m |  | forgid |

---

## 工艺路线F7(废弃)-多语言表 t_pdm_route_l

- **表名称：** 工艺路线F7(废弃)-多语言表
- **表名：** t_pdm_route_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工艺路线名称 | varchar | 100 |  | √ | ' ' | 工艺路线名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_route_l_pkey |  | fpkid |
| 2 | idx_pdm_route_l |  | fid,flocaleid |

---

## 工艺路线F7(废弃)-使用范围表 t_pdm_route_u

- **表名称：** 工艺路线F7(废弃)-使用范围表
- **表名：** t_pdm_route_u

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
| 1 | idx_t_pdm_route_u_uo |  | fuseorgid |
| 2 | t_pdm_route_u_pkey |  | fdataid,fuseorgid |

---

## 子单据体-子表 t_pdm_routesource

- **表名称：** 子单据体-子表
- **表名：** t_pdm_routesource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fresourceid | 资源编码 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
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
| 1 | t_pdm_routesource_pkey |  | fdetailid |
| 2 | idx_pdm_routesource |  | fentryid,fseq |

---

## 工序信息-存值-子表 t_pdm_routeoperation

- **表名称：** 工序信息-存值-子表
- **表名：** t_pdm_routeoperation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperationno | 工序号 | varchar | 100 |  | √ | ' ' | 工序号 |
| 3 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 4 | ffirstcheck | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 5 | foverlapqty | 重叠批量 | numeric | 23 | 10 | √ | 0.0000000000 | 重叠批量 |
| 6 | fstoragepoint | fstoragepoint | bpchar | 1 |  | √ | '0' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foperationqty | 工序数量 | numeric | 23 | 10 | √ | 0.0000000000 | 工序数量 |
| 9 | fchecktype | 检验方式 | varchar | 50 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 10 | foverlapunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | ffloorratio | 汇报下限比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 汇报下限比例(%) |
| 12 | fbasebatchqty | 基本批量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本批量 |
| 13 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 14 | fminoverlaptime | 重叠最小时间 | numeric | 23 | 10 | √ | 0.0000000000 | 重叠最小时间 |
| 15 | fminworktime | 最小加工时间 | numeric | 23 | 10 | √ | 0.0000000000 | 最小加工时间 |
| 16 | foperationid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 17 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fparentid | 工序序列 | varchar | 100 |  | √ | ' ' | 工序序列 |
| 19 | fissplit | 是否拆分排程 | bpchar | 1 |  | √ | '0' | 是否拆分排程 |
| 20 | fsplitqty | 建议拆分数 | numeric | 23 | 10 | √ | 0.0000000000 | 建议拆分数 |
| 21 | foperationunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fheadqty | 表头数量 | numeric | 23 | 10 | √ | 0.0000000000 | 表头数量 |
| 23 | foprctrlstrategy | 工序控制策略 | varchar | 100 |  | √ | ' ' | 工序控制策略(废弃) mpdm_proctrlstrategy |
| 24 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 25 | foverlaptimeunit | 重叠时间单位 | bpchar | 1 |  | √ | ' ' | 重叠时间单位,枚举: A :分钟 B :秒 |
| 26 | fbottleprocedure | fbottleprocedure | bpchar | 1 |  | √ | '0' |  |
| 27 | ftimeunit | 加工时间单位 | bpchar | 1 |  | √ | ' ' | 加工时间单位,枚举: A :分钟 B :秒 |
| 28 | fisprocessoverlap | 是否工序重叠 | bpchar | 1 |  | √ | '0' | 是否工序重叠 |
| 29 | fproductionorgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fheadunitid | 表头单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fupperratio | 汇报上限比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 汇报上限比例(%) |
| 32 | fismilestoneprocess | fismilestoneprocess | bpchar | 1 |  | √ | '0' |  |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fcollaborative | fcollaborative | bpchar | 1 |  | √ | '0' |  |
| 35 | fworkstationid | fworkstationid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_routeoperation_pkey |  | fentryid |
| 2 | idx_pdm_routeoperation |  | fid,fseq |

---

## 工序信息-存值-分表 t_pdm_routeoperation_e

- **表名称：** 工序信息-存值-分表
- **表名：** t_pdm_routeoperation_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurchaserid | fpurchaserid | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 4 | ftaxpricea | ftaxpricea | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fsettlementcoefficient | 结算系数 | numeric | 23 | 10 | √ | 0.0000000000 | 结算系数 |
| 6 | fpurchasepersonid | 采购员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 8 | ftaxpriceb | ftaxpriceb | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 10 | fpricea | fpricea | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | fpriceb | fpriceb | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmachiningtype | 加工类型 | bpchar | 4 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 16 | fentrymaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | fcurrencyfield | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fsettlementunitid | 结算单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_routeoperation_e_pkey |  | fentryid |
| 2 | idx_pdm_routeoperation_e |  | fid |

---

## 工序序列-子表 t_pdm_routeprocess

- **表名称：** 工序序列-子表
- **表名：** t_pdm_routeprocess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessseqname | 序列名称 | varchar | 100 |  | √ | ' ' | 序列名称 |
| 3 | fprocessseqtype | 序列类型 | bpchar | 1 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | frelation | 并行关系 | varchar | 50 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :开始-结束 C :结束-开始 D :结束-结束 |
| 6 | freference | 参照序列 | varchar | 50 |  | √ | ' ' | 参照序列 |
| 7 | foutput | 转出工序 | varchar | 50 |  | √ | ' ' | 转出工序 |
| 8 | fprocessseqremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | finput | 转入工序 | varchar | 50 |  | √ | ' ' | 转入工序 |
| 11 | fprocessseq | 序列号 | varchar | 100 |  | √ | ' ' | 序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_routeprocess_pkey |  | fentryid |
| 2 | idx_pdm_routeprocess |  | fid,fseq |

---

## 序列关系-子表 t_pdm_routerelation

- **表名称：** 序列关系-子表
- **表名：** t_pdm_routerelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseqrelationparname | 并行序列名称 | varchar | 100 |  | √ | ' ' | 并行序列名称 |
| 3 | ftransferprocessno | 转入工序号 | varchar | 100 |  | √ | ' ' | 转入工序号 |
| 4 | fseqrelationseq | 序列号 | varchar | 100 |  | √ | ' ' | 序列号 |
| 5 | ftransferprocessname | 转入工序名称 | varchar | 100 |  | √ | ' ' | 转入工序名称 |
| 6 | fparallelration | 并行关系 | bpchar | 1 |  | √ | ' ' | 并行关系,枚举: A :开始-开始 B :结束-开始 C :结束-结束 D :开始-结束 |
| 7 | fseqrelationname | 序列名称 | varchar | 100 |  | √ | ' ' | 序列名称 |
| 8 | fturnoutprocessno | 转出工序号 | varchar | 100 |  | √ | ' ' | 转出工序号 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fturnoutprocessname | 转出工序名称 | varchar | 100 |  | √ | ' ' | 转出工序名称 |
| 11 | fseqrelationparseq | 并行序列号 | varchar | 100 |  | √ | ' ' | 并行序列号 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_routerelation_pkey |  | fentryid |
| 2 | idx_pdm_routerelation |  | fid,fseq |
