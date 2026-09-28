# 认证报告-adm_approve_in

## 品类节点子分录-子表 t_srm_approvedetail

- **表名称：** 品类节点子分录-子表
- **表名：** t_srm_approvedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccessnodeid | 准入节点 | int8 | 64 |  | √ | 0 | [供应商准入节点 srm_accessnode](../srm_files/srm_accessnode.md) |
| 2 | fnodestatus | 结果 | bpchar | 1 |  | √ | ' ' | 结果,枚举: 0 :未开始 1 :合格 2 :不合格 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnodebillno | 单号 | varchar | 50 |  | √ | ' ' | 单号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_approvedetail |  | fdetailid |
| 2 | idx_approvedetail_entryid_seq |  | fentryid,fseq |
| 3 | idx_approvedetail_nodeid |  | faccessnodeid |

---

## 认证报告-主表 t_pur_approve

- **表名称：** 认证报告-主表
- **表名：** t_pur_approve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscenenoid | 现场评审单号 | int8 | 64 |  | √ | 0 | [现场评审单号 srm_scenebillno](../srm_files/srm_scenebillno.md) |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fgroupid | 供应商分类 | int8 | 64 |  | √ | 0 | [供应商分类 bd_suppliergroup](../basedata_files/bd_suppliergroup.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 6 | fcertifiapply | 认证申请单号 | int8 | 64 |  | √ | 0 | [供应商认证申请编号 pbd_certificationapplyno](../pbd_files/pbd_certificationapplyno.md) |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 10 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 11 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 12 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 13 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 F :已终止 |
| 14 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 15 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 6 :供方生效 |
| 16 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :邀约注册 1 :公开注册 |
| 17 | forgstatus | forgstatus | bpchar | 1 |  | √ | ' ' |  |
| 18 | faptitudenoid | 资质审查单号 | int8 | 64 |  | √ | 0 | [资质审查单号 srm_aptitudebillno](../srm_files/srm_aptitudebillno.md) |
| 19 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_approve_fbillno |  | fbillno |
| 2 | t_pur_approve_pkey |  | fid |
| 3 | idx_pur_approve_fbilldate |  | fbilldate |
| 4 | idx_pur_approve_aptitudeid |  | faptitudenoid |

---

## 品类分录-子表 t_pur_approveentry

- **表名称：** 品类分录-子表
- **表名：** t_pur_approveentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 5 | fissourcelist | 是否更新货源清单 | bpchar | 1 |  | √ | '0' | 是否更新货源清单 |
| 6 | fcategorytype | 类型 | bpchar | 1 |  | √ | 'B' | 类型,枚举: A :物料 B :品类 |
| 7 | fcategorystatus | 品类引入状态 | bpchar | 1 |  | √ | ' ' | 品类引入状态,枚举: 1 :有效 2 :无效 |
| 8 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 10 | ftryresult | 试用结果 | bpchar | 1 |  | √ | ' ' | 试用结果,枚举: 1 :合格 2 :不合格 3 :物料未试用 |
| 11 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | ftestresult | 试样结果 | bpchar | 1 |  | √ | ' ' | 试样结果,枚举: 1 :合格 2 :不合格 3 :样品未确认 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ftrynoid | 物料试用单号 | int8 | 64 |  | √ | 0 | [物料试用单号 srm_materialbillno](../srm_files/srm_materialbillno.md) |
| 15 | fsamplenoid | 样品确认单号 | int8 | 64 |  | √ | 0 | [样品确认单号 srm_samplebillno](../srm_files/srm_samplebillno.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_approveentry_pkey |  | fentryid |
| 2 | idx_pur_approve_fid_fseq |  | fid,fseq |

---

## 认证报告-多语言表 t_pur_approve_l

- **表名称：** 认证报告-多语言表
- **表名：** t_pur_approve_l

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
| 1 | idx_pur_approve_l_fid |  | fid,flocaleid |
| 2 | t_pur_approve_l_pkey |  | fpkid |

---

## 认证报告-分表 t_pur_approve_a

- **表名称：** 认证报告-分表
- **表名：** t_pur_approve_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
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
| 1 | idx_pur_approve_a_ftime |  | fcreatetime |
| 2 | t_pur_approve_a_pkey |  | fid |
