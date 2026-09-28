# 发放RFI-srm_issuerfi

## 发放RFI-关联追踪表 t_pur_issuerfi_tc

- **表名称：** 发放RFI-关联追踪表
- **表名：** t_pur_issuerfi_tc

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
| 1 | idx_pur_issuerfi_tc_tbill |  | ftbillid |
| 2 | pk_pur_issuerfi_tc |  | fid |
| 3 | idx_pur_issuerfi_tc_tid |  | ftid |

---

## 发放RFI-反写记录表 t_pur_issuerfi_wb

- **表名称：** 发放RFI-反写记录表
- **表名：** t_pur_issuerfi_wb

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
| 1 | pk_pur_issuerfi_wb |  | fentryid |
| 2 | idx_pur_issuerfi_wb_fk |  | fid |

---

## 发放RFI-主表 t_pur_issuerfi

- **表名称：** 发放RFI-主表
- **表名：** t_pur_issuerfi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fphone | 手机号 | varchar | 30 |  | √ | ' ' | 手机号 |
| 4 | fregsupplierid | 供应商查询 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :审批驳回 |
| 6 | fhaveregrfi | 是否生成RFI | bpchar | 1 |  | √ | ' ' | 是否生成RFI,枚举: 1 :是 2 :否 |
| 7 | fregtplid | 注册模板 | int8 | 64 |  | √ | 0 | [注册资料模板配置 pbd_supplierregconfig](../pbd_files/pbd_supplierregconfig.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fhaveconfirm | 供应商回应 | bpchar | 1 |  | √ | ' ' | 供应商回应,枚举: Y :是 N :否 |
| 10 | forgid | 认证组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 12 | fsuppliername | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 13 | fmailvalidity | 邮件有效期至 | timestamp | 0 |  |  | null | 邮件有效期至 |
| 14 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fcertifiapplyid | 供应商认证申请 | int8 | 64 |  | √ | 0 | [供应商认证申请编号 srm_certificationapplyno](../srm_files/srm_certificationapplyno.md) |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbiztypeid | 准入类型 | int8 | 64 |  | √ | 0 | [准入类型 srm_biztype](../srm_files/srm_biztype.md) |
| 21 | flinkman | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 22 | frfimsgconfigid | 文案模板 | int8 | 64 |  | √ | '2071754486262589440' | [邀约注册消息配置 srm_rfimsgconfig](../srm_files/srm_rfimsgconfig.md) |
| 23 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_issuerfi |  | fid |
| 2 | idx_pur_issuerfi |  | fsuppliername,fbillno,fcertifiapplyid |

---

## RFI配置分录-子表 t_pur_rficonentry

- **表名称：** RFI配置分录-子表
- **表名：** t_pur_rficonentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequired | 要求提供 | bpchar | 1 |  | √ | ' ' | 要求提供 |
| 3 | frfidesc | 说明 | text | 0 |  |  | ' ' | 说明 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frficontentid | RFI配置 | int8 | 64 |  | √ | 0 | [RFI配置 pbd_rficontent](../pbd_files/pbd_rficontent.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_rficonentry |  | fid,frficontentid |
| 2 | pk_pur_rficonentry |  | fentryid |

---

## 关联子实体-子表 t_pur_issuerfi_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_issuerfi_lk

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
| 1 | idx_pur_issuerfi_lk_fk |  | fid |
| 2 | pk_pur_issuerfi_lk |  | fpkid |

---

## 发放RFI-多语言表 t_pur_issuerfi_l

- **表名称：** 发放RFI-多语言表
- **表名：** t_pur_issuerfi_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliername | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_issuerfi_l |  | fpkid |
| 2 | idx_pur_issuerfi_l_idlocalid |  | fid,flocaleid |
