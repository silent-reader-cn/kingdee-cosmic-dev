# 回标详情F7(工具)-src_bidopensupplier_tool

## 限定供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
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

## 回标详情F7(工具)-主表 t_src_invitesupplier

- **表名称：** 回标详情F7(工具)-主表
- **表名：** t_src_invitesupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 2 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 3 | fisupload | 是否上传标书 | bpchar | 1 |  | √ | '0' | 是否上传标书 |
| 4 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 5 | fisbidpush | 评标任务下达否 | bpchar | 1 |  | √ | '0' | 评标任务下达否 |
| 6 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fbizopenuser | 商务表开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdocamount | 标书费 | numeric | 23 | 10 | √ | 0 | 标书费 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 12 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 13 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 14 | fcount2 | 标的附件 | int4 | 32 |  | √ | 0 | 标的附件 |
| 15 | fisabandon | 是否拒标 | bpchar | 1 |  | √ | '0' | 是否拒标 |
| 16 | faptopenuser | 资审开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 18 | fisnegotiate | 是否议标报价 | bpchar | 1 |  | √ | '0' | 是否议标报价 |
| 19 | fabandonreason | 弃标原因 | varchar | 255 |  | √ | ' ' | 弃标原因 |
| 20 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 21 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 22 | fisfeeagent | 采购方代理缴费 | bpchar | 1 |  | √ | '0' | 采购方代理缴费 |
| 23 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 24 | ftecopendate | 技术标开标时间 | timestamp | 0 |  |  | null | 技术标开标时间 |
| 25 | fsumscore | 当前得分 | numeric | 19 | 4 | √ | 0 | 当前得分 |
| 26 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 28 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 29 | fisaptopen | 资审已开标 | bpchar | 1 |  | √ | '0' | 资审已开标 |
| 30 | fisaptpush2 | 资质后审下达否 | bpchar | 1 |  | √ | '0' | 资质后审下达否 |
| 31 | fassessorder | 评标顺序 | int4 | 32 |  | √ | 0 | 评标顺序 |
| 32 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 33 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 36 | frank | 开标顺序 | int4 | 32 |  | √ | 0 | 开标顺序 |
| 37 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 38 | fisaptpush | 资质预审下达否 | bpchar | 1 |  | √ | '0' | 资质预审下达否 |
| 39 | fisviepublish | 竞价发布否 | bpchar | 1 |  | √ | '0' | 竞价发布否 |
| 40 | fbizamount | 商务价格 | numeric | 23 | 10 | √ | 0 | 商务价格 |
| 41 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | ' ' | 评标状态,枚举: A :待下达 B :已下达 C :部分评标 D :已评标 |
| 42 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 43 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :来源采委会 2 :立项新增 9 :补充供应商 |
| 44 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 45 | fbidderid | 投标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fispayfee | 是否缴纳保证金 | bpchar | 1 |  | √ | '0' | 是否缴纳保证金 |
| 47 | fcurrentrank | 当前排名 | int4 | 32 |  | √ | 0 | 当前排名 |
| 48 | ffeeamount | 投标保证金 | numeric | 23 | 10 | √ | 0 | 投标保证金 |
| 49 | ftecopenuser | 技术标开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fcount | 单据附件 | int4 | 32 |  | √ | 0 | 单据附件 |
| 51 | fisexempt | 是否免交 | bpchar | 1 |  | √ | '0' | 是否免交 |
| 52 | fispuragent | 采购方代理投标/报价 | bpchar | 1 |  | √ | '0' | 采购方代理投标/报价 |
| 53 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 54 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 55 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 56 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 57 | fbizopendate | 商务标开标时间 | timestamp | 0 |  |  | null | 商务标开标时间 |
| 58 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 59 | fisbidpublish | 招标发布否 | bpchar | 1 |  | √ | '0' | 招标发布否 |
| 60 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 61 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 62 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 63 | fispaydocfee | 是否缴纳标书费 | bpchar | 1 |  | √ | '0' | 是否缴纳标书费 |
| 64 | faptopendate | 资审开标时间 | timestamp | 0 |  |  | null | 资审开标时间 |
| 65 | fisbizopen | 商务标已开标 | bpchar | 1 |  | √ | '0' | 商务标已开标 |

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
