# 底稿体系主表-rdem_declare_main_tsd

## 底稿体系主表-主表 t_rdem_declare_main_tsd

- **表名称：** 底稿体系主表-主表
- **表名：** t_rdem_declare_main_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fremarks | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | faccrualplan | 计提方案 | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 7 | fcurrentperiodamount | 本期数 | numeric | 23 | 10 | √ | 0 | 本期数 |
| 8 | fhyncpmcid | 耗用农产品名称 | int8 | 64 |  | √ | 0 | [耗用农产品名称 tcvat_hyncp_name](../tcvat_files/tcvat_hyncp_name.md) |
| 9 | fcurrentyearamount | 本年数 | numeric | 23 | 10 | √ | 0 | 本年数 |
| 10 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fadjustperiod | 调整期间 | varchar | 50 |  | √ | ' ' | 调整期间,枚举: 13 :13期 |
| 13 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 14 | fisadjustperiod | 调整期 | bpchar | 1 |  | √ | '0' | 调整期 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 17 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 18 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 19 | fbillno | 底稿编号 | varchar | 100 |  | √ | ' ' | 底稿编号 |
| 20 | fcomparisontype | 比对类型 | varchar | 50 |  | √ | ' ' | 比对类型,枚举: sdbd :审定比对 hjbd :汇缴比对 sdhjbd :审定汇缴比对 |
| 21 | fgeneratebusinessdoc | 生成业务单据 | bpchar | 1 |  | √ | '0' | 生成业务单据 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbusinessdocno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 24 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | [模板配置 rdem_template](../rdem_files/rdem_template.md) |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | faccountsettype | 账套类型 | varchar | 50 |  | √ | ' ' | 账套类型,枚举: 1 :按期申报 2 :按次申报 |
| 28 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 31 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 32 | fnsrmc | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 33 | ftype | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型,枚举: WP11 :居民企业底稿 WP12 :居民企业分支机构底稿 WP13 :核定征收底稿 WP14 :非居民企业底稿 |
| 34 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
| 35 | fdraftstatus | 底稿状态 | varchar | 50 |  | √ | ' ' | 底稿状态,枚举: |
| 36 | fdeadline | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 37 | fjtynsesum | 计提应纳税额 | numeric | 23 | 2 | √ | 0 | 计提应纳税额 |
| 38 | fpzhc | 凭证红冲 | varchar | 50 |  | √ | ' ' | 凭证红冲,枚举: 1 :是 0 :否 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :导入 1 :系统生成 |

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

---

## 单据体-子表 t_rdem_declare_detail_tsd

- **表名称：** 单据体-子表
- **表名：** t_rdem_declare_detail_tsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | varchar | 1000 |  | √ | ' ' | 值 |
| 3 | fdynrowno | 动态行标识 | varchar | 200 |  | √ | ' ' | 动态行标识 |
| 4 | frow | 行维 | int8 | 64 |  | √ | 0 | [行维成员管理 rdem_row_member](../rdem_files/rdem_row_member.md) |
| 5 | findex | 动态行所在行数 | int8 | 64 |  | √ | 0 | 动态行所在行数 |
| 6 | fcolumn | 列维 | int8 | 64 |  | √ | 0 | [列维成员管理 rdem_col_member](../rdem_files/rdem_col_member.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fvaluetype | 值类型 | varchar | 50 |  | √ | ' ' | 值类型 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fversion | fversion | varchar | 50 |  | √ | ' ' |  |
| 11 | fcellnumber | 报表项标识 | varchar | 128 |  | √ | ' ' | 报表项标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_declare_detail_tsd_m0 |  | fcolumn |
| 2 | pk_rdem_declare_detail_tsd |  | fid |

---

## 附件字段-附件表 t_rdem_sbzb_tsd_at

- **表名称：** 附件字段-附件表
- **表名：** t_rdem_sbzb_tsd_at

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_sbzb_tsd_at |  | fpkid |
| 2 | idx_t_rdem_sbzb_tsd_at_fid |  | fid |
