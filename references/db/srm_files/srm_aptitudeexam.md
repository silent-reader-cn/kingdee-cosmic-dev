# 资质审查-srm_aptitudeexam

## 关联子实体-子表 t_pur_aptitude_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_aptitude_lk

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
| 1 | idx_pur_aptitude_lk_fk |  | fid |
| 2 | pk_pur_aptitude_lk |  | fpkid |

---

## 资质审查-反写记录表 t_pur_aptitude_wb

- **表名称：** 资质审查-反写记录表
- **表名：** t_pur_aptitude_wb

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
| 1 | pk_pur_aptitude_wb |  | fentryid |
| 2 | idx_pur_aptitude_wb_fk |  | fid |

---

## 资质评估分录-子表 t_pur_assessentry

- **表名称：** 资质评估分录-子表
- **表名：** t_pur_assessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexamcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fissatisfied | 是否满足 | varchar | 50 |  | √ | ' ' | 是否满足,枚举: 0 :是 1 :否 |
| 4 | fexamremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fassesscontent | 评估内容 | varchar | 255 |  | √ | ' ' | 评估内容 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftarget | 目标值 | varchar | 255 |  | √ | ' ' | 目标值 |
| 9 | fevafactorconfigid | 评估要素 | int8 | 64 |  | √ | 0 | 资审评估要素维护 pbd_evafactorconfig |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_assessentry |  | fentryid |
| 2 | idx_pur_assessentry |  | fid |

---

## 资质审查-主表 t_pur_aptitude

- **表名称：** 资质审查-主表
- **表名：** t_pur_aptitude

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 供应商分类 | int8 | 64 |  | √ | 0 | 供应商分类 bd_suppliergroup |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fentertypeid | 准入类型 | int8 | 64 |  | √ | 0 | 准入类型 srm_biztype |
| 6 | fhassample | 已样品确认 | bpchar | 1 |  | √ | ' ' | 已样品确认 |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fisapprove | 需要供应商生效 | bpchar | 1 |  | √ | '0' | 需要供应商生效 |
| 9 | fhasmaterial | 已物料试用 | bpchar | 1 |  | √ | ' ' | 已物料试用 |
| 10 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 E :已完成 |
| 11 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 2 :资质审查 |
| 12 | fisautopush | 自动下推业务单据 | bpchar | 1 |  | √ | '1' | 自动下推业务单据 |
| 13 | fispurorg | 按组织控制 | bpchar | 1 |  | √ | ' ' | 按组织控制 |
| 14 | fischgflow | 允许调整流程 | bpchar | 1 |  | √ | ' ' | 允许调整流程 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 16 | fisscene | 需要现场评审 | bpchar | 1 |  | √ | '0' | 需要现场评审 |
| 17 | fhasapprove | 已供应商生效 | bpchar | 1 |  | √ | ' ' | 已供应商生效 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fremark | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 20 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fhasscene | 已现场评审 | bpchar | 1 |  | √ | ' ' | 已现场评审 |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 23 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 24 | fisshopmall | 允许入驻商城 | bpchar | 1 |  | √ | ' ' | 允许入驻商城 |
| 25 | fresultremark | 备注 | text | 0 |  |  | ' ' | 备注 |
| 26 | fissample | 需要样品确认 | bpchar | 1 |  | √ | '0' | 需要样品确认 |
| 27 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 32 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 33 | fiscategory | 按品类控制 | bpchar | 1 |  | √ | ' ' | 按品类控制 |
| 34 | fcertifiapplyid | 认证申请单号 | int8 | 64 |  | √ | 0 | 供应商认证申请编号 pbd_certificationapplyno |
| 35 | fexamresult | 资审结果 | bpchar | 1 |  | √ | ' ' | 资审结果,枚举: 0 :通过 1 :不通过 |
| 36 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 0 :邀约注册 1 :公开注册 |
| 37 | fismaterial | 需要物料试用 | bpchar | 1 |  | √ | '0' | 需要物料试用 |
| 38 | fissuppcolla | 启用采购协同 | bpchar | 1 |  | √ | '0' | 启用采购协同 |
| 39 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 40 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_aptitude_fbillno |  | fbillno |
| 2 | t_pur_aptitude_pkey |  | fid |
| 3 | idx_pur_aptitude_fbilldate |  | fbilldate |

