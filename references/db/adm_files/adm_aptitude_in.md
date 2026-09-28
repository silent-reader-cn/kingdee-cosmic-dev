# 资质审查-adm_aptitude_in

## 准入节点-子表 t_srm_aptitude_nodeentry

- **表名称：** 准入节点-子表
- **表名：** t_srm_aptitude_nodeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccessnodeid | 准入节点 | int8 | 64 |  | √ | 0 | [供应商准入节点 srm_accessnode](../srm_files/srm_accessnode.md) |
| 3 | fnodestatus | 是否完成 | bpchar | 1 |  | √ | ' ' | 是否完成,枚举: 1 :已完成 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fnodebilldate | fnodebilldate | timestamp | 0 |  |  | null |  |

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

## 附件-附件表 t_pur_examattachment

- **表名称：** 附件-附件表
- **表名：** t_pur_examattachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
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
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
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
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fendreason | 终止原因 | varchar | 512 |  | √ | ' ' | 终止原因 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

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
| 5 | fisenter | 是否引入 | bpchar | 1 |  | √ | ' ' | 是否引入 |
| 6 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fissourcelist | 更新货源清单 | bpchar | 1 |  | √ | '0' | 更新货源清单 |
| 8 | forgstatus | 采购组织状态 | bpchar | 1 |  | √ | ' ' | 采购组织状态,枚举: 1 :有效 2 :无效 3 :冻结 4 :退出 9 :引入中 |
| 9 | fcategorytype | 类型 | bpchar | 1 |  | √ | 'B' | 类型,枚举: A :物料 B :品类 |
| 10 | fcategorystatus | 品类状态 | bpchar | 1 |  | √ | ' ' | 品类状态,枚举: 1 :有效 2 :失效 3 :冻结 4 :退出 9 :引入中 |
| 11 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 13 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
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
| 2 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | faccounttype | 账户类型 | bpchar | 1 |  | √ | ' ' | 账户类型,枚举: 1 :基本账户 2 :请款账户 |
| 4 | faccountname | 银行账户名称 | varchar | 255 |  | √ | ' ' | 银行账户名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | faccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 8 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
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

---

## 资质评估分录-子表 t_pur_assessentry

- **表名称：** 资质评估分录-子表
- **表名：** t_pur_assessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexamcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fissatisfied | 是否满足 | varchar | 50 |  | √ | ' ' | 是否满足,枚举: 0 :是 1 :否 |
| 4 | fexamremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fassesscontent | 评估内容 | varchar | 255 |  | √ | ' ' | 评估内容 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftarget | 目标值 | varchar | 255 |  | √ | ' ' | 目标值 |
| 9 | fevafactorconfigid | 评估要素 | int8 | 64 |  | √ | 0 | [资审评估要素维护 pbd_evafactorconfig](../pbd_files/pbd_evafactorconfig.md) |

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
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fentertypeid | 准入类型 | int8 | 64 |  | √ | 0 | [准入类型 srm_biztype](../srm_files/srm_biztype.md) |
| 6 | fhassample | 已样品确认 | bpchar | 1 |  | √ | ' ' | 已样品确认 |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fisapprove | 需要供应商生效 | bpchar | 1 |  | √ | '0' | 需要供应商生效 |
| 9 | fhasmaterial | 已物料试用 | bpchar | 1 |  | √ | ' ' | 已物料试用 |
| 10 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 E :已完成 F :已终止 |
| 11 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 2 :资质审查 |
| 12 | fisautopush | fisautopush | bpchar | 1 |  | √ | '1' |  |
| 13 | fispurorg | 按组织控制 | bpchar | 1 |  | √ | ' ' | 按组织控制 |
| 14 | fischgflow | 允许调整流程 | bpchar | 1 |  | √ | ' ' | 允许调整流程 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fisscene | 需要现场评审 | bpchar | 1 |  | √ | '0' | 需要现场评审 |
| 17 | fhasapprove | 已供应商生效 | bpchar | 1 |  | √ | ' ' | 已供应商生效 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fhasscene | 已现场评审 | bpchar | 1 |  | √ | ' ' | 已现场评审 |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 23 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 24 | fisshopmall | fisshopmall | bpchar | 1 |  | √ | ' ' |  |
| 25 | fresultremark | 备注 | text | 0 |  |  | ' ' | 备注 |
| 26 | fissample | 需要样品确认 | bpchar | 1 |  | √ | '0' | 需要样品确认 |
| 27 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 28 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 30 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 32 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 33 | fiscategory | 按品类控制 | bpchar | 1 |  | √ | ' ' | 按品类控制 |
| 34 | fcertifiapplyid | 认证申请单号 | int8 | 64 |  | √ | 0 | [供应商认证申请编号 pbd_certificationapplyno](../pbd_files/pbd_certificationapplyno.md) |
| 35 | fexamresult | 资审结果 | bpchar | 1 |  | √ | ' ' | 资审结果,枚举: 0 :通过 1 :不通过 |
| 36 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 0 :邀约注册 1 :公开注册 |
| 37 | fismaterial | 需要物料试用 | bpchar | 1 |  | √ | '0' | 需要物料试用 |
| 38 | fissuppcolla | fissuppcolla | bpchar | 1 |  | √ | '0' |  |
| 39 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
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
