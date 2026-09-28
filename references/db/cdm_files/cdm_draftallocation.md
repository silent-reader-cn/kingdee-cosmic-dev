# 票据池调度-cdm_draftallocation

## 票据池调度-反写记录表 t_cdm_draftalloc_wb

- **表名称：** 票据池调度-反写记录表
- **表名：** t_cdm_draftalloc_wb

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
| 1 | idx_cdm_draftalloc_wb_fk |  | fid |
| 2 | pk_cdm_draftalloc_wb |  | fentryid |

---

## 背书明细-子表 t_cdm_draftalloc_entry

- **表名称：** 背书明细-子表
- **表名：** t_cdm_draftalloc_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexecutetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 3 | ferrmsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftransoptionstatus | 操作状态 | varchar | 50 |  | √ | ' ' | 操作状态,枚举: success :成功 fail :失败 processing :处理中 |
| 6 | ftransstatusdesc | 交易状态说明 | varchar | 30 |  | √ | ' ' | 交易状态说明,枚举: A :调拨背书失败 B :调拨登记失败 C :归集背书失败 D :归集登记失败 E :下拨背书失败 F :下拨登记失败 |
| 7 | ftransstatus | 交易状态 | varchar | 30 |  | √ | ' ' | 交易状态,枚举: doing :交易中 succeed :交易成功 failed :交易失败 cancelled :交易作废 |
| 8 | ferrmsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 9 | fopbilltsteps | 操作步骤 | varchar | 50 |  | √ | ' ' | 操作步骤,枚举: init :初始化 endorseup_create :归集单创建 endorseup_complete :归集单确认完成 endorseup_submitele :归集单提交电票 endorsedown_create :下拨单创建 endorsedown_complete :下拨单确认完成 endorsedown_submitele :下拨单提交电票 endorse_create :调拨单创建 endorse_complete :调拨单确认完成 endorse_submitele :调拨单提交电票 poolout :票据出池 final :结束 |
| 10 | fopbilltype | 操作单据 | varchar | 50 |  | √ | ' ' | 操作单据,枚举: allocate :调拨业务处理单 allocateup :归集业务处理单 allocatedown :下拨业务处理单 out :出池申请 non :无 |
| 11 | ftransfinish | 调度完成标志 | bpchar | 1 |  | √ | '0' | 调度完成标志 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftalloc_entry |  | fentryid |
| 2 | idx_cdm_draftalloc_entry_fid |  | fid |

---

## 关联子实体-子表 t_cdm_draftalloc_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cdm_draftalloc_lk

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
| 1 | idx_cdm_draftalloc_lk_fk |  | fid |
| 2 | pk_cdm_draftalloc_lk |  | fpkid |

---

## 票据池调度-关联追踪表 t_cdm_draftalloc_tc

- **表名称：** 票据池调度-关联追踪表
- **表名：** t_cdm_draftalloc_tc

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
| 1 | idx_cdm_draftalloc_tc_tbill |  | ftbillid |
| 2 | pk_cdm_draftalloc_tc |  | fid |
| 3 | idx_cdm_draftalloc_tc_tid |  | ftid |

---

## 票据池调度-多语言表 t_cdm_draftalloc_l

- **表名称：** 票据池调度-多语言表
- **表名：** t_cdm_draftalloc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftalloc_l |  | fpkid |
| 2 | idx_cdm_draftalloc_l_fid |  | fid |

---

## 票据池调度-主表 t_cdm_draftalloc

- **表名称：** 票据池调度-主表
- **表名：** t_cdm_draftalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fincompanyid | 调入收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdispatchrule | 票据调度规则 | varchar | 30 |  | √ | ' ' | 票据调度规则,枚举: direct :直接调度 indirect :间接调度 |
| 4 | famount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 7 | fbiztype | 业务处理 | varchar | 50 |  | √ | ' ' | 业务处理,枚举: allocateup :票据归集 allocatedown :票据下拨 allocate :票据调拨 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcreatepoolaccount | 建池收付组织账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 10 | fdraftcount | 票据张数 | int4 | 32 |  | √ | 0 | 票据张数 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fissubmitendorse | 提交背书 | bpchar | 1 |  | √ | '0' | 提交背书 |
| 13 | fsucamount | 调度成功金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调度成功金额 |
| 14 | finaccountid | 调入收付组织账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | foutcompanyid | 调出收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 23 | ftransstatus | 调度状态 | varchar | 30 |  | √ | ' ' | 调度状态,枚举: init :初始化 processing :调度中 finished :已完成 |
| 24 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 25 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 26 | fbillpoolid | 票据池 | int8 | 64 |  | √ | 0 | [票据池维护 cdm_billpool](../cdm_files/cdm_billpool.md) |
| 27 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | flocamt | 金额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 金额折本位币 |
| 30 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_draftalloc_billno |  | fbillno |
| 2 | pk_t_cdm_draftalloc |  | fid |
