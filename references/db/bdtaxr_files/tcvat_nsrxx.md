# 纳税申报表-tcvat_nsrxx

## 附件字段-附件表 t_tctb_declare_main_att

- **表名称：** 附件字段-附件表
- **表名：** t_tctb_declare_main_att

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_main_att |  | fpkid |
| 2 | idx_t_tctb_declare_main_att |  | fid |

---

## 单据体-子表 t_tctb_declare_entry

- **表名称：** 单据体-子表
- **表名：** t_tctb_declare_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fszysno | fszysno | varchar | 50 |  | √ | ' ' |  |
| 3 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 4 | fyjsjje | fyjsjje | numeric | 23 | 10 | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdeferpayapply | 申请缓缴 | bpchar | 1 |  | √ | '0' | 申请缓缴 |
| 7 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 8 | fewblname | fewblname | varchar | 50 |  | √ | ' ' |  |
| 9 | fjmse | fjmse | numeric | 23 | 10 | √ | 0 |  |
| 10 | fynse | fynse | numeric | 23 | 10 | √ | 0 |  |
| 11 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ftaxtype | 税种 | varchar | 50 |  | √ | ' ' | 税种,枚举: 1 :增值税 2 :附加税费 |
| 14 | fbqdybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_entry |  | fentryid |
| 2 | idx_tctb_declare_entry_fk |  | fid |

---

## 纳税申报表-主表 t_tctb_declare_main

- **表名称：** 纳税申报表-主表
- **表名：** t_tctb_declare_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 集团名册 | int8 | 64 |  | √ | 0 | 集团名册 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fversiontype | 版本类型 | varchar | 50 |  | √ | ' ' | 版本类型,枚举: zcsb :正常申报 gzsb :更正申报 sjxz :税局下载 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 7 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0.0000000000 | 应税收入 |
| 8 | ftaxsourcetype | 税源类型 | varchar | 50 |  | √ | ' ' | 税源类型,枚举: tdm_tdzzs_clearing_unit :土地增值税项目 |
| 9 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期应补（退）税额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fattachmentcount | fattachmentcount | int8 | 64 |  | √ | 0 |  |
| 12 | fismodified | 是否修改 | varchar | 50 |  | √ | '0' | 是否修改,枚举: 1 :是 0 :否 |
| 13 | ftaxsourceid | 税源ID | int8 | 64 |  | √ | 0 | 土地增值税项目 tdm_tdzzs_clearing_unit |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fapanage | 属地管理 | varchar | 50 |  | √ | ' ' | 属地管理 |
| 16 | ftemplateid | 申报表模板 | varchar | 50 |  | √ | ' ' | 申报表模板 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fserialno | 申报数据流水号 | varchar | 50 |  | √ | ' ' | 申报数据流水号 |
| 19 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: month :按月申报 season :按季申报 halfyear :半年申报 year :按年申报 false :—— |
| 20 | fqjje | 欠缴金额 | numeric | 23 | 10 | √ | 0 | 欠缴金额 |
| 21 | foperatorno | 经办人身份证号 | varchar | 50 |  | √ | ' ' | 经办人身份证号 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 24 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 25 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 27 | fzcdz | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 28 | ftcrettype | 房产申报表类型 | varchar | 50 |  | √ | ' ' | 房产申报表类型,枚举: fcscztdsys :房产和城镇土地使用税 |
| 29 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 30 | fsbbid | 关联申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 31 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fnsrtype | 申报表类型 | varchar | 36 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构） ccxws :财产行为税 dkdj :代扣代缴 kjqysds :扣缴企业所得税 szys_a :水资源税A szys_b :水资源税B FR0002 :一般企业会计准则（已执行） FR0001 :一般企业会计准则（未执行） FR0003 :小企业会计准则 FR0004 :企业会计制度 FR0011 :金融企业会计准则 zdsybs_yd :重点税源报送（月度） zdsybs_jd :重点税源报送（季度） qhjtbs :千户集团报送 |
| 34 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 : |
| 35 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 36 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 37 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 38 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 40 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 declaring :● 申报中 declared :● 申报成功 undeclare :● 未编制 declarefailed :● 申报失败 |
| 41 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 paying :● 缴款中 paid :● 全部缴款 payfailed :● 缴款失败 nopay :● 无需缴款 partpaid :● 部分缴款 |
| 42 | fsblx | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: 1 :按期申报 2 :按次申报 |
| 43 | fjbrysfzjlx | 经办人员身份证件类型 | varchar | 50 |  | √ | ' ' | 经办人员身份证件类型,枚举: 1 :居民身份证 2 :军官证 3 :武警警官证 4 :士兵证 5 :港澳居民来往内地通行证 6 :中华人民共和国往来港澳通行证 7 :中国护照 8 :组织机构代码证 9 :营业执照 10 :税务登记证 11 :其他单位证件 12 :军队离退休干部证 13 :残疾人证 14 :残疾军人证（1-8级） 15 :外国护照 16 :台湾居民来往大陆通行证 17 :大陆居民往来台湾通行证 18 :外国人居留证 19 :外交官证 20 :使（领事）馆证 21 :海员证 22 :香港永久性居民身份证 23 :台湾身份证 24 :澳门特别行政区永久性居民身份证 25 :外国人身份证件 26 :就业失业登记证 27 :退休证 28 :离休证 29 :城镇退役士兵自谋职业证 30 :随军家属身份证明 31 :中国人民解放军军官转业证书 32 :中国人民解放军义务兵退出现役证 33 :中国人民解放军士官退出现役证 34 :外国人永久居留身份证（外国人永久居留证） 35 :就业创业证 36 :香港特别行政区护照 37 :澳门特别行政区护照 38 :中华人民共和国港澳居民居住证 39 :中华人民共和国台湾居民居住证 40 :《中华人民共和国外国人工作许可证》（A类） 41 :《中华人民共和国外国人工作许可证》（B类） 42 :《中华人民共和国外国人工作许可证》（C类） 43 :医学出生证明 44 :其他个人证件 |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fsshymc | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 46 | fzerodeclare | 是否零申报 | bpchar | 1 |  | √ | '0' | 是否零申报 |
| 47 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 48 | fkhyh | 开户银行 | varchar | 120 |  | √ | ' ' | 开户银行 |
| 49 | fjbrphone | 联系电话 | varchar | 200 |  | √ | ' ' | 联系电话 |
| 50 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 53 | fdeclaredate | 申报编制日期 | timestamp | 0 |  |  | null | 申报编制日期 |
| 54 | foperator | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fsbrq | 申报日期1 | timestamp | 0 |  |  | null | 申报日期1 |
| 57 | fdeclaretype | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 58 | fmaindataid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 59 | fdeferpayapply | 申请缓缴 | bpchar | 1 |  | √ | '0' | 申请缓缴 |
| 60 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 61 | fsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 62 | farchivestatus | 归档状态 | varchar | 50 |  | √ | 'unfiled' | 归档状态,枚举: unfiled :未归档 filed :已归档 |
| 63 | friskstatus | 风险异常状态 | varchar | 50 |  | √ | ' ' | 风险异常状态 |
| 64 | fbusinessno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 65 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
| 66 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_declare_main |  | fid |
| 2 | idx_tctb_declare_main |  | fskssqq,fskssqz,forgid,fnsrtype |
