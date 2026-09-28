# 回标详情F7-src_bidopensupplier

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

## 回标详情F7-主表 t_src_invitesupplier

- **表名称：** 回标详情F7-主表
- **表名：** t_src_invitesupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 2 | faptrank | 资审开标顺序 | int4 | 32 |  | √ | 0 | 资审开标顺序 |
| 3 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 4 | fisupload | 是否上传标书 | bpchar | 1 |  | √ | '0' | 是否上传标书 |
| 5 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 6 | fisexemptapt | 免资审 | bpchar | 1 |  | √ | '0' | 免资审 |
| 7 | fisbidpush | 评标任务下达否 | bpchar | 1 |  | √ | '0' | 评标任务下达否 |
| 8 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fbizopenuser | 商务表开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdocamount | 标书费 | numeric | 23 | 10 | √ | 0 | 标书费 |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 14 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 15 | ftecrank | 技术开标顺序 | int4 | 32 |  | √ | 0 | 技术开标顺序 |
| 16 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 17 | fcount2 | 标的附件 | int4 | 32 |  | √ | 0 | 标的附件 |
| 18 | fisabandon | 是否拒标 | bpchar | 1 |  | √ | '0' | 是否拒标 |
| 19 | faptopenuser | 资审开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 21 | fisnegotiate | 是否议标报价 | bpchar | 1 |  | √ | '0' | 是否议标报价 |
| 22 | fabandonreason | 弃标原因 | varchar | 255 |  | √ | ' ' | 弃标原因 |
| 23 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 24 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 25 | fisfeeagent | 采购方代理缴费 | bpchar | 1 |  | √ | '0' | 采购方代理缴费 |
| 26 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 27 | ftecopendate | 技术标开标时间 | timestamp | 0 |  |  | null | 技术标开标时间 |
| 28 | fsumscore | 当前得分 | numeric | 19 | 4 | √ | 0 | 当前得分 |
| 29 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 31 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 32 | fisaptopen | 资审已开标 | bpchar | 1 |  | √ | '0' | 资审已开标 |
| 33 | ftempsupplierid | 临时供应商ID | int8 | 64 |  | √ | 0 | 临时供应商ID |
| 34 | fisaptpush2 | 资质后审下达否 | bpchar | 1 |  | √ | '0' | 资质后审下达否 |
| 35 | fassessorder | 评标顺序 | int4 | 32 |  | √ | 0 | 评标顺序 |
| 36 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 37 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 40 | frank | 开标顺序 | int4 | 32 |  | √ | 0 | 开标顺序 |
| 41 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 42 | fisaptpush | 资质预审下达否 | bpchar | 1 |  | √ | '0' | 资质预审下达否 |
| 43 | fisviepublish | 竞价发布否 | bpchar | 1 |  | √ | '0' | 竞价发布否 |
| 44 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 45 | fbizamount | 商务价格 | numeric | 23 | 10 | √ | 0 | 商务价格 |
| 46 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | ' ' | 评标状态,枚举: A :待下达 B :已下达 C :部分评标 D :已评标 |
| 47 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 48 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :来源采委会 2 :立项新增 9 :补充供应商 |
| 49 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 50 | fbidderid | 投标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fispayfee | 是否缴纳保证金 | bpchar | 1 |  | √ | '0' | 是否缴纳保证金 |
| 52 | fcurrentrank | 当前排名 | int4 | 32 |  | √ | 0 | 当前排名 |
| 53 | ffeeamount | 投标保证金 | numeric | 23 | 10 | √ | 0 | 投标保证金 |
| 54 | ftecopenuser | 技术标开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fpurlistnote | 关联标的 | varchar | 50 |  | √ | ' ' | 关联标的 |
| 56 | fcount | 单据附件 | int4 | 32 |  | √ | 0 | 单据附件 |
| 57 | fispuraptitude | 采购方代理资审回复 | bpchar | 1 |  | √ | '0' | 采购方代理资审回复 |
| 58 | fisexempt | 是否免交 | bpchar | 1 |  | √ | '0' | 是否免交 |
| 59 | fispuragent | 采购方代理投标/报价 | bpchar | 1 |  | √ | '0' | 采购方代理投标/报价 |
| 60 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 61 | fquotedate | 投标/报价时间 | timestamp | 0 |  |  | null | 投标/报价时间 |
| 62 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 63 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 64 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 65 | fbizopendate | 商务标开标时间 | timestamp | 0 |  |  | null | 商务标开标时间 |
| 66 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 67 | fisbidpublish | 招标发布否 | bpchar | 1 |  | √ | '0' | 招标发布否 |
| 68 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 69 | fbizrank | 商务开标顺序 | int4 | 32 |  | √ | 0 | 商务开标顺序 |
| 70 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 71 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 72 | fispaydocfee | 是否缴纳标书费 | bpchar | 1 |  | √ | '0' | 是否缴纳标书费 |
| 73 | faptopendate | 资审开标时间 | timestamp | 0 |  |  | null | 资审开标时间 |
| 74 | fisaptitudereply | 资审回复否 | bpchar | 1 |  | √ | '0' | 资审回复否 |
| 75 | fisbizopen | 商务标已开标 | bpchar | 1 |  | √ | '0' | 商务标已开标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_invitesupplier |  | fentryid |
| 2 | idx_src_invitesupplier_fpag |  | fpackageid |
| 3 | idx_src_invitesupplier_fsup |  | fsupplierid |
| 4 | idx_src_invitesupplier_fid |  | fid |
| 5 | idx_src_invitesupplier_fpid |  | fparentid |
