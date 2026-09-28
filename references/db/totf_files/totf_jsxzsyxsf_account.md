# 城镇垃圾处理费台账-totf_jsxzsyxsf_account

## 城镇垃圾处理费台账-主表 t_totf_jsxzsyxsf_account

- **表名称：** 城镇垃圾处理费台账-主表
- **表名：** t_totf_jsxzsyxsf_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzsxm | 征收项目 | varchar | 50 |  | √ | ' ' | 征收项目 |
| 3 | ftaxrate | 征收比例 | numeric | 23 | 10 | √ | 0 | 征收比例 |
| 4 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 7 | fsourcedata | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: hand :手工新增 import :数据导入 autofetch :自动取数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 10 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 11 | ftaxdeductiontype | ftaxdeductiontype | varchar | 50 |  | √ | ' ' |  |
| 12 | fjbrysfzjlx | 办理人员身份证件类型 | varchar | 50 |  | √ | ' ' | 办理人员身份证件类型,枚举: 1 :居民身份证 2 :军官证 3 :武警警官证 4 :士兵证 5 :港澳居民来往内地通行证 6 :中华人民共和国往来港澳通行证 7 :中国护照 8 :组织机构代码证 9 :营业执照 10 :税务登记证 11 :其他单位证件 12 :军队离退休干部证 13 :残疾人证 14 :残疾军人证（1-8级） 15 :外国护照 16 :台湾居民来往大陆通行证 17 :大陆居民往来台湾通行证 18 :外国人居留证 19 :外交官证 20 :使（领事）馆证 21 :海员证 22 :香港永久性居民身份证 23 :台湾身份证 24 :澳门特别行政区永久性居民身份证 25 :外国人身份证件 26 :就业失业登记证 27 :退休证 28 :离休证 29 :城镇退役士兵自谋职业证 30 :随军家属身份证明 31 :中国人民解放军军官转业证书 32 :中国人民解放军义务兵退出现役证 33 :中国人民解放军士官退出现役证 34 :外国人永久居留身份证（外国人永久居留证） 35 :就业创业证 36 :香港特别行政区护照 37 :澳门特别行政区护照 38 :中华人民共和国港澳居民居住证 39 :中华人民共和国台湾居民居住证 40 :《中华人民共和国外国人工作许可证》（A类） 41 :《中华人民共和国外国人工作许可证》（B类） 42 :《中华人民共和国外国人工作许可证》（C类） 43 :医学出生证明 44 :其他个人证件 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftaxdeductionid | 减免性质代码和名称 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 15 | fjbrphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | ftaxableitem | 应缴费基数 | numeric | 23 | 10 | √ | 0 | 应缴费基数 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | foperator | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fzsxmname | 征收品目名称 | varchar | 50 |  | √ | ' ' | 征收品目名称,枚举: czljclf :城镇垃圾处理费 |
| 24 | foperatorno | 办理人员身份证件号码 | varchar | 50 |  | √ | ' ' | 办理人员身份证件号码 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | ftaxdeductionname | ftaxdeductionname | varchar | 50 |  | √ | ' ' |  |
| 27 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 28 | fquickdeduction | 扣除数 | numeric | 23 | 10 | √ | 0 | 扣除数 |
| 29 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 count :次 |
| 30 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 31 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 32 | fdeductitem | 应缴税费减除额 | numeric | 23 | 10 | √ | 0 | 应缴税费减除额 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fbqyjse | 本期已缴税（费）额 | numeric | 23 | 10 | √ | 0 | 本期已缴税（费）额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_jsxzsyxsf_account |  | fid |
| 2 | idx_jsxzsyxsf_account_group |  | forgid,fzspm,fstartdate,fenddate |
