# 附加税费分配列表-tcvat_fjsffp_list

## 附加税费分配列表-主表 t_tpo_declare_main_tsc

- **表名称：** 附加税费分配列表-主表
- **表名：** t_tpo_declare_main_tsc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fversiontype | fversiontype | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 7 | ftaxsourcetype | ftaxsourcetype | varchar | 50 |  | √ | ' ' |  |
| 8 | ftemplatetype | 模板类型 | varchar | 36 |  | √ | ' ' | 模板类型 tpo_template_type |
| 9 | fbqybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fismodified | fismodified | varchar | 50 |  | √ | ' ' |  |
| 12 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 13 | ftaxsourceid | ftaxsourceid | int8 | 64 |  | √ | 0 |  |
| 14 | fsourcebillno | 来源单据编码 | varchar | 50 |  | √ | ' ' | 来源单据编码 |
| 15 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 16 | fbqmssrhj | 本期免税收入合计 | numeric | 23 | 10 | √ | 0 | 本期免税收入合计 |
| 17 | fapanage | fapanage | varchar | 50 |  | √ | ' ' |  |
| 18 | ftemplateid | 申报表模板 | int8 | 64 |  | √ | 0 | 模板配置 tpo_template |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fserialno | 申报数据流水号 | varchar | 50 |  | √ | ' ' | 申报数据流水号 |
| 21 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: |
| 22 | fqjje | fqjje | numeric | 23 | 10 | √ | 0 |  |
| 23 | foperatorno | foperatorno | varchar | 50 |  | √ | ' ' |  |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fskssqq | 所属期起 | timestamp | 0 |  |  | null | 所属期起 |
| 26 | fitemofincome | fitemofincome | int8 | 64 |  | √ | 0 |  |
| 27 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 28 | fnsrmc | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 29 | fdeclarer | 申报人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fljsre | fljsre | numeric | 23 | 10 | √ | 0 |  |
| 31 | ftaxrefundstatus | ftaxrefundstatus | varchar | 50 |  | √ | ' ' |  |
| 32 | fzcdz | fzcdz | varchar | 300 |  | √ | ' ' |  |
| 33 | ftcrettype | ftcrettype | varchar | 50 |  | √ | ' ' |  |
| 34 | fyhzh | fyhzh | varchar | 50 |  | √ | ' ' |  |
| 35 | fsbbid | fsbbid | int8 | 64 |  | √ | 0 |  |
| 36 | fdeclareversiontype | fdeclareversiontype | int8 | 64 |  | √ | 0 |  |
| 37 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 3 :税局下载 |
| 40 | ffddbrxm | ffddbrxm | varchar | 50 |  | √ | ' ' |  |
| 41 | fscjydz | fscjydz | varchar | 300 |  | √ | ' ' |  |
| 42 | fphonenum | fphonenum | varchar | 50 |  | √ | ' ' |  |
| 43 | fpayer | 缴款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fhistoryversion | 历史版本 | varchar | 50 |  | √ | ' ' | 历史版本,枚举: 1 :历史版本 |
| 45 | farchivetime | farchivetime | timestamp | 0 |  |  | null |  |
| 46 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: |
| 47 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 paying :● 缴款中 paid :● 全部缴款 payfailed :● 缴款失败 nopay :● 无需缴款 partpaid :● 部分缴款 |
| 48 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 49 | fsblx | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: 1 :按期申报 2 :按次申报 |
| 50 | fjbrysfzjlx | fjbrysfzjlx | varchar | 50 |  | √ | ' ' |  |
| 51 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fsshymc | fsshymc | varchar | 50 |  | √ | ' ' |  |
| 53 | fsszt | fsszt | varchar | 50 |  | √ | ' ' |  |
| 54 | fzerodeclare | fzerodeclare | bpchar | 1 |  | √ | '0' |  |
| 55 | fskssqz | 所属期止 | timestamp | 0 |  |  | null | 所属期止 |
| 56 | fynse | fynse | numeric | 23 | 10 | √ | 0 |  |
| 57 | fmultitemplateid | fmultitemplateid | int8 | 64 |  | √ | 0 |  |
| 58 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 59 | fkhyh | fkhyh | varchar | 120 |  | √ | ' ' |  |
| 60 | fjbrphone | fjbrphone | varchar | 200 |  | √ | ' ' |  |
| 61 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 62 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 64 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 65 | fdeclaredate | fdeclaredate | timestamp | 0 |  |  | null |  |
| 66 | fdeclaredataversion | fdeclaredataversion | varchar | 50 |  | √ | ' ' |  |
| 67 | foperator | foperator | varchar | 50 |  | √ | ' ' |  |
| 68 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 69 | fsbrs | fsbrs | int4 | 32 |  | √ | 0 |  |
| 70 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 71 | fmaindataid | fmaindataid | int8 | 64 |  | √ | 0 |  |
| 72 | fdeferpayapply | fdeferpayapply | bpchar | 1 |  | √ | '0' |  |
| 73 | fpaytype | 缴款方式 | varchar | 50 |  | √ | ' ' | 缴款方式,枚举: 0 :手工缴款 1 :直连缴款 |
| 74 | fsjje | fsjje | numeric | 23 | 10 | √ | 0 |  |
| 75 | farchivestatus | farchivestatus | varchar | 50 |  | √ | 'unfiled' |  |
| 76 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 77 | fbqsrehj | fbqsrehj | numeric | 23 | 10 | √ | 0 |  |
| 78 | flogsummary | 日志摘要 | varchar | 255 |  | √ | ' ' | 日志摘要 |
| 79 | friskstatus | friskstatus | varchar | 50 |  | √ | ' ' |  |
| 80 | fbusinessno | fbusinessno | varchar | 50 |  | √ | ' ' |  |
| 81 | fjmse | fjmse | numeric | 23 | 10 | √ | 0 |  |
| 82 | friskcontent | friskcontent | varchar | 50 |  | √ | ' ' |  |
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
