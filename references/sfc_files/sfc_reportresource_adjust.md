# 汇报资源调整单(废弃)-sfc_reportresource_adjust

## 汇报资源调整单(废弃)-关联追踪表 t_sfc_sourceadjust_tc

- **表名称：** 汇报资源调整单(废弃)-关联追踪表
- **表名：** t_sfc_sourceadjust_tc

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
| 1 | pk_sfc_sourceadjust_tc |  | fid |
| 2 | idx_sfc_sourceadjust_tc_tbill |  | ftbillid |
| 3 | idx_sfc_sourceadjust_tc_tid |  | ftid |

---

## 关联子实体-子表 t_sfc_adjustentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_adjustentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_adjustentry_lk_fk |  | fentryid |
| 2 | pk_sfc_adjustentry_lk |  | fpkid |

---

## 汇报资源调整单(废弃)-反写记录表 t_sfc_sourceadjust_wb

- **表名称：** 汇报资源调整单(废弃)-反写记录表
- **表名：** t_sfc_sourceadjust_wb

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
| 1 | idx_sfc_sourceadjust_wb_fk |  | fid |
| 2 | pk_sfc_sourceadjust_wb |  | fentryid |

---

## 活动-子表 t_sfc_reportsubentry

- **表名称：** 活动-子表
- **表名：** t_sfc_reportsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | frepactualqty | 实际总量 | numeric | 23 | 10 | √ | 0.0000000000 | 实际总量 |
| 2 | freportactentity | 工序活动-汇报分录行ID | varchar | 50 |  | √ | ' ' | 工序活动-汇报分录行ID |
| 3 | fsourceid | 源单分录id | varchar | 50 |  | √ | ' ' | 源单分录id |
| 4 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | factstandardformulaid | factstandardformulaid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fadjustactualqty | 调整实际总量 | numeric | 23 | 10 | √ | 0.0000000000 | 调整实际总量 |
| 8 | frepbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | frepactualfinishtime | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 10 | frepactivityid | 活动编码 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 11 | frepresources | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 12 | frepactualbegintime | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_reportsub_fentryid |  | fentryid |
| 2 | pk_sfc_reportsubentry |  | fdetailid |

---

## 汇总-多语言表 t_sfc_adjustentry_l

- **表名称：** 汇总-多语言表
- **表名：** t_sfc_adjustentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_adjustentry_l_fentryid |  | fentryid,flocaleid |
| 2 | pk_sfc_adjustentry_l |  | fpkid |

---

## 汇报资源调整单(废弃)-多语言表 t_sfc_resourceadjust_l

- **表名称：** 汇报资源调整单(废弃)-多语言表
- **表名：** t_sfc_resourceadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_resourceadjust_l |  | fpkid |
| 2 | idx_sfc_resourceadjust_fid |  | fid,flocaleid |

---

## 汇报资源调整单(废弃)-主表 t_sfc_resourceadjust

- **表名称：** 汇报资源调整单(废弃)-主表
- **表名：** t_sfc_resourceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fischargeoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 9 | fadjustdate | 调整时间 | timestamp | 0 |  |  | null | 调整时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fproductworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 12 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 16 | fbilltypeid | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: 10020 :工序汇报单 10030 :工单汇报单 10040 :工序汇报资源调整单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_resourceadjust |  | fid |
| 2 | idx_sfc_resourceadjust_fbillno |  | fbillno |

---

## 关联子实体-子表 t_sfc_reportsubentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_reportsubentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_reportsubentry_lk |  | fpkid |
| 2 | idx_sfc_reportsubentry_lk_fk |  | fdetailid |

---

## 汇总-子表 t_sfc_adjustentry

- **表名称：** 汇总-子表
- **表名：** t_sfc_adjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmanufacturebill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 3 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 4 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fwarehousepoint | 入库点 | bpchar | 1 |  | √ | '0' | 入库点 |
| 6 | fmanufacturebillrow | 生产工单行号 | int8 | 64 |  | √ | 0 | 生产工单行号 |
| 7 | forderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 10 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 11 | fcompletqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 12 | foprparent | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 13 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 14 | foprworkcenterid | foprworkcenterid | int8 | 64 |  | √ | 0 |  |
| 15 | foprunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fmanftechno | 工序计划编码 | int8 | 64 |  | √ | 0 | 工序计划f7(废弃) sfc_manftech_head_f7 |
| 17 | fmanftechentry | 工序计划分录ID | varchar | 50 |  | √ | ' ' | 工序计划分录ID |
| 18 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 19 | foproperationid | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 20 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fmanufactureentryid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录F7 sfc_mftorder_f7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_adjustentry_fid |  | fid |
| 2 | idx_adentry_fconfiguredcode |  | fconfiguredcodeid |
| 3 | pk_sfc_adjustentry |  | fentryid |
| 4 | idx_adentry_ftracknumber |  | ftracknumberid |
