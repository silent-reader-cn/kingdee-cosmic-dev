# 其他收入台账-totf_otherincome_account

## 其他收入台账-主表 t_totf_otherincome

- **表名称：** 其他收入台账-主表
- **表名：** t_totf_otherincome

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzsxm | 征收项目 | varchar | 50 |  | √ | ' ' | 征收项目 |
| 3 | ftaxrate | 应税所得率 | numeric | 23 | 10 | √ | 0 | 应税所得率 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdeductionamount | 减免税（费）额 | numeric | 23 | 10 | √ | 0 | 减免税（费）额 |
| 8 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 9 | fjbrysfzjlx | 办理人员身份证件类型 | varchar | 50 |  | √ | ' ' | 办理人员身份证件类型,枚举: 1 :居民身份证 2 :军官证 3 :武警警官证 4 :士兵证 5 :港澳居民来往内地通行证 6 :中华人民共和国往来港澳通行证 7 :中国护照 8 :组织机构代码证 9 :营业执照 10 :税务登记证 11 :其他单位证件 12 :军队离退休干部证 13 :残疾人证 14 :残疾军人证（1-8级） 15 :外国护照 16 :台湾居民来往大陆通行证 17 :大陆居民往来台湾通行证 18 :外国人居留证 19 :外交官证 20 :使（领事）馆证 21 :海员证 22 :香港永久性居民身份证 23 :台湾身份证 24 :澳门特别行政区永久性居民身份证 25 :外国人身份证件 26 :就业失业登记证 27 :退休证 28 :离休证 29 :城镇退役士兵自谋职业证 30 :随军家属身份证明 31 :中国人民解放军军官转业证书 32 :中国人民解放军义务兵退出现役证 33 :中国人民解放军士官退出现役证 34 :外国人永久居留身份证（外国人永久居留证） 35 :就业创业证 36 :香港特别行政区护照 37 :澳门特别行政区护照 38 :中华人民共和国港澳居民居住证 39 :中华人民共和国台湾居民居住证 40 :《中华人民共和国外国人工作许可证》（A类） 41 :《中华人民共和国外国人工作许可证》（B类） 42 :《中华人民共和国外国人工作许可证》（C类） 43 :医学出生证明 44 :其他个人证件 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fzzsdeductiontype | 增值税小规模纳税减免性质 | varchar | 50 |  | √ | ' ' | 增值税小规模纳税减免性质 |
| 12 | ftaxdeductionid | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 13 | fjbrphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 14 | fbillno | 申报表编号 | varchar | 30 |  | √ | ' ' | 申报表编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ftaxableitem | 应税项 | numeric | 23 | 10 | √ | 0 | 应税项 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | foperator | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fzzsdeductrate | 增值税小规模纳税人享受减征比例（%） | numeric | 23 | 10 | √ | 0 | 增值税小规模纳税人享受减征比例（%） |
| 21 | foperatorno | 办理人员身份证件号码 | varchar | 50 |  | √ | ' ' | 办理人员身份证件号码 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fzspmname | 征收品目名称 | varchar | 50 |  | √ | ' ' | 征收品目名称,枚举: ghjf :工会经费 ghcbj :工会筹备金 |
| 24 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 25 | fquickdeduction | 速算扣除数 | numeric | 23 | 10 | √ | 0 | 速算扣除数 |
| 26 | fpayperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 count :次 |
| 27 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 28 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 29 | fdeductitem | 减除项 | numeric | 23 | 10 | √ | 0 | 减除项 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fbqyjse | 本期已缴税（费）额 | numeric | 23 | 10 | √ | 0 | 本期已缴税（费）额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_totf_otherincome_group |  | forgid,fzspm,fstartdate,fenddate |
| 2 | pk_totf_otherincome |  | fid |
