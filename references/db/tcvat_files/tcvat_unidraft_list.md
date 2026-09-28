# 申报底稿查询-tcvat_unidraft_list

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
| 1 | pk_tcvat_dg_ybnsr_ybhz |  | fentryid |
| 2 | idx_tcvat_dg_ybnsr_ybhz |  | fsbbid |
| 3 | idx_tcvat_dg_ybnsr_ybhz_1 |  | fewblxh,fsbbid |

---

## 申报底稿查询-主表 t_tpo_declare_main_tsd

- **表名称：** 申报底稿查询-主表
- **表名：** t_tpo_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 4 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 6 | fcurrentyearamount | 本年数 | numeric | 23 | 10 | √ | 0 | 本年数 |
| 7 | fhyncpmcid | 耗用农产品名称 | int8 | 64 |  | √ | 0 | [耗用农产品名称 tcvat_hyncp_name](../tcvat_files/tcvat_hyncp_name.md) |
| 8 | fsteplevel | 汇总层级 | varchar | 50 |  | √ | ' ' | 汇总层级,枚举: root :根节点 middle :中间节点 leaf :叶子节点 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fadjustperiod | 调整期间 | varchar | 50 |  | √ | ' ' | 调整期间,枚举: 13 :13期 |
| 11 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | ftotalsbse | ftotalsbse | numeric | 23 | 10 | √ | 0 |  |
| 14 | fflexbizdims | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fdrafttype | 底稿类别 | varchar | 50 |  | √ | ' ' | 底稿类别,枚举: qysdsjb :企业所得税预缴底稿 qysdsnb :企业所得税年报底稿 zzs :增值税底稿 |
| 16 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 17 | ffrequency | ffrequency | varchar | 50 |  | √ | ' ' |  |
| 18 | fstepsummary | 逐级汇总 | bpchar | 1 |  | √ | '0' | 逐级汇总 |
| 19 | ftotalbtse | ftotalbtse | numeric | 23 | 10 | √ | 0 |  |
| 20 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |
| 21 | fbusinessdocno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 25 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 26 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 27 | fisdeclare | 是否生成申报表 | bpchar | 1 |  | √ | '0' | 是否生成申报表 |
| 28 | fdraftstatus | 底稿状态 | varchar | 50 |  | √ | ' ' | 底稿状态,枚举: |
| 29 | fjtynsesum | 计提应纳税额 | numeric | 23 | 10 | √ | 0 | 计提应纳税额 |
| 30 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 纳税申报基础资料 tpo_declare_base |
| 31 | fpzhc | 凭证红冲 | varchar | 50 |  | √ | ' ' | 凭证红冲,枚举: 1 :是 0 :否 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :引入 1 :系统生成 |
| 34 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | faccrualdate | 计提日期 | timestamp | 0 |  |  | null | 计提日期 |
| 36 | fcurrentperiodamount | 本期数 | numeric | 23 | 10 | √ | 0 | 本期数 |
| 37 | faccrualplan | 计税方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 38 | fhjybtse | 合计应补（退）税额 | numeric | 23 | 10 | √ | 0 | 合计应补（退）税额 |
| 39 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 40 | fisadjustperiod | 调整期 | bpchar | 1 |  | √ | '0' | 调整期 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 43 | fjtnumber | 计提单号 | varchar | 100 |  | √ | ' ' | 计提单号 |
| 44 | fmultitemplateid | 新模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_multi_template |
| 45 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 46 | ftotaljtse | ftotaljtse | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsbbno | 申报表编号 | varchar | 100 |  | √ | ' ' | 申报表编号 |
| 48 | fcomparisontype | 比对类型 | varchar | 50 |  | √ | 'sdhjbd' | 比对类型,枚举: sdbd :审定比对 hjbd :汇缴比对 sdhjbd :审定汇缴比对 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fgeneratebusinessdoc | 生成业务单据 | bpchar | 1 |  | √ | '0' | 生成业务单据 |
| 51 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 54 | fisxxwlqy | fisxxwlqy | varchar | 50 |  | √ | ' ' |  |
| 55 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 56 | fstepparentid | 汇总父级报表id | int8 | 64 |  | √ | 0 | 汇总父级报表id |
| 57 | ftype | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型,枚举: WP11 :居民企业底稿 WP12 :居民企业分支机构底稿 WP13 :核定征收底稿 WP14 :非居民企业底稿 |
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
