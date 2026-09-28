# 索赔单-scp_claim

## 索赔单-关联追踪表 t_pur_claim_tc

- **表名称：** 索赔单-关联追踪表
- **表名：** t_pur_claim_tc

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
| 1 | idx_pur_claim_tc_tbill |  | ftbillid |
| 2 | idx_pur_claim_tc_tid |  | ftid |
| 3 | pk_pur_claim_tc |  | fid |

---

## 索赔明细-子表 t_pur_claimentry

- **表名称：** 索赔明细-子表
- **表名：** t_pur_claimentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 3 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | freceiptbillno | 收货单号 | varchar | 80 |  | √ | ' ' | 收货单号 |
| 8 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 9 | fclaimamount | 本次索赔金额 | numeric | 23 | 10 | √ | 0 | 本次索赔金额 |
| 10 | fmainbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 11 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 12 | fremark | 说明 | varchar | 512 |  | √ | ' ' | 说明 |
| 13 | fclassify | 分类 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 14 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 15 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 17 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 19 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 22 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 23 | fclaimtax | 本次索赔税额 | numeric | 23 | 10 | √ | 0 | 本次索赔税额 |
| 24 | fmainbillentryid | 核心单据行ID | varchar | 50 |  | √ | ' ' | 核心单据行ID |
| 25 | fclaimtaxamount | 本次索赔价税合计 | numeric | 23 | 10 | √ | 0 | 本次索赔价税合计 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 28 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_claimentry |  | fentryid |
| 2 | idx_pur_claimentry_fid_fseq |  | fid,fseq |
| 3 | idx_pur_claimentry_fmaterialid |  | fmaterialid |

---

## 索赔单-反写记录表 t_pur_claim_wb

- **表名称：** 索赔单-反写记录表
- **表名：** t_pur_claim_wb

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
| 1 | pk_pur_claim_wb |  | fentryid |
| 2 | idx_pur_claim_wb_fk |  | fid |

---

## 关联子实体-子表 t_pur_claimentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_claimentry_lk

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
| 1 | pk_pur_claimentry_lk |  | fpkid |
| 2 | idx_pur_claimentry_lk_fk |  | fentryid |

---

## 申诉附件-附件表 t_pur_claimrecordatta

- **表名称：** 申诉附件-附件表
- **表名：** t_pur_claimrecordatta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_claimrecordatta |  | fpkid |
| 2 | idx_pur_claimrecord_fentryid |  | fentryid |
| 3 | idx_pur_claimrecord_fbaseid |  | fbasedataid |

---

## 关联子实体-子表 t_pur_claim_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_claim_lk

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
| 1 | idx_pur_claim_lk_fk |  | fid |
| 2 | pk_pur_claim_lk |  | fpkid |

---

## 索赔单-主表 t_pur_claim

- **表名称：** 索赔单-主表
- **表名：** t_pur_claim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | forgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fclaimtype | 索赔类型 | bpchar | 1 |  | √ | ' ' | 索赔类型,枚举: 1 :品质扣款 2 :其他扣款 |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcancelid | 取消人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbillno | 索赔单号 | varchar | 80 |  | √ | ' ' | 索赔单号 |
| 12 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fpurorgid | 发起方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 20 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fcfmstatus | 索赔状态 | bpchar | 1 |  | √ | ' ' | 索赔状态,枚举: A :待确认 B :已确认 G :已申诉 Z :已取消 |
| 23 | fcanceldate | 取消日期 | timestamp | 0 |  |  | null | 取消日期 |
| 24 | fclaimdesc | 索赔说明 | varchar | 512 |  | √ | ' ' | 索赔说明 |
| 25 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 26 | fhopendate | 要求反馈日期 | timestamp | 0 |  |  | null | 要求反馈日期 |
| 27 | fsumtaxamount | 索赔价税合计 | numeric | 23 | 10 | √ | 0 | 索赔价税合计 |
| 28 | fversionstatus | 版本状态 | bpchar | 1 |  | √ | '1' | 版本状态 |
| 29 | fsrcbilltype | 来源单据类型 | bpchar | 1 |  | √ | ' ' | 来源单据类型,枚举: 0 :新增 1 :质量问题通知 2 :采购收货 |
| 30 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_claim_fbilldate |  | fbilldate |
| 2 | idx_pur_claim_fbizid |  | fbizpartnerid |
| 3 | idx_pur_claim_forgid |  | fpurorgid |
| 4 | idx_pur_claim_fbillno |  | fbillno |
| 5 | pk_pur_claim |  | fid |

---

## 申诉记录-子表 t_pur_claimrecordentry

- **表名称：** 申诉记录-子表
- **表名：** t_pur_claimrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclaimexplain | 申诉说明 | varchar | 512 |  | √ | ' ' | 申诉说明 |
| 3 | fclaimantid | 申诉人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdisposaltype | 处理方式 | bpchar | 1 |  | √ | ' ' | 处理方式,枚举: 1 :变更索赔 2 :取消索赔 3 :不处理 |
| 5 | fdisposalerid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fdisposalnote | 处理意见 | varchar | 512 |  | √ | ' ' | 处理意见 |
| 7 | fdisposalertime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fclaimanttime | 申诉时间 | timestamp | 0 |  |  | null | 申诉时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_claimrecord_fid_fseq |  | fid,fseq |
| 2 | pk_pur_claimrecordentry |  | fentryid |
