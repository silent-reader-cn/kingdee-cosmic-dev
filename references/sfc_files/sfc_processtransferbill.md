# 工序转移单（废弃）-sfc_processtransferbill

## 工序转移单（废弃）-关联追踪表 t_sfc_processtransfer_tc

- **表名称：** 工序转移单（废弃）-关联追踪表
- **表名：** t_sfc_processtransfer_tc

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
| 1 | idx_sfc_processtransfer_tc_tid |  | ftid |
| 2 | idx_sfc_processtransfer_tc_tbill |  | ftbillid |
| 3 | pk_sfc_processtransfer_tc |  | fid |

---

## 工序转移单（废弃）-主表 t_sfc_processtransfer

- **表名称：** 工序转移单（废弃）-主表
- **表名：** t_sfc_processtransfer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 3 | forgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 5 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 10 | fdate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 11 | fstrandirection | 转移方向 | bpchar | 1 |  | √ | ' ' | 转移方向,枚举: A :主组织-协作组织 B :协作组织-协作组织 C :协作组织-主组织 D :主组织-主组织 |
| 12 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 13 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 14 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 22 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 25 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processtransfer |  | fid |
| 2 | idx_sfc_protransfer_billno |  | fbillno |

---

## 关联子实体-子表 t_sfc_processtransfer_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_processtransfer_lk

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
| 1 | pk_sfc_processtransfer_lk |  | fpkid |
| 2 | idx_sfc_processtransfer_lk_fk |  | fid |

---

## 工序转移单（废弃）-反写记录表 t_sfc_processtransfer_wb

- **表名称：** 工序转移单（废弃）-反写记录表
- **表名：** t_sfc_processtransfer_wb

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
| 1 | idx_sfc_processtransfer_wb_fk |  | fid |
| 2 | pk_sfc_processtransfer_wb |  | fentryid |

---

## 工序转移单（废弃）-分表 t_sfc_processtransfer_t

- **表名称：** 工序转移单（废弃）-分表
- **表名：** t_sfc_processtransfer_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finbizuser | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | findepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 5 | ftransferqty | 转移数量 | numeric | 23 | 10 | √ | 0 | 转移数量 |
| 6 | finproplanid | 工序计划_不显示，带数据 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 7 | foutdepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | finproplanentryid | 工序计划分录_不显示，带数据 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 9 | foutproplanbillid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 10 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 11 | foutprocessunit | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | foutorgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | foutbizuser | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | finorgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fcolprice | 协作单价 | numeric | 23 | 10 | √ | 0 | 协作单价 |
| 16 | foutproplanid | 工序计划_不显示，带数据 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 17 | fpriceunit | 计价单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | finproplanbillid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 19 | fsettleqty | 已结算数量 | numeric | 23 | 10 | √ | 0 | 已结算数量 |
| 20 | fsettlebillqty | 生成结算单数量 | numeric | 23 | 10 | √ | 0 | 生成结算单数量 |
| 21 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 22 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 23 | foutproplanentryid | 工序计划分录_不显示，带数据 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processtransfer_t |  | fid |
| 2 | idx_sfc_protran_t_outdep |  | foutdepartid |
| 3 | idx_sfc_protran_t_indep |  | findepartid |
