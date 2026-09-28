# 开标申请-src_bidopenapply

## 开标申请-主表 t_src_bidopenapply

- **表名称：** 开标申请-主表
- **表名：** t_src_bidopenapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbilldate | 申请时间 | timestamp | 0 |  |  | null | 申请时间 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fopentype | 开标方式 | varchar | 30 |  | √ | ' ' | 开标方式,枚举: allopen :全部开标 tecopen :开技术标 bizopen :开商务标 aptopen :开资审标 |
| 13 | fstopbiddate | 投标/报价截止时间 | timestamp | 0 |  |  | null | 投标/报价截止时间 |
| 14 | fsrcbilltype | 待开标单据 | varchar | 30 |  | √ | ' ' | 待开标单据,枚举: src_aptitudeaudit :资质预审 src_aptitudeaudit2 :资审后审 src_bidassess :开技术标 src_compare :开商务标 src_scorertask :开标与评标 src_predecision :预定标 src_decision :定标 |
| 15 | fisconfirm | 是否从源单发起 | bpchar | 1 |  | √ | '0' | 是否从源单发起 |
| 16 | fbillno | 申请单号 | varchar | 30 |  | √ | ' ' | 申请单号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_bidopenapply |  | fid |
| 2 | idx_src_bidopenapply_billno |  | fbillno |

---

## 项目成员分录-子表 t_src_openapply_man

- **表名称：** 项目成员分录-子表
- **表名：** t_src_openapply_man

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :正常 B :已转交 C :已授权 D :已处理 E :已终止 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fisnotify | fisnotify | bpchar | 1 |  | √ | '0' |  |
| 7 | fclarifytime | fclarifytime | timestamp | 0 |  |  | null |  |
| 8 | fbidderid | 姓名 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fisclarify | fisclarify | bpchar | 1 |  | √ | '0' |  |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fbizroleid | 业务角色 | int8 | 64 |  | √ | 0 | 业务角色 pds_bizrole |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fbidder1 | fbidder1 | int8 | 64 |  | √ | 0 |  |
| 15 | fphone | 联系电话 | varchar | 20 |  | √ | ' ' | 联系电话 |
| 16 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 18 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | femail | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | fbidder5 | fbidder5 | int8 | 64 |  | √ | 0 |  |
| 23 | fbidder4 | fbidder4 | int8 | 64 |  | √ | 0 |  |
| 24 | fneedmessage | 是否发送消息 | bpchar | 1 |  | √ | '0' | 是否发送消息 |
| 25 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 26 | fbidder3 | fbidder3 | int8 | 64 |  | √ | 0 |  |
| 27 | fbidder2 | fbidder2 | int8 | 64 |  | √ | 0 |  |
| 28 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 29 | ftype | ftype | bpchar | 1 |  | √ | ' ' |  |
| 30 | fissignin | fissignin | bpchar | 1 |  | √ | '0' |  |
| 31 | fsignintime | fsignintime | timestamp | 0 |  |  | null |  |
| 32 | fisbenifit | fisbenifit | bpchar | 1 |  | √ | '0' |  |
| 33 | fneedsignin | 是否需要签到 | bpchar | 1 |  | √ | '0' | 是否需要签到 |
| 34 | fenable | fenable | bpchar | 1 |  | √ | '1' |  |
| 35 | fnumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_openapply_man_fbiz |  | fbizroleid |
| 2 | idx_src_openapply_man_fpid |  | fparentid |
| 3 | pk_src_openapply_man |  | fentryid |
| 4 | idx_src_openapply_man_fid |  | fid |
| 5 | idx_src_openapply_man_ftype |  | ftype |
| 6 | idx_src_openapply_man_fbid |  | fbidderid |

---

## 参标类型-多选基础资料表 t_src_referencetype

- **表名称：** 参标类型-多选基础资料表
- **表名：** t_src_referencetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_referencetype |  | fpkid |
| 2 | idx_src_reftype_bid |  | fbasedataid |
| 3 | idx_src_reftype_eid |  | fentryid |

---

## 开标情况-子表 t_src_openapply_open

- **表名称：** 开标情况-子表
- **表名：** t_src_openapply_open

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisaptassess2 | 资审后审已评标 | bpchar | 1 |  | √ | '0' | 资审后审已评标 |
| 3 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 4 | fpackfeeitemid | fpackfeeitemid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizopenuser | 商务开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fisbizassess | 商务标已评标 | bpchar | 1 |  | √ | '0' | 商务标已评标 |
| 8 | fbizassessdate | 商务标评标时间 | timestamp | 0 |  |  | null | 商务标评标时间 |
| 9 | fisaptassess | 资质预审已评标 | bpchar | 1 |  | √ | '0' | 资质预审已评标 |
| 10 | ftecopenuser | 技术开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ffeeamount | ffeeamount | numeric | 19 | 6 | √ | 0 |  |
| 12 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 13 | fturns | 当前轮次 | varchar | 2 |  | √ | ' ' | 当前轮次,枚举: 1 :第一轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 |
| 14 | faptopenuser | 资质预审开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | faptassessdate2 | 资审后审评标时间 | timestamp | 0 |  |  | null | 资审后审评标时间 |
| 16 | fisnegotiate | 是否议标 | bpchar | 1 |  | √ | '0' | 是否议标 |
| 17 | fistecassess | 技术标已评标 | bpchar | 1 |  | √ | '0' | 技术标已评标 |
| 18 | fnegopendate | 议标开标时间 | timestamp | 0 |  |  | null | 议标开标时间 |
| 19 | fbizopendate | 商务标开标时间 | timestamp | 0 |  |  | null | 商务标开标时间 |
| 20 | ftecopendate | 技术标开标时间 | timestamp | 0 |  |  | null | 技术标开标时间 |
| 21 | fisnegopen | 议标已开标 | bpchar | 1 |  | √ | '0' | 议标已开标 |
| 22 | ftecassessdate | 技术标评标时间 | timestamp | 0 |  |  | null | 技术标评标时间 |
| 23 | faptopendate | 资质预审开标时间 | timestamp | 0 |  |  | null | 资质预审开标时间 |
| 24 | fisaptopen | 资质预审已开标 | bpchar | 1 |  | √ | '0' | 资质预审已开标 |
| 25 | fpackdocamount | fpackdocamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | fnegopenuser | 议标开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fisbizopen | 商务标已开标 | bpchar | 1 |  | √ | '0' | 商务标已开标 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fpackage | fpackage | varchar | 50 |  | √ | ' ' |  |
| 30 | faptassessdate | 资质预审评标时间 | timestamp | 0 |  |  | null | 资质预审评标时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_openapply_open_pid |  | fpackageid |
| 2 | pk_src_openapply_open |  | fentryid |
| 3 | idx_src_openapply_open_fid |  | fid |

