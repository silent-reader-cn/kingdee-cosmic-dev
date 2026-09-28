# 税局版申报表-tsate_declare_history

## 税局版申报表-主表 t_bdtaxr_taxbureau_sbb

- **表名称：** 税局版申报表-主表
- **表名：** t_bdtaxr_taxbureau_sbb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 集团名册 | int8 | 64 |  | √ | 0 | 集团名册 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 7 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcomparestatus | 差异比对结果 | varchar | 50 |  | √ | ' ' | 差异比对结果,枚举: undo :未比对 comparing :比对中 diff :有差异 same :无差异 nodata :无比对数据 fail :比对失败 noneed :无需比对 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fapanage | 属地管理 | varchar | 50 |  | √ | ' ' | 属地管理 |
| 12 | ftemplateid | 申报表模板 | varchar | 50 |  | √ | ' ' | 申报表模板 |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fserialno | 申报数据流水号 | varchar | 50 |  | √ | ' ' | 申报数据流水号 |
| 15 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 halfyear :半年申报 year :按年申报 false :—— |
| 16 | fqjje | 欠缴金额 | numeric | 23 | 10 | √ | 0 | 欠缴金额 |
| 17 | foperatorno | 经办人身份证号 | varchar | 50 |  | √ | ' ' | 经办人身份证号 |
| 18 | fconvertstatus | 数据覆盖状态 | varchar | 50 |  | √ | ' ' | 数据覆盖状态,枚举: undo :未覆盖 converting :覆盖中 converted :覆盖成功 fail :覆盖失败 noneed :无需覆盖 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 21 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 22 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fzcdz | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 24 | ftcrettype | 房产申报表类型 | varchar | 50 |  | √ | ' ' | 房产申报表类型,枚举: fcscztdsys :房产和城镇土地使用税 |
| 25 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 26 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 27 | fdeclaredata_tag | 申报表数据_详情 | text | 0 |  |  | null | 申报表数据_详情 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fnsrtype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） ccxws :财产行为税 zdsybs_yd :重点税源表（月度） zdsybs_jd :重点税源表（季度） FR0002 :财务报表（一般企业_已执行） FR0003 :财务报表（小企业会计准则） totf_cjrjybzj :残疾人就业保障金缴费申报表 |
| 30 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 : |
| 31 | ffddbrxm | 法定代表人姓名 | varchar | 150 |  | √ | ' ' | 法定代表人姓名 |
| 32 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 33 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 34 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 declaring :● 申报中 declared :● 申报成功 undeclare :● 未编制 declarefailed :● 申报失败 |
| 36 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 paying :● 缴款中 paid :● 全部缴款 payfailed :● 缴款失败 nopay :● 无需缴款 partpaid :● 部分缴款 |
| 37 | fsblx | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: 1 :按期申报 2 :按次申报 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fsshymc | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 40 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 41 | fdeclaredatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: 0 :初始化数据 1 :已申报数据 |
| 42 | fkhyh | 开户银行 | varchar | 120 |  | √ | ' ' | 开户银行 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 45 | fdeclaredate | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 46 | foperator | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 49 | fmaindataid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 50 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 51 | fdeferpayapply | 申请缓缴 | bpchar | 1 |  | √ | '0' | 申请缓缴 |
| 52 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 53 | fsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 54 | friskstatus | 风险异常状态 | varchar | 50 |  | √ | ' ' | 风险异常状态 |
| 55 | fbusinessno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 56 | fdeclaredata | 申报表数据 | varchar | 255 |  | √ | ' ' | 申报表数据 |
| 57 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bdtaxr_taxbureau_sbb |  | forgid,fnsrtype,fskssqq,fskssqz |
| 2 | pk_bdtaxr_taxbureau_sbb |  | fid |
