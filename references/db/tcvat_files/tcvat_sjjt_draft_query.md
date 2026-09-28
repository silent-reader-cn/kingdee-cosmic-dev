# 计提底稿查询-tcvat_sjjt_draft_query

## 单据体-子表 t_tcvat_dg_ybnsr

- **表名称：** 单据体-子表
- **表名：** t_tcvat_dg_ybnsr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjxsezc | 进项税额转出 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额转出 |
| 3 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 4 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fjyffj | 教育费附加 | numeric | 23 | 10 | √ | 0 | 教育费附加 |
| 7 | fjyffynse | 简易方法应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 简易方法应纳税额 |
| 8 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 9 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 10 | fxxse | 销项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 销项税额 |
| 11 | fqmldse | 期末留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末留抵税额 |
| 12 | fdfjyffj | 地方教育费附加 | numeric | 23 | 10 | √ | 0 | 地方教育费附加 |
| 13 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 14 | fxse | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 15 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 16 | fcswhjss | 城市维护建设税 | numeric | 23 | 10 | √ | 0 | 城市维护建设税 |
| 17 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 18 | fjjdjse | 加计抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 加计抵减税额 |
| 19 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_dg_ybnsr |  | fentryid |
| 2 | idx_tcvat_dg_ybnsr_1 |  | fewblxh,fsbbid |
| 3 | idx_tcvat_dg_ybnsr |  | fid |

---

## 单据体-子表 t_tcvat_dg_xgmnsr

- **表名称：** 单据体-子表
- **表名：** t_tcvat_dg_xgmnsr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 3 | fbhsxse | 应征增值税不含税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 应征增值税不含税销售额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fjyffj | 教育费附加 | numeric | 23 | 10 | √ | 0 | 教育费附加 |
| 6 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 7 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 8 | fdfjyffj | 地方教育费附加 | numeric | 23 | 10 | √ | 0 | 地方教育费附加 |
| 9 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 10 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 11 | fcswhjss | 城市维护建设税 | numeric | 23 | 10 | √ | 0 | 城市维护建设税 |
| 12 | fmsxse | 免税销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 免税销售额 |
| 13 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 14 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_dg_xgmnsr |  | fid |
| 2 | pk_tcvat_dg_xgmnsr |  | fentryid |
| 3 | idx_tcvat_dg_xgmnsr_1 |  | fewblxh,fsbbid |

---

## 单据体-子表 t_tcvat_dg_ybnsr_ybhz

- **表名称：** 单据体-子表
- **表名：** t_tcvat_dg_ybnsr_ybhz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjxsezc | 进项税额转出 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额转出 |
| 3 | fewblxh | fewblxh | varchar | 50 |  | √ | ' ' |  |
| 4 | fjxse | 进项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 进项税额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fjyffj | fjyffj | numeric | 23 | 10 | √ | 0 |  |
| 7 | fjyffynse | 简易方法应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 简易方法应纳税额 |
| 8 | fynsejze | 应纳税额减征额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额减征额 |
| 9 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 10 | fxxse | 销项税额 | numeric | 23 | 10 | √ | 0.0000000000 | 销项税额 |
| 11 | fqmldse | 期末留抵税额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末留抵税额 |
| 12 | fdfjyffj | fdfjyffj | numeric | 23 | 10 | √ | 0 |  |
| 13 | fybtse | 应补(退)税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应补(退)税额 |
| 14 | fxse | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 15 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 16 | fcswhjss | fcswhjss | numeric | 23 | 10 | √ | 0 |  |
| 17 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0.0000000000 | 应纳税额 |
| 18 | fjjdjse | 加计抵减税额 | numeric | 23 | 10 | √ | 0.0000000000 | 加计抵减税额 |
| 19 | fyjse | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_dg_ybnsr_ybhz |  | fentryid |
| 2 | idx_tcvat_dg_ybnsr_ybhz |  | fsbbid |
| 3 | idx_tcvat_dg_ybnsr_ybhz_1 |  | fewblxh,fsbbid |

---

## 计提底稿查询-主表 t_tpo_declare_main_tsd

- **表名称：** 计提底稿查询-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | ftemplatetype | 纳税人类型 | varchar | 36 |  | √ | ' ' | 纳税人类型,枚举: draft_zzsybnsr_sjjt :一般纳税人增值税 draft_zzsybnsr_ybhz_sjjt :汇总一般企业增值税 draft_zzsybnsr_hz_zjg_sjjt :一般企业汇总申报仅汇总 draft_zzsybnsr_yz_zjg_sjjt :一般企业汇总申报预征方式总机构 draft_zzsxgmnsr_sjjt :小规模纳税人增值税 |
| 6 | fcurrentyearamount | fcurrentyearamount | numeric | 23 | 10 | √ | 0 |  |
| 7 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 8 | fsteplevel | fsteplevel | varchar | 50 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 11 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 14 | fflexbizdims | fflexbizdims | int8 | 64 |  | √ | 0 |  |
| 15 | fdrafttype | fdrafttype | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 17 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 18 | fstepsummary | fstepsummary | bpchar | 1 |  | √ | '0' |  |
| 19 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 20 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusinessdocno | fbusinessdocno | varchar | 50 |  | √ | ' ' |  |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 25 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 26 | fnsrmc | fnsrmc | varchar | 100 |  | √ | ' ' |  |
| 27 | fisdeclare | fisdeclare | bpchar | 1 |  | √ | '0' |  |
| 28 | fdraftstatus | fdraftstatus | varchar | 50 |  | √ | ' ' |  |
| 29 | fjtynsesum | fjtynsesum | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 31 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | fdatatype | varchar | 50 |  | √ | ' ' |  |
| 34 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 35 | faccrualdate | faccrualdate | timestamp | 0 |  |  | null |  |
| 36 | fcurrentperiodamount | fcurrentperiodamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | faccrualplan | 计提方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 38 | fhjybtse | fhjybtse | numeric | 23 | 10 | √ | 0 |  |
| 39 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 40 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 43 | fjtnumber | fjtnumber | varchar | 100 |  | √ | ' ' |  |
| 44 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 45 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 46 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsbbno | fsbbno | varchar | 100 |  | √ | ' ' |  |
| 48 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | 'sdhjbd' |  |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fgeneratebusinessdoc | 生成计提单 | bpchar | 1 |  | √ | '0' | 生成计提单 |
| 51 | ftaxauthority | ftaxauthority | int8 | 64 |  | √ | 0 |  |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 54 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 55 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 56 | fstepparentid | fstepparentid | int8 | 64 |  | √ | 0 |  |
| 57 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 58 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
| 59 | fdeadline | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: aysb :按月申报 ajsb :按季申报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tpo_declare_main_tsd |  | fid |
| 2 | idx_declare_main_tsd_fbillno |  | fbillno |
| 3 | idx_decl_main_tsd_orgid_qzme |  | forgid,fskssqq,fskssqz,ftaxsystem,faccountsettype |