---

## 回标详情-子表 t_src_openapply_sup

- **表名称：** 回标详情-子表
- **表名：** t_src_openapply_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 3 | fisupload | 是否上传标书 | bpchar | 1 |  | √ | '0' | 是否上传标书 |
| 4 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 5 | fisbidpush | 评标下达否 | bpchar | 1 |  | √ | '0' | 评标下达否 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fbizopenuser | fbizopenuser | int8 | 64 |  | √ | 0 |  |
| 9 | fdocamount | 标书费 | numeric | 23 | 10 | √ | 0 | 标书费 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 12 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 13 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 14 | fcount2 | 标的附件 | int4 | 32 |  | √ | 0 | 标的附件 |
| 15 | fisabandon | 是否拒标 | bpchar | 1 |  | √ | '0' | 是否拒标 |
| 16 | faptopenuser | faptopenuser | int8 | 64 |  | √ | 0 |  |
| 17 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 18 | fisnegotiate | 是否议标报价 | bpchar | 1 |  | √ | '0' | 是否议标报价 |
| 19 | fabandonreason | 拒标原因 | varchar | 255 |  | √ | ' ' | 拒标原因 |
| 20 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 21 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 22 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 23 | ftecopendate | ftecopendate | timestamp | 0 |  |  | null |  |
| 24 | fsumscore | 当前得分 | numeric | 19 | 4 | √ | 0 | 当前得分 |
| 25 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 26 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 27 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 28 | fisaptopen | 资质预审已开标 | bpchar | 1 |  | √ | '0' | 资质预审已开标 |
| 29 | fisaptpush2 | 后审下达否 | bpchar | 1 |  | √ | '0' | 后审下达否 |
| 30 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 31 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 34 | frank | frank | int4 | 32 |  | √ | 0 |  |
| 35 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 36 | fisaptpush | 资审下达否 | bpchar | 1 |  | √ | '0' | 资审下达否 |
| 37 | fisviepublish | 竞价发布否 | bpchar | 1 |  | √ | '0' | 竞价发布否 |
| 38 | fbizamount | 商务价格 | numeric | 23 | 10 | √ | 0 | 商务价格 |
| 39 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | ' ' | 评标状态,枚举: A :待下达 B :已下达 C :部分评标 D :已评标 |
| 40 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 41 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :来源采委会 2 :立项新增 9 :补充供应商 |
| 42 | fisaptitude | 资审/评标结果 | bpchar | 1 |  | √ | '0' | 资审/评标结果,枚举: 0 :未资审/评标 1 :资审/评标合格 2 :资审/评标不合格 |
| 43 | fbidderid | 投标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fispayfee | 已缴纳保证金 | bpchar | 1 |  | √ | '0' | 已缴纳保证金 |
| 45 | fcurrentrank | 当前排名 | int4 | 32 |  | √ | 0 | 当前排名 |
| 46 | ffeeamount | 投标保证金 | numeric | 23 | 10 | √ | 0 | 投标保证金 |
| 47 | ftecopenuser | ftecopenuser | int8 | 64 |  | √ | 0 |  |
| 48 | fcount | 单据附件 | int4 | 32 |  | √ | 0 | 单据附件 |
| 49 | fisexempt | fisexempt | bpchar | 1 |  | √ | '0' |  |
| 50 | fispuragent | fispuragent | bpchar | 1 |  | √ | '0' |  |
| 51 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 52 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 53 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 54 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 55 | fbizopendate | fbizopendate | timestamp | 0 |  |  | null |  |
| 56 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 57 | fisbidpublish | 招标发布否 | bpchar | 1 |  | √ | '0' | 招标发布否 |
| 58 | faptitudenote | 资审/评标意见 | varchar | 255 |  | √ | ' ' | 资审/评标意见 |
| 59 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 60 | fduty | fduty | varchar | 50 |  | √ | ' ' |  |
| 61 | fispaydocfee | 已缴纳标书费 | bpchar | 1 |  | √ | '0' | 已缴纳标书费 |
| 62 | faptopendate | faptopendate | timestamp | 0 |  |  | null |  |
| 63 | fisbizopen | 商务标已开标 | bpchar | 1 |  | √ | '0' | 商务标已开标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_openapply_sup_fpag |  | fpackageid |
| 2 | idx_openapply_sup_fsup |  | fsupplierid |
| 3 | pk_src_openapply_sup |  | fentryid |
| 4 | idx_openapply_sup_fid |  | fid |
| 5 | idx_openapply_sup_fpid |  | fparentid |
