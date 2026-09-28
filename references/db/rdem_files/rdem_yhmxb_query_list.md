# 研发加计优惠明细表查询-rdem_yhmxb_query_list

## 研发加计优惠明细表查询-主表 t_rdem_declare_main_tsd

- **表名称：** 研发加计优惠明细表查询-主表
- **表名：** t_rdem_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | faccrualplan | faccrualplan | int8 | 64 |  | √ | 0 |  |
| 7 | fcurrentperiodamount | 本期数 | numeric | 23 | 10 | √ | 0 | 本期数 |
| 8 | fhyncpmcid | fhyncpmcid | int8 | 64 |  | √ | 0 |  |
| 9 | fcurrentyearamount | 本年数 | numeric | 23 | 10 | √ | 0 | 本年数 |
| 10 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fadjustperiod | fadjustperiod | varchar | 50 |  | √ | ' ' |  |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fisadjustperiod | fisadjustperiod | bpchar | 1 |  | √ | '0' |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftaxareagroup | ftaxareagroup | int8 | 64 |  | √ | 0 |  |
| 17 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 18 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 19 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 20 | fcomparisontype | fcomparisontype | varchar | 50 |  | √ | ' ' |  |
| 21 | fgeneratebusinessdoc | 生成计提单 | bpchar | 1 |  | √ | '0' | 生成计提单 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbusinessdocno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 24 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | [模板配置 rdem_template](../rdem_files/rdem_template.md) |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | faccountsettype | 版本 | varchar | 50 |  | √ | ' ' | 版本,枚举: dsyj :第三季度预缴 hsqj :年度汇算清缴 |
| 28 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 31 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 32 | fnsrmc | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 33 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 34 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
| 35 | fdraftstatus | 底稿状态 | varchar | 50 |  | √ | ' ' | 底稿状态,枚举: A :暂存 B :已提交 C :已审核 D :重新审核 |
| 36 | fdeadline | fdeadline | varchar | 50 |  | √ | ' ' |  |
| 37 | fjtynsesum | fjtynsesum | numeric | 23 | 2 | √ | 0 |  |
| 38 | fpzhc | fpzhc | varchar | 50 |  | √ | ' ' |  |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据导入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_declare_main_tsd |  | fid |
| 2 | idx_rdem_main_tsd_qzme |  | forgid,fskssqq,fskssqz,ftaxsystem,faccountsettype |
| 3 | idx_rdem_declare_main_tsd_m0 |  | fbillno |