---

## 准入节点-子表 t_srm_aptitude_nodeentry

- **表名称：** 准入节点-子表
- **表名：** t_srm_aptitude_nodeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccessnodeid | 准入节点 | int8 | 64 |  | √ | 0 | 供应商准入节点 srm_accessnode |
| 3 | fnodestatus | 是否完成 | bpchar | 1 |  | √ | ' ' | 是否完成,枚举: 1 :已完成 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fnodebilldate | 节点业务日期 | timestamp | 0 |  |  | null | 节点业务日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_aptitude_nodeentry |  | fentryid |
| 2 | idx_aptitudeentry_id_seq |  | fid,fseq |
| 3 | idx_aptitudeentry_nodeid |  | faccessnodeid |

---

## 资质审查-关联追踪表 t_pur_aptitude_tc

- **表名称：** 资质审查-关联追踪表
- **表名：** t_pur_aptitude_tc

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
| 1 | idx_pur_aptitude_tc_tbill |  | ftbillid |
| 2 | pk_pur_aptitude_tc |  | fid |
| 3 | idx_pur_aptitude_tc_tid |  | ftid |

---

## 附件-附件表 t_pur_examattachment

- **表名称：** 附件-附件表
- **表名：** t_pur_examattachment

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
| 1 | pk_t_pur_examattachment |  | fpkid |
| 2 | idx_t_pur_examattachment |  | fbasedataid |

---

## 资质审查-多语言表 t_pur_aptitude_l

- **表名称：** 资质审查-多语言表
- **表名：** t_pur_aptitude_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 申请原因 | varchar | 255 |  | √ | ' ' | 申请原因 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_aptitude_lfid |  | fid,flocaleid |
| 2 | t_pur_aptitude_l_pkey |  | fpkid |

---

## 资质审查-分表 t_pur_aptitude_a

- **表名称：** 资质审查-分表
- **表名：** t_pur_aptitude_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 8 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_aptitude_a_pkey |  | fid |
| 2 | idx_pur_aptitude_a_ftime |  | fcreatetime |

---

## 品类分录-子表 t_pur_aptitudeentry

- **表名称：** 品类分录-子表
- **表名：** t_pur_aptitudeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | foriginsupplier | 原厂商名称 | varchar | 255 |  | √ | ' ' | 原厂商名称 |
| 5 | fisenter | 是否引入 | bpchar | 1 |  | √ | ' ' | 是否引入,枚举: 1 :引入 0 :不引入 |
| 6 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fissourcelist | 更新货源清单 | bpchar | 1 |  | √ | '0' | 更新货源清单 |
| 8 | forgstatus | 当前组织状态 | bpchar | 1 |  | √ | ' ' | 当前组织状态,枚举: 1 :有效 2 :无效 3 :冻结 4 :退出 9 :引入中 |
| 9 | fcategorytype | 类型 | bpchar | 1 |  | √ | 'B' | 类型,枚举: A :物料 B :品类 |
| 10 | fcategorystatus | 当前品类状态 | bpchar | 1 |  | √ | ' ' | 当前品类状态,枚举: 1 :有效 2 :无效 3 :冻结 4 :退出 9 :引入中 |
| 11 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 13 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_aptitude_fid_fseq |  | fid,fseq |
| 2 | t_pur_aptitudeentry_pkey |  | fentryid |

---

## 银行分录-子表 t_pur_aptitudebank

- **表名称：** 银行分录-子表
- **表名：** t_pur_aptitudebank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | faccounttype | 账户类型 | bpchar | 1 |  | √ | ' ' | 账户类型,枚举: 1 :基本账户 2 :请款账户 |
| 4 | faccountname | 银行账户名称 | varchar | 255 |  | √ | ' ' | 银行账户名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | faccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 8 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fisdefault | 默认 | bpchar | 1 |  | √ | ' ' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_aptitudebank_pkey |  | fentryid |
| 2 | idx_pur_aptitudebank_fidseq |  | fid,fseq |
