# 税金缴纳信息-bdtaxr_pay_record

## 税金缴纳信息-主表 t_bdtaxr_pay_record

- **表名称：** 税金缴纳信息-主表
- **表名：** t_bdtaxr_pay_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsbbentryid | 申报表子表id | int8 | 64 |  | √ | 0 | 申报表子表id |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 7 | fentrydate | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |
| 8 | fsjznj | 实缴滞纳金 | numeric | 23 | 10 | √ | 0 | 实缴滞纳金 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | felectrictaxno | 电子税票号 | varchar | 50 |  | √ | ' ' | 电子税票号 |
| 11 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: 1 :已缴款 2 :未缴款 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 14 | fssbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 15 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fcs :房产税 fjsf :附加税费 cztdsys :城镇土地使用税 hbs :环境保护税 xfs :消费税 zys :资源税 szys :水资源税 cswhjss :城市维护建设税 jyffj :教育费附加 dfjyfj :地方教育附加 ccs :车船税 qs :契税 tvpt :车辆购置税 gdzys :耕地占用税 tdzzs :土地增值税 yys :烟叶税 ghjf :工会经费 sljsjj :地方水利建设基金 ljclf :城镇垃圾处理费 whsyjsf :文化事业建设费 ghcbj :工会筹备金 fcscztdsys :房产税 dwfhf :堤围防护费 dkdj :代扣代缴 totf_cjrjybzj :残疾人就业保障金 kjqysds :扣缴企业所得税 |
| 16 | fhjsqid | 缓缴申请id | int8 | 64 |  | √ | 0 | 缓缴申请id |
| 17 | fsbbno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 |
| 21 | foperator | 缓缴操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fpayno | 缴款编号 | varchar | 50 |  | √ | ' ' | 缴款编号 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fyjje | 应缴金额 | numeric | 23 | 10 | √ | 0 | 应缴金额 |
| 25 | foperatetime | 缓缴操作时间 | timestamp | 0 |  |  | null | 缓缴操作时间 |
| 26 | fsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 29 | fyspzno | 应税凭证号 | varchar | 50 |  | √ | ' ' | 应税凭证号 |
| 30 | fdeadline | 缴款期限 | timestamp | 0 |  |  | null | 缴款期限 |
| 31 | fsyqjje | 剩余欠缴金额 | numeric | 23 | 10 | √ | 0 | 剩余欠缴金额 |
| 32 | fsssq | 所属税期 | varchar | 50 |  | √ | ' ' | 所属税期 |
| 33 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 34 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 35 | fjkbl | 缴款比例 | numeric | 23 | 10 | √ | 0 | 缴款比例 |
| 36 | fnsrtype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产税和城镇土地税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） ccxws :财产行为税 szys_a :水资源税纳税申报表A szys_b :水资源税纳税申报表B tcrt :资源税 tvpt :车辆购置税 tcvvt :车船税 tcept :环保税 yys :烟叶税 zzsybnsr_zjg :汇总申报（一般纳税人总机构） zzsybnsr_fzjg :汇总申报（一般纳税人分支机构） zzsyjskb :增值税预缴税款表 zzsybnsr_yz_zjg :一般企业汇总申报预征方式总机构 zzsybnsr_yz_fzjg :一般企业汇总申报预征方式分支机构 qtsf_tysbb :通用申报表（税及附征税费） qtsf_fsstysbb :非税收入通用申报表 whsyjsf :文化事业建设费 zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 dkdj :代扣代缴 totf_cjrjybzj :残疾人就业保障金 kjqysds :扣缴企业所得税 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_pay_record |  | fsbbid |
| 2 | idx_bdtaxr_pay_record_entryid |  | fsbbentryid |
| 3 | pk_bdtaxr_pay_record |  | fid |
| 4 | idx_bdtaxr_pay_record_sqid |  | fhjsqid |

---

## 单据体-子表 t_bdtaxr_pay_detail

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_pay_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyjjemx | 应缴金额 | numeric | 23 | 10 | √ | 0 | 应缴金额 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdelaypay | 实缴滞纳金 | numeric | 23 | 10 | √ | 0 | 实缴滞纳金 |
| 5 | fsjjemx | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 6 | fprojectnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 7 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fcs :房产税 fjsf :附加税费 cztdsys :城镇土地使用税 hbs :环境保护税 xfs :消费税 zys :资源税 szys :水资源税 tvpt :车辆购置税 ccs :车船税 yys :烟叶税 dfjyfj :地方教育附加 jyffj :教育费附加 cswhjss :城市维护建设税 szys_a :资源税 ghjf :工会经费 sljsjj :地方水利建设基金 whsyjsf :文化事业建设费 ljclf :城镇垃圾处理费 ghcbj :工会筹备金 dwfhf :堤围防护费 totf_cjrjybzj :残疾人就业保障金 dkdj :代扣代缴 kjqysds :扣缴企业所得税 |
| 8 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 9 | fsourceid | 税源id | int8 | 64 |  | √ | 0 | 税源id |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fprojectname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 12 | fsyqjjemx | 剩余欠缴金额 | numeric | 23 | 10 | √ | 0 | 剩余欠缴金额 |
| 13 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 14 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_pay_detail |  | fentryid |
| 2 | idx_bdtaxr_pay_detail_fk |  | fid |
