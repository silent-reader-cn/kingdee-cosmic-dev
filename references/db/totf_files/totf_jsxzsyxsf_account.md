# 建设行政事业性收费收入台账-totf_jsxzsyxsf_account

## 建设行政事业性收费收入台账-主表 t_totf_jsxzsyxsf_account

- **表名称：** 建设行政事业性收费收入台账-主表
- **表名：** t_totf_jsxzsyxsf_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzsxm | 征收项目 | varchar | 50 |  | √ | ' ' | 征收项目 |
| 3 | ftaxrate | 征收比例 | numeric | 23 | 10 | √ | 0 | 征收比例 |
| 4 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 9 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 10 | ftaxdeductiontype | ftaxdeductiontype | varchar | 50 |  | √ | ' ' |  |
| 11 | fjbrysfzjlx | 办理人员身份证件类型 | varchar | 50 |  | √ | ' ' | 办理人员身份证件类型,枚举: 1 :居民身份证 2 :军官证 3 :武警警官证 4 :士兵证 5 :港澳居民来往内地通行证 6 :中华人民共和国往来港澳通行证 7 :中国护照 8 :组织机构代码证 9 :营业执照 10 :税务登记证 11 :其他单位证件 12 :军队离退休干部证 13 :残疾人证 14 :残疾军人证（1-8级） 15 :外国护照 16 :台湾居民来往大陆通行证 17 :大陆居民往来台湾通行证 18 :外国人居留证 19 :外交官证 20 :使（领事）馆证 21 :海员证 22 :香港永久性居民身份证 23 :台湾身份证 24 :澳门特别行政区永久性居民身份证 25 :外国人身份证件 26 :就业失业登记证 27 :退休证 28 :离休证 29 :城镇退役士兵自谋职业证 30 :随军家属身份证明 31 :中国人民解放军军官转业证书 32 :中国人民解放军义务兵退出现役证 33 :中国人民解放军士官退出现役证 34 :外国人永久居留身份证（外国人永久居留证） 35 :就业创业证 36 :香港特别行政区护照 37 :澳门特别行政区护照 38 :中华人民共和国港澳居民居住证 39 :中华人民共和国台湾居民居住证 40 :《中华人民共和国外国人工作许可证》（A类） 41 :《中华人民共和国外国人工作许可证》（B类） 42 :《中华人民共和国外国人工作许可证》（C类） 43 :医学出生证明 44 :其他个人证件 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ftaxdeductionid | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 14 | fjbrphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 15 | fbillno | 申报表编号 | varchar | 30 |  | √ | ' ' | 申报表编号 |
| 16 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ftaxableitem | 应缴费基数 | numeric | 23 | 10 | √ | 0 | 应缴费基数 |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | foperator | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fzsxmname | 征收品目名称 | varchar | 50 |  | √ | ' ' | 征收品目名称,枚举: czljclf :城镇垃圾处理费 |
| 23 | foperatorno | 办理人员身份证件号码 | varchar | 50 |  | √ | ' ' | 办理人员身份证件号码 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | ftaxdeductionname | ftaxdeductionname | varchar | 50 |  | √ | ' ' |  |
| 26 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 27 | fquickdeduction | 扣除数 | numeric | 23 | 10 | √ | 0 | 扣除数 |
| 28 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 count :次 |
| 29 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 30 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 31 | fdeductitem | 应缴税费减除额 | numeric | 23 | 10 | √ | 0 | 应缴税费减除额 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fbqyjse | 本期已缴税（费）额 | numeric | 23 | 10 | √ | 0 | 本期已缴税（费）额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_jsxzsyxsf_account |  | fid |
| 2 | idx_jsxzsyxsf_account_group |  | forgid,fzspm,fstartdate,fenddate |
