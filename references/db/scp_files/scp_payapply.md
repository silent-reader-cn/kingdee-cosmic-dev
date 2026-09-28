# 收款通知-scp_payapply

## 收款通知分录-子表 t_pur_payapplyentry

- **表名称：** 收款通知分录-子表
- **表名：** t_pur_payapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fapproveamt | 预计收款金额 | numeric | 23 | 10 | √ | 0.000000 | 预计收款金额 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 6 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | fapplyamt | 申请金额 | numeric | 23 | 10 | √ | 0.000000 | 申请金额 |
| 10 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fpayeeacc | 收款银行账号 | varchar | 50 |  | √ | ' ' | 收款银行账号 |
| 12 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | ftraceid | 跟踪号（废弃） | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 14 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目号 pur_project](../pbd_files/pur_project.md) |
| 15 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 16 | fexpectdate | 预计收款日期 | timestamp | 0 |  |  | null | 预计收款日期 |
| 17 | fpurpose | 用途 | varchar | 50 |  | √ | ' ' | 用途 |
| 18 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 20 | fpayamt | 应收金额 | numeric | 23 | 10 | √ | 0.000000 | 应收金额 |
| 21 | fduedate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 22 | fpayeebank | 收款开户银行 | varchar | 50 |  | √ | ' ' | 收款开户银行 |
| 23 | fmaterialnametext | fmaterialnametext | varchar | 255 |  | √ | ' ' |  |
| 24 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 25 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 26 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 29 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_payapplyentry_pkey |  | fentryid |
| 2 | idx_pur_payapplyentry_fid_fseq |  | fid,fseq |

---

## 收款通知-多语言表 t_pur_payapply_l

- **表名称：** 收款通知-多语言表
- **表名：** t_pur_payapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_payapply_l_fid |  | fid,flocaleid |
| 2 | t_pur_payapply_l_pkey |  | fpkid |

---

## 收款通知-分表 t_pur_payapply_a

- **表名称：** 收款通知-分表
- **表名：** t_pur_payapply_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_payapply_a_pkey |  | fid |
| 2 | idx_pur_payapply_a_fcreatetime |  | fcreatetime |

---

## 收款通知分录-分表 t_pur_payapplyentry_a

- **表名称：** 收款通知分录-分表
- **表名：** t_pur_payapplyentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocpayamt | 应付金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 应付金额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 5 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 6 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 7 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 8 | flocapplyamt | 申请金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 申请金额(本位币) |
| 9 | flocapproveamt | 核准金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 核准金额(本位币) |
| 10 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 11 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 12 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 15 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_payapplyentry_a_pkey |  | fentryid |
| 2 | idx_pur_payapplyentry_a_fid |  | fid |

---

## 收款通知-主表 t_pur_payapply

- **表名称：** 收款通知-主表
- **表名：** t_pur_payapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | forgid | 申请方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 8 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :内部采购 |
| 10 | fsumpayamt | 合计应收金额 | numeric | 23 | 10 | √ | 0.000000 | 合计应收金额 |
| 11 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 18 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 19 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 pur_paycond](../basedata_files/pur_paycond.md) |
| 21 | fexpectdate | 预计收款日期 | timestamp | 0 |  |  | null | 预计收款日期 |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fdelisupid | 送货方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 24 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 26 | fsupplierid | 销售方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 29 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 30 | fsumapproveamt | 预计收款金额 | numeric | 23 | 10 | √ | 0.000000 | 预计收款金额 |
| 31 | fsumapplyamt | 申请金额 | numeric | 23 | 10 | √ | 0.000000 | 申请金额 |
| 32 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 33 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |
| 35 | fcontacterid | 销售方联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 36 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_payapply_pkey |  | fid |
| 2 | idx_pur_payapply_fbilldate |  | fbilldate |
| 3 | idx_pur_payapply_fbillno |  | fbillno |
| 4 | idx_pur_payapply_fbizpartnerid |  | fbizpartnerid |
