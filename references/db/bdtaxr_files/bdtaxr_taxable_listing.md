# 应报清单-bdtaxr_taxable_listing

## 应报清单-主表 t_bdtaxr_taxable_listing

- **表名称：** 应报清单-主表
- **表名：** t_bdtaxr_taxable_listing

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxauthority | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 3 | ftemplateid | 模板id | varchar | 50 |  | √ | ' ' | 模板id |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdraftno | 底稿编码 | varchar | 50 |  | √ | ' ' | 底稿编码 |
| 6 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 9 | fpaystatus | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: unpaid :● 未缴款 submitted :● 已提交待缴款 paying :● 缴款中 paid :● 全部缴款 payfailed :● 缴款失败 nopay :● 无需缴款 partpaid :● 部分缴款 yypaid :● 预约成功 yypayfailed :● 预约失败 |
| 10 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :● 未申报 submitted :● 已提交待申报 declaring :● 申报中 declared :● 申报成功 declarefailed :● 申报失败 importing :● 已申报未导入 nodata :● 未编制 |
| 11 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 12 | fdraftstatus | 底稿状态 | varchar | 50 |  | √ | ' ' | 底稿状态,枚举: A :暂存 B :已提交 C :已审核 noneed :无需编制 nodata :未编制 |
| 13 | fdeadline | 征期截止日 | timestamp | 0 |  |  | null | 征期截止日 |
| 14 | fmonth | 生成年月 | timestamp | 0 |  |  | null | 生成年月 |
| 15 | fsbbcategory | 申报表类别 | varchar | 50 |  | √ | ' ' | 申报表类别,枚举: qysdsjb :企业所得税预缴申报表 qysdsnb :企业所得税年报申报表 zzs :增值税申报表 ccxws :财产和行为税申报表 whsyjsf :文化事业建设费 qtsf_tysbb :通用申报表（税及附征税费） qtsf_fsstysbb :非税收入通用申报表 cwbbnd :年度财务报表 cwbbfnd :非年度财务报表 |
| 16 | fdgcategory | 底稿类别 | varchar | 50 |  | √ | ' ' | 底稿类别,枚举: qysdsjb :企业所得税预缴底稿 qysdsnb :企业所得税年报底稿 zzs :增值税底稿 |
| 17 | fnsrtype | 模板类型 | varchar | 50 |  | √ | ' ' | 模板类型 tpo_template_type |
| 18 | fsbbno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bdtaxr_taxable_listing_1 |  | forgid,fmonth |
| 2 | pk_bdtaxr_taxable_listing |  | fid |
