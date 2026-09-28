# 统计税金表-tctb_tjsjb

## 统计税金表-主表 t_tctb_new_tjsjb

- **表名称：** 统计税金表-主表
- **表名：** t_tctb_new_tjsjb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: |
| 3 | fbusinesssource | 业务来源 | varchar | 50 |  | √ | ' ' | 业务来源,枚举: 0 :国内纳税申报 1 :事项填报 2 :计提底稿 3 :税金计提单 4 :海外纳税申报 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsjsj | 实缴税金 | numeric | 23 | 10 | √ | 0 | 实缴税金 |
| 6 | fsourceid | 来源id | varchar | 100 |  | √ | ' ' | 来源id |
| 7 | flevytype | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: zxsb :自行申报 dkdj :代扣代缴 |
| 8 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 9 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 10 | fyzse | 预征税额 | numeric | 23 | 10 | √ | 0 | 预征税额 |
| 11 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 12 | fdeclarestatus | 申报表状态 | varchar | 50 |  | √ | ' ' | 申报表状态,枚举: editing :● 申报中 declared :● 已申报 undeclare :● 未编制 |
| 13 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 14 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 15 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 16 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 17 | fapanage | 属地管理 | varchar | 200 |  | √ | ' ' | 属地管理 |
| 18 | fjkdate | 缴款日期(已废弃) | timestamp | 0 |  |  | null | 缴款日期(已废弃) |
| 19 | ftaxitemname | 税目 | varchar | 200 |  | √ | ' ' | 税目 |
| 20 | fmetadataid | 元数据标识 | varchar | 200 |  | √ | ' ' | 元数据标识 |
| 21 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 22 | fhsorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fnsrmc | 纳税人名称 | varchar | 200 |  | √ | ' ' | 纳税人名称 |
| 24 | fyhstaxitems | 印花税税目 | int8 | 64 |  | √ | 0 | 印花税-税目及税率 tpo_tcsd_taxrate |
| 25 | fformno | 申报表编码 | varchar | 500 |  | √ | ' ' | 申报表编码 |
| 26 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 27 | ffsl | 税负率 | numeric | 23 | 10 | √ | 0 | 税负率 |
| 28 | ffcstaxitems | 房产税税目 | int8 | 64 |  | √ | 0 | 房产税和城镇土地税-税目及税率 tpo_tcret_taxrate |
| 29 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 30 | ftaxoffice | 主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 31 | fnsrtype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 dkdj :代扣代缴 kjqysds :扣缴企业所得税 totf_cjrjybzj :残疾人就业保障金缴费申报表 |
| 32 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 : |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_new_tjsjb |  | fid |
| 2 | idx_tctb_new_tjsjb |  | forgid,fskssqq,fskssqz |

---

## 单据体-子表 t_tctb_new_tjsjb_djt

- **表名称：** 单据体-子表
- **表名：** t_tctb_new_tjsjb_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdjtjkdate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |
| 3 | fdjtsjsj | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_new_tjsjb_djt_fk |  | fid |
| 2 | pk_tctb_new_tjsjb_djt |  | fentryid |
