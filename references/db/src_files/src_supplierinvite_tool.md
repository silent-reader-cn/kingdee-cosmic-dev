# 选择供应商F7(工具)-src_supplierinvite_tool

## 限定供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商用户 pur_supuser](../basedata_files/pur_supuser.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierusers |  | fpkid |
| 2 | idx_src_supplierusers_eid |  | fentryid |
| 3 | idx_src_supplierusers_bid |  | fbasedataid |

---

## 关联标的(发标)-多选基础资料表 t_src_invitesupplier_item

- **表名称：** 关联标的(发标)-多选基础资料表
- **表名：** t_src_invitesupplier_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_invitesup_item_bid |  | fbasedataid |
| 2 | idx_src_invitesup_item_eid |  | fentryid |
| 3 | pk_src_invitesupplier_item |  | fpkid |

---

## 关联标的(范围)-多选基础资料表 t_src_invitesupplierscope

- **表名称：** 关联标的(范围)-多选基础资料表
- **表名：** t_src_invitesupplierscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_invitesupplierscope |  | fpkid |
| 2 | idx_src_invitesupscope_bid |  | fbasedataid |
| 3 | idx_src_invitesupscope_eid |  | fentryid |

---

## 选择供应商F7(工具)-主表 t_src_invitesupplier_temp

- **表名称：** 选择供应商F7(工具)-主表
- **表名：** t_src_invitesupplier_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 2 | fismanualselect | 是否手工选择供应商 | bpchar | 1 |  | √ | '0' | 是否手工选择供应商 |
| 3 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 4 | fisexemptapt | 免资审 | bpchar | 1 |  | √ | '0' | 免资审 |
| 5 | fisbidpush | 评标任务下达否 | bpchar | 1 |  | √ | '0' | 评标任务下达否 |
| 6 | fisselect | 是否推荐 | bpchar | 1 |  | √ | '0' | 是否推荐 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 10 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 11 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 12 | fisabandon | fisabandon | bpchar | 1 |  | √ | '0' |  |
| 13 | fsupname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 14 | fisconfirm | 是否应标(确认) | bpchar | 1 |  | √ | '0' | 是否应标(确认) |
| 15 | fabandonreason | fabandonreason | varchar | 255 |  | √ | ' ' |  |
| 16 | fisnegotiate | 是否议标报价 | bpchar | 1 |  | √ | '0' | 是否议标报价 |
| 17 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 18 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 19 | fisfeeagent | 采购方代理缴费 | bpchar | 1 |  | √ | '0' | 采购方代理缴费 |
| 20 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 21 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 23 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 24 | ftempsupplierid | 临时供应商ID | int8 | 64 |  | √ | 0 | 临时供应商ID |
| 25 | fisaptpush2 | 资质后审下达否 | bpchar | 1 |  | √ | '0' | 资质后审下达否 |
| 26 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 27 | fpublishdate | 发标日期 | timestamp | 0 |  |  | null | 发标日期 |
| 28 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 31 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 32 | fisaptpush | 资质预审下达否 | bpchar | 1 |  | √ | '0' | 资质预审下达否 |
| 33 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 34 | fk_sf_textfield | fk_sf_textfield | varchar | 50 |  | √ | ' ' |  |
| 35 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 36 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :来源采委会 2 :立项新增 9 :补充供应商 |
| 37 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 38 | fispayfee | fispayfee | bpchar | 1 |  | √ | '0' |  |
| 39 | fcurrentrank | 初选排名 | int4 | 32 |  | √ | 0 | 初选排名 |
| 40 | ffeeamount | ffeeamount | numeric | 23 | 10 | √ | 0 |  |
| 41 | fpurlistnote | 关联标的 | varchar | 50 |  | √ | ' ' | 关联标的 |
| 42 | fpublisherid | 发标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fispuraptitude | 采购方代理资审回复 | bpchar | 1 |  | √ | '0' | 采购方代理资审回复 |
| 44 | fremark | 报名说明 | varchar | 100 |  | √ | ' ' | 报名说明 |
| 45 | fispuragent | 采购方代理报价 | bpchar | 1 |  | √ | '0' | 采购方代理报价 |
| 46 | fquotedate | 投标/报价时间 | timestamp | 0 |  |  | null | 投标/报价时间 |
| 47 | fpublishstatus | 发标状态 | bpchar | 1 |  | √ | ' ' | 发标状态,枚举: A :待发标 B :已发标 |
| 48 | fparentid | 父单据id | varchar | 50 |  | √ | ' ' | 父单据id |
| 49 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 50 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 51 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 52 | fentrysupplierip | 报名供应商IP | varchar | 100 |  | √ | ' ' | 报名供应商IP |
| 53 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 54 | fisaptitudereply | 资审回复否 | bpchar | 1 |  | √ | '0' | 资审回复否 |
| 55 | fisvalid | 初选合格否 | bpchar | 1 |  | √ | '0' | 初选合格否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_invitesupplier_temp |  | fentryid |
| 2 | idx_src_invitesup_temp_fpid |  | fparentid |
| 3 | idx_src_invitesup_temp_fid |  | fid |
| 4 | idx_src_invitesup_temp_fpag |  | fpackageid |
| 5 | idx_src_invitesup_temp_fsup |  | fsupplierid |
