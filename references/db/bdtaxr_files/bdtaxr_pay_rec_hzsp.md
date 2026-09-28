# 税金缴纳汇总审批单-bdtaxr_pay_rec_hzsp

## 主表-子表 t_bdtaxr_pay_hzsp_head

- **表名称：** 主表-子表
- **表名：** t_bdtaxr_pay_hzsp_head

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjkbh | 缴款编号 | varchar | 50 |  | √ | ' ' | 缴款编号 |
| 3 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fyjje | 应缴金额 | numeric | 23 | 10 | √ | 0 | 应缴金额 |
| 6 | fisdelay | 是否逾期 | varchar | 50 |  | √ | ' ' | 是否逾期,枚举: |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :正常 B :已变更 C :已删除 |
| 11 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: 1 :已缴款 2 :未缴款 |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 14 | fdeadline | 缴款期限 | timestamp | 0 |  |  | null | 缴款期限 |
| 15 | fbillid | 单据ID | varchar | 100 |  | √ | ' ' | 单据ID |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fcs :房产税 fjsf :附加税费 cztdsys :城镇土地使用税 hbs :环境保护税 xfs :消费税 zys :资源税 szys :水资源税 cswhjss :城市维护建设税 jyffj :教育费附加 dfjyfj :地方教育附加 ccs :车船税 qs :契税 tvpt :车辆购置税 gdzys :耕地占用税 tdzzs :土地增值税 yys :烟叶税 ghjf :工会经费 sljsjj :地方水利建设基金 ljclf :城镇垃圾处理费 whsyjsf :文化事业建设费 ghcbj :工会筹备金 fcscztdsys :房产税 dwfhf :堤围防护费 dkdj :代扣代缴 totf_cjrjybzj :残疾人就业保障金 kjqysds :扣缴企业所得税 stbcbcf :水土保持补偿费收入 stbcbcf_jsqsr :水土保持补偿费收入-建设期收入 stbcbcf_kcqsr :水土保持补偿费收入-开采期收入 stbcbcf_qtsr :水土保持补偿费收入-其他收入 |
| 18 | fsbbno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |
| 19 | fnsrtype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产税和城镇土地税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） ccxws :财产行为税 szys_a :水资源税纳税申报表A szys_b :水资源税纳税申报表B tcrt :资源税 tvpt :车辆购置税 tcvvt :车船税 tcept :环保税 yys :烟叶税 zzsybnsr_zjg :汇总申报（一般纳税人总机构） zzsybnsr_fzjg :汇总申报（一般纳税人分支机构） zzsyjskb :增值税预缴税款表 zzsybnsr_yz_zjg :一般企业汇总申报预征方式总机构 zzsybnsr_yz_fzjg :一般企业汇总申报预征方式分支机构 qtsf_tysbb :通用申报表（税及附征税费） qtsf_fsstysbb :非税收入通用申报表 whsyjsf :文化事业建设费 zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 dkdj :代扣代缴 totf_cjrjybzj :残疾人就业保障金 kjqysds :扣缴企业所得税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_pay_hzsp_head |  | fentryid |
| 2 | idx_t_bdtaxr_pay_hzsp_hea |  | fid |

---

## 税金缴纳汇总审批单-主表 t_bdtaxr_pay_rec_hzsp

- **表名称：** 税金缴纳汇总审批单-主表
- **表名：** t_bdtaxr_pay_rec_hzsp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fhzamount | 应缴金额合计 | numeric | 23 | 10 | √ | 0 | 应缴金额合计 |
| 5 | fhzsprule | 汇总审批规则 | int8 | 64 |  | √ | 0 | [汇总审批规则 tctb_hzsp_rule](../tctb_files/tctb_hzsp_rule.md) |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fhzspruletype | 汇总审批规则类型 | int8 | 64 |  | √ | 0 | [汇总审批规则类型 tctb_hzsp_rule_type](../tctb_files/tctb_hzsp_rule_type.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fhzspbilltype | 汇总审批单据类型 | int8 | 64 |  | √ | 0 | [汇总审批单据类型 tctb_hzsp_bill_type](../tctb_files/tctb_hzsp_bill_type.md) |
| 16 | fbillno | 汇总审批单编码 | varchar | 30 |  | √ | ' ' | 汇总审批单编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bdtaxr_pay_rec_hzsp |  | fbillno |
| 2 | pk_bdtaxr_pay_rec_hzsp |  | fid |

---

## 子表-子表 t_bdtaxr_pay_hzsp_item

- **表名称：** 子表-子表
- **表名：** t_bdtaxr_pay_hzsp_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprojectname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 2 | fyjjemx | 应缴金额 | numeric | 23 | 10 | √ | 0 | 应缴金额 |
| 3 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fprojectnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 5 | fzszm | 征收子目 | varchar | 50 |  | √ | ' ' | 征收子目 |
| 6 | ftaxitem | 税目 | varchar | 50 |  | √ | ' ' | 税目,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fcs :房产税 fjsf :附加税费 cztdsys :城镇土地使用税 hbs :环境保护税 xfs :消费税 zys :资源税 szys :水资源税 tvpt :车辆购置税 ccs :车船税 yys :烟叶税 dfjyfj :地方教育附加 jyffj :教育费附加 cswhjss :城市维护建设税 szys_a :资源税 ghjf :工会经费 sljsjj :地方水利建设基金 whsyjsf :文化事业建设费 ljclf :城镇垃圾处理费 ghcbj :工会筹备金 dwfhf :堤围防护费 totf_cjrjybzj :残疾人就业保障金 dkdj :代扣代缴 kjqysds :扣缴企业所得税 stbcbcf :水土保持补偿费收入 stbcbcf_jsqsr :水土保持补偿费收入-建设期收入 stbcbcf_kcqsr :水土保持补偿费收入-开采期收入 stbcbcf_qtsr :水土保持补偿费收入-其他收入 |
| 7 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 8 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fsubbillid | 单据子表ID | varchar | 50 |  | √ | ' ' | 单据子表ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_pay_hzsp_item |  | fdetailid |
| 2 | idx_t_bdtaxr_pay_hzsp_ite |  | fentryid |
