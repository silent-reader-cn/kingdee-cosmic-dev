# 年报申报表查询-tccit_year_declare_list

## 年报申报表查询-主表 t_tpo_declare_main_tsc

- **表名称：** 年报申报表查询-主表
- **表名：** t_tpo_declare_main_tsc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 集团名册 | int8 | 64 |  | √ | 0 | 集团名册 |
| 3 | fversiontype | 版本类型 | varchar | 50 |  | √ | ' ' | 版本类型,枚举: zcsb :正常申报 gzsb :更正申报 zxsb :注销申报 sjxz :税局下载 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 7 | ftaxsourcetype | 税源类型 | varchar | 50 |  | √ | ' ' | 税源类型,枚举: tdm_tdzzs_clearing_unit :土地增值税项目 |
| 8 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 9 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fismodified | 是否修改 | varchar | 50 |  | √ | ' ' | 是否修改,枚举: 1 :是 0 :否 |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | ftaxsourceid | 税源ID | int8 | 64 |  | √ | 0 | 土地增值税项目 tdm_tdzzs_clearing_unit |
| 14 | fsourcebillno | 来源单据编码 | varchar | 50 |  | √ | ' ' | 来源单据编码 |
| 15 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 16 | fbqmssrhj | fbqmssrhj | numeric | 23 | 10 | √ | 0 |  |
| 17 | fapanage | 属地管理 | varchar | 50 |  | √ | ' ' | 属地管理 |
| 18 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fserialno | 申报数据流水号 | varchar | 50 |  | √ | ' ' | 申报数据流水号 |
| 21 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: |
| 22 | fqjje | 欠缴金额 | numeric | 23 | 10 | √ | 0 | 欠缴金额 |
| 23 | foperatorno | 经办人身份证号 | varchar | 50 |  | √ | ' ' | 经办人身份证号 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 26 | fitemofincome | fitemofincome | int8 | 64 |  | √ | 0 |  |
| 27 | fdraftpurpose | fdraftpurpose | varchar | 50 |  | √ | ' ' |  |
| 28 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 29 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fljsre | fljsre | numeric | 23 | 10 | √ | 0 |  |
| 31 | ftaxrefundstatus | 留抵退税 | varchar | 50 |  | √ | ' ' | 留抵退税,枚举: -- :-- yc :异常 wxsq :无需申请 wsq :未申请 ysq :已申请 zyts :准予退税 yts :已退税 |
| 32 | fzcdz | 注册地址 | varchar | 300 |  | √ | ' ' | 注册地址 |
| 33 | ftcrettype | 房产申报表类型 | varchar | 50 |  | √ | ' ' | 房产申报表类型,枚举: fcscztdsys :房产和城镇土地使用税 |
| 34 | fyhzh | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 35 | fsbbid | 关联申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 36 | fdeclareversiontype | 版本类型 | int8 | 64 |  | √ | 0 | 版本类型 tpo_declare_versiontype |
| 37 | fregistertype | 注册登记类型 | varchar | 50 |  | √ | ' ' | 注册登记类型 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据导入 3 :税局下载 |
| 40 | ffddbrxm | 法定代表人姓名 | varchar | 50 |  | √ | ' ' | 法定代表人姓名 |
| 41 | fscjydz | 生产经营地址 | varchar | 300 |  | √ | ' ' | 生产经营地址 |
| 42 | fphonenum | 电话号码 | varchar | 50 |  | √ | ' ' | 电话号码 |
| 43 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fhistoryversion | fhistoryversion | varchar | 50 |  | √ | ' ' |  |
| 45 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 46 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 submitted :● 已提交待申报 declaring :● 申报中 importing :● 已申报未导入 declared :● 申报成功 declarefailed :● 申报失败 |
| 47 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 paying :● 缴款中 paid :● 全部缴款 payfailed :● 缴款失败 nopay :● 无需缴款 partpaid :● 部分缴款 yypaid :● 预约成功 submitted :● 已提交待缴款 yypayfailed :● 预约失败 |
| 48 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 49 | fsblx | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: 1 :按期申报 2 :按次申报 |
| 50 | fjbrysfzjlx | 经办人员身份证件类型 | varchar | 50 |  | √ | ' ' | 经办人员身份证件类型,枚举: 1 :居民身份证 2 :军官证 3 :武警警官证 4 :士兵证 5 :港澳居民来往内地通行证 6 :中华人民共和国往来港澳通行证 7 :中国护照 8 :组织机构代码证 9 :营业执照 10 :税务登记证 11 :其他单位证件 12 :军队离退休干部证 13 :残疾人证 14 :残疾军人证（1-8级） 15 :外国护照 16 :台湾居民来往大陆通行证 17 :大陆居民往来台湾通行证 18 :外国人居留证 19 :外交官证 20 :使（领事）馆证 21 :海员证 22 :香港永久性居民身份证 23 :台湾身份证 24 :澳门特别行政区永久性居民身份证 25 :外国人身份证件 26 :就业失业登记证 27 :退休证 28 :离休证 29 :城镇退役士兵自谋职业证 30 :随军家属身份证明 31 :中国人民解放军军官转业证书 32 :中国人民解放军义务兵退出现役证 33 :中国人民解放军士官退出现役证 34 :外国人永久居留身份证（外国人永久居留证） 35 :就业创业证 36 :香港特别行政区护照 37 :澳门特别行政区护照 38 :中华人民共和国港澳居民居住证 39 :中华人民共和国台湾居民居住证 40 :《中华人民共和国外国人工作许可证》（A类） 41 :《中华人民共和国外国人工作许可证》（B类） 42 :《中华人民共和国外国人工作许可证》（C类） 43 :医学出生证明 44 :其他个人证件 |
| 51 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fsshymc | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业 |
| 53 | fsszt | 试算状态 | varchar | 50 |  | √ | ' ' | 试算状态,枚举: 试算中 :1 试算成功 :2 试算失败 :3 |
| 54 | fzerodeclare | 是否零申报 | bpchar | 1 |  | √ | '0' | 是否零申报 |
| 55 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 56 | fynse | fynse | numeric | 23 | 10 | √ | 0 |  |
| 57 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 58 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 59 | fkhyh | 开户银行 | varchar | 120 |  | √ | ' ' | 开户银行 |
| 60 | fjbrphone | 联系电话 | varchar | 200 |  | √ | ' ' | 联系电话 |
| 61 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 62 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 64 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 65 | fdeclaredate | 申报编制日期 | timestamp | 0 |  |  | null | 申报编制日期 |
| 66 | fdeclaredataversion | fdeclaredataversion | varchar | 50 |  | √ | ' ' |  |
| 67 | foperator | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 68 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 69 | fsbrs | fsbrs | int4 | 32 |  | √ | 0 |  |
| 70 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 71 | fmaindataid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 72 | fdeferpayapply | 申请缓缴 | bpchar | 1 |  | √ | '0' | 申请缓缴 |
| 73 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 74 | fsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 75 | farchivestatus | 归档状态 | varchar | 50 |  | √ | 'unfiled' | 归档状态,枚举: unfiled :未归档 filed :已归档 |
| 76 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 77 | fbqsrehj | fbqsrehj | numeric | 23 | 10 | √ | 0 |  |
| 78 | flogsummary | flogsummary | varchar | 255 |  | √ | ' ' |  |
| 79 | friskstatus | 风险异常状态 | varchar | 50 |  | √ | ' ' | 风险异常状态 |
| 80 | fbusinessno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 81 | fjmse | fjmse | numeric | 23 | 10 | √ | 0 |  |
| 82 | friskcontent | 风险提示 | varchar | 50 |  | √ | ' ' | 风险提示,枚举: normal :正常 abnormal :异常 |
| 83 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 84 | fdeclaremethod | 申报方式 | varchar | 50 |  | √ | ' ' | 申报方式,枚举: 0 :手工申报 1 :直连申报 |
| 85 | fpaydate | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_declare_main_tsc_fbillno |  | fbillno |
| 2 | idx_declare_main_tsc_2 |  | fsourcebillid |
| 3 | pk_tpo_declare_main_tsc |  | fid |
